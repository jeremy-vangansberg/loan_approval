from django.shortcuts import render
from .form import ApiForm
from requests import Session
import requests
import json

# Create your views here.
def home(request):
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
    }

    # session = Session()
    # session.headers.update(headers)

    url = 'https://api2-afro.onrender.com/predict'

    form = ApiForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            data = json.dumps(form.cleaned_data)
            response = requests.post(url, data=data, headers=headers)
            info = response.text
            return render(request, 'main/home_page.html', context={
                'form': form,
                'info' : info
            })
    return render(request, 'main/home_page.html', context={
        'form': form
    })