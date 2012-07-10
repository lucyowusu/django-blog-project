from django.contrib import admin

from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	def __unicode__(self):
		return self.title

	def title_first_60(self):
		return self.body[:60]

class Comment(models.Model):
	body = models.TextField()
	author = models.CharField(max_length=60)
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	post = models.ForeignKey(Post,related_name='posted comment')
	def __unicode__(self):
		return self.author

class CommentInline(admin.TabularInline):
	model = Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','body','created','updated')
	list_filter = ('title','body')
	search_fields = ('title','body')
	ordering = ('title','-created')
	inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author','body','created','updated')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)






