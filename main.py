import os
import shutil
import psutil
import time
#C:\\Program Files (x86)\\Steam\\
dosyalar = [r"C:\\Program Files (x86)\\Steam\\steamapps\\libraryfolders.vdf"]
klasorler = [r"C:\\Program Files (x86)\\Steam\\userdata",r"C:\\Program Files (x86)\\Steam\\package",r"C:\\Program Files (x86)\\Steam\\logs",r"C:\\Program Files (x86)\\Steam\\depotcache",r"C:\\Program Files (x86)\\Steam\\config",r"C:\\Program Files (x86)\\Steam\\appcache"]
dosyayayakindosyalar = [r"C:\\Program Files (x86)\\Steam\\steamapps"]

def steamkapat():
    for process in psutil.process_iter(["name"]):
        if process.info["name"] == "steam.exe":
            process.terminate()
            process.wait()
            print("steam başarıyla kapatıldı")
            time.sleep(5)
        else:
            pass

def dosyatemizle():
    for dosya in dosyalar:
        if os.path.exists(dosya):
            os.remove(dosya)
            print(f"{dosya} Bulundu ve temizlendi")
        else:
            print(f"{dosya} Zaten temizlenmiş")

def dosyayakintemizle():
    for klasor in dosyayayakindosyalar:
        if os.path.exists(klasor):
            for dosyayayakindosya in os.listdir(klasor):
                if dosyayayakindosya.startswith("appmanifest"):
                    print(f"{dosyayayakindosya} Bulundu ve temizlendi")
        else:
            print(f"{klasor} Bulunamadı")

def klasortemizle():
    for klasor in klasorler:
        if os.path.exists(klasor):
            shutil.rmtree(klasor)
            print(f"{klasor} Bulundu ve temizlendi")
        else:
            print(f"{klasor} Zaten temizlenmiş")    

def steamac():
    os.startfile(r"C:\\Program Files (x86)\\Steam\\steam.exe")

def main():
    steamkapat()
    dosyatemizle()
    dosyayakintemizle()
    klasortemizle()
    time.sleep(3)
    steamac()

main()
