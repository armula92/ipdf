# IPDF alt3 시안(weforum.org 구조) 빌드: python3 _src/build_alt3.py  ->  alt3/index.html
import os
from content import VALUES1, VALUES2
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P, Q, D = '../images/photo/', '../images/poster/', '../downloads/'
LANG = ('<ul class="lang" aria-label="언어 선택 (Google 번역)" translate="no">'
        '<li><a href="?lang=ko" data-lang="ko">KO</a></li><li><a href="?lang=en" data-lang="en">EN</a></li>'
        '<li><a href="?lang=zh-CN" data-lang="zh-CN">中文</a></li><li><a href="?lang=ja" data-lang="ja">日本語</a></li></ul>')


def tile(img, title, small, href):
    return f'<a class="tile" href="{href}"><img src="{P}{img}" alt="" loading="lazy"><b><small>{small}</small>{title}</b></a>'


def intro(label, head, text, link, href):
    return f'<div class="intro-card"><small>{label}</small><b>{head}</b><p>{text}</p><a class="pill" href="{href}">{link}</a></div>'


# How we drive impact: 탭 세 개
T_GOALS = intro('About the Goals', '4개 목표와 12개 핵심 지표로 공공가치를 추구합니다', '지속가능발전목표(SDGs)를 바탕으로 사회, 공동체, 환경, 문화의 문제를 디자인으로 풉니다.', '비전과 계획', '../vision.html') + ''.join(
    tile(i, t, s, '../vision.html#goals') for i, t, s in [
        ('f2024-hall2.jpg', '공공편의', 'Safety, Universal, Affordable'), ('china-group.jpg', '협력사회', 'Equality, Network, Community'),
        ('parkingday-2022.jpg', '환경지속', 'Net Zero, Ecology, Biophilic'), ('cab2023-room.jpg', '문화창조', 'Human, Diversity, Impact'),
        ('sem-7.jpg', '외교, 문화, 교육, 학술', 'Four Fields of Activity')])
T_MEET = intro('About the Meetings', '해마다 회원국을 돌며 국제포럼을 엽니다', '2021년 발대식 이후 서울, 선양, 시안, 도쿄에서 다섯 번의 국제포럼과 사전 세미나를 열었습니다.', '포럼 아카이브', '../forums.html') + ''.join(
    tile(i, t, s, f'../forums.html#{h}') for i, t, s, h in [
        ('f2025-stage.jpg', '제5회 국제공공디자인포럼', '2025 / 서울', 'f2025'), ('f2024-banner.jpg', '제4회 국제공공디자인포럼', '2024 / 시안', 'f2024'),
        ('gk2024-group.jpg', 'GK 세미나 &amp; Pre-IPDF', '2024 / 도쿄', 'pre2024'), ('china-hall.jpg', '제3회 국제공공디자인포럼', '2023 / 선양', 'f2023'),
        ('f2021-1st-group.jpg', '제1회 국제공공디자인포럼', '2021 / 서울', 'f2021'), ('f2021-founding-1.jpg', '국제공공디자인포럼 발대식', '2021 / 서울', 'founding')])
T_MEM = intro('About the Members', '네 나라의 대학, 기업, 기관이 함께합니다', 'IPDF Korea, IPDF China, IPDF Japan을 중심으로 2022년부터 프랑스가 함께합니다.', '조직과 위원', '../about.html#organization') + ''.join(
    tile(i, t, s, '../about.html#people') for i, t, s in [
        ('f2025-poster-stand.jpg', 'IPDF Korea', '홍익대학교 공공디자인연구센터 외'), ('f2024-group.jpg', 'IPDF China', '노신미술대학, 시안건축과기대학 외'),
        ('gk2024-seminar.jpg', 'IPDF Japan', '토요대학, GK 디자인그룹 외'), ('cab2023-talk.jpg', 'IPDF France', 'Cabanon Vertical')])

# Spotlight
SPOT2 = [('f2025-hall.jpg', 'The 5th Forum / Seoul', '지속 가능한 도시를 위한 ‘문화적 공공재’: 공공디자인의 사회적 책임과 미래 비전', '../forums.html#f2025', '창립 5주년 포럼이 문화역서울284 RTO에서 한국, 중국, 일본 연사와 함께 열렸습니다.'),
         ('f2024-outdoor.jpg', 'The 4th Forum / Xi’an', '도시를 위한 공공디자인, 시안에서 아시아 3국의 기반을 다지다', '../forums.html#f2024', '“공공디자인이 한국을 넘어 아시아 디자인의 리더로 자리매김하도록 국제 교류를 넓히겠습니다.”')]
SPOT3 = [('gk2024-seminar.jpg', 'Pre-IPDF / Tokyo', '도시디자인을 통한 공공가치 실현, 도쿄 GK 디자인그룹 세미나', '../forums.html#pre2024'),
         ('cab2023-hall.jpg', 'IPDF France', '프랑스 공공디자인 거버넌스, Cabanon Vertical과 함께', '../forums.html#cabanon2023'),
         ('sem-1.jpg', 'Seminar', '세미나와 교육 프로그램으로 다음 세대 공공디자이너를 기릅니다', '../gallery.html')]
spot = ''.join(f'<article class="s2"><div class="im" data-lb data-cap="{t}"><img src="{P}{i}" alt="{t}" loading="lazy"></div><span class="lab">{l}</span><a class="st" href="{h}">{t}</a><p class="ex">{e}</p></article>' for i, l, t, h, e in SPOT2)
spot += ''.join(f'<article class="s3"><div class="im" data-lb data-cap="{t}"><img src="{P}{i}" alt="{t}" loading="lazy"></div><span class="lab">{l}</span><a class="st" href="{h}">{t}</a></article>' for i, l, t, h in SPOT3)

# 어두운 띠: 제5회 포럼 프로그램
TALKS = [('f2025-poster-stand.jpg', '기조발제', '김주연 / IPDF 의장'), ('f2025-keynote.jpg', '‘공공디자인 거버넌스’를 통한 사회적 가치 실현 전략', '우용호 / 사회공헌센터'),
         ('f2025-hall.jpg', '기업의 사회적 책임(S)을 디자인으로 확장하다', '김수민 / 현대자동차'), ('f2025-audience.jpg', '중국의 참여형 공공디자인 정책 실행 사례', '조위지 / 노신미술대학'),
         ('f2025-stage.jpg', '사회를 위한 디자인 실험', '이즈미야마 루이 / 일본대학'), ('sem-5.jpg', '소셜벤처와 공공디자인의 역량 강화', '이지영 / 홍익대학교'),
         ('f2024-designx.jpg', '시민 편의성 향상을 위한 중국의 공공디자인', '주가혜 / 노신미술대학'), ('sem-8.jpg', '참여를 통한 포용적 소통 공간디자인', '추민아 / 비들')]
talks = ''.join(f'<a class="mini" href="../forums.html#f2025"><img src="{P}{i}" alt="" loading="lazy"><b>{t}<small>{s}</small></b></a>' for i, t, s in TALKS)


def disc(title, img, vals, href):
    k, e, d, pj, pd, t = vals[0]
    grid = ''.join(f'<div><span class="lab">{e}</span><a class="st" href="{href}">{kk}: {pjj}</a><p>{dd}</p></div>' for kk, e, dd, pjj, pdd, tt in vals[1:])
    return (f'<div class="dp"><div class="top"><h3>{title}</h3><a class="pill" href="{href}">View more</a></div>'
            f'<div class="big"><img src="{P}{img}" alt="" loading="lazy"></div><span class="lab">{e}</span><a class="st l" href="{href}">{k}: {pj}</a>'
            f'<p style="font-size:14.5px;color:var(--ink2)">{pd}</p><div class="grid">{grid}</div></div>')


NEWS = [('2025. 10. 29', '제5회 국제공공디자인포럼, 문화역서울284에서 ‘문화적 공공재’를 논하다', '포럼 아카이브', '../forums.html#f2025'),
        ('2024. 6. 17', '제4회 IPDF 국제공공디자인포럼 성료, 중국 시안에서 ‘도시를 위한 공공디자인’', '보도자료 PDF', D + 'IPDF-2024-press.pdf'),
        ('2024. 1. 19', '한중일, 공공디자인으로 만나다: GK 세미나 &amp; Pre-IPDF 2024', '포럼 아카이브', '../forums.html#pre2024'),
        ('2023. 6. 12', '제3회 국제공공디자인포럼, 선양 노신미술대학에서 도시재생과 공공디자인 논의', '포럼 아카이브', '../forums.html#f2023'),
        ('2022. 10. 26', 'IPDF 2022 코리아 에디션, 대한민국 공공디자인 페스티벌과 함께', '포럼 아카이브', '../forums.html#korea2022'),
        ('2021. 12. 10', '제1회 IPDF 국제공공디자인포럼 개최, ‘환경, 사회 그리고 협력(E.S.G)과 공공디자인’', '보도자료 PDF', D + 'IPDF-2021-press.pdf')]
news = ''.join(f'<li><time>{d}</time><a class="st" href="{h}">{t}</a><a class="src" href="{h}">{s}</a></li>' for d, t, s, h in NEWS)

ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M3 6h12M3 12h8M3 18h12"/><circle cx="17" cy="11" r="3.2"/><path d="m19.4 13.4 2.1 2.1"/></svg>'

HTML = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IPDF 국제공공디자인포럼 | International Public Design Forum</title>
<meta name="description" content="공공디자인으로 세계의 공공 문제를 함께 풀어 가는 국제공공디자인포럼(IPDF).">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0A2F38">
<link rel="icon" type="image/svg+xml" href="../images/logo-mark-teal.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap">
<link rel="stylesheet" href="assets/alt3.css">
</head>
<body>
<a class="sr" href="#main">본문 바로가기</a>
<header class="hd"><div class="in">
  <button class="ic menu-open" aria-expanded="false" aria-controls="drawer">{ICON}<span>Menu</span></button>
  <a class="logo" href="#main" aria-label="IPDF 홈"><img src="../images/logo-h-white.svg" alt="IPDF International Public Design Forum" width="305" height="112"></a>
  <div class="r">{LANG}<a class="pill fill noarr hide-m" href="#join">참가 신청</a><a class="pill ghost noarr" href="mailto:ipdfmanager@gmail.com">문의</a></div>
</div></header>
<div class="scrim"></div>
<aside class="drawer" id="drawer" aria-label="전체 메뉴">
  <button class="x" aria-label="메뉴 닫기">×</button>
  <h5>About us</h5><a class="dl" href="../about.html">포럼 소개</a><a class="dl" href="../about.html#greeting">인사말</a><a class="dl" href="../about.html#charter">헌장</a><a class="dl" href="../about.html#people">조직과 위원</a>
  <h5>Our work</h5><a class="dl" href="../vision.html">비전과 계획</a><a class="dl" href="../forums.html">포럼 아카이브</a><a class="dl" href="../gallery.html">갤러리</a>
  <h5>Engage</h5><a class="dl" href="#join">참가 신청</a><a class="dl" href="{D}IPDF-introduction-ko.pdf">소개자료 다운로드</a>
  {LANG}
</aside>

<main id="main">
<section class="hero">
  <div class="in hero-g">
    <div>
      <h1>공공디자인으로 세계의 공공 문제를 함께 이해하고, 더 나은 도시를 향해 함께 나아갑니다</h1>
      <a class="pill soft" href="../about.html">포럼 소개</a>
    </div>
    <div class="vid" data-lb data-cap="제5회 국제공공디자인포럼 / 서울 / 2025"><img src="{P}f2025-stage.jpg" alt="제5회 국제공공디자인포럼 무대" fetchpriority="high"><span><i>▶</i>제5회 포럼 현장 보기</span></div>
  </div>
  <div class="impact" data-car>
    <div class="in ihead">
      <h2>How IPDF works</h2>
      <div class="seg" role="tablist" aria-label="IPDF가 일하는 방식">
        <button role="tab" aria-selected="true" aria-controls="tp1">Goals</button>
        <button role="tab" aria-selected="false" aria-controls="tp2">Meetings</button>
        <button role="tab" aria-selected="false" aria-controls="tp3">Members</button>
      </div>
    </div>
    <div class="panel" id="tp1" role="tabpanel"><div class="track">{T_GOALS}</div></div>
    <div class="panel" id="tp2" role="tabpanel" hidden><div class="track">{T_MEET}</div></div>
    <div class="panel" id="tp3" role="tabpanel" hidden><div class="track">{T_MEM}</div></div>
    <div class="in arrows"><button data-dir="-1" aria-label="이전">←</button><button data-dir="1" aria-label="다음">→</button></div>
  </div>
</section>

<section class="sec" style="padding-top:20px">
  <div class="in">
    <div class="sh"><div><h2>Spotlight</h2><p>포럼과 세미나, 교류 현장의 최근 소식입니다.</p></div><a class="pill" href="../forums.html">More Stories</a></div>
    <div class="spot">{spot}</div>
  </div>
</section>

<section class="band" data-car>
  <img src="{P}f2025-audience.jpg" alt="">
  <div class="in"><h2>제5회 국제공공디자인포럼 2025 프로그램</h2></div>
  <div class="track">{talks}</div>
  <div class="in arrows"><button data-dir="-1" aria-label="이전">←</button><button data-dir="1" aria-label="다음">→</button></div>
</section>

<section class="sec gray">
  <div class="in">
    <div class="sh"><div><h2>Discover</h2><p>IPDF의 8대 공공가치와 국제 프로젝트를 주제별로 살펴봅니다.</p></div><a class="pill" href="../vision.html">More topics</a></div>
    <div class="disc">{disc('사회를 위한 공공디자인', 'f2024-hall.jpg', VALUES1, '../vision.html#values')}{disc('함께하는 공공디자인', 'f2021-mou-3.jpg', VALUES2, '../vision.html#values')}</div>
  </div>
</section>

<section class="sec" id="join" style="padding-bottom:20px">
  <div class="in">
    <div class="news">
      <div class="a"><img src="../images/logo-mark-white.svg" alt="" width="145" height="112"><div><b>IPDF <span>참가 신청과 소식</span></b><p>포럼 참가, 발표, 공동 개최와 협력을 원하시면 사무국으로 연락해 주십시오.</p></div><a class="pill ghost" href="mailto:ipdfmanager@gmail.com?subject=%5BIPDF%5D%20%EC%B0%B8%EA%B0%80%20%EC%8B%A0%EC%B2%AD">참가 신청</a></div>
      <div class="b">홍익대학교 공공디자인연구센터 사무국<span>ipdfmanager@gmail.com / +82 2 320 1237 / 서울시 마포구 와우산로 94, 홍문관 1310호</span></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="in">
    <div class="sh"><div><h2>IPDF in the news</h2></div><a class="pill" href="{D}IPDF-2024-press.pdf">Press releases</a></div>
    <ul class="newsl">{news}</ul>
  </div>
</section>

<section class="sec gray">
  <div class="in">
    <div class="sh"><div><h2>IPDF 자료와 헌장</h2></div></div>
    <div class="promo">
      <div class="pr a"><div class="t"><b>IPDF Introduction</b><p>인사말, 포럼 소개, 비전과 계획, 주요 활동, 헌장을 담은 공식 소개자료입니다. 한국어와 영어로 받아 보실 수 있습니다.</p><div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:auto"><a class="pill ghost" href="{D}IPDF-introduction-ko.pdf" download>한국어 PDF</a><a class="pill ghost" href="{D}IPDF-introduction-en.pdf" download>English PDF</a></div></div><div class="v"><img src="{Q}2021-founding.jpg" alt="" loading="lazy"></div></div>
      <div class="pr b"><div class="t"><b style="color:var(--light)">Mission of IPDF</b><ol><li>공공의 이익과 안전의 공공가치를 추구한다</li><li>디자인을 통해 인류의 삶의 질 향상에 기여한다</li><li>공공의 문제를 해결하는 협력과 전략을 발전시킨다</li><li>공공가치를 실현하는 연구와 실천을 협력한다</li><li>공공디자인의 방향을 제시하고 문화를 창조한다</li></ol><a class="pill ghost" href="../about.html#charter">헌장 전문 보기</a></div><div class="v"><img src="{Q}2025-5th.jpg" alt="" loading="lazy"></div></div>
    </div>
  </div>
</section>
</main>

<footer class="ft"><div class="in">
  <div class="cols">
    <div><h6>About us</h6><ul><li><a href="../about.html">포럼 소개</a></li><li><a href="../about.html#greeting">인사말</a></li><li><a href="../about.html#founding">발기문</a></li><li><a href="../about.html#charter">헌장</a></li></ul></div>
    <div><h6>More from IPDF</h6><ul><li><a href="../vision.html">비전과 계획</a></li><li><a href="../forums.html">포럼 아카이브</a></li><li><a href="../gallery.html">갤러리</a></li><li><a href="{D}IPDF-2024-press.pdf">보도자료</a></li></ul></div>
    <div><h6>Engage with us</h6><ul><li><a href="#join">참가 신청</a></li><li><a href="mailto:ipdfmanager@gmail.com">ipdfmanager@gmail.com</a></li><li><a href="tel:+8223201237">+82 2 320 1237</a></li><li>홍익대학교 홍문관 1310호</li></ul></div>
    <div><h6>Language editions</h6>{LANG}<h6 style="margin-top:22px">Other drafts</h6><ul><li><a href="../index.html">기본 시안</a></li><li><a href="../alt2/">alt2 시안</a></li></ul></div>
  </div>
  <div class="bot"><img src="../images/logo-h-teal.svg" alt="IPDF" width="305" height="112"><span>International Public Design Forum Committee / R1310, 94 Wausan-ro, Mapo-gu, Seoul, Republic of Korea</span><span>&copy; 2026 International Public Design Forum</span></div>
</div></footer>
<div id="gt-el" aria-hidden="true"></div>
<script src="assets/alt3.js"></script>
</body>
</html>
'''
open(os.path.join(ROOT, 'alt3', 'index.html'), 'w', encoding='utf-8').write(HTML)
print('built alt3/index.html')
