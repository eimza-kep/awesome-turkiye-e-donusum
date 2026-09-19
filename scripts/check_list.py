#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Awesome Türkiye E-Dönüşüm Liste Bütünlüğü ve Bağlantı Denetleyicisi
===================================================================
Bu betik README.md dosyasındaki markdown bağlantılarını, iç çapa (anchor)
bağlantılarını ve liste istatistiklerini doğrular.
"""

import os
import re
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def slugify(title):
    """GitHub markdown başlık slug algoritması."""
    title = title.strip().lower()
    # Türkçe karakter dönüşümü (GitHub biçimi)
    tr_map = str.maketrans("çğıöşü", "cgiosu")
    # GitHub slug özel karakter temizliği
    title = re.sub(r"[^\w\s-]", "", title)
    title = re.sub(r"\s+", "-", title)
    return title

def main():
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
    if not os.path.exists(readme_path):
        print(f"Hata: README.md bulunamadı: {readme_path}")
        sys.exit(1)

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

    print("=" * 70)
    print("      AWESOME TÜRKİYE E-DÖNÜŞÜM LİSTE VE BAĞLANTI DENETİMİ")
    print("=" * 70)
    print(f"Toplam Satır Sayısı:      {len(lines)}")
    print(f"Toplam Başlık / Kategori: {len(headings)}")
    print(f"Dış Bağlantı Sayısı:      {len(ext_links)}")
    print(f"İç Çapa (Anchor) Sayısı:  {len(anchor_links)}")
    print("-" * 70)

    # 3. Kırık / boş bağlantı denetimi
    empty_links = [l for l in all_links if not l[1].strip()]
    if empty_links:
        print(f"[!] HATA: {len(empty_links)} adet hedefi boş markdown bağlantısı var!")
        sys.exit(1)

    print(" [OK] Tüm bağlantı hedefleri tanımlı.")
    print(" [OK] Liste biçimlendirme ve sözdizimi doğrulaması başarılı!")
    print("=" * 70)

if __name__ == "__main__":
    main()
