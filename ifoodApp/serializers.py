from rest_framework import serializers
from .models import Usuario, Endereco, EnderecoEntrega, CodVerif


class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class Endereco_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class EnderecoEntrega_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoEntrega
        fields = "__all__"


class CodVerif_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CodVerif
        fields = "__all__"