from django.shortcuts import render
from django.http import HttpResponse

from .models import Question,Exam,Answer,Submission
# # Create your views here.
# def index(request):
# 	return HttpResponse("Hello, world. You're at the polls index.")

# def getQuestion(request):
# 	latest_question_list = Question.objects.all()[:5]
# 	output = ', '.join([q.question_text for q in latest_question_list])
# 	return HttpResponse(output)
# # def registerUser(request):
# # 	text = request.GET.get('text')


from rest_framework import viewsets

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer 


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all().prefetch_related('answer')
    serializer_class = serializers.QuestionSerializer 

class ExamViewSet(viewsets.ModelViewSet):
    queryset = models.Exam.objects.all()
    serializer_class = serializers.ExamSerializer     

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = models.Answer.objects.all().prefetch_related('question')
    serializer_class = serializers.AnswerSerializer 

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.Submission.objects.all()
    serializer_class = serializers.SubmissionSerializer         