from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('', views.home, name="home"),
    path("ingredients/", views.IngredientList.as_view(), name="ingredientlist"),
    path("ingredients/create", views.IngredientCreateView.as_view(), name="ingredientcreate"),
    path("ingredients/update/<pk>", views.IngredientUpdateView.as_view(), name="ingredientupdate"),
    path("ingredients/delete/<pk>", views.IngredientDeleteView.as_view(), name="ingredientdelete"),
    path("menu/create", views.MenuCreateView.as_view(),name="menucreate"),
    path("menu/", views.MenuList.as_view(), name="menulist"),
    path("purchases/create", views.PurchasesCreateView.as_view(), name="purchasecreate"),
    path("purchases/", views.PurchasesList.as_view(), name="purchaselist"),
    path("recipe/create", views.RecipeRequirementView.as_view(), name="recipecreate"),
    path("report/", views.ReportView.as_view(), name="report"),
]