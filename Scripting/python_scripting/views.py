from django.shortcuts import render
# Create your views here.
# Python logic goes here!!!!
def index(request):
    try:
        context ={'message':'Hello world'}
        return render(request,'index.html', context)
    except Exception as e:
        print str(e)
    
    
    
    

