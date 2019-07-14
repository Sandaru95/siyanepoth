from django.shortcuts import render
from django.views import generic

from .models import Publisher, GreatQuote

class IndexView(generic.TemplateView):
    template_name = 'home/index.htm'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['publisher_team_list'] = Publisher.objects.all()
        context['great_quote_list'] = GreatQuote.objects.all()
        return context