from .models import Resource, footerData, Libary


def latest_resource(request):
    latest_resource = Resource.published.all()
    context = {
        'latest_resource': latest_resource,
    }
    return context


def footer(request):
    footer = footerData.objects.all()
    context = {
        'footer': footer,
    }
    return context


def libary(request):
    libary = Libary.objects.all()
    context = {
        'libary': libary,
    }
    return context
