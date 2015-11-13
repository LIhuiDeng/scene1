from django.conf.urls.defaults import *
from mysite.views import *

urlpatterns = patterns('',
    ('^home/$',index),
    ('^search/$',search),
    ('^search/$',search),
    ('^delete/$',delete),
    ('^author/$',author),
    ('^deleteauthor/$',deleteauthor),
    ('^addbook/$',addbook),
    ('^submit/$',submit),
    ('^addauthor/$',addauthor),
    ('^submit_author/$',submit_author),
    ('^detail/$',detail),
)
