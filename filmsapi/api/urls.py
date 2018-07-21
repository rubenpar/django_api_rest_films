
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PeopleCreateView, PeopleDetailsView

urlpatterns = {
    url(r'^people/$', PeopleCreateView.as_view(), name="create"),
    url(r'^people/(?P<pk>[0-9]+)/$',
        PeopleDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)