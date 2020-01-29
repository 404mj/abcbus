# from django.contrib.auth import get_user_model
from .models import PersonalFinance

ROOT_DEPTID = 1


def savepf(request):
    large_deposit = request.POST.get('large_deposit')
    precious_metal = request.POST.get('precious_metal')
    found = request.POST.get('found')
    memo = request.POST.get('memo')
    print(memo)
    # user = get_user_model()
    # print(request.user)
    pf = PersonalFinance(large_deposit=large_deposit,
                         precious_metal=precious_metal,
                         found=found,
                         memo=memo,
                         submitter=request.user.id,
                         bank_subbrch=request.user.dept_id
                         )
    pf.save()
    return 0
