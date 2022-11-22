from .serializers import dailySerializer
from .models import daily
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView

class dailyList(ListAPIView):
    queryset = daily.objects.all()
    serializer_class = dailySerializer
    
class dailyCreate(CreateAPIView):
    queryset = daily.objects.all()
    serializer_class = dailySerializer

class dailyDestroy(DestroyAPIView):
    queryset = daily.objects.all()
    serializer_class = dailySerializer
    lookup_field = 'id'