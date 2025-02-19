# import json
# import requests
# from django.http import JsonResponse
# from rest_framework import generics
# from models import Profile
# from serializer import ProfileSerializer


# class HomePage(generics.RetrieveAPIView):

#     serializer_class = ProfileSerializer
#     lookup_field = 'id'
#     queryset = Profile.objects.all()
