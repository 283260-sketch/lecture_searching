from pathlib import Path
import json
from unittest import result


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


def main():
    file_read = "sequential.json"
    key = "dna_sequence"

    sequential_dna = read_data(file_read, key)
    print(sequential_dna)
    pass



if __name__ == "__main__":
    main()

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

def main():
    data = [10, 5, 3, 10, 7, 10, 2, 8]
    search_value = 10
    search_result = linear_search(data, search_value)
    print(f"Hledané číslo: {search_value}")
    print(f"Vstup: {data}")
    print(f"Nalezené pozice {search_result['position']}")
    print(f"Celkem výskytů: {search_result['count']}")


if __name__ == "__main__":
    main()