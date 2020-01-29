from django.shortcuts import render, get_object_or_404
from .forms import PersonalFinanceForm
from .models import PersonalFinance, BankUser
from .service import savepf
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# from django.template import loader
# from django.http import Http404

PAGENUM = 3


# 添加个金数据
@login_required
def add_pf(request):
    if request.method == 'POST':
        form = PersonalFinanceForm(request.POST)
        if form.is_valid():
            res = savepf(request)
            # if res > 0:
            return HttpResponseRedirect('/collect/pf/list')
    else:
        form = PersonalFinanceForm()
    return render(request, 'collect/newpf.html', {'form': form})


@login_required
def list_pf(request):
    pflist = PersonalFinance.objects.all().order_by('-submit_time')
    paginator = Paginator(pflist, PAGENUM)
    page = request.GET.get('page')
    try:
        pfs = paginator.page(page)
    except PageNotAnInteger:
        pfs = paginator.page(1)
    except EmptyPage:
        pfs = paginator.page(paginator.num_pages)
    return render(request, 'collect/listpf.html', {'pfs': pfs})


@login_required
def edit_pf(request, pfid):
    pf_instance = get_object_or_404(PersonalFinance, pfid=pfid)
    form = PersonalFinanceForm(request.POST or None, instance=pf_instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collect/pf/list')
    return render(request, 'collect/newpf.html', {'form': form})


@login_required
def delete_pf(request, pfid):
    print(pfid)
    PersonalFinance.objects.filter(pfid=pfid).delete()
    pflist = PersonalFinance.objects.all().order_by('-submit_time')
    paginator = Paginator(pflist, PAGENUM)
    page = request.GET.get('page')
    try:
        pfs = paginator.page(page)
    except PageNotAnInteger:
        pfs = paginator.page(1)
    except EmptyPage:
        pfs = paginator.page(paginator.num_pages)
    return render(request, 'collect/listpf.html', {'pfs': pfs})


@login_required
def summary_pf(request):
    pass
