from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
def index(request):

    return render (request, 'index.html')

def contact(request):

    return render (request, 'contact.html')

def about(request):

    return render (request, 'about.html')

def skills(request):

    return render (request, 'skills.html')

def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)

            project.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})

def viewproject(request):
    projects = Project.get_all()
    return render (request, 'viewproject.html', {"projects":projects})
