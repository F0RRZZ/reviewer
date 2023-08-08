import django.views.generic


class GenreListMixin(django.views.generic.ListView):
    context_object_name = 'genres'
    paginate_by = 20
    template_name = 'genres/genres_feed.html'
