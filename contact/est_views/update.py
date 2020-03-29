from django.db import IntegrityError, transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from contact import models
from contact.forms import list, new
from django.core import serializers

@transaction.atomic
def update_func(request, pk):

    mitsumori = models.Mitsumori.objects.get(pk=pk)
    service = models.Service.objects.all()
    
    if request.method == 'POST':    
        form = new.UpdateForm(request.POST)
        sv_list = [int(sid) for sid in request.POST.getlist('sv_check')]
        
        if 'copy' in request.POST:            
            context = {
                'service': sv_list,
                'mitsumori': serializers.serialize('json', [mitsumori,]),
            }
            request.session['update_to_copy'] = context
            request.session.modified = True
            return HttpResponseRedirect('/contact/estimates/new')

        elif 'update' in request.POST:
            mitsumori = models.Mitsumori.objects.select_for_update().get(pk=pk)
            print('update')
        elif 'delete' in request.POST:
            print('delete')

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
        'pk': pk,
        'service': service,
    }

    return render(request, 'contact/est_update.html', context)


def upd_mitsumori(mitsumori, form):
    mitsumori.name = form['name'].data
    mitsumori.request_no = form['request_no'].data
    mitsumori.message = form['message'].data
    mitsumori.update_date = datetime.datetime.now()


def upd_mitsumori_sv(mitsumori, service_id):
    #create new record
    service = models.Service.objects.get(pk=service_id)
    msv = models.MitsumoriService()
    msv.mitsumori = mitsumori
    msv.service = service
    msv.service_group = service.service_group
    msv.department_id = service.department_id
    return msv


def create_mitsumori_dtls():
    pass

