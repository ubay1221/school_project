from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def teachers_list(request):
    t_list = Teacher.objects.all
    ctx = {'t_list': t_list}
    return render(request, 'teacher/teacher_list.html', ctx)


def teachers_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subjects = request.POST.get('subjects')
        if first_name and last_name and subjects:
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subjects=subjects,
            )
            return redirect('teachers:list')
    return render(request, 'teacher/teacher_create.html')


def teachers_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teacher/teacher_detail.html', ctx)


def teachers_del(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:list')