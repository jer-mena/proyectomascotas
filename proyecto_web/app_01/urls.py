from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('', views.index, name='home'),
    path('', views.registro, name='home'),
    path('', views.contactanos, name='home'),
    path('', views.tienda, name='home'),
    path('', views.somos, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)