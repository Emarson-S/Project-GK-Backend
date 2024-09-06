from django.urls import URLPattern, path
from . import views

urlpatterns= [
    path('auth',views.ProtectedView.as_view(), name='auth')
]