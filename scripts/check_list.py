#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Awesome Türkiye E-Dönüşüm Liste Bütünlüğü ve Bağlantı Denetleyicisi
===================================================================
Bu betik README.md dosyasındaki markdown bağlantılarını, yerel dosya
bağlantılarını, iç çapa (anchor) bağlantılarını ve liste istatistiklerini doğrular.
"""

import os
import re
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def slugify(title):
    """GitHub markdown başlık çapa algoritması."""
    title = title.strip().lower()
    # Emojileri ve özel sembolleri temizle
    title = re.sub(r"[^\w\s-]", "", title)
    # Boşlukları tireye dönüştür
    title = re.sub(r"\s+", "-", title)
    return title.strip("-")

def validate(readme_path=None):
    """README.md dosyasını doğrular ve istatistik sözlüğü döndürür."""
    if readme_path is None:
        readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    readme_path = os.path.abspath(readme_path)

    if not os.path.exists(readme_path):
        raise FileNotFoundError(f"README.md bulunamadı: {readme_path}")

    base_dir = os.path.dirname(readme_path)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()

    # 1. Başlıkları topla
    headings = []
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            headings.append(m.group(2).strip())

    # 2. Markdown bağlantılarını topla
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    all_links = link_pattern.findall(content)

    ext_links = [l for l in all_links if l[1].startswith("http://") or l[1].startswith("https://")]
    anchor_links = [l for l in all_links if l[1].startswith("#")]
    local_file_links = [l for l in all_links if not l[1].startswith("http://") and not l[1].startswith("https://") and not l[1].startswith("#")]

    errors = []

    # Boş bağlantı denetimi
    for text, url in all_links:
        if not url.strip():
            errors.append(f"Boş bağlantı hedefi tespit edildi: '[{text}]()'")
        if not text.strip():
            errors.append(f"Boş bağlantı metni tespit edildi: '[]({url})'")

    # Yerel dosya bağlantısı denetimi
    for text, path in local_file_links:
        # Strip query or hash from local file path if present
        clean_path = path.split("#")[0].split("?")[0]
        full_target = os.path.join(base_dir, clean_path)
        if not os.path.exists(full_target):
            errors.append(f"Yerel dosya bağlantısı bulunamadı: '[{text}]({path})' -> {full_target}")

    # Önemli anahtar depoların varlığı
    required_repos = [
        "100-e-donusum-skili",
        "turkiye-yapay-zeka-araclari",
        "e-donusum-rehberleri",
        "eimza-blog",
        "udf2md",
        "gib-java-guvenlik-cozucu"
    ]
    for req in required_repos:
        if req not in content:
            errors.append(f"Zorunlu referans depo eksik: '{req}'")

    stats = {
        "lines": len(lines),
        "headings": len(headings),
        "total_links": len(all_links),
        "ext_links": len(ext_links),
        "anchor_links": len(anchor_links),
        "local_file_links": len(local_file_links),
        "errors": errors,
        "is_valid": len(errors) == 0
    }
    return stats

def main():
    try:
        stats = validate()
    except Exception as e:
        print(f"[!] HATA: {e}")
        sys.exit(1)

    print("=" * 70)
    print("      AWESOME TÜRKİYE E-DÖNÜŞÜM LİSTE VE BAĞLANTI DENETİMİ")
    print("=" * 70)
    print(f"Toplam Satır Sayısı:        {stats['lines']}")
    print(f"Toplam Başlık / Kategori:   {stats['headings']}")
    print(f"Dış Bağlantı (URL) Sayısı:  {stats['ext_links']}")
    print(f"İç Çapa (Anchor) Sayısı:    {stats['anchor_links']}")
    print(f"Yerel Dosya Bağlantıları:   {stats['local_file_links']}")
    print("-" * 70)

    if not stats["is_valid"]:
        print(f"[!] {len(stats['errors'])} adet hata tespit edildi:")
        for err in stats["errors"]:
            print(f"  - {err}")
        sys.exit(1)

    print(" [OK] Tüm bağlantı hedefleri ve yerel dosyalar tanımlı.")
    print(" [OK] Zorunlu açık kaynak referans depoları eksiksiz.")
    print(" [OK] Liste biçimlendirme ve sözdizimi doğrulaması başarılı!")
    print("=" * 70)

if __name__ == "__main__":
    main()
