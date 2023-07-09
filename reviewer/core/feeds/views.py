import django.views.generic


class FeedBaseView(django.views.generic.ListView):
    context_object_name = 'movies'
    paginate_by = 5
    template_name = 'feeds/feed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed_name'] = self.__class__.feed_name
        return context
