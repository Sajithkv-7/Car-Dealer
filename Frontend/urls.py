from django.urls import path
from Frontend import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home_page/',views.home_page,name="home_page"),
    path('car_details/<int:d_id>/',views.car_details,name="car_details"),
    path('all_cars/',views.all_cars,name="all_cars"),
    path('search_car/',views.search_car,name="search_car"),
    path('login_user/',views.login_user,name="login_user"),
    path('register_user/',views.register_user,name="register_user"),
    path('save_registration/',views.save_registration,name="save_registration"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('signup_view/',views.signup_view,name="signup_view"),
    path('VerifyOtp/',views.VerifyOtp,name="VerifyOtp"),
    path('account_created/',views.account_created,name="account_created"),
    path('about_page/',views.about_page,name="about_page"),
    path('teams/',views.teams,name="teams"),
    path('blog/',views.blog,name="blog"),
    path('testimonials/',views.testimonials,name="testimonials"),
    path('faq/',views.faq,name="faq"),
    path('contact/',views.contact,name="contact"),
    path('Enquiry/<int:d_id>/',views.Enquiry,name="Enquiry"),
    path('enquiry_page/',views.enquiry_page,name="enquiry_page"),
    path('delete_inq/<int:d_id>/',views.delete_inq,name="delete_inq"),
    path('review_page/',views.review_page,name="review_page"),
    path('save_review/',views.save_review,name="save_review"),
    path('make_payment/<int:e_id>/',views.make_payment,name="make_payment"),
    path('success/',views.success,name="success"),
    path('chatbot/',views.chatbot,name="chatbot"),
    path('payment_pdf/',views.payment_pdf,name="payment_pdf"),
    path('pay_success/',views.pay_success,name="pay_success"),
    path('fetch_resources/',views.fetch_resources,name="fetch_resources"),
    path('render_to_pdf/',views.render_to_pdf,name="render_to_pdf"),
    path('GenerateInvoice/<int:pk>/',views.GenerateInvoice.as_view(),name="GenerateInvoice"),
    path('change_pass/',views.change_pass,name="change_pass"),
    path('pay_details/<int:p_id>/',views.pay_details,name="pay_details"),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='forgot_pas.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='pass_res-done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='change_pass.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='pass_reset_complete.html'),name='password_reset_complete')


]