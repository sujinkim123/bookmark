from django.contrib import admin
from django.urls import path
from chart import views                                     # !!!

urlpatterns = [
    path('', views.home, name='home'),
    path('ticket-class/1/',
         views.ticket_class_view_1, name='ticket_class_view_1'),
    path('ticket-class/2/',
         views.ticket_class_view_2, name='ticket_class_view_2'),
    path('ticket-class/3/',
         views.ticket_class_view_3, name='ticket_class_view_3'),
    path('world-population/',
         views.world_population, name='world_population'),  # !!!
    path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
    path('admin/', admin.site.urls),
    path('COVID19-ConfirmedCases/',
         views.COVID19_ConfirmedCases, name='COVID19_ConfirmedCases'),
    path('COVID19-Deaths/',
         views.COVID19_Deaths, name='COVID19_Deaths'),
    path('COVID19-Recoveries/',
         views.COVID19_Recoveries, name='COVID19_Recoveries'),

]