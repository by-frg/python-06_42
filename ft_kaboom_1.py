print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
import alchemy.grimoire.dark_spellbook
print("Testing record dark spell: "
      f"{alchemy.grimoire.dark_spellbook.dark_spell_record("Dark", "frogs")}"
      )
