from django.contrib import admin
from .models import Quiz,Quiz1,Quiz9,Quiz8,Quiz10,Quiz6,Quiz7,Quiz4,Quiz5,Quiz3,Quiz2

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id','no','qns','ans')

class Quiz1Admin(admin.ModelAdmin):
    list_display = ('id','n1','qns1','ans1')

class Quiz2Admin(admin.ModelAdmin):
    list_display = ('id','n2','qns2','ans2')

class Quiz3Admin(admin.ModelAdmin):
    list_display = ('id','n3','qns3','ans3')
class Quiz4Admin(admin.ModelAdmin):
    list_display = ('id','n4','qns4','ans4')
class Quiz5Admin(admin.ModelAdmin):
    list_display = ('id','n5','qns5','ans5')
class Quiz6Admin(admin.ModelAdmin):
    list_display = ('id','n6','qns6','ans6')
class Quiz7Admin(admin.ModelAdmin):
    list_display = ('id','n7','qns7','ans7')
class Quiz8Admin(admin.ModelAdmin):
    list_display = ('id','n8','qns8','ans8')
class Quiz9Admin(admin.ModelAdmin):
    list_display = ('id','n9','qns9','ans9')
class Quiz10Admin(admin.ModelAdmin):
    list_display = ('id','n10','qns10','ans10')




admin.site.register(Quiz,QuizAdmin)
admin.site.register(Quiz1,Quiz1Admin)
admin.site.register(Quiz2,Quiz2Admin)
admin.site.register(Quiz3,Quiz3Admin)
admin.site.register(Quiz4,Quiz4Admin)
admin.site.register(Quiz5,Quiz5Admin)
admin.site.register(Quiz6,Quiz6Admin)
admin.site.register(Quiz7,Quiz7Admin)
admin.site.register(Quiz8,Quiz8Admin)
admin.site.register(Quiz9,Quiz9Admin)
admin.site.register(Quiz10,Quiz10Admin)









