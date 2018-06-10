from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    #index,post_list 皆為首頁, view為個別文章的頁面, category為特定分類的文章列表, (new add save update)
    url(r'^$', views.index, name='index'),
    # url(r'^category/$', views.category, name='category'),
    url(r'^view/$', views.view, name='view'),
    # url(r'^view/(?P<p_id>[0-9]+)/post_comment/$', views.post_comment, name='post_comment'), 
    url(r'^shop1/$', views.shop1, name='shop1'),
    url(r'^shop2/$', views.shop2, name='shop2'),
    url(r'^shop3/$', views.shop3, name='shop3'),
    ]
urlpatterns += staticfiles_urlpatterns()