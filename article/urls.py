from django.conf.urls import url

from article.views import IndexView, ArticleView, AuthorView, EditView

app_name = "article"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', ArticleView.as_view(), name='article-detail-pk'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>(\w|-)+)/$', ArticleView.as_view(), name='article-detail-wp'),
    url(r'^categorie/(\w+)/$', IndexView.as_view(), name='article-category'),
    url(r'^page-auteurs/$', AuthorView.as_view(), name='author'),
    url(r'^edit/(?P<slug>(\w|-)+)/$', EditView.as_view(), name='edit'),
]