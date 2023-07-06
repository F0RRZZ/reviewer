import django.contrib.admin
import django.urls
import homepage.views

urlpatterns = [
    django.urls.path('', homepage.views.HomepageView.as_view()),
    django.urls.path('admin/', django.contrib.admin.site.urls),
]
