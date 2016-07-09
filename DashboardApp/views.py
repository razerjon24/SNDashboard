from django.views import generic
from django.http import JsonResponse
from collections import Counter
from .models import Points

class IndexView(generic.TemplateView):
   template_name = "DashboardApp/index.html"

class HeatMapView(generic.TemplateView):
    template_name = "DashboardApp/visualization.html"

class TopicView(generic.TemplateView):
    template_name = "DashboardApp/topic.html"

def test(request):
    start_day = request.GET['start_day']
    start_hour = request.GET['start_hour']
    end_day = request.GET['end_day']
    end_hour = request.GET['end_hour']
    geo_points = Points.objects.filter(day__range=(start_day,end_day)).filter(hour__range=(start_hour,end_hour))
    geo_points = [str(point) for point in geo_points]
    frecuencias=list(Counter(geo_points).most_common())
    lons, lats, counts = [frecuencia[0].split(',')[0] for frecuencia in frecuencias],[frecuencia[0].split(',')[1] for frecuencia in frecuencias],[frecuencia[1] if frecuencia[1] < 30 else 30 for frecuencia in frecuencias]
    return JsonResponse({'lons': lons,'lats': lats, 'counts': counts, 'len': len(frecuencias)})