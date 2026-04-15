import os
import sys
import requests

# Pydroid Internal Folder ထဲသွားမယ်
home = os.path.expanduser("~")
os.chdir(home)

# GitHub Links
# ဖိုင်နာမည်ကို GitHub ကအတိုင်း တိတိကျကျ ရေးထားပါတယ်
URL_PYC = "https://raw.githubusercontent.com/demoppal/kk/main/qq.cpython-313.pyc"
URL_SO = "https://raw.githubusercontent.com/demoppal/kk/main/qq.so"

def setup():
    # .pyc ဖိုင်ကို ဒေါင်းပြီး qq.pyc လို့ နာမည်ပြောင်းသိမ်းမယ်
    if not os.path.exists("qq.pyc"):
        print("[-] qq.pyc ကို ရယူနေပါသည်...")
        r = requests.get(URL_PYC)
        with open("qq.pyc", "wb") as f:
            f.write(r.content)
            
    # .so ဖိုင်ကို ဒေါင်းမယ်
    if not os.path.exists("qq.so"):
        print("[-] qq.so ကို ရယူနေပါသည်...")
        r = requests.get(URL_SO)
        if r.status_code == 200:
            with open("qq.so", "wb") as f:
                f.write(r.content)

def start():
    setup()
    print("[+] Files အားလုံး အဆင်သင့်ဖြစ်ပါပြီ။")
    print("[*] Script စတင်နေပါပြီ...\n" + "="*20)
    
    try:
        sys.path.append(home)
        import qq # qq.pyc ကို လှမ်းခေါ်ပါပြီ
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    start()
    
