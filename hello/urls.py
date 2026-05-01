
'''
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world),
]
'''
from django.urls import path
from .views import document_list, document_create, document_update, document_delete

urlpatterns = [
    path('',                    document_list,   name='document_list'),
    path('create/',             document_create, name='document_create'),
    path('<int:pk>/edit/',      document_update, name='document_update'),
    path('<int:pk>/delete/',    document_delete, name='document_delete'),
]

'''
urlpatterns = [
    path('', document_list, name='document_list'),
]
'''