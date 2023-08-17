from django.urls import path
from . import views
urlpatterns=[
     path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('<int:pk>',views.DrugDetails.as_view(),name='drug'),
    #path('<int:pk>',views.Drug2Details.as_view(),name='drug2'),
]
#<int:id>
