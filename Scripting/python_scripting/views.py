from django.shortcuts import render
# Create your views here.
# Python logic goes here!!!!
import pdb,os
def index(request):
    try:
        context ={'message':'Hello world'}
        return render(request,'python_scripting/index.html', context)
    except Exception as e:
        print str(e)
    
    
    
def Documents(request):
    try:
        pdb.set_trace()
        context ={}
        print os.getcwd()
        with open("Documents.html") as file:
            context =dict(enumerate(line.strip() for line in file))
        return render(request,'python_scripting/Documents.html', context)
    except Exception as e:
        print str(e)

