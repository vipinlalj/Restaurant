from django.contrib import admin
from django.urls import path
from RestaurantApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('AddCat/', views.AddCat, name="AddCat"),
    path('SaveCat/', views.SaveCat, name="SaveCat"),
    path('ViewCat/', views.ViewCat, name="ViewCat"),
    path('editCat/<int:cat_id>/', views.editCat, name="editCat"),
    path('updateCat/<int:cat_id>/', views.updateCat, name="updateCat"),
    path('deleteCat/<int:cat_id>/', views.deleteCat, name="deleteCat"),


    path('AddFood/', views.AddFood, name="AddFood"),
    path('SaveFood/', views.SaveFood, name="SaveFood"),
    path('ViewFood/', views.ViewFood, name="ViewFood"),
    path('editFood/<int:f_id>/', views.editFood, name="editFood"),
    path('updateFood/<int:f_id>/', views.updateFood, name="updateFood"),
    path('deleteFood/<int:f_id>/', views.deleteFood, name="deleteFood"),

    path('AdminLogin/', views.AdminLogin, name="AdminLogin"),
    path('Admin_login/', views.Admin_login, name="Admin_login"),

]
