from django.shortcuts import render
from article.models import Article, Part
from staticContent.models import StaticContent
from home.models import Category

def search_Category(value):
    r = []
    c = Category.objects.all()
    for i in c:
        if str(i.displayed_name).lower() == str(value).lower() or str(i.name).lower() == str(value).lower():
            r.append(i)
    return r

def search_site(value, **kwargs):
    """Search in the website.
    Arguments :
        - value         : What you're looking for
    Optionnal arguments:
        - type          : Can be 'article', 'category', 'profil', 'poll' (comming soon), 'static_page' 
        - category_name : If you're looking for an article, this option 
                          restrain your search to a specific category. 
                          A primary key is requiered."""
    r = {}
    r['categories'] = search_Category(value)
    return r

def search(request, **kwargs):
    try:
        searched = request.GET['q'].lower()
    except:
        searched = 'rien'
    r = search_site(searched)
    r['searched'] = searched
    return render(request, 'search/search.html', r)

def get_search(request):
    return render(request, 'search/get_search.html')

