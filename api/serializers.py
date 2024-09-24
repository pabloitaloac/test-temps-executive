from rest_framework import serializers
from .models import Article, Order, OrderArticle

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class OrderArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = OrderArticle
        fields = ['article', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    articles = OrderArticleSerializer(source='orderarticle_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'articles', 'total_price_before_tax', 'total_price_with_tax', 'created_at']
