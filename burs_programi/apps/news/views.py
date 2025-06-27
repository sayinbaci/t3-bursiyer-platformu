from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, NewsCategory
from django.db.models import Q

def news_list_view(request):
    """
    Haberleri blog formatında listeler. Arama ve kategori filtreleme destekler.
    """
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    news_list = NewsArticle.objects.all().order_by('-created_at')

    if query:
        news_list = news_list.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category_id:
        news_list = news_list.filter(category__id=category_id)

    categories = NewsCategory.objects.all()

    return render(request, 'news/news_list.html', {
        'news_list': news_list,
        'categories': categories,
        'query': query,
        'selected_category': category_id
    })


def news_detail_view(request, slug):
    """
    Tekil haber detay sayfası.
    """
    news = get_object_or_404(NewsArticle, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news})
