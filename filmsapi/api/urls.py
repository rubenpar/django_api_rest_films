
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PeopleCreateView, StudioCreateView, FilmCreateView, FilmYearCreateView

urlpatterns = {
    url(r'^people$', PeopleCreateView.as_view(), name="create_person"),
    url(r'^studio$', StudioCreateView.as_view(), name="create_studio"),
    url(r'^film$', FilmCreateView.as_view(), name="create_film"),
    url(r'^film/(?P<year>[0-9]+)$',
        FilmYearCreateView.as_view(), name="retrieve_film"),
}

urlpatterns = format_suffix_patterns(urlpatterns)