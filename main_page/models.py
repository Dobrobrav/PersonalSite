from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=60)
    region = models.CharField(max_length=60, blank=True, null=True)
    locality = models.CharField(max_length=70)
    street_name = models.CharField(max_length=130)
    street_number = models.IntegerField()
    apartment_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.street_name} {self.street_number} {self.apartment_number}"


class ContactDetails(models.Model):
    telephone_extension = models.CharField(max_length=10, blank=True, null=True)
    work_phone_number = models.CharField(max_length=17, blank=True, null=True)
    additional_phone_number = models.CharField(max_length=17, blank=True, null=True)
    telegram_name = models.CharField(max_length=35, blank=True, null=True)
    link_to_telegram = models.URLField(blank=True, null=True)
    link_to_vk = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.work_phone_number)


class Department(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Office(models.Model):
    address = models.ForeignKey(Address, models.DO_NOTHING)
    postcode = models.IntegerField()

    def __str__(self):
        return f"office on {self.address}"


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    office = models.ForeignKey(Office, models.DO_NOTHING, blank=True, null=True)
    contact_details = models.ForeignKey(ContactDetails, models.DO_NOTHING)
    link_to_photo = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Interest(models.Model):
    name = models.CharField(max_length=50)
    link_to_picture = models.URLField(blank=True, null=True)
    profiles = models.ManyToManyField(Profile, related_name='interests')

    def __str__(self):
        return self.name


class Certificates(models.Model):
    name = models.CharField(max_length=150)
    link_to_picture = models.URLField(blank=True, null=True)
    profiles = models.ManyToManyField(Profile, related_name='certificates')

    def __str__(self):
        return self.name
