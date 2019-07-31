from django.shortcuts import render
from . import models as blog_model


def BlogList(request):
	context = {"posts": blog_model.Post.objects.all()}
	return render(request, "blog/all-posts.html", context)


def blog(request, post_id):
	post_data = blog_model.Post.objects.get(pk=post_id)
	data = []
	image = ""

	# exception handling
	try:
		image = post_data.cover.url.split('/static/')[1]
	except Exception as e:
		print(e)

	data.append({
		'title': post_data.title,
		'image': image,
		'text': post_data.text,
		'author': post_data.author,
		'category': post_data.category,
		'published_date': post_data.published_date
	})

	context = data[0]
	print(post_data.category)
	return render(request, "blog/blog.html", context)

