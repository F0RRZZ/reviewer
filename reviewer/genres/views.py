from core.mixins import SearchViewMixin
from core.genres.mixins import GenreListMixin
from genres.models import Genre


class GenreListView(GenreListMixin):
    queryset = Genre.objects.order_by(
        Genre.name.field.name,
    ).all()


class SearchView(GenreListMixin, SearchViewMixin):
    context_object_name = 'genres'
    paginate_by = 20
    template_name = 'genres/genres_feed.html'

    def get_queryset(self):
        return Genre.objects.filter(name__icontains=self.request.GET.get('q'))
