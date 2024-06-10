from django.http import JsonResponse
from rest_framework import generics
from accounts.models import CustomUser
from .serializers import MenteeSerializer
from rest_framework.response import Response
from rest_framework import status
class MenteeListView(generics.ListAPIView):
    serializer_class = MenteeSerializer
    
    def get_queryset(self):
        try:
            # Filter queryset to include only users with the role of "mentor"
            queryset = CustomUser.objects.filter(role='MENTEE')
            return queryset
        except:
            print("An error occurred while retrieving data.")
            return JsonResponse("Data retrieval failed", safe=False)
class MenteeBlockView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MenteeSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Invert the current value of is_blocked
        instance.is_blocked = not instance.is_blocked
        
        instance.save()
        
        serializer = MenteeSerializer(instance)  # Instantiate the serializer with the updated instance
        return Response(serializer.data, status=status.HTTP_200_OK)
