from extract import extract_data_from_dummy_api

def test_successful_extraction():
    data = extract_data_from_dummy_api()
    assert data is not None
    assert isinstance(data, list)

def test_failed_extraction():
    # Simulate a failed extraction
    # Modify the URL to a non-existent endpoint to simulate a failure
    url = 'https://jsonplaceholder.typicode.com/nonexistent_endpoint'
    data = extract_data_from_dummy_api(url)
    assert data is None
