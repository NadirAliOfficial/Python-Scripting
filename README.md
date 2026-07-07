# Python Scripting Collection

A growing collection of Python utility scripts for automation, file processing, web scraping, and system tasks.

## Scripts

| Script | Description |
|--------|-------------|
| `CSV TO TEXT.py` | Convert CSV files to formatted plain text reports |
| `file_renamer.py` | Bulk rename files with regex patterns |
| `dir_cleaner.py` | Auto-organize downloads folder by file type |
| `site_monitor.py` | Monitor website uptime and alert on downtime |

## Usage

```bash
# CSV to text
python "CSV TO TEXT.py" input.csv output.txt

# Bulk rename
python file_renamer.py --dir ./photos --pattern "IMG_{n:04d}"

# Clean downloads
python dir_cleaner.py --dir ~/Downloads
```

## Requirements

```bash
pip install requests beautifulsoup4
```
