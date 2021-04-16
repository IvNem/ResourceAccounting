from rest_framework import serializers

from ..models import Product


# класс для отображения продукта без стоимости
class ProductWithoutCost(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    amount = serializers.DecimalField(required=True, decimal_places=2, max_digits=7, coerce_to_string=False)
    unit = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, decimal_places=2, max_digits=7, coerce_to_string=False)
    date = serializers.DateField(required=True)

    # метакласс прикрепленный к модели продуктов
    class Meta:
        model = Product
        # отображение всех полей модели
        fields = '__all__'


# класс для отображения продукта с расчетом стоимости
class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    amount = serializers.DecimalField(required=True, decimal_places=2, max_digits=7, coerce_to_string=False)
    unit = serializers.CharField(required=True)
    price = serializers.DecimalField(required=True, decimal_places=2, max_digits=7, coerce_to_string=False)
    date = serializers.DateField(required=True)
    # вычисляемое поле для подсчета стоимости продукта с помощью метода
    cost = serializers.SerializerMethodField('get_cost', default=0, read_only=True)

    class Meta:
        model = Product
        # настройка отображения интересующих полей
        fields = [
            'id', 'title', 'amount', 'unit', 'price', 'cost', 'date'
        ]

    # методля для расчета стоимости продукта
    def get_cost(self, obj, **kwargs):
        return obj.price * obj.amount
