"""
This code should be copy and pasted into blog/urls.py
"""


from django.conf.urls.defaults import *
   
urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail'),
    url(r'^posts/search/(\w*)/$', 'blog.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit/$', 'blog.views.edit_comment', name='edit_comment'),
    ## add your url here
)
