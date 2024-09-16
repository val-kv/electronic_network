from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
        Пользовательская модель, которая наследуется от AbstractUser Django.

        Эта модель может быть использована для добавления пользовательских полей или поведения к модели пользователя по умолчанию.
        """
    pass

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Supplier(models.Model):
    """
        Представляет поставщика в сети.

        Атрибуты:
            name (str): Имя поставщика.
            debt (Decimal): Долг поставщика, с максимальной длиной 10 цифр и 2 десятичными знаками.
        """
    name = models.CharField(max_length=255)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    """
        Представляет узел в сети.

        Атрибуты:
            LEVELS (кортеж): Кортеж кортежей, содержащий различные уровни сети.
            name (строка): Имя узла сети.
            email (строка): Электронный адрес узла сети.
            country (строка): Страна, где находится узел сети.
            city (строка): Город, где находится узел сети.
            street (строка): Адрес узла сети.
            house_number (строка): Номер дома узла сети.
            products (список): Список продуктов, связанных с узлом сети.
            supplier (Supplier): Поставщик, связанный с узлом сети.
            debt_to_supplier (Decimal): Долг перед поставщиком.
            creation_time (DateTime): Время создания узла сети.
            level (целое число): Уровень узла сети.
        """
    LEVELS = (
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Entrepreneur'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    products = models.JSONField()  # Store a list of products
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(choices=LEVELS)

    def __str__(self):
        return self.name


class Address(models.Model):
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.postal_code}, {self.country}, {self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Network(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
