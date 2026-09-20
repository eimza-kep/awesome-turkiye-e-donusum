# Awesome Türkiye E-Dönüşüm 🇹🇷⚡

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Lisans: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Portal](https://img.shields.io/badge/Rehber-E--%C4%B0mza%20Blog-22c55e.svg)](https://eimza-kep.github.io/eimza-blog/)

> Türkiye'deki **E-İmza**, **Mali Mühür**, **KEP (Kayıtlı Elektronik Posta)**, **e-Fatura**, **e-Defter**, **e-İrsaliye**, **e-SMM**, **UYAP**, **GİB** ve **e-Devlet** ekosistemi için derlenmiş açık kaynaklı kütüphaneler, resmi standartlar, sürücüler, araçlar, komut satırı hileleri (cheat sheet) ve teknik çözüm rehberleri listesi.

---

## 📑 İçindekiler

- [🏛️ Yasal Çerçeve, Kanunlar ve Resmi Kurumlar](#️-yasal-çerçeve-kanunlar-ve-resmi-kurumlar)
- [🔑 Yetkili Sertifika Sağlayıcıları (ESHS) ve KEP Operatörleri](#-yetkili-sertifika-sağlayıcıları-eshs-ve-kep-operatörleri)
- [🛠️ Açık Kaynak E-Dönüşüm Araçları (CLI & Scriptler)](#️-açık-kaynak-e-dönüşüm-araçları-cli--scriptler)
- [💻 Kütüphaneler, SDK'lar ve Geliştirici Paketleri](#-kütüphaneler-sdklar-ve-geliştirici-paketleri)
  - [Java](#java)
  - [Python](#python)
  - [.NET / C#](#net--c)
  - [Node.js / TypeScript](#nodejs--typescript)
  - [Go & Rust](#go--rust)
  - [C / C++](#c--c)
- [📜 Standartlar, İmzalar ve Kriptografik Protokoller](#-standartlar-imzalar-ve-kriptografik-protokoller)
- [🧾 GİB E-Belge Standartları ve UBL-TR](#-gib-e-belge-standartları-ve-ubl-tr)
- [⚖️ Hukuk Teknolojileri (LegalTech) ve UYAP Ekosistemi](#️-hukuk-teknolojileri-legaltech-ve-uyap-ekosistemi)
- [📱 Mobil İmza (m-İmza) ve Çipli Kimlik Kartı](#-mobil-imza-m-imza-ve-çipli-kimlik-kartı)
- [🔐 Donanım, Akıllı Kartlar ve Çip Teknolojisi](#-donanım-akıllı-kartlar-ve-çip-teknolojisi)
- [🌐 Tematik Bilgi Portalları ve Başvuru Ağları](#-tematik-bilgi-portalları-ve-başvuru-ağları)
- [💡 Geliştirici Hızlı Başvuru Kılavuzu (Cheat Sheet)](#-geliştirici-hızlı-başvuru-kılavuzu-cheat-sheet)
- [❓ Sık Karşılaşılan Hatalar ve Hızlı Çözümler](#-sık-karşılaşılan-hatalar-ve-hızlı-çözümler)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)
- [⚖️ Lisans](#-lisans)

---

## 🏛️ Yasal Çerçeve, Kanunlar ve Resmi Kurumlar

Türkiye'de dijital dönüşümün ve elektronik delil hukukunun temelini oluşturan mevzuatlar ve kamu otoriteleri:

* **[5070 Sayılı Elektronik İmza Kanunu](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=5070&MevzuatTur=1&MevzuatTertip=5):** Güvenli elektronik imzanın ıslak imza ile aynı hukuki sonuçları doğuracağını hükme bağlayan temel kanun.
* **[Türk Ticaret Kanunu (TTK) Madde 18/3](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6102&MevzuatTur=1&MevzuatTertip=5):** Tacirler arası fesih, temerrüt ve sözleşmeden dönme ihtarlarının noter veya KEP ile yapılması zorunluluğu.
* **[7201 Sayılı Tebligat Kanunu (Madde 7/a)](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=7201&MevzuatTur=1&MevzuatTertip=5):** Anonim, limited ve komandit şirketlere tebligatların elektronik yolla yapılmasını zorunlu kılan hükümler.
* **[Vergi Usul Kanunu 509 Sıra No.lu Genel Tebliği](https://www.gib.gov.tr/):** e-Fatura, e-Arşiv, e-İrsaliye, e-Defter, e-SMM ve e-Müstahsil düzenleme zorunlulukları ve ciro limitleri.
* **[Bilgi Teknolojileri ve İletişim Kurumu (BTK)](https://www.btk.gov.tr/):** ESHS ve KEP hizmet sağlayıcılarını yetkilendiren, denetleyen ve standartları belirleyen düzenleyici kurum.
* **[Gelir İdaresi Başkanlığı (GİB) e-Belge Portalı](https://ebelge.gib.gov.tr/):** Fatura şemaları, UBL-TR paketleri ve e-defter duyurularının ana merkezi.
* **[TÜBİTAK BİLGEM Kamu SM](https://kamusm.bilgem.tubitak.gov.tr/):** Türkiye'nin ulusal kök sertifika otoritesi ve Mali Mühür sağlayıcısı.
* **[Adalet Bakanlığı UYAP Bilişim Sistemi](https://uyap.gov.tr/):** Mahkemeler, avukatlar ve icra daireleri arasındaki yargı ağı altyapısı.
* **[Ticaret Bakanlığı MERSİS Portalı](https://mersis.ticaret.gov.tr/):** Merkezi Sicil Kayıt Sistemi; şirket kuruluş ve tescil işlemlerinin e-imzalı merkezi.
* **[Kamu İhale Kurumu (EKAP)](https://ekap.kik.gov.tr/):** Devlet ihalelerinde e-teklif hazırlama ve şifreli teklif paketi imzalama sistemi.

---

## 🔑 Yetkili Sertifika Sağlayıcıları (ESHS) ve KEP Operatörleri

BTK tarafından 5070 sayılı Kanun kapsamında yetkilendirilmiş resmi sağlayıcılar:

* **[TÜBİTAK Kamu SM](https://kamusm.bilgem.tubitak.gov.tr/):** Kamu kurumları personeli e-imzaları ve tüzel şirketlerin yasal Mali Mührü.
* **[TÜRKTRUST](https://www.turktrust.com.tr/):** Nitelikli elektronik sertifika (NES), zaman damgası ve SSL/TLS sağlayıcısı.
* **[E-Güven](https://www.e-guven.com/):** Türkiye'nin ilk özel elektronik sertifika hizmet sağlayıcısı.
* **[E-Tuğra](https://www.e-tugra.com.tr/):** E-İmza, zaman damgası, SSL ve kurumsal e-dönüşüm çözümleri.
* **[PTT KEP](https://www.ptt.gov.tr/):** Posta ve Telgraf Teşkilatı'nın resmi Kayıtlı Elektronik Posta altyapısı.
* **[TN KEP / TN Bilişim](https://www.tnkep.com.tr/):** Yetkili KEP operatörü ve güvenli veri saklama hizmetleri.
* **[TÜRKKEP](https://turkkep.com.tr/):** KEP operatörlüğü, e-Yazışma ve e-Saklama hizmetleri.

---

## 🛠️ Açık Kaynak E-Dönüşüm Araçları (CLI & Scriptler)

Geliştiriciler, mali müşavirler, avukatlar ve KOBİ'ler için açık kaynak GitHub projelerimiz ve kurumsal web scriptleri:

### 🛠️ E-Dönüşüm Sistem ve Masaüstü Araçları
* 🔧 **[gib-java-guvenlik-cozucu](https://github.com/eimza-kep/gib-java-guvenlik-cozucu):** GİB e-Beyanname, e-Fatura ve UYAP'taki Java "Application Blocked" ve sertifika istisna engellerini tek tıkla çözen PowerShell scripti.
* ⏱️ **[mali-muhur-eimza-suresi-kontrol](https://github.com/eimza-kep/mali-muhur-eimza-suresi-kontrol):** Bilgisayara takılı akıllı kart veya token cihazındaki sertifikanın bitiş süresini tarayıp kalan gün sayısını ve kriz uyarılarını raporlayan araç.
* 🩺 **[akilli-kart-surucu-teshis](https://github.com/eimza-kep/akilli-kart-surucu-teshis):** Windows 10/11'de "Akıllı kart tanınmıyor" hatasını teşhis eden, Akıllı Kart (Smart Card) servisini onaran ve AKİS/SafeNet sürücü durumunu inceleyen tanı asistanı.
* 📄 **[python-pdf-eimza-dogrulayici](https://github.com/eimza-kep/python-pdf-eimza-dogrulayici):** ETSI PAdES-BES ve B-LTV standartlarında imzalanmış PDF belgelerini sıfır harici kütüphane bağımlılığıyla ayrıştıran, sertifika geçerliliğini ve özet (hash) bütünlüğünü doğrulayan Python CLI aracı.
* ⚖️ **[uyap-editor-hizli-onarim](https://github.com/eimza-kep/uyap-editor-hizli-onarim):** Avukatlar için UYAP UDF Doküman Editörü açılmama, donma, Java bellek aşımı (`-Xmx1024m`) ve ekran ölçekleme sorunlarını gideren onarım yardımcısı.
* 📬 **[kep-adresi-dogrulayici](https://github.com/eimza-kep/kep-adresi-dogrulayici):** RFC 5322 ve BTK standartlarına göre `hs01.kep.tr`, `hs02.kep.tr`, `hs03.kep.tr` uzantılı KEP e-posta adreslerinin sözdizimini ve yetkili operatör eşleşmesini doğrulayan Python modülü.
* 🧾 **[e-fatura-xml-goruntuleyici](https://github.com/eimza-kep/e-fatura-xml-goruntuleyici):** GİB UBL-TR 1.2 formatındaki e-Fatura, e-Arşiv ve e-İrsaliye XML dosyalarını XSLT şablonuyla dönüştürüp yerel tarayıcıda görselleştiren CLI aracı.
* 🔓 **[eimza-pin-bloke-asistani](https://github.com/eimza-kep/eimza-pin-bloke-asistani):** 3 kez yanlış girilerek kilitlenen USB token PIN kodunu PUK kullanarak güvenle sıfırlamaya rehberlik eden terminal arayüzü.
* 📊 **[gib-edefter-berat-xml-dogrulayici](https://github.com/eimza-kep/gib-edefter-berat-xml-dogrulayici):** e-Defter Yevmiye, Kebir ve Berat XML dosyalarının GİB şema (XSD) geçerliliğini, özet değerlerini ve Mali Mühür imza bloğunu denetleyen Python aracı.

### 🌐 Hızlı Kurulan Kurumsal Web Scriptleri (Zero-Dependency Web Apps)
* 🛡️ **[kurumsal-kvkk-basvuru-scripti](https://github.com/eimza-kep/kurumsal-kvkk-basvuru-scripti):** 6698 Sayılı KVKK İlgili Kişi (Veri Sahibi) Başvuru Formu, 30 günlük yasal süre takip paneli ve hafif çerez izin barı scripti.
* 💼 **[kobi-hizli-teklif-scripti](https://github.com/eimza-kep/kobi-hizli-teklif-scripti):** KOBİ ve B2B firmalar için 1 dakikada kurulan fiyat teklifi talep scripti, dinamik sepet/KDV hesaplayıcı, yazdırılabilir proforma ve WhatsApp entegrasyonu.
* ⚖️ **[avukat-muvekkil-on-kayit-scripti](https://github.com/eimza-kep/avukat-muvekkil-on-kayit-scripti):** Avukatlar ve hukuk büroları için müvekkil ön görüşme, dosya kabul ve Avukatlık Kanunu Md. 38 çıkar çatışması (conflict check) portalı.
* 📊 **[muhasebe-mukellef-evrak-scripti](https://github.com/eimza-kep/muhasebe-mukellef-evrak-scripti):** SMMM ve mali müşavirler için ay sonu mükellef fatura/fiş/ekstre toplama portalı, teslim tutanağı üretici ve WhatsApp hatırlatıcı.
* 👥 **[kurumsal-ik-is-basvuru-scripti](https://github.com/eimza-kep/kurumsal-ik-is-basvuru-scripti):** Kurumsal İK ve Kariyer İş Başvuru Formu, KVKK açık rıza onaylı CV yükleme ve aday yönetim paneli.
* 📑 **[e-fatura-itiraz-ve-iade-scripti](https://github.com/eimza-kep/e-fatura-itiraz-ve-iade-scripti):** TTK Md. 18/3 uyarınca 8 günlük yasal itiraz süresi takip, e-Fatura iade ve itiraz tutanağı portalı.
* ⚖️ **[avukat-arabuluculuk-basvuru-scripti](https://github.com/eimza-kep/avukat-arabuluculuk-basvuru-scripti):** 6325 sayılı Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu uyumlu dava şartı ve ihtiyari arabuluculuk başvuru portalı.
* 🔧 **[kobi-servis-ariza-takip-scripti](https://github.com/eimza-kep/kobi-servis-ariza-takip-scripti):** KOBİ ve teknik servisler için cihaz arıza kayıt, otomatik SERV-XXXX takip kodu ve online durum sorgulama scripti.
* 📦 **[smmm-stok-sayim-tutanak-scripti](https://github.com/eimza-kep/smmm-stok-sayim-tutanak-scripti):** VUK Md. 227 & 186 uyarınca dönem sonu / fiili stok sayım, fire ve envanter tutanağı düzenleme scripti.
* 📋 **[kurumsal-isg-ziyaretci-kayit-scripti](https://github.com/eimza-kep/kurumsal-isg-ziyaretci-kayit-scripti):** 6331 sayılı İSG Kanunu uyumlu şirket lobi/tesis ziyaretçi kabul, acil durum tahliye listesi ve ziyaretçi takip scripti.
* 🤝 **[kobi-tedarikci-teklif-toplama-scripti](https://github.com/eimza-kep/kobi-tedarikci-teklif-toplama-scripti):** KOBİ'ler için satın alma talep açma, tedarikçi teklif toplama ve karşılaştırmalı matris değerlendirme scripti.
* ⭐ **[kobi-musteri-memnuniyet-nps-scripti](https://github.com/eimza-kep/kobi-musteri-memnuniyet-nps-scripti):** KOBİ'ler için 0-10 NPS ve CSAT müşteri memnuniyet anketi, anlık skor hesaplama ve şikayet yönetim scripti.
* 🏠 **[kira-tahliye-ve-sozlesme-scripti](https://github.com/eimza-kep/kira-tahliye-ve-sozlesme-scripti):** TBK Md. 352 uyumlu tahliye taahhütnamesi hazırlama, kira sözleşmesi ve TÜFE yasal artış hesaplayıcı scripti.
* 🏢 **[kurumsal-bayi-basvuru-scripti](https://github.com/eimza-kep/kurumsal-bayi-basvuru-scripti):** Üretici ve toptancılar için kurumsal bayi / franchise ön başvuru, teminat-ciro değerlendirme ve onay scripti.

### 📚 Bilgi Bankaları, AI Portalleri ve Excel Kütüphaneleri
* 🤖 **[turkiye-yapay-zeka-araclari](https://github.com/eimza-kep/turkiye-yapay-zeka-araclari):** Mali müşavirler, avukatlar ve KOBİ'ler için 20 yapay zeka aracı ve BYOK web portali (OpenAI & Google Gemini destekli, sıfır bağımlılık, yerel web arayüzü).
* 📚 **[e-donusum-rehberleri](https://github.com/eimza-kep/e-donusum-rehberleri):** Türkiye E-Dönüşüm ekosistemi için 20 adet kapsamlı, adım adım teknik rehber ve arıza çözüm kılavuzu.
* 📊 **[muhasebe-excel-sablonlari](https://github.com/eimza-kep/muhasebe-excel-sablonlari):** SMMM ve mali müşavirler için 7 adet tam formüllü Excel hesaplama ve denetim aracı (KDV tevkifat, amortisman, kıdem-ihbar, örtülü sermaye vb.).
* ⚖️ **[avukat-hukuk-excel-hesaplamalari](https://github.com/eimza-kep/avukat-hukuk-excel-hesaplamalari):** Avukatlar ve hukuk büroları için 7 adet dinamik Excel hesaplama aracı (vekalet ücreti, harç-masraf, yasal/avans faiz, işçilik alacakları vb.).
* 🏢 **[kobi-finans-yonetim-excel-sablonlari](https://github.com/eimza-kep/kobi-finans-yonetim-excel-sablonlari):** KOBİ ve işletmeler için 6 adet profesyonel finansal planlama ve nakit akış Excel şablonu (13 haftalık nakit akışı, başabaş analizi vb.).
* ⚡ **[awesome-turkiye-e-donusum](https://github.com/eimza-kep/awesome-turkiye-e-donusum):** Türkiye E-Dönüşüm ekosistemi açık kaynak projeleri, mevzuatları ve kaynaklarının güncel ana fihristi.

---

## 💻 Kütüphaneler, SDK'lar ve Geliştirici Paketleri

### Java
* **[TÜBİTAK Kamu SM MA3 API](https://kamusm.bilgem.tubitak.gov.tr/urunler/yazilim/ma3api/):** Türkiye'nin resmi CAdES, PAdES, XAdES e-imza, doğrulama ve zaman damgası kütüphanesi.
* **[OpenSC Java PKCS11 Provider](https://github.com/OpenSC/OpenSC):** Standart SunPKCS11 sağlayıcısı ile akıllı kart yönetimi.
* **[Apache Santuario (xmlsec)](https://santuario.apache.org/):** XML Digital Signature (XMLDSig/XAdES) standart uygulaması.
* **[Bouncy Castle Java](https://www.bouncycastle.org/java.html):** ASN.1 ayrıştırma, X.509 sertifika yönetimi ve kriptografik ilkel işlemler.

### Python
* **[pyHanko](https://github.com/MatthiasValvekens/pyHanko):** Python ile PAdES, CAdES, LTV ve RFC 3161 zaman damgalı PDF imzalama/doğrulama kütüphanesi.
* **[python-pkcs11](https://github.com/danni/python-pkcs11):** Akıllı kart donanımları ve HSM'ler için PKCS#11 API Python sarmalayıcısı.
* **[cryptography](https://cryptography.io/):** Python ekosisteminin en popüler kriptografi kütüphanesi (X.509, RSA, ECC).
* **[signxml](https://github.com/kislyuk/signxml):** Python için W3C XML Signature ve XAdES imzalama/doğrulama paketi.

### .NET / C#
* **[BouncyCastle.Cryptography](https://www.nuget.org/packages/BouncyCastle.Cryptography/):** C# ile gelişmiş CMS/PKCS#7 ve X.509 imzalama.
* **[PCSC-Sharp](https://github.com/danm-de/pcsc-sharp):** .NET uygulamaları için Windows PC/SC akıllı kart okuyucu kütüphanesi.
* **[Pkcs11Interop](https://github.com/Pkcs11Interop/Pkcs11Interop):** C# ile unmanaged PKCS#11 DLL'lerini çağıran endüstri standardı sarmalayıcı.

### Node.js / TypeScript
* **[node-pcsclite](https://github.com/pokusew/node-pcsclite):** PC/SC akıllı kart okuyucuları için Node.js bindings.
* **[node-webcrypto-p11](https://github.com/PeculiarVentures/node-webcrypto-p11):** PKCS#11 token cihazlarını WebCrypto API standardıyla kullanma arayüzü.
* **[xml-crypto](https://github.com/node-saml/xml-crypto):** Node.js için saf XML imzalama motoru.

### Go & Rust
* **[pkcs11 (Go)](https://github.com/miekg/pkcs11):** Go dili için PKCS#11 API arayüzü.
* **[cryptoki (Rust)](https://github.com/parallaxsecond/rust-cryptoki):** Rust dili için güvenli ve modern PKCS#11 sarmalayıcısı.

### C / C++
* **[OpenSC](https://github.com/OpenSC/OpenSC):** Akıllı kartlar için açık kaynaklı sürücü, PKCS#11 ve mini-driver altyapısı.
* **[PCSC-Lite](https://pcsclite.apdu.org/):** Unix/Linux işletim sistemlerinde akıllı kart okuyucuları çalıştırmak için PC/SC ara katmanı.

---

## 📜 Standartlar, İmzalar ve Kriptografik Protokoller

Türkiye'de ve uluslararası arenada kullanılan temel e-imza formatları ve kriptografik standartlar:

| Format / Standart | Açıklama | Türkiye'deki Kullanım Alanı |
|---|---|---|
| **CAdES (CMS Advanced Electronic Signatures)** | ETSI TS 101 733 standardı; ikili (binary) verileri PKCS#7 formatında imzalar. | Ham veri, e-posta, metin dosyaları, bankacılık talimatları. |
| **PAdES (PDF Advanced Electronic Signatures)** | ETSI TS 102 778 standardı; doğrudan PDF içine gömülü görsel ve dijital imza. | Sözleşmeler, mahkeme dilekçeleri, kurum içi resmi yazışmalar. |
| **XAdES (XML Advanced Electronic Signatures)** | ETSI TS 101 903 standardı; XML dokümanlarını yapısal olarak imzalar. | e-Fatura, e-İrsaliye, e-Defter, e-Arşiv, e-SMM. |
| **RFC 3161 Zaman Damgası** | Yetkili bir zaman sunucusundan atomik saate dayalı zaman kanıtı alma. | KEP iletileri, e-Defter beratları, uzun vadeli arşivleme. |
| **PKCS#11** | Kriptografik donanım ve akıllı kartlarla konuşma API standardı. | USB Token'lar, HSM cihazları, AKİS sürücüsü. |
| **PC/SC (Personal Computer/Smart Card)** | İşletim sistemlerinin akıllı kart okuyucularla haberleşme standardı. | Windows Smart Card Service, Linux `pcscd`. |
| **PAdES-LTV (Long Term Validation)** | İmza sertifikası süresi dolsa dahi imzanın geçerliliğini koruyan mimari. | Yasal arşiv zorunluluğu olan 10-20 yıllık resmi sözleşmeler. |

---

## 🧾 GİB E-Belge Standartları ve UBL-TR

Gelir İdaresi Başkanlığı tarafından yayımlanan UBL-TR 1.2 veri modeli standartları:

* **UBL-TR 1.2 Şeması:** OASIS Universal Business Language tabanlı fatura ve irsaliye XML şeması (`Invoice.xsd`, `DespatchAdvice.xsd`).
* **XSLT Görüntüleme Şablonları:** XML verisinin görsel faturaya dönüştürülmesini sağlayan stil sayfaları.
* **GİB İmza Profili:** Fatura üzerindeki `<ds:Signature>` düğümünün `XAdES-EPES` formatında oluşturulması zorunluluğu.
* **e-İrsaliye Karekod (QR Kod):** 24 karakterlik belge numarası, düzenleme tarihi ve saatini içeren güvenlik dizesi.
* **e-Defter Şemaları:** `Yevmiye.xsd`, `Kebir.xsd` ve bunlara ait `Berat.xsd` XML yapıları.

---

## ⚖️ Hukuk Teknolojileri (LegalTech) ve UYAP Ekosistemi

Adalet Bakanlığı ve Türkiye Barolar Birliği bilişim sistemleri:

* **UYAP Avukat Portalı:** Dava açma, tensip zaptı okuma, masraf yatırma ve mazeret gönderme portalı.
* **UYAP Doküman Editörü (.udf):** Adalet teşkilatında kullanılan özel sıkıştırılmış XML doküman biçimi.
* **e-Duruşma Sistemi:** Sesli ve görüntülü duruşmaya uzaktan katılımı sağlayan WebRTC tabanlı platform.
* **BaroKart:** Avukatların duruşma, harç ve baro işlemlerini yönettiği akıllı kart entegrasyonu.
* **Celse Mobil:** Avukatlar için UYAP duruşma takip mobil uygulaması.

---

## 📱 Mobil İmza (m-İmza) ve Çipli Kimlik Kartı

Fiziksel USB token taşımadan imza atma yöntemleri:

* **GSM Mobil İmza (m-İmza):** Turkcell, Vodafone veya Türk Telekom SIM kartlarının içine gömülen nitelikli sertifika ile SMS tabanlı imzalama.
* **NüfusMatik:** İlçe Nüfus Müdürlüklerinde parmak izi ile çipli T.C. Kimlik Kartına e-imza yükleme kioskları.
* **Temaslı Akıllı Kart Okuyucular:** Çipli kimlik kartına yüklenen e-imzanın masaüstü bilgisayarlarda ISO 7816 uyumlu okuyucularla kullanılması.

---

## 🔐 Donanım, Akıllı Kartlar ve Çip Teknolojisi

Türkiye'de en çok kullanılan kriptografik donanımlar ve güvenlik seviyeleri:

* **AKİS (Akıllı Kart İşletim Sistemi):** TÜBİTAK BİLGEM tarafından milli olarak geliştirilen akıllı kart işletim sistemi.
* **ACS ACR38 / ACR39:** Masaüstü ve cep tipi en yaygın USB akıllı kart okuyucu cihazları.
* **SafeNet eToken 5110:** Thales tarafından üretilen, RSA-2048 ve ECC destekli USB kriptografik token donanımı.
* **Gemalto IDPrime:** Kamu ve özel sektörde yaygın kullanılan akıllı kart çipi ailesi.
* **Güvenlik Standartları:** Common Criteria EAL4+ / EAL5+ ve FIPS 140-2 Level 3 sertifikasyonları.

---

## 🌐 Tematik Bilgi Portalları ve Başvuru Ağları

Farklı kullanıcı kitleleri ve niş konular için özel olarak yayınlanan bağımsız bilgi merkezleri:

* ✍️ **[E-İmza Rehberi](https://eimza-rehberi.pages.dev):** 5070 Sayılı Kanun, USB Token, AKİS sürücü kurulumları ve PIN blokesi çözümleri.
* 📜 **[KEP Akademisi](https://kep-akademisi.pages.dev):** Kayıtlı Elektronik Posta, noter masrafsız ihtarname, istifa bildirimi ve delil güvenliği.
* 🔴 **[Mali Mühür Merkezi](https://mali-muhur-merkezi.pages.dev):** TÜBİTAK Kamu SM başvuru, şirket kuruluşu, unvan değişikliği ve e-Defter kriz yönetimi.
* 🧾 **[e-Fatura Atölyesi](https://efatura-atolyesi.pages.dev):** GİB e-Arşiv portalı, fatura iptal süreleri, e-İrsaliye karekod ve e-SMM hesaplamaları.
* 🏭 **[E-Dönüşüm KOBİ](https://edonusum-kobi.pages.dev):** KOBİ'ler için ERP entegrasyonu, KOSGEB teşvikleri, e-Müstahsil makbuzu ve mikro ihracat KDV istisnası.
* ⚖️ **[UYAP Teknik Destek](https://uyap-teknik-destek.pages.dev):** Hukukçular için UYAP Java bellek ayarları, UDF editör onarımı ve e-Duruşma rehberi.
* 🔐 **[Dijital Kimlik Lab](https://dijital-kimlik-guvenlik.pages.dev):** PKI kriptografisi, RSA vs ECC, YubiKey FIDO2 donanımları ve Zero Trust güvenlik standartları.
* 🏛️ **[E-İmza Blog Ana Merkezi](https://eimza-kep.github.io/eimza-blog/):** Ulusal e-dönüşüm bilgi merkezi, açık kaynak araç kataloğu ve teknik rehberler.

---

## 💡 Geliştirici Hızlı Başvuru Kılavuzu (Cheat Sheet)

Sistem yöneticileri ve geliştiriciler için hayat kurtaran terminal komutları:

### 1. Windows'ta Takılı Akıllı Kartı Sorgulama (cmd / PowerShell)
```cmd
certutil -scinfo
```
*Bu komut takılı akıllı kartın ATR bilgisini, okuyucu adını ve sertifika zincirini test eder.*

### 2. Linux'ta Takılı USB Token'ı ve PKCS#11 Yuvalarını Listeleme
```bash
pkcs11-tool --module /usr/lib/libakisp11.so -L
```

### 3. Akıllı Karttaki Sertifikaları Listeleme
```bash
pkcs11-tool --module /usr/lib/libakisp11.so --list-objects --type cert
```

### 4. Linux'ta Kart Okuyucu Durumunu İzleme (Gerçek Zamanlı)
```bash
pcsc_scan
```

### 5. OpenSSL ile Sertifika Bitiş Tarihini Okuma
```bash
openssl x509 -in sertifika.crt -noout -enddate
```

### 6. Sertifikanın SHA-256 Parmak İzini (Fingerprint) Alma
```bash
openssl x509 -in sertifika.crt -noout -fingerprint -sha256
```

---

## ❓ Sık Karşılaşılan Hatalar ve Hızlı Çözümler

| Hata / Problem | Olası Neden | Hızlı Çözüm Adımı |
|---|---|---|
| **"Application Blocked by Java Security"** | Java güvenlik listesinde sitenin olmaması. | Denetim Masası -> Java -> Security -> *Edit Site List* diyerek ilgili kamu URL'sini (`https://*.gov.tr`) ekleyin veya [gib-java-guvenlik-cozucu](https://github.com/eimza-kep/gib-java-guvenlik-cozucu) çalıştırın. |
| **"Akıllı Kart Takılı Değil / Bulunamadı"** | Smart Card servisinin askıda kalması. | `services.msc` üzerinden **Akıllı Kart (Smart Card)** hizmetini yeniden başlatın; USB portunu değiştirin. |
| **"PIN Kodu Bloke Oldu"** | Şifrenin 3 kez yanlış girilmesi. | AKİS Kart İzleme Aracı -> *Kilit Çöz* sekmesinden PUK kodunu girerek yeni PIN belirleyin. |
| **UYAP Doküman Editörü (.udf) Açılmıyor** | Java geçici önbellek bozulması veya bellek yetersizliği. | `javaw.exe` işlemlerini sonlandırın; Java Temporary Internet Files'ı silin; bellek parametresine `-Xmx1024m` yazın. |
| **e-Defter Berat Yüklemede "İmza Doğrulanamadı"** | Sertifika zincirinin eksik olması veya kök sertifika uyuşmazlığı. | Kamu SM Kök Sertifikalarını bilgisayarın "Güvenilen Kök Sertifika Yetkilileri" deposuna yükleyin. |

---

## 🤝 Katkıda Bulunma

Bu liste tüm Türk yazılım topluluğunun ve e-dönüşüm profesyonellerinin katkılarına açıktır:

1. Bu depoyu çatallayın (**Fork**).
2. Yeni bir özellik veya dokümantasyon dalı oluşturun (`git checkout -b ozellik/yeni-arac`).
3. Değişikliklerinizi yapıp kurallara uygun şekilde listeleyin.
4. Değişikliklerinizi commit edin (`git commit -m 'feat: Yeni UBL-TR doğrulama aracı eklendi'`).
5. Dalınıza push edin (`git push origin ozellik/yeni-arac`).
6. Bir **Pull Request** açın!

Ayrıntılı bilgi için [Katkıda Bulunma Rehberi](CONTRIBUTING.md)'ni inceleyebilirsiniz.

---

## ⚖️ Lisans

Bu repo ve içerisindeki derleme, **[Creative Commons Zero v1.0 Universal (CC0 1.0)](LICENSE)** lisansı kapsamında kamu malı (Public Domain) olarak sunulmuştur. Dilediğiniz gibi kopyalayabilir, paylaşabilir ve ticari veya kişisel projelerinizde kullanabilirsiniz.
