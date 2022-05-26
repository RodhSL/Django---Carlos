from django.shortcuts import render, reverse
from .forms import CustomUserCreationForm

def register(request):
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return reverse('/accounts/login/')
    else:
        form = CustomUserCreationForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'registration/login.html', context)