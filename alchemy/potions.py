from .elements import create_earth, create_air
from elements import create_fire, create_water


def healing_potion() -> str:
    air: str = create_air()
    earth: str = create_earth()
    return (f"Healing potion brewed with ’{earth}’ and ’{air}’")


def strength_potion() -> str:
    fire: str = create_fire()
    water: str = create_water()
    return (f"Strength potion brewed with ’{fire}’ and ’{water}’")
