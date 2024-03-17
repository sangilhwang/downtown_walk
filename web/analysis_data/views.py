from django.shortcuts import render
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from analysis_data.models import EmpData


# Create your views here.
def analysisplot(request):
    queryset = EmpData.objects.all().order_by("smallfirstfloor").values("borough", "smallfirstfloor", "emptopopul")
    labels = [item["borough"] for item in queryset]
    values1 = [item["smallfirstfloor"] for item in queryset]
    values2 = [item["emptopopul"] for item in queryset]
    context = {
        "labels" : labels,
        "values1" : values1,
        "values2" : values2,
        }
    return render(request, "analysis_page.html", context)

