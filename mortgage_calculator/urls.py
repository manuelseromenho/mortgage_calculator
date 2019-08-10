from django.conf.urls import url
from django.contrib import admin
from mortgage_calculator import views
from mortgage_calculator.views import SubmitFormData, HomeView

urlpatterns = [
  url(r'^admin/', admin.site.urls),
# url(r'^$', views.home, name='home'),
  url(r'^mortgage_calc', SubmitFormData.as_view(), name='submitformdata'),
  url(r'^$', HomeView.as_view(), name='home')
]
