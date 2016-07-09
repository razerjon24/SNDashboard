from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^heatmap/$', views.HeatMapView.as_view(), name='heatmap'),
    url(r'^heatmap/test/$', views.test, name='test'),
    url(r'^topic/$', views.TopicView.as_view(), name='topic'),
    # ex: /polls/5/vote/
]