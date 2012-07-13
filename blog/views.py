# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


from models import Post, Comment 


def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))


class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude=['post']


@csrf_exempt
def post_detail(request, id, showComments=False): 
    post_item = Post.objects.get(pk=id)
    if request.method == 'POST':
       comment = Comment(post=post_item)
       form = CommentForm(request.POST,instance=comment)
       if form.is_valid():
            form.save()
	    return HttpResponseRedirect(request.path)
    else:
	form = CommentForm()

   
    if showComments !=False:
        comment=Comment.objects.filter(post_id=id)

        tt = loader.get_template('blog/post_detail.html')
        cc = Context({'comments':comment })
    else:
        pass
    return render_to_response('blog/post_detail.html',{'post': post_item, 'comments':comment,'form':form})


    
def post_search(request, term):
    found = ''
    found_item = Post.objects.filter(body__contains=term)
    for everyitem in found_item:
        found += str(everyitem.title)
    return render_to_response('blog/post_search.html',{'posts':found,'term':term})
    

def home(request):
	return render_to_response('blog/base.html',{})

