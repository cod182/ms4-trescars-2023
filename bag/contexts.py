from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from vehicles.models import Vehicle


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
