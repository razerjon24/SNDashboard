from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import Choice, Question
class IndexView(generic.TemplateView):
   template_name = "DashboardApp/index.html"

class DetailView(generic.TemplateView):
    template_name = "DashboardApp/visualization.html"
    context_object_name = "visualization"


class ResultsView(generic.DetailView):
   model = Question
   template_name = "DashboardApp/results.html"

   def vote(request, question_id):
       p = get_object_or_404(Question, pk=question_id)
       try:
           selected_choice = p.choice_set.get(pk=request.POST['choice'])
       except (KeyError, Choice.DoesNotExist):
           return render(request, 'DashboardApp/detail.html', {
               'question': p,
               'error_message': "You didn't select a choice",
           })
       else:
           selected_choice.votes += 1
           selected_choice.save()
           return HttpResponseRedirect(reverse('DashboardApp:results', args=(p.id,)))