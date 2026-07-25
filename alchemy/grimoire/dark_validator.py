from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    l_ing: list[str] = (ingredients.replace(",", "")).split()
    if any(
           ing.lower() == x.lower()
           for ing in dark_spell_allowed_ingredients()
           for x in l_ing
          ):
        return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
