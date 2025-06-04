# Incident Response and Forensics Automation Scripts

This repository contains scripts to automate common Incident Response and Forensics tasks.

## Folder Structure

- **log_parsers/** Python scripts to extract Indicators of Compromise (IPs, URLs, hashes) from log files.
- **artifact_extraction/** Scripts (Python) to pull strings, compute hashes, and extract metadata from binaries.
- **memory_dumps/** Shell and PowerShell scripts to automate memory and process collection on Linux/Windows.

---

## Usage

### 1. Extract IP Addresses from a Single Log File

**Script:** log_parsers/extract_ips.py

This Python script scans a given log file, finds all IPv4 addresses via regex, deduplicates them, sorts them, and prints each unique IP on its own line.

#### 1.1 Make sure the script is executable

```bash
chmod +x log_parsers/extract_ips.py
```

#### 1.2 Run the script against your log

```bash
./log_parsers/extract_ips.py /path/to/your/logfile.log
```

* **Argument**: path to a single log file (plain‐text or mixed content).
* **Output**: a sorted list of unique IPv4 addresses found in that file.

#### 1.3 Example

1. **Example input file** (`log_parsers/sample.log`):

```text
2025-06-04 12:00:01 Connection attempt from 10.10.11.14
2025-06-04 12:00:05 Connection attempt from 10.10.11.31
2025-06-04 12:05:17 Failed login from 10.10.11.14
2025-06-04 12:10:02 Connection from 1.10.11.71
2025-06-04 12:12:40 Access granted to 10.20.14.41
2025-06-04 12:15:00 Connection attempt from 10.10.11.51
2025-06-04 12:20:33 Connection attempt from 10.10.13.144
2025-06-04 12:25:11 Connection attempt from 10.103.141.141
2025-06-04 12:30:02 Connection attempt from 10.14.101.11
2025-06-04 12:35:17 Connection attempt from 10.144.11.11
2025-06-04 12:40:05 Connection attempt from 10.15.101.11
2025-06-04 12:45:00 Connection attempt from 10.15.11.61
2025-06-04 12:50:33 Connection attempt from 10.20.13.11
2025-06-04 12:55:17 Connection attempt from 10.50.11.141
2025-06-04 13:00:01 Connection attempt from 120.10.11.11
```

2. **Run the script**:

```bash
./log_parsers/extract_ips.py log_parsers/sample.log
```

3. **Example output** (printed to stdout):

```text
1.10.11.71
10.10.11.14
10.10.11.31
10.10.11.51
10.10.13.144
10.103.141.141
10.14.101.11
10.144.11.11
10.15.101.11
10.15.11.61
10.20.13.11
10.20.14.41
10.50.11.141
120.10.11.11
```

## Next Steps

1. **Recursive Extraction (TIP):** To process multiple logs in a folder, you can wrap this call in a loop or use `find` + `xargs`, for example:

```bash
find /path/to/logs -type f -name '*.log' -print0 \
| xargs -0 -n1 ./log_parsers/extract_ips.py \
> all_unique_ips.txt
```

2. Explore other folders to see scripts for binary artifact extraction (`artifact_extraction/`) and memory‐dump collection (`memory_dumps/`).

*Feel free to open issues or contribute improvements via pull requests.*