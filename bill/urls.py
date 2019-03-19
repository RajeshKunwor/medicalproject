from django.urls import path
from .views import *
urlpatterns =[
    # path('dashboard/<int:pk>/bill_create/',BillCreateView.as_view(),name='bill_create'),
    path('dashboard/<int:pk>/bill_list/',BillListView.as_view(),name='bill_list'),
    path('dashboard/',generate_bill,name='generate_bill'),
    path('dashboard/generate_pdf',generate_pdf,name='generate_pdf'),
    # path('dashboard/<int:pk>/history_update',HistoryUpdateView.as_view(),name='history_update'),
    path('load_prescription_data/',load_prescription,name='load_prescription_data'),
    path('load_service_data/',load_service,name='load_service_data'),
    path('check_prescription/', check_prescription, name='check_prescription'),

]