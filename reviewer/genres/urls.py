import django.urls

import genres.views

app_name = 'genres'
urlpatterns = [
    django.urls.path('', genres.views.GenresListView.as_view(), name='genres'),
]
