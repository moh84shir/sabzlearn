from django.urls import path
from . import views


urlpatterns = [
    path('', views.CoursesListView.as_view()),
    path('course/<pk>', views.CourseDetailView.as_view()),
    # render partials
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
]
