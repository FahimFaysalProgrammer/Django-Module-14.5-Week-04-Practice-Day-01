from django.urls import path
from first_app.views import home, DjangoFormApi, DjangoModel

urlpatterns = [
    path('', home, name='homepage'),
    path('django_api/', DjangoFormApi, name = "django_api"),
    path('django_model/', DjangoModel, name = "django_model"),
]