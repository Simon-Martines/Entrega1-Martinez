from . import views
from django.urls import path

urlpatterns = [
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/', views.PostList.as_view(), name='miblog-index'),
]