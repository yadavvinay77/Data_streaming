# src/streaming_app/stream_processor.py
import re
from datetime import datetime

def analyze_line(line_number: int, text: str, timestamp: datetime) -> dict:
    """
    Analyze a single line: count words ≥5 chars and digits.
    Returns a dict with batch, long words count, list, digit count, and formatted time.
    """
    # extract words
    words = re.findall(r"\b\w+\b", text)
    long_words_list = [w for w in words if len(w) >= 5]
    long_words_count = len(long_words_list)
    digits_count = sum(ch.isdigit() for ch in text)
    ts_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    return {
        "batch":            line_number,
        "long_words":       long_words_count,
        "long_words_list":  long_words_list,
        "digits":           digits_count,
        "time":             ts_str
    }

def process_rdd(time_stamp, rdd, results_data, batch_details, spark):
    """
    Called on each micro‐batch. Wraps analyze_line.
    - time_stamp: datetime of the batch
    - rdd: the incoming RDD
    - results_data & batch_details: lists to append to
    - spark: SparkSession (to build DataFrame)
    """
    if rdd.isEmpty():
        return

    # convert to DataFrame to extract line_number & text
    df = spark.createDataFrame(rdd, ["line_number", "line"])
    ln, txt = df.collect()[0]

    # delegate to pure helper
    info = analyze_line(ln, txt, time_stamp)

    # save into your two lists
    results_data.append({
        "batch_number": info["batch"],
        "time":         info["time"],
        "long_words":   info["long_words"],
        "digits":       info["digits"]
    })
    batch_details.append({
        "Batch Number":            info["batch"],
        "Timestamp":               info["time"],
        "Words Count > 5 Letters": info["long_words"],
        "List of Long Words":      ", ".join(info["long_words_list"]) or "None"
    })
