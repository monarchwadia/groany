from mock import patch, MagicMock
from groany import groany
from tempfile import mkdtemp
from pytest import fixture
from pathlib import Path
from io import StringIO
from groany.scripts import cli
from typing import Any

class MockBuffer:
  def __init__(self, data: str):
    self.data = data

  def readline(self) -> str:
    return self.data

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

def test_funny_exits_program():
  with patch("sys.stdin", StringIO("funny")), patch("sys.stdout", new_callable=StringIO) as mocked_out:
    cli.exec()
  
  the_mock: Any = mocked_out # Ugly hack to get Pylance to stop complaining about types
  assert isinstance(the_mock, StringIO)
  assert the_mock.getvalue() == "Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.\nWhat kind of dad joke are you in the mood for?\n(groany)> What kind of dad joke are you in the mood for?\nGoodbye!\n"

@patch('groany.api.search')
def test_uniqueness(search: MagicMock):
  api_return_value = {
    'results':[
      {
        'joke': 'first joke',
        'id': 'test_id_1'
      },
      {
        'joke': 'second joke',
        'id': 'test_id_2'
      }
    ],
    'total_jokes': 3,
    'total_pages': 1,
    'current_page': 1,
    'next_page': 1,
    'previous_page': 1,
    'search_term': 'test',
    'status': 200,
    'limit': 30
  }

  search.return_value = api_return_value

  with patch("sys.stdin", StringIO("test\ntest\ntest\nfunny\n")), patch("sys.stdout", new_callable=StringIO) as mocked_out:
    cli.exec()

  the_mock: Any = mocked_out # Ugly hack to get Pylance to stop complaining about types
  assert isinstance(the_mock, StringIO)
  assert the_mock.getvalue() == "Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.\nWhat kind of dad joke are you in the mood for?\n(groany)> first joke\nWhat kind of dad joke are you in the mood for?\n(groany)> second joke\nWhat kind of dad joke are you in the mood for?\n(groany)> No jokes found.\nWhat kind of dad joke are you in the mood for?\n(groany)> What kind of dad joke are you in the mood for?\nGoodbye!\n"
  

@patch('groany.api.search')
def test_uniqueness_across_invocations(search: MagicMock):
  api_return_value = {
    'results':[
      {
        'joke': 'first joke',
        'id': 'test_id_1'
      },
      {
        'joke': 'second joke',
        'id': 'test_id_2'
      }
    ],
    'total_jokes': 3,
    'total_pages': 1,
    'current_page': 1,
    'next_page': 1,
    'previous_page': 1,
    'search_term': 'test',
    'status': 200,
    'limit': 30
  }

  search.return_value = api_return_value

  # First invocation

  with patch("sys.stdin", StringIO("test\nfunny\n")), patch("sys.stdout", new_callable=StringIO) as mocked_out:
    cli.exec()

  the_mock: Any = mocked_out # Ugly hack to get Pylance to stop complaining about types
  assert isinstance(the_mock, StringIO)
  assert the_mock.getvalue() == "Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.\nWhat kind of dad joke are you in the mood for?\n(groany)> first joke\nWhat kind of dad joke are you in the mood for?\n(groany)> What kind of dad joke are you in the mood for?\nGoodbye!\n"

  # 2nd invocation

  with patch("sys.stdin", StringIO("test\nfunny\n")), patch("sys.stdout", new_callable=StringIO) as mocked_out:
    cli.exec()

  the_mock: Any = mocked_out # Ugly hack to get Pylance to stop complaining about types
  assert isinstance(the_mock, StringIO)
  assert the_mock.getvalue() == "Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.\nWhat kind of dad joke are you in the mood for?\n(groany)> second joke\nWhat kind of dad joke are you in the mood for?\n(groany)> What kind of dad joke are you in the mood for?\nGoodbye!\n"

  # 3rd invocation

  with patch("sys.stdin", StringIO("test\nfunny\n")), patch("sys.stdout", new_callable=StringIO) as mocked_out:
    cli.exec()

  the_mock: Any = mocked_out # Ugly hack to get Pylance to stop complaining about types
  assert isinstance(the_mock, StringIO)

  assert the_mock.getvalue() == "Welcome to groany. You can use this to get dad jokes. Type help or ? to list commands.\nWhat kind of dad joke are you in the mood for?\n(groany)> No jokes found.\nWhat kind of dad joke are you in the mood for?\n(groany)> What kind of dad joke are you in the mood for?\nGoodbye!\n"
  
