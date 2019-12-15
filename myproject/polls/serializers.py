from rest_framework import serializers
from .models import Poll, Choice, Vote,Match, Sport,Book,Author, Market, Selection,UserArticle,UserPublication,Exercise,Module,Lesson,Position,level_3,level_2,level_4

from django.db import transaction



class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = '__all__'

class UserPublicationSerializer(serializers.ModelSerializer):
    #choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = UserPublication
        fields = ('id','title')
class level_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = level_2
        fields = '__all__'


class level_3Serializer(serializers.ModelSerializer):
    level_2 = level_2Serializer(read_only=True, many=False)
    class Meta:
        model = level_3
        fields = '__all__'

class level_4Serializer(serializers.ModelSerializer):
    level_3 = level_3Serializer(read_only=True, many=False)
    class Meta:
        model = level_4
        fields = '__all__'



class PositionSerializer(serializers.ModelSerializer):
    level_4 = level_4Serializer(read_only=True, many=True)
    class Meta:
        model = Position
        fields = '__all__'

class UserArticleSerializer(serializers.ModelSerializer):

    publications = UserPublicationSerializer(read_only=True, many=True)
    #position = PositionSerializer(read_only=True, many=True)
    position = serializers.RelatedField(source='Position', read_only=True)
    class Meta:
        model = UserArticle
        fields = '__all__'

class Positions2Serializer(serializers.ModelSerializer):
    level_4 = level_4Serializer(read_only=True, many=False)
   # rritws = UserArticle1Serializer(many=True, read_only=True)
    class Meta:
        model = Position
        fields = ['types','level_4']


class UserArticle1Serializer(serializers.ModelSerializer):

    #position = serializers.RelatedField(source='Position', read_only=True)
    position = Positions2Serializer(many=False, read_only=True)

    employeetitles = serializers.PrimaryKeyRelatedField(queryset=UserPublication.objects.all(), many=False)
    #queryset = UserPublication.objects.all()
    #print("kkkkkkkkkk")
    #employeetitles = UserPublicationSerializer(queryset, many=True)

    class Meta:
        model = UserArticle
        fields = ['id','employeetitles','headline','position','publicatins']


class PositionsSerializer(serializers.ModelSerializer):
    level_4 = level_4Serializer(read_only=True, many=True)
    rritws = UserArticle1Serializer(many=True, read_only=True)
    class Meta:
        model = Position
        fields = '__all__'


class UserPublication1Serializer(serializers.ModelSerializer):
    level_4 = level_4Serializer(read_only=True, many=True)
    rritws = UserArticle1Serializer(many=True, read_only=True)
    #title = UserArticle1Serializer(many=False, read_only=True)
    #choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = UserPublication
        fields = '__all__'

    #def get_lessons(self, obj):
    #    return UserArticle1Serializer(obj.rritws.all().order_by('index'), many=True, read_only=True).data


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
class LessonSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = '__all__'

    def get_exercises(self, obj):
        qs = obj.exercises.all().order_by('index')
        return ExerciseSerializer(qs, many=True, read_only=True).data

class ModuleSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Module
        fields = '__all__'

    def get_lessons(self, obj):
        return LessonSerializer(obj.lessons.all().order_by('index'), many=True, read_only=True).data


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name')
class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('id', 'name', 'odds')
class MarketSerializer(serializers.ModelSerializer):
    selections = SelectionSerializer(many=True)
    class Meta:
        model = Market
        fields = ('id', 'name','selections')

class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime')
class MatchDetailSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    market = MarketSerializer()
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime', 'sport', 'market')


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),many=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'published', 'authors')


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'last_name', 'book_list')