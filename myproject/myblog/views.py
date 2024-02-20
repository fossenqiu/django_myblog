from myblog.models import MyBlogPost, MyBlogPostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime as dt
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def archive(request):

    posts = MyBlogPost.objects.all()[:10]
    text = loader.get_template("archive.html")
    context = {'posts': posts, 'form': MyBlogPostForm}
    return HttpResponse(text.render(context, request))


# @csrf_exempt
def create_myblog_post(request):
    if request.method == 'POST':
        form = MyBlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = dt.now()
            post.save()
    print("create myblog post ok", dt.now())
    return HttpResponseRedirect('/myblog')
