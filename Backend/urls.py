from django.urls import path
from Backend import views
urlpatterns =[
    path('index_page/',views.index_page,name="index_page"),
    path("add_car/",views.add_car,name="add_car"),
    path('save_car/',views.save_car,name="save_car"),
    path('display_car/',views.display_car,name="display_car"),
    path('edit_car/<int:c_id>/',views.edit_car,name="edit_car"),
    path('update_car/<int:c_id>/',views.update_car,name="update_car"),
    path('delete_car/<int:c_id>/',views.delete_car,name="delete_car"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('enquiry_page_backend/',views.enquiry_page_backend,name="enquiry_page_backend"),
    path('enq_approve/<str:enq_id>/',views.enq_approve,name="enq_approve"),
    path('enq_reject/<str:enq_id>/',views.enq_reject,name="enq_reject"),
    path('payment_details/',views.payment_details,name="payment_details")
]