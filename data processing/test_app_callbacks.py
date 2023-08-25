from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

# Import the names of callback functions you want to test
from data_visualization_rework import update_line_chart


def test_update_line_chart():
    output = update_line_chart('north')
    assert output == 'chart displays data from north'
