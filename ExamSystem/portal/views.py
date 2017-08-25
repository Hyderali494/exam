from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
#from portal.models import Register,FeedBack
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login
def index(request):
    return HttpResponse("we are in polls app")
def showlogin(request):
    return render_to_response('log.html')
@csrf_exempt
def getlogin(request):
    username = request.POST['username'];
    password = request.POST['password'];
    if username and password:
        user = User.objects.filter(username= username,password = password)
        if not user:
            user = User(username = username,password = password)
            user.save()
            return render_to_response('dashboard.html')
        else:
            return render_to_response('dashboard.html')
    return render_to_response('log.html')
def showregister(request):
    return render_to_response('showregister.html')
@csrf_exempt
def getregister(request):
    mail = request.POST['email']
    passw = request.POST['passw']
    phone = request.POST['phone_no']
    address = request.POST['address']
    data1 = Register.objects.filter(user_mail = mail)
    if data1:
        return HttpResponse("User Already Exists")    
    else:
        data1 = Register(user_mail = mail,password_R = passw,phone_no = phone,address = address)
        data1.save()
        return render_to_response("log.html")
def showfeedback(request):
    return render_to_response("showfeedback.html")
	
@csrf_exempt
def getfeedback(request):
    feed = int(request.POST['s'])
    if feed == 0:
        data = FeedBack(feedback = 'Excellent')
        data.save()
        return HttpResponse("Saved Sucessfully")
    elif feed == 1:
        data = FeedBack(feedback = 'Good')
        data.save()
        return HttpResponse("Saved Sucessfully")
    elif feed == 2:
        data = FeedBack(feedback = 'Average')
        data.save()
        return HttpResponse("Saved Sucessfully")
    elif feed == 3:
        data = FeedBack(feedback = 'Bad')
        data.save()
        return HttpResponse("Saved Sucessfully")

def viewfeedback(request):
    results = FeedBack.objects.all()
    return render(request,'viewfeedback.html',{'results':results})

def showhome(request):
    return render_to_response("home.html")
def showusers(request):
    users = User.objects.all()
    return render(request,'showusers.html',{'users':users})
def getcourse(request):
    choice =request.POST['course']
    data = Questions.objects.filter(course__course =  choice)
    print data.values()
def showdashboard(request):
    return render_to_response("dashboard.html")

def showCheck(request):
    return render_to_response("check.html")
