"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views import (
    list_book_view,
    add_book,
    book_update_view,
    book_delete_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_book_view, name='list-book'),
    path('book/add/', add_book, name="add-book"),
    path('update/', book_update_view, name='update-book'),
    path('delete/', book_delete_view, name='delete-book')
]
