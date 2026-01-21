import os

import pandas as pd

from data_parsing import read_data
from photo_finder import get_photo_path


people, families = read_data("data.csv")

# Sort people by family ID for faster search lookup
people.sort(key=lambda p: p.family_id)

photos = []
family_labels = []
for family_num in families.keys():
    family = []

    # Group people with same family ID assuming the list is sorted
    found_someone = False
    for person in people:
        if person.family_id == family_num:
            found_someone = True
            family.append(person)
        elif found_someone:
            break

    photo_path, family_label = get_photo_path(family, families[family_num])

    family_labels.append(family_label)
    if photo_path is None:
        print(family_label, photo_path)
