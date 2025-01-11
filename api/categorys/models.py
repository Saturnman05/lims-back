from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column="CategoryId")
    category_name = models.CharField(max_length=255, db_column="CategoryName")

    class Meta:
        managed = False
        db_table = "Categorys"

    def __str__(self):
        return self.category_name
