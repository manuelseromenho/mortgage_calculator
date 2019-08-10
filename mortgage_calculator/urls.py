from django.conf.urls import url
from django.contrib import admin
from mortgage_calculator import views
from mortgage_calculator.views import SubmitFormData

urlpatterns = [
  url(r'^admin/', admin.site.urls),
# url(r'^$', views.home, name='home'),
  url(r'^$', SubmitFormData.as_view(), name='submitformdata'),
]
