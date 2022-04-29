from django.contrib import admin
from .models import User
from .models import Category
from .models import Product
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