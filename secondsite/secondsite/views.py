from django.http import HttpResponse  
import datetime

def hello(request):
    return HttpResponse("Hello world,lin yue lin")
	
def linyuelin(request):
	return HttpResponse("CONGRADUALATION!!!")

def my_homepage_view(request):
	return HttpResponse('This is the homepage!')
	
def current_datetime(request):
	now=datetime.datetime.now()
	html = "it is now %s."%now 
	return HttpResponse(html)