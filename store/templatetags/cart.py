from django import template

register = template.Library()

@register.filter(name='in_cart')
def in_cart(Product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == Product.id:
            return True
        else:
            return False
    return False
@register.filter(name='cart_count')
def cart_count(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='total_cart')
def total_cart(product, cart):
    return cart_count(product, cart) * 1

@register.filter(name='total_price')
def total_price(product, cart):
    if product.saleprice <=0:
        return product.price * cart_count(product, cart)
    else:
        return product.saleprice * cart_count(product, cart)

@register.filter(name='cart_total')
def cart_total(product, cart):
    sum = 0
    for p in product:
        sum += total_price(p, cart)

    return sum