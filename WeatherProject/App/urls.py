from django.contrib import admin
from django.urls import path
from App import views

admin.site.site_header = "ADMIN PORTAL"
admin.site.site_title = "ZAHEER Admin Portal"
admin.site.index_title = "Welcome to weather forecast Website Portal"

urlpatterns = [
    # path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('home', views.home, name='home'),
    path('', views.userLogin, name='userLogin'),
    path('showTables', views.showTables, name='showTables'),
    path('delete/<int:id>/', views.deleteRow, name='deleteRow'),
    path('deleteHistory/<int:id>/', views.deleteHistoryRow, name='deleteHistoryRow'),
    path('deleteJoin/<int:id>/', views.deleteJoin, name='deleteJoin'),
]
