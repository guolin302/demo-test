from django.http import JsonResponse


def hello(request):
    # 创建一个字典，包含你想要返回的数据
    data = {'domain1': 'www.eastbuy.com','domain2':'app.eastbuy.com'}
    # 使用JsonResponse返回这个字典作为JSON格式的响应
    return JsonResponse(data)
