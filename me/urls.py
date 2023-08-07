
from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.main, name="homepage"),
    path('about', views.about, name="about"),
    path('works', views.works, name="works"),
    path('shop', views.shop, name="shop"),
    path('django', views.django, name="django"),
    path('php', views.php, name="php"),
    path('htmlcss', views.htmlcss, name="htmlcss"),
    path('paid', views.paid, name="paid"),
    path('free', views.free, name="free"),
    
    path('comments', views.comments, name="comments"),
    path('comments_page', views.comments_page, name="comments_page"),
    
    
    path('counter/', views.counter, name='counter'),
]
