# Car Price Prediction

Bu proje, otomobil özelliklerine dayalı olarak bir aracın fiyatını tahmin etmek için bir model ve Streamlit kullanıcı arayüzü içerir.

## Model Hakkında

- **Model Türü**: Regresyon
- **Kullanılan Algoritma**: Lineer Regresyon
- **Özellikler**:
  - Make (Marka)
  - Model
  - Trim
  - Mileage (Kilometre)
  - Type (Araç Tipi)
  - Cylinder (Silindir Sayısı)
  - Liter (Motor Hacmi)
  - Doors (Kapı Sayısı)
  - Cruise (Cruise Control - Hız Kontrolü)
  - Sound (Ses Sistemi)
  - Leather (Deri Döşeme)
- **Metrikler**:
  - Ortalama Kare Hata (Mean Squared Error - MSE)
  - R-kare (R² Score)

## Kurulum

1. Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

   ```
   pip install pandas scikit-learn streamlit
   ```

2. GitHub deposunu klonlayın:

   ```
   git clone https://github.com/osmantemel/Car-Prediction-streamlit-deploy.git
   ```

3. Projeyi çalıştırmak için:

   ```
   cd Car-Prediction-streamlit-deploy
   streamlit run app.py
   ```

## Kullanım

1. Streamlit uygulaması başladığında, arabaya ait özellikleri seçebilirsiniz.
2. "Tahmin" butonuna tıklayarak fiyat tahminini görebilirsiniz.

## Veri

Veri, araba özellikleri ve fiyatlarını içeren bir Excel dosyasından yüklenir.

## Katkılar

Her türlü katkı ve geri bildirim için açığız. Lütfen bir Issue açarak veya bir Pull Request göndererek katkıda bulunun.

Hugging Face adresi: [Car Price Prediction - Hugging Face](https://huggingface.co/spaces/osmanteme1/car_predictions)

Bu README dosyası, projenin genel yapısı ve kullanımı hakkında temel bilgiler sağlar. İhtiyacınıza göre güncelleyebilirsiniz.