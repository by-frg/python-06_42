import elements
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    air: str = create_air()
    fire: str = elements.create_fire()
    str_potion: str = strength_potion()

    return (
        f"Recipe transmuting Lead to Gold: brew ’{air}’ "
        f"and ’{str_potion}’ mixed with ’{fire}’"
        )
