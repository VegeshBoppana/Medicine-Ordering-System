from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Medicines

from pymongo import MongoClient


client=MongoClient('mongodb+srv://FinalProject:hemanagachand@cluster0.lvwc1rs.mongodb.net/')
mydb=client['login_details']
coll=mydb.credentials

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']

        user=coll.find_one({'username': username, 'password': password})

        if user:
            return redirect('home')
        
    return render(request,"index.html")    

def register(request):
    return render(request,"register.html")

def save_details(request):
    if request.method == 'POST':
        username=request.POST['username']
        age=request.POST['age']
        gender=request.POST['gender']
        password1=request.POST['Password1']
        password2=request.POST['Password2']

        if password1==password2:
            coll.insert_one({'username': username, 'age': age, 'gender': gender, 'password': password1})
            return render(request,"index.html")
        
    return render(request,"register.html")
def meds(request):
    medicine = Medicines.objects.all()
    medicines = {'medicines': medicine}
    return render(request, 'meds.html', medicines)

from django.shortcuts import render
from .models import Medicines
def search_meds(request):
    search_input = request.POST['search']

    
    if search_input:
        medicines = Medicines.objects.filter(name__icontains=search_input)
    else:
        medicines = Medicines.objects.all()

   
    if not medicines:
        message = 'No medicines found.'
    else:
        message = ''

    return render(request, 'meds.html', {'medicines': medicines, 'message': message})
def logout(request):
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")
def payment(request):
    return render(request,"payment.html")