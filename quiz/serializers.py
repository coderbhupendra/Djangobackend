from rest_framework import serializers
from .models import Question,Exam,Answer,Submission,User



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		fields = "__all__"
		model = User

# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = "__all__"
#         model = Question

class QuestionSerializer(serializers.ModelSerializer):
	choices = serializers.SerializerMethodField()

	def get_choices(self, obj):
		ordered_queryset = Answer.objects.filter(choices__id=obj.id).order_by('?')
		return AnswerSerializer(ordered_queryset, many=True, context=self.context).data
	class Meta:
		model = Question
		fields = ('question_text', 'choices')


class ExamSerializer(serializers.ModelSerializer):
	class Meta:
		fields = "__all__"
		model = Exam        

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		fields = "__all__"
		model = Answer 


class SubmissionSerializer(serializers.ModelSerializer):
	# user = serializers.SerializerMethodField()

	# def get_user(self, obj):
	# 	ordered_queryset = User.objects.filter(user__id=obj.id).order_by('?')
	# 	return UserSerializer(ordered_queryset, many=True, context=self.context).data
	
	question = serializers.SerializerMethodField()
	# answer = serializers.SerializerMethodField()

	def get_question(self, obj):
		ordered_queryset = Question.objects.filter(question__id=obj.id).order_by('?')
		return QuestionSerializer(ordered_queryset, many=True, context=self.context).data

	# def get_answer(self, obj):
	# 	ordered_queryset = Answer.objects.filter(answer__id=obj.id).order_by('?')
	# 	return AnswerSerializer(ordered_queryset, many=True, context=self.context).data	

	class Meta:
		# fields = (
		#     'id',
		#     'user',
		#     'question',
		#     'answer',
		# )    
		fields = "__all__"
		model = Submission         
