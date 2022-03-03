from django.http import JsonResponse


def json_response(status, message, data, ensure_ascii=False):
    return JsonResponse({
        'status': status,
        'message': message,
        'data': data
    }, json_dumps_params={'ensure_ascii': ensure_ascii})