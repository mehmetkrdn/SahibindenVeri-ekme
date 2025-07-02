import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import json
import time

veriler = []

def sayfayi_cek(sayfa):
    print(f"{sayfa}. sayfa çekiliyo")

    options = uc.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        driver = uc.Chrome(options=options)

        url = f"https://www.sahibinden.com/oto-tamir-servis-hizmetleri/istanbul?currentPageIndex={sayfa}"
        driver.get(url)
        time.sleep(10)  # sayfa yüklenmesi için bekleme süresi

        for i in range(1, 16):  # sayfada kaç ilanı alacağımız belirtir sırasıyla.
            try:
                anayol = f'//*[@id="profileSearchResults"]/a[{i}]'
                yerismi=driver.find_element(By.XPATH,f'{anayol}/div/div[1]/h3/span').text.strip()
                isim = driver.find_element(By.XPATH, f'{anayol}/div/div[3]/div[1]').text.strip()
                adres = driver.find_element(By.XPATH, f'{anayol}/div/div[3]/div[2]').text.strip()
                kategori = driver.find_element(By.XPATH, f'{anayol}/div/div[3]/div[3]').text.strip()
                link = driver.find_element(By.XPATH, anayol).get_attribute("href")

                veriler.append({
                    "yerismi":yerismi,
                    "isim": isim,
                    "adres": adres,
                    "kategori": kategori,
                    "link": link
                })

            except Exception as e:
                print(f"{sayfa}. sayfa {i}. ilanda hata oluştu:", e)
                continue

        driver.quit()

    except Exception as e:
        print(f"{sayfa}. sayfa genel hata:", e)

# sayfa aralığını belirtiriz
for sayfa in range(1, 51):
    sayfayi_cek(sayfa)

# JSONa kaydetme
with open("arabailan.json", "w", encoding="utf-8") as f:
    json.dump(veriler, f, ensure_ascii=False, indent=4)

print("\n Tüm sayfalar başarıyla çekildi. 'arabailannlar.json' dosyasına kaydedildi.")
