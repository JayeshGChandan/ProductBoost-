from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from producthunt import settings
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
