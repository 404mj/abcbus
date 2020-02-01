# from django.contrib.auth import get_user_model
from .models import PersonalFinance
import xlwt
from django.http import HttpResponse

ROOT_DEPTID = 1


def savepf(request):
    large_deposit = request.POST.get('large_deposit')
    precious_metal = request.POST.get('precious_metal')
    found = request.POST.get('found')
    memo = request.POST.get('memo')
    # print(memo)
    # user = get_user_model()
    # print(request.user)
    pf = PersonalFinance(large_deposit=large_deposit,
                         precious_metal=precious_metal,
                         found=found,
                         memo=memo,
                         submitter=request.user.id,
                         submitter_name=request.user.username,
                         bank_subbrch=request.user.dept_id
                         )
    pf.save()
    return 0


def statpf(request):
    response = HttpResponse(content_type='application/ms-excel')
    summary_date = request.POST.get('summary_date')
    fname = str(summary_date) + str(request.user.dept_id) + '.xls'
    response['Content-Disposition'] = 'attachment; filename=%s' % fname

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("sheet1")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    '''
    # dummy method to fetch data.
    data = get_data()  
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.name, font_style)
        ws.write(row_num, 1, my_row.start_date_time, font_style)
        ws.write(row_num, 2, my_row.end_date_time, font_style)
        ws.write(row_num, 3, my_row.notes, font_style)
'''
    wb.save(response)
    return response
