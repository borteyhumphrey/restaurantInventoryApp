from dataclasses import fields
from pyexpat import model
from django import forms
from . models import Ingredient, MenuItem, RecipeRequirement, Purchases

class IngredientCreate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class IngredientUpdate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuCreate(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class PurchaseCreate(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = ["menu_item"]

class RecipeRequirementCreate(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'