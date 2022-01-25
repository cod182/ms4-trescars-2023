from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import vehicle_order_line_item, accessory_order_line_item


@receiver(post_save, sender=vehicle_order_line_item)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line item created/updated
    """
    instance.order.update_total()


@receiver(post_delete, sender=vehicle_order_line_item)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line item deleted
    """
    instance.order.update_total()


@receiver(post_save, sender=accessory_order_line_item)
def update_accessory_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line item created/updated
    """
    instance.order.update_total()


@receiver(post_delete, sender=accessory_order_line_item)
def update_accessory_on_delete(sender, instance, **kwargs):
    """
    Update order total on line item deleted
    """
    instance.order.update_total()
