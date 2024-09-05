# Streamlit App README

## Overview

This application provides an interactive way to navigate and view data related to USF practicums. The app includes two main views that you can switch between using the navigation bar:

1. **All Practicums** - Displays comprehensive data for all practicums.
2. **Individual Practicums** - Shows detailed tables for individual practicums.

## Features

- **Navigation Bar**: Allows users to easily switch between different views.
- **Dynamic Data Display**: Shows data and tables based on user selection.

## Requirements

To run this app, you will need:

- Python 3.x
- Streamlit
- `streamlit_navigation_bar` (for the navigation bar component)

## Setting Up the Environment

Follow these steps to set up a virtual environment and install the required packages:

1. **Clone the repository**:
2. **Navigate to the project directory**:
3. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**:

    - **On Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - **On macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

5. **Install the required libraries**:

    ```bash
    pip install pandas
    pip install requests
    pip install streamlit
    pip install streamlit_navigation_bar
    ```


## Running the App

1. **Ensure the virtual environment is activated** (refer to the activation instructions above).

2. **Run the Streamlit app**:

    ```bash
    streamlit run app/main.py
    ```

3. **Open your browser** and go to the URL provided in the terminal to view the app.

## File Structure

- `app.py`: Main application file that initializes the navigation bar and handles page rendering.
- `data.py`: Contains the `show_data` function which displays data for all practicums.
- `table.py`: Contains the `show_table` function which displays detailed tables for individual practicums.

## Functions

### `show_data()`

- **Purpose**: Displays data for all practicums.
- **Location**: Defined in `data.py`.

### `show_table()`

- **Purpose**: Displays detailed tables for individual practicums.
- **Location**: Defined in `table.py`.


## Configuring Data Source

The application uses a function to load data from a URL. You can configure it to fetch data directly from a CSV file available online or adjust it to use a local file. Here’s how you can set up the data source:

### Using a URL

1. **Edit the `load_data` Function**

   Open the `app.py` file and locate the `load_data` function. You'll see the `url` variable where you can specify the URL of the CSV file you want to load.
   To find the Google Sheet ID, follow these steps:

   Open the Google Sheet you want to find the ID for.

   Look at the URL in your browser's address bar. It will look something like this:

    ```
    https://docs.google.com/spreadsheets/d/1AbCDefGhIJKlmnOpQRsTuvWxYz/edit#gid=0
    ```
    The Google Sheet ID is the long string of characters between /d/ and /edit. In the example URL above, the ID is `1AbCDefGhIJKlmnOpQRsTuvWxYz.`

    You can copy this ID for use in various applications or scripts where you need to reference the specific Google Sheet.
   ```python
   @st.cache_data
    def load_data():
        google_id=''
        url = f"https://docs.google.com/spreadsheets/d/1qvDe5a66Vju5Cgp8v6Tty6MOhTdLQ0c6SzusIryDDi8/export?format=tsv&id=1qvDe5a66Vju5Cgp8v6Tty6MOhTdLQ0c6SzusIryDDi8&gid={google_id}"
        response = requests.get(url)
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data, sep="\t")
        return df

### Using a Local CSV File

1. **Edit the `load_data` Function**

   If you prefer to use a local TSV file instead of fetching it from a URL, modify the `load_data` function as follows:

   ```python
   @st.cache_data
   def load_data():
       file_path = "path/to/your/local/file.tsv"  # Provide the path to your local TSV file
       # Load the TSV data from the local file
       df = pd.read_csv(file_path, sep='\t')
       return df


