import logging

from winter_openapi import PathParametersInspector
from winter_openapi import register_route_parameters_inspector
from winter_openapi.inspectors.route_parameters_inspector import _route_parameters_inspectors


def test_add_same_inspector_write_warning_log(caplog):
    initial_count = len(_route_parameters_inspectors)
    with caplog.at_level(logging.WARNING):
        register_route_parameters_inspector(PathParametersInspector())
    assert 'PathParametersInspector already registered' in caplog.text
    # Clean up the duplicate inspector added by this test
    del _route_parameters_inspectors[initial_count:]
