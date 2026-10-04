from pyspark.sql import SparkSession, DataFrame, types as t
from datetime import date


def dummy_data_ingestion(spark: SparkSession) -> DataFrame:
    """
    Dummy data ingestion, creating fake data within a Function to test creating data on
    Databricks.
    :return: Spark DataFrame containing the dummy data.
    """
    schema = t.StructType(
        [
            t.StructField("investor_id", t.StringType(), False),
            t.StructField("name", t.StringType(), False),
            t.StructField("email", t.StringType(), False),
            t.StructField("total_portfolio_value", t.DoubleType(), False),
            t.StructField("account_creation_date", t.DateType(), False),
            t.StructField("holdings_count", t.IntegerType(), False),
            t.StructField("annual_return_percentage", t.DoubleType(), False),
        ]
    )

    data = [
        (
            "INV001",
            "Alice Johnson",
            "alice.johnson@email.com",
            250000.50,
            date(2020, 3, 15),
            12,
            8.5,
        ),
        (
            "INV002",
            "Bob Smith",
            "bob.smith@email.com",
            1200000.75,
            date(2018, 7, 22),
            28,
            12.3,
        ),
        (
            "INV003",
            "Carol Williams",
            "carol.williams@email.com",
            450000.00,
            date(2021, 1, 10),
            18,
            6.8,
        ),
        (
            "INV004",
            "David Martinez",
            "david.martinez@email.com",
            800000.25,
            date(2019, 11, 5),
            22,
            10.2,
        ),
        (
            "INV005",
            "Emma Thompson",
            "emma.thompson@email.com",
            620000.00,
            date(2020, 9, 30),
            15,
            9.7,
        ),
    ]

    return spark.createDataFrame(data, schema=schema)


if __name__ == "__main__":
    spark_session = SparkSession.builder.appName("ingestion").getOrCreate()
    df = dummy_data_ingestion(spark_session)
    df.show()