from django.urls import path
from django.urls import include
from .views import school_view, school_view2


from .views import welcome

urlpatterns = [
    path('<int:id>/', school_view, name='school'),
    path('', welcome),   
]
