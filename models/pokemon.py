import typing
import enum
import decimal


class AbilitySlot(enum.Enum):
    FIRST = 'F'
    SECOND = 'S'
    HIDDEN = 'H'
    MEGA = 'M'


class TypeSlot(enum.Enum):
    PRIMARY = 'P'
    SECONDARY = 'S'


class Ability():

    def __init__(self, name: str):
        self._name = name


class PokemonType():

    def __init__(self, name: str):
        self._name = name


class EggGroup():

    def __init(self, name: str):
        self._name = name


class Generation():

    def __init(self, name: str):
        self._name = name


class Region():

    def __init(self, name: str):
        self._name = name


class PokemonDex():

    def __init__(
            self,
            region: Region,
            pokemon,
            regional_dex: int,
    ):
        self._region = region
        self._pokemon = pokemon
        self._regional_dex = regional_dex


class Pokemon():
    #pylint: disable-msg=too-many-arguments
    #pylint: disable-msg=too-many-locals
    def __init__(
            self,
            national_dex: int,
            name: str,
            japanese_name: str,
            japanese_transliteration: str,
            japanese_romanized: str,
            has_mega: bool,
            category: str,
            regional_numbers: typing.List[PokemonDex],
            egg_groups: typing.List[EggGroup],
            hatch_time: int,
            experience_yield: int,
            gender_code: decimal.Decimal,
            catch_rate: int,
            introduced_generation: Generation,
            base_friendship: int,
            url: str,
    ):
        self._national_dex = national_dex
        self._name = name
        self._japanese_name = japanese_name
        self._japanese_transliteration = japanese_transliteration
        self._japanese_romanized = japanese_romanized
        self._has_mega = has_mega
        self._category = category
        self._regional_numbers = regional_numbers
        self._egg_groups = egg_groups
        self._hatch_time = hatch_time
        self._experience_yield = experience_yield
        self._gender_code = gender_code
        self._catch_rate = catch_rate
        self._introduced_generation = introduced_generation
        self._base_friendship = base_friendship
        self._url = url


class FormAbility():

    def __init__(
            self,
            ability: Ability,
            form,
            slot: AbilitySlot,
    ):
        self._ability = ability
        self._form = form
        self._slot = slot


class FormType():

    def __init__(
            self,
            pokemon_type: PokemonType,
            form,
            slot: TypeSlot,
    ):
        self._pokemon_type = pokemon_type
        self._form = form
        self._slot = slot


class MegaStonePicture():

    def __init__(
            self,
            name: str,
            image_relative_link: str,
            pokemon: Pokemon,
    ):
        self._name = name
        self._image_relative_link = image_relative_link
        self._pokemon = pokemon


class Form():
    #pylint: disable-msg=too-many-arguments
    #pylint: disable-msg=too-many-locals
    def __init__(
            self,
            name: str,
            image_relative_link: str,
            sprite_relative_link: str,
            abilities: typing.List[AbilitySlot],
            types: typing.List[TypeSlot],
            weight: decimal.Decimal,
            height: decimal.Decimal,
            pokemon: Pokemon,
    ):
        self._name = name
        self._image_relative_link = image_relative_link
        self._sprite_relative_link = sprite_relative_link
        self._abilities = abilities
        self._types = types
        self._weight = weight
        self._height = height
        self._pokemon = pokemon
