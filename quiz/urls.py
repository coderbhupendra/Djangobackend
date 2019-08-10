from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('questions/', views.getQuestion, name='getQuestion'),
# ]


from .views import QuestionViewSet,ExamViewSet,AnswerViewSet,SubmissionViewSet,UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet, base_name='user')
router.register('questions', QuestionViewSet, base_name='questions')
router.register('exam', ExamViewSet, base_name='exam')
router.register('answer', AnswerViewSet, base_name='answer')
router.register('submission', SubmissionViewSet, base_name='submission')
urlpatterns = router.urls