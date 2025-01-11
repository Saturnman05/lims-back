from django.db import models


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True, db_column="IngredientId")
    ingredient_name = models.CharField(max_length=255, db_column="IngredientName")

    class Meta:
        managed = False
        db_table = "Ingredients"

    def __str__(self):
        return self.ingredient_name
