from django.shortcuts import render, get_object_or_404
from .models import Template, Setting

def index(request):
    templates = Template.objects.all()
    context = {'templates': templates}
    return render(request, 'index.html', context)

def template(request, template_id):
    template = get_object_or_404(Template, pk=template_id)
    settings = Setting.objects.all()
    return render(request, 'template.html', {'template': template, 'settings': settings})
