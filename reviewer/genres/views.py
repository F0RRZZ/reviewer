import core.mixins
import core.genres.mixins
import genres.models


class GenreListView(core.genres.mixins.GenreListMixin):
    queryset = genres.models.Genre.objects.order_by(
        genres.models.Genre.name.field.name,
    ).all()


class SearchView(
    core.genres.mixins.GenreListMixin, core.mixins.SearchViewMixin
):
    context_object_name = 'genres'
    paginate_by = 20
    template_name = 'genres/genres_feed.html'

    def get_queryset(self):
        return genres.models.Genre.objects.filter(
            name__icontains=self.request.GET.get('q')
        )
