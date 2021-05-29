from django.http import HttpResponse

from .models import Blogpost

from  django.shortcuts import render

def index(request):
    myPost = Blogpost.objects.all();
    print(myPost)
    return  render(request,'blog/index.html',{'myPost':myPost})


def blogpost(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post':post})
