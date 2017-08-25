from django.conf.urls import url
from . import views
urlpatterns = [

url(r'^$',views.index,name = 'index'),
url(r'^showlogin/$',views.showlogin,name = 'showlogin'),
url(r'^getlogin/$',views.getlogin,name = 'getlogin'),
url(r'^showregister/$',views.showregister,name = 'showregister'),
url(r'^getregister/$',views.getregister,name = 'getregister'),
url(r'^showfeedback/$',views.showfeedback,name = 'showfeedback'),
url(r'^getfeedback/$',views.getfeedback,name = 'getfeedback'),
url(r'^viewfeedback/$',views.viewfeedback,name = 'viewfeedback'),
url(r'^showhome/$',views.showhome,name = 'showhome'),
url(r'^showusers/$',views.showusers,name = 'showusers'),
url(r'^showdashboard/$',views.showdashboard,name = 'showdashboard'),
url(r'^getcourse/$',views.getcourse,name = 'getcourse'),
url(r'^showCheck/$',views.showCheck,name = 'showCheck'),
]
