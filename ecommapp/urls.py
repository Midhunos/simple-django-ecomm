from django.urls import path
from ecommapp import views

app_name='ecommapp'


urlpatterns = [
    path('',views.Allprodcat,name="Allprodcat"),
    path('<slug:c_slug>/',views.Allprodcat,name='products_by_category'),
    path('<slug:c_slug>,<slug:product_slug>/', views.proDetail, name='procatdetail'),

]