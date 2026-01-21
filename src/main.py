import pandas as pd
from docx import Document

from data_parsing import read_data
from photo_finder import get_photo_path
from document_creation import add_photo_grid_page, add_preset_page

people, families = read_data("data.csv")

# Sort people by family ID for faster search lookup
people.sort(key=lambda p: p.family_id)

# Sort families alphabetically by last name
families = {k: v for k, v in sorted(families.items(), key=lambda item: item[1])}

# Get the photo path and label for the photos for each family
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
    if photo_path is not None:
        family_labels.append(family_label)
        photos.append(photo_path)

# === Create Document ===
from docx.shared import Inches
pages = 0
doc = Document()

# Add cover pages
coverImages = ["Other/CoverPages-01.png","Other/CoverPages-02.png","Other/CoverPages-03.png",
               "Other/CoverPages-04.png","Other/CoverPages-05.png"]
for coverImage in coverImages:
    add_preset_page(doc, coverImage)
    pages += 1

# Add family photos
for i in range(0, len(photos), 12):
    add_photo_grid_page(doc, photos[i:i+12], family_labels[i:i+12])
    pages += 1

# Add final pages
if pages % 2 == 0:
    doc.add_page_break()
add_preset_page(doc, "Other/Final_Page.png")

# Save
doc.save("photo_grid.docx")
