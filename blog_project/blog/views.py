from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/post.html',{'post_list_view':post_list})



def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,publish__year=year,publish__month=month,publish__day=day,slug=post,)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
            return redirect('/{}/{}/{}/{}'.format(post.publish.year,post.publish.strftime('%m'),post.publish.strftime("%d"),post.slug))
    else:
        form=CommentForm()




    return render(request,"blog/post_detail.html",{'post':post,'csubmit':csubmit,'form':form,'comments':comments})
from django.core.mail import send_mail
from blog.forms import Mail,CommentForm
def send_mail_view(request,id):
    obj=get_object_or_404(Post,id=id)
    sent=False
    if request.method == 'POST':
        form=Mail(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) Recommends you to read this \"{}\" Post'.format(cd['name'],cd['From'],obj.title)
            post_url=request.build_absolute_uri(obj.get_absolute_url())
            message='Read post At:\n {}\n\n{}\' Comments:\n{}\n\n\n{}'.format(post_url,cd['name'],cd['comments'],obj.body)
            send_mail(subject,message,'puneettrivediblog77',[cd['to']])
            sent=True
    else:
        form=Mail()

    return render(request,'blog/sharemail.html',{'form':form,'obj':obj,'sent':sent})
