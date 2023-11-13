from . import views
from django.urls import path

urlpatterns = [
    path('miblog/', views.PostList.as_view(), name='miblog-index'),
    path('miblog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]