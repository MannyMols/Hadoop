from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("globalEVdata").getOrCreate()

# Define the schema
customSchema = StructType([
    StructField("column1", StringType(), True),
    StructField("column2", StringType(), True),
    StructField("column3", StringType(), True),
    StructField("column4", StringType(), True),
    StructField("column5", StringType(), True),
    StructField("column6", StringType(), True),
    StructField("column7", StringType(), True),
])
# Read the CSV file into a DataFrame with the specified schema
df = spark.read.csv("/Users/ebimol/Downloads/Big Data /Dataset /IEA_Global_EV_Data2023.csv", header=False, inferSchema=True)
# Select and rename the relevant columns
df = df.select(
    col("_c0").alias("Region"),
    col("_c2").alias("Parameter"),
    col("_c3").alias("Mode"),
    col("_c4").alias("Powertrain"),
    col("_c5").alias("Year"),
    col("_c6").alias("Unit"),
    col("_c7").alias("Value"),
)

# Assuming the DataFrame is already loaded and named 'df'
countries_to_select = ["Australia", "Austria", "Belgium", "Canada", "India", "Germany", "Japan", "New Zealand",
                       "South Africa", "United Kingdom"]
selected_countries_df = df.filter(col("Region").isin(countries_to_select) & (col("Powertrain") == "EV"))

# Count and show the total number of rows
total_rows = selected_countries_df.count()
print(f"Total number of rows: {total_rows}")

# Show the DataFrame with the selected countries
selected_countries_df.show()
