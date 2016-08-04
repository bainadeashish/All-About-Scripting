from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    try:
        context = {'message':'This is homepage'}
        #return HttpResponse(html)
        return render(request,'homepage.html', context)
    except Exception as e:
        print str(e)