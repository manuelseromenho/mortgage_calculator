from django.conf.urls import url
from django.contrib import admin
from mortgage_calculator.views import SubmitFormData, HomeView, SubmitFormDataNumberPayments

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^mortgage_calc_monthly_payment', SubmitFormDataNumberPayments.as_view(), name='submitformdata_number_payments'),
  url(r'^mortgage_calc', SubmitFormData.as_view(), name='submitformdata'),
  url(r'^$', HomeView.as_view(), name='home')
]
