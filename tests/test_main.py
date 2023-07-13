import unittest
from unittest.mock import patch
import click.testing
from starwars_through_spyglass.main import make_request, display, cli


class TestMain(unittest.TestCase):

    @patch("requests.get")
    def test_make_request(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"results": "data"}
        self.assertEqual(make_request("https://swapi.dev/api/planets/"), {"results": "data"})

    @patch("builtins.print")
    def test_display(self, mock_print):
        test_data = [{"name": "Tatooine"}]
        display(test_data)
        mock_print.assert_called_with("Tatooine")

    @patch("starwars_through_spyglass.main.make_request")
    def test_planets(self, mock_request):
        mock_request.return_value = {"results": [{"name": "Tatooine"}]}
        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["planets", "1"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Tatooine", result.output)

    @patch("starwars_through_spyglass.main.make_request")
    def test_planet(self, mock_request):
        mock_request.return_value = {"name": "Tatooine"}
        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["planet", "1"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Tatooine", result.output)

    @patch("starwars_through_spyglass.main.make_request")
    def test_planet_search(self, mock_request):
        mock_request.return_value = {"results": [{"name": "Tatooine"}]}
        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ["planet-search", "Tatooine"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Tatooine", result.output)


if __name__ == "__main__":
    unittest.main()
