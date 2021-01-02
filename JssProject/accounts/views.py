from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    regi_form = UserCreationForm()
    
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            print("jj")
            return redirect('index')

    return render(request, 'signup.html', {'regi_form':regi_form})