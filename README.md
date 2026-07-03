# Chemstractor 🧪

```text
   ________                                         __             
  / ____/ /_  ___  ____ ___  _______________ ______/ /_____  _____ 
 / /   / __ \/ _ \/ __ `__ \/ ___/ ___/ ___/ __ `/ __/ __ \/ ___/ 
/ /___/ / / /  __/ / / / / (__  |__  ) /  / /_/ / /_/ /_/ / /     
\____/_/ /_/\___/_/ /_/ /_/____/____/_/   \__,_/\__/\____/_/      

           .---.
          |[ ]  |                 🧪 Chemstractor v0.1.0
          |  _  |                 Chemistry Table & Metadata Extraction
          | (_) |                 
         /       \                Powered by Docling & LLMs
        /    o    \               
       /  o     o  \              
      /_____________\             
```

**Chemstractor** is a powerful command-line tool designed to orchestrate the extraction, classification, and summarisation of chemistry-related table data and metadata from scientific PDFs. By combining robust document layout analysis (via **Docling**) with modern Large Language Models (online via **Gemini** and offline via **Ollama / Llama**), Chemstractor automates the conversion of complex scientific publications into clean, structured datasets.

---

## ✨ Features

- **📄 Document Layout Extraction**: Powered by **Docling** to parse PDF structures into clean markdown files, extracting in-memory tables and saving them in both CSV and TXT formats.
- **💎 Hardware Acceleration**: Out-of-the-box support for hardware backends (DirectML for Windows AMD/Intel GPUs, CUDA for NVIDIA, and MPS for Apple Silicon).
- **🏷️ Smart Table Categorisation**: Automatically inspects and categorizes extracted tables (e.g., reaction conditions, reagents, catalyst screenings) using configured LLMs.
- **📝 Metadata Retrieval**: Automatically parses publication metadata such as Paper Title, Authors, and DOI.
- **✍️ Condition Summarisation**: Leverages LLM reasoning to summarize experimental reaction conditions, yields, and chemical formulations directly from the extracted tables.
- **⚖️ Pipeline Validation**: Supports validation commands to compare pipeline outputs directly against ground-truth validation datasets, reporting precise key-value matching percentages.
- **📊 Excel Reporting**: Compiles output folders into professional, multi-sheet Excel workbooks (`.xlsx`) for easy downstream analysis.

---

## 📂 Pipeline Output Structure

When processing a PDF, Chemstractor generates a clean output directory structure containing everything from raw extractions to final AI summaries:

```text
[Output Directory]/
└── 📂 [pdf_filename_without_extension]/
    ├── 📂 extract/
    │   ├── 📄 clean_[filename].pdf      # Copy of the original processed PDF
    │   ├── 📄 output.md                 # Document content parsed into Markdown
    │   ├── 📄 log_[filename].log        # Complete timing and parser logs
    │   └── 📂 tables/
    │       ├── 📊 table1.csv            # Raw table data in CSV format
    │       └── 📄 table1.txt            # Raw table content in formatted text
    │
    ├── 📂 categorisation/
    │   └── 📄 table1.json               # Table category tags (JSON)
    │
    └── 📂 summary/
        ├── 📄 summary.json              # Paper metadata and summarized reaction conditions
        └── 📊 tables_summary.csv        # Tabular summary compilation
```

---

## ⚡ Getting Started

### 1. Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com/) (Optional, required for offline/local model usage)

### 2. Installation

Clone the repository and install the dependencies inside a virtual environment:

```bash
# Clone the repository
git clone https://github.com/henry/ChemistryExtract.git
cd ChemistryExtract

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -e .
```

### 3. Environment Configuration

Create a `.env` file in the root directory to store your Gemini API Key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🚀 CLI Reference

Chemstractor exposes a rich command-line interface via `click`.

> [!TIP]
> If you run any processing commands without specifying the `--model` flag, Chemstractor will open an interactive menu letting you choose the target model.

### Complete Process Pipeline
Process an entire PDF file (runs extraction, categorisation, metadata, and summarisation):
```bash
python src/chemstractor/main.py process path/to/paper.pdf [output_dir] --model gemini-2.5-flash
```
*Use the `-d` or `--direct` flag to re-run pipeline steps on a folder containing pre-extracted data.*

### Batch Process Directory
Process all PDF files found within a directory:
```bash
python src/chemstractor/main.py process_all path/to/pdf_dir/ [output_parent_dir] --model gemini-2.5-flash
```

### Extract Only
Extract text and tables from a PDF (no LLM classification or summarisation):
```bash
python src/chemstractor/main.py extract path/to/paper.pdf [output_dir]
```

### Categorise Only
Categorise extracted tables:
```bash
python src/chemstractor/main.py categorise path/to/paper.pdf [output_dir] --model gemini-2.5-flash
```

### Summarise Only
Summarise reaction conditions and metadata:
```bash
python src/chemstractor/main.py summarise path/to/paper.pdf [output_dir] --model gemini-2.5-flash
```

### Validate Outputs
Compare extracted run results against a directory of correct ground-truth validation files:
```bash
python src/chemstractor/main.py validate path/to/run_output/ path/to/validation_data/
```

### Batch Validation
Validate all runs under the run parent folder against the validation folder:
```bash
python src/chemstractor/main.py validate_all [outputs_dir] [validation_dir]
```

### Excel Report Generation
Compile run results into an Excel report (`.xlsx` file):
```bash
python src/chemstractor/main.py report path/to/processed_output_folder/ -o reports/compilation.xlsx
```

---

## 🤖 Supported Models

Chemstractor supports both online LLM providers and local/offline engines:

### ☁️ Online Models (Google Gemini)
Configured with input/output pricing parameters per 1M tokens:
- `gemini-2.5-flash`
- `gemini-2.5-pro`
- `gemini-3.5-flash`
- `gemini-3.1-flash-lite`

### 💻 Offline Models (Ollama)
Run models locally on your hardware without internet requirements:
- `llama3.1`
- `llama3`

---

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.

---

```text
       O   H
       ║  ╱
       C ─── N ─── H          Happy Extracting!
      ╱ ╲                     🧪✨
     H   O ─── CH₃
```
