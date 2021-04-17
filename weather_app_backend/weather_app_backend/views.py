
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action

from weather_app_backend.serializers import UserSerializer
#  , GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]



"""
1-Django Projesi Başlatılmalıdır    +
2-Virtualenv kurulmalıdır   +
3-Bootsrap kütüphanesi projeye dahil edilmelidir 
4-https://www.worldweatheronline.com/developer/ sitesine 60 günlük ücretsiz üyelik yapılmalıdır. + 
5-Projede 3 ana ekran olmalıdır 
    1-Login ekranı, django user auth işlemlerini kullanarak login olunmalı, login olunmadan diğer  sayfalara geçiş yapılmamalıdıdr. 
    2- 3 Günlük hava durumu , Şehir bilgisi alınmalı ve bu şehirin önümüzdeki 3 günlük verisi  gösterilmelidir. 
        Temel bilgiler bir bakışta görünmeli detay butonuna basıldığında pop-up içerisinde  detay bilgiler gösterilmelidir. 
    3- 5 günlük hava durumu , şehir biligisi alınmalı ve bu şehrin önümüzdeki 5 günlük verisi  gösterilmelidir. 
        Temel bilgiler bir bakışta görünmeli detay butonuna basıldığında pop-up içerisinde  detay bilgiler gösterilmelidir.

todo:
    django rest jwt auth + 
    şehiri parametre olarak al önümüzdeki n günlük hava durumunu listele, detayla için popup yap, 3 ve 5 günlük şekilde
    
    
ek özellik olarak signup 
proje kurulumu user guide
istekleri backendden atıp isteklerin logu tutulabilir.
"""