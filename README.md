---

# Sri Lanka Exporters Directory Scraper

This project is a Python-based web scraper designed to extract exporter information from the [Sri Lanka Business Exporters Directory](https://www.srilankabusiness.com/exporters-directory/). The scraped data is saved in CSV format, organized by the type of exporters.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Project Overview

The `Sri Lanka Exporters Directory Scraper` fetches and parses web pages from the Exporters Directory, collecting exporter names across multiple pages. The exporter names are saved in separate CSV files, based on their directory categories. The script is modular, allowing additional URLs and page numbers to be easily added to the scraping pipeline.

## Features

- Automated extraction of exporter information.
- Organized storage of data in category-specific CSV files.
- Error handling for failed page requests.
- Clean and reusable codebase with dependency management.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anush47/exporters-extract-srilanka.git
   cd exporters-extract-srilanka
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   venv/Scripts/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add additional URLs and page numbers** *(optional)*:
   - Open `main.py` and add more entries to the `urls_and_pages` dictionary:
     ```python
     urls_and_pages = {
         "https://www.srilankabusiness.com/exporters-directory/apparel-exporters-in-sri-lanka": 14,
         # Add more URLs and their page counts here
     }
     ```

## Usage

To start scraping, simply run `main.py`:
```bash
python main.py
```

### Output
- Each category of exporters is saved in a separate CSV file located in the `exporters` directory.
- The CSV files are named after the last segment of the category URL (e.g., `apparel-exporters-in-sri-lanka.csv`).

## Project Structure

```plaintext
exporters-extract-srilanka/
├── exporters/                # Output directory for CSV files (ignored by Git)
├── main.py                   # Main script for scraping and saving exporter data
├── requirements.txt          # Project dependencies
└── .gitignore                # Git ignore file for excluding unnecessary files
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
