from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    import logging
    logger = logging.getLogger(__name__)

    # Setup
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
        logger.info(
            f"Stripe Event Type: {event['type']} received successfully."
        )
    except ValueError:
        logger.error("Invalid payload received from Stripe")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        logger.error("Invalid signature from Stripe")
        return HttpResponse(status=400)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return HttpResponse(content=str(e), status=400)

    return HttpResponse(status=200)
