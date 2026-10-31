# REST API to CSV Project

## 1. Project Overview

The project retrieves  data from a REST API.It examines the JSON structure, extracts important fields, flattens nested dictionaries, and exports the results into CSV files using Python.

## 2. Data Source

- API: JSONPlaceholder Users API
- URL: https://jsonplaceholder.typicode.com/users
- Data type: JSON
- Data acquisition method: HTTP GET request using Python Requests.


## 3. Technologies Used

- Python
- Requests
- Pandas
- JSON

## 4. Project Files

- `main.py`: Retrieves and processes API data.
- `requirements.txt`: Lists the required Python libraries.
- `users_core.csv`: Stores selected user fields.
- `users_flattened.csv`: Stores the flattened user records.
- `.gitignore`: Excludes the virtual environment and unnecessary files.

## 5. Data Structure and Nested Fields

| Field | Description | Depth |
|---|---|---|
| `id` | User identifier | 1 |
| `name` | User name | 1 |
| `email` | Email address | 1 |
| `address.city` | City | 2 |
| `address.geo.lat` | Latitude | 3 |
| `address.geo.lng` | Longitude | 3 |
| `company.name` | Company name | 2 |

Depth 1 indicates a top-level field. Depth 2 indicates a field inside one nested dictionary. Depth 3 indicates a field inside two nested dictionaries.

## 6. Outputs

The program generates two CSV files:

- `users_core.csv` contains the user ID, name, email, city, and company.
- `users_flattened.csv` contains the available user fields in flattened form.

## 7. How to Run

Install dependencies:

`python -m pip install -r requirements.txt`

Run the program:

`python main.py`

## 8. Error Handling

The program handles HTTP errors, request timeouts, invalid JSON responses, and CSV file-writing errors.
