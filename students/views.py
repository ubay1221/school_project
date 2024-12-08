from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def students_list(request):
    s_list = Student.objects.all
    ctx = {'s_list': s_list}
    return render(request, 'student/student_list.html', ctx)


def students_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        if first_name and last_name and age and email:
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                email=email,
            )
            return redirect('students:list')
    return render(request, 'student/student_create.html')


def students_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'student/student_detail.html', ctx)


def students_del(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')