from . import views
from django.urls import path


app_name = 'qq'
urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask_question, name='ask'),
    path('questions/', views.QuestionListView.as_view(), name='questions'),
    path('questions/<int:pk>', views.QuestionDetailView.as_view(),
         name='question-thread'),
    path('questions/<int:pk>/<int:answer_id>/downvote', views.downvote_answer,
         name='downvote-answer'),
    path('questions/<int:pk>/<int:answer_id>/upvote', views.upvote_answer,
         name='upvote-answer'),
    path('questions/<int:pk>/answer', views.answer_question, name='answer'),
]
