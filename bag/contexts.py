from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from vehicles.models import Vehicle
from accessories.models import Accessory


def vehicle_bag_contents(request):

    vehicle_bag_items = []
    total = 0
    item_count = 0
    vehicle_bag = request.session.get('vehicle_bag', {})

    for vehicle_sku, item_data in vehicle_bag.items():
        if isinstance(item_data, int):
            vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)
            total += item_data * vehicle.price
            item_count += item_data
            vehicle_bag_items.append({
                'vehicle_sku': vehicle_sku,
                'quantity': item_data,
                'vehicle': vehicle,
            })
        else:
            vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)
            for quantity in item_data['items_by_size'].items():
                total += quantity * vehicle.price
                item_count += quantity
                vehicle_bag_items.append({
                    'vehicle_sku': vehicle_sku,
                    'quantity': quantity,
                    'vehicle': vehicle,
                })

    delivery = 0

    grand_total = delivery + total

    context = {
        'vehicle_bag_items': vehicle_bag_items,
        'vehicle_total': total,
        'vehicle_item_count': item_count,
        'vehicle_grand_total': grand_total,
    }

    return context


def bag_contents(request):

    bag_items = []
    total = 0
    accessory_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            accessory = get_object_or_404(Accessory, pk=item_id)
            total += item_data * accessory.price
            accessory_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'accessory': accessory,
            })
        else:
            accessory = get_object_or_404(Accessory(), pk=item_id)
            for quantity in item_data.items():
                total += quantity * accessory.price
                accessory_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'accessory': accessory,
                })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'accessory_count': accessory_count,
        'grand_total': grand_total,
    }

    return context
