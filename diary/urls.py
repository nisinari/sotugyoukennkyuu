from django.urls import path
from . import views
app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('user_login/', views.User_LoginView.as_view(), name='user_login'),
    path('company_login/', views.Company_LoginView.as_view(), name='company_login'),
    path('user_entry/', views.User_EntryView.as_view(), name='user_entry'),
    path('user_detail/', views.User_DetailView.as_view(), name='user_detail'),
    path('company_entry/', views.Company_EntryView.as_view(), name='company_entry'),
    path('company_detail/', views.Company_DetailView.as_view(), name='company_detail'),
    path('service_entry/', views.Service_EntryView.as_view(), name='service_entry'),
    path('service_detail/', views.Service_DetailView.as_view(), name='service_detail'),
    path('post_entry/', views.Post_EntryView.as_view(), name='post_entry'),
    path('post_detail/', views.Post_DetailView.as_view(), name='post_detail'),
    path('post_finish/', views.Post_FinishView.as_view(), name='post_finish'),
    path('after_login/', views.After_LoginView.as_view(), name='after_login'),
# {% url 'diary:' %}
]



'''
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),

]
'''