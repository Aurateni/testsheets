import pretty_html_table
from django.shortcuts import render
from .models import SheetModel
import pandas as pd

from .tasks import data_sheet


def home(request):
    item = SheetModel.objects.all().values()
    df = pd.DataFrame(item)

    mydict = {
        'df': pretty_html_table.build_table(df, 'blue_light')
    }
    return render(request, 'index.html', context=mydict)
# Create your views here.
