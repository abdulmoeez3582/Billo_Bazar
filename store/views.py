import datetime

import shortuuid as shortuuid
from django.core.files.images import get_image_dimensions
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.db.models import Count
from django.core import serializers

from store.models import Orders
from store.models.category import Category
from store.models.product import Product
from store.models.customer import Customer
from store.models.address_book import Address_Book
from django.core.mail import send_mail
from django.contrib.auth import login as auth_login

# Create your views here.
class Index(View):
    def post(self,request):
        pId = request.POST.get('productId')
        rId = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pId)
            if quantity:
                if rId:
                    if quantity <= 1:
                        cart.pop(pId)
                    else:
                        cart[pId] = quantity - 1
                else:
                    cart[pId] = quantity + 1
            else:
                cart[pId] = 1
        else:
            cart = {}
            cart[pId] = 1

        request.session['cart'] = cart
        return redirect('/')

    def get(self_, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = Product.feature_products()

        category1 = Category.category1()
        category_id1 = None
        category_id1 = Product.category_id1()
        category2 = Category.category2()
        category_id2 = None
        category_id2 = Product.category_id2()
        category3 = Category.category3()
        category_id3 = None
        category_id3 = Product.category_id3()
        category4 = Category.category4()
        category_id4 = None
        category_id4 = Product.category_id4()
        category5 = Category.category5()
        category_id5 = None
        category_id5 = Product.category_id5()
        category6 = Category.category1()
        category_id6 = None
        category_id6 = Product.category_id6()
        category7 = Category.category7()
        category_id7 = None
        category_id7 = Product.category_id7()
        category8 = Category.category8()
        category_id8 = None
        category_id8 = Product.category_id8()
        category9 = Category.category9()
        category_id9 = None
        category_id9 = Product.category_id9()
        category10 = Category.category10()
        category_id10 = None
        category_id10 = Product.category_id10()
        data = {}
        data['products'] = product
        data['justlaunch'] = Product.justLaunch()
        data['category_1'] = category_id1
        data['category1'] = category1
        data['category_2'] = category_id2
        data['category2'] = category2
        data['category_3'] = category_id3
        data['category3'] = category3
        data['category_4'] = category_id4
        data['category4'] = category4
        data['category_5'] = category_id5
        data['category5'] = category5
        data['category_6'] = category_id6
        data['category6'] = category6
        data['category_7'] = category_id7
        data['category7'] = category7
        data['category_8'] = category_id8
        data['category8'] = category8
        data['category_9'] = category_id9
        data['category9'] = category9
        data['category_10'] = category_id10
        data['category10'] = category10
        if cart:
            ids = list(request.session.get('cart').keys())
            products = Product.getProductById(ids)
            data['product'] = products
        return render(request, 'user_dir/user_index.html', data)

def single_product(request,id):
    data ={}
    cart = request.session.get('cart')
    data['products'] = Product.objects.all().filter(id=id)
    if cart:
        ids = list(request.session.get('cart').keys())
        products = Product.getProductById(ids)
        data['product'] = products
    return render(request, 'user_dir/single-product.html',data)

def single_page_cart(request):
    pId = request.POST.get('productId')
    rId = request.POST.get('remove')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(pId)
        if quantity:
            if rId:
                if quantity <= 1:
                    cart.pop(pId)
                else:
                    cart[pId] = quantity - 1
            else:
                cart[pId] = quantity + 1
        else:
            cart[pId] = 1
    else:
        cart = {}
        cart[pId] = 1
    request.session['cart'] = cart
    url = f'/products/{pId}'
    return redirect(url)

class Cart(View):
    def get(self, request):
        Cart = request.session.get('cart')
        if not Cart:
            request.session['cart'] = {}
        ids = list(Cart.keys())
        products = Product.getProductById(ids)
        print(Cart)
        return render(request, 'user_dir/cart.html', {'product':products})
    def post(self, request):
        pId = request.POST.get('productId')
        rId = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pId)
            if quantity:
                if rId:
                    if quantity <= 1:
                        cart.pop(pId)
                    else:
                        cart[pId] = quantity - 1
                else:
                    cart[pId] = quantity + 1
            else:
                cart[pId] = 1
        else:
            cart = {}
            cart[pId] = 1

        request.session['cart'] = cart
        return redirect('/cart')
class Checkout(View):
    def get(self, request):
        try:
            if request.session['customerAdmin'] == 1:
                Customer_id = request.session.get('customerId')
                customer_data = Customer.customer(Customer_id)
                Cart = request.session.get('cart')
                ids = list(Cart.keys())
                address = Address_Book.objects.all().filter(customer=Customer_id)
                products = Product.getProductById(ids)
                data ={}
                data['product'] = products
                data['address'] = address
                return render(request,'user_dir/checkout.html',data)
        except:
            return redirect('/login')
        else:
            return redirect('/')
    def post(self, request):
        pId = request.POST.get('productId')
        rId = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pId)
            if quantity:
                if rId:
                    if quantity <= 1:
                        cart.pop(pId)
                    else:
                        cart[pId] = quantity - 1
                else:
                    cart[pId] = quantity + 1
            else:
                cart[pId] = 1
        else:
            cart = {}
            cart[pId] = 1

        request.session['cart'] = cart
        return redirect('/checkout')

def ship_address(request):
    ship_fname = request.POST.get('ship_fname')
    ship_lname = request.POST.get('ship_lname')
    ship_street = request.POST.get('ship_street')
    ship_street1 = request.POST.get('ship_street1')
    ship_street2 = request.POST.get('ship_street2')
    country = request.POST.get('country')
    state = request.POST.get('state')
    city = request.POST.get('city')
    ship_zipcode = request.POST.get('ship_zipcode')
    ship_phone = request.POST.get('ship_phone')
    customer = request.session.get('customerId')

    shipping_address = Address_Book(customer=Customer(id=customer),first_name=ship_fname,last_name=ship_lname,phone=ship_phone,address1=ship_street,address2=ship_street1,address3=ship_street2,country=country,city=city,state=state,postal_code=ship_zipcode)
    shipping_address.insert()
    return redirect('/address-book')


def myaccount(request):
    try:
        if request.session['customerAdmin'] == 1:
            session_id = request.session.get('customerId')
            customer = Customer.customer(session_id)
            address = Address_Book.objects.all().filter(customer=session_id)
            print(address)
            data ={}
            data['customer']= customer
            data['address']= address
            print(address)
            return render(request,'user_dashboard/myaccount.html', data)
    except:
        return redirect('/login')

def account_information(request):
    try:
        if request.session['customerAdmin'] == 1:
            session_id = request.session.get('customerId')
            customer = Customer.customer(session_id)
            data = {}
            data['customer'] = customer
            return render(request,'user_dashboard/edit-account.html', data)
    except:
        return redirect('/login')

def address_book(request):
    try:
        if request.session['customerAdmin'] == 1:
            session_id = request.session.get('customerId')
            customer = Customer.customer(session_id)
            data = {}
            data['customer'] = customer
            return render(request, 'user_dashboard/address-book.html', data)
    except:
        return redirect('/login')

def update_address(request):
    if request.method == 'POST':
        session_id = request.session.get('customerId')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        phone = request.POST.get('phone')
        add1 = request.POST.get('add1').strip()
        add2 = request.POST.get('add2').strip()
        add3 = request.POST.get('add3').strip()
        country = request.POST.get('country').strip()
        state = request.POST.get('state').strip()
        city = request.POST.get('city').strip()
        zip_code = request.POST.get('zip_code').strip()
        customer = Customer.objects.get(id=session_id)
        address = Address_Book(customer=customer,first_name=first_name,last_name=last_name,phone=phone,address1=add1,address2=add2,address3=add3,country=country,state=state,city=city,postal_code=zip_code)
        address.insert()
        print(address,customer,session_id)
        return redirect('/myaccount')
    else:
        return redirect('/address-book')
data1=''
total=''
gtotal=''
def order(request):
    billing_address = ' '

    s = shortuuid.ShortUUID(alphabet="0123456789")
    order_id = s.random(length=6)
    customer = request.session.get('customerId')
    Existing_Address = request.POST.get('existing_address')
    Same_Billing_address = request.POST.get('billing_same')
    Pay_Method = request.POST.get('paymentmode')
    if Existing_Address:
        if Same_Billing_address:
            billing_add = Address_Book.objects.all().filter(id=Existing_Address)
            for a in billing_add:
                add1 = a.address1
                add2 = a.address2
                add3 = a.address3
                country = a.country
                state = a.state
                city = a.city
                post_code = a.postal_code
                phone = a.phone
            billing_address = str(add1)+" "+str(add2)+" "+str(add3)+" "+str(country)+" "+str(state)+" "+str(city)+" "+str(post_code)+" "+str(phone)
            cart = request.session.get('cart')
            products = Product.getProductById(list(cart.keys()))
            order_id_fetch = Orders.objects.all().filter(order_num=order_id)
            if order_id_fetch:
                order_id = s.random(length=6)
            for p in products:
                order = Orders(customer=Customer(id=customer), product=Product(id=p.id), price=p.price,quantity=cart.get(str(p.id)),
                               shipping_address=Address_Book(id=Existing_Address),order_num=order_id,payment_method=Pay_Method ,billing_address=billing_address)
                order.order()
            data1 = Orders.objects.filter(order_num=order_id)


            print(billing_address)
            a=[]
            r=range(0,len(data1),1)
            for x in r:
                print(x)
            # for o in data1:
            #    a[] = o.price * o.quantity
            # print(a)
            del cart
            data_set = {}
            data_set['data1'] = data1
            data_set['order_id'] = order_id
            return redirect('/confirmation')
        else:
            Existing_Address = request.POST.get('existing_address')
            session_id = request.session.get('customerId')
            first_name = request.POST.get('bship_fname')
            last_name = request.POST.get('bship_lname')
            phone = request.POST.get('bship_phone')
            add1 = request.POST.get('bship_street').strip()
            add2 = request.POST.get('bship_street1').strip()
            add3 = request.POST.get('bship_street2').strip()
            country = request.POST.get('bcountry').strip()
            state = request.POST.get('bstate').strip()
            city = request.POST.get('bcity').strip()
            zip_code = request.POST.get('bship_zipcode').strip()
            customer = request.session.get('customerId')
            address = Address_Book(customer=Customer(id=customer), first_name=first_name, last_name=last_name, phone=phone,
                                   address1=add1, address2=add2, address3=add3, country=country, state=state, city=city,
                                   postal_code=zip_code)
            address.insert()
            billing_address = str(add1) + " " + str(add2) + " " + str(add3) + " " + str(country) + " " + str(
                state) + " " + str(city) + " " + str(zip_code) + " " + str(phone)
            print("new billing address and exisiting address")
            cart = request.session.get('cart')
            products = Product.getProductById(list(cart.keys()))
            data1=Orders.objects.filter(order_num=order_id)

            print(customer)
            print(Pay_Method)

            for p in products:
                order = Orders(customer=Customer(id=customer), product=Product(id=p.id), price=p.price,
                               quantity=cart.get(str(p.id)),
                               shipping_address=Address_Book(id=Existing_Address), order_num=order_id,
                               payment_method=Pay_Method, billing_address=billing_address)
                order.order()
            data1 = Orders.objects.filter(order_num=order_id)

            print(billing_address)
            a = []
            r = range(0, len(data1), 1)
            for x in r:
                print(x)
            # for o in data1:
            #    a[] = o.price * o.quantity
            # print(a)
            del cart
            data_set = {}
            data_set['data1'] = data1
            data_set['order_id'] = order_id
            return redirect('/confirmation')
    else:
        print("logic failed")
    return render(request,'user_dir/confirmation.html')

def confirmation(request):
    cart = request.session.get('cart')
    customer = request.session.get('customerId')
    orders = Orders.objects.all().filter(customer=customer)
    order_num = ''
    for o in orders:
        order_num = o.order_num
    order_data = Orders.objects.all().filter(order_num=order_num)
    data={}
    order_number = ''
    amount=0;
    for odata in order_data:
        order_number = odata.order_num
        price=odata.price*odata.quantity
        amount+=price

    data['order_data']=order_data
    data['order_total'] = amount
    data['order_id'] = order_number
    del request.session['cart']
    return render(request,'user_dir/confirmation.html',data)

def track_order(request):
    return render(request, 'user_dir/track_order.html')
def track_order_detail(request,order_id):
    order_detail = Orders.objects.filter(order_num=order_id).all()
    for od in order_detail:
        print(od)
    data = serializers.serialize("json",order_detail)
    return JsonResponse(data,safe=False)

def add_new_address(request):
    session_id = request.session.get('customerId')
    first_name = request.POST.get('ship_fname')
    last_name = request.POST.get('ship_lname')
    phone = request.POST.get('ship_phone')
    add1 = request.POST.get('ship_street').strip()
    add2 = request.POST.get('ship_street1').strip()
    add3 = request.POST.get('ship_street2').strip()
    country = request.POST.get('country').strip()
    state = request.POST.get('state').strip()
    city = request.POST.get('city').strip()
    zip_code = request.POST.get('ship_zipcode').strip()
    customer = Customer.objects.get(id=session_id)
    address = Address_Book(customer=customer, first_name=first_name, last_name=last_name, phone=phone,
                               address1=add1, address2=add2, address3=add3, country=country, state=state, city=city,
                               postal_code=zip_code)
    address.insert()
    return redirect('/checkout')
def myorder(request):
    data={}
    Session = request.session.get('customerId')
    order = Orders.objects.all().filter(customer=Session)
    data['order'] = order
    return render(request,'user_dashboard/myorder.html',data)

def insert_category(request):
    if request.session['customerAdmin'] == 0:
        name= request.post('cat_name')
        parent = request.post('parent')
        slug = request.post('slug')
        if parent == '':
            cat = Category(name=name,slug=slug,level=0,parent_id=parent)
        cat.save()
    else:
        return redirect('/')

def add_category(request,hierarchy = ''):
    if request.session['customerAdmin'] == 0:
        category_slug = hierarchy.split('/')
        parent = None
        root = Category.objects.all()

        instance=''

        for slug in category_slug[:-1]:
            parent = root.get(parent=parent, slug=slug)
            instance = Category.objects.get(parent=parent, slug=category_slug[-1])
            return render(request, 'add_category.html', {'instance': instance})

        return render(request,'add_category.html',{'instance': root})
    else:
        return redirect('/')

def show_category(request,hierarchy = ''):
    if request.session['customerAdmin'] == 0:
        category_slug = hierarchy.split('/')
        parent = None
        root = Category.objects.all()

        instance = ''

        for slug in category_slug[:-1]:
            parent = root.get(parent=parent, slug=slug)
            instance = Category.objects.get(parent=parent, slug=category_slug[-1])
            return render(request, 'categories.html', {'instance': instance})

        return render(request, 'categories.html', {'instance': root})
    return redirect('/')

def add_products(request,hierarchy = ''):
    if request.session['customerAdmin'] == 0:
        category_slug = hierarchy.split('/')
        parent = None
        root = Category.objects.all()
        instance = ''

        for slug in category_slug[:-1]:
            parent = root.get(parent=parent, slug=slug)
            instance = Category.objects.get(parent=parent, slug=category_slug[-1])
            return render(request, 'add_products.html', {'instance': instance})

        if request.method == 'POST':
            data = request.POST
            product_name= data.get('product_name')
            category = data.get('category')
            product_sku = data.get('product_sku')
            description = data.get('description')
            price = data.get('price')
            sale_price = data.get('sale_price')
            product_image = request.FILES.get('product_image')
            product = Product(name=product_name,category_id=category,sku=product_sku,description=description,price=price,saleprice=sale_price,image=product_image)
            product.add_product()
            return redirect("/add_products")
        else:
            return render(request, 'add_products.html', {'instance': root})
    return redirect('/')

def show_products(request):
    if request.session['customerAdmin'] == 0:

        prod= Product.objects.all()
        data={}
        data['products']=prod
        return render(request,'ProductDetail.html',data)
    else:
        return redirect('/')

def feature_product(request,id):
    if request.session['customerAdmin'] == 0:
        pid = Product.objects.get(id=id)
        update = pid.feature
        if update == True:
            pid.feature = False
            pid.save()
        else:
            pid.feature = True
            pid.save()
        return redirect("/show_products")
    else:
        return redirect('/')

def delete_product(request,id):
    if request.session['customerAdmin'] == 0:
        pid = Product.objects.get(id=id)
        pid.delete()
        return redirect("/show_products")
    else:
        return redirect('/')

def order_detail(request):
    if request.session['customerAdmin'] == 0:
        order = Orders.objects.all()
        data={}
        data['orders'] = order
        return render(request,'orders.html',data)
    else:
        return redirect('/login')

def login(request):
    return render(request,'Register.html')

def auth_register(request):
    data = request.POST
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    password = data.get('pass')
    enc_pass = make_password(password)

    reg = Customer(first_name=fname,last_name=lname,email=email,password=enc_pass,phone='')
    reg.insert()
    send_mail(
        'Thanks For Registeration',
        'Welcome '+fname+' '+lname + '<br/> Thanks for the Registeration for more details please contact on our page',
        'amoeez14@gmail.com',
        ['abdulmoeez3582@gmail.com', ''+email],
    )
    cart = request.session.get('cart')
    if cart:
        if reg:
            login = Customer.loginByEmail(reg.email)
            if login:
                chk = check_password(password, login.password)
                if chk:
                    request.session['customerName'] = login.first_name + ' ' + login.last_name
                    request.session['customerAdmin'] = login.admin
                    request.session['customerId'] = login.id
                    return redirect('/cart')
    else:
        return redirect('/login')

def auth_login(request):
    data = request.POST
    email = data.get('email')
    password = data.get('pass')

    login = Customer.loginByEmail(email)
    error_msg = None
    if login:
        chk = check_password(password,login.password)
        cart = request.session.get('cart')
        if chk:
            request.session['customerName'] = login.first_name + ' '+login.last_name
            request.session['customerAdmin'] = login.admin
            request.session['customerId'] = login.id
            if request.session['customerAdmin'] == 0:
                return redirect('/admindashboard')
            elif request.session['customerAdmin'] == 1:
                if cart:
                    return redirect('/checkout')
                else:
                    return redirect('/myaccount')
        else:
            error_msg = "Inncorect password"
    else:
        error_msg = "Email Inccorect"
    return render(request,'Register.html', {'error_msg': error_msg})

def logout(request):
    del request.session['customerName']
    del request.session['customerAdmin']
    return redirect('/')

def admin_index(request):
    try:
        if request.session['customerAdmin'] == 0:
            count_order = Orders.objects.all().count()
            sum = 0
            price = Orders.objects.all()
            for p in price:
                sum += p.price
            ms = 0
            current_month = datetime.datetime.now().month
            order_month = Orders.objects.filter(date__month=current_month)
            for om in order_month:
                ms+=om.price
            all_orders = Orders.objects.all()
            data = {}
            data['Total_sale_items'] = count_order
            data['Total_sale_revenue'] = sum
            data['Current_month_sale'] = ms
            data['all_orders'] = all_orders
            return render(request,'admin_dashboard.html',data)
    except:
            return redirect('/')
    else:
        return redirect('/')