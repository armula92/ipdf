# IPDF 홈페이지 빌드: python3 _src/build.py
# 공통 머리말/꼬리말을 각 페이지 본문에 입혀 루트에 html 파일을 만든다.
import os, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://armula92.github.io/ipdf/'
from content import PAGES  # noqa: E402

NAV = [('about.html', '포럼 소개'), ('vision.html', '비전과 계획'), ('forums.html', '포럼 아카이브'),
       ('gallery.html', '갤러리'), ('about.html#contact', '참가 문의')]
LANG = ('<ul class="lang" aria-label="언어 선택 (Google 번역)" translate="no">'
        '<li><a href="?lang=ko" data-lang="ko" lang="ko" title="한국어">KO</a></li>'
        '<li><a href="?lang=en" data-lang="en" lang="en" title="English (Google Translate)">EN</a></li>'
        '<li><a href="?lang=zh-CN" data-lang="zh-CN" lang="zh-CN" title="中文 (Google 翻译)">中文</a></li>'
        '<li><a href="?lang=ja" data-lang="ja" lang="ja" title="日本語 (Google 翻訳)">日本語</a></li></ul>')

def head(p):
    url = BASE + ('' if p['file'] == 'index.html' else p['file'])
    img = BASE + 'images/photo/' + p.get('og', 'f2025-stage.jpg')
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": "국제공공디자인포럼",
          "alternateName": ["International Public Design Forum", "IPDF"], "url": BASE, "foundingDate": "2021-08-28",
          "email": "ipdfmanager@gmail.com", "telephone": "+82-2-320-1237",
          "address": {"@type": "PostalAddress", "streetAddress": "와우산로 94 홍문관 1310호", "addressLocality": "마포구",
                      "addressRegion": "서울특별시", "postalCode": "04066", "addressCountry": "KR"}}
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p['title'])}</title>
<meta name="description" content="{html.escape(p['desc'])}">
<meta name="keywords" content="국제공공디자인포럼, IPDF, International Public Design Forum, 공공디자인, 국제포럼, 사회를 위한 공공디자인, 함께하는 공공디자인, 홍익대학교 공공디자인연구센터, 公共设计, 公共デザイン">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="IPDF 국제공공디자인포럼">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{html.escape(p['title'])}">
<meta property="og:description" content="{html.escape(p['desc'])}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#134B57">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<link rel="icon" type="image/svg+xml" href="images/logo-mark-teal.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="page-{p['file'][:-5]}">
<a class="sr" href="#main">본문 바로가기</a>
<header class="site">
  <div class="wrap nav">
    <a href="index.html" class="logo" aria-label="IPDF 국제공공디자인포럼 홈"><img src="images/logo-h-white.svg" alt="IPDF International Public Design Forum" width="305" height="112"></a>
    <nav class="nav-menu" aria-label="주 메뉴"><ul class="menu">{''.join(f'<li><a href="{h}"{" aria-current=page" if h == p["file"] else ""}>{t}</a></li>' for h, t in NAV)}</ul></nav>
    <div class="nav-actions">{LANG}<button class="burger" aria-label="메뉴 열기" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button></div>
  </div>
</header>
<div class="mobile-menu" id="mobileMenu">
  {LANG}
  {''.join(f'<a class="m-link" href="{h}">{t}</a>' for h, t in [('index.html', '홈')] + NAV)}
  <p class="m-contact">ipdfmanager@gmail.com<br>+82 2 320 1237</p>
</div>
<main id="main">
'''

FOOT = '''</main>
<footer class="site">
  <div class="wrap">
    <div class="foot">
      <div>
        <a href="index.html" class="logo" aria-label="IPDF 홈"><img src="images/logo-h-white.svg" alt="IPDF International Public Design Forum" width="305" height="112" style="height:46px;width:auto"></a>
        <p class="foot-note">국제공공디자인포럼은 공공의 이익과 안전의 가치를 추구하며, 외교, 문화, 교육, 학술 분야에서 디자인을 통한 비영리 국제 협력을 이어 갑니다.</p>
      </div>
      <div>
        <h4>Menu</h4>
        <ul><li><a href="about.html">포럼 소개</a></li><li><a href="vision.html">비전과 계획</a></li><li><a href="forums.html">포럼 아카이브</a></li><li><a href="gallery.html">갤러리</a></li><li><a href="about.html#contact">참가 문의</a></li></ul>
      </div>
      <div>
        <h4>Secretariat</h4>
        <ul><li>국제공공디자인포럼 위원회 사무국</li><li>홍익대학교 공공디자인연구센터</li><li>서울시 마포구 와우산로 94, 홍문관 1310호 (04066)</li><li><a href="tel:+8223201237">T. +82 2 320 1237</a></li><li><a href="mailto:ipdfmanager@gmail.com">E. ipdfmanager@gmail.com</a></li></ul>
      </div>
    </div>
    <div class="copy"><span>&copy; International Public Design Forum. All rights reserved.</span><span>R1310, 94 Wausan-ro, Mapo-gu, Seoul, Republic of Korea</span></div>
  </div>
</footer>
<div id="gt-el" aria-hidden="true"></div>
<script src="assets/site.js"></script>
</body>
</html>
'''

for p in PAGES:
    with open(os.path.join(ROOT, p['file']), 'w', encoding='utf-8') as f:
        f.write(head(p) + p['body'] + FOOT)
    print('built', p['file'])
