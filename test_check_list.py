#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import os
import sys
from pathlib import Path

# Add scripts directory to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))
import check_list

class TestAwesomeList(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).parent
        self.readme_path = self.repo_root / "README.md"

    def test_readme_file_exists(self):
        self.assertTrue(self.readme_path.exists(), "README.md dosyası bulunamadı")
        content = self.readme_path.read_text(encoding="utf-8")
        self.assertGreater(len(content), 2000, "README.md içeriği beklenenden kısa")

    def test_validator_execution(self):
        stats = check_list.validate(str(self.readme_path))
        self.assertTrue(stats["is_valid"], f"Doğrulama hataları: {stats.get('errors')}")
        self.assertEqual(len(stats["errors"]), 0)
        self.assertGreater(stats["ext_links"], 50, "En az 50 dış bağlantı olmalı")
        self.assertGreater(stats["anchor_links"], 10, "En az 10 iç çapa bağlantısı olmalı")

    def test_key_repositories_included(self):
        content = self.readme_path.read_text(encoding="utf-8")
        key_repos = [
            "100-e-donusum-skili",
            "turkiye-yapay-zeka-araclari",
            "e-donusum-rehberleri",
            "eimza-blog",
            "udf2md",
            "python-pdf-eimza-dogrulayici",
            "gib-java-guvenlik-cozucu",
            "akilli-kart-surucu-teshis",
            "mali-muhur-eimza-suresi-kontrol"
        ]
        for repo in key_repos:
            self.assertIn(repo, content, f"Zorunlu repo eksik: {repo}")

    def test_cheat_sheet_commands(self):
        content = self.readme_path.read_text(encoding="utf-8")
        self.assertIn("security list-smartcards", content, "macOS akıllı kart tanılama komutu eksik")
        self.assertIn("pcsctest", content, "macOS pcsctest komutu eksik")
        self.assertIn("Cert:\\CurrentUser\\My", content, "PowerShell sertifika sorgulama komutu eksik")
        self.assertIn("udf2md", content, "udf2md dönüştürücü komutu eksik")

    def test_local_documentation_files(self):
        license_file = self.repo_root / "LICENSE"
        contrib_file = self.repo_root / "CONTRIBUTING.md"
        self.assertTrue(license_file.exists(), "LICENSE dosyası bulunamadı")
        self.assertTrue(contrib_file.exists(), "CONTRIBUTING.md dosyası bulunamadı")

if __name__ == "__main__":
    unittest.main()
