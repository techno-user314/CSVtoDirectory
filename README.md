# CSVtoDirectory
Converts directory information from a CSV file into a Word Document with two sections: A photo directory with names and photos, and a table containing information for each person. Optionally, cover pages can also be added.  
  
## Usage 
Copy the CSV file into the working directory of the program. It should have one row per person with the following headers:   

| Header | Contents |
| --- | --- |
| Family ID | Unique ID number for every family; Leave black if person is single |
| First Name | Formal first name of the person |
| Preffered Name | Preffered first name of the person |
| Last Name | Family's last name/surname |
| Family Relationship | One of: Primary, Husband, Wife, Other |
| Family Members | Comma separated list of the direct members of the family this person is in (including self) |
| Email | This person's primary email address |
| Home Phone | This person's home phone number |
| Cell Phone | This person's cell phone number |
| Address |This person's address |
| City | City of residence |
| State | State of residence |
| Zip | Postal code of the person's address |
| Died On | Date of the person's death; Leave blank of not applicable |
*(Not all of these headers are required for the program to work, but are recommended for future proofing.)  
  
Also ensure that images for everybody are in:  
  `./Images`  
The images should be .jpg files named in one of the following formats:
  - `lastname firstname.jpg`
  - `lastname firstname family.jpg`
Where lastname is the family lastname, and firstname is the firstname of the primary member of the family (primary member as defined in the 'Family Relationship' field of the CSV; Every family must have a primary member, either labeled primary or husband in the CSV).  
If the person is single, 'family' may be dropped from the filename, as shown above.
  
If there is info on the spreadsheet that needs to be adjusted before being put into the directory, out can be done automatically in special_cases.json. See the example file.  
  
Run the program (which should take about a minute), and "directory.docx" should appear in the working directory of the program.  
  
## Install and Run (Windows)
 1. [Install Python](https://www.python.org/downloads/).
 2. Download the zip file for the [latest release](https://github.com/techno-user314/csv-to-directory/releases).
 3. Unzip the folder.
 4. Open the folder in File Explorer, and navigate into the "src" directory.
 5. Put the family photos into the /Images folder.
 6. Optionally modify special_cases.json.
 7. If you have cover photos, put these into the /Covers folder/
 8. Open main.py in a text editor, and modify the first three lines to specify the file paths of your cover photos and data file.
 9. Paste your data CSV file into /src.
 10. Right click anywhere in the folder, and select "Open in Terminal".
 11. Run this command:
  - `python -m venv virtenv`
 8. Go back into File Explorer (but don't close your terminal window) and navigate into the new "virtenv" folder, into the "Scripts" folder, right click "Activate.ps1" and select "Copy as Path".
 9. Return to the terminal window and type `powershell -ExecutionPolicy Bypass -File ` (with a space at the end) and then paste the file path you just copied.  
    > If you are on Linux or MacOS, run `source virtenv/bin/activate`  instead.
 10. Run `pip install pandas python-docx`
  
Now the program is fully installed. To execute it immediatly, run `python main.py`.  
If you need to execute the program after having already completed the install:  
## Run after install
 1. Open the program folder in File Explorer, and navigate into the "src" directory.
 2. Put your images into the /Images folder.
 3. Optionally modify special_cases.json
 4. If you have cover photos, put these into the /Covers folder.
 5. Open main.py in a text editor, and modify the first three lines to specify the file paths of your cover photos and data file.
 6. Paste your data CSV file into /src.
 7. Navigate into the "virtenv" folder, into the "Scripts" folder, right click "Activate.ps1" and select "Copy as Path".
 8. Go back to /src, right click anywhere in the folder, and select "Open in Terminal".
 9. Type `powershell -ExecutionPolicy Bypass -File ` (with a space at the end) and then paste the file path you just copied.  
    > If you are on Linux or MacOS, run `source virtenv/bin/activate`  instead.
 10. Run `python main.py`.
