
import requests
import pandas as pd
import json

# API endpoint
url = "https://jsonplaceholder.typicode.com/users"


def extract_users():
    try:
        # Retrieve data
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        print("API request successful!")
        print("HTTP Status:", response.status_code)
        print("Total users:", len(data))

        # Save original JSON response
        with open("users_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        # Create flattened dataset
        df = pd.json_normalize(data)

        # Select core fields
        core_df = df[
            [
                "id",
                "name",
                "email",
                "address.city",
                "company.name"
            ]
        ].copy()

        core_df.columns = [
            "user_id",
            "name",
            "email",
            "city",
            "company"
        ]

        # Export datasets
        core_df.to_csv("users_core.csv", index=False)
        df.to_csv("users_flattened.csv", index=False)

        print("\nCore dataset exported successfully.")
        print("Flattened dataset exported successfully.")

        print("\nCore dataset preview:")
        print(core_df.head())

        print("\nFlattened dataset shape:", df.shape)

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    except (ValueError, KeyError) as error:
        print("Data processing error:", error)


if __name__ == "__main__":
    extract_users()
