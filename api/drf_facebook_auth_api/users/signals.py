from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialAccount
from django.dispatch import receiver


@receiver(user_logged_in)
def update_user_profile_image(request, user, **kwargs):
    """Update user's profile image on every login."""

    try:
        social_account = user.socialaccount_set.get(provider="facebook")
    except SocialAccount.DoesNotExist:
        return

    user.profile_image = social_account.get_avatar_url()
    user.save()
