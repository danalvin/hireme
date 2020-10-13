from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from .views import *

app_name = "accounts"

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
