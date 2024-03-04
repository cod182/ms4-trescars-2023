# management/widgets.py
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _("Remove")
    initial_text = _("Current Images")
    input_text = _("")
    template_file = "custom_clearable_file_input.html"
    template_name = f"management/custom_widget_templates/{template_file}"

    def __init__(self, attrs=None, multiple=False):
        self.multiple = multiple
        super().__init__(attrs)

    def get_template_substitution_values(self, value):
        """
        Return value-related substitutions.
        """
        return {
            "initial_text": self.initial_text,
            "input_text": self.input_text,
            "clear_checkbox_label": self.clear_checkbox_label,
            "value": value,
            "multiple": "multiple" if self.multiple else "",
        }
