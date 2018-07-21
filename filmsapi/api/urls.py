
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
    url(r'^people$', PeopleCreateView.as_view(), name="create"),
    # url(r'^people/(?P<pk>[0-9]+)/$',
    #     PeopleDetailsView.as_view(), name="details"),
    url(r'^studio$', StudioCreateView.as_view(), name="create"),
    # url(r'^studio/(?P<pk>[0-9]+)/$',
    #     StudioDetailsView.as_view(), name="details"),
    url(r'^film$', FilmCreateView.as_view(), name="create"),
    url(r'^film/(?P<year>[0-9]+)$',
        FilmDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)