from django_elasticsearch_dsl_drf.viewsets import (
    DocumentViewSet
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)

from .serializers import (
    ArticleDocumentSerializer,
)
from .documents import (
    ArticleDocument,
)

class PublisherDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
        'title',
        'content',
    )
    filter_fields = {
        'title': 'title',
        'content': 'content',
    }