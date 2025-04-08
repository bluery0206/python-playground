""""
    This is laid out as plain as possible for future me to understand lol
    # and probably some other people as well
"""


def word_morph(word: str, from_last: bool = False, ltr: bool = False, centered: bool = False) -> None:
    """
    Shows the root word first then gradually remove characters
    depending on the configuration in the parameters
    """
    for idx in range(len(word)):
        if idx == 0:
            print(word)
        else:
            spaces = ""

            if ltr:
                n = idx

                # just to make it look like a triangle, if enabled
                # it doesnt really look centered due to how characters are shown in the terminal
                # ltr has to be True for this to take effect
                if centered:
                    n = int(idx / 2)

                spaces = " " * (n)

            new_word = new_word = word[:-idx] if from_last else word[idx:]
            new_word = spaces + new_word if ltr else new_word

            print(new_word)


word_morph(
    word = "hilario",
    from_last = True, # Whether to remove letters from last to beginning or vice versa
    ltr = True, # Whether to show the letters in left or right
    centered = False # A bool to make the output look centered from the root word however
)
