from django.urls import path
from .views import deploy_autoextending_pa

urlpatterns = [
    path(
        "deploy_autoextending_pa/",
        deploy_autoextending_pa,
        name="deploy_autoextending_pa",
    )
]
