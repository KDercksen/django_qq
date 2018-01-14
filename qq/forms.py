from django import forms


class QuestionForm(forms.Form):
    author = forms.CharField(label='Your name', max_length=50)
    question_title = forms.CharField(label='Question title', max_length=100)
    question_text = forms.CharField(label='Your question', widget=forms.Textarea)


class AnswerForm(forms.Form):
    author = forms.CharField(label='Your name', max_length=50)
    answer_text = forms.CharField(label='Your answer', widget=forms.Textarea)
