# FileSignatureChecker
A Python tool to check file signatures against extensions.  
Helps detect suspicious or potentially malicious files by comparing actual file headers with their claimed extensions.

---

## Features

- Checks the file’s **extension** vs its **signature (magic bytes)**.  
- Warns if there is a **mismatch**.  
- Suggests scanning with [VirusTotal](https://www.virustotal.com) for suspicious files.  
- Reads signatures from an external **`signatures.json`**, making it easy to update.  
- Supports **50+ common file types** including exe, dll, pdf, jpg, png, docx, and more.  

---

## Installation / Usage

1. Clone the repository:

```bash
git clone https://github.com/muzzamilarain/FileSignatureChecker.git
cd SigGuard
pip install -r requirements.txt
python SigGuard.py /file_path
