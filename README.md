# HR Recruitment and Management System

Terminal üzerinden çalışan, basit bir İK (İnsan Kaynakları) aday eleme simülasyonu. Aday bilgilerine (yetenek, mezuniyet yılı, deneyim veya GPA) göre uygun açık pozisyonlarla eşleştirme yapar.

## Özellikler

- Aday adı, ana yetenek (`python`, `al`, `data`, `any`), mezuniyet yılı girişi
- Mezuniyetten **1 yıldan fazla** süre geçmişse: profesyonel deneyim (ay) bazlı eşleştirme
- Mezuniyetten **1 yıl veya daha az** süre geçmişse: GPA bazlı giriş seviyesi / staj pozisyonu eşleştirme
- Uygun pozisyon yoksa alternatif açık pozisyonları listeleme
- Bir pozisyon doldurulduğunda otomatik olarak kapatma (aynı oturumda tekrar dolmuş gösterilir)
- Hatalı/boş girişlerde kullanıcıyı tekrar yönlendirme, `exit` ile her adımda çıkış

## Gereksinimler

- Python 3.x (ek bir kütüphane gerekmiyor, yalnızca standart kütüphane kullanılıyor)

## Kurulum

```bash
git clone https://github.com/<kullanici-adin>/<repo-adin>.git
cd <repo-adin>
```

## Kullanım

```bash
python hr_management_system.py
```

Çalıştırdığında sırasıyla şunlar istenir:

1. Ad
2. Ana yetenek (`python`, `al`, `data`, `any`)
3. Mezuniyet yılı
4. Duruma göre: profesyonel deneyim (ay) **veya** GPA (`sistem/puan` formatında, örn. `4/3.7`)

Herhangi bir adımda `exit` yazarak programdan çıkabilirsin.

## Proje Yapısı

```
.
├── hr_management_system.py
└── README.md
```

## Notlar

- `jobs` listesi kod içinde sabit (hardcoded) tanımlıdır; gerçek bir veritabanı veya dosya kullanılmaz.
- Program her çalıştırıldığında pozisyon doluluk durumu sıfırlanır (bellek içi state).

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır. (İstersen GitHub repo oluştururken otomatik MIT lisansı ekleyebilirsin.)
