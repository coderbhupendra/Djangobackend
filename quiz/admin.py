from django.contrib import admin

# Register your models here.
from django.contrib import admin
from quiz.models import Question,Exam,Answer,User,Submission


admin.site.register(Exam)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Submission)