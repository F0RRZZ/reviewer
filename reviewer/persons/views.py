from django.views.generic import DetailView

from persons.models import Person


class PersonDetailView(DetailView):
    context_object_name = 'person'
    pk_url_kwarg = 'person_id'
    model = Person
    queryset = Person.objects.prefetch_related(
        Person.career.field.name,
        Person.genres.field.name,
    )
    template_name = 'persons/person_detail.html'
