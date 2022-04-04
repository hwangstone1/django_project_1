from django.shortcuts import render
from articleapp.models import Article
from django.db.models import Q
# Create your views here.

def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        results = Article.objects.all().filter(
            Q(writer__icontains=query) |
            Q(title_icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    return render(request, 'search.html', {'query':query, 'results': results})