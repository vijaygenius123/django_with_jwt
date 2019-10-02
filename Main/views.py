from django.contrib.auth import get_user_model
from rest_framework import serializers, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = get_user_model()
    fields = ('first_name', 'last_name', 'email')

class UserDetailView(generics.ListAPIView):
  permission_classes = [IsAuthenticated]

  def list(self, request):
    queryset = get_user_model().objects.get(id=request.user.id)
    serializer = UserDetailSerializer(queryset, many=False)
    return Response(serializer.data)