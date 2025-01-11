from django.db import models


class Allergens(models.Model):
    allergen_id = models.AutoField(primary_key=True, db_column="AllergenId")
    allergen_name = models.CharField(max_length=255, db_column="AllergenName")

    class Meta:
        managed = False
        db_table = "Allergens"

    def __str__(self):
        return self.allergen_name


class AllergenSample(models.Model):
    class Meta:
        managed = False
        db_table = "AllergenSample"

    Allergen = models.ForeignKey(
        "allergens.Allergens", on_delete=models.CASCADE, db_column="AllergenId"
    )
    Sample = models.ForeignKey(
        "samples.Sample", on_delete=models.CASCADE, db_column="SampleId"
    )
