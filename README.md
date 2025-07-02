# Sahibinden.com Veri Çekme

Bu proje, [sahibinden.com](https://www.sahibinden.com) üzerindeki **"İstanbul oto tamir & servis hizmetleri"** kategorisinden ilanları otomatik olarak toplar ve bu ilanları bir JSON dosyasına kaydeder. İsteğe bağlı değiştirebilirsiniz

## 🧰 Kullanılan Teknolojiler

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- [undetected_chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
- JSON

## 📦 Özellikler

- Sahibinden.com üzerindeki her sayfa için yeni bir tarayıcı başlatılır (robot engelini aşmak için).
- Her sayfadaki 15 ilanın:
  - Yer adı (başlık)
  - Firma ismi
  - Adresi
  - Kategorisi
  - İlan linki
- Bilgiler json dosyasında saklanır

## ▶️ Nasıl Kullanılır?


### 1. Gerekli Kurulumlar

```bash
pip install selenium undetected-chromedriver
python scrape_sahibinden.py

