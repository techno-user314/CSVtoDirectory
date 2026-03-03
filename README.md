# CSVtoDirectory
Converts directory information from a CSV file into a Word Document with two sections: A photo directory with names and photos, and a table containing information for each person. Optionally, cover pages can also be added.  
  
## Usage 
Copy the CSV file into the working directory of the program. It should have one row per person with the following headers:   

| Header | Contents |
| --- | --- |
| Family ID | Unique ID number for every family; Leave blank if person is single |
| First Name | Formal first name of the person |
| Preffered Name | Preferred first name of the person |
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
  
If you have cover photos, make sure they are in the /Covers folder.  
  
If there is info on the spreadsheet that needs to be adjusted before being put into the directory, out can be done automatically in special_cases.json.  
- To exclude a family, add the name of the primary member of the family in the "ignore family" list.
- To change a person's information, add the name of the person and then new info under the desired secion in "change info".
  For example, to change the family members listed for a person:
  Under "change info"/"family", paste { "name":"John Doe", "new info","John, Mary, Alice, Bob"} to override whatever is in the CSV.
  Notice that setting the "new info" field to "", will remove that person's info from the final directory.
  
Run the program (which should take about a minute), and "directory.docx" should appear in the working directory of the program.  
  
## Install and Build
 1. [Install Python](https://www.python.org/downloads/).
 2. Download the zip file for the [latest release](https://github.com/techno-user314/csv-to-directory/releases).
 3. Unzip the folder.
 4. Open the folder in File Explorer, and navigate into the "src" directory.
 5. Open main.py in a text editor, and modify the first three lines to specify the file paths of your cover photos and data file.
 6. Right click anywhere in the folder, and select "Open in Terminal".
 7. Run this command:
  - `python -m venv virtenv`
 8. Go back into File Explorer (but don't close your terminal window) and navigate into the new "virtenv" folder, into the "Scripts" folder, right click "Activate.ps1" and select "Copy as Path".
 9. Return to the terminal window and type `powershell -ExecutionPolicy Bypass -File ` (with a space at the end) and then paste the file path you just copied.  
    > If you are on Linux or MacOS, run `source virtenv/bin/activate`  instead.
 10. Run `pip install pandas python-docx pyinstaller`
 11. Run `python -m PyInstaller main.py`
 12. Wait for the command to finish, then go into /src/dist, cut main.exe, and paste it into the parent folder of /src (the on containing the /Images and /Covers folders).
 13. The program will run when you open main.exe (see usage instructions above).
