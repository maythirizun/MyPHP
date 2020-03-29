from django.shortcuts import render
from django.http import HttpResponse
from contact import models
from contact.forms import list, new

def list_func(request):

    mitsumori = models.Mitsumori.objects.all()
    if request.method == 'POST':    
        form = list.ListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = list.ListForm()
        context = {
            'form': form,
            'data': mitsumori,
        }

    return render(request, 'contact/est_list.html', context)
