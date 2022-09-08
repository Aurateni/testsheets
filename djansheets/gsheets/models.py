from django.db import models


class SheetModel(models.Model):
    number = models.IntegerField("№", blank=True, null=True)
    number_order = models.IntegerField("заказ №", blank=True, null=True)
    cost = models.FloatField("стоимость,$", blank=True, null=True)
    delivery_time = models.DateField("Срок поставки", blank=True, null=True)
    cost_rub = models.FloatField("Стоимость в рублях", blank=True, null=True)


