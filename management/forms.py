from django import forms
from vehicles.models import Vehicle, VehicleImages

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        exclude = ('price', 'type', 'available')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'sku': 'e.g - Registration without spaces',
            'name': 'make+reg',
            'registration': 'Full Registration',
            'make': 'Make of Vehicle. E.g Audi',
            'model': 'Model of Vehicle. E.g A3',
            'trim': 'Trim Level of Vehicle. E.g S-Line',
            'colour': 'Colour of Vehicle. E.g White',
            'fuel': 'Fuel of Vehicle. E.g Diesel',
            'engine_size': 'Vehicle engine size. E.g 2.0',
            'body_type': 'Body type of Vehicle. E.g Hatchback',
            'gearbox': 'Type of Gearbox. E.g Automatic',
            'drivetrain': 'Vehicle drivetrain. 2WD or 4WD',
            'seats': 'Number of seats. E.g 5',
            'description': 'Description of Vehicle',
            'price': 'Price to Reserve (Default - £200)',
            'full_price': 'Full price of vehicle. E.g 10000',
            'mileage': 'Mileage of Vehicle. Eng. 28469',
            'model_year': 'Year of first registration. E.g 2018',
            'doors': 'Number of doors. E.g 5',
            'type': 'Type',
            'available': 'Available',
            }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control my-2'
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
