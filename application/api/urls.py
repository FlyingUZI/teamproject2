from django.urls import path, include
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.test, name='test'),
    path('open/', views.open, name='open'),
    path('opened/', views.opened, name='opened'),
    path('publish/', views.publish, name='publish'),
]
