from django.shortcuts import render
from .models import Year, Month, Week, Event
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
def get_events(WeekList):
    event_list = []
    for week in WeekList:
        event_list += Event.objects.filter(week_id = week)
    return event_list


