from django.shortcuts import render
from apps.main.models import Main
# Create your views here.

def main(request):
    return render(request, 'index-kenburns.html', locals())
