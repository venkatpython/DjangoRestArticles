# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from Articles.serializers import ArticleSerializer
from Articles.models import Articles


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer


# Create your views here.
def home(request):
    return HttpResponse("Hey! I'm Ok")


class ArticlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Articles.objects.all().order_by('-created')
    serializer_class = ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    """
    Retrieve, update or delete a article.
    """
    try:
        article = Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)

def article_vote(request, pk):
    """
    Vote the Article
    :param request:
    :param pk:
    :return:
    """
    try:
        article = Articles.objects.get(pk=pk)
        article.vote = 1
        article.save()
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    except Articles.DoesNotExist:
        return HttpResponse(status=404)
