from django.shortcuts import render
from .models import Goods

# Create your views here.
def show_all_goods(request):
    goods = Goods.objects.all()
    return render(request,'/templates/goods_list.html',{'goods':goods})