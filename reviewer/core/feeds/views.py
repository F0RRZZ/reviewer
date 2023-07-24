import django.views.generic

import core.tools
import persons.models


class FeedBaseView(django.views.generic.ListView):
    context_object_name = 'movies'
    paginate_by = 12
    template_name = 'feeds/feed.html'

    def get_persons_birthday(self):
        today = core.tools.get_today_date(self.request)
        persons_birthday = persons.models.Person.objects.filter(
            date_of_birth__day=today.day,
            date_of_birth__month=today.month,
        ).only(
            persons.models.Person.name.field.name,
            persons.models.Person.surname.field.name,
        )
        return persons_birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed_name'] = self.__class__.feed_name
        context['persons_birthday'] = self.get_persons_birthday()
        return context
