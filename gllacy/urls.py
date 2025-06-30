"""
URL configuration for gllacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home.views import home
from catalog.views import catalog
from forms.views import email_form, feedback_form, search_form
from users.views import register_form, personal_account, add_to_cart, delete_from_cart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_url'),
    path('register/', register_form, name='register_url'),
    path('catalog/', catalog, name='catalog_url'),
    path('personal_account/', personal_account, name='personal_account_url'),
    path('email_form/', email_form, name='email_form_url'),
    path('feedback_form/', feedback_form, name='feedback_form_url'),
    path('search_form/', search_form, name='search_url'),
    path('login/', auth_views.LoginView.as_view(), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_url'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart_url'),
    path('delete_from_cart/<int:product_id>/', delete_from_cart, name='delete_from_cart_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)
