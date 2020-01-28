from django.shortcuts import render
from .forms import PersonalFinanceForm
from .models import PersonalFinance, BankUser
from .service import savepf
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404


# 添加个金数据
def add_pf(request):
    if request.method == 'POST':
        form = PersonalFinanceForm(request.POST)
        if form.is_valid():
            res = savepf(request)
            # if res > 0:
            return HttpResponseRedirect('/collect/pf/list')
    else:
        form = PersonalFinanceForm()
    return render(request, 'collect/newpf.html', {'form': form, 'name': 'zsx'})


def list_pf(request):
    pfs = PersonalFinance.objects.order_by('-submit_time')
    # submit_name = BankUser.objects.filter(id=pfs[0].submitter)
    return render(request, 'collect/listpf.html', {'pfs': pfs})


def edit_pf(request, pfid):
    pass
