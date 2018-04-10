from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib import auth
from news.forms import registrationform



def register(request):
    if request.method =='POST':
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Landing_Page/subscribe')
    else:
        form = registrationform()
    args = {'form':form}
    return render(request,'register.html',args)






