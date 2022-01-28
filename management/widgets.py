from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Images')
    input_text = _('')
    template_file = 'custom_clearable_file_input.html'
    template_name = f'management/custom_widget_templates/{template_file}'
