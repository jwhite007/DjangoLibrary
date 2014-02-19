from django.conf.urls import patterns, url
from books import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<user_id>\d+)/books/$', views.index, name='books'),
    url(r'^checkout_book/(?P<pk>\w+)/$', views.CheckoutBook),
    url(r'^checkin_book/(?P<pk>\w+)/$', views.CheckinBook),
)
