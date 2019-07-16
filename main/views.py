from django.shortcuts import render
from .forms import AramaForm
import requests

# Create your views here.
base_url="https://api.github.com/users/"

def index_view(request):

    form=AramaForm()

    if request.method == "POST":

        form = AramaForm(request.POST)

        if form.is_valid():

            githubname = form.cleaned_data.get('githubname')

            response_user=requests.get(base_url+githubname)
            response_repo = requests.get(base_url + githubname + "/repos")

            user_info=response_user.json()
            repos=response_repo.json()

            profile = user_info

            '''if "message" in user_info:

                return render("index.html", error="Kullanıcı Bulunamadı...")
            else:

            '''

            return render(request, 'index.html',{'profile':profile,'repos':repos})

    else:

        return render(request,'index.html',{'form':form})