# tests/test_stream_processor.py
import re
from streaming_app.stream_processor import process_rdd

def test_long_word_extraction(tmp_path):
    # simulate an RDD with one line
    line = "Testing longerword and short"
    # mock time_stamp and results_data
    results, details = [], []
    class DummyRDD:
        def isEmpty(self): return False
        def collect(self): return [(1, line)]
    from datetime import datetime
    process_rdd(datetime(2025,1,1,0,0,0), DummyRDD(), results, details)
    assert results[0]["long_words"] == 1
    assert "longerword" in details[0]["List of Long Words"]
