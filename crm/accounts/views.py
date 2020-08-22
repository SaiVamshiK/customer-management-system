from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm,UserRegistrationForm,CustomerForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group


# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    pending_orders=Order.objects.filter(status='Pending').count()
    delivered_orders = Order.objects.filter(status='Delivered').count()
    content={
        'orders':orders,
        'customers':customers,
        'total_customers':total_customers,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    }
    return render(request,'accounts/dashboard.html',content)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    total_orders=orders.count()
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs
    context={
        'customer':customer,
        'orders':orders,
        'count':total_orders,
        'myFilter':myFilter
    }
    return render(request,'accounts/customers.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    cur_cust=Customer.objects.get(id=pk)
    form=OrderForm(initial={'customer':cur_cust})
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/order_form.html',{'form':form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    cur_order=Order.objects.get(id=pk)
    form=OrderForm(instance=cur_order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=cur_order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/order_form.html',{'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    cur_order=Order.objects.get(id=pk)
    if request.method=='POST':
        cur_order.delete()
        return redirect('/')
    return render(request,'accounts/delete.html',{'order':cur_order})

@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            u=form.cleaned_data.get('username')
            messages.success(request,f'Account successfully created for {u}')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders=request.user.customer.order_set.all()
    total_orders = orders.count()
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    context={
        'orders':orders,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    }
    return render(request,'accounts/user.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountsettings(request):
    user=request.user.customer
    form=CustomerForm(instance=user)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'accounts/account_settings.html',context)








