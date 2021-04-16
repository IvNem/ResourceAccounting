from django.db.models import Sum, F
from rest_framework import status

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import *
from ..models import Product


# класс для обработки GET и POST запросов
class ProductListAPIView(APIView):
    # функция обработки GET запроса
    def get(self, request):
        # получение всех обьектов из таблицы
        products = Product.objects.all()
        # сериализация данных из таблицы
        serializer = ProductSerializer(products, many=True)
        # возврат данных в требуемом формате
        return Response({"resources": serializer.data, "total_count": products.count()})

    # функция обработки POST запроса
    def post(self, request, format=None):
        # сериализация данных
        serializer = ProductWithoutCost(data=request.data)
        # проверка данных на нормализацию
        if serializer.is_valid():
            # сохранение данных
            serializer.save()
            # вовзрат статуса об успешном создании
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # вовзрат статуса об ошибке
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# класс для обработки GET, PUT, PATCH, DELETE запросов
# для обработки используется комбинированный класс RetrieveUpdateDestroyAPIView
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # получение всех обьектов из таблицы
    queryset = Product.objects.all()
    # сериализация данных из таблицы
    serializer_class = ProductSerializer


# класс для подсчета общей стоимости продуктов
class TotalCostAPIView(APIView):
    # функция обработки GET запроса
    def get(self, request):
        # получение всех обьектов из таблицы
        products = Product.objects.all()
        # агрегирования данных в нужном формате
        all_sum = products.aggregate(total_cost=Sum(F('price') * F('amount')))
        # возврат суммы произведения
        return Response(all_sum)

