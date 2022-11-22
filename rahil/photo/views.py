from .serializers import photoSerializer
from .models import photo
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class photoList(ListAPIView):
    queryset = photo.objects.all()
    serializer_class = photoSerializer


class photoView(RetrieveAPIView):
    queryset = photo.objects.all()
    serializer_class = photoSerializer
    lookup_field = 'id'

# class photoGet(APIView):
#     def get(self, request, id):
#         model = photo.objects.get(id=id)
#         serializer = photoSerializer(model, many=False)
#         return Response(serializer.data)


class photoCreate(CreateAPIView):
    queryset = photo.objects.all()
    serializer_class = photoSerializer

class photoDestroy(DestroyAPIView):
    queryset = photo.objects.all()
    serializer_class = photoSerializer
    lookup_field = 'id'

