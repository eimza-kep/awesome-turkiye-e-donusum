# Awesome Türkiye E-Dönüşüm 🇹🇷⚡

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Lisans: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Portal](https://img.shields.io/badge/Rehber-E--%C4%B0mza%20Blog-22c55e.svg)](https://eimza-kep.github.io/eimza-blog/)

> Türkiye'deki **E-İmza**, **Mali Mühür**, **KEP (Kayıtlı Elektronik Posta)**, **e-Fatura**, **e-Defter**, **UYAP**, **GİB** ve **e-Devlet** ekosistemi için derlenmiş açık kaynaklı kütüphaneler, resmi portallar, sürücüler, araçlar ve teknik rehberler listesi.

---

## 📑 İçindekiler

- [🏛️ Resmi Kurumlar ve Mevzuat](#️-resmi-kurumlar-ve-mevzuat)
- [🔑 Nitelikli Elektronik Sertifika (NES) Sağlayıcıları](#-nitelikli-elektronik-sertifika-nes-sağlayıcıları)
- [💻 Açık Kaynak Kütüphaneler ve SDK'lar](#-açık-kaynak-kütüphaneler-ve-sdklar)
- [🛠️ Faydalı Araçlar ve Betikler](#️-faydalı-araçlar-ve-betikler)
- [📚 Teknik Çözüm ve Hata Rehberleri](#-teknik-çözüm-ve-hata-rehberleri)
- [💼 KOBİ & E-Dönüşüm İş Modelleri](#-kobi--e-dönüşüm-iş-modelleri)
- [🤝 Katkıda Bulunma](#-katkıda-bulunma)

---

## 🏛️ Resmi Kurumlar ve Mevzuat

* [5070 Sayılı Elektronik İmza Kanunu](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=5070&MevzuatTur=1&MevzuatTertip=5) - Türkiye'de elektronik imzanın hukuki temeli ve ıslak imzaya eşdeğerlik hükümleri.
* [Bilgi Teknolojileri ve İletişim Kurumu (BTK)](https://www.btk.gov.tr/) - Elektronik sertifika hizmet sağlayıcılarını yetkilendiren ve denetleyen üst kurul.
* [Gelir İdaresi Başkanlığı (GİB) e-Belge Portalı](https://ebelge.gib.gov.tr/) - e-Fatura, e-Arşiv, e-İrsaliye, e-Defter ve e-SMM mevzuat ve standartları.
* [TÜBİTAK BİLGEM Kamu Sertifikasyon Merkezi (Kamu SM)](https://kamusm.bilgem.tubitak.gov.tr/) - Devlet kurumlarına ve şirketlere Mali Mühür sağlayan resmi otorite.
* [Adalet Bakanlığı UYAP Bilişim Sistemi](https://uyap.gov.tr/) - Yargı organları, avukatlar ve vatandaşlar için e-imzalı adli işlemler portalı.
* [Ticaret Bakanlığı MERSİS Portalı](https://mersis.ticaret.gov.tr/) - Şirket kuruluşu, ana sözleşme ve tescil işlemlerinin e-imzayla yürütüldüğü merkezi sicil sistemi.
* [Kamu İhale Kurumu (EKAP)](https://ekap.kik.gov.tr/) - Elektronik Kamu Alımları Platformu ve e-teklif imzalama sistemi.

---

## 🔑 Nitelikli Elektronik Sertifika (NES) Sağlayıcıları

BTK tarafından yetkilendirilmiş resmi Elektronik Sertifika Hizmet Sağlayıcıları (ESHS):

* [TÜBİTAK Kamu SM](https://kamusm.bilgem.tubitak.gov.tr/) - Mali Mühür ve kamu e-imza sağlayıcısı.
* [TÜRKTRUST](https://www.turktrust.com.tr/) - Nitelikli elektronik sertifika, zaman damgası ve SSL sağlayıcısı.
* [E-Güven (Elektronik Bilgi Güvenliği A.Ş.)](https://www.e-guven.com/) - Türkiye'nin ilk özel e-imza sağlayıcısı.
* [E-Tuğra (E-Tuğra EBG A.Ş.)](https://www.e-tugra.com.tr/) - E-İmza, KEP ve mobil imza hizmetleri.
* [TN KEP / TN Bilişim](https://www.tnkep.com.tr/) - KEP ve e-imza altyapısı.
* [Bilgi Teknolojileri (BilgiTek)](https://www.bilgiteknolojileri.com.tr/) - Elektronik sertifika hizmet sağlayıcısı.
* [EDM Bilişim](https://www.edmbilisim.com.tr/) - E-Dönüşüm, e-Fatura ve e-İmza operatörü.

---

## 💻 Açık Kaynak Kütüphaneler ve SDK'lar

### Java
* [TÜBİTAK Kamu SM MA3 API](https://kamusm.bilgem.tubitak.gov.tr/urunler/yazilim/ma3api/) - Türkiye'deki resmi CAdES, PAdES, XAdES e-imza ve zaman damgası kütüphanesi.
* [SmartCard-API](https://github.com/) - Java akıllı kart (PKCS#11) erişim arayüzleri.

### Python
* [python-pdf-eimza-dogrulayici](https://github.com/eimza-kep/python-pdf-eimza-dogrulayici) - Türkiye PAdES/CAdES standartlarındaki PDF imzalarını sıfır harici bağımlılıkla doğrulayan araç.
* [pyHanko](https://github.com/MatthiasValvekens/pyHanko) - Python için gelişmiş PDF dijital imzalama ve doğrulama kütüphanesi.
* [python-pkcs11](https://github.com/danni/python-pkcs11) - Akıllı kartlar ve HSM'ler için PKCS#11 standardı Python sarmalayıcısı.

### .NET / C#
* [BouncyCastle C#](https://www.bouncycastle.org/csharp/) - X.509 sertifika yönetimi ve kriptografik imzalama.
* [PCSC-Sharp](https://github.com/danm-de/pcsc-sharp) - Windows PC/SC akıllı kart okuyucu kütüphanesi.

---

## 🛠️ Faydalı Araçlar ve Betikler

* [gib-java-guvenlik-cozucu](https://github.com/eimza-kep/gib-java-guvenlik-cozucu) - GİB, UYAP, MERSİS ve EKAP Java "Application Blocked" güvenlik engelini tek tıkla çözen araç.
* [mali-muhur-eimza-suresi-kontrol](https://github.com/eimza-kep/mali-muhur-eimza-suresi-kontrol) - Takılı Mali Mühür ve E-İmzaların bitiş süresini tarayan ve kalan gün sayısını raporlayan denetleyici.
* [akilli-kart-surucu-teshis](https://github.com/eimza-kep/akilli-kart-surucu-teshis) - Windows 10/11 "Akıllı kart tanınmıyor" hatasını teşhis eden ve servisleri onaran araç.
* [python-pdf-eimza-dogrulayici](https://github.com/eimza-kep/python-pdf-eimza-dogrulayici) - Türkiye PAdES/CAdES standartlarındaki PDF imzalarını sıfır harici bağımlılıkla doğrulayan araç.

---

## 📚 Resmi Rehberler ve Dokümantasyon

* 📖 [Kamu SM Kılavuzları](https://kamusm.bilgem.tubitak.gov.tr/destek/kilavuzlar/) - TÜBİTAK Kamu SM resmi kullanım ve kurulum kılavuzları.
* 📖 [GİB e-Defter Kılavuzları](https://edefter.gov.tr/kilavuzlar.html) - Gelir İdaresi Başkanlığı e-Defter teknik ve mevzuat kılavuzları.
* 📖 [GİB e-Arşiv Fatura Portalı Kullanım Kılavuzu](https://ebelge.gib.gov.tr/) - e-Belge portalı resmi rehberleri.
* 📖 [EKAP Yardım Dokümanları](https://ekap.kik.gov.tr/) - Kamu İhale Kurumu e-teklif ve ihale rehberleri.
* 📖 [Adalet Bakanlığı UYAP Yardım Masası](https://uyap.gov.tr/Uyap-Yardim) - Avukat ve vatandaş portalı e-imza sorun giderme kılavuzları.
* 📖 [MERSİS Kullanım Kılavuzları](https://mersis.ticaret.gov.tr/) - Şirket tescil ve kuruluş adımları.

---

## 🤝 Katkıda Bulunma

Bu liste topluluk katkılarıyla büyümektedir. Yeni bir kütüphane, resmi kılavuz veya faydalı bir araç önermek isterseniz lütfen [Pull Request](https://github.com/eimza-kep/awesome-turkiye-e-donusum/pulls) gönderin veya [Issue](https://github.com/eimza-kep/awesome-turkiye-e-donusum/issues) açın.

---

## ⚖️ Lisans

Bu çalışma [Creative Commons Zero v1.0 Universal (CC0 1.0)](LICENSE) kapsamında kamu malı (Public Domain) olarak sunulmuştur.
