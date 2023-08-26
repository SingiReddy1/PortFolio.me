from django.urls import path
from django.contrib import admin
#now import the views.py file into this code
from . import views
urlpatterns=[
path('admin/', admin.site.urls),
path('',views.home, name="Home"),
# path('contact/',views.contact, name="Contact")
]
