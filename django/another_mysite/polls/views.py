from django.shortcuts import render, HttpResponse
from .models import Question

# Create your views here.
def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    question = Question.objects.all()
    choice = Choice.objects.all()
    # return HttpResponse(output)
    return render(request, 'polls/home.html', {'question': question, 'choice': choice})

def detail(request, question_id):
    return HttpResponse("You're looking at question {}s.".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}s.".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question {}s.".format(question_id))