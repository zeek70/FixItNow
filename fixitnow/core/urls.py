from django.urls import path
from core import views
urlpatterns = [
    path("",views.home,name="home"),
    path("requests/",views.service_request_list,name="service_request_list"),
    path("request/<int:request_id>",views.service_request_detail,name="service_request_detail"),
    path("requests/new/",views.create_service_request,name="create_service_request"),
    path("about/",views.aboutus,name="about"),
    path("requests/<int:pk>/edit/", views.update_service_request, name="update_service_request"),
    path("requests/<int:pk>/delete/", views.delete_service_request, name="delete_service_request"),
    
]



