# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.getOrCreate()
# COMMAND ----------
schema = StructType([
  StructField('CustomerID', IntegerType(), False),
  StructField('FirstName',  StringType(),  False),
  StructField('LastName',   StringType(),  False)
])
# COMMAND ----------
data = [
  [ 1000, 'Mathijs', 'Oosterhout-Rijntjes' ],
  [ 1001, 'Joost',   'van Brunswijk' ],
  [ 1002, 'Stan',    'Bokenkamp' ]
]
# COMMAND ----------
customers = spark.createDataFrame(data, schema)
customers.show()


