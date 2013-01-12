#from datetime import datetime
import datetime

import ordrin

# from lazyfood.orders.models import Restaurant, Tray, TrayItem, Option


#CHICKEN_ORDER_STRING = "8579535/1,8579538,8579543,8579559,8579568+8580458/1,8580460,8580461,8580464,8580476,8580481"

INDIAN_ITEMS = [
    ordrin.data.TrayItem(8524273, 1),
    ordrin.data.TrayItem(8524311, 2),
    ordrin.data.TrayItem(8524284, 1),
]
INDIAN_RESTAURANT_ID = 5699

FIRST_NAME = 'David'
LAST_NAME  = 'Kay'
EMAIL  = 'dk@gargoyle.co'

ADDRESS  = ordrin.data.Address('500 7th Ave', 'New York', 'NY', '10018', '(555) 555-5555')

BILL_ADDRESS = ADDRESS
CARD_NAME = "%s %s" % (FIRST_NAME, LAST_NAME)
EXPIRY_YEAR = '2016'
EXPIRY_MONTH = '02'
CVC = '123'
CARD_NUMBER = '4111111111111111'

CREDIT_CARD  = ordrin.data.CreditCard(
CARD_NAME,
EXPIRY_MONTH,
EXPIRY_YEAR,
BILL_ADDRESS,
CARD_NUMBER,
CVC)

api = ordrin.APIs('TL_I5c1ncrALpc7bfoHsCQ3d3LhhOC0B-FqVzTJTZpc', ordrin.TEST)

def make_order(items, restaurant_id):
  tray = ordrin.data.Tray(*items)

  tip = 5.05
  delivery_date_time = 'ASAP'

  return api.order.order(restaurant_id,
  tray,
  tip,
  delivery_date_time,
  FIRST_NAME,
  LAST_NAME,
  ADDRESS,
  CREDIT_CARD,
  email=EMAIL
                  )

def make_test_order():
  return make_order(INDIAN_ITEMS, INDIAN_RESTAURANT_ID)
  #make_order_with_tray_id(1)

if __name__ == '__main__':
  make_test_order()
