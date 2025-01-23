from django.db import models


class File(models.Model):
    class Meta:
        managed = False
        db_table = "Files"

    file_id = models.AutoField(primary_key=True, db_column="FileId")
    certificado_registro_mercantil = models.BooleanField(
        db_column="CertificadoRegistroMercantil", default=False
    )
    poder_representacion = models.BooleanField(
        db_column="PoderRepresentacion", default=False
    )
    certificado_marca = models.BooleanField(db_column="CertificadoMarca", default=False)
    permiso_sanitario = models.BooleanField(db_column="PermisoSanitario", default=False)
    contrato_fabricacion = models.BooleanField(
        db_column="ContratoFabricacion", default=False
    )
    contrato_acondicionamiento = models.BooleanField(
        db_column="ContratoAcondicionamiento", default=False
    )
    listado_ingredientes = models.BooleanField(
        db_column="ListadoIngredientes", default=False
    )
    analisis_original_producto = models.BooleanField(
        db_column="AnalisisOriginalProducto", default=False
    )
    analisis_original_materiales = models.BooleanField(
        db_column="AnalisisOriginalMateriales", default=False
    )
    estudio_estabilidad = models.BooleanField(
        db_column="EstudioEstabilidad", default=False
    )
    especificacion_empaque = models.BooleanField(
        db_column="EspecificacionEmpaque", default=False
    )
    diagrama_flujo = models.BooleanField(db_column="DiagramaFlujo", default=False)
    arte_etiqueta = models.BooleanField(db_column="ArteEtiqueta", default=False)
    recibo_pago_servicios = models.BooleanField(
        db_column="ReciboPagoServicios", default=False
    )
