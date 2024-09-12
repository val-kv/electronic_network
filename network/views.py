from rest_framework import viewsets, permissions
from .models import Supplier, NetworkNode
from .serializers import SupplierSerializer, NetworkNodeSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """
        Представление для управления поставщиками.

        Это представление обеспечивает CRUD-операции для поставщиков и требует аутентификации.
        """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
        Представление для управления экземплярами NetworkNode.

        Это представление предоставляет операции CRUD для экземпляров NetworkNode,
        с фильтрацией по стране.
        """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
                Возвращает запрос для экземпляров NetworkNode, отфильтрованный по стране, если указано.

                :return: Запрос для экземпляров NetworkNode
                """
        queryset = super().get_queryset()
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(country=country)
        return queryset
