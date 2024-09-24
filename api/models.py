from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Article(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price_before_tax = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reference} - {self.name}'

class Order(models.Model):
    articles = models.ManyToManyField(Article, through='OrderArticle')
    total_price_before_tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total_price_with_tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'

class OrderArticle(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.article.name} (x{self.quantity}) in Order #{self.order.id}'
