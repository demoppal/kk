import os
import sys
import requests

# Pydroid ရဲ့ လုံခြုံတဲ့ Internal Path ထဲကို အရင်ဝင်မယ်
home = os.path.expanduser("~")
os.chdir(home)

# GitHub က ဖိုင်အသစ် (qq.pyc) ရဲ့ Link
URL_PYC = "https://raw.githubusercontent.com/demoppal/kk/main/qq.pyc"
# အရင်က တင်ထားတဲ့ qq.so ရဲ့ Link (Link အမှန်ကို ပြန်ထည့်ပေးပါ)
URL_SO = "https://raw.githubusercontent.com/demoppal/kk/main/qq.so"

def download_updates():
    # qq.pyc ကို အမြဲ update ဖြစ်အောင် အရင်ဖျက်ပြီး ပြန်ဒေါင်းတာ ပိုစိတ်ချရပါတယ်
    for file in ["qq.pyc", "qq.so"]:
        if not os.path.exists(file):
            print(f"[-] {file} ကို ရယူနေပါသည်...")
            r = requests.get(URL_PYC if ".pyc" in file else URL_SO)
            with open(file, "wb") as f:
                f.write(r.content)
    print("[+] ဖိုင်များ ပြည့်စုံပါပြီ။")

def start():
    download_updates()
    print("\n[*] Script စတင်နေပါပြီ...")
    print("=" * 20)
    
    try:
        if home not in sys.path:
            sys.path.append(home)
        
        # ဤနေရာတွင် qq.pyc ရော qq.so ကိုပါ Python က ရှာဖွေသွားပါလိမ့်မယ်
        import qq
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    start()
    
