from django.shortcuts import render,redirect
from subscribe.forms import NewsletterSignUpForm
from django.http import HttpResponse
from .forms import *


def subscribe(request):
    form = NewsletterSignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/Landing_Page/intrest/')

    return render(request, 'subscribe.html', {'form': form})


def unsubscribe(request):
        form = NewsletterSignUpForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetterUser.objects.filter(email=instance.email).exists():
                NewsLetterUser.objects.filter(email=instance.email).delete()
            else:
                print("Sorry! we did not find your email.")

        return render(request, 'unsubscribe.html', {'form': form})

def subscribers_intrest(request):
    if request.user.is_authenticated:
        form = intrestform(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
    else:
        return redirect('/login/')


    return render(request, "intrest.html", context)




