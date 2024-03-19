from django.urls import path
from . import views

app_name = "analysis"
urlpatterns = [
    path("", views.analysisplot, name="analysis_page"),
    path("back/", views.easteregg, name="easteregg_page"),
]