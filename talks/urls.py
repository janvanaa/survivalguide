from __future__ import absolute_import

from django.conf.urls import patterns, url, include

from . import views


lists_patterns = patterns(
    '',
    url(r'^$', views.TalkListListView.as_view(), name='list'),
    url(r'^d/(?P<slug>[-\w]+)/$', views.TalkListDetailView.as_view(), name='detail'),
    url(r'^create/$', views.TalkListCreateView.as_view(), name='create'),
    url(r'^e/(?P<slug>[-\w]+)/$', views.TalkListUpdateView.as_view(), name='update'),
    url(r'^s/(?P<slug>[-\w]+)/$', views.TalkListScheduleView.as_view(), name='schedule'),
    url(r'^r/(?P<slug>[-\w]+)/$', views.TalkListDeleteView.as_view(), name='delete'),
    url(r'^remove/(?P<talklist_pk>\d+)/(?P<pk>\d+)/$', views.TalkListRemoveTalkView.as_view(), name='remove_talk'),
)

urlpatterns = patterns(
    '',
    url(r'^lists/', include(lists_patterns, namespace='lists')),
)