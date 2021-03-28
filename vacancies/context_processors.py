from .models import Settings


def site_title(request):
    return {'site_title': Settings.objects.get(name='site_title').value}


def site_description(request):
    return {'site_description': Settings.objects.get(name='site_description').value}
