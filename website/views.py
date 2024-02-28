from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    #authentication
    records = Record.objects.all()
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"{} is logged in !!!!".format(username))
            return redirect('home')
        else:
            messages.error(request,"Error in logging!!!!!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You're successfully logged out ! ! !")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You're successfully registered")
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def record_view(request,pk):
    if request.user.is_authenticated:
        #fetch records
        individual_record = Record.objects.get(id=pk)
        return render(request,'record.html',{'individual_record':individual_record})
    else:
        messages.success("Youre not logged in ")
        return redirect('home')



    

