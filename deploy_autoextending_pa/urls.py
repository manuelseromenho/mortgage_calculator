from django.urls import path

from .views import DeployAutoExtendingPAView

urlpatterns = [
    path(
        "/deploy",
        DeployAutoExtendingPAView.as_view(),
        name="deploy",
    )
]
