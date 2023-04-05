from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList =[
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title':'Portfoli Website',
        'description':'This is a sample project'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Open source project'
    },
]

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
# Create your views here.
