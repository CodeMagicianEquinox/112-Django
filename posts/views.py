from django.shortcuts import render, HttpResponse

# Create your views here.

def list_posts(request):
    return HttpResponse("All posts")

def detail_post(request, id):
    return HttpResponse(f"Post {id}")

def new_post(request):
    return HttpResponse("Create a new post")

def delete_post(request, id):
    return HttpResponse(f"Delete post {id}")
