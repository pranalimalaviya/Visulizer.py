import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")


print("Pandas Version :", pd.__version__)
print("NumPy Version :", np.__version__)
print("Matplotlib Version :", plt.matplotlib.__version__)
print("Seaborn Version :", sns.__version__)

import pandas as pd

data = pd.read_csv("Chocolate_Sales.csv")

print("Dataset Loaded Successfully!")

data.head(5)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    # Constructor
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        self.data = pd.read_csv("Chocolate_Sales.csv")
        print("Data loaded successfully")

    # Destructor
    def __del__(self):
        print("\nSalesDataAnalyzer object destroyed.")
        
    #Explore  Data
    def explore_data(self):

       if self.data is None:
           print("Please load dataset first.")
           return

       while True:

            print("\n========== EXPLORE DATA ==========")

            print("1. Display First 5 Rows")
            print("2. Display Last 5 Rows")
            print("3. Display Column Names")
            print("4. Display Data Types")
            print("5. Display Basic Information")
            print("6. Display Statistical Summary")
            print("7. Display Shape")
            print("8. Back")

            choice = input("Enter choice: ")

            
            if choice == '1':
                print(self.data.head())

            elif choice == '2':
                print(self.data.tail())

            elif choice == '3':
                print(self.data.columns)

            elif choice == '4':
                print(self.data.dtypes)

            elif choice == '5':
                print(self.data.info())

            elif choice == '6':
                print(self.data.describe(include='all'))

            elif choice == '7':
                print("Shape :", self.data.shape)

            elif choice == '8':
                break

            else:
                print("Invalid Choice")

    #Handle Missing Values

    def clean_data(self):

        if self.data is None:
            print("Load dataset first")
            return
        while True:

            print("\n========== HANDLE MISSING DATA ==========")

            print("1. Display Missing Values")
            print("2. Fill Numeric Missing Values with Mean")
            print("3. Fill Missing Values with Forward Fill")
            print("4. Drop Missing Rows")
            print("5. Replace Missing Values")
            print("6. Back")

            choice = input("Enter Choice : ")

            if choice == '1':
                print("Missing Values")
                print(self.data.isnull().sum())

            elif choice == '2':
                numeric = self.data.select_dtypes(include=np.number).columns

                for col in numeric:
                    self.data[col].fillna(self.data[col].mean(), inplace=True)
                    print("Missing values filled using mean.")

            elif choice == '3':

                self.data.fillna(method='ffi11', inplace=True)
                print("Forward Fill Completed.")

            elif choice == '4':

                self.data.dropna(inplace=True)
                print("Rows Removed.")

            elif choice == '5':

                value = input("Enter Replacement Value : ")

                self.data.fillna(value, inplace=True)

                print("Replacement Done.")

            elif choice == '6':
                break

            else:
                print("Invalid Choice.")

    #Numpy Operations
    def numpy_operations(self):

            if self.data is None:
                print("Load dataset first.")
                return

            print("\nAvailable Numeric Columns:")

            numeric = self.data.select_dtypes(include=np.number).columns

            for col in numeric:
                print(col)

            column = input("\nEnter Numeric Column Name : ")

            if column not in self.data.columns:
                print("Invalid Column")
                return

            array = self.data[column].to_numpy()

            print("\nNumPy Array")
            print(array)

            print("\nIndexing")

            if len(array) > 0:
                print("First Element :", array[0])

            print("\nSlicing")
            print(array[:5])

            print("\nElement-wise Operations")

            print("Array + 10")
            print(array + 10)

            print("\nArray * 2")
            print(array * 2)

            print("\nSquare Root")
            print(np.sqrt(array))

            print("\nSquare")
            print(np.square(array))

            print("\nStatistics")

            print("Sum :", np.sum(array))
            print("Mean :", np.mean(array))
            print("Maximum :", np.max(array))
            print("Minimum :", np.min(array))
            print("Standard Deviation :", np.std(array))
            print("Variance :", np.var(array))
            print("Median :", np.median(array))
            print("25 Percentile :", np.percentile(array,25))
            print("50 Percentile :", np.percentile(array,50))
            print("75 Percentile :", np.percentile(array,75))

    def mathematical_operations(self):

            if self.data is None:
                print("Load Dataset First.")
                return

            numeric = self.data.select_dtypes(include=np.number)

            if numeric.empty:
                print("No Numeric Columns Found.")
                return

            print("\n========= MATHEMATICAL OPERATIONS =========")

            print("Column Wise Sum")
            print(numeric.sum())

            print("\nColumn Wise Mean")
            print(numeric.mean())

            print("\nColumn Wise Maximum")
            print(numeric.max())

            print("\nColumn Wise Minimum")
            print(numeric.min())

            print("\nColumn Wise Product")
            print(numeric.product())

            print("\nColumn Wise Cumulative Sum")
            print(numeric.cumsum().head())

            print("\nColumn Wise Absolute Values")
            print(numeric.abs().head())


    #Search, Sort, Filter, Aggregate & Statistical Analysis
    def search_product(self):

            if self.data is None:
                print("Load dataset first.")
                return

            product = input("Enter Product Name : ")

            result = self.data[
                self.data["Product"].astype(str).str.lower()
                == product.lower()
            ]

            if result.empty:
                print("No Record Found.")
            else:
                print(result)


    def search_sales_id(self):

            if self.data is None:
                print("Load dataset first.")
                return

            sales_id = input("Enter Sales ID : ")

            result = self.data[
                self.data["SalesID"].astype(str) == sales_id
        ]

            if result.empty:
                print("No Record Found.")
            else:
                print(result)

    def search_sales_amount(self):

            if self.data is None:
                print("Load dataset first.")
                return

            amount = float(input("Enter Minimum Sales : "))

            result = self.data[
                self.data["Sales"] >= amount
            ]

            print(result)

    def sort_data(self):

            if self.data is None:
                print("Load dataset first.")
                return

            print("\nAvailable Columns")
            print(self.data.columns)

            column = input("Sort By : ")

            if column not in self.data.columns:
                print("Invalid Column")
                return

            order = input("Ascending (Y/N): ")

            if order.upper() == "Y":
                sorted_data = self.data.sort_values(
                    by=column,
                    ascending=True
                )
            else:
                sorted_data = self.data.sort_values(
                    by=column,
                    ascending=False
                )

            print(sorted_data)

    def filter_product(self):

            if self.data is None:
                return

            product = input("Enter Product : ")

            filtered = self.data[
                self.data["Product"].astype(str).str.lower()
                == product.lower()
            ]

            print(filtered)

    def aggregate_functions(self):

            if self.data is None:
                print("Load dataset first.")
                return

            numeric = self.data.select_dtypes(include="number")

            print("\n========== AGGREGATE FUNCTIONS ==========")

            print("\nSUM")
            print(numeric.sum())

            print("\nMEAN")
            print(numeric.mean())

            print("\nCOUNT")
            print(numeric.count())

            print("\nMAXIMUM")
            print(numeric.max())

            print("\nMINIMUM")
            print(numeric.min())

    def statistical_analysis(self):

            if self.data is None:
                print("Load dataset first.")
                return

            numeric = self.data.select_dtypes(include="number")

            print("\n========== STATISTICS ==========")

            print("\nDescribe")
            print(numeric.describe())

            print("\nMedian")
            print(numeric.median())

            print("\nMode")
            print(numeric.mode())

            print("\nVariance")
            print(numeric.var())

            print("\nStandard Deviation")
            print(numeric.std())

            print("\nQuantiles")
            print(numeric.quantile([0.25,0.50,0.75]))

            print("\nCorrelation Matrix")
            print(numeric.corr())


    def groupby_analysis(self):

            if self.data is None:
                return

            print("\nAvailable Columns")
            print(self.data.columns)

            column = input("Group By Column : ")

            if column not in self.data.columns:
                print("Invalid Column")
                return

            grouped = self.data.groupby(column).sum(
                numeric_only=True
            )

            print(grouped)

    def transform_sales(self):

            if self.data is None:
                return

            if "Sales" not in self.data.columns:
                print("Sales Column Not Found")
                return

            self.data["Sales_Normalized"] = (
                self.data["Sales"] /
                self.data["Sales"].max()
            )

            print(self.data.head())

    def search_sort_filter(self):

            while True:

                print(" SEARCH, SORT & FILTER MENU ")

                print("1. Search Product")
                print("2. Search Region")
                print("3. Search Sales ID")
                print("4. Search Sales Amount")
                print("5. Sort Data")
                print("6. Filter by Region")
                print("7. Filter by Product")
                print("8. Filter by Sales Range")
                print("9. Aggregate Functions")
                print("10. Statistical Analysis")
                print("11. GroupBy Analysis")
                print("12. Transform Sales")
                print("13. Back")

                choice = input("Enter Choice : ")

                if choice == "1":
                    self.search_product()

                elif choice == "2":
                    self.search_region()

                elif choice == "3":
                    self.search_sales_id()

                elif choice == "4":
                    self.search_sales_amount()

                elif choice == "5":
                    self.sort_data()

                elif choice == "6":
                    self.filter_region()

                elif choice == "7":
                    self.filter_product()

                elif choice == "8":
                    self.filter_sales_range()

                elif choice == "9":
                    self.aggregate_functions()

                elif choice == "10":
                    self.statistical_analysis()

                elif choice == "11":
                    self.groupby_analysis()

                elif choice == "12":
                    self.transform_sales()

                elif choice == "13":
                    break

                else:
                    print("Invalid Choice.")

    def prepare_amount(self):

            self.data["Amount"] = (
                self.data["Amount"]
                .replace(r'[$,]', '', regex=True)
                .astype(float)
            )

    def bar_plot(self):

            self.prepare_amount()
            sales = self.data.groupby("Country")["Amount"].sum()
            plt.figure(figsize=(8,5))
            plt.bar(sales.index, sales.values)
            plt.title("Total Sales by Country")
            plt.xlabel("Country")
            plt.ylabel("Amount")
            plt.grid(True)
            plt.show()

    def line_plot(self):

            self.prepare_amount()
            monthly = self.data.groupby("Date")["Amount"].sum()
            plt.figure(figsize=(10,5))
            plt.plot(monthly.index,
                    monthly.values,
                    marker="o")
            plt.title("Sales Trend")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.show()

    def scatter_plot(self):

            self.prepare_amount()
            plt.figure(figsize=(8,5))
            plt.scatter(self.data["Boxes Shipped"],
                        self.data["Amount"])
            plt.title("Boxes Shipped vs Amount")
            plt.xlabel("Boxes Shipped")
            plt.ylabel("Amount")
            plt.grid(True)
            plt.show()

    def pie_chart(self):

            self.prepare_amount()
            product = self.data.groupby("Product")["Amount"].sum()
            plt.figure(figsize=(8,8))
            plt.pie(product.values,
                    labels=product.index,
                    autopct="%1.1f%%")
            plt.title("Sales by Product")
            plt.show()
        
    def histogram(self):

            self.prepare_amount()
            plt.figure(figsize=(8,5))
            plt.hist(self.data["Amount"],
                    bins=10)
            plt.title("Amount Distribution")
            plt.xlabel("Amount")
            plt.ylabel("Frequency")
            plt.grid(True)
            plt.show()

    def stack_plot(self):

            self.prepare_amount()
            summary = self.data.groupby("Country")["Amount"].sum()
            x = range(len(summary))
            plt.figure(figsize=(8,5))
            plt.stackplot(x,
                        summary.values,
                        labels=["Sales"])
            plt.xticks(x, summary.index)
            plt.legend()
            plt.title("Stack Plot - Country Sales")
            plt.show()

    def subplot_chart(self):

            self.prepare_amount()
            fig, ax = plt.subplots(1,2, figsize=(12,5))
            country = self.data.groupby("Country")["Amount"].sum()
            ax[0].bar(country.index,
                    country.values)
            ax[0].set_title("Country Sales")
            product = self.data.groupby("Product")["Amount"].sum()
            ax[1].pie(product.values,
                    labels=product.index,
                    autopct="%1.1f%%")
            ax[1].set_title("Product Share")
            plt.tight_layout()
            plt.show()

    def heatmap(self):

            self.prepare_amount()
            numeric = self.data[["Amount","Boxes Shipped"]]
            plt.figure(figsize=(6,4))
            sns.heatmap(numeric.corr(),
                        annot=True,
                        cmap="Blues")
            plt.title("Correlation Heatmap")
            plt.show()

    def box_plot(self):

            self.prepare_amount()
            plt.figure(figsize=(8,5))
            sns.boxplot(data=self.data,
                        x="Country",
                        y="Amount")
            plt.title("Country Wise Sales")
            plt.xticks(rotation=30)
            plt.show()

    def save_plot(self):

            filename = input("Enter file name (Chocolate_Sales.png): ")

            plt.savefig("Chocolate_Sales.png")

            print("Visualization Saved Successfully!")

    def visualize_data(self):

            while True:

                print("\n========== DATA VISUALIZATION ==========")

                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. Pie Chart")
                print("5. Histogram")
                print("6. Stack Plot")
                print("7. Subplots")
                print("8. Heatmap")
                print("9. Box Plot")
                print("10. Save Plot")
                print("11. Back")

                choice = input("Enter Choice : ")

                if choice == "1":
                    self.bar_plot()

                elif choice == "2":
                    self.line_plot()

                elif choice == "3":
                    self.scatter_plot()

                elif choice == "4":
                    self.pie_chart()

                elif choice == "5":
                    self.histogram()

                elif choice == "6":
                    self.stack_plot()

                elif choice == "7":
                    self.subplot_chart()

                elif choice == "8":
                    self.heatmap()

                elif choice == "9":
                    self.box_plot()

                elif choice == "10":
                    self.save_plot()

                elif choice == "11":
                    break

                else:
                    print("Invalid Choice.")

def main():

    analyzer = SalesDataAnalyzer()

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Explore Data")
        print("2. Handle Missing Data")
        print("3. NumPy Operations")
        print("4. Mathematical Operations")
        print("5. Search / Sort / Filter")
        print("6. Data Visualization")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            analyzer.explore_data()

        elif choice == "2":
            analyzer.clean_data()

        elif choice == "3":
            analyzer.numpy_operations()

        elif choice == "4":
            analyzer.mathematical_operations()

        elif choice == "5":
            analyzer.search_sort_filter()

        elif choice == "6":
            analyzer.visualize_data()

        elif choice == "7":
            print("\nThank you for using Sales Data Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()