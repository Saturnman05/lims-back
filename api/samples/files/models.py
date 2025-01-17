from django.db import models
from ..models import Sample


class File(models.Model):
    class Meta:
        managed = False
        db_table = "Files"

    file_id = models.AutoField(primary_key=True, db_column="FileId")
    certificado_registro_mercantil = models.BooleanField(
        db_column="CertificadoRegistroMercantil"
    )
    poder_representacion = models.BooleanField(db_column="PoderRepresentacion")
    certificado_marca = models.BooleanField(db_column="CertificadoMarca")
    permiso_sanitario = models.BooleanField(db_column="PermisoSanitario")
    contrato_fabricacion = models.BooleanField(db_column="ContratoFabricacion")
    contrato_acondicionamiento = models.BooleanField(
        db_column="ContratoAcondicionamiento"
    )
    listado_ingredientes = models.BooleanField(db_column="ListadoIngredientes")
    analisis_original_producto = models.BooleanField(
        db_column="AnalisisOriginalProducto"
    )
    analisis_original_materiales = models.BooleanField(
        db_column="AnalisisOriginalMateriales"
    )
    estudio_estabilidad = models.BooleanField(db_column="EstudioEstabilidad")
    especificacion_empaque = models.BooleanField(db_column="EspecificacionEmpaque")
    diagrama_flujo = models.BooleanField(db_column="DiagramaFlujo")
    arte_etiqueta = models.BooleanField(db_column="ArteEtiqueta")
    recibo_pago_servicios = models.BooleanField(db_column="ReciboPagoServicios")
    sample_id = models.ForeignKey(
        Sample, on_delete=models.CASCADE, db_column="SampleId"
    )
