from mock import patch
from groany import groany


@patch('groany.api.api_search')
def test_that_the_mock_works(api_search):
  api_search.return_value={'results': [{'joke': 'test'}]}
  result = groany("")
  assert result['joke'] == 'test'

@patch('groany.api.api_search')
def test_api_search_was_called_with_groany_prompt(api_search):
  groany("this is a test")
  api_search.assert_called_with('this is a test')