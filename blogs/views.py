from django.shortcuts import render,redirect,reverse
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts = Post.objects.order_by('-created_at')

    return render(request,'blogs/posts_list.html',context={'posts':posts})

def post_detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)

    return render(request,'blogs/post_detail.html',context={'post':post})

@login_required
def post_write(request):
    errors = {}
    if request.method == "POST":
        print(request.FILES)
        title = request.POST.get('title','').strip()
        content = request.POST.get('content','').strip()
        image = request.FILES.get('image')
        print(image)
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