from django.db import models
from ..models import Sample


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column="CategoryId")
    category_name = models.CharField(max_length=255, db_column="CategoryName")

    class Meta:
        managed = False
        db_table = "Categorys"

    def __str__(self):
        return self.category_name


class CategorySample(models.Model):
    class Meta:
        managed = False
        db_table = "CategorySample"

    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_column="CategoryId"
    )
    Sample = models.ForeignKey(Sample, on_delete=models.CASCADE, db_column="SampleId")
