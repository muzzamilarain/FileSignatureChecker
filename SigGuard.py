import os
import sys
import json
from pyfiglet import figlet_format
from termcolor import colored

print(colored(figlet_format("SigGuard", font="slant"), "red"))
print(colored("file extensions can lie, but signatures don’t.... ... ...", "yellow"))
print(colored(figlet_format("By Muzzamil Arain", font="digital"),"red"))
print(colored("LinkedIn: muzzamil-sadiq-7195b2258\t \t Github: github.com/muzzamilarain\n" , "yellow"))


def get_file_signature(file_path, length=8):
    with open(file_path, "rb") as f:
        return f.read(length).hex().upper()

def check_file(file_path, signatures):
    ext = os.path.splitext(file_path)[1].lower().replace(".", "")
    sig = get_file_signature(file_path)

    matched_ext = None
    matched_extensions = []
    for extension, sig_list in signatures.items():
        for s in sig_list:
            if sig.startswith(s):
                matched_extensions.append(extension)

    
    if ext in matched_extensions:
        matched_ext = ext
    elif matched_extensions:
        matched_ext = matched_extensions[0]

    print(f"\n[+] File: {file_path}")
    print(f"    Extension : {ext if ext else 'None'}")
    print(f"    Signature : {sig}")
    print(f"    Detected  : {matched_ext if matched_ext else 'Unknown'}")

    if ext and matched_ext and ext != matched_ext:
        print("⚠️  Warning: Extension and signature do not match!")
        print("   → Please scan this file with VirusTotal or Anyother Platform You Like.\n")
    else:
        print("✅ File looks consistent.\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_signature.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open("signatures.json", "r") as f:
        signatures = json.load(f)

    if os.path.exists(file_path):
        check_file(file_path, signatures)
    else:
        print("❌ File does not exist. Please provide a valid path.")


