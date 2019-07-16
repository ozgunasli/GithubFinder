from django.shortcuts import render
from .forms import AramaForm
import requests

# Create your views here.
base_url="https://api.github.com/users/"

def index_view(request):

    if request.method == "POST":
        form = AramaForm(request.POST)

        githubname=form.cleaned_data.get("githubname")

        response=requests.get(base_url+githubname)
        user_info=response.json()
        profile = user_info
        return render(request, 'index.html',profile)

    else:

        return render(request,'index.html')