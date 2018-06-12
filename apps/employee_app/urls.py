from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^add_employee', views.add_new_employee),
    url(r'^save_employee', views.save_employee),
    url(r'^get_detail_employee/(?P<id>\d+)$', views.get_employee),
    url(r'^update_employee/(?P<id>\d+)$', views.update_employee),
    url(r'^delete_employee/(?P<id>\d+)$', views.destroy_employee)
]

