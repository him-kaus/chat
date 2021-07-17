from django.contrib import admin
from .models._user import User1
from .models.profile import Profile
from .models.chatroom import USER,CHAT_MESSAGE


# Register your models here.

class AdminUser1(admin.ModelAdmin):
    # model = Product
    list_display = ['name1', 'phno', 'email', 'password']

class AdminUSER(admin.ModelAdmin):
    # model = Product
    list_display = ['userName']

class AdminCHAT_MESSAGE(admin.ModelAdmin):
    # model = Product
    list_display = ['messageText','author']

class AdminProfile(admin.ModelAdmin):
    # model = Product
    list_display = ['user', 'first_name', 'last_name', 'email', 'date_birth','bio']




admin.site.register(User1, AdminUser1)
admin.site.register(Profile,AdminProfile)
admin.site.register(USER,AdminUSER)
admin.site.register(CHAT_MESSAGE,AdminCHAT_MESSAGE)
