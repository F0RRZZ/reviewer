import django.views.generic


class BaseMovieStaffView(django.views.generic.ListView):
    context_object_name = 'persons'
    paginate_by = 10
    pk_url_kwarg = 'movie_id'
    template_name = 'movies/movie_staff.html'


class BaseMovieStaffWithModifiedContextData(BaseMovieStaffView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_id'] = self.kwargs[self.pk_url_kwarg]
        context['staff_type'] = self.__class__.staff_type
        return context
