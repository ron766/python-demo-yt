from django.urls import path
from . import views

app_name='technicalCourses'

urlpatterns = [
  path('', views.Courses, name='home-page'),
  path('<int:course_id>/', views.Detail, name='detail'),
  path('<int:course_id>/yourchoice/', views.YourChoice, name='yourchoice')
]
