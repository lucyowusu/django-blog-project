# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Post, Comment 


def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))



def post_detail(request, id, showComments=False):
    print id
    post_item = Post.objects.get(pk=id)
    if showComments !=False:

        for eachcomment in Comment.objects.filter(id=id):
		comment = eachcomment.body
   # html = "<html><body><b>Post:</b><br/> %s <br/> <b>Comments:</b><br/> %s</body> </html>" %(post_item,comment)

    return render_to_response('blog/post_detail.html',{'post': post, 'comments':comment})


    
def post_search(request, term):
    found = ''
    found_item = Post.objects.filter(body__contains=term)
    for everyitem in found_item:
        found += str(everyitem.title)
    return render_to_response('blog/post_search.html',{'posts':found,'term':term})
    

def home(request):
	return render_to_response('blog/base.html',{})

