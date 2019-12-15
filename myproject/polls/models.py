from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choicevote = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    votername = models.CharField(max_length=100)


class level_2(models.Model):

    name = models.CharField(max_length=30)
    level_name_id = models.CharField(max_length=100)


class level_3(models.Model):

    level_2 = models.ForeignKey(level_2,  on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    level_name_id = models.CharField(max_length=100)

class level_4(models.Model):

    level_3 = models.ForeignKey(level_3,  on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    level_name_id = models.CharField(max_length=100)

class Position(models.Model):
    level_3 = models.ForeignKey(level_3,  on_delete=models.CASCADE)
    level_2 = models.ForeignKey(level_2,  on_delete=models.CASCADE)
    level_4 = models.ForeignKey(level_4,  on_delete=models.CASCADE)
    types = models.CharField(max_length=100)

    def __str__(self):
        return '%s: %s' % (self.level_4, self.types)


class Publication(models.Model):
    #poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)


class Tpublication(models.Model):
    title = models.CharField(max_length=30)


class Article(models.Model):
    employeetitles = models.ForeignKey(Tpublication, related_name='titws', on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)


class UserPublication(models.Model):
    title = models.CharField(max_length=30)

    def natural_key(self):
        return (self.title)

    class Meta:
        ordering = ('id',)


class UserArticle(models.Model):

    position = models.ForeignKey(Position, related_name='positionss', on_delete=models.CASCADE)
    employeetitles = models.ForeignKey(UserPublication,  on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    publicatins = models.ManyToManyField(UserPublication,related_name='rritws', blank=True)

    class Meta:
        ordering = ('id',)

    @property
    def a_property_method(self,id):
        return "I am a Property Method"

    def an_instance_method(self,id):
        return "I am a Instance Method"

    @property
    def position_name(self):
        return self.position.types

class UserArti(models.Model):

    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employeetitles = models.ForeignKey(UserPublication, related_name='jkk', on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(UserPublication)    


class Module(models.Model):
   
    title = models.CharField(max_length=255, default='')
    #course = models.ForeignKey(OnlineCourse, on_delete=models.CASCADE, null=True, related_name="modules")

class Lesson(models.Model):
    
    title = models.CharField(max_length=255, default='')
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, related_name="lessons")

class Exercise(models.Model):
    """
    A specific exercise for a lesson
    """
    TYPES = (
        ('vid', 'Video'),
        ('mcq', 'Multiple Choice Quiz'),
        ('fib', 'Fill in Blank'),
        ('text', 'Text Lesson')
    )
    type = models.CharField(max_length=255, default='video', choices=TYPES)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, related_name="exercises")



class Sport(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return self.name

class Market(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport,related_name='markets', on_delete =models.CASCADE)    
    def __str__(self):
        return self.name + ' | ' + self.sport.name

class Selection(models.Model):
    name = models.CharField(max_length=100)
    odds = models.FloatField()
    market = models.ForeignKey(Market,related_name='selections', on_delete =models.CASCADE)   

    def __str__(self):
        return self.name

class Match(models.Model):
    name = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    sport = models.ForeignKey(Sport, related_name='matches', on_delete =models.CASCADE)
    market = models.ForeignKey(Market, related_name='matches', on_delete =models.CASCADE)  
    class Meta:
        ordering = ('startTime',)
        verbose_name_plural = 'Matches'    
        def __str__(self):
            return self.name


class Pizza(models.Model):

    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping', related_name='pizzas')

    def __str__(self):
        return self.name


class Topping(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class ToppingAmount(models.Model):

    REGULAR = 1
    DOUBLE = 2
    TRIPLE = 3
    AMOUNT_CHOICES = (
        (REGULAR, 'Regular'),
        (DOUBLE, 'Double'),
        (TRIPLE, 'Triple'),
    )

    pizza = models.ForeignKey('Pizza', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
    topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)



class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    last_name = models.IntegerField(default=0)

    def __str__(self):
        return self.name+"-"+str(self.id)

class Book(models.Model):
    authors = models.ManyToManyField(Author, related_name="book_list", blank=True)
    name = models.CharField(max_length=100, default="")
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name+"-"+str(self.id)
