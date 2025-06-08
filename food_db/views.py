from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Food
from .serializers import FoodSerializer
from .tasks import process_food_task

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        food = serializer.save()
        process_food_task.delay(food.id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Skip the CSRF check