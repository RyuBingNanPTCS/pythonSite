from django.contrib import admin
from .models import User
from .models import Category
from .models import Product
from .models import UserInfo

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= [
        'pk',
        'username',
        'realname',
        'py',
        'email',
        'password',
    ]
    fieldsets = (
        
    )
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserInfo)