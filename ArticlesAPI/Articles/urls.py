# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from .views import home, ArticlesViewSet
from Articles import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^$', home, name='home'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    url(r'^articles/$', views.article_list),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.article_detail),
    url(r'^articles/vote/(?P<pk>[0-9]+)/$', views.article_vote),
    url(r'^articles/order/$', views.article_list_desc),
    url(r'^create/article/$', views.create_article)
]
