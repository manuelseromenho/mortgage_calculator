import os, subprocess
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def deploy_autoextending_pa(request):
    secret = os.environ.get('DEPLOY_SECRET')
    auth = request.headers.get('Authorization')
    if auth != f'Bearer {secret}':
        return HttpResponseForbidden('Forbidden')

    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        subprocess.check_call(f'cd {BASE_DIR} && git pull', shell=True)

        username = os.environ.get('PA_USERNAME')
        domain = os.environ.get('PA_DOMAIN')
        token = os.environ.get('PA_API_TOKEN')

        subprocess.check_call(
            f"curl -X POST https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/"
            f" -H 'Authorization: Token {token}'",
            shell=True
        )

        return JsonResponse({'status': 'success'})
    except subprocess.CalledProcessError as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
