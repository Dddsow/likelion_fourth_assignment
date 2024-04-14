from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# READ
def home(request): 
    #이게 발동된거임 2번호출을 받아서 냉장고매니저(models) 를 통해 가져오게 됨 짜여진 틀안에서
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj}) 
    #요청행위(url)로 요리(views)을 만들어서 냉장고매니저(models)를 통해서 그릇에 담아서 나가야하니 
    #response를 통해서 
    #template를 return하여 나간다 식탁(home.html)으로 다시 나간다

# DETAIL READ
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})#blog를 blog라는 이름으로 detail.html에 담을거야


# CREATE
def new(request):
    return render(request, 'new.html')


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content'] 
    new_blog.image = request.FILES.get('image')
    
    new_blog.save() #여기서 채워진걸 save를 한다
    return redirect('detail', new_blog.id) #redirect('detail') url의 별명이 detail인걸로 가라는거임
    # return render(request, 'detail.html', {'blog': new_blog})


# UPDATE
def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('detail', old_blog.id)
    # return render(request, 'detail.html', {'blog': old_blog})


# DELETE
def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')