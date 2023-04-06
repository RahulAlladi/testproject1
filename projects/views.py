from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# projectsList =[
#     {
#         'id':'1',
#         'title':'Ecommerce Website',
#         'description':'Fully functional ecommerce website'
#     },
#     {
#         'id':'2',
#         'title':'Portfoli Website',
#         'description':'This is a sample project'
#     },
#     {
#         'id':'3',
#         'title':'Social Network',
#         'description':'Open source project'
#     },
# ]

def projects(request):
    # msg="products"
    # age=20
    # context={'page':msg, 'age':age,'projects':projectsList}
    projects = Project.objects.all()
    context={'projects':projects}
    return render(request, 'projects/projects.html',context)

def project2(request,pk):
    #print("the parameter that you passed is "+pk)
    # projectObj = None
    # for i in projectsList:
    #     if i['id'] == pk:
    #         projectObj = i
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html',{'project':projectObj, 'tags':tags})

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, request.FILES)
        #print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html',context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        #print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html',context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
