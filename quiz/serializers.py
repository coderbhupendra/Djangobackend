from rest_framework import serializers
from .models import Question,Exam,Answer,Submission,User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Question

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Exam        

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Answer 


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = (
        #     'id',
        #     'user',
        #     'question',
        #     'answer',
        # )
        fields = "__all__"
        model = Submission         
