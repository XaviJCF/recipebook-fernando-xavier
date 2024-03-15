from django.db import models
from django.urls import reverse

# Create your models here.




class Ingredient(models.Model):
    name = models.CharField(max_length = 100, )

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100, null = True, blank = True)
    created_on = models.DateTimeField(null = False, auto_now_add = True)
    update_on = models.DateTimeField(null = True, auto_now = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe', args = [str(self.name)])
    
    
class RecipeIngredient(models.Model):
    quantity = models.FloatField(default = 0)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'recipe',
    )
    
    recipe = models.ForeignKey(
        Recipe,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'ingredients',
    )