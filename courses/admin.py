from django.contrib import admin
from .models import Course, Session


# display models for admin site
class CourseAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'teacher', 'create_date', 'updated_date']

	class Meta:
		model = Course


class SessionAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'course', 'time']

	class Meta:
		model = Session

# register models for admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Session, SessionAdmin)