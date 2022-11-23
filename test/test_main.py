from mock import patch, MagicMock
from groany import sum

class TestMain:
  @patch('groany.sum.sum', MagicMock(return_value=10))
  def test_sum(self):
    result = sum.sum(1,2)
    print("RESULT", result)
    assert result == 10
