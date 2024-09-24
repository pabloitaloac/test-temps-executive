from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Article, Order, OrderArticle
from .serializers import ArticleSerializer, OrderSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        articles_data = data.pop('articles')
        
        order = Order.objects.create(**data)
        total_price_before_tax = 0
        total_price_with_tax = 0

        for item in articles_data:
            article = Article.objects.get(reference=item['article']['reference'])
            quantity = item['quantity']
            OrderArticle.objects.create(order=order, article=article, quantity=quantity)
            
            # Calculate prices
            total_price_before_tax += article.price_before_tax * quantity
            total_price_with_tax += (article.price_before_tax + (article.price_before_tax * (article.tax_rate / 100))) * quantity

        order.total_price_before_tax = total_price_before_tax
        order.total_price_with_tax = total_price_with_tax
        order.save()

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
