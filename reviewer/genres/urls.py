import django.urls
import django.views.decorators.cache

import genres.views

app_name = 'genres'
urlpatterns = [
    django.urls.path(
        '',
        django.views.decorators.cache.cache_page(43200)(
            genres.views.GenresListView.as_view()
        ),
        name='genres',
    ),
]
