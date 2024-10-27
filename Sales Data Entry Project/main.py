import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

data = {
    "Date": [],
    "Product": [],
    "Quantity": [],
    "Sales Value": [],
    "Region": []
}


def add_sale():
    while True:
        try:
            date = input("Please enter the date (dd-mm-yyyy):\n").strip().lower()
            date = datetime.strptime(date, "%d-%m-%Y")
            data["Date"].append(date)
            break
        except ValueError:
            print("Please enter in this format (dd-mm-yyyy)")

    while True:
        product = input("Please enter the product name:\n").strip().lower()
        if len(product) > 20:
            print("Product name must not exceed 20 characters")
        elif len(product) < 3:
            print("Product name must not be less than 3 characters")
        else:
            data["Product"].append(product)
            break

    while True:
        try:
            quantity = float(input("Please enter the quantity sold:\n"))
            data["Quantity"].append(quantity)
            break
        except ValueError:
            print("Enter a valid value")

    while True:
        try:
            sales_value = float(input("Please enter the Sales Value:\n£"))
            data["Sales Value"].append(sales_value)
            break
        except ValueError:
            print("Enter a valid value")

    region = input("Please enter the sale region (Country):\n").strip().lower()
    data["Region"].append(region)


def view_sales():
    df = pd.DataFrame(data)
    print("Here is your Sales History")
    print("***************************")
    print(df)


def save_data():
    new_df = pd.DataFrame(data)
    new_df.to_csv("Sales_data.csv", index=False)


def view_filtered_data():
    df = pd.read_csv("Sales_data.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df["Day"] = df["Date"].dt.date
    while True:
        try:
            start_date = input("Enter your start date (dd-mm-yyyy):\n")
            start_date = datetime.strptime(start_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Your date must be in this format dd-mm-yyyy")

    while True:
        try:
            end_date = input("Enter your end date (dd-mm-yyyy):\n")
            end_date = datetime.strptime(end_date, "%d-%m-%Y")
            break
        except ValueError:
            print("Your date must be in this format dd-mm-yyyy")

    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
    print(filtered_df)

    plt.plot(filtered_df["Day"], filtered_df["Sales Value"], label="Sales", marker="x")
    style1 = {'fontweight': 'bold'}
    plt.title("Sales Chart", fontdict=style1)
    plt.xlabel("Day", fontdict=style1)
    plt.ylabel("Sales", fontdict=style1)

    plt.legend()
    plt.show()


def sales_data_info():
    while True:
        print("Select from the following")
        print("1. Show Total Sales")
        print("2. Show average Sales")
        print("3. Total quantity sold")
        print("5. Exit")
        choice = input("")
        if choice == "1":
            df = pd.read_csv("Sales_data.csv")
            sales_sum = df["Sales Value"].sum()
            print(f"Your total sales are:\n£{sales_sum}")
            break
        elif choice == "2":
            df = pd.read_csv("Sales_data.csv")
            sales_average = df["Sales Value"].mean()
            print(f"Your sales average are:\n£{sales_average}")
            break
        elif choice == "3":
            df = pd.read_csv("Sales_data.csv")
            quantity_sum = df["Quantity"].sum()
            print(f"Your total quantity sold is:\n{quantity_sum}")
            break
        elif choice == "5":
            break
        else:
            print("Please enter a valid input")


def main():
    while True:
        print("Welcome...Select from the following options:\n")
        print("1. Add a new sale")
        print("2. View Sales History")
        print("3. View Filtered Sales History With Graph")
        print("4. Save data to CSV File")
        print("5. Sales Data")
        choice = input("")
        if choice == "1":
            add_sale()
            print("Sale successfully added")
        elif choice == "2":
            view_sales()
        elif choice == "3":
            view_filtered_data()
        elif choice == "4":
            save_data()
            print("Sales Data Saved To CSV File")
        elif choice == "5":
            sales_data_info()

        else:
            print("Enter a valid choice")


main()
