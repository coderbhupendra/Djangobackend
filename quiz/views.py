from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import Question,Exam,Answer,Submission
# # Create your views here.

from rest_framework import viewsets

from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer 


class QuestionViewSet(viewsets.ModelViewSet):
	queryset = models.Question.objects.all()
	serializer_class = serializers.QuestionSerializer 

class ExamViewSet(viewsets.ModelViewSet):
	queryset = models.Exam.objects.all()
	serializer_class = serializers.ExamSerializer     

class AnswerViewSet(viewsets.ModelViewSet):
	queryset = models.Answer.objects.all()
	serializer_class = serializers.AnswerSerializer 

class SubmissionViewSet(viewsets.ModelViewSet):
	queryset = models.Submission.objects.all()
	serializer_class = serializers.SubmissionSerializer  


#get unanswered question based on userid ans exam id
def get_unanswered_questions(request:HttpResponse):
	userid=request.GET.get('userid'); 
	examid=request.GET.get('examid'); 
	answered_questions = models.Submission.objects.filter(user__pk=userid,question__exam__id=examid).values_list('question__pk', flat=True);
	questions_set= models.Question.objects.exclude(pk__in=answered_questions).filter(exam__id=examid)
	serializer= serializers.QuestionSerializer(questions_set,many=True) 
	return  HttpResponse(serializer.data)

def get_submission(request:HttpResponse):
	userid=request.GET.get('userid'); 
	answered_questions = models.Submission.objects.filter(user__pk=userid).values_list('question__question_text','answers__answer_text');
	return  HttpResponse(answered_questions)
				 
	# answered_questions = models.Submission.objects.filter(user__pk=userid).all();
	# response=[]
	# res={
	# 	'question':'',
	# 	'answer':''
	# }
	# for obj in answered_questions :
	# 	print(obj)
	# 	res.question=obj.question_text;
	# 	res.answer=obj.answers.answer_text;
	# 	response.append(res)

	

	