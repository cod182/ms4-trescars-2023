from django import forms
from .widgets import CustomClearableFileInput
from vehicles.models import Vehicle, VehicleImages
from accessories.models import Accessory, Category
from checkout.models import Order, accessory_order


class vehicle_form(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ("price", "type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "sku": "e.g - Registration without spaces",
            "name": "make+reg",
            "registration": "Full Registration",
            "make": "Make of Vehicle. E.g Audi",
            "model": "Model of Vehicle. E.g A3",
            "trim": "Trim Level of Vehicle. E.g S-Line",
            "engine_size": "Vehicle engine size. E.g 2.0",
            "seats": "Number of seats. E.g 5",
            "description": "Description of Vehicle",
            "price": "Price to Reserve (Default - £200)",
            "full_price": "Full price of vehicle. E.g 10000",
            "mileage": "Mileage of Vehicle. Eng. 28469",
            "model_year": "Year of first registration. E.g 2018",
            "doors": "Number of doors. E.g 5",
            "type": "Type",
            "available": "Available",
        }

        no_placeholder = [
            "colour",
            "fuel",
            "body_type",
            "gearbox",
            "drivetrain",
            "available",
        ]

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control my-2"
        for field in self.fields:
            if field not in no_placeholder:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder


class vehicle_images_form(forms.ModelForm):
    class Meta:
        model = VehicleImages
        fields = {"image", "main"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["onchange"] = "loadFile(event)"

    images = forms.FileField(
        label="Image",
        required=False,
        widget=CustomClearableFileInput({"multiple": True}),
    )


class accessory_form(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        placeholders = {
            "sku": "sku autofills",
            "name": "name autofills",
            "category": "Category of item",
            "brand": "Brand of Item",
            "vehicle_make": "Vehicle Make the item is for E.g Nissan or 'all'",
            "vehicle_model": "Vehicle Model item is for E.g Qashqai or 'all'",
            "price": "Price of item",
            "quantity_available": "Number of item available",
            "accessory_type": "Type of Item. E.g Mudflaps",
            "description": "Description of Item",
            "image": "",
        }

        no_placeholder = ["category", "image"]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
        for field in self.fields:
            if field not in no_placeholder:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder


class vehicle_order_form(forms.ModelForm):
    class Meta:
        model = Order
        exclude = (
            "order_type",
            "stripe_pid",
            "delivery_cost",
            "original_bag",
            "order_total",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control my-2"


class accessory_order_form(forms.ModelForm):
    class Meta:
        model = accessory_order
        exclude = (
            "order_type",
            "stripe_pid",
            "delivery_cost",
            "original_bag",
            "order_total",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control my-2"
