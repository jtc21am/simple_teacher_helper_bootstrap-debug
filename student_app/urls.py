from django.urls import path
from student_app.views import IndexView, StudentDetailView, StudentEditView, NewStudentView, StudentDeleteView
from . import views

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('<int:id>', StudentDetailView.as_view(), name='studentdetail'),
  path('add', NewStudentView.as_view(), name='add'),
  path('edit/<int:id>/', StudentEditView.as_view(), name='edit'),
  path('delete/<int:id>/', StudentDeleteView.as_view(), name='delete'),
]