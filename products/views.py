from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product, Vote, Reply


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':

        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] \
                and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('https://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'https://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # vote = get_object_or_404(Vote, voter=User, product=product)
        # if not vote:
        product_name = Product.title
        user_name = User.username
        if not Vote.objects.filter(product__title__contains=product_name, voter__username__contains=user_name).exists():
            print("Here we are")
            product.votes_total += 1
            product.save()
            vote = Vote()
            # user = User.objects.get(username=user_name)
            vote.voter = request.user
            vote.product = product
            vote.save()
        else:
            print("Object already there")
    return redirect('/products/' + str(product.id))


@login_required(login_url="/accounts/signup")
def reply(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        replyObj = Reply()
        replyObj.body = request.POST.get('val', False)
        replyObj.forProduct = product
        replyObj.save()
        return redirect('/products/' + str(product.id))
    else:
        return render(request, 'products/reply.html', {'product': product})
