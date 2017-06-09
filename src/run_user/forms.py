from django import forms
from django.forms.extras.widgets import SelectDateWidget

class signupForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'col-xs-12 col-sm-4 form-control flatTextInput', 'placeholder':'Name'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class':'col-xs-12 col-sm-4 form-control flatTextInput', 'placeholder':'Email'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'col-xs-12 col-sm-4 form-control flatTextInput', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'col-xs-12 col-sm-4 form-control flatTextInput', 'placeholder':'Password'}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'col-xs-12 col-sm-4 form-control flatTextInput', 'placeholder':'Confirm Password'}))
    Grad_Date = (
    	('1','Graduated'),
    	('2','2016'),
    	('3','2017'),
    	('4','2018'),
    	('5','2019'),
    	('6','2020'),
    	('7','2021'),
    	)
    status = (
    	('1','I\'m an Undergradute Student'),
		('2','I\'m a Graduate Student'),
		('3','I\'m an Alumni'),
		('4','I\'m a Teacher'),
		('5','I\'m a lifelong learner'),
    	)
    
    grad = forms.ChoiceField(label='', choices=Grad_Date, widget=forms.Select(attrs={'class':'form-control flatSelectInput'}))
    student = forms.ChoiceField(label='', choices=status, widget=forms.Select(attrs={'class':'form-control flatSelectInput'}))
    '''
    Clean:

    name: check if long enough, exists,
    username: check if available, exists
    password: check if long enough
    confirm password: check if same

    check if the two boxes are filled

    check recaptcha

    finally:

    	post save user.
    	send email confirm

    '''