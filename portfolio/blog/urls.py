from django.urls import path
import blog.views as views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.single_blog, name='single_blog')
]
