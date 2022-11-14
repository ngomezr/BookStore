from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import MainMenu

from .forms import BookForm
from django.http import HttpResponseRedirect

from .models import Book

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

import calendar
from calendar import HTMLCalendar
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event

from .forms import WishListForm
from .models  import WishList
from .models  import ShoppingCart
from .models import ForumPost
from .forms import PostForm

from .forms import SignUpForm

from decimal import *


def index(request):
    return render(request,
                  'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


def about_us(request):
    return render(request,
                  'bookMng/about_us.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


@login_required(login_url=reverse_lazy('login'))
def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # not enough form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/postbook.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def displaybooks(request):
    books = Book.objects.all()
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books
                  })


@login_required(login_url=reverse_lazy('login'))
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]
    return render(request,
                  'bookMng/book_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'book': book
                  })


@login_required(login_url=reverse_lazy('login'))
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/book_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


@login_required(login_url=reverse_lazy('login'))
def search(request):
    if request.method == 'GET':
        searchItem = request.GET.get('search')
        books = Book.objects.all().filter(name=searchItem)
        for b in books:
            b.pic_path = b.picture.url[14:]
        return render(request, 'bookMng/search.html',
                      {
                          'item_list': MainMenu.objects.all(),
                          'books': books
                      })


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day,events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f' <li> {event.title} </li> '

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek,events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d,events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        cal +=f'</table>'
        return cal


class CalendarView(generic.ListView):
    model = Event
    template_name = 'bookMng/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


@login_required(login_url=reverse_lazy('login'))
def wishlist(request):
    submitted = False
    if request.method == 'POST':
        form = WishListForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/wishlist?submitted=True')
    else:
        form = WishListForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'bookMng/wishlist.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def mywishlist(request):
    wishlist1 = WishList.objects.filter(username=request.user)
    return render(request,
                  'bookMng/mywishlist.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'wishlist1': wishlist1
                  })


@login_required(login_url=reverse_lazy('login'))
def wishlist_delete(request, wishlist_id):
    item = WishList.objects.get(id=wishlist_id)
    item.delete()
    return render(request,
                  'bookMng/wishlist_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


@login_required(login_url=reverse_lazy('login'))
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    item = ShoppingCart(name=book.name, web=book.web, price=book.price, publishdate=book.publishdate, picture=book.picture, pic_path=book.pic_path, username=request.user)
    item.save()
    return render(request,
                  'bookMng/add_to_cart.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


@login_required(login_url=reverse_lazy('login'))
def shopping_cart(request):
    books = ShoppingCart.objects.filter(username=request.user)
    rbooks = Book.objects.all();
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/shopping_cart.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'rbooks': rbooks,
                  })


@login_required(login_url=reverse_lazy('login'))
def shopping_cartSum(request):
    submitted = False
    if request.method == 'POST':
        return HttpResponseRedirect('/shopping_cartCheckout?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
        rbooks = ShoppingCart.objects.filter(username=request.user)
        book_sum = 0
        for b in rbooks:
            book_sum += b.price
        tax = 0.0975
        total_tax = round(Decimal(book_sum) * Decimal(tax),2)
        total_sum = total_tax + book_sum
    return render(request,
                  'bookMng/shopping_cartCheckout.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'rbooks': rbooks,
                      'book_sum' : book_sum,
                      'tax' : tax,
                      'total_tax': total_tax,
                      'total_sum': total_sum,
                      'submitted' : submitted
                  })


@login_required(login_url=reverse_lazy('login'))
def cart_delete(request, book_id):
    book = ShoppingCart.objects.get(id=book_id)
    book.delete()
    return render(request,
                  'bookMng/cart_delete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  })


@login_required(login_url=reverse_lazy('login'))
def chat(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect("/chatroom")
    else:
        form = PostForm()

    return render(request, 'bookMng/chatroom.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'chat_list': ForumPost.objects.all(),
                  })