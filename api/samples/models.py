from django.db import models
from django.conf import settings


class Sample(models.Model):
    class Meta:
        managed = False
        db_table = "Samples"

    sample_id = models.AutoField(primary_key=True, db_column="SampleId")
    comercial_name = models.CharField(max_length=255, db_column="ComercialName")
    product_brand = models.CharField(max_length=255, db_column="ProductBrand")
    batch_code = models.CharField(max_length=255, db_column="BatchCode")
    production_date = models.DateField(db_column="ProductionDate")
    expiration_date = models.DateField(db_column="ExpirationDate")
    quantity_units = models.IntegerField(db_column="QuantityUnits")
    is_rejected = models.BooleanField(db_column="IsRejected")
    origin_country = models.CharField(max_length=255, db_column="OriginCountry")
    collection_date = models.DateField(db_column="CollectionDate")
    temperature = models.FloatField(db_column="Temperature")
    special_conditions = models.TextField(blank=True, db_column="SpecialConditions")
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="UserId"
    )
    is_request = models.BooleanField(default=True, db_column="IsRequest")

    # Relaciones muchos a muchos
    categorys = models.ManyToManyField(
        "categorys.Category", through="categorys.CategorySample"
    )
    subcategorys = models.ManyToManyField(
        "subcategorys.Subcategory", through="subcategorys.SubcategorySample"
    )

    def __str__(self):
        return self.comercial_name
