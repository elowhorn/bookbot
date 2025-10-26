import string


def count_words(text: str) -> int:
    return len(text.split())


def count_characters(text: str) -> dict[str, int]:
    # Initialize empty dict and letter set
    char_count = {}
    # Check if char is valid alpha character
    # Instantiate value at 0 if first hit, otherwise increment
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    return char_count


def sort_char_counts(char_counts: dict[str, int]) -> list[dict]:
    sorted_count_list = []

    for char in char_counts:
        sorted_count_list.append({"char": char, "num": char_counts[char]})

    sorted_count_list.sort(reverse=True, key=lambda char_count: char_count["num"])

    return sorted_count_list
