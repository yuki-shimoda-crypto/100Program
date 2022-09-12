from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f'質問：{question_id}')

def results(request, question_id):
    response = "投票結果:{}"
    return HttpResponse(response.format(question_id))

def vote(request, question_id):
    return HttpResponse(f'投票する質問：{question_id}')

# Create your views here.
