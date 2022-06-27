from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('py_spark').getOrCreate()

dataFrame = spark.read.csv("/home/pk/Downloads/CHARTS/charts_01")
dataFrame.printSchema()
dataFrame.show(truncate=False)