from .models import ContactInfo


def contact_info(request):
    try:
        contact_info = ContactInfo.objects.latest('updated_at')
    except ContactInfo.DoesNotExist:
        contact_info = None
    return {
        'contact_info': contact_info
    }
