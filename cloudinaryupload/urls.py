from django.urls import path

from cloudinaryupload.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
