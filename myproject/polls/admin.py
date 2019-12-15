from django.contrib import admin
# from django.contrib import admin
# #from myapp.models import employees
from polls.models import Poll,Choice,Vote,Publication,Article,UserArticle,UserPublication,Author,Book,Position,ToppingAmount,level_3,Pizza,Topping,level_2,level_4
#
 #admin.site.register(employees)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(UserPublication)
admin.site.register(UserArticle)
admin.site.register(level_3)
admin.site.register(level_2)
admin.site.register(level_4)
admin.site.register(Position)
admin.site.register(Pizza)
admin.site.register(Author)
admin.site.register(Book)
