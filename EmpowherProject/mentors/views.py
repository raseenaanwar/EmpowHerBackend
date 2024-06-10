from django.http import JsonResponse
from rest_framework import generics
from accounts.models import CustomUser
from .serializers import MentorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserGeneralProfileSerializer
class MentorListView(generics.ListAPIView):
    serializer_class = MentorSerializer
    print("Inside mentor lsit view")
    def get_queryset(self):
        try:
            # Filter queryset to include only users with the role of "mentor"
            queryset = CustomUser.objects.filter(role='MENTOR')
            print(queryset)
            return queryset
        except:
            print("An error occurred while retrieving data.")
            return JsonResponse("Data retrieval failed", safe=False)
class MentorBlockView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MentorSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Invert the current value of is_blocked
        instance.is_blocked = not instance.is_blocked
        
        instance.save()
        
        serializer = MentorSerializer(instance)  # Instantiate the serializer with the updated instance
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def create_general_user_profile(request):
    if request.method == 'POST':
        print("inside creategeneralprofiule")
        email = request.data.get('email')  # Assuming email is used as a unique identifier
        print(email)
        print(request.data)
        # Check if a user with the provided email exists
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)

        # Check if the user is a mentor
        if user.role != 'MENTOR':
            return Response("User is not a mentor", status=status.HTTP_400_BAD_REQUEST)
        
        # If the user exists and is a mentor, proceed to save the general profile
        serializer = UserGeneralProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

