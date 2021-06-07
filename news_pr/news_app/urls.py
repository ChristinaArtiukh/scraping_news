from django.urls import path
from .views import home_view, news_page_view

urlpatterns = [
    path('', home_view, name='home'),
    path('news/<name>', news_page_view, name='news_page')

]
