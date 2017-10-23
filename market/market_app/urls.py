from django.conf.urls import url, include
from .views import show_all_goods

urlpatterns = [
    url(r'^$', show_all_goods, name='show_all_goods'),
]
