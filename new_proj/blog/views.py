from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts=[
    {
        'author':'Pada',
        'title':'Blog post 1',
        'content':'First Post',
        'date_posted':'August 28 2023'
    },
    {
        'author':'Dada',
        'title':'Blog post 2',
        'content':'2nd Post',
        'date_posted':'August 30 2023'
    },
    
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})


