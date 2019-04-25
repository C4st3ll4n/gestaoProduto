
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from produtos import urls as produto_urls
from home import urls as home_urls

urlpatterns = [
    path('', include(home_urls), name='home'),
    path('produto/', include(produto_urls), name='produto'),
    path('admin/', admin.site.urls, name='admin'),
    path('login', auth_views.LoginView.as_view(), name='login')
]
