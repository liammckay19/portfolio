from contact.models import ExternalWebsites

def websitelist(request):
    websites = ExternalWebsites.objects.all()
    return {'external_websites':websites}