__author__ = 'Bertrand'

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mezzanine.pages.models import Page
from league_manager.models.general_post import GeneralPost
from league_manager.models.pages.general_page import GeneralPage
from league_manager.serializer import PageSerializer
from league_manager.serializer import GeneralPostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def post_content(request, slug, format = None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post = GeneralPost.objects.get(slug=slug)
    except Page.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = GeneralPostSerializer(post)
    return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def post(request, format = None):
    """
    Retrieve, update or delete a post
    """
    if request.method == 'GET':
        post = GeneralPost.objects.all()
        serializer = GeneralPostSerializer(post, many=True)
        return Response(serializer.data)