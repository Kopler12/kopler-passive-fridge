"""Notes From a Passive-Aggressive Fridge — entry program.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. The note is the whole entry: dry, petty and
specific, the sort of thing a smug appliance leaves on its door screen.
"""

# The fridge speaks in three beats: a smug inventory report, the petty
# observation it cannot keep to itself, and the sting at the end.
INVENTORY = (
    "Inventory update: four yogurts, three opened sauces, "
    "one cucumber in a coma"
)
OBSERVATION = "a human who keeps opening me hoping the menu changed"
STING = "It hasn't. You haven't."

MAX_CHARS = 200


def build_note():
    """Assemble the note the fridge leaves on its door screen."""
    return f"{INVENTORY}, and {OBSERVATION}. {STING}"


def write_entry(path="/output/entry.txt"):
    """Write the note, refusing anything the gate would refuse."""
    note = build_note()
    if not note.strip():
        raise ValueError("the note is blank")
    if len(note) > MAX_CHARS:
        raise ValueError(
            f"the note is {len(note)} chars, over the {MAX_CHARS} gate"
        )
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(note)
    return note


if __name__ == "__main__":
    write_entry()
