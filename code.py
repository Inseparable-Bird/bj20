from django.http import HttpResponse
from booktest.models import User

    def index(request):
        return HttpResponse("首页")

    def login(request):
        username = request.POST.get('username')
        return HttpResponse("登录成功")
