from django.urls import path

from home.views import IndexView
app_name = 'Home'
urlpatterns = [
    path('', IndexView.as_view(), name='landing_page')
]