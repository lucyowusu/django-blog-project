# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    print id
    post_item = Post.objects.get(pk=id)
    if showComments !=False:

        for eachcomment in Comment.objects.filter(id=id):
		comment = eachcomment.body
    html = "<html><body><b>Post:</b><br/> %s <br/> <b>Comments:</b><br/> %s</body> </html>" %(post_item,comment)
    return HttpResponse(html)


    
def post_search(request, term):
    found = ''
    found_item = Post.objects.filter(body__contains=term)
    for everyitem in found_item:
        found += str(everyitem.title)
    return HttpResponse(found)
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
