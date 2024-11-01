from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import (StringType, StructField, StructType)

def main():
    spark = SparkSession.builder \
        .appName("MyApp") \
        .config("spark.cassandra.connection.host", "cassandra.us-east-1.amazonaws.com:9142") \
        .config("spark.cassandra.auth.username", "leandropalermo-keyspace+1-at-137007611514") \
        .config("spark.cassandra.auth.password", "EMxJQZHSZl5PrpwQaj1oa804GmzkzoG8uagwsAGMfmE=") \
        .config("spark.sql.extensions", "com.datastax.spark.connector.CassandraSparkExtensions") \
        .getOrCreate()

    df = spark.read.format("org.apache.spark.sql.cassandra") \
        .options(table="user", keyspace="aws") \
        .load()

    df.show()


if __name__ == '__main__':
    main()
