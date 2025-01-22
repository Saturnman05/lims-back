from rest_framework import serializers

from .models import File

from ...utils import convert_to_snake_case


class FileSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        if type(data) == type([]):
            data = data[0]
        print("data ne to_internal_value:", data)
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

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
        ]
