from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include


urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+/$)', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+/$)', views.UserDetail.as_view()),
    url(r'^$', 'api_root'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),



)

urlpatterns = format_suffix_patterns(urlpatterns)

# idk why tutorial 4 said to put this here...im sure you can put it elsewhere
# but this adds the login button to the page
urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework')),
)