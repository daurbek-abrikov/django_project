from django.shortcuts import render
from .models import Post

posts = [
    {
        'author':'MCKiki',
        'title':'how to cook pizza',
        'content':'first pizza ever',
        'date_posted':'August 28, 2019'
    },
    {
        'author':'LOTRfar',
        'title':'Gimli and halаlings',
        'content':'falls and highs',
        'date_posted':'September 3, 2004'
    },
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
