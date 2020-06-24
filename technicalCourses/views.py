from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import AllCourses, Details
from django.template import loader

def Courses(req):
  ac = AllCourses.objects.all()
  template = loader.get_template('./TechnicalCourses/courses.html')
  context = {
    'ac': ac,
  }
  return HttpResponse(template.render(context, req))

def Detail(req, course_id):
  # try:
  #   course = AllCourses.objects.get(pk=course_id)
  # except AllCourses.DoesNotExist:
  #   raise Http404('Course not available')
  # # return HttpResponse('<h2>These are the course details for course id: ' + str(course_id)+ '</h2>')
  # return render(req, './TechnicalCourses/detail.html', { 'course':course })
  course = get_object_or_404(AllCourses, pk=course_id)
  return render(req, './TechnicalCourses/detail.html', {
    'course': course
  })

def YourChoice(req, course_id):
  course = get_object_or_404(AllCourses, pk=course_id)
  try:
    selected_ct = course.details_set.get(pk=req.POST['choice'])
  except (KeyError, AllCourses.DoesNotExist):
    return render (req, 'AllCourses/detail.html', {
      'course': course,
      'error_message': 'Select a valid option '
    })
  else:
    selected_ct.your_choice=True
    selected_ct.save()
    return render(req, './TechnicalCourses/detail.html', {
      'course': course
    })


# Create your views here.
