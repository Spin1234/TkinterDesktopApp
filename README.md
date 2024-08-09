# TkinterDesktopApp
Tkinter Desktop app that perform store data, retrieve, display data and delete data from database.

# Person Image Storage Application

This application is a simple GUI program developed using Python's Tkinter library. It allows users to add persons to a SQLite database along with an image of the person. Users can also view all the stored persons and delete entries as needed.

## Features

- **Add Person**: Enter a name and upload an image to store the person's details in a SQLite database.
- **Show All Persons**: Display all stored persons in a new window with their names and images.
- **Delete Person**: Remove a person from the database.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
- PIL (Pillow) for image processing
- SQLite3 for database management

## Installation

1. Ensure you have Python installed on your system.
2. Install the required packages using pip:
   ```bash
   pip install pillow


## Workings

### Main Window Setup

- The application begins by creating a Tkinter window object using `tkinter.Tk()`.
- The window's geometry is set to `300x300`, and its title is set to "Add Person".

### Upload Image Functionality

- The `upload_image` function allows users to select an image file using a file dialog.
- The file path of the selected image is inserted into the entry widget `e2` for display and use.

### Add Person Functionality

- The `add_person` function is responsible for inserting a new person's name and image into the database.
- A nested function, `convertToBinaryData`, converts the image file into binary data suitable for storage in the database.
- The function connects to the `persondb.db` SQLite database and ensures the `PERSONS` table exists, creating it if necessary.
- It checks if both the name and image fields are filled and whether the image already exists in the database to prevent duplicates.
- If the entry is new, the function inserts the name and binary image data into the database and displays a success message.

### Show All Persons Functionality

- The `show_all` function creates a new window displaying all persons stored in the database.
- It retrieves all rows from the `PERSONS` table and iterates over them to create labels displaying the name and image.
- The image data is converted back to an image using `PIL` and displayed using `ImageTk.PhotoImage`.

### Delete Functionality

- The `delete` function is defined to remove an entry from the database.
- It confirms the deletion with the user using a message box to ensure intentional deletion.
- If confirmed, it deletes the entry with the specified `id` from the database and updates the display.
