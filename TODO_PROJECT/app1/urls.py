from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('display',views.display,name='display'),
    path('update/<int:ud>',views.update,name='update'),
    path('delete/<int:dl>',views.delete,name='delete'),
    path('history/',views.history,name='history'),
    path('complete/<int:com>',views.complete,name='complete'),
    path('single/<int:pk>',views.single,name='single'),
]