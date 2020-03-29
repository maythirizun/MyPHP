from django.shortcuts import render
from django.http import HttpResponse
from contact.models import Contact

def index(request):
    return render(request, 'contact/contact.html')

def checklist(request):
    list = Contact.objects.all()
    teams = [
        '3',
        '8'
    ]
    context = {
        'list' : list,
        'teams': teams,
    }
    return render(request, 'contact/list.html', context)

def register(request):
    record = Contact()
    record.name = request.POST.get('name')
    record.email = request.POST.get('email')
    record.phone = request.POST.get('phone')
    record.address = request.POST.get('address')
    record.message = request.POST.get('message')
    record.save()
    context = {
        
    }
    return render(request, 'contact/contact.html')

def update(request, id):
    if request.method=='GET':
        record = Contact.objects.get(id=id)
        context = {
            'record' : record,
        }
        return render(request, 'contact/contact.html', context)
    else:
        # Must be in a transaction to grab a lock
        # with transaction.atomic():
        #     record = Contact.objects.select_for_update().filter(id = id)
        #     record.name = request.POST.get('name')
        #     # record.save()
        #     record.email = request.POST.get('email')
        #     record.phone = request.POST.get('phone')
        #     record.address = request.POST.get('address')
        #     record.message = request.POST.get('message')
        #     record.update()
        context = {

        }
        Contact.update_checklist(request, id)
        return render(request, 'contact/list.html', context)

