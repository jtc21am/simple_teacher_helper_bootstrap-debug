from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from student_app.models import Student
from student_app.forms import StudentForm

# Create your views here.
class IndexView(View):
  def get(self, request):
    students = Student.objects.all()

    context = {
    'student_list': students,
  }

    return render(  
      request=request,
      template_name='index.html', 
      context=context
  )

    def post(self, request):
        task_form = TaskForm(request.POST)
        task_form.save()


class StudentDetailView(View):
  def get(self, request, student_id):
    student = Student.objects.get(pk=id)
    return render(
        request=request,
        context=context,
  )


class NewStudentView(View):
  def get(self, request):
    form = StudentForm()

    return render(
        request=request,
        template_name='add.html',
        context={
            'form': StudentForm,
        },
    )

  def post(self, request):
    form = StudentForm(request.POST)

    if form.is_valid():
      new_studentnumber = form.cleaned_data['studentnumber']
      new_firstname = form.cleaned_data['firstname']
      new_lastname = form.cleaned_data['lastname']
      new_telephone = form.cleaned_data['telephone']
      new_email = form.cleaned_data['email']
      new_fieldofstudy = form.cleaned_data['fieldofstudy']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        studentnumber = new_studentnumber,
        firstname = new_firstname,
        lastname = new_lastname,
        telephone = new_telephone,
        email = new_email,
        fieldofstudy = new_fieldofstudy,
        gpa = new_gpa)
      new_student.save()


      return render(
        request=request,
        template_name='add.html',
        context={
        'form': StudentForm,
        'success': True},)      

    return redirect ('index')


class StudentEditView(View):
  def get(self, request, id):
    student = Student.objects.get(id = id)
    form = StudentForm(instance = student)

  

    return render(
      request=request,
      template_name='edit.html',
      context={
          'student' : student,
          'form' :  form

          })

  def post(self, request,id):
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
      form.save()

      return render(
        request=request,
        template_name='edit.html',
        context={
          'form' : form,
          'success' : True
          },)



    else:
      return render(
        request=request,
        template_name='edit.html',
        context={
          'form' : form,
          'success' : False
          },)

    return render(
      request=request,
      template_name='edit.html',
      context={
      'form': StudentForm,
      })      

    return redirect ('index')


class StudentDeleteView(View):
  def get(self, request, id):
        student = Student.objects.get(id = id)
        form = StudentForm(instance = student)
        return render(
                    request=request,
                    template_name='add.html',
                    context={
                       'student' : student,
                       'form' :  form
                    }
                )

  def post(self, request, id):
    student = Student.objects.get(pk=id)
    form = StudentForm()
    student.delete()

    return render(
      request=request,
      template_name='add.html',
      context={
      'form': StudentForm,
      'success': True},)  

    return redirect ('index')
