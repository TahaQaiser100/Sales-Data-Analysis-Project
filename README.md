# Sales Tracker

A simple Python application for tracking and analyzing sales data. This application allows users to add sales records, view and filter sales history, generate a graph of filtered sales, and calculate total and average sales data. It also saves sales data in a CSV format for future reference.

## Features

- **Add a New Sale**: Allows users to input details of a sale, including date, product, quantity, sales value, and region.
- **View Sales History**: Displays all recorded sales in tabular format.
- **Save Data to CSV**: Saves all sales data to a CSV file for persistent storage.
- **View Filtered Sales History with Graph**: Filters sales records within a specified date range and generates a line plot showing sales values over time.
- **Sales Data Summary**: Provides total sales, average sales, and total quantity sold statistics.

## Requirements

- Python 3.x
- Pandas library
- Matplotlib library

To install the required libraries, run:

```bash
pip install pandas matplotlib
```

## Usage

Follow the on-screen menu to navigate through the features:

   - **Add a New Sale**: Record new sales data.
   - **View Sales History**: Display all sales records.
   - **Save Data to CSV**: Save sales records to `Sales_data.csv`.
   - **View Filtered Sales History with Graph**: View sales data within a date range and display it in a graph.
   - **Sales Data Summary**: Show total sales, average sales, and total quantity sold.

## Data Format

Each sale includes:

- **Date**: Sale date (dd-mm-yyyy)
- **Product**: Name of the product (3-20 characters)
- **Quantity**: Quantity sold
- **Sales Value**: Total sales value (in GBP)
- **Region**: Sales region or country

## Example Output

- **Sales History**: Displays all recorded sales in tabular format.
- **Filtered Sales Graph**: Line plot showing sales values within the filtered date range.
- **Sales Data Summary**: Displays total and average sales, and total quantity sold.

## License

