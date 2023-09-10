# scum-json-to-sheets
SCUM JSON to Google Sheets utility 

The goal of the project is to create a tool with a GUI that facilitates the interaction between JSON files and Google Sheets. This tool will essentially serve as a bridge to translate and synchronize data between these two formats..

Main objectives and specific requirements:

1. The tool should allow users to select a JSON file. This file's data should then be populated into a Google Sheet, including additional fields for user input for categorization (such as weapons, food, health, etc.). This will help sort and manage the data.
2. The tool should allow for the creation and storage of backup copies of both the original Google Sheet and the original JSON file, providing an option for the user to specify custom names for these backup files.
3. The Google Sheet should be editable, with any changes made to the sheet directly reflected in the JSON file's corresponding fields. This implies a two-way data synchronization between the Google Sheet and the JSON file. *Requires access via a service account*
4. The interface should reflect the exact structure of the current Google Sheet being used, allowing users to clone it and work with an accurate representation of their data.
5. Users should be able to open any JSON file, populate a Google Sheet with its data, edit the sheet, and save it under a new unique file name for later re-use. 
6. Once the Google Sheet editing is complete, the tool should write the changes to a new JSON file and save it under a new unique name. This file should then be ready for loading into the game. 
7. Users should be able to switch between different saved JSON files at any point, likely to modify game settings or data as needed.
This tool is aimed at facilitating the management of game data, allowing for better flexibility, categorization, and backup of game information. 
 The ultimate aim is to provide an easy-to-use and effective way to manipulate game data through a Google Sheet interface, improving the game's adaptability and maintainability.

