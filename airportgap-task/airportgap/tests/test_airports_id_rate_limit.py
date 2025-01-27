import pytest
import requests
import time

BASE_URL = "https://airportgap.com/api"


def test_100_requests_within_1min_rate_limit():
    """
    Test that 100 requests to the /airports/:id endpoint can be sent within 1 minute without error.
    """
    airport_id = "ATL"  # Example airport ID
    max_requests = 100
    # request_interval = 55 / max_requests  # Interval to stay within 1 minute

    responses = []
    start_time = time.time()

    # Send 100 requests
    for i in range(max_requests):
        response = requests.get(f"{BASE_URL}/airports/{airport_id}")
        responses.append(response)
        print("Request: "+str(i))

        # Maintain a steady request interval
        # elapsed_time = time.time() - start_time
        # if elapsed_time < (i + 1) * request_interval:
        #     time.sleep((i + 1) * request_interval - elapsed_time)

    total_elapsed_time = time.time() - start_time

    # Verify all 100 requests returned status code 200
    for idx, response in enumerate(responses):
        assert response.status_code == 200, f"Request {idx+1} failed with status {response.status_code}"

    # Ensure requests were sent within 1 minute
    assert total_elapsed_time <= 60, f"Test took too long: {total_elapsed_time:.2f} seconds"


def test_101_requests_exceed_1min_rate_limit():
    """
    Test that 101 requests to the /airports/:id endpoint within 1 minute triggers the rate limit.
    """
    airport_id = "ATL"  # Example airport ID
    max_requests = 101

    responses = []
    start_time = time.time()

    # Send 101 requests
    for i in range(max_requests):
        response = requests.get(f"{BASE_URL}/airports/{airport_id}")
        responses.append(response)

    total_elapsed_time = time.time() - start_time

    # Verify the 101st request triggers the rate limit (429 Too Many Requests)
    rate_limit_response = responses[-1]
    assert rate_limit_response.status_code == 429, "Expected 429 Too Many Requests for exceeding rate limit"

    # Ensure requests were sent within 1 minute
    assert total_elapsed_time <= 60, f"Test took too long: {total_elapsed_time:.2f} seconds"
