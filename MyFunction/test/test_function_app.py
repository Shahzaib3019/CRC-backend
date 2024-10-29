import pytest
from azure.cosmos import exceptions
from function_app import http_triggershahzaib  # Import your function

def test_http_triggershahzaib(mocker):
    mocker.patch('azure.cosmos.CosmosClient')  # Mock CosmosClient

    # Setup your mock client, database, and container
    mock_client = mocker.Mock()
    mock_database = mock_client.get_database_client.return_value
    mock_container = mock_database.get_container_client.return_value

    # Mock read_item and upsert_item methods
    mock_container.read_item.return_value = {'count': 5}
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

    # Assert that upsert_item was called
    mock_container.upsert_item.assert_called_once_with({
        'id': 'visitor_count',
        'count': 6
    })
