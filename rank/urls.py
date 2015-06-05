from django.conf.urls import patterns, url
from rank.views import rank_view

NUMBER_ONLY_REGEX = '[0-9]+'
urlpatterns = patterns(
    '',  # the '' is nessarry,avoid /endpoints/ Page Not Found Error.
    url(r'^rank/(?P<score>{})/?$'.format(NUMBER_ONLY_REGEX), rank_view),
)