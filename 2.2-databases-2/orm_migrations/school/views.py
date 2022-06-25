from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


#
# def students_list(request):
#     template = 'school/students_list.html'
#     all_students = Student.objects.all().prefetch_related('teachers')
#     context = {'object_list': all_students}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = 'group'
#
#     return render(request, template, context)
#

class StudentsView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    ordering = 'group'
    context_object_name = 'object_list'
    queryset = Student.objects.prefetch_related('teachers').all()
