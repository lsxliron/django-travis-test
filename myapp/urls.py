from django.conf.urls import url
import views

urlpatterns = [
    url(r'^create/$', views.CreatePersonView.as_view(), name="create-person"),
    url(r'^list/$', views.ListPersonView.as_view(), name='list-person'),
    url(r'^edit/(?P<uuid>[A-Fa-f0-9\-]+)/$', views.EditPersonView.as_view(), name='edit-person'),
    url(r'^delete/(?P<uuid>[A-Fa-f0-9\-]+)/$', views.DeletePersonView.as_view(), name='delete-person'),
]
