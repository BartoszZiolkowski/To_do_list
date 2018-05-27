from django.contrib import admin
from .models import Category, Task


# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        'name',
        'color'
    )
    search_fields = (
        'name',
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass