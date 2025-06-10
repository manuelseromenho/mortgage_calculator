from django.contrib import admin
from django.urls import path, include

from mortgage_calculator.views import (
    HomeView,
    SubmitFormData,
    SubmitFormDataNumberPayments,
)

urlpatterns = [
    path("admin", admin.site.urls),
    path(
        "mortgage_calc_monthly_payment",
        SubmitFormDataNumberPayments.as_view(),
        name="submitformdata_number_payments",
    ),
    path("mortgage_calc", SubmitFormData.as_view(), name="submitformdata"),
    path("deploy_autoextending_pa", include("deploy_autoextending_pa.urls")),
    path("", HomeView.as_view(), name="home"),
]
