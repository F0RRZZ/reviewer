from django.views.generic import ListView


class GenreListMixin(ListView):
    context_object_name = 'genres'
    paginate_by = 20
    template_name = 'genres/genres_feed.html'
