import typing
import collections
import enum

Section = collections.namedtuple(
    'Section',
    [
        'toclevel',
        'level',
        'line',
        'number',
        'index',
        'fromtitle',
        'byteoffset',
        'anchor',
    ],
)


class PokemonSection(enum.Enum):
    BASE = 'Base'
    EVOLUTION = 'Evolution'


def extract_content(data: dict) -> str:
    result = data['query']['pages'][0][0]['revisions'][-1][-1][-1]
    return result


def extract_picture_url(data: dict) -> str:
    result = data['query']['pages'][0][0]['imageinfo'][0]['url']
    result.replace('"', '')
    return result


def extract_section_list(data: dict) -> typing.List[Section]:
    result = data['parse']['sections']
    return result


def extract_section_list(
        section_list: typing.List[Section],
        section_to_find: PokemonSection,
) -> int:
    switch = {
        PokemonSection.BASE: (lambda: 0),
        PokemonSection.EVOLUTION: (
            lambda: filter(
                (lambda x: x.anchor == 'Evolution'),
                section_list,
            )[0]
        )
    }

    return switch.get(section_to_find, (lambda: -1))()
