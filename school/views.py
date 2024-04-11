from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from school.models import Register, Customer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse

# Create your views here.
def index(request):
     return render(request,"index.html")


def home(request):
    return render(request, "home.html")
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            login(request)
            return render(request,"click.html")  # Redirect to the dashboard or any other desired page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data=Register.objects.all()
        for i in data:
            print(i[0])
            if username in i[0]:

                print("yes")
            else:
                print("no")


    return render(request, 'login.html')


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully")
            return redirect(index)
        else:

            HttpResponse("Invaid data")
    return render(request, 'register.html',{'form': form})


def click(request):
    return render(request,'click.html')

def form(request):

    return render(request, "form.html")


def submitted(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        birthDate = request.POST['birthDate']
        Age = request.POST['Age']
        gender = request.POST['gender']
        PhoneNumber = request.POST['PhoneNumber']
        address = request.POST['address']
        email = request.POST['email']
        if Customer.objects.filter(Email=email).exists():
            return HttpResponse('Error, Email already exist')
        else:
            new_user = Customer(name=Name, Age=Age, birthDate=birthDate, Email=email, gender=gender,phoneNumber=PhoneNumber, address=address)
            new_user.save()
            return redirect('submitted')
    return render(request, "submitted.html")

def logout(request):
    return render(request,"home.html")
def homepage(request):
    return render(request,"home.html")

