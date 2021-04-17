from django.urls import include, path
from rest_framework import routers
#from weather_app_backend import views
from weather_app_backend.service.custom_token import TokenWithExtras
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from log.views import get_logs
from weather.views import get_weather
router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)  # users viewsetleri, signin(register) işlemi için kullanılabilir.
urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenWithExtras.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('logs/', get_logs, name='get_logs'),  # logları döner
    path('weather/', get_weather, name='get_weather'),  # hava durumu döner, city ve days parametreleri alır

]