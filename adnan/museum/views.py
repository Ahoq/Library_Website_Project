from django.shortcuts import render

posts = [

	{

		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'

	},

	{

		'author': 'Adnan',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2018'

	}




]




def home(request):
	context ={
		'posts': posts
	}
	return render(request, 'museum/index.html', context)

def hours(request):
	return render(request, 'museum/hours.html/')

def about(request):
	return render(request, 'museum/about.html/')

def ex1(request):
	return render(request, 'museum/item1.html/')

def ex2(request):
	return render(request, 'museum/ex2.html/')

def ex3(request):
	return render(request, 'museum/ex3.html/')

def ex4(request):
	return render(request, 'museum/ex4.html/')














