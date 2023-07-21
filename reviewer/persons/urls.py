import django.urls

import persons.views

app_name = 'persons'
urlpatterns = [
    django.urls.path(
        '<int:person_id>',
        persons.views.PersonDetailView.as_view(),
        name='person_detail',
    )
]
