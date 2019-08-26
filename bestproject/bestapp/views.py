from django.shortcuts import render
from .models import ApplicationForm, LoginClass
import random
import sys
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
import json
import matplotlib.pyplot as plt

client = MongoClient()
db = client['dddd']

username1=''
dob1=''


def indexPage(request):
    return render(request, "index.html")


def applicationForm(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    dob = request.POST.get('dob')
    board = request.POST.get('board')
    father = request.POST.get("father")
    mother = request.POST.get("mother")
    qualification = request.POST.get('qualification')
    sname = request.POST.get('sname')
    saddress = request.POST.get('saddress')
    haddress = request.POST.get('haddress')
    anum = request.POST.get('aadharnum')
    phonenum = request.POST.get('phonenum')
    email = request.POST.get('email')
    personphoto = request.FILES['personphoto']
    signaturephoto = request.FILES['signaturephoto']
    state = request.POST.get('state')
    number = '19'+'{:03d}'.format(random.randrange(1, 999))
    username = (state + board + qualification+ number)
    # password = dob
   
   
    af = ApplicationForm(firstName = fname, lastName = lname, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress, aadharNumber = anum, phoneNumber = phonenum, emailID = email, personPhoto = personphoto,  signaturePhoto = signaturephoto,state = state, username = username)
    af.save()
 
    sub="Email From Best Scholarship"
    msg = "Hello Mr/Ms." + fname + "." + "\n" + "\n"+ "Your Application for Best Scholarship has been submitted successfully"+"\n"+ "Username:" + username + "\n" + "Password:" + dob + "\n" + "Please use the above Username and Dob to login" + "\n" + "Good Luck" + "\n" + "-Team Best Scholarship"
    send_mail(sub,msg,'best.scholarstest@gmail.com',[email])
    return HttpResponse('mail sent successfully')

# def loginCheck(request):
#     username = request.POST.get('username')
#     dob= request.POST.get('dob')
#     dbuser = ApplicationForm.objects.get(username = username, date_of_birth = dob)
#     if dbuser:
#         # login=LoginClass(username = username, dob = dob).save()
#         context={"username":dbuser.username}
#         return render(request,"studentscreen.html",context)
#     else:
#         return render(request,"loginpage.html",{"msg":"Invalid login credentials"})

def loginCheck(request):
    global username1, dob1
    username1 = request.POST.get('username')
    dob1= request.POST.get('dob')
    dbuser = ApplicationForm.objects.filter(username = username1, date_of_birth = dob1)
    if dbuser:
        return render(request,"studentscreen.html")
    else:
        return render(request,"loginpage.html",{"msg":"Invalid login credentials"})


def logout(request):
    return render(request, "loginpage.html", {"msgl": "Sucessfully Logout"})

def home2(request):
    dbuser=ApplicationForm.objects.get(username=username1,date_of_birth=dob1)
    return render(request,'a.html',{'username':dbuser.username,'photo':dbuser.personPhoto,'sign':dbuser.signaturePhoto})


def changepassword(request):
    if request.method=='POST':
        pas1=request.POST['p1']
        pas2=request.POST['p2']
        if pas1==pas2:
            a=ApplicationForm.objects.get(username=username1)
            a.date_of_birth=pas1
            a.save()
            return HttpResponse('password update sucessfully')
        else:
            return HttpResponse('both password not match')
    return render(request,'c.html')



def chart(request):
    if request.method=='POST':
        slices=[7,2,2,13]
        activities=['sleeping','eating','working','playing']
        cols=['c','m','r','b']

        plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True)
        plt.title('pie plot')
        plt.show()
    return render(request,'chat.html')







    
