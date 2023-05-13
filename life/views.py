import logging

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import InquiryForm
# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('life:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'you sent messages.')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)