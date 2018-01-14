from . import models
from .forms import AnswerForm, QuestionForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic


def index(request):
    return HttpResponse('placeholder')


def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['question_title']
            text = form.cleaned_data['question_text']
            models.Question(author=author, question_title=title,
                            question_text=text).save()
            return redirect('qq:questions')
    else:
        form = QuestionForm()
    return render(request, 'qq/ask_question.html', {'form': form})


def answer_question(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            answer = form.cleaned_data['answer_text']
            models.Answer(question=question, author=author,
                          answer_text=answer).save()
            return redirect('qq:question-thread', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'qq/answer_question.html', {'object': question, 'form': form})


def vote_answer(request, pk, answer_id, amount):
    a = get_object_or_404(models.Answer, pk=answer_id)
    a.votes += amount
    a.save()
    return redirect('qq:question-thread', pk=pk)


def downvote_answer(request, pk, answer_id):
    return vote_answer(request, pk, answer_id, -1)


def upvote_answer(request, pk, answer_id):
    return vote_answer(request, pk, answer_id, 1)


class QuestionListView(generic.ListView):
    model = models.Question


class QuestionDetailView(generic.DetailView):
    model = models.Question
