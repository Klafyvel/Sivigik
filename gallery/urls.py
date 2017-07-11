from django.conf.urls import url

from gallery.views import GalleryView, ImageView

app_name = "gallery"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', ArticleView.as_view(), name='article-detail-pk'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<slug>(\w|-)+)/$', ArticleView.as_view(), name='article-detail-wp'),
    url(r'^categorie/(\w+)/$', IndexView.as_view(), name='article-category'),
    url(r'^page-auteurs/$', AuthorView.as_view(), name='author'),
]