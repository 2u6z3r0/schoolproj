from django.urls import re_path
from django.urls import include


from .views import welcome

urlpatterns = [
    re_path('^$', welcome),
]
