from rest_framework import serializers
from .models import Article, Order, OrderArticle


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class OrderArticleSerializer(serializers.ModelSerializer):
    article_reference = serializers.CharField(source='article.reference', read_only=False)

    class Meta:
        model = OrderArticle
        fields = ['article_reference', 'quantity']

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        if value > 999:
            raise serializers.ValidationError("Quantity cannot exceed 999.")
        return value

    def create(self, validated_data):
        article_data = validated_data.pop('article')
        article_reference = article_data.get('reference')
        article = Article.objects.get(reference=article_reference)
        return OrderArticle.objects.create(article=article, **validated_data)


class OrderSerializer(serializers.ModelSerializer):
    articles = OrderArticleSerializer(source='orderarticle_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'articles', 'total_price_before_tax', 'total_price_with_tax', 'created_at', 'updated_at']
        read_only_fields = ['total_price_before_tax', 'total_price_with_tax', 'created_at', 'updated_at']

    def _calculate_totals(self, order, articles_data):
        """
        Helper method to calculate the total price before and after tax.
        """
        total_price_before_tax = 0
        total_price_with_tax = 0

        for article_data in articles_data:
            article_reference = article_data['article']['reference']
            quantity = article_data['quantity']

            try:
                article = Article.objects.get(reference=article_reference)
            except Article.DoesNotExist:
                raise serializers.ValidationError(f"Article with reference {article_reference} does not exist.")

            OrderArticle.objects.create(order=order, article=article, quantity=quantity)

            price_before_tax = article.price_before_tax * quantity
            total_price_before_tax += price_before_tax
            price_with_tax = price_before_tax + (price_before_tax * (article.tax_rate / 100))
            total_price_with_tax += price_with_tax


        order.total_price_before_tax = total_price_before_tax
        order.total_price_with_tax = total_price_with_tax
        order.save()

    def create(self, validated_data):
        articles_data = validated_data.pop('orderarticle_set')
        order = Order.objects.create()

        self._calculate_totals(order, articles_data)

        return order

    def update(self, instance, validated_data):
        articles_data = validated_data.pop('orderarticle_set')

        instance.articles.clear()

        self._calculate_totals(instance, articles_data)

        return instance
