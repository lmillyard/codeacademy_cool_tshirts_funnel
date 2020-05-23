import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

'''print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())'''

visits_cart = pd.merge(visits, cart, how = 'left')
#print(visits_cart)
visits_cart_count = len(visits_cart)
#print(visits_cart_count)

null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
#print(null_cart_times)

cart_times_percentage = float(null_cart_times) / visits_cart_count * 100 
print(cart_times_percentage)


##############

cart_checkout = pd.merge(cart, checkout, how = 'left')
#print(cart_checkout)
cart_checkout_count = len(cart_checkout)
null_cart_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])

cart_checkout_percentage = float(null_cart_checkout) / cart_checkout_count * 100

print(cart_checkout_percentage)

###########
checkout_purchase = pd.merge(checkout, purchase, how = 'left')
#print(checkout_purchase.head())
checkout_purchase_count = len(checkout_purchase)
#print(checkout_purchase_count)
checkout_purchase_null = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])
#print(checkout_purchase_null)
checkout_purchase_percentage = float(checkout_purchase_null) / checkout_purchase_count * 100
print(checkout_purchase_percentage)

#############

all_data = visits\
  .merge(cart, how = 'left')\
  .merge(checkout, how = 'left')\
  .merge(purchase, how = 'left')

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.head())
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
