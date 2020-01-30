from django.shortcuts import render, get_object_or_404
from .forms import PersonalFinanceForm
from .models import PersonalFinance, BankUser, Dept
from .service import savepf
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# from django.template import loader
# from django.http import Http404

PAGENUM = 3


# ======================== 添加个金数据 =======================
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


# ==================== 提交记录列表 ======================#
@login_required
def list_pf(request):
    from django.contrib.auth.models import Permission
    # permissions = Permission.objects.filter(user=request.user)
    # group_permissions = Permission.objects.filter(group__user=request.user)
    # perm_tuple = [(x.id, x.name) for x in permissions]
    # gperm_tuple = [(x.id, x.name) for x in group_permissions]
    # print('========>')
    # print(perm_tuple)
    # print(gperm_tuple)
    # print(request.user.has_perm('collect.add_personalfinance'))
    # print(request.user.has_add_perm(PersonalFinance))

    user_dept = Dept.objects.filter(dept_id=request.user.dept_id).first()
    # 三级网点只显示自己提交的，二级支行显示自己和下属提交的，一级分行全部显示
    if user_dept.level == 1:
        pflist = PersonalFinance.objects.all().order_by('-submit_time')
    elif user_dept.level == 2:
        depts_l2 = Dept.objects.raw('select dept_id from collect_dept where level=3 and parent = %s',
                                    [user_dept.dept_id])
        deptl2_list = [obj.dept_id for obj in depts_l2]
        deptl2_list.append(user_dept.dept_id)
        pflist = PersonalFinance.objects.filter(bank_subbrch__in=deptl2_list).order_by('-submit_time')
    else:
        pflist = PersonalFinance.objects.filter(bank_subbrch=user_dept.dept_id).order_by('-submit_time')

    paginator = Paginator(pflist, PAGENUM)
    page = request.GET.get('page')
    try:
        pfs = paginator.page(page)
    except PageNotAnInteger:
        pfs = paginator.page(1)
    except EmptyPage:
        pfs = paginator.page(paginator.num_pages)
    return render(request, 'collect/listpf.html', {'pfs': pfs})


# ==================== 修改已提交数据 ======================#
@login_required
def edit_pf(request, pfid):
    pf_instance = get_object_or_404(PersonalFinance, pfid=pfid)
    form = PersonalFinanceForm(request.POST or None, instance=pf_instance)
    if request.method == 'POST':
        pf_instance.change_times = 1
        form = PersonalFinanceForm(request.POST or None, instance=pf_instance)
        form.save()
        return HttpResponseRedirect('/collect/pf/list')
    return render(request, 'collect/newpf.html', {'form': form})


# ==================== 删除某条提记录 ======================#
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


# ==================== 报表统计 ======================#
@login_required
def summary_pf(request):
    pass
