#!/usr/bin/python3
"""
Script to add words to add_item.json
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    file_name = 'add_item.json'
    items_to_add = sys.argv[1:]
    existing_items = []

    if os.path.exists(file_name):
        existing_items = load_from_json_file(file_name)

    existing_items.extend(items_to_add)

    save_to_json_file(existing_items, file_name)


if __name__ == "__main__":
    main()
