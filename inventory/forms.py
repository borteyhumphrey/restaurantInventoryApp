from django import forms
from . models import Ingredient, MenuItem, RecipeRequirement, Purchases

class IngredientCreate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class IngredientUpdate(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuCreate(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price':forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PurchaseCreate(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = ["menu_item"]

        widgets = {
            'menu_item':forms.Select(attrs={'class': 'form-control'}),
        }

class RecipeRequirementCreate(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'

        widgets = {
            'menu_item':forms.Select(attrs={'class': 'form-control'}),
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }