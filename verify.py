#!/usr/bin/env python3
"""Verify landing page structure."""
from html.parser import HTMLParser
from urllib.request import urlopen
import re, os

html = urlopen("http://localhost:8088/index.html").read().decode()

class StructureChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = []
        self.classes = []
        self.imgs = []
        self.links = []
        self.forms = []
        self.svgs = 0
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.tags.append(tag)
        if 'id' in attrs_dict:
            self.ids.append(attrs_dict['id'])
        if 'class' in attrs_dict:
            self.classes.extend(attrs_dict['class'].split())
        if tag == 'img':
            self.imgs.append(attrs_dict.get('src', ''))
        if tag == 'link':
            self.links.append(attrs_dict.get('href', ''))
        if tag == 'form':
            self.forms.append(attrs_dict.get('class', ''))
        if tag == 'svg':
            self.svgs += 1

checker = StructureChecker()
checker.feed(html)

print("=== STRUCTURAL VERIFICATION ===")
print(f"Total HTML tags parsed: {len(checker.tags)}")
print(f"Section IDs found: {checker.ids}")
print(f"SVG icons: {checker.svgs}")
print(f"Images: {checker.imgs}")
print(f"External links (CSS): {checker.links}")
print(f"Forms: {checker.forms}")

required_ids = ['hero', 'features', 'gallery', 'roadmap', 'platforms', 'email', 'footer']
missing = [id for id in required_ids if id not in checker.ids]
print(f"All 7 sections present: {'PASS' if not missing else 'FAIL: ' + str(missing)}")

lazy_count = html.count('loading="lazy"')
print(f"Images with loading=lazy: {lazy_count}")

card_count = checker.classes.count('feature-card')
print(f"Feature cards: {card_count}")

soon_count = checker.classes.count('badge--soon')
dev_count = checker.classes.count('badge--dev')
planned_count = checker.classes.count('badge--planned')
print(f"Badges - soon: {soon_count}, dev: {dev_count}, planned: {planned_count}")

ext_http = re.findall(r'(?:href|src)="(https?://[^"]+)"', html)
print(f"External HTTP resources: {len(ext_http)}")
if ext_http:
    for url in ext_http:
        print(f"  ! {url}")

html_size = os.path.getsize("/home/dawg0/.hermes/Projects/cannalog/.worktrees/t_78d40822/docs/landing-page/index.html")
css_size = os.path.getsize("/home/dawg0/.hermes/Projects/cannalog/.worktrees/t_78d40822/docs/landing-page/styles.css")
print(f"index.html: {html_size:,} bytes")
print(f"styles.css: {css_size:,} bytes")
print(f"Total (HTML+CSS): {html_size + css_size:,} bytes")
