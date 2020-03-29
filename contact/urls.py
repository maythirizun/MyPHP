from django.urls import path
from . import views
from contact.est_views import list, new, update

#app_name = 'contact'
urlpatterns = [
    path('', views.index, name='contact'),
    path('register', views.register, name="register"),
    path('checklist', views.checklist, name="checklist"),
    path('update/<int:id>/', views.update, name="update"),
    path('estimates/list', list.list_func, name='list'),
    path('estimates/new', new.new_func, name='new'),
    path('estimates/update/<int:pk>/', update.update_func, name='upd'),    
]

