from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': "Main page", 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form was invalid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
# class Create(CreateView):
#     template_name = 'main/create.html'
#     form_class = TaskForm
#     success_url = reverse_lazy('main:home')
