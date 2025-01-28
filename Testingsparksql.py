
print("add new line")

df = spark.sql("select * from hls_yatish.hls_interop_yatish.cohort ")
display(df)

