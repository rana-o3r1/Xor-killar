import os
import time
from colorama import Fore, init
import sys
import webbrowser

# Colorama ইনিশিয়ালাইজ
init(autoreset=True)

# ASCII টেক্সট ব্যানার প্রদর্শন
def print_banner():
    print(Fore.CYAN + """
░█████╗░██████╗░██████╗░░░███╗░░
██╔══██╗╚════██╗██╔══██╗░████║░░
██║░░██║░█████╔╝██████╔╝██╔██║░░
██║░░██║░╚═══██╗██╔══██╗╚═╝██║░░
╚█████╔╝██████╔╝██║░░██║███████╗
░╚════╝░╚═════╝░╚═╝░░╚═╝╚══════╝
    """)
    print()  # নতুন লাইন

# XOR ডিক্রিপশন ফাংশন
def xor_decrypt(file_path, key, output_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        # XOR ডিক্রিপশন
        decrypted_data = bytes([b ^ (key % 256) for b in data])

        # ডিক্রিপ্টেড ফাইল আউটপুটে লিখুন
        with open(output_path, "wb") as f:
            f.write(decrypted_data)

        # সফল ডিক্রিপশন মেসেজ দুই লাইনে
        print()
        print()  # নতুন লাইন
        print(Fore.GREEN + f"Decrypted Successfully 🥳")
        print()
        print(Fore.GREEN + f"💾 Save To:→{output_path}")
        print()  # নতুন লাইন

    except Exception as e:
        print(Fore.RED + f"WTF A ERROR ❗: {e}")
        print()  # নতুন লাইন

# ইউজার থেকে XOR কী ইনপুট নিন
def get_key():
    while True:
        try:
            print(Fore.YELLOW + "🔑 Enter XOR key : ", end="")  # নতুন লাইনে প্রম্পট দেখান
            key = input().strip()  # ইনপুট নেওয়া
            if key.lower() == 'q':  # 'q' প্রেস করলে প্রোগ্রাম বন্ধ
                print(Fore.RED + "Script Closing...")
                exit()  # প্রোগ্রাম বন্ধ
            else:
                return int(key)  # কী রিটার্ন করুন
        except ValueError:
            print(Fore.RED + "Plz Enter a Valid Key ❗")
            print()  # নতুন লাইন

# ফাইল পাথ ইনপুট নিন এবং চেক করুন
def get_file_path():
    default_path = '/storage/emulated/0/MT2/apks/546875204F'  # ডিফল্ট পাথ
    while True:
        # ইউজারের জন্য পাথের প্রম্পট দেখানো
        print(Fore.YELLOW + f"📀 Enter Your Path: ", end="")  
        file_path = input().strip()  # ইনপুট নেওয়া
        print()  # নতুন লাইন
        
        if file_path.lower() == "q":  # ইউজার যদি 'q' টাইপ করে
            print(Fore.RED + "Script Closing...")
            exit()  # প্রোগ্রাম বন্ধ
        
        # যদি ইউজার পাথ না দেন, ডিফল্ট পাথ সেট করুন
        if not file_path:
            file_path = default_path  # ডিফল্ট পাথ

        # ফাইল পাথ চেক করা এবং এটি সঠিক কিনা
        if os.path.exists(file_path):
            # যদি এটি একটি ডিরেক্টরি হয়
            if os.path.isdir(file_path):
                print(Fore.RED + "⚠️Please Enter Full Path, Not Folder Name Only")
                print()  # নতুন লাইন
            else:
                return file_path  # সঠিক ফাইল পাথ দিলে রিটার্ন করুন
        else:
            print(Fore.RED + "❗ ENTER A VALID PATH")
            print()  # নতুন লাইন

# লোডিং এনিমেশন ফাংশন (এবার দ্রুত)
def loading_animation():
    print(Fore.YELLOW + "Loading...", end="\r")
    for _ in range(2):  # ১ সেকেন্ডের মধ্যে
        print(Fore.YELLOW + "Loading .", end="\r")
        time.sleep(0.3)  # সময় কমানো (0.3 সেকেন্ড)
        print(Fore.YELLOW + "Loading ..", end="\r")
        time.sleep(0.3)
        print(Fore.YELLOW + "Loading ...", end="\r")
        time.sleep(0.3)
    print(Fore.YELLOW + "Love From Rana Odri 💘")
    print("-" * 30)  # লম্বা লাইন
    print()  # নতুন লাইন
    print(Fore.GREEN + "Press q For exit") # দুটি নতুন লাইন
    print()  
    print(Fore.GREEN + "Press Enter For Default Path")
    print("-" * 30)  # আরেকটি লম্বা লাইন
    print()  # নতুন লাইন

# টার্মিনাল ক্লিয়ার করার ফাংশন
def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

# টেলিগ্রাম চ্যানেল লিংক ওপেন করা
def open_telegram_channel():
    # আপনার চ্যানেলের URL এখানে দিন
    telegram_link = "https://t.me/odri_modz"
    print(Fore.YELLOW + f"\n{telegram_link}")  # শুধুমাত্র লিংক প্রদর্শন
    webbrowser.open(telegram_link)  # লিংকটি ওপেন করা

def main():
    # টার্মিনাল ক্লিয়ার করা
    clear_terminal()

    # ASCII ব্যানার প্রদর্শন
    print_banner()

    # টেলিগ্রাম চ্যানেল লিংক প্রদর্শন
    open_telegram_channel()  # চ্যানেল লিংক দেখাবে এবং ওপেন করবে
    print()  # নতুন লাইন

    # লোডিং এনিমেশন দেখান
    loading_animation()
    
    # ইউজার থেকে ফাইল পাথ নেওয়া
    file_path = get_file_path()

    # ফাইল পাথ পাওয়া গেলে
    if file_path:
        # ইউজার থেকে XOR কী নেওয়া
        key = get_key()

        # আউটপুট পাথ যেখানে ডিক্রিপ্ট করা ফাইল সেভ হবে
        output_path = os.path.join(os.path.dirname(file_path), "decrypt.apk")

        # ডিক্রিপ্ট ফাংশন কল করা
        xor_decrypt(file_path, key, output_path)

if __name__ == "__main__":
    main()