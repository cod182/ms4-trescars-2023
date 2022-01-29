import uuid
from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django_countries.fields import CountryField


from vehicles.models import Vehicle
from accessories.models import Accessory
from profiles.models import UserProfile

order_status = (
    ("processing", "Processing"),
    ("paid", "Paid"),
    ("shipped", "Shipped"),
    ("refunded", "Refunded"),
    ("patrial-refund", "Patrial Refund")
)


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    order_type = models.CharField(
        max_length=15, null=False, blank=False, default="vehicle"
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default="")
    status = models.CharField(max_length=80, null=True, blank=True,
                              choices=order_status, default="Processing")

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"] or 0
        )
        self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class vehicle_order_line_item(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    vehicle = models.ForeignKey(
        Vehicle, null=False, blank=False, on_delete=models.CASCADE
    )
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=0, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = int(self.vehicle.price)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.vehicle.sku} on order {self.order.order_number}"


class accessory_order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    order_type = models.CharField(
        max_length=15, null=False, blank=False, default="accessories"
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="AccessoryOrders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default="")
    status = models.CharField(max_length=80, null=True, blank=True,
                              choices=order_status, default="Processing")

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = (
            self.accessorylineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )
        self.delivery_cost = 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class accessory_order_line_item(models.Model):
    order = models.ForeignKey(
        accessory_order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="accessorylineitems",
    )
    accessory = models.ForeignKey(
        Accessory, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=1)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=0, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = int(self.accessory.price * self.quantity)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU {self.accessory.sku} on order {self.order.order_number}"
