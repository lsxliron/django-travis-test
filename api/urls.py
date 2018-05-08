from django.conf.urls import url
import views

urlpatterns = [
    url(r'^person/(?P<uuid>[A-Fa-f0-9\-]+)/$', views.PersonViewSet.as_view({"get": "get", "patch": "patch", "delete": "delete"})),
    url(r'^person/$', views.PersonViewSet.as_view({"put": "put"}))
]
