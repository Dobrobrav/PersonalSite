from utils.utils import query_debugger
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
        serializer_obj = MainInfoSerializer(profile)
        return Response(serializer_obj.data)


class ContactDetailsAPIView(APIView):
    @query_debugger
    def get(self, request):
        profile_id = request.data['profile_id']
        profile = Profile.objects \
            .select_related('contact_details', 'office__address') \
            .get(pk=profile_id)

        serializer_obj = ContactDetailsSerializer(profile)
        return Response(serializer_obj.data)


class InterestsAPIView(APIView):
    @query_debugger
    def get(self, request):
        profile_id = request.data['profile_id']
        profile = Profile.objects.get(pk=profile_id)
        serializer_obj = InterestsSerializer(profile)
        return Response(serializer_obj.data)


class CertificatesAPIView(APIView):
    @query_debugger
    def get(self, request):
        profile_id = request.data['profile_id']
        profile = Profile.objects.get(pk=profile_id)
        certificates_serializer = CertificatesSerializer(profile)
        return Response(certificates_serializer.data)
