from django.test import TestCase
import datetime
from django.utils import timezone
from .models import AllCourses

class AllCoursesModelTests(TestCase):
  def test_was_published_recently_with_future_course(self):
    time = timezone.now() + datetime.timedelta(days=30)
    future_questions = AllCourses(startedfrom=time)
    self.assertIs(future_questions.was_published_recently(), False)

  def test_was_published_recently_with_old_course(self):
    time = timezone.now() + datetime.timedelta(days=1, seconds=1)
    old_course = AllCourses(startedfrom=time)
    self.assertIs((old_course.was_published_recently(), False))

  def test_was_published_recently_with_recent_course(self):
    time = timezone.now() + datetime.timedelta(hours=23, minutes=59, seconds=59)
    old_course = AllCourses(startedfrom=time)
    self.assertIs((old_course.was_published_recently(), True))


