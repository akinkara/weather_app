
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from log.models import Log
from log.serializers import LogSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_logs(request):
    logs = Log.objects.all()
    serializer = LogSerializer(logs, many=True)
    return Response(serializer.data)
