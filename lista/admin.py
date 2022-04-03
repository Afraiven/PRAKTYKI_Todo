from django.contrib import admin
from .models import Todo, Projekt
from django.contrib.auth.models import User

class TodoAdmin(admin.ModelAdmin):
    pass

class ProjektAdmin(admin.ModelAdmin):
    pass
    
    
class ChannelAdmin(admin.TabularInline):
    model = Todo
    extra = 0

class RuleAdmin(admin.ModelAdmin):
   inlines = [ChannelAdmin,]

admin.site.unregister(User)
admin.site.register(User,RuleAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Projekt, ProjektAdmin)
