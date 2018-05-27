"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import index, categories, add_category, edit_category, delete_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('categories/', categories, name='categories-list'),
    path('add_category/', add_category, name='add_category'),
    path('edit_category/<int:category_id>', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>', delete_category, name='delete_category')
]


