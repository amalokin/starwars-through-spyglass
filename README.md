# Star Wars Planets CLI

A Python command-line application that interacts with the [Star Wars API](https://swapi.dev/api/) to fetch data about planets.
This project is created to respond to technical assessment for the position of Founding Engineer at [Spyglass](https://spyglass.software/).

## Installation

Install the package by accessing Test Pypi with pip:

```bash
pip install --index-url https://test.pypi.org/simple/ starwars-through-spyglass
```
Tested with the following package versions:
- python 3.10, 3.11
- requests 2.31.0
- click 8.1.4

## Usage

The CLI tool provides the following commands:

### `planets`

Get a list of planets from the Star Wars API.

```sh
starwars planets [LIMIT] [--verbose]
```

Options:
- `--verbose, -v`: Display detailed information about each planet. The info is **NOT** verbose by default.
- `LIMIT`: Integer, =>0. Limit the number of planets to display. If not specified, all planets will be displayed.

### `planet`

Get a single planet from the Star Wars API based on its id. The info is verbose by default.

```sh
starwars planet PLANET_ID
```

Arguments:
- `PLANET_ID`: The id of the planet.

### `planet_search`

Search for a planet from the Star Wars API based on its name. The info is verbose by default.

```sh
starwars planet-search NAME
```

Arguments:
- `NAME`: The name of the planet.

## Error Handling

The tool handles HTTP errors and other exceptions by printing an error message to the console.

## Author

This tool was developed by [Alex Malokin](mailto:amalokin@gmail.com). Feel free to contact if you have any questions or suggestions.
