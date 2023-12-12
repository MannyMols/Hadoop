from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a Spark session
spark = SparkSession.builder.appName("globalCO2emissions").getOrCreate()

# Define the schema
customSchema = StructType([
    StructField("column1", StringType(), True),
    StructField("column2", StringType(), True),
    StructField("column3", StringType(), True),
    StructField("column4", StringType(), True),
    StructField("column5", StringType(), True),
    StructField("column6", StringType(), True),
    StructField("column7", StringType(), True),
    StructField("column8", StringType(), True),
    StructField("column9", StringType(), True),
    StructField("column10", StringType(), True),
    StructField("column11", StringType(), True),
    StructField("column12", StringType(), True),
    StructField("column13", StringType(), True),
])
# Read the CSV file into a DataFrame with the specified schema
df = spark.read.csv("/Users/ebimol/Downloads/Big Data /Dataset /globalCO2emissions.csv", header=False, inferSchema=True)
# Select and rename the relevant columns
df = df.select(
    col("_c0").alias("id"),
    col("_c1").alias("country"),
    col("_c4").alias("indicator"),
    col("_c5").alias("unit"),
    col("_c10").alias("industry"),
    col("_c28").alias("2011"),
    col("_c29").alias("2012"),
    col("_c30").alias("2013"),
    col("_c31").alias("2014"),
    col("_c32").alias("2015"),
    col("_c33").alias("2016"),
    col("_c34").alias("2017"),
    col("_c35").alias("2018")
)

# Assuming the DataFrame is already loaded and named 'df'
countries_to_select = ["Australia", "Austria", "Belgium", "Canada", "India", "Germany", "Japan", "New Zealand", "South Africa", "United Kingdom"]
selected_countries_df = df.filter(col("country").isin(countries_to_select))

# Filter industries
industries_to_select = ["Air transport", "Motor vehicles, trailers and semi-trailers"]
selected_countries_and_industries_df = selected_countries_df.filter(col("industry").isin(industries_to_select))

# Count and show the total number of rows
total_rows = selected_countries_and_industries_df.count()
print(f"Total number of rows: {total_rows}")

# Show the resulting DataFrame
selected_countries_and_industries_df.show()