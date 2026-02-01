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
  
Run the program (which should take about a minute), and "directory.docx" should appear in the working directory of the program.  
  
If there is info on the spreadsheet that needs to be adjusted before being put into the directory, out can be done automatically in special_cases.json.  