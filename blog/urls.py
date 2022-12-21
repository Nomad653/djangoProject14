from .views import PostList, ShowPost
from django.urls import include, path
urlpatterns = [
    path("home/",PostList.as_view()),
    path("<slug:slug>",ShowPost.as_view())
]