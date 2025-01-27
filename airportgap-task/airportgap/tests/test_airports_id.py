import pytest
import requests


BASE_URL = "https://airportgap.com/api"


def test_get_airports_status_code():
    """Test that the /airports endpoint returns a 200 status code."""
    response = requests.get(f"{BASE_URL}/airports")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_get_airports_json_structure():
    """Test that the /airports endpoint returns a dictionary with airport data."""
    response = requests.get(f"{BASE_URL}/airports")
    assert response.status_code == 200

    # Validate response is a dictionary with "data"
    data = response.json()
    assert isinstance(data, dict), f"Expected a dict, got {type(data).__name__}"
    assert "data" in data, "Missing 'data' key in response"

    # Validate that 'data' contains a list of airports
    airports = data["data"]
    assert isinstance(airports, list), f"Expected 'data' to be a list, got {type(airports).__name__}"

    # Check that the first item in the list has required fields
    if airports:
        first_airport = airports[0]
        assert "attributes" in first_airport, "Missing 'attributes' key in airport data"
        attributes = first_airport["attributes"]
        assert "iata" in attributes, "Missing 'iata' field in airport attributes"
        assert "name" in attributes, "Missing 'name' field in airport attributes"
        assert "city" in attributes, "Missing 'city' field in airport attributes"
        assert "country" in attributes, "Missing 'country' field in airport attributes"


@pytest.mark.parametrize("airport_code, expected_name", [
    ("ATL", "Hartsfield Jackson Atlanta International Airport"),
    ("LAX", "Los Angeles International Airport"),
    ("JFK", "John F Kennedy International Airport"),
])
def test_get_airport_by_iata(airport_code, expected_name):
    """Test fetching a specific airport by its IATA code."""
    response = requests.get(f"{BASE_URL}/airports/{airport_code}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Extract "data" and "attributes" from the response
    data = response.json()
    assert "data" in data, "Missing 'data' key in response"
    airport = data["data"]
    assert "attributes" in airport, "Missing 'attributes' key in airport data"
    attributes = airport["attributes"]

    # Validate the response details
    assert attributes["iata"] == airport_code, f"Expected IATA {airport_code}, got {attributes['iata']}"
    assert attributes["name"] == expected_name, f"Expected name {expected_name}, got {attributes['name']}"


