from rest_framework import serializers
from .models import Supplier, NetworkNode


class SupplierSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели Supplier.

        Этот сериализатор используется для преобразования модели Supplier в формат JSON.
        Он включает поля 'id', 'name' и 'debt'. Поле 'debt' доступно только для чтения.
        """
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'debt']
        read_only_fields = ['debt']


class NetworkNodeSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели NetworkNode.

        Этот сериализатор используется для преобразования экземпляров NetworkNode в JSON-данные и обратно.
        Он включает все поля из модели NetworkNode.
        """
    class Meta:
        model = NetworkNode
        fields = '__all__'
