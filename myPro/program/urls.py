from django.urls import path,re_path
from .views import ListView,DetailView,DeleteView,AddView,EditView
app_name='program'
urlpatterns=[
    path('list/',ListView.as_view(),name='list'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('delete/',DeleteView.as_view(),name='delet'),
    path('add/',AddView.as_view(),name='add'),
    path('edit/',EditView.as_view(),name='edit')
]