from rest_framework.response import Response
from rest_framework.views import APIView

from ...models.user_profile import UserProfile
from ..serializers import UserProfileCreateSerializer, UserProfileOutputSerializer, CreateUserSerializer


class UserProfileView(APIView):
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileOutputSerializer(profiles, many=True)
        return Response({"profiles": serializer.data})

    def post(self, request):
        profile = request.data.get('profile')
        profile['user'] = request.user
        profile_saved = None
        # Create an article from the above data
        serializer = UserProfileCreateSerializer(data=profile)
        if serializer.is_valid(raise_exception=True):
            profile_saved = UserProfile.objects.create(**profile)   
        out_serializer = UserProfileOutputSerializer(profile_saved)

        return Response({"success": out_serializer.data})
    