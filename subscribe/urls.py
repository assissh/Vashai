from django.contrib import admin
from django.urls import path
from.views import subscribe,unsubscribe,subscribers_intrest


urlpatterns = [

    path('subscribe/', subscribe),
    path('unsubscribe/', unsubscribe),
    path('intrest/',subscribers_intrest)



]
