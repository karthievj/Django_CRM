from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
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
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        obj = Record.objects.get(id=pk)
        id = obj.pk
        obj.delete()
        messages.success(request,f"Record with id : {id} delete successfully.....")
        return redirect('home')
    else:
        messages.success(request,"You must need to login to delete the record...")
        return redirect('home')
    
def add_record(request):
        form = AddRecordForm(request.POST or None)
        if request.user.is_authenticated:
            if request.method =="POST":
                if form.is_valid():
                    form.save()
                    first_name = form.cleaned_data['first_name']
                    last_name = form.cleaned_data['last_name']
                    # name = str(form.first_name) + str(form.last_name)
                    messages.success(request,f"{first_name} {last_name} added successfully...")
                    return redirect('home')
            return render(request,'add_record.html',{'form':form})
        else:
            messages.success(request,"You must need to login to add the record...")
            return redirect('home')
        
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Has been updated")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})

    else:
        messages.success(request,"You must need to login to update the record...")
        return redirect('home')
        


    
        



    

