from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from polls.models import Choice, Question

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5] #-pub_date : decrease로 5개만 가지고와
    context = {'latest_question_list': latest_question_list} #받은 변수 저장
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # 내가 선택한 값만 가지고옴
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return a n HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))