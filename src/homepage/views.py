from django.shortcuts import render
from models import post
from models import terms
# Create your views here.
def home(request):
	list_posts = post.objects.order_by('id')

	# Check if user is authenticated, if so redirect them 
	
	return render(request, "index.html",{"number_1": list_posts[0], "number_2": list_posts[1],"number_3": list_posts[2]})

def details_1(request):
	list_posts = post.objects.order_by('id')
	
	return render(request, "view_details.html",{"data": list_posts[0]})

def details_2(request):
	list_posts = post.objects.order_by('id')

	return render(request, "view_details.html",{"data": list_posts[1]})

def details_3(request):
	list_posts = post.objects.order_by('id')

	return render(request, "view_details.html",{"data": list_posts[2]})

def term(request):
	info = terms.objects.get(pk=1).info

	return render(request, "terms.html",{"info":info})
