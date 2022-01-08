from django.urls import path
from .views import (
    PublisherDocumentView,
)

urlpatterns = [
    path('search/', PublisherDocumentView.as_view({'get': 'list'})),
]
