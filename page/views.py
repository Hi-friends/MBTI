from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from .models import MbtiUser, Match, Joined
from django.db.models import Count
from django.db import connection

# Create your views here.
def register(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        print(form)
        if form.is_valid() :
            user = form.save(commit=False)
            user.save()
            print('user :', user)
            return redirect('list')
    else :
        form = PostForm()
    return render(request, 'page/register.html', {'form': form})

def list(request):
    users = MbtiUser.objects.all()
    return render(request, 'page/list.html', {'users':users})

def entire_list(request):
    total = MbtiUser.objects.count()
    users = MbtiUser.objects.values('mbti1', 'region').annotate(num_mbtis=Count('mbti1')).order_by('-num_mbtis')

    for user in users:
        user['num_mbtis'] = round((user['num_mbtis'] / total)*100, 2)
    return render(request, 'page/entire.html', {'users':users})

def same_list(request):
    user = MbtiUser.objects.last()
    mbti = user.mbti1
    region = user.region
    users = MbtiUser.objects.filter(mbti1=mbti, region = region)
    return render(request, 'page/same.html', {'users':users})

def same_detail(request):
    user = MbtiUser.objects.last()
    mbti = user.mbti1
    region = user.region
    users = MbtiUser.objects.filter(mbti1=mbti, region = region)

    total = users.count()
    ages = users.values('age').annotate(num_ages=Count('age')).order_by('-num_ages')
    for age in ages:
        age['num_ages'] = round((age['num_ages'] / total)*100, 2)
    wholesex = users.values('sex').annotate(num_sex=Count('sex')).order_by('-num_sex')
    for sex in wholesex:
        sex['num_sex'] = round((sex['num_sex'] / total)*100, 2)

    formset = zip(users, ages)
    return render(request, 'page/same_detail.html', {'formset':formset, 'wholesex':wholesex})

def match_list(request):
    user = MbtiUser.objects.last()
    mbti = user.mbti1
    region = user.region
    id = user.id
    matches = Match.objects.filter(mbti1=mbti).order_by('-match_score')
    users = MbtiUser.objects.filter(region = region)
    users = users.exclude(id = id)

    return render(request, 'page/match.html', {'users':users, 'matches':matches})

def match_detail(request):
    user = MbtiUser.objects.last()
    mbti = user.mbti1
    region = user.region
    id = user.id
    matches = Match.objects.filter(mbti1=mbti).order_by('-match_score')
    users = MbtiUser.objects.filter(region = region)
    users = users.exclude(id = id)

    total = users.count()
    mbtis = users.values('mbti1').annotate(num_mbtis=Count('mbti1')).order_by('-num_mbtis')
    for mbti in mbtis:
        mbti['num_mbtis'] = round((mbti['num_mbtis'] / total)*100, 2)

    return render(request, 'page/match_detail.html', {'region':region, 'matches':matches, 'mbtis':mbtis})
