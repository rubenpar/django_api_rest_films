
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PeopleCreateView

urlpatterns = {
    url(r'^people/$', PeopleCreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)