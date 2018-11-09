from django.urls import path, include
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.test, name='test'),
    path('publish/', views.publish, name='publish'),
]
