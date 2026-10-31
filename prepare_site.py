from pathlib import Path
from urllib.parse import urlparse
import os, html

repo = os.environ.get('REPOSITORY', '')
if '/' not in repo:
    raise SystemExit('Set REPOSITORY to owner/repository (GitHub Actions sets it automatically).')
owner, name = repo.split('/', 1)
source = Path(__file__).resolve().parent
out = source / '_site'
out.mkdir(exist_ok=True)
custom_file = source / 'CNAME'
custom = custom_file.read_text().strip() if custom_file.exists() else ''
if custom:
    host = custom.replace('https://', '').replace('http://', '').strip('/')
    base = 'https://' + host + '/'
    (out / 'CNAME').write_text(host + '\n')
else:
    path = '/' if name.lower() == f'{owner.lower()}.github.io' else f'/{name}/'
    base = f'https://{owner.lower()}.github.io{path}'

page = (source / 'index.html').read_text(encoding='utf-8')
canon = '<link rel="canonical" href="' + html.escape(base, quote=True) + '">'
page = page.replace('<!-- CANONICAL_URL_PLACEHOLDER -->', canon)
(out / 'index.html').write_text(page, encoding='utf-8')
(out / '.nojekyll').write_text('')
(out / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + html.escape(base) + '</loc></url></urlset>\n', encoding='utf-8')
# robots.txt must live at the hostname root to be effective. A project-site
# robots.txt under /repository/ does not apply to the hostname.
if custom or name.lower() == f'{owner.lower()}.github.io':
    (out / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + base + 'sitemap.xml\n', encoding='utf-8')
print('Site URL:', base)
