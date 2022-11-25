from mock import patch, MagicMock
from groany import groany
from tempfile import mkdtemp
from pytest import fixture
from pathlib import Path

@fixture(autouse=True)
def setup():
  # setup
  tmpdir = Path(mkdtemp())
  patch('groany.unique.get_groany_home_path', return_value=tmpdir).start()

  #run test
  yield

  # cleanup
  for file in tmpdir.iterdir():
    file.unlink()
  tmpdir.rmdir()

@patch('groany.api.search')
def test_that_the_mock_works(search: MagicMock):
  return_value = {
    'results':[
      {
        'joke': 'test joke',
        'id': 'test_id_1'
      }
    ],
    'total_jokes': 1,
    'total_pages': 1,
    'current_page': 1,
    'next_page': 1,
    'previous_page': 1,
    'search_term': 'test params',
    'status': 200,
    'limit': 30
  }

  search.return_value = return_value
  result = groany('test params')
  assert result != None
  assert result['joke'] == 'test joke'

@patch('groany.api.search')
def test_api_search_was_called_with_groany_prompt(search: MagicMock):
  groany('this is a test')
  search.assert_called_with({ 'page': 1, 'term': 'this is a test', 'limit': 30 })

