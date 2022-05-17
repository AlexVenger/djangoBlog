from django.shortcuts import render
from .models import Post

posts = [
	{
		"author": "Average Chungus",
		"title": "How to yeet. Beginner's manual",
		"content": "yes",
		"date": "8 April 2018"
	},
	{
		"author": "Big Chungus",
		"title": "How to yeet. Professional's guide",
		"content": "no",
		"date": "8 April 2018"
	}
]


def home(request):
	context = {
		'posts': Post.objects.all(),
		'title': "Home Page"
	}
	return render(request, 'blog_app/home.html', context)


def about(request):
	return render(request, 'blog_app/about.html', {'title': 'About'})
