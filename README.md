# 📊 My Data Streaming App

A modular **PySpark** application for processing streaming text data, extracting counts of **“long words”** (≥5 letters) and **digits** per batch. Includes real-time console output, tabulated summaries, and visualizations.

Designed as a Python package with **unit tests** and **GitHub Actions CI**.

---

## 🚀 Features

- ✅ **Modular design**: Clean separation of logic:
  - `stream_processor` for streaming logic
  - `visualizer` for visualizations
  - `config` for parameters
- 🔍 **Pure helper function**: `analyze_line()` is testable without Spark
- ⚡ **Real-time streaming**: Processes micro-batches via Spark DStream queue
- 🖥️ **Console output**: Shows batch number, timestamp, line content, counts
- 📋 **Summary**: Tabulated long-word list with timestamps (via `tabulate`)
- 📊 **Visualization**: Bar chart of batch vs. long-word count (via `matplotlib`)
- 🧪 **Unit testing**: via `pytest`
- 🔄 **CI/CD**: GitHub Actions pipeline for linting & tests on every push/PR

---

## 📁 Project Structure

    my_streaming_app/
    ├── setup.py                # Package metadata & entry point
    ├── requirements.txt        # Runtime dependencies
    ├── src/
    │   └── streaming_app/
    │       ├── __init__.py
    │       ├── config.py           # Constants (e.g. sample data, batch interval)
    │       ├── stream_processor.py # Spark streaming logic & analyze_line()
    │       └── visualizer.py       # Tabulate & matplotlib plotting functions
    ├── tests/
    │   └── test_stream_processor.py # Unit tests for analyze_line()
    └── .github/
        └── workflows/
            └── ci.yml             # GitHub Actions CI pipeline

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yadavvinay77/Data_streaming.git
cd Data_streaming

# (Optional) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # On Linux/macOS
.venv\Scripts\Activate         # On Windows

# Install dependencies and the package
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

---

## ▶️ Usage

Run the streaming app via its console script:

```bash
streamapp
```

Default behavior:
- Simulates a stream of paragraphs
- Logs batch-wise information to the console
- Shows a tabulated summary
- Plots a bar chart of long-word counts per batch

Disable plotting with:

```bash
streamapp --no-plot
```

---

## 🧪 Testing

```bash
pytest -q
```

Your CI pipeline also runs tests automatically on every push and pull request.

---

## 📈 CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) performs:

- ✅ Repository checkout
- 🐍 Python 3.11 setup
- 📦 Install dependencies & package
- 🧪 Run `pytest` tests

---

## ✨ Extending

- Replace in-memory queue with:
  - socket
  - file stream
  - Kafka or any real-time data source
- Add environment-based config management
- Integrate Docker for deployment
- Publish to PyPI for public reuse

---

## 📜 License

**MIT License © 2025 Vinay Yadav**

Feel free to open [issues](https://github.com/yadavvinay77/Data_streaming/issues) or [pull requests](https://github.com/yadavvinay77/Data_streaming/pulls) — happy streaming! 🚀