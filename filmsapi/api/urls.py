
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PeopleCreateView, StudioCreateView, FilmCreateView

urlpatterns = {
    url(r'^people$', PeopleCreateView.as_view(), name="create"),
    url(r'^studio$', StudioCreateView.as_view(), name="create"),
    url(r'^film$', FilmCreateView.as_view(), name="create"),
    url(r'^film/(?P<year>[0-9]+)$',
        FilmCreateView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)