from django.views import generic
from django.http import JsonResponse
from collections import Counter
from .models import Points,Bursts,Clusters,Pics

class IndexView(generic.TemplateView):
   template_name = "DashboardApp/index.html"

class HeatMapView(generic.TemplateView):
    template_name = "DashboardApp/visualization.html"

class TopicView(generic.TemplateView):
    template_name = "DashboardApp/topic.html"

class GeoPicsView(generic.TemplateView):
    template_name = "DashboardApp/geopics.html"

def get_points(request):
    start_day = request.GET['start_day']
    start_hour = request.GET['start_hour']
    end_day = request.GET['end_day']
    end_hour = request.GET['end_hour']
    geo_points = Points.objects.filter(day__range=(start_day,end_day)).filter(hour__range=(start_hour,end_hour))
    geo_points = [str(point) for point in geo_points]
    frecuencias=list(Counter(geo_points).most_common())
    lons, lats, counts = [frecuencia[0].split(',')[0] for frecuencia in frecuencias],[frecuencia[0].split(',')[1] for frecuencia in frecuencias],[frecuencia[1] if frecuencia[1] < 30 else 30 for frecuencia in frecuencias]
    return JsonResponse({'lons': lons,'lats': lats, 'counts': counts, 'len': len(frecuencias)})

def get_topics(request):
    start_day = request.GET['start_day']
    end_day = request.GET['end_day']
    burst_topics = Bursts.objects.filter(day__range=(start_day,end_day))
    burst_topics = [(str(topic).split(",")[0],str(topic).split(",")[1]) for topic in burst_topics if not str(topic).split(",")[0].lower().__contains__("sigueme")
                    and not str(topic).split(",")[0].lower().__contains__("seguidores") and not str(topic).split(",")[0].lower().__contains__("foll")
                    and not str(topic).split(",")[0].lower().__contains__("pss") and not str(topic).split(",")[0].isdigit() and (str(topic).split(",")[0].lower().startswith('@') or str(topic).split(",")[0].lower().startswith('#')) ]
    burst_topics = sorted(burst_topics, key=lambda tup: tup[1], reverse= True)
    burst_topics = burst_topics[:101]
    topics = [topic[0] for topic in burst_topics]
    levels = [str(topic[1]) for topic in burst_topics]
    return JsonResponse({'words':topics,'levels':levels})

def get_clusters(request):
    tipo = request.GET['tipo']
    points = Clusters.objects.filter(tipo__exact=tipo)
    points = [str(point).split(",") for point in points]
    clusters = [i for i in xrange(1,len(points)+1)]
    tam = len(points)
    return JsonResponse({'points':points,'len':tam,'tipo':tipo,'clusters':clusters})

def get_pics(request):
    cluster = request.GET['cluster']
    tipo = request.GET['tipo']
    pics = Pics.objects.filter(tipo__exact=tipo).filter(cluster__exact=cluster)
    urls = [str(pic.url) for pic in pics]
    texts = [pic.text for pic in pics]
    tam = len(pics)
    return JsonResponse({'pics':urls,'len':tam,'texts':texts})