# Chemstractor 🧪

```text
   ________                                         __             
  / ____/ /_  ___  ____ ___  _______________ ______/ /_____  _____ 
 / /   / __ \/ _ \/ __ `__ \/ ___/ ___/ ___/ __ `/ __/ __ \/ ___/ 
/ /___/ / / /  __/ / / / / (__  |__  ) /  / /_/ / /_/ /_/ / /     
\____/_/ /_/\___/_/ /_/ /_/____/____/_/   \__,_/\__/\____/_/      

           .---.
          |     |                 🧪 Chemstractor v0.1.0
          |     |                 Chemistry Table & Metadata Extraction
          |     |                 
         /       \                Powered by Docling & LLMs
        /    o    \               
       /  o     o  \              
      /_____________\             
```

**Chemstractor** is an automated pipeline and command-line tool for extracting, categorising, interpreting, and synthesising chemistry table data and metadata from scientific publications. Combining document layout parsing (**Docling**) with Large Language Models (**Google Gemini** or local **Ollama**), Chemstractor turns complex PDF literature into structured, homogenised datasets and Excel reports.

---

## ✨ Key Features

- **📄 Document Layout Extraction**: Uses **Docling** to parse PDF structures into Markdown and extract tables into CSV and formatted text files.
- **🏷️ Table Categorisation**: Automatically classifies extracted tables (e.g. reaction conditions, physical parameters, screening results) using configured LLMs.
- **📝 Metadata & Condition Summarisation**: Extracts paper metadata (title, authors, DOI) and synthesises experimental reaction parameters, yields, and formulations.
- **🔬 Parameter Interpretation**: Extracts and interprets specialised chemical coefficients, such as **Flory-Huggins** interaction parameters and **Mark-Houwink** parameters.
- **🔄 Data Combination & Homogenisation**: Standardises chemical names (solvents & polymers) across multiple papers, generates combined datasets, and plots summary diagrams (e.g., Sankey flowcharts).
- **📥 Paper Downloader**: Bulk downloads open-access research papers from **OpenAlex** via keyword or semantic search.
- **📊 Excel Reporting**: Compiles extractions into structured, multi-sheet Excel workbooks (`.xlsx`).
- **⚖️ Pipeline Validation**: Benchmark extraction accuracy against ground-truth validation datasets.

---

## ⚡ Setup Tutorial

Follow these steps to get Chemstractor installed and ready on your system.

### 1. Prerequisites

- **Python 3.10** or higher
- **Git**
- **Ollama** *(Optional — required only for offline/local model execution)*

### 2. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/henry/ChemistryExtract.git
   cd ChemistryExtract
   ```

2. **Create and activate a virtual environment:**
   - On **Windows (PowerShell)**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - On **Linux / macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the package and dependencies:**
   ```bash
   pip install -e .
   ```

### 3. Environment Configuration

Create a `.env` file in the root directory to configure your API credentials for online models (Google Gemini):

```env
API_KEY=your_gemini_api_key_here
```

> [!NOTE]
> If you are using local models via Ollama (e.g. `gemma4:31b`), ensure the Ollama application or daemon is running (`ollama serve`) and pull the target model (`ollama pull gemma4:31b`).

---

## 🚀 Quick Start Tutorial

Here is a quick walkthrough showing how to download scientific papers, extract data, interpret results, and build a unified dataset.

### Step 1: Download Scientific Papers (Optional)
Fetch 5 Open Access papers on polymer solutions from OpenAlex:
```bash
python src/chemstractor/main.py download "polymer solution viscosity" --limit 5 -n test_papers
```

### Step 2: Process a Single PDF
Run the full pipeline (extraction, categorisation, metadata, summarisation, and interpretation) on a single PDF paper:
```bash
python src/chemstractor/main.py process path/to/paper.pdf output_folder --model gemini-2.5-flash --all
```

### Step 3: Batch Process a Folder of PDFs
Process an entire directory of PDFs into individual structured output folders:
```bash
python src/chemstractor/main.py process_all path/to/pdf_dir output_parent_dir --model gemini-2.5-flash --all
```

### Step 4: Combine & Homogenise Data Across Papers
Homogenise chemical names and aggregate parameter tables across all processed papers into an Excel workbook:
```bash
python src/chemstractor/main.py combine output_parent_dir -o report.xlsx --model gemini-2.5-flash
```

---

## 📖 CLI Reference

Chemstractor provides a command-line interface driven by `click`. 

> [!TIP]
> If you omit the `--model` flag in processing commands, Chemstractor will open an interactive selector menu.

### Core Pipelines

| Command | Description | Example Usage |
| :--- | :--- | :--- |
| `process` | Process a single PDF paper | `python src/chemstractor/main.py process paper.pdf out_dir --all` |
| `process_all` | Batch process all PDFs in a folder | `python src/chemstractor/main.py process_all ./corpus ./outputs --all` |
| `combine` | Standardise & merge extractions across papers | `python src/chemstractor/main.py combine ./outputs -o dataset.xlsx` |
| `download` | Bulk download OpenAccess PDFs from OpenAlex | `python src/chemstractor/main.py download "flory huggins" -l 10` |

### Stage-by-Stage Commands

- **Extract Only** (Docling layout parsing):
  ```bash
  python src/chemstractor/main.py extract path/to/paper.pdf [output_dir]
  python src/chemstractor/main.py extract_all path/to/pdf_dir/ [output_dir]
  ```

- **Categorise Only** (Table classification):
  ```bash
  python src/chemstractor/main.py categorise path/to/paper.pdf [output_dir] --model gemini-2.5-flash
  ```

- **Metadata & Summarise**:
  ```bash
  python src/chemstractor/main.py metadata path/to/paper.pdf [output_dir] --model gemini-2.5-flash
  python src/chemstractor/main.py summarise path/to/paper.pdf [output_dir] --model gemini-2.5-flash
  ```

- **Interpret Coefficients** (Flory parameters `-f` / Mark-Houwink `-m`):
  ```bash
  python src/chemstractor/main.py interpret path/to/paper.pdf [output_dir] --flory --model gemini-2.5-flash
  python src/chemstractor/main.py interpret_all path/to/pdf_dir [output_dir] --flory --model gemini-2.5-flash
  ```

- **Excel Reporting**:
  ```bash
  python src/chemstractor/main.py report path/to/processed_output_folder -o report.xlsx
  ```

- **Validation & Benchmarking**:
  ```bash
  python src/chemstractor/main.py validate path/to/output/ path/to/ground_truth/
  python src/chemstractor/main.py validate_all path/to/runs/ path/to/ground_truth/
  ```

---

## 🤖 Supported Models

Chemstractor supports both cloud API models and local offline execution:

### ☁️ Cloud Models (Google Gemini)
Requires `API_KEY` set in `.env`:
- `gemini-2.5-flash`
- `gemini-2.5-pro`
- `gemini-3.5-flash`
- `gemini-3.1-flash-lite`

### 💻 Local Offline Models (Ollama)
Requires [Ollama](https://ollama.com/) running locally:
- `gemma4:31b` *(Default local model)*
- `qwen3.6:35b`

---

## 📂 Output Folder Structure

When processing a PDF, Chemstractor outputs a structured folder containing raw extractions, classified tables, and AI summaries:

```text
[Output Directory]/
└── 📂 [paper_name]/
    ├── 📂 extract/
    │   ├── 📄 clean_[filename].pdf      # Clean copy of original PDF
    │   ├── 📄 [filename].pdf            # Copy of source PDF
    │   ├── 📄 output.md                 # Raw document content parsed into Markdown
    │   ├── 📄 output_clean.md           # Cleaned document content parsed into Markdown
    │   ├── 📄 formulae.json             # Extracted chemical formulae
    │   ├── 📄 log_[filename].log        # Complete timing and parser logs
    │   └── 📂 tables/
    │       ├── 📂 csv/
    │       │   └── 📊 table1.csv        # Raw table data in CSV format
    │       └── 📂 txt/
    │           └── 📄 table1.txt        # Raw table content in formatted text
    │
    ├── 📂 categorisation/
    │   └── 📄 table1.json               # Table category tags (JSON)
    │
    ├── 📂 interpretation/
    │   ├── 📄 table1_flory.json         # Flory parameter interpretation (JSON)
    │   └── 📄 table1_mh.json            # Mark-Houwink parameter interpretation (JSON)
    │
    └── 📂 summary/
        ├── 📄 summary.json              # Paper metadata (Title, Authors, DOI)
        └── 📂 tables/
            └── 📄 table1.json           # Reaction condition summary per table (JSON)
```

---

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](file:///c:/Users/henry/Github/ChemistryExtract/LICENSE) file for details.

---


