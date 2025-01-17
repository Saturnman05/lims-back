from rest_framework import serializers

from .models import File

from ..models import Sample

from ...utils import convert_to_snake_case


class SampleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    sample_id = serializers.PrimaryKeyRelatedField(queryset=Sample.objects.all())

    class Meta:
        model = File
        fields = [
            "file_id",
            "certificado_registro_mercantil",
            "poder_representacion",
            "certificado_marca",
            "permiso_sanitario",
            "contrato_fabricacion",
            "contrato_acondicionamiento",
            "listado_ingredientes",
            "analisis_original_producto",
            "analisis_original_materiales",
            "estudio_estabilidad",
            "especificacion_empaque",
            "diagrama_flujo",
            "arte_etiqueta",
            "recibo_pago_servicios",
            "sample_id",
        ]
