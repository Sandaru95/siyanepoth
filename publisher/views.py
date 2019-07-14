from django.shortcuts import render
from django.views import generic

from home.models import Publisher, GreatQuote

class PublisherDetailView(generic.DetailView):
    model = Publisher
    template_name = 'publisher/publisher_detail.htm'

    def get_context_data(self, **kwargs):
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        context['great_quote_list'] = GreatQuote.objects.all()
        return context