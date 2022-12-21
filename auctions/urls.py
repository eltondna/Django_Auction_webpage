from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #action 
    path("create", views.create, name="create"),
    path("item_info/<int:item_id>", views.item_info,name="item_info"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("close",views.close,name='close')

]
