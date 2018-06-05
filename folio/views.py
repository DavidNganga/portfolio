from django.shortcuts import render
from .models import Project
# Create your views here.
def index(request):

    return render (request, 'index.html')

def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect('index')
    else:
        form = ProfileForm()
    return render(request, 'project.html', {"form": form})

def viewproject(request):
    projects = Project.get_all()
    return render (request, 'viewproject.html', {"projects":projects})
