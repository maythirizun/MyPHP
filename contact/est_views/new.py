from django.shortcuts import render
from django.http import HttpResponse
from contact import models
from contact.forms import list, new
import json
from django.core import serializers

def new_func(request):
    service = models.Service.objects.all()    
    if request.method == 'POST':    
        form = new.UpdateForm(request.POST)
        sv_list = [int(sid) for sid in request.POST.getlist('sv_check')]

        if form.is_valid() and sv_list:
            try:
                with transaction.atomic():
                    # mitsumori
                    upd_mitsumori(mitsumori, form)
                    mitsumori.save()
                    # mitsumori_sv
                    msv = models.MitsumoriService.objects.filter(mitsumori=pk).delete()
                    for sid in sv_list:
                        msv = upd_mitsumori_sv(mitsumori, sid)
                        msv.save()
                    # add_mitsumori_dtl

                    # send_mail
                    #if(mail ststus is checked)
                    #   send mail
                    #else
                    #   not send mail
            except IntegrityError as e:
                print(e)
                # handle exception
                pass
            
            return HttpResponseRedirect('/contact/estimates/list')
        else:
            pass           

    else:
        if 'update_to_copy' in request.session:
            context = request.session['update_to_copy']
            sv_list = context.get('service')

            for obj in serializers.deserialize('json', context.get('mitsumori')):
                mitsumori = obj.object
            initials = {
                'request_no': mitsumori.request_no,
                'name': mitsumori.name,
                'message': mitsumori.message,
                'create_date': mitsumori.create_date,
                'update_date': mitsumori.update_date
            }        
            form = new.UpdateForm(initials)

    context = {
        'form': form,
        'service': service,
        'sv_list': sv_list,
    }
    return render(request, 'contact/est_new.html', context)

def create_mitsumori(mitsumori, form):
    mitsumori.name = form['name'].data
    mitsumori.request_no = form['request_no'].data
    mitsumori.message = form['message'].data
    mitsumori.create_date = datetime.datetime.now()
    mitsumori.update_date = datetime.datetime.now()


def create_mitsumori_sv(mitsumori, service_id):
    #create new record
    service = models.Service.objects.get(pk=service_id)
    msv = models.MitsumoriService()
    msv.mitsumori = mitsumori
    msv.service = service.id
    msv.service_group = service.service_group
    msv.department_id = service.department_id
    return msv


def create_mitsumori_dtls():
    pass

