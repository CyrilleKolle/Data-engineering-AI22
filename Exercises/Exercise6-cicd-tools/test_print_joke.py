from print_joke import get_random_reaction, print_random_joke_and_reaction


def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert isinstance(reaction, str)


def test_get_random_reaction_repeats():
    reactions_set = {get_random_reaction() for _ in range(100)}
    assert len(reactions_set) == 10


def test_get_random_joke_and_reaction_unique():
    complete_joke_set = {print_random_joke_and_reaction() for _ in range(5)}

    assert len(complete_joke_set) == 1
