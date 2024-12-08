from django.shortcuts import render, redirect, get_object_or_404
from .models import Group


def home(request):
    return render(request, 'index.html')


def gorups_list(request):
    g_list = Group.objects.all
    ctx = {'g_list': g_list}
    return render(request, 'group/group_list.html', ctx)


def groups_create(request):
    if request.method == 'POST':
        g_name = request.POST.get('g_name')
        g_type = request.POST.get('g_type')
        if g_name and g_type:
            Group.objects.create(
                g_name = g_name,
                g_type = g_type,
            )
            return redirect('groups:list')
    return render(request, 'group/group_create.html')


def groups_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'group/group_detail.html', ctx)


def groups_del(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:list')

