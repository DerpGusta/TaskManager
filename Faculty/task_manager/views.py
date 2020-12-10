""" views for all apps """
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import TaskForm
from .models import Task, KRA, Metric
from .models import Task


class TaskListView(ListView):
    """ Generic Listview for all the tasks """
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_manager/tasks.html'
    paginate_by = 10

class TaskDetailView(DetailView):
    model = Task

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'
#  UserPassesTestMixin,
    # def test_func(self):
    #     task = self.get_object()
    #     if self.request.user == task.author:
    #         return True
    #     return False

class TaskCreateView(LoginRequiredMixin, CreateView):
    """ CreateView for Tasks """
    model = Task
    form_class = TaskForm
    # fields = ['key_area', 'metric', 'description']

    def form_valid(self, form):
        form.instance.department = self.request.user.userdata.department
        form.instance.branch = self.request.user.userdata.branch
        # form.instance.author = self.request.user.username
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """ UpdateView for Tasks """
    model = Task
    fields = ['key_area', 'metric', 'description']

    def form_valid(self, form):
        form.instance.department = self.request.user.userdata.department
        form.instance.branch = self.request.user.userdata.branch

        return super().form_valid(form)
        #  UserPassesTestMixin
    # def test_func(self):
    #     task = self.get_object()
    #     if self.request.user == task.author:
    #         return True
    #     return False

        # Create your views here.
def load_metrics(request):
    key_area = request.GET.get('key_area')
    metrics = Metric.objects.filter(category_id=key_area)

    return render(request, 'task_manager/metrics.html', {'metrics': metrics})
