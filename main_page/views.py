from rest_framework import generics

from utils import query_debugger
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


# Create your views here.
class MainInfoAPIView(APIView):
    @query_debugger
    def get(self, request):
        profile_id = request.data['profile_id']
        profile = Profile.objects.select_related('department') \
            .get(pk=profile_id)

        serialized = MainInfoSerializer(profile)
        return Response(serialized.data)


# class MainInfoAPIView(generics.RetrieveAPIView):



class ContactDetailsAPIView(APIView):
    @query_debugger
    def get(self, request):
        profile_id = request.data['profile_id']
        profile = Profile.objects \
            .select_related('contact_details', 'office__address') \
            .get(pk=profile_id)

        serialized = ContactDetailsSerializer(profile)
        return Response(serialized.data)


# class InterestsAPIView(APIView):
#     @query_debugger
#     def get(self, request):
#         profile_id = request.data['profile_id']
#         profile = Profile.objects.get(pk=profile_id)
#         serialized = InterestsSerializer(profile)
#         return Response(serialized.data)


class InterestsAPIView(generics.ListAPIView):
    serializer_class = InterestsSerializer

    def get_queryset(self):
        profile_id = self.request.data['profile_id']
        profile = Profile.objects.get(pk=profile_id)
        return profile.interests.all()


# class CertificatesAPIView(APIView):
#     @query_debugger
#     def get(self, request):
#         profile_id = request.data['profile_id']
#         profile = Profile.objects.get(pk=profile_id)
#         queryset = profile.certificates.all()
#         return Response({
#             'certificates': CertificatesSerializer(queryset, many=True).data
#         })


class CertificatesAPIView(generics.ListAPIView):
    serializer_class = CertificatesSerializer

    def get_queryset(self):
        profile_id = self.request.data['profile_id']
        profile = Profile.objects.get(pk=profile_id)
        return profile.certificates.all()

