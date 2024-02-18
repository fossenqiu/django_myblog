from myblog.models import MyBlogPost
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def archive(request):

    posts = MyBlogPost.objects.all()[:10]
    text = loader.get_template("archive.html")
    context = {'posts': posts}
    return HttpResponse(text.render(context))
