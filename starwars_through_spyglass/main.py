from typing import Optional
import json

import requests
import click

API_URL = "https://swapi.dev/api/"


def display(data: list, **kwargs) -> None:
    """Helper function to display data from the Star Wars API."""
    verbose = kwargs.get("verbose", False)
    if verbose:
        for element in data:
            print("=" * 50)
            print(json.dumps(element, indent=4))
            print("=" * 50)
    else:
        for element in data:
            print(element["name"])


def make_request(url: str) -> Optional[dict]:
    """Helper function to make requests to the Star Wars API."""
    try:
        raw_response = requests.get(url)
        raw_response.raise_for_status()
    except requests.exceptions.RequestException as r_exception:
        print(f"Request error occurred: {r_exception}")
        return None
    except Exception as other_exception:
        print(f"Other error occurred: {other_exception}")
        return None
    else:
        return raw_response.json()


@click.group()
def cli() -> None:
    """CLI group for the Star Wars API."""
    pass


@cli.command()
@click.argument("limit", type=click.INT, required=False, default=None)
@click.option("--verbose", "-v", is_flag=True, default=False)
def planets(limit: Optional[int] = None, verbose: bool = False) -> None:
    """Get a list of planets from the Star Wars API. Limit and verbosity are supported."""
    response = make_request(f"{API_URL}planets/")["results"]
    if limit:
        response = response[:limit]
    display(response, verbose=verbose)


@cli.command()
@click.argument("planet_id", type=click.STRING, required=True)
def planet(planet_id: str) -> None:
    """Get a single planet from the Star Wars API based on its id."""
    response = make_request(f"{API_URL}planets/{planet_id}/")
    if response:
        display([response], verbose=True)
    else:
        print(f"No planet found with id {planet_id}")


@cli.command()
@click.argument("name", type=click.STRING, required=True)
def planet_search(name: str) -> None:
    """Search for a planet from the Star Wars API based on its name."""
    response = make_request(f"{API_URL}planets/?search={name}")["results"]
    if response:
        display([response], verbose=True)
    else:
        print(f"No planets found with name {name}")


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
