from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

def get_question(question_id):
    return Question.objects.get(id=question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    data = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', data)

def detail(request, question_id):
    question = get_question(question_id)
    data = {
        'question' : question
    }
    return render(request, 'polls/detail.html', data)

def results(request, question_id):
    question = get_question(question_id)
    data = {
        'question' : question
    }
    return render(request, 'polls/results.html', data)

def vote(request, question_id):
    question = get_question(question_id)
    data = {
        'question' : question,
        'error_message' : "You didn't select a choice",
    }
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', data)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))