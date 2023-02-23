from django.contrib import admin
from django.urls import re_path

from mortgage_calculator.views import HomeView, SubmitFormData, SubmitFormDataNumberPayments

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(
        r"^mortgage_calc_monthly_payment", SubmitFormDataNumberPayments.as_view(), name="submitformdata_number_payments"
    ),
    re_path(r"^mortgage_calc", SubmitFormData.as_view(), name="submitformdata"),
    re_path(r"^$", HomeView.as_view(), name="home"),
]
