from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.db import connection
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def about(request):
    admins = Admins.objects.all()
    return render(request, 'about.html', {'admins':admins})

def account(request):
    return render(request, 'account.html')

def cart(request):
    car = Cart.objects.all()
    return render(request, 'cart.html', {'car':car})

def product(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'product':products})

def support(request):
    return render(request, 'support.html')

def home(request):
    admin = Admins.objects.all()
    products = Products.objects.all()
    return render(request, 'home.html', {'products':products, 'admin':admin})

def details(request, id):
    data = Details.objects.filter(id=id)
    prod = Products.objects.all()
    com = Comments.objects.filter(to_id=id)
    c = Details.objects.filter(id=id)
    return render(request, 'product-details.html', {'data':data, 'prod':prod, 'com':com, 'c':c})

@csrf_exempt
def comm(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        to_id = request.POST['to_id']
        if form.is_valid():
            try:
                form.save()
                return redirect('/details/' + str(to_id))
            except:
                pass
    return redirect('/products/')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        login = request.POST['login']
        em = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['ver_pass']
        email_subject = 'User activation'
        email_body = render_to_string('active.html')
        email = EmailMessage(subject=email_subject, body=email_body,
                             from_email='200103214@stu.sdu.edu.kz',
                             to=[em])
        if pass1 == pass2:
            if Users.objects.filter(login=login).exists():
                print("login name already used")
                return redirect('/')
            else:
                if form.is_valid():
                    try:
                        form.save()
                        print("user created")

                        email.send()
                        return redirect('/home/')
                    except:
                        pass

        else:
            print("invalid password")
            return redirect('/')
    return redirect('/')

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        form = UsersLog(request.POST)
        login = request.POST['login']
        password = request.POST['password']
        data = Users.objects.filter(login=login)
        for q in data:
            if q.password == password:
                return redirect('/products/')
    return redirect('/')

def delete(request, id):
    com = Comments.objects.get(id=id)
    to = com.to_id
    com.delete()
    return redirect("/details/" + str(to))

def edit(request, id):
    com = Comments.objects.get(id=id)
    return render(request, 'edit.html', {'com': com})

@csrf_exempt
def update(request, id):
    id = int(id)
    try:
        post_sel = Comments.objects.get(id=id)
    except Comments.DoesNotExist:
        return redirect('/products/')
    post_form = CommentForm(request.POST or None, instance=post_sel)
    if post_form.is_valid:
        post_form.save()
        return redirect('/products/')
    products = Products.objects.all()
    return render(request, 'products.html', {'product': products})


def admins(request, post_slug):
    post = get_object_or_404(Admins, slug=post_slug)
    context = {'post': post}
    return render(request, 'admins.html', context=context)


@csrf_exempt
def cart_buy(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        pr_id = request.POST['pr_id']
        if form.is_valid():
            try:
                form.save()
                return redirect('/details/' + str(pr_id))
            except:
                pass
    return redirect('/products/')

def dele(request, id):
    com = Cart.objects.get(id=id)
    com.delete()
    return redirect("/cart/")