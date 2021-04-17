"""
Middleware to log all requests and responses.
"""
import logging
from django.utils.deprecation import MiddlewareMixin

import socket
import time
import json
from rest_framework.response import Response
from django.conf import settings
import traceback
from rest_framework import status
import rest_framework
request_logger = logging.getLogger('django.request')
from log.models import Log


class RequestLogMiddleware(MiddlewareMixin):
    """Request Logging Middleware."""

    def __init__(self, *args, **kwargs):
            """Constructor method."""
            super().__init__(*args, **kwargs)

    def process_request(self, request):
        """Set Request Start Time to measure time taken to service request."""
        if request.method in ['POST', 'PUT', 'PATCH'] and "token" not in str(request.get_full_path()):
            request.req_body = request.body
        if str(request.get_full_path()).startswith('/'):
            request.start_time = time.time()

    def extract_log_info(self, request, response=None, exception=None):
        """Extract appropriate log info from requests/responses/exceptions."""
        log_data = {
            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'run_time': time.time() - request.start_time,
        }
        if request.method in ['PUT', 'POST', 'PATCH']:
            try:
                log_data['request_body'] = json.loads(
                    str(request.req_body, 'utf-8'))
                if response and isinstance(response, rest_framework.response.Response):
                    if response['content-type'] == 'application/json':
                        response_body = response.content
                        log_data['response_body'] = response_body
            finally:
                return log_data


    def process_response(self, request, response):
        """Log data using logger."""
        if request.method != 'GET':
            if str(request.get_full_path()).startswith('/'):
                log_data = self.extract_log_info(request=request,
                                                 response=response)
                Log.objects.create(log_detail=str(log_data))
        return response

    def process_exception(self, request, exception):
        """Log Exceptions."""
        if not settings.DEBUG:
            if exception:
                message = "**{url}**\n\n{error}\n\n````{tb}````".format(url=request.build_absolute_uri(),
                                                                        error=repr(exception),
                                                                        tb=traceback.format_exc())
                Log.objects.create(log_detail=str(message))
            return Response({'error':'Error processing the request'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)