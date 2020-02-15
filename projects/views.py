# Create your views here.
from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'projects': projects,
        'num_visits': num_visits
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
