from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . forms import IngredientCreate, IngredientUpdate, MenuCreate, PurchaseCreate, RecipeRequirementCreate

@login_required
def home(request):
    return render(request, "inventory/home.html")

def logout_view(request):
    logout(request)
    return redirect("home")

# Create your views here.
class IngredientList(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"

class IngredientCreateView(LoginRequiredMixin,CreateView):
    model = Ingredient
    template_name = "inventory/ingredients_create.html"
    form_class = IngredientCreate
    success_url = "/ingredients"

class IngredientUpdateView(LoginRequiredMixin,UpdateView):
    model = Ingredient
    template_name = "inventory/ingredients_update.html"
    form_class = IngredientUpdate
    success_url = "/ingredients"

class IngredientDeleteView(LoginRequiredMixin,DeleteView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"
    success_url = "/ingredients"

class PurchasesList(LoginRequiredMixin,ListView):
    model = Purchases
    template_name = "inventory/purchases_list.html"

class PurchasesCreateView(LoginRequiredMixin,CreateView):
    model = Purchases
    template_name = "inventory/purchases_create.html"
    form_class = PurchaseCreate
    success_url = "/purchases"

class MenuCreateView(LoginRequiredMixin,CreateView):
    model = MenuItem
    template_name = "inventory/menu_create.html"
    form_class = MenuCreate
    success_url = "/menu"

class MenuList(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"

class RecipeRequirementView(LoginRequiredMixin,CreateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_create.html"
    form_class = RecipeRequirementCreate
    success_url = "/menu"