from django.conf import settings


def site_metadata(request):
    return {
        "site_name": settings.SITE_NAME,
        "site_url": settings.SITE_URL,
        "site_description": settings.SITE_DESCRIPTION,
        "canonical_url": f"{settings.SITE_URL}{request.path}",
    }
