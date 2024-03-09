from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

# Register your models here.
# ADMIN DETAILS
# USERNAME: xavi
# PASSWORD: recipebookpw

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    inlines = [RecipeIngredientInline, ]

    search_fields = ('name', )


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)




