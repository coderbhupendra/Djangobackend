from django.db import models

# Create your models here.

class User(models.Model):
	name=models.CharField(max_length=64)
	age= models.IntegerField()
	email= models.CharField(max_length=64)

	def __str__(self):
		return self.name

class Answer(models.Model):
	answer_text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')

	def __str__(self):
		return self.answer_text
		
class Exam(models.Model):
	name = models.CharField(max_length=64, verbose_name=u'Exam name', )

	def __str__(self):
		return self.name

class Question(models.Model):
	question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text')
	answer = models.OneToOneField(Answer, on_delete=models.CASCADE,related_name='correct_answer', null=True, blank=True)
	choices = models.ManyToManyField(Answer, related_name='choices')
	exam= models.ForeignKey(Exam, related_name='exam',on_delete=models.PROTECT)

	def __str__(self):
		return "{content}".format(content=self.question_text)



class Submission(models.Model):
	user= models.ForeignKey(User, related_name='user',on_delete=models.PROTECT)
	question = models.ForeignKey(Question, related_name='question',on_delete=models.PROTECT)
	answers= models.ForeignKey(Answer, related_name='answer',on_delete=models.PROTECT)
	result=models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		print(self.user,self.question)
		self.result=self.question.answer==self.answers;
		super(Submission, self).save(*args, **kwargs) 
		
	def __str__(self):
		return "{user} - {question} - {answer}".format(user=self.user.name, question=self.question.question_text, answer=self.answers.answer_text)        