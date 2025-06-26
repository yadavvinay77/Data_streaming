# src/streaming_app/stream_processor.py
import re
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

def create_spark_stream(batch_interval=1):
    spark = SparkSession.builder.master("local[*]").appName("StreamingApp").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark, StreamingContext(spark.sparkContext, batch_interval)

def process_rdd(time_stamp, rdd, results_data, batch_details):
    """Extract long-words count and digit count from each RDD."""
    if rdd.isEmpty():
        return
    df = spark.createDataFrame(rdd, ["line_number","line"])
    ln, txt = df.collect()[0]
    words = re.findall(r"\b\w+\b", txt)
    long_words = [w for w in words if len(w) >= 5]
    long_count = len(long_words)
    digit_count = sum(ch.isdigit() for ch in txt)
    ts_str = time_stamp.strftime("%Y-%m-%d %H:%M:%S")

    results_data.append({"batch": ln, "time": ts_str,
                         "long_words": long_count, "digits": digit_count})
    batch_details.append({"Batch Number": ln, "Timestamp": ts_str,
                          "Words Count > 5 Letters": long_count,
                          "List of Long Words": ", ".join(long_words) or "None"})
