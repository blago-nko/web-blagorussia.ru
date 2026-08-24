#!/usr/bin/env python3
"""
Генератор карты 301-редиректов из sitemap.xml Blogger.
Поддерживает sitemap index с множественными страницами.
"""
import json
import re
from pathlib import Path
from datetime import datetime
import xml.etree.ElementTree as ET
import urllib.request
import ssl

def parse_sitemap_file(sitemap_file):
    """Парсит локальный sitemap.xml файл."""
    urls = []
    sitemap_locs = []
    
    try:
        tree = ET.parse(sitemap_file)
        root = tree.getroot()
        
        if root.tag.endswith('sitemapindex'):
            ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for sitemap_elem in root.findall('ns:sitemap', ns):
                loc_elem = sitemap_elem.find('ns:loc', ns)
                if loc_elem is not None and loc_elem.text:
                    sitemap_locs.append(loc_elem.text.strip())
        else:
            ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for url_elem in root.findall('ns:url', ns):
                loc_elem = url_elem.find('ns:loc', ns)
                if loc_elem is not None and loc_elem.text:
                    urls.append(loc_elem.text.strip())
    except ET.ParseError:
        with open(sitemap_file, 'r', encoding='utf-8') as f:
            content = f.read()
        urls = re.findall(r'<loc>([^<]+)</loc>', content)
    
    return urls, sitemap_locs

def download_sitemap_from_url(sitemap_url):
    """Скачивает sitemap по URL (игнорируя SSL ошибки)."""
    print(f"   Скачиваем: {sitemap_url}")
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        with urllib.request.urlopen(sitemap_url, context=ctx) as response:
            content = response.read().decode('utf-8')
        
        # ИСПРАВЛЕНИЕ: парсим напрямую из строки, а не через ET.parse
        root = ET.fromstring(content)
        
        urls = []
        ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        for url_elem in root.findall('ns:url', ns):
            loc_elem = url_elem.find('ns:loc', ns)
            if loc_elem is not None and loc_elem.text:
                urls.append(loc_elem.text.strip())
        
        print(f"    ✅ Найдено {len(urls)} URL")
        return urls
    except Exception as e:
        print(f"    ⚠️  Ошибка: {e}")
        return []

def blogger_url_to_hugo_slug(blogger_url):
    """Преобразует URL Blogger в slug для Hugo."""
    match = re.search(r'/\d{4}/\d{2}/(.+?)\.html$', blogger_url)
    if match:
        return match.group(1)
    return None

def generate_redirect_map(sitemap_file, output_file="migration_seo_map.json"):
    """Генерирует карту редиректов из sitemap."""
    print(f"🔄 Парсинг индексной карты: {sitemap_file}")
    
    _, sitemap_locs = parse_sitemap_file(sitemap_file)
    
    if not sitemap_locs:
        print("⚠️  Не найдены под-sitemap в индексе!")
        return None
    
    print(f" Найдено под-sitemap: {len(sitemap_locs)}")
    
    all_urls = []
    for loc in sitemap_locs:
        urls = download_sitemap_from_url(loc)
        all_urls.extend(urls)
    
    print(f"\n Всего URL из всех sitemap: {len(all_urls)}")
    
    redirects = {}
    skipped = []
    
    for url in all_urls:
        slug = blogger_url_to_hugo_slug(url)
        if slug:
            old_path = re.search(r'(\/\d{4}\/\d{2}\/.+?\.html)$', url)
            if old_path:
                redirects[old_path.group(1)] = f"/{slug}/"
            else:
                skipped.append(url)
        else:
            skipped.append(url)
    
    output = {
        "site": "web-blagorussia",
        "generated_at": datetime.now().isoformat(),
        "source": sitemap_file,
        "total_urls": len(all_urls),
        "redirects_count": len(redirects),
        "skipped_count": len(skipped),
        "redirects": redirects
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Карта редиректов создана: {output_file}")
    print(f"📊 Всего редиректов: {len(redirects)}")
    print(f"⚠️  Пропущено: {len(skipped)}")
    
    return output_file

if __name__ == "__main__":
    generate_redirect_map(
        sitemap_file="data/blogger/sitemap.xml",
        output_file="data/blogger/migration_seo_map.json"
    )
