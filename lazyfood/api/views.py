import re
from pprint import pprint

import ordrin

from django.contrib.auth.models import User

from piston.handler import BaseHandler
from piston.utils import rc, throttle


from lazyfood.orders.models import Restaurant, Tray, TrayItem, Option

from lazyfood.lib import order


############################################################
# Resources / Handlers
############################################################

class ArbitraryDataHandler(BaseHandler):
  methods_allowed = ('GET',)

  def read(self, request, username, data):
    user = User.objects.get(username=username)

    return { 'user': user, 'data_length': len(data) }

class TrayRandomHandler(BaseHandler):
  ''' takes orders from the user and sends them to Ordr.in '''
  methods_allowed = ('POST', )

  def create(self, request):

    response = make_random_order()
    pprint(response)
    return response


class TrayDataHandler(BaseHandler):
  ''' takes orders from the user and sends them to Ordr.in '''
  methods_allowed = ('POST', )

  #def create(self, request, tray_num):
  def create(self, request, tray_num):

    #tray_num = username
    print "received ID: %s" % tray_num

    response = make_order_with_tray_id(tray_num)
    pprint(response)
    return response

    #return 'OH HERRO'
    #return { 'user': user, 'data_length': len(data) }
    #return rc.CREATED

############################################################
# Utilities
############################################################

def make_random_order():
  tray = Tray.objects.order_by('?')[0]
  print "ordering with tray: %s" % tray
  return make_order_with_tray_id(tray.pk)

def make_order_with_tray_id(tray_id):
  print "making order with tray id: %d" % tray_id
  local_tray = Tray.objects.get(pk=tray_id)

  items = []
  for tray_item in local_tray.trayitem_set.all():
    options = []
    #for option in tray_item.option_set.all():
    #  options.append(option.option_code)

    if len(options) > 0:
      print "using options: %s" % options
      items.append(ordrin.data.TrayItem(tray_item.item_code, tray_item.quantity, *options))
    else:
      print "not using options"
      items.append(ordrin.data.TrayItem(tray_item.item_code, tray_item.quantity))

  return order.make_order(
    items,
    local_tray.restaurant.restaurant_code
  )
