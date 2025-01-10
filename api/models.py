from django.db import models
from django.contrib.auth.hashers import check_password


class User(models.Model):

    class Meta:
        managed = False
        db_table = "Users"

    UserId = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=255)
    UserName = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    Cedula = models.CharField(max_length=11)
    Email = models.EmailField(max_length=255, null=True, blank=True)
    Phone = models.CharField(max_length=12, null=True, blank=True)
    Active = models.BooleanField(null=True, blank=True)
    RNC = models.CharField(max_length=20, null=True, blank=True)
    ComercialCompanyName = models.CharField(max_length=255, null=True, blank=True)
    CompanyName = models.CharField(max_length=255, null=True, blank=True)
    IsMaster = models.BooleanField(null=True, blank=True)

    USERNAME_FIELD = "UserName"
    REQUIRED_FIELDS = ["FullName", "Cedula"]

    def __str__(self):
        return self.UserName

    # Es necesario definir este método para que funcione la autenticación
    def check_password(self, raw_password):
        return check_password(raw_password, self.Password)
