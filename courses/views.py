from django.views.generic import ListView, DetailView
from .models import Course, Session
from django.shortcuts import render


class CoursesListView(ListView):
    template_name = 'courses/course_list.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_course = context.get('course')
        sessions = Session.objects.filter(course=this_course)
        context['sessions'] = sessions
        return context


# Render partials
def header(request):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/Footer.html', context)
