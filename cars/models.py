from django.db import models


# tabela de marcas
class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# tabela de carros
class Car(models.Model):
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='car_brand'
    )
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.model
