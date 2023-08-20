from django.urls import path

from persons.views import PersonDetailView

app_name = 'persons'
urlpatterns = [
    path(
        '<int:person_id>',
        PersonDetailView.as_view(),
        name='person_detail',
    )
]
