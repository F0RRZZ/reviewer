import django.views.generic

import genres.models


class GenresListView(django.views.generic.ListView):
    context_object_name = 'genres'
    paginate_by = 20
    queryset = genres.models.Genre.objects.order_by(
        genres.models.Genre.name.field.name,
    ).all()
    template_name = 'genres/genres_feed.html'
