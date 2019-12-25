from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def register(request):
	url = reverse_lazy('login')+'register.html'
	return render(request, url)