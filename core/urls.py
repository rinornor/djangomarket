from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("logout/", views.logout_user, name='logout'),
    path("signup/", views.signup, name='signup'),
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
