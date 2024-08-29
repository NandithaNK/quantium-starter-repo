import pytest
from dash import html
from app import app

@pytest.fixture
def dash_duo_fixture(dash_duo):
    dash_duo.start_server(app)  #starting server
    return dash_duo

def test_header_is_present(dash_duo_fixture): #checking if header is present
    header = dash_duo_fixture.find_element("h1")
    assert header.text == "Header Title"
    assert header.is_displayed()

def test_visualization_is_present(dash_duo_fixture): #checking if graph is present
    graph = dash_duo_fixture.find_element("#example-graph")
    assert graph.is_displayed()

def test_region_picker_is_present(dash_duo_fixture):  #checking if region is present
    region_picker = dash_duo_fixture.find_element("#region-radio")
    assert region_picker.is_displayed()
