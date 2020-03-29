from django.db import models
from datetime import datetime
from django.db import transaction

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    user_type = models.IntegerField(default=1)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    update_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def update_checklist(request, id):
        with transaction.atomic():
            record = Contact.objects.select_for_update().get(pk=id)
            record.name = request.POST.get('name')
            record.email = request.POST.get('email')
            record.phone = request.POST.get('phone')
            record.address = request.POST.get('address')
            record.message = request.POST.get('message')
            record.save()


class Mitsumori(models.Model):
    name = models.CharField(max_length=100, blank=False)
    request_no = models.CharField(max_length=6, blank=False)
    message = models.CharField(max_length=1000, blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    update_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name


class Departmet(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=False)
    def __str__(self):
        return self.name

class ServiceGroup(models.Model):
    name = models.CharField(max_length=100, blank=False)
    department = models.ForeignKey(Departmet ,on_delete=models.CASCADE,)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100, blank=False)
    service_group = models.ForeignKey(ServiceGroup ,on_delete=models.CASCADE,)
    department = models.ForeignKey(Departmet ,on_delete=models.CASCADE,)
    upload = models.FileField(upload_to = 'uploads/%Y/%m/%d/') 
    def __str__(self):
        return self.name

class MitsumoriService(models.Model):
    mitsumori = models.ForeignKey(Mitsumori, on_delete=models.CASCADE,)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,)
    service_group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE,)
    department = models.ForeignKey(Departmet ,on_delete=models.CASCADE,)


class Mitsumori_Details(models.Model):
    name = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=1000, blank=True)
    m_file = models.FileField(upload_to = 'create/%Y/%m/%d/', blank=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    update_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
