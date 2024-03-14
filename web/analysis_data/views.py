from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from analysis_data.models import EmpData


# Create your views here.
def main(request):
    queryset = EmpData.objects.all().order_by("smallfirstfloor").values("borough", "smallfirstfloor", "emptopopul")
    labels = [item["borough"] for item in queryset]
    values1 = [item["smallfirstfloor"] for item in queryset]
    values2 = [item["emptopopul"] for item in queryset]
    context = {
        "labels" : labels,
        "values1" : values1,
        "values2" : values2,
        }
    return render(request, "main.html", context)







    # sns.set(style="whitegrid")
    # fig = plt.figure(figsize = (15, 8))

    # ax1 = fig.add_subplot(1, 1, 1)
    # ax2 = ax1.twinx()

    # groups = len(df.index)
    # idx = np.arange(groups)

    # sns.barplot(x = df["borough"], y = df["smallfirstfloor"], ax = ax1)
    # ax1.set_ylim(20, 90)
    # ax2.plot(df["borough"], df["emptopopul"], "ko-")

    # ax1.set_xticklabels([i for i in df["borough"]], rotation = 45, size = 12)

    # img_path = "static/sample_plot.png"
    # plt.savefig(img_path)