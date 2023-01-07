from django.shortcuts import render
from . models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . forms import IngredientCreate, IngredientUpdate, IngredientDelete, MenuCreate, PurchaseCreate, RecipeRequirementCreate



def home(request):
    return render(request, "inventory/home.html")

# Create your views here.
class IngredientList(ListView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"

class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/ingredients_create.html"
    form_class = IngredientCreate
    success_url = "/ingredients"

class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredients_update.html"
    form_class = IngredientUpdate
    success_url = "/ingredients"

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"
    success_url = "/ingredients"

class PurchasesList(ListView):
    model = Purchases
    template_name = "inventory/purchases_list.html"

class PurchasesCreateView(CreateView):
    model = Purchases
    template_name = "inventory/purchases_create.html"
    form_class = PurchaseCreate
    success_url = "/purchases"

class MenuCreateView(CreateView):
    model = MenuItem
    template_name = "inventory/menu_create.html"
    form_class = MenuCreate
    success_url = "/menu"

class MenuList(ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"

class RecipeRequirementView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/recipe_requirement_create.html"
    form_class = RecipeRequirementCreate
    success_url = "/menu"