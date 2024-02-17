import pytest
from selenium.webdriver.common.by import By
from dash.testing.application_runners import import_app


def test_header_presence(dash_duo):
    # Start the app
    app = import_app("your_dash_app_file_name")  # Replace with your Dash app's filename
    dash_duo.start_server(app)

    # Check if the header is present
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Sales Visualizer"

def test_visualisation_presence(dash_duo):
    app = import_app("your_dash_app_file_name")  # Replace with your Dash app's filename
    dash_duo.start_server(app)

    # Check if the visualization (graph) is present
    visualization = dash_duo.find_element("#sales-line-chart")
    assert visualization

def test_region_picker_presence(dash_duo):
    app = import_app("your_dash_app_file_name")  # Replace with your Dash app's filename
    dash_duo.start_server(app)

    # Check if the region picker (radio items) is present
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker
