# 🎓 T3 Burs Platformu

T3 Vakfı tarafından geliştirilen Django tabanlı bir burs başvuru ve yönetim platformudur. Öğrenciler için kolay başvuru süreci, başarı hikayeleri ve topluluk yorumlarını bir araya getirir. Responsive tasarımı ve modern kullanıcı deneyimi ile her cihazda sorunsuz çalışır.

---

## 🧩 Özellikler

- ✅ **Burs Başvuru Formu**: Form alanları, resim yükleme ve yorum bölümü içerir.
- ✅ **Video Röportajlar**: YouTube embed destekli slider ile bursiyer videoları.
- ✅ **Başarı Hikayeleri**: Kullanıcıların hikayeleri, detay sayfası ile birlikte.
- ✅ **Yorumlar**: Kullanıcılar yorum yapabilir, yorumlar slider'da görüntülenir.
- ✅ **Haberler & Duyurular**: Güncel haberler ve tüm haberleri görüntüleme sayfası.
- ✅ **Responsive Tasarım**: Tüm cihazlarda mobil uyumlu kullanıcı arayüzü.
- ✅ **Modern UI/UX**: Tailwind CSS, gradyan geçişli ayraçlar ve kart bileşenleri.
- ✅ **Çok Dilli Destek**: `tr` ve `en` dillerinde çeviri destekli altyapı.
- ✅ **Yönetim Paneli**: Django Admin ile içerik kontrolü.
- ✅ **Swiper Slider**: Video, başarı hikayesi ve yorumlar için responsive slider.

---

## 🏗️ Kurulum

### 1. Reposu klonla

git clone https://github.com/kullanici-adi/t3-burs-platformu.git
cd t3-burs-platformu
### 2. Sanal ortam oluştur

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
###3. Gereksinimleri yükle

pip install -r requirements.txt
### 4. Migrasyonları çalıştır

python manage.py migrate
### 5. Statik dosyaları topla
python manage.py collectstatic --noinput
### 6. Geliştirme sunucusunu başlat

python manage.py runserver
### 🌐 Yayına Alma (Railway)
Railway üzerinde hızlıca canlıya almak için aşağıdaki ayarları kullanabilirsiniz:

### 🔧 Procfile
web: gunicorn burs_programi.wsgi:application
📦 requirements.txt içinde olması gerekenler
🎯 Railway Panel Ayarları
Start Command: gunicorn burs_programi.wsgi:application

Buildpacks: Nixpacks (Python detected)

Python versiyonu: 3.12

Ortam değişkenleri: DEBUG=False, ALLOWED_HOSTS=..., SECRET_KEY=..., DATABASE_URL=...

📁 Sayfa Yapısı
Sayfa	URL Örneği	Açıklama
Anasayfa	/	Hero alanı, burs programları, başarı hikayeleri, yorumlar
Başvuru Formu	/application/	Form ile kullanıcı başvurusu
Röportajlar	/testimonials/	Video slider, yorum bırakma formu
Burs Programları	/scholarship-programs/	Kartlar halinde tüm programlar
Hikaye Detayı	/story/<slug>/	Başarı hikayesi detayları
Haber Detayı	/news/<slug>/	Tekil haber görüntüleme
Yönetim Paneli	/admin/	Django admin

### 🖼️ Kullanılan Teknolojiler
Python 3.12
Django
Tailwind CSS
Swiper.js
Gunicorn
Whitenoise
PostgreSQL (Canlıda)
SQLite (Geliştirme ortamında)

### ⚙️ Geliştirici Komutları
Çeviri dosyaları oluştur:

django-admin makemessages -l tr
django-admin makemessages -l en
django-admin compilemessages
### Süper kullanıcı oluştur:

python manage.py createsuperuser
