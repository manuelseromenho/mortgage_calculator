import os
import subprocess

from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class DeployAutoExtendingPAView(View):
    def post(self, request, *args, **kwargs):
        secret = os.environ.get("DEPLOY_SECRET")
        auth = request.headers.get("Authorization")
        if auth != f"Bearer {secret}":
            return HttpResponseForbidden("Forbidden")

        try:
            project_dir = "/home/manuelseromenho/autoextending"
            subprocess.run(
                f"GIT_SSH_COMMAND='ssh -i /home/manuelseromenho/.ssh/id_rsa_deploy' cd {project_dir} "
                f"&& git pull origin master",
                shell=True,
                check=True,
            )

            return JsonResponse({"status": "success"})
        except subprocess.CalledProcessError as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(["POST"])
