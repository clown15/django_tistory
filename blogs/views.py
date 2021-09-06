from django.shortcuts import render,redirect,reverse
from .models import Post,Comment
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('-created_at')

    return render(request,'blogs/posts_list.html',context={'posts':posts})

def post_detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request,'blogs/post_detail.html',context={'post':post,'comments':comments, 'is_liked':is_liked, 'total_likes':post.total_likes()})

@login_required
def post_write(request):
    errors = {}

    if request.method == "POST":
        title = request.POST.get('title','').strip()
        content = request.POST.get('content','').strip()
        image = request.FILES.get('image')

        if not title:
            errors['title'] = '제목을 입력하세요.'
        if not content:
            errors['content'] = '내용을 입력하세요.'

        if not errors:
            post = Post.objects.create(user=request.user,title=title,content=content,image=image)
            
            # post_detail/post_id로 리턴한다
            return redirect(reverse('post_detail', kwargs={'post_id': post.id}))
        
        return render(request, 'blogs/post_write.html', {'user':request.user, 'errors':errors})
    
    return render(request, 'blogs/post_write.html')

@login_required
def post_update(request,post_id):
    errors = {}

    # post = Post.objects.filter(id=post_id, user=request.user)
    post = get_object_or_404(Post,pk=post_id, user=request.user)
    if request.method == "POST":
        title = request.POST.get('title','').strip()
        content = request.POST.get('content','').strip()
        image = request.FILES.get('image')

        if not title:
            errors['title'] = '제목을 입력하세요.'
        if not content:
            errors['content'] = '내용을 입력하세요.'
        if not errors:
            post.title = title
            post.content = content
            post.image = image
            post.save()

            return redirect(reverse('post_detail', kwargs={'post_id': post_id}))
        
        return render(request, 'blogs/post_update.html', {'post':post, 'errors':errors})
    return render(request,'blogs/post_update.html',{'post':post})

@login_required
def comment_write(request):
    errors = {}
    if request.method == "POST":
        post = request.POST.get('post_id','').strip()
        content = request.POST.get('content','').strip()

        if not post:
            errors['post'] = '잘못된 접근입니다.'
        if not content:
            errors['content'] = '내용을 입력하세요.'

        if not errors:
            comment = Comment.objects.create(user=request.user, post_id=int(post), content=content)

    # post_detail/post_id로 리턴한다
    return redirect(reverse('post_detail', kwargs={'post_id': post}))

@login_required
@require_POST
def post_like(request):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    is_liked = post.likes.filter(id=request.user.id).exists()

    # 누른상태
    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    # return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
    return HttpResponse(status=200)