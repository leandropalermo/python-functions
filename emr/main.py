from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import (StringType, StructField, StructType)


def main():
    spark = SparkSession.builder.appName("EMRTestDemoApp").getOrCreate()
    simple_schema = StructType([
        StructField("username", StringType(), True),
        StructField("fname", StringType(), True),
        StructField("lname", StringType(), True)
    ])

    data = [("duda", "Maria Eduarda", "Rodrigues Palermo"), ("aylinha", "Ayla", "Rodrigues Palermo"),
            ("bia", "Beatriz", "Rodrigues Palermo")]
    df = spark.createDataFrame(data, simple_schema)
    df.show()


if __name__ == '__main__':
    main()
