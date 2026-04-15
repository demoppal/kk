import os
import sys
import requests

# ၁။ Pydroid ရဲ့ လုံခြုံတဲ့ Internal Folder ထဲသို့ အရင်သွားမယ်
home = os.path.expanduser("~")
os.chdir(home)

# ၂။ GitHub က ဖိုင်လမ်းကြောင်း
URL = "https://raw.githubusercontent.com/demoppal/kk/main/qq.pyc"
FILE = "qq.pyc"

def start():
    # ဖိုင်မရှိရင် ဒေါင်းမယ်
    if not os.path.exists(FILE):
        print("[-] File ကို GitHub မှ ရယူနေပါသည်...")
        r = requests.get(URL)
        with open(FILE, "wb") as f:
            f.write(r.content)
        print("[+] ဒေါင်းလုဒ် ပြီးပါပြီ။")

    # ၃။ Import လုပ်ပြီး Run မည့်အပိုင်း
    print("[*] Script စတင်နေပါပြီ...")
    print("-" * 20)
    
    try:
        # လက်ရှိ folder ထဲက qq.pyc ကို ရှာတွေ့အောင် path ထည့်ပေးခြင်း
        sys.path.append(home)
        
        # qq.pyc ကို ခေါ်သုံးခြင်း
        import qq
        
    except Exception as e:
        print(f"[!] Error တက်သွားသည်: {e}")

if __name__ == "__main__":
    start()
  
