"""
Additional Widgets Provided for use with Bootstrap
"""
from .util import bootstrap_styled
from ..abstract import MultiField as _MultiField
from ..abstract import CustomWidgetMixin
from .core import PlainCheckbox, PlainRadio


__all__ = ['JasnyFileInput', 'MultiField', 'CheckboxGroup','RadioGroup']

from wtforms.widgets import FileInput

@bootstrap_styled(input_class=None)
class JasnyFileInput(CustomWidgetMixin):
    """
    A Jasny-Bootstrap renderer widget. (Requires Jasny-bootstrap js and css)
    """

    def __init__(self):
        self._field_renderer = FileInput()

    def __call__(self, field, **kwargs):
        html = """
        <div class="fileinput fileinput-new input-group" data-provides="fileinput" style="width:100%;">
            <div class="form-control" data-trigger="fileinput">
                <span class="fileinput-filename"></span>
            </div>
            <span class="input-group-addon btn btn-default btn-file">
            <span class="fileinput-new">Select file</span>
            <span class="fileinput-exists">Change</span>
                {rendered_field}
            </span>
            <a href="#" class="input-group-addon btn btn-default fileinput-exists" data-dismiss="fileinput">Remove</a>
        </div>
        """.format(
            rendered_field=self._field_renderer(field, **kwargs)
        )
        return html


@bootstrap_styled(input_class=None)
class MultiField(_MultiField, CustomWidgetMixin):
    """
    Render a compatible field's possible choices using the given choice renderer.
    """

    def __init__(self, choice_renderer):
        self.choice_renderer = choice_renderer


class RadioGroup(MultiField):
    """
    Render a compatible field's possible choices using radio boxes
    """
    def __init__(self):
        self.choice_renderer = PlainRadio()

class CheckboxGroup(MultiField):
    """
    Render a compatible field's possible choices using check boxes.
    """
    def __init__(self):
        self.choice_renderer = PlainCheckbox()
