import pytest
from function_app import http_triggershahzaib  # Import your Azure Function

def test_http_triggershahzaib(mocker):
    # Mock CosmosClient
    mocker.patch('azure.cosmos.CosmosClient')  # Mock CosmosClient

    # Setup your mock client, database, and container
    mock_client = mocker.Mock()
    mock_database = mock_client.get_database_client.return_value
    mock_container = mock_database.get_container_client.return_value

    # Mock read_item to return a count of 5
    mock_container.read_item.return_value = {'id': 'visitor_count', 'count': 5}
    mock_container.upsert_item.return_value = None

    # Create a mock HttpRequest
    class MockHttpRequest:
        def __init__(self):
            self.method = 'GET'

    req = MockHttpRequest()

    # Call your function
    response = http_triggershahzaib(req)

    # Check response
    assert response.status_code == 200
    assert response.get_body().decode() == '6'  # Expecting incremented value

# Additional tests can be added here as needed
