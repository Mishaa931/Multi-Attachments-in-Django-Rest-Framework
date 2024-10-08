# Django Multi-Attachment Handling API with Import/Export

This Django project provides an API for managing leave applications with multiple file attachments.

## Features
- **Create Leave Application**: Apply for leave with multiple file attachments.
- **Update Leave Application**: Update an existing leave application and replace its file attachments.
- **File Size Validation**: Ensures uploaded files do not exceed the 3 MB limit.
- **Import Data**: Import data from a CSV file into a Django model using a management command.
- **Export Data**: Export data from a Django model to a CSV file.

## Setup
1. **Clone the repository:**

    ```bash
    git clone https://github.com/Mishaa931/Multi-Attachments-in-Django-Rest-Framework/.git
    cd Multi-Attachments-in-Django-Rest-Framework
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

## API Endpoints
### Create Leave Application
**Endpoint:** `POST /api/leave-apply/`

Upload leave application details along with attachments.

### Update Leave Application
**Endpoint:** `PUT /api/leave-apply/{id}/`

Update an existing leave application and replace its attachments.

## File Size Validation
The project includes a custom file size validator validate_file_size in the LeaveAttachmentSerializer. It limits the file size to 3 MB (modifiable).

## Example Payload
    
      {
        "from_date": "2024-08-27",
        "to_date": "2024-08-29",
        "apply_date": "2024-08-25T12:34:56Z",
        "approved_date": "2024-08-26",
        "report_back_date": "2024-08-30",
        "attachment": [<file1>, <file2>, ...]
      }

## How to Use

1. **Run the Django server:**

    ```bash
    python manage.py runserver
    ```

2. **Test the API Endpoints:**

   Use an API client like [Postman](https://www.postman.com/) to test the create and update endpoints for leave applications.
   
## Management Command

### Import Data from CSV

**Command:**

    python manage.py import_data <app_name> <model_name> <file_path>

The command reads data from the CSV file, processes it, and creates instances of the specified model.


Memory updated
Here’s the updated README with the new title and added import/export functionalities:

markdown
Copy code
# Django Multi-Attachment Handling API with Import/Export

A Django project for managing leave applications with support for multiple file attachments. Includes features for creating and updating leave applications, importing data from CSV files, and exporting data to CSV files. The project also includes file size validation to ensure attachments do not exceed 3 MB.

## Features

- **Create Leave Application**: Apply for leave with multiple file attachments.
- **Update Leave Application**: Update an existing leave application and replace its file attachments.
- **File Size Validation**: Ensures uploaded files do not exceed 3 MB.
- **Import Data**: Import data from a CSV file into a Django model using a management command.
- **Export Data**: Export data from a Django model to a CSV file.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

## API Endpoints

### Create Leave Application

**Endpoint:** `POST /api/leave-apply/`

Upload leave application details along with attachments.

### Update Leave Application

**Endpoint:** `PUT /api/leave-apply/{id}/`

Update an existing leave application and replace its attachments.

## Example Payload
    {
      "from_date": "2024-08-27",
      "to_date": "2024-08-29",
      "apply_date": "2024-08-25T12:34:56Z",
      "approved_date": "2024-08-26",
      "report_back_date": "2024-08-30",
      "attachment": [<file1>, <file2>, ...]
    }

## Management Command 
### Import Data from CSV

#### Command:

    python manage.py import_data <app_name> <model_name> <file_path>
    
This command imports data from a CSV file into a specified Django model.

**Arguments:**

- `app_name`: The name of the Django app.
- `model_name`: The name of the model.
- `file_path`: The path to the CSV file.

**Example:**

    python manage.py import_data multiattachment1 LeaveApply /path/to/your/file.csv

## Notes:

* File size is limited to 3 MB per attachment.
* The API returns the URLs of uploaded attachments in the response.


