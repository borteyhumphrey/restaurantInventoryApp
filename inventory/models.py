from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(verbose_name='Name', max_length=200)
    quantity = models.DecimalField(decimal_places=1, max_digits=4)
    unit = models.CharField(verbose_name='Unit', max_length=200)
    unit_price = models.DecimalField(verbose_name='Unit Price', decimal_places=2, max_digits=3)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
       return f"""
       name = {self.name};
       quantity = {self.name};
       unit = {self.unit};
       unit_price = {self.unit_price}
       """

class MenuItem(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=3)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"title={self.title}; price={self.price}"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=1, max_digits=3)

    def __str__(self):
        return f"menu_item = [{self.menu_item.__str__()}]; ingredient = {self.ingredient.name}; quantity = {self.quantity}"

    def get_absolute_url(self):
        return "/menu"

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"menu_item = [{self.menu_item.__str__()}]; time = {self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"
    