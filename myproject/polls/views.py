#from django.http import Http404
from django.http import Http404
from django.http import HttpResponse,Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import admin
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.filters import OrderingFilter
from polls.models import Poll,Author,Book, Choice,Publication,Article,UserPublication,UserArticle,Position,Match, Sport, Selection, Market
from .serializers import PollSerializer,ChoiceSerializer,AuthorSerializer,VoteSerializer,UserArticleSerializer,MatchListSerializer, MatchDetailSerializer,UserPublication1Serializer, UserPublicationSerializer
#from .serializers import employeesSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import routers, serializers, viewsets

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
#from django_filters import rest_framework as filters

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# ...
from django.contrib.auth import authenticate
class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        print(request.data.get("username"))
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"})
#######################Json data
def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()
    data = {"results": list(polls.values("question", "created_by__username","pub_date"))}
    return JsonResponse(data)

def polls_detail(request, id):
    poll = get_object_or_404(Poll, pk=id)
    data = {"results": {
    "question": poll.question,
    "created_by": poll.created_by.username,
    "pub_date": poll.pub_date
    }}
    return JsonResponse(data)



################Creating Views with APIView

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.get_queryset.get('question'):
            return ['question']
        return super(CustomSearchFilter, self).get_search_fields(view, request)

class PollList(APIView):
    filter_backends = (CustomSearchFilter,)
    search_fields = ['question']

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.
        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        #print(Poll.objects.all().get('question'))
        return Poll.objects.all()

    def get(self, request):
        print(request.data)
        #print(self.get_queryset)

        filter_backends = (CustomSearchFilter,)
        polls = self.get_queryset()
        #polls = Poll.objects.all()
        #print(polls.values('question'))
        data = PollSerializer(polls, many=True).data
        search_fields = ['question']
        return Response(data)

class PollDetail(APIView):
    def get(self, request, id):
        poll = get_object_or_404(Poll, pk=id)
        data = PollSerializer(poll).data
        return Response(data)


####################generics Views
class ProductList(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    search_fields = ['question','choices__choice_text','choices__votes__votername']

class PollListgenerics(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    search_fields = ['question','choices__choice_text','choices__votes__votername']

class PollDetailgenerics(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

#####################viewsets//////////

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Poll.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(user)
        return Response(serializer.data)


class PollViewSet(ModelViewSet):
    filter_backends = [filters.SearchFilter]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    search_fields = ['question','choices__choice_text','choices__votes__votername']
    #print(serializer.data)
    #def list(self, request,id):
    #     if id !='':
    #         users = Poll.objects.filter(pk=id)
    #     else:
    #         users = Poll.objects.all()
    #     serializer = PollSerializer(users, many=True)
    #     return Response(serializer.data)
    #return Response(serializer.data)
class PollpublicSet(ModelViewSet):
    queryset = UserPublication.objects.all()
    print(UserPublication.objects.filter(userarticle__id=1).values())
    serializer_class = UserPublicationSerializer

def particle_list(request):
    queryset = UserPublication.objects.all().values()

        #print(xxx)
    #return Response(serializers.data)
    return HttpResponse("html")
    #return JsonResponse(serializers.data)


class voterlist(APIView):

    def get(self, request):
        users = UserArticle.objects.all()
        #print(users.values)
        serializer = UserArticleSerializer(users, many=True)
        return Response(serializer.data)


class voter1list(APIView):

    def get(self, request):
        users = Author.objects.all()
        #print(users.values)
        serializer = AuthorSerializer(users, many=True)
        return Response(serializer.data)




