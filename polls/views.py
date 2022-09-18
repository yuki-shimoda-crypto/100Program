from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SentenceForm

def index(request):
    context = {}
    
    context['sentence'] = SentenceForm()
    return render(request,'polls/index.html', context)

def result(request):
    form = SentenceForm(request.POST)
    if not form.is_valid():
        return HttpResponse('invalid', status=500)

    sentence = form.cleaned_data['sentence']
    
    context = {}
    context['sentence'] = sentence
    
    return render(request, 'polls/result.html', context)

# Create your views here.
