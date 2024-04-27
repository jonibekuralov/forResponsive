from django.urls import path

from .views import news_list, news_detail, homePageView, ContactPageView, search_view, CalendarPageView, LocationView, \
    NewsCreateView, NewsUpdtaeView, NewsDeleteView, admin_page

urlpatterns = [
    path('', homePageView, name="home_list"),
    path('adminpage/', admin_page, name='admin_page'),
    path('news/', news_list, name="all_news_list"),
    path('news/<slug:news>/', news_detail, name="news_detail_page"),
    path('news/<slug>/edit/', NewsUpdtaeView.as_view(), name='news_update'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact/', ContactPageView.as_view(), name="contact_page"),
    path('searchresult/', search_view, name="search_results"),
    path('calendar/', CalendarPageView, name="calendar"),
    path('location/', LocationView.as_view(), name="location"),

]
