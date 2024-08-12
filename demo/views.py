from django.http import JsonResponse


def hello(request):
    data = {'domain1': 'www.eastbuy.com','domain2':'app.eastbuy.com'}
    return JsonResponse(data)
