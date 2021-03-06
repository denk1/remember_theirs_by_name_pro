from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from remember_theirs_by_name_pro.models import Person
from remember_theirs_by_name_pro.data import fill_new_line
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html')


@login_required
def data_input(request):
    return render(request, 'data_input.html')


def persons_listing(request):
    persons_list = Person.objects.all()
    paginator = Paginator(persons_list, 25)
    page = request.GET.get('page')
    is_new_item = request.POST.get('is_new_item')
    if is_new_item is not None and int(is_new_item) == 1:
        fill_new_line(request.POST)
    persons = paginator.get_page(page)
    return render(request,'persons_list.html', {'persons': persons})

