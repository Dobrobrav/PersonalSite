from rest_framework import serializers


class MainInfoSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    middle_name = serializers.CharField(max_length=30)
    department_name = serializers.CharField(source='department.name')


class ContactDetailsSerializer(serializers.Serializer):
    country = serializers.CharField(max_length=60, source='office.address.country')
    region = serializers.CharField(max_length=60, source='office.address.region')
    locality = serializers.CharField(max_length=70, source='office.address.locality')
    street_name = serializers.CharField(max_length=130, source='office.address.street_name')
    street_number = serializers.IntegerField(source='office.address.street_number')
    postcode = serializers.IntegerField(source='office.postcode')
    telephone_extension = serializers.IntegerField(source='contact_details.telephone_extension')
    work_phone_number = serializers.CharField(max_length=17, source='contact_details.work_phone_number')
    additional_phone_number = serializers.CharField(max_length=17, source='contact_details.additional_phone_number')
    link_to_photo = serializers.CharField(max_length=100)
    telegram_name = serializers.CharField(max_length=35, source='contact_details.telegram_name')
    link_to_telegram = serializers.CharField(max_length=100, source='contact_details.link_to_telegram')
    link_to_vk = serializers.CharField(max_length=100, source='contact_details.link_to_vk')
