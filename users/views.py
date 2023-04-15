from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


def registration(request):
    if request.method != 'POST':
        form = CreateUserForm()
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('exams:index'))
    context = {'form': form}
    return render(request, 'users/registration.html', context)