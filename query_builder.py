import os
import typing
import enum

base_api_url = os.environ.get('base_api_url')
base_url = os.environ.get('base_url')


class ResourceType(enum.Enum):
    POKEMON = '_(Pokémon)'
    MISCELLANEOUS = ''


def _base_content_query(
        resource: str,
        section: int,
        resource_type: ResourceType,
) -> str:
    return (
        f'{base_api_url}api.php?'
        'action=query'
        '&prop=revisions'
        f'&titles={resource}{resource_type.value}'
        '&rvprop=content'
        f'&rvsection={section}'
        '&format=json'
    )


def _base_parse_query(
        resource: str,
        section: int,
        resource_type: ResourceType,
) -> str:
    return (
        f'{base_api_url}api.php?'
        'action=parse'
        f'&page={resource}{resource_type}'
        '&prop=text'
        f'&section={section}'
        '&format=json'
    )


def _base_sections_query(
        resource: str,
        resource_type: ResourceType,
) -> str:
    return (
        f'{base_api_url}api.php?'
        'action=parse'
        f'&page={resource}{resource_type}'
        '&prop=sections'
        '&format=json'
    )


def _base_url_query(
        resource: str,
        resource_type: ResourceType,
) -> str:
    return f'{base_url}{resource}{resource_type}'


def _base_picture_location_query(picture_link: str, ) -> str:
    return (
        f'{base_api_url}api.php?'
        'action=query'
        f'&titles={picture_link}'
        '&prop=imageinfo'
        '&iiprop=url'
        '&format=json'
    )


def pokemon_url_query(pokemon_name: str) -> str:
    return _base_url_query(pokemon_name, ResourceType.POKEMON)


def pokemon_content_query(
        pokemon_name: str,
        section: int,
) -> str:
    return _base_content_query(pokemon_name, section, ResourceType.POKEMON)


def pokemon_parse_query(
        pokemon_name: str,
        section: int,
) -> str:
    return _base_parse_query(pokemon_name, section, ResourceType.POKEMON)


def pokemon_list_query(generation: typing.Optional[int] = 1) -> str:
    return _base_content_query(
        'List_of_Pokémon_by_National_Pokédex_number',
        generation,
        ResourceType.MISCELLANEOUS,
    )
