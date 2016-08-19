from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^heatmap/$', views.HeatMapView.as_view(), name='heatmap'),
    url(r'^heatmap/points/$', views.get_points, name='points'),
    url(r'^topic/$', views.TopicView.as_view(), name='topic'),
    url(r'^topic/bursts/$',views.get_topics, name='bursts'),
    url(r'^geopics/$',views.GeoPicsView.as_view(), name='geopics'),
    url(r'^geopics/clusters/$',views.get_clusters, name='clusters'),
    url(r'^geopics/pics/$',views.get_pics, name='pics'),
    url(r'^sentiment/$',views.SentimentView.as_view(), name='sentiment'),
    url(r'^sentiment/emotions/$',views.get_emotions, name='emotions')
    # ex: /polls/5/vote/
]