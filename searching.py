from pathlib import Path
import json
from unittest import result

# nacteni dat ze souboru
def read_data(file_name, field):
    try:
        with open(file_name, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        if field not in data:
            return None
        return data[field]
    except FileNotFoundError:
        print(f"Soubor {file_name} nebyl nalezen.")
        return None
    except json.decoder.JSONDecodeError:
        print(f"Soubor {file_name} není platný.")
        return None
    # """
    # Reads a JSON file and returns data for a given field.
    #
    # Args:
    #     file_name (str): Name of the JSON file.
    #     field (str): Key to retrieve from the JSON data.
    #         Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.
    #
    # Returns:
    #     list | str | None:
    #         - list: If data retrieved by the selected field contains numeric data.
    #         - str: If field is 'dna_sequence'.
    #         - None: If the field is not supported.
    # """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
# sekvencni vyhledavani
def linear_search(sequence, number):
    position = []

    for i in range(len(sequence)):
        if sequence[i] == number:
            position.append(i)

    result = {
        "position": position,
        "count": len(position)
    }
    return result

#binarni vyhledavani
def binary_search(seznam, hledane_cislo):
    levy = 0
    pravy = len(seznam) - 1

    while levy <= pravy:
        stred = (levy + pravy) // 2
        if seznam[stred - 1] == hledane_cislo:
            return stred
        elif seznam[stred] < hledane_cislo:
            levy = stred + 1
        else:
            pravy = stred - 1
    return None


def main():
    # nacteni dat se souboru
    print()
    file_read = "sequential.json"
    key_dna = "dna_sequence"
    key_ordered_numbers = "ordered_numbers"
    key_unordered_numbers = "unordered_numbers"

    sequential_dna = read_data(file_read, key_dna)
    print(sequential_dna)
    sequential_unordered_numbers = read_data(file_read, key_unordered_numbers)
    print(sequential_unordered_numbers)
    sequential_ordered_numbers = read_data(file_read, key_ordered_numbers)
    print(sequential_ordered_numbers)

    pass
    print()
    #sekvencni vyhledavani
    # data = [10, 5, 3, 10, 7, 10, 2, 8, 18, 5, 2, 2]
    search_value = 14
    search_result = linear_search(sequential_ordered_numbers, search_value)
    print(f"Hledané číslo: {search_value}")
    print(f"Vstup '{key_ordered_numbers}': {sequential_ordered_numbers}")
    print(f"Nalezené pozice {search_result['position']}")
    print(f"Celkem výskytů: {search_result['count']}")

    print()
    # binarni vyhledavani
    hledane_cislo = 39
    result = binary_search(sequential_ordered_numbers, hledane_cislo)
    print(f"Hledané číslo: {hledane_cislo}")
    if result is not None:
        print(f" => Číslo {hledane_cislo} nalezeno na {result}")
    else:
        print(f" => Číslo {hledane_cislo} nenalezeno")
    print()


if __name__ == "__main__":
    main()

