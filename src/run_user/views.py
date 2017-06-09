from django.shortcuts import render
from .forms import signupForm

# Create your views here.
def login(request):
	return render(request, "login.html",{})
	
def signup(request):
	if request.method == 'POST':
		form = signupForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = signupForm()
	return render(request, "signup.html",{'form': form})