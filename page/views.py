from django.shortcuts import render


def index(request):
	context_dict ={'name' : 'Rose'}
	return render(request, 'index.html' , context_dict)


# Create your views here.
