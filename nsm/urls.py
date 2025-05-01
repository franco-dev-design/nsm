from django.urls.conf import path
from .views import HomePageView


urlpatterns = [
    path('home/', HomePageView.as_view(), name='homepage'),

]
