zzfrom models import Post

def set_menu_context(request):
	video =  Post.objects.filter(content_type__media_type="video")
	article = Post.objects.filter(content_type__media_type="article")
	photo = Post.objects.filter(content_type__media_type="photo")
	code = Post.objects.filter(category__tag__in=['code'])

	video_business = video.filter(category__tag__in="business")[:2]
	video_fashion = video.filter(category__tag__in="fashion")[:2]
	video_music = video.filter(category__tag__in="music")[:2]
	video_art = video.filter(category__tag__in="art")[:2]
	video_culture = video.filter(category__tag__in="culture")[:2]
	video_tech = video.filter(category__tag__in="technology")[:2]
	video_news = video.filter(category__tag__in="news")[:2]

	article_business = article.filter(category__tag__in="business")[:2]
	article_fashion = article.filter(category__tag__in="fashion")[:2]
	article_music = article.filter(category__tag__in="music")[:2]
	article_art = article.filter(category__tag__in="art")[:2]
	article_culture = article.filter(category__tag__in="culture")[:2]
	article_tech = article.filter(category__tag__in="technology")[:2]
	article_news = article.filter(category__tag__in="news")[:2]

	photo_fashion = photo.filter(category__tag__in="fashion")[:2]
	photo_music = photo.filter(category__tag__in="music")[:2]
	photo_art = photo.filter(category__tag__in="art")[:2]
	photo_culture = photo.filter(category__tag__in="culture")[:2]
	photo_tech = photo.filter(category__tag__in="technology")[:2]

	code_project = code.filter(category__tag__in="project")[:2]
	code_lib = code.filter(category__tag__in="library")[:2]
	code_tutorial = code.filter(category__tag__in="tutorial")[:2]

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