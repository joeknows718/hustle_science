from models import Post

def set_menu_context(request):
	video =  Post.objects.filter(content_type="video")
	article = Post.objects.filter(content_type="article")
	photo = Post.objects.filter(content_type="photo")
	code = Post.objects.filter(catagory__icontains="code")

	video_business = video.filter(catagory__icontains="business")[:2]
	video_fashion = video.filter(catagory__icontains="fashion")[:2]
	video_music = video.filter(catagory__icontains="music")[:2]
	video_art = video.filter(catagory__icontains="art")[:2]
	video_culture = video.filter(catagory__icontains="culture")[:2]
	video_tech = video.filter(catagory__icontains="technology")[:2]
	video_news = video.filter(catagory__icontains="news")[:2]

	article_business = article.filter(catagory__icontains="business")[:2]
	article_fashion = article.filter(catagory__icontains="fashion")[:2]
	article_music = article.filter(catagory__icontains="music")[:2]
	article_art = article.filter(catagory__icontains="art")[:2]
	article_culture = article.filter(catagory__icontains="culture")[:2]
	article_tech = article.filter(catagory__icontains="technology")[:2]
	article_news = article.filter(catagory__icontains="news")[:2]

	photo_fashion = photo.filter(catagory__icontains="fashion")[:2]
	photo_music = photo.filter(catagory__icontains="music")[:2]
	photo_art = photo.filter(catagory__icontains="art")[:2]
	photo_culture = photo.filter(catagory__icontains="culture")[:2]
	photo_tech = photo.filter(catagory__icontains="technology")[:2]

	code_project = code.filter(catagory__icontains="project")[:2]
	code_lib = code.filter(catagory__icontains="library")[:2]
	code_tutorial = code.filter(catagory__icontains="tutorial")[:2]

	return {
		'video_business' : video_business,
		'video_news' : video_news,
		'video_tech' : video_tech,
		'video_culture' : video_culture,
		'video_music' : video_music,
		'video_art' : video_art,
		'video_fashion' : video_fashion,
		'article_news': article_news,
		'article_tech': article_tech,
		'article_culture' : article_culture,
		'article_music' : article_music,
		'article_art' : article_art,
		'article_fashion' : article_fashion,
		'article_business' : article_business,
		'photo_tech': photo_tech,
		'photo_culture' : photo_culture,
		'photo_art' : photo_art,
		'photo_music' : photo_music,
		'photo_fashion' : photo_fashion,
		'code_tutorial' : code_tutorial,
		'code_lib' : code_lib,
		'code_project' : code_project
		}
	}