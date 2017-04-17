from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. This is the bash_to_cmd index.")

def bash_translation_results(request, cmd_id):
    return HttpResponse(reponse)

def cmd_translation_results(request, bash_id):
    return HttpResponse(reponse)
