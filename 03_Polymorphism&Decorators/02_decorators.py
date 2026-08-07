def pandas_decorators(fx):

    def mainfunc(*args):
        response = fx(*args)
        response.to_parquet(r"C:\Users\Suryansh\Documents\gitsql\Python-for-DE-Advanced\03_polymorphism&decorators\output.parquet")
        return response
    return mainfunc

@pandas_decorators
def csv_to_parquet(file_path:str):
    import pandas as pd
    df = pd.read_csv(file_path)
    return df.head()

response = csv_to_parquet(r"C:\Users\Suryansh\Documents\gitsql\SQL- Data-Warehouse\Project DW\sql-data-warehouse-project-main\datasets\source_crm\cust_info.csv")
print(response)
