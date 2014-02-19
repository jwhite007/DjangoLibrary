from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^submit/$', views.SubmitView, name='submit'),
    url(r'^delete_user/(?P<first_name>\w+)/$', views.DeleteUser),
)
