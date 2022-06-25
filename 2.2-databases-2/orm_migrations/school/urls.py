from django.urls import path

from school.views import StudentsView

urlpatterns = [
    path('', StudentsView.as_view(), name='students'),
]
