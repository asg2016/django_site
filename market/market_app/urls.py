from django.conf.urls import url, include
from .views import show_all_goods, detail_goods

urlpatterns = [
    url(r'^$', show_all_goods, name='show_all_goods'),
    url(r'^detail/(?P<pk>\d+)$', detail_goods, name='detail_goods')
]
