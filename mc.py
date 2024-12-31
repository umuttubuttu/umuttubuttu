import requests
import zipfile
import os
import warnings

def download_github_repo_zip(repo_url, destination):
    """
    Bir GitHub reposunu ZIP olarak indirir ve çıkartır.
    
    Args:
        repo_url (str): GitHub repo URL'si (örnek: https://github.com/kullanici_adi/proje_adi).
        destination (str): Depoyu kaydedeceğiniz dizin.
    """
    try:
        # SSL sertifikası doğrulamasını devre dışı bırakma uyarısını gizle
        warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

        # GitHub'ın zipball indirilebilir linki (main yerine master branch kullanılabilir)
        zip_url = repo_url.rstrip("/") + "/archive/refs/heads/master.zip"
        
        # SSL sertifikası doğrulamasını devre dışı bırak
        response = requests.get(zip_url, stream=True, verify=False)
        
        if response.status_code == 200:
            zip_path = os.path.join(destination, "repo.zip")
            os.makedirs(destination, exist_ok=True)
            
            # ZIP dosyasını kaydet
            with open(zip_path, "wb") as f:
                f.write(response.content)
            
            # ZIP dosyasını çıkart
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(destination)
            
            # Geçici ZIP dosyasını sil
            os.remove(zip_path)
            print(f"Repo başarıyla indirildi ve çıkartıldı: {destination}")
        else:
            print(f"Hata: Repo indirilemedi. HTTP {response.status_code}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Belirtilen URL ve konum
repo_url = "https://github.com/Eaglercraft1-8/Eaglercraft1-8.github.io"
destination = r"C:\Users\Ogrenci\Desktop"
download_github_repo_zip(repo_url, destination)

# Programın kapanmasını önlemek için bekleme
input("İşlem tamamlandı. Programı kapatmak için Enter tuşuna basın...")
