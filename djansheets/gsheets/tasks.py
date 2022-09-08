from datetime import datetime
import pygsheets
from cbrf.models import DailyCurrenciesRates
from celery import shared_task
from gsheets.models import SheetModel


@shared_task
def data_sheet():
    gsheets = pygsheets.authorize(service_file='my-project-test-361705-f60152cfc5ee.json')
    sh_google = gsheets.open('test')
    worksheets = sh_google[0]
    table = worksheets.get_all_records()
    usd = get_dollar()
    SheetModel.objects.all().delete()
    for sheets in table:
        number = sheets.get("№")
        number_order = sheets.get("заказ №")
        cost = sheets.get("стоимость,$")
        delivery_time = sheets.get("срок поставки")
        delivery_time = datetime.strptime(delivery_time, "%d.%m.%Y").date()
        # Получаем стоимость по актуальному курсу
        cost_rub = int(float(cost) * float(usd))
        SheetModel.objects.create(number=number, number_order=number_order, cost=cost, delivery_time=delivery_time,
                                  cost_rub=cost_rub, )


def get_dollar():
    daily = DailyCurrenciesRates()
    currency = 'R01235'
    return daily.get_by_id(currency).value
