from django.contrib import admin

# Register your models here.
from .models import MainMenu
from .models import Book
from .models import Event
from .models import ForumPost
from .models import ShoppingCart

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Event)
admin.site.register(ForumPost)
admin.site.register(ShoppingCart)