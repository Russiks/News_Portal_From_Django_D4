from django.urls import path
# from django.urls.resolvers import URLPattern
from django.urls import path
from .views import (
    PostList, PostDetail, PostSearch, PostCreate, NewsCreate, PostUpdate, NewsUpdate, PostDelete, NewsDelete
)  # Импортируем представления, написанные в файле "views.py"

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),  # pk — это первичный ключ новости или статьи,
    # который будет выводиться у нас в шаблон int — указывает на то, что принимаются только целочисленные значения
    path('search/', PostSearch.as_view(), name='posts_search'),
    path('articles/create/', PostCreate.as_view(), name='post_create'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]
# Path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, чуть позже станет ясно почему.
# Т.к. наше объявленное представление является классом, а Django ожидает функцию, нам надо представить этот класс в
# виде view. Для этого вызываем метод f as_view.