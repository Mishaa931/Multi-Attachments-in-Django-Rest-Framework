# Django Multi-Attachment Handling API

This Django project provides an API for managing leave applications with multiple file attachments.

## Features
- **Create Leave Application**: Apply for leave with multiple file attachments.
- **Update Leave Application**: Update an existing leave application and replace its file attachments.
- **File Size Validation**: Ensures uploaded files do not exceed the 3 MB limit.

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
