from django.shortcuts import render, get_object_or_404
from .models import Goods

# Create your views here.


def show_all_goods(request):
    goods = Goods.objects.all()
    return render(request,'goods_list.html',{'entries':goods})


def detail_goods(request, pk):
    goods = get_object_or_404(Goods, pk=pk)
    return render(request, 'goods_detail.html', {'entry': goods})
