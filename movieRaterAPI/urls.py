from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # API
    path('api/', include('api.urls')),
    # AUTH
    path('auth/', obtain_auth_token),
]
