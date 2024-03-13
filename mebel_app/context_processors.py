from .models import Contact, Social


def contact_info(request):
    active_contact = Contact.objects.filter(active=True).first()
    return {'contact_info': active_contact}


def social_info(request):
    socials = Social.objects.all()
    return {'socials': socials}