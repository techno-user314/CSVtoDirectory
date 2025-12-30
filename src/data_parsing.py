import pandas as pd

class Person:
    def __init__(self, first_name, last_name, is_primary=False):
        self.lastname = last_name
        self.firstname = first_name
        self.is_primary = is_primary
        self.family_id = None

        self.mobile_number = ""
        self.email = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""

    def set_contact(self, phone, email):
        self.mobile_number = phone
        self.email = email

    def set_address(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def set_family(self, fid_num):
        self.family_id = fid_num

    def __str__(self):
        return (f"{self.firstname} {self.lastname}")

def read_data(csv_path):
    df = pd.read_csv(csv_path)

    people = []  # List of People objects
    family_ids = []  # List of unique family id's
    for index, row in df.iterrows():
        # Create a new person with information that will
        # be compiled later for the contact info section
        if not pd.isnull(row["Died On"]):
            continue  # Skip dead people
        firstname = row["First Name"] if pd.isnull(row["Preferred Name"]) else row["Preferred Name"]
        lastname = row["Last Name"]

        fam_rel = row["Family Relationship"]
        new_person = Person(firstname, lastname,
                            is_primary=(fam_rel == "Primary" or fam_rel == "Husband"))
        new_person.set_contact(row["Cell Phone"], row["Email"])
        new_person.set_address(row["Address"], row["City"], row["State"], row["Zip Code"])

        if not pd.isnull(row["Family ID"]):
            new_person.set_family(row["Family ID"])
            if row["Family ID"] not in family_ids:
                family_ids.append(row["Family ID"])

        people.append(new_person)

    return people, family_ids
