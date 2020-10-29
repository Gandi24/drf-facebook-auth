from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import UserDetailsView

from users.serializers import UserMeSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserMeView(UserDetailsView):
    serializer_class = UserMeSerializer
