import django.views.generic

import persons.models


class PersonDetailView(django.views.generic.DetailView):
    context_object_name = 'person'
    pk_url_kwarg = 'person_id'
    model = persons.models.Person
    queryset = persons.models.Person.objects.prefetch_related(
        'career', 'genres'
    )
    template_name = 'persons/person_detail.html'
