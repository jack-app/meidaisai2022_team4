import uuid

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Year, Month, Week, Event
from .forms import EventPostForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from account.models import Account # ユーザーアカウントデータベース
# Create your views here.

# 年を取得
def get_years(UserID):
    year_list = Year.objects.filter(user_id = UserID)
    return year_list

# 月を取得
def get_months(YearList):
    month_list = []
    for year in YearList:
        month_list += Month.objects.filter(year_id = year)
    return month_list

# 週を取得
def get_weeks(MonthList):
    week_list = []
    for month in MonthList:
        week_list += Week.objects.filter(month_id = month)
    return week_list

# イベントを取得
def get_events(UserID):
    # ユーザごとのイベントを日付順で取得
    event_list = Event.objects.filter(user_id = UserID).order_by("date")
    event_vector = []
    event_len = len(event_list)
    i = 0
    j = 0
    k = 1
    l = 1
    while(i < event_len):
        year = event_list[i].date.year
        event_vector.append([])
        event_vector[j].append(year)
        while(i < event_len and year == event_list[i].date.year):
            month = event_list[i].date.month
            event_vector[j].append([])
            event_vector[j][k].append(month)
            while(i < event_len and year == event_list[i].date.year and month == event_list[i].date.month):
                day = event_list[i].date.day
                event_vector[j][k].append([])
                event_vector[j][k][l].append(day)
                while(i < event_len and year == event_list[i].date.year and month == event_list[i].date.month and day == event_list[i].date.day):
                    event_vector[j][k][l].append(event_list[i])
                    i += 1
                l += 1
            k += 1
            l = 1
        j += 1
        k = 1
        l  = 1
    return event_vector

def set_submit_token(request):
    submit_token = str(uuid.uuid4())
    request.session['submit_token'] = submit_token
    return submit_token

def exists_submit_token(request):
    token_in_request = request.POST.get('submit_token')
    token_in_session = request.session.pop('submit_token', '')

    if not token_in_request:
        return False
    if not token_in_session:
        return False

    return token_in_request == token_in_session

def user_params(cur_user, userid, request):
    # ユーザごとに情報を取得
    # year_list = get_years(cur_user)
    # month_list = get_months(year_list)
    # week_list = get_weeks(month_list)
    event_list = get_events(cur_user)



    params = {"UserID":userid, 
              "display_name":cur_user.display_name, 
            #   "year_list": year_list, 
            #   "month_list": month_list,
            #   "week_list": week_list,
              "event_list": event_list,
              "form": EventPostForm(),
               }
    return params


#ホーム
@login_required
def home(request):

    # アクセスしたユーザの情報を取得
    userid = request.user
    cur_user = Account.objects.get(user_id=userid)

    if request.method == 'POST':
        if exists_submit_token(request):
            form = EventPostForm(request.POST)
            tag = form.save(commit=False)
            tag.user_id = cur_user
            tag.save()
            # return HttpResponse(f'{post.id}', status=200)

    # ユーザに応じてDBから表示する情報を取得
    params = user_params(cur_user, userid, request)
    # 多重送信用
    params['submit_token'] = set_submit_token(request)
    return render(request, "timeline/home.html",context=params)

@require_POST
def delete_event(request, event_id):
    memo = get_object_or_404(Event, id=event_id)
    memo.delete()
    return redirect('home')

