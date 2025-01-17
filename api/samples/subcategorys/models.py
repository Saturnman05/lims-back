from django.db import models


class Subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True, db_column="SubcategoryId")
    subcategory_name = models.CharField(max_length=255, db_column="SubcategoryName")

    class Meta:
        managed = False
        db_table = "Subcategorys"

    def __str__(self):
        return self.subcategory_name


class SubcategorySample(models.Model):
    class Meta:
        managed = False
        db_table = "SubcategorySample"

    Subcategory = models.ForeignKey(
        "subcategorys.Subcategory", on_delete=models.CASCADE, db_column="SubcategoryId"
    )
    Sample = models.ForeignKey(
        "samples.Sample", on_delete=models.CASCADE, db_column="SampleId"
    )
