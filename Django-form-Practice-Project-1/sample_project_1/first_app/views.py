from django.shortcuts import render
from first_app.forms import DjangoFormApiExample
from . import models


# Create your views here.
def home(request):
    return render(request, './first_app/home.html')


def DjangoFormApi(request):
    if request.method == 'POST':
        form = DjangoFormApiExample(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = DjangoFormApiExample()
    return render(request, './first_app/django_form_api.html', {'form' : form})


def DjangoModel(request):
    data = models.MyModel.objects.all()
    return render(request, './first_app/django_model.html', {'data' : data})