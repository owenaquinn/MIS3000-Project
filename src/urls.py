from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('addclass/', views.add_class),
    path('printclasses/', views.print_all_classes),
    path('addoffering/', views.add_offering),
    path('printdays/', views.print_days),
    path('printclass/', views.print_class)
]