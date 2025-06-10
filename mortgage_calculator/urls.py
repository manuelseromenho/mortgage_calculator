from django.contrib import admin
from django.urls import path, include

from mortgage_calculator.views import (
    HomeView,
    SubmitFormData,
    SubmitFormDataNumberPayments,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "mortgage_calc_monthly_payment",
        SubmitFormDataNumberPayments,
        name="submitformdata_number_payments",
    ),
    path("mortgage_calc", SubmitFormData, name="submitformdata"),
    path("deploy_autoextending_pa", include("deploy_autoextending_pa.urls")),
    path("", HomeView, name="home"),
]
