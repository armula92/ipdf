# IPDF alt2 시안 빌드: python3 _src/build_alt2.py  ->  alt2/index.html
import os
from content import GOALS, CHARTER, VALUES1, VALUES2
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P, Q = '../images/photo/', '../images/poster/'
LANG = ('<ul class="lang" aria-label="언어 선택 (Google 번역)" translate="no">'
        '<li><a href="?lang=ko" data-lang="ko">KO</a></li><li><a href="?lang=en" data-lang="en">EN</a></li>'
        '<li><a href="?lang=zh-CN" data-lang="zh-CN">中文</a></li><li><a href="?lang=ja" data-lang="ja">日本語</a></li></ul>')

# ---- 행사 데이터: (id, year, date, city, kind, title, theme, desc, poster, photos, program, related)
EV = [
 ('f2025', '2025', '2025. 10. 29', 'Seoul', 'The 5th Forum', '제5회 국제공공디자인포럼', '지속 가능한 도시를 위한 ‘문화적 공공재’ / 공공디자인의 사회적 책임과 미래 비전',
  '창립 5주년을 맞아 문화역서울284 RTO에서 열렸습니다.', '2025-5th.jpg', ['f2025-stage.jpg', 'f2025-keynote.jpg', 'f2025-audience.jpg'],
  [('기조발제', '김주연 / IPDF 의장'), ('‘공공디자인 거버넌스’를 통한 사회적 가치 실현 전략', '우용호 / 사회공헌센터'),
   ('기업의 사회적 책임(S)을 디자인으로 확장하다', '김수민 / 현대자동차'), ('중국의 참여형 공공디자인 정책 실행 사례', '조위지 / 노신미술대학'),
   ('사회를 위한 디자인 실험', '이즈미야마 루이 / 일본대학'), ('소셜벤처와 공공디자인의 역량 강화', '이지영 / 홍익대학교 공공디자인연구센터'),
   ('시민 편의성 향상을 위한 중국의 공공디자인', '주가혜 / 노신미술대학'), ('참여를 통한 포용적 소통 공간디자인', '추민아 / 비들')], False),
 ('festival2024', '2024', '2024. 11. 3', 'Seoul', 'Public Design Day', '공공디자인 페스티벌 2024', '함께 하실래요? / 사람을 위한 공공공간 디자인',
  '공공디자인 페스티벌과 함께 문화역서울284 RTO에서 연 시민 참여 프로그램입니다.', '2024-festival.jpg', [], [], False),
 ('f2024', '2024', '2024. 6. 14', 'Xi’an', 'The 4th Forum', '제4회 국제공공디자인포럼', '도시를 위한 공공디자인 / Public Design for the City',
  '시안건축과기대학에서 열렸으며, 아시아 3국의 공공디자인 확산을 위한 기반을 마련했습니다. 한국공예디자인문화진흥원이 후원했습니다.', '2024-4th.jpg',
  ['f2024-banner.jpg', 'f2024-designx.jpg', 'f2024-hall.jpg', 'f2024-panel.jpg'],
  [('기조발제', '인보강 / 시안건축과기대학 예술학원 원장'), ('기조발제', '김주연 / IPDF 의장'),
   ('관람은 표현에 앞선다: 공공예술과 도시 갱신', '한유봉 / 시안건축과기대학'), ('Design X: Socio-Value and Effect', '이현성 / 홍익대학교'),
   ('일본의 토탈디자인 사례', '엄지연 / 이오디 디자인 연구소'), ('도시 조각의 치유 기능', '진정이 / 시안건축과기대학'),
   ('가치를 만드는 디자인', '홍태의 / 홍익대학교 공공디자인연구센터'), ('사회적 처방과 공공서비스 디자인', '주하나 / PSDI 심리사회 디자인연구소'),
   ('도시 환경에서 빨간색 테마 조각 디자인과 적용', '임자겸 / 시안건축과기대학')], False),
 ('tachikawa2024', '2024', '2024. 5. 24', 'Seoul', 'Related Program', 'The Public Design Forum 2024', '디자인을 위한 진화사고 / Evolutional Creativity for Public Design',
  'NOSIGNER 대표, WDO 이사, JIDA 이사장 에이스케 타치카와 초청 특강, 홍익대학교.', '2024-tachikawa.jpg', [], [], True),
 ('pre2024', '2024', '2024. 1. 19', 'Tokyo', 'Pre-IPDF', 'GK 세미나 & Pre-IPDF 2024', '도시디자인을 통한 공공가치 실현',
  '일본 도쿄 GK 디자인그룹에서 한국, 중국, 일본 전문가 21명이 3국의 도시디자인 프로젝트를 나눈 사전 세미나입니다.', '2024-pre-ipdf.jpg',
  ['gk2024-group.jpg', 'gk2024-seminar.jpg'],
  [('인사말', '다나카 / GK 디자인그룹 회장'), ('인사말', '김주연 / 홍익대학교'), ('일본 토탈디자인 사례: 우쓰노미야 LRT', '이리에 / GK 디자인그룹'),
   ('Urban Design Tomorrow: Insights from Suwon and Incheon', '고은정 / 전 인천광역시 도시디자인과장'),
   ('중국 도시 설계 프로젝트의 전형적 사례: 시안 대당불야성', '민신러 / 시안건축과기대학')], False),
 ('cabanon2023', '2023', '2023. 9. 19', 'Seoul', 'IPDF France', 'PDF X Cabanon Vertical', '프랑스 공공디자인 거버넌스 / Public Design Governance in France',
  '프랑스 회원 Cabanon Vertical과 함께 프랑스의 참여형 어바니즘을 이야기했습니다. 주한 프랑스 대사관 문화과가 후원했습니다.', '2023-cabanon.jpg',
  ['cab2023-hall.jpg', 'cab2023-talk.jpg', 'cab2023-book.jpg'],
  [('프랑스의 도시를 만드는 사람들', '추민아 / 비들'), ('프랑스 참여형 어바니즘 접근법', '올리비에 브뒤 / Cabanon Vertical'),
   ('토론: 트랜지셔널 어바니즘', '김상아 / 홍익대학교 공공디자인연구센터')], False),
 ('loud2023', '2023', '2023. 7. 21', 'Seoul', 'Related Program', 'The Public Design Forum X LOUD', '사회갈등 예방을 위한 디자인 Vol. 1',
  '공공소통연구소 LOUD와 함께 공공소통 관점의 사회갈등과 공공디자인 해법을 논의했습니다.', '2023-pdfx-loud.jpg', [],
  [('공공소통 관점에서 찾는 사회적 소통 과제', '이종혁 / 광운대학교'), ('강남역 토끼굴 흡연 문제 해결 공공디자인 실험실', '이미정 / 강남구청'),
   ('사회갈등 예방을 위한 흡연부스 디자인', '문현배 / SEDG')], True),
 ('f2023', '2023', '2023. 6. 12', 'Shenyang', 'The 3rd Forum', '제3회 국제공공디자인포럼', '도시재생과 공공디자인 / Urban Regeneration and Public Design',
  '노신미술대학 건축예술디자인대학 학술강당에서 온라인과 오프라인으로 열렸습니다.', '2023-3rd.jpg', ['china-group.jpg', 'china-hall.jpg'],
  [('공공디자인의 시대', '김주연 / 홍익대학교'), ('공공을 위한 디자인', '이현성 / 홍익대학교'), ('공공미술의 공간연출', 'Zhou Yufang / 중앙미술학원')], False),
 ('f2022', '2022', '2022. 12. 10', 'Shenyang / Online', 'The 2nd Forum', '제2회 국제공공디자인포럼', '도시재생과 공공디자인 / 도시를 재생하고, 지속 가능하게 하는 공공디자인',
  '중국, 한국, 일본, 프랑스 연사 열네 명이 VooV, Bilibili, Zoom, YouTube 생중계로 도시재생의 의미와 가능성을 논의했습니다.', '2022-2nd.jpg', [],
  [('현대 공공디자인 속의 환경의식', '소단 / 중국공예미술관'), ('미래 생활유산을 통한 지역재생', '권영재 / 상지대학교'),
   ('제3의 공간과 관계자본의 힘', '황석연 / 행정안전부'), ('도시, 디자인, 실천', '上田孝明 / Nikken Activity Design Lab'),
   ('공공디자인 실천', 'Olivier Bedu / Cabanon Vertical'), ('공중 건강을 위한 디자인', '조초 / 칭화대학 미술학원'),
   ('', '외 조로, 양엽, 마극신, 주우방, 설문개, 진외, 고양, 강민')], False),
 ('korea2022', '2022', '2022. 10. 26', 'Seoul', 'Korea Edition', 'IPDF 2022 코리아 에디션', '공공을 치유하고 변화시킨 도시 실험 이야기',
  '대한민국 공공디자인 페스티벌 2022와 함께 문화역서울284 RTO에서 연 외전 행사입니다.', '2022-korea-edition.jpg', [],
  [('질문을 던지는 공공디자인', '젤리장 대표'), ('Park(ing) Day A to Z: ‘함께’의 가치', '홍태의 / 홍익대학교 공공디자인연구센터'),
   ('사회를 위한 공공디자인 실험, Socio-Public Design Activism', '이현성 / 홍익대학교')], False),
 ('parking2022', '2022', '2022. 9. 16~17', 'Seoul', 'Culture Movement', '2022 국제 파킹데이', '누구나 쉬어갈 수 있는 사람을 위한 주차장',
  '주차 공간을 하루 동안 시민의 쉼터로 바꾸는 국제 문화 운동입니다.', '2022-parkingday.jpg', ['parkingday-2022.jpg'], [], False),
 ('f2021', '2021', '2021. 12. 18', 'Seoul / Online', 'The 1st Forum', '제1회 국제공공디자인포럼', '환경, 사회 그리고 협력(E.S.G)과 공공디자인 / 공공성을 위한 디자인의 가치',
  '홍익대학교 공공디자인연구센터에서 YouTube와 Zoom으로 중계한 첫 포럼입니다.', '2021-1st.jpg', ['f2021-1st-group.jpg', 'f2021-1st-studio.jpg', 'f2021-1st-speakers.jpg'],
  [('걷는 의식을 디자인하다', '이소베 타카후미 / GK설계'), ('퍼블릭 라이프로부터의 도시디자인', '다케다 시게아키 / 오사카부립대학'),
   ('도시문화의 전승과 재편', '강민 / 노신미술대학'), ('How to Incorporate Design into Healthcare Innovation', '조초 / 칭화대학'),
   ('ESG 경영의 이해', '박성훈 / 사회적가치연구원'), ('불확실성 시대 공공성과 시민', '이광재 / 한국매니페스토실천본부'),
   ('사회적 가치 향상을 위한 기업의 ESG 활용 사례', '안진근 / 백석대학교'), ('토론 좌장', '장영호 / 홍익대학교')], False),
 ('founding', '2021', '2021. 8. 28', 'Seoul', 'Founding Congregation', '국제공공디자인포럼 발대식', '사회를 위한 공공디자인, 함께하는 공공디자인',
  '한국, 중국, 일본 3개국 전문가가 문화역서울284에 모여 포럼을 창립하고 헌장을 선포했습니다.', '2021-founding.jpg',
  ['f2021-founding-1.jpg', 'f2021-founding-speech.jpg', 'f2021-mou-1.jpg', 'f2021-online-1.jpg'],
  [('인사말', '김주연 / 한국'), ('인사말', '수단 / 중국'), ('인사말', '스가와라 마이코 / 일본'), ('축사', '김태훈 원장')], False),
]
YEAR_NOTE = {'2025': 'Seoul', '2024': 'Xi’an, Tokyo, Seoul', '2023': 'Shenyang, Seoul', '2022': 'Shenyang, Seoul', '2021': 'Seoul'}


def ev_html(e):
    eid, y, d, city, kind, title, theme, desc, pst, ph, prog, rel = e
    photos = ''.join(f'<img src="{P}{p}" alt="{title}" data-lb data-cap="{title} / {city} / {y}" loading="lazy">' for p in ph)
    acc = ''
    if prog:
        items = ''.join((f'<li><b>{t}</b><small>{s}</small></li>' if t else f'<li class="m">{s}</li>') for t, s in prog)
        acc = (f'<button class="acc-b" aria-expanded="false" aria-controls="p-{eid}"><span>프로그램 보기</span></button>'
               f'<div class="acc-p" id="p-{eid}"><div><ul>{items}</ul></div></div>')
    return (f'<article class="ev rv" id="{eid}"><div class="pi"><img src="{Q}{pst}" alt="{title} 포스터" data-lb data-cap="{title} 포스터" loading="lazy"></div>'
            f'<div><p class="k">{kind}<span>{d} / {city}</span></p><h4>{title}</h4><p class="th">{theme}</p><p class="ds">{desc}</p>'
            + (f'<div class="ph">{photos}</div>' if photos else '') + acc + '</div></article>')


years = ['2025', '2024', '2023', '2022', '2021']
archive = ''.join(
    f'<div class="year" data-y="{y}"><h3>{y}<i>{YEAR_NOTE[y]}</i></h3><div>' + ''.join(ev_html(e) for e in EV if e[1] == y) + '</div></div>'
    for y in years)
filters = '<button data-y="all" aria-pressed="true">All</button>' + ''.join(f'<button data-y="{y}" aria-pressed="false">{y}</button>' for y in years)

SL = ['f2025-stage.jpg', 'f2024-banner.jpg', 'gk2024-group.jpg', 'f2024-hall.jpg', 'f2021-founding-1.jpg']
slides = ''.join(f'<div class="sl"><img src="{P}{s}" alt="" {"fetchpriority=high" if i == 0 else "loading=lazy"}></div>' for i, s in enumerate(SL))
hbtn = ''.join(f'<button aria-label="사진 {i + 1}"></button>' for i in range(len(SL)))

goals = ''.join(f'<div class="goal rv"><h3>{k}</h3><p class="en">{e}</p><ul>' + ''.join(f'<li><b>{n}</b>{t}</li>' for n, t in ind) + '</ul></div>'
                for k, e, ind in GOALS)


def vals(vs):
    return '<div class="vals" style="margin-top:40px">' + ''.join(
        f'<div class="rv d{i}"><h4>{k}<i>{e}</i></h4><p>{d}</p><p class="pj">{pj}</p><p>{pd}</p></div>' for i, (k, e, d, pj, pd, t) in enumerate(vs)) + '</div>'


charter = ''.join(f'<li class="rv"><span>하나.</span><p>{k}<i>{e}</i></p></li>' for k, e in CHARTER)

GAL = [('f2025-hall.jpg', '제5회 국제공공디자인포럼', '서울 / 2025'), ('f2024-outdoor.jpg', '제4회 국제공공디자인포럼', '시안 / 2024'),
       ('f2025-poster-stand.jpg', '기조발제', '서울 / 2025'), ('cab2023-room.jpg', 'PDF X Cabanon Vertical', '서울 / 2023'),
       ('f2024-group.jpg', '제4회 국제공공디자인포럼', '시안 / 2024'), ('sem-5.jpg', 'IPDF 세미나', '홍익대학교'),
       ('gk2024-seminar.jpg', 'GK 세미나 & Pre-IPDF', '도쿄 / 2024'), ('f2024-audience.jpg', '토론', '시안 / 2024'),
       ('cab2023-night.jpg', 'Cabanon Vertical과 함께', '서울 / 2023'), ('sem-7.jpg', '사례 발표', '홍익대학교'),
       ('f2021-mou-3.jpg', '협약 서명', '발대식 / 2021'), ('f2024-hall2.jpg', '포럼 강당', '시안 / 2024'),
       ('sem-9.jpg', 'IPDF 세미나', '홍익대학교'), ('f2021-1st-speakers.jpg', '제1회 포럼 연사', '서울 / 2021'),
       ('sem-3.jpg', '토론', '홍익대학교'), ('f2025-audience.jpg', '세미나', '서울 / 2025'), ('sem-8.jpg', '토론', '홍익대학교'),
       ('f2021-founding-room.jpg', '발대식', '서울 / 2021'), ('sem-1.jpg', '세미나 현장', '홍익대학교'), ('china-hall.jpg', '국제 교류', '중국')]
gal = ''.join(f'<figure data-lb data-cap="{t} / {s}"><img src="{P}{f}" alt="{t} {s}" loading="lazy"><figcaption><b>{t}</b>{s}</figcaption></figure>' for f, t, s in GAL)

CITIES = '<span class="f">Seoul</span><span>Shenyang</span><span class="a">Public Design</span><span class="f">Xi’an</span><span>Tokyo</span><span class="a">Together</span><span class="f">Paris</span><span>Seoul</span><span class="a">for Society</span>'

NAV = [('#about', 'About', '포럼 소개'), ('#forum2025', 'Forum 2025', '제5회 포럼'), ('#agenda', 'Agenda', '비전과 목표'),
       ('#archive', 'Archive', '포럼 아카이브'), ('#gallery', 'Gallery', '갤러리'), ('#charter', 'Mission', '헌장'), ('#contact', 'Contact', '참가 문의')]

HTML = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IPDF International Public Design Forum | 국제공공디자인포럼</title>
<meta name="description" content="Public Design for Society, Public Design Together. 한국, 중국, 일본, 프랑스가 함께하는 국제공공디자인포럼(IPDF).">
<meta name="robots" content="noindex">
<meta property="og:title" content="IPDF International Public Design Forum">
<meta property="og:image" content="https://www.armula.com/ipdf/images/photo/f2025-stage.jpg">
<meta name="theme-color" content="#0E1416">
<link rel="icon" type="image/svg+xml" href="../images/logo-mark-teal.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="assets/alt2.css">
</head>
<body>
<a class="sr" href="#about">본문 바로가기</a>
<header class="top"><div class="in">
  <a class="logo" href="#top" aria-label="IPDF 처음으로"><img src="../images/logo-h-white.svg" alt="IPDF International Public Design Forum" width="305" height="112"></a>
  <div class="top-r">
    <nav class="top-nav" aria-label="주 메뉴"><a href="#about">About</a><a href="#forum2025">Forum 2025</a><a href="#archive">Archive</a><a href="#gallery">Gallery</a></nav>
    {LANG}
    <button class="menu-btn" aria-expanded="false" aria-controls="overlay"><span>Menu</span><i></i></button>
  </div>
</div></header>
<div class="overlay" id="overlay">
  <nav aria-label="전체 메뉴">{''.join(f'<a href="{h}">{e}<small>{k}</small></a>' for h, e, k in NAV)}</nav>
  <aside>{LANG}<b>International Public Design Forum</b>홍익대학교 공공디자인연구센터<br>서울시 마포구 와우산로 94, 홍문관 1310호<br>ipdfmanager@gmail.com<br>+82 2 320 1237<p style="margin-top:24px"><a href="../index.html" style="text-decoration:underline">기본 시안 보기</a></p></aside>
</div>

<main id="top">
<section class="hero" aria-label="국제공공디자인포럼">
  {slides}
  <div class="hero-prog">{hbtn}</div>
  <div class="hero-t in">
    <span class="label">International Public Design Forum / Since 2021</span>
    <h1 class="display">Public Design<br>for Society, <span class="l2"><span class="it acc">Public Design</span> Together</span></h1>
    <div class="hero-row">
      <p class="ko-sub">사회를 위한 공공디자인, 함께하는 공공디자인. 한국, 중국, 일본, 프랑스의 공공디자인 전문가가 공공가치를 위한 국제 연대를 만듭니다.</p>
      <dl class="next"><dt>Latest</dt><dd>The 5th IPDF / 29 October 2025</dd><dt>Venue</dt><dd>Culture Station Seoul 284, RTO</dd></dl>
    </div>
  </div>
</section>

<div class="marq" aria-hidden="true"><div class="marq-t">{CITIES}{CITIES}</div></div>

<section class="blk paper" id="about">
  <div class="in">
    <div class="mani">
      <div class="rv"><span class="label">About IPDF</span><span class="bar"></span></div>
      <div>
        <p class="big rv">공공디자인은 공공의 이익과 안전을 추구하며 <b>인류의 삶의 질을 높이는 디자인</b>입니다. 국제공공디자인포럼은 공공디자인을 <em>문화적 공공재</em>로 만들기 위해 국경을 넘어 협력합니다.</p>
        <div class="cols">
          <p class="rv">2021년 한국, 중국, 일본 3개국 전문가가 모여 시작한 포럼은 2022년 프랑스가 참여하며 4개 회원국의 국제 협력 관계로 자랐습니다. 공공환경의 다양한 문제를 찾고, 공공과 민간이 협력하는 전략으로서 공공디자인을 발전시켜 우리 삶의 문제를 해결하는 대안적 가치를 만들어 갑니다.</p>
          <p class="rv d1">포럼은 안전, 배려, 편의, 품격의 공공디자인 가치를 추구합니다. 외교, 문화, 교육, 학술 분야의 비영리 활동으로 공공디자인의 방향을 제시하고, 다양한 매체와 프로그램으로 공공디자인의 지식과 지혜를 나눕니다.</p>
        </div>
        <p class="facts rv"><span class="s">Founded 2021</span><span class="sep">I</span><span class="s">회원국 한국, 중국, 일본, 프랑스</span><span class="sep">I</span><span class="s">국제포럼 5회</span><span class="sep">I</span><span class="s">핵심 지표 12</span></p>
      </div>
    </div>
  </div>
</section>

<section class="blk paper" style="padding-top:0">
  <div class="in greet">
    <img class="rv" src="{P}chair.jpg" alt="국제공공디자인포럼 의장 김주연" loading="lazy">
    <div class="rv d1">
      <span class="label">Greeting from the Chair</span>
      <p class="q">“공공디자인을 통해 <em>더 좋은 세상</em>을 만들기 위한 우리의 발걸음에 함께해 주십시오.”</p>
      <div class="tx">
        <p>2021년 발대식을 시작으로 5년 차에 접어든 국제공공디자인포럼은 한국을 비롯한 일본, 중국, 프랑스 등 여러 나라와 공공가치 실현을 위한 국제적 연대와 교류를 펼치고 있습니다.</p>
        <p>많은 변화가 일고 있는 현대 사회에서 공공디자인은 디자인의 선한 영향력을 넓히기 위해 노력하고 있습니다. 국제공공디자인포럼은 지속 가능한 세계를 위한 국제 사회와의 협력을 이어 가겠습니다.</p>
      </div>
      <p class="sg">국제공공디자인포럼 의장<b>김주연</b></p>
    </div>
  </div>
</section>

<section class="blk" id="forum2025">
  <div class="in feat">
    <div class="pst rv"><img src="{Q}2025-5th.jpg" alt="제5회 국제공공디자인포럼 2025 포스터" data-lb data-cap="제5회 국제공공디자인포럼 포스터"></div>
    <div>
      <span class="label rv">The 5th International Public Design Forum / 2025</span>
      <h2 class="d2 rv">Cultural Public Goods<br><span class="it acc">for a Sustainable City</span></h2>
      <p class="ko-sub rv" style="margin-top:22px">지속 가능한 도시를 위한 ‘문화적 공공재’<br>공공디자인의 사회적 책임과 미래 비전</p>
      <dl class="meta rv"><dt>Date</dt><dd>2025년 10월 29일 수요일, 오후 2시~5시</dd><dt>Venue</dt><dd>문화역서울284 RTO, 서울 중구 통일로 1</dd><dt>Host</dt><dd>국제공공디자인포럼, 한국공간디자인단체총연합회, 한국공예디자인문화진흥원</dd><dt>Organizer</dt><dd>홍익대학교 공공디자인연구센터, 노신미술대학 도시재생 및 문화전승 국제교류센터</dd></dl>
      <div class="talks">
        <div class="g rv"><span>Keynote</span><ul><li><b>기조발제</b><small>김주연 / IPDF 의장, 홍익대학교 교수</small></li></ul></div>
        <div class="g rv"><span>Forum</span><ul>
          <li><b>‘공공디자인 거버넌스’를 통한 사회적 가치 실현 전략</b><small>우용호 / 사회공헌센터 소장, 한국</small></li>
          <li><b>기업의 사회적 책임(S)을 디자인으로 확장하다</b><small>김수민 / 현대자동차 ESG 매니저, 한국</small></li>
          <li><b>중국의 참여형 공공디자인 정책 실행 사례</b><small>조위지 / 노신미술대학 교수, 중국</small></li>
          <li><b>사회를 위한 디자인 실험</b><small>이즈미야마 루이 / 일본대학 교수, 일본</small></li></ul></div>
        <div class="g rv"><span>Seminar</span><ul>
          <li><b>소셜벤처와 공공디자인의 역량 강화</b><small>이지영 / 홍익대학교 공공디자인연구센터</small></li>
          <li><b>시민 편의성 향상을 위한 중국의 공공디자인</b><small>주가혜 / 노신미술대학 교수</small></li>
          <li><b>참여를 통한 포용적 소통 공간디자인</b><small>추민아 / 비들 대표</small></li></ul></div>
      </div>
      <div class="shots">
        <div class="w rv"><img src="{P}f2025-hall.jpg" alt="제5회 포럼 현장" data-lb data-cap="제5회 국제공공디자인포럼 / 서울 / 2025" loading="lazy"></div>
        <div class="rv"><img src="{P}f2025-poster-stand.jpg" alt="기조발제" data-lb data-cap="기조발제 / 서울 / 2025" loading="lazy"></div>
        <div class="rv d1"><img src="{P}f2025-keynote.jpg" alt="포럼 발표" data-lb data-cap="포럼 발표 / 서울 / 2025" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="blk paper" id="agenda">
  <div class="in">
    <div class="agenda-head">
      <div class="rv"><span class="label">Agenda / SDGs</span><h2 class="d2">4 Goals,<br><span class="it acc">12 Indicators</span></h2></div>
      <p class="ko-sub rv d1">국제사회가 함께 정한 지속가능발전목표(SDGs)를 바탕으로 사회, 공동체, 환경, 삶, 문화의 문제에 대한 대안을 찾고 디자인으로 해결합니다. ‘사회를 위한 공공디자인, 함께하는 공공디자인’을 의제로 4개 목표와 12개 핵심 지표를 세웠습니다.</p>
    </div>
    {goals}
  </div>
</section>

<section class="blk night2">
  <div class="in">
    <div class="vals-h rv"><div><span class="label">Public Design for Society</span><h2 class="d3">사회를 위한 공공디자인</h2></div></div>
    {vals(VALUES1)}
    <div class="vals-h rv"><div><span class="label">Public Design Together</span><h2 class="d3">함께하는 공공디자인</h2></div></div>
    {vals(VALUES2)}
  </div>
</section>

<section class="blk paper" id="archive">
  <div class="in">
    <div class="arch-head">
      <div class="rv"><span class="label">Archive 2021 to 2025</span><h2 class="d2">Forums and<br><span class="it acc">Gatherings</span></h2></div>
      <div class="filters rv" role="toolbar" aria-label="연도별 보기">{filters}</div>
    </div>
    {archive}
  </div>
</section>

<div class="marq" aria-hidden="true" style="background:var(--paper)"><div class="marq-t" style="animation-direction:reverse">{CITIES.replace('class="f"', 'class="f" style="color:var(--ink)"').replace('<span>', '<span style="-webkit-text-stroke-color:rgba(22,25,26,.35)">').replace('class="a"', 'class="a" style="color:var(--accent)"')}{CITIES.replace('class="f"', 'class="f" style="color:var(--ink)"').replace('<span>', '<span style="-webkit-text-stroke-color:rgba(22,25,26,.35)">').replace('class="a"', 'class="a" style="color:var(--accent)"')}</div></div>

<section class="blk" id="gallery" style="padding-bottom:8px">
  <div class="in gal-h">
    <div class="rv"><span class="label">Gallery</span><h2 class="d2">In the <span class="it acc">Room</span></h2></div>
    <p class="ko-sub rv d1">서울, 선양, 시안, 도쿄의 포럼과 세미나 현장입니다. 사진을 누르면 크게 볼 수 있습니다.</p>
  </div>
  <div class="masonry">{gal}</div>
</section>

<section class="blk teal" id="charter">
  <div class="in">
    <span class="label rv">Mission of IPDF</span>
    <h2 class="d2 rv" style="margin-bottom:clamp(40px,5vw,72px)">국제공공디자인포럼 헌장</h2>
    <ol class="charter">{charter}</ol>
  </div>
</section>

<section class="blk paper" id="people">
  <div class="in">
    <span class="label rv">Founders and Committee</span>
    <h2 class="d2 rv" style="margin-bottom:clamp(48px,6vw,90px)">Four Countries,<br><span class="it acc">One Forum</span></h2>
    <div class="ppl">
      <div class="rv"><h4>한국<i>IPDF Korea</i></h4><ul><li><b>김주연</b>IPDF 의장, 홍익대학교 교수</li><li><b>이현성</b>자문위원, 홍익대학교 공공디자인전공 교수</li><li><b>김상아</b>사무총장</li><li><b>홍태의</b>책임연구원</li><li><b>엄지연</b>위원, 이오디 디자인 연구소</li></ul></div>
      <div class="rv d1"><h4>중국<i>IPDF China</i></h4><ul><li><b>강민</b>노신미술대학 건축예술디자인학원 교수</li><li><b>조덕리</b>노신미술대학</li><li><b>주가혜</b>노신미술대학 교수</li></ul></div>
      <div class="rv d2"><h4>일본<i>IPDF Japan</i></h4><ul><li><b>高橋儀平</b>토요대학 명예교수</li><li><b>菅原麻衣子</b>토요대학 교수</li><li><b>川内美彦</b>토요대학 교수</li></ul></div>
      <div class="rv d3"><h4>프랑스<i>IPDF France</i></h4><ul><li><b>Olivier Bedu</b>Cabanon Vertical 디렉터</li></ul></div>
    </div>
  </div>
</section>

<section class="blk teal" id="contact">
  <div class="in cta">
    <div class="rv"><span class="label">Register and Contact</span><h2 class="d2">Join the<br><span class="it" style="color:var(--accent-light)">Forum</span></h2>
      <p class="ko-sub" style="color:rgba(255,255,255,.75);margin-top:24px">포럼 참가, 발표, 공동 개최와 협력에 관한 문의를 기다립니다.</p>
      <div class="dls"><a class="more" href="../downloads/IPDF-introduction-ko.pdf" download>소개자료 / 한국어 PDF</a><a class="more" href="../downloads/IPDF-introduction-en.pdf" download>Introduction / English PDF</a></div></div>
    <div class="rv d1"><dl><dt>Office</dt><dd>International Public Design Forum Committee<br>홍익대학교 공공디자인연구센터<br>서울시 마포구 와우산로 94, 홍문관 1310호 (04066)</dd><dt>Tel</dt><dd><a href="tel:+8223201237">+82 2 320 1237</a></dd><dt>Email</dt><dd><a href="mailto:ipdfmanager@gmail.com">ipdfmanager@gmail.com</a></dd></dl>
      <a class="btn" href="mailto:ipdfmanager@gmail.com?subject=%5BIPDF%5D%20Inquiry">이메일로 문의하기</a></div>
  </div>
</section>
</main>

<footer class="foot"><div class="in">
  <p class="big">Public Design<br><i>Together.</i></p>
  <div class="row">
    <div><img src="../images/logo-h-white.svg" alt="IPDF" width="305" height="112">국제공공디자인포럼 위원회 사무국 / 홍익대학교 공공디자인연구센터<br>R1310, 94 Wausan-ro, Mapo-gu, Seoul, Republic of Korea</div>
    <div>&copy; International Public Design Forum<br><a href="../index.html">기본 시안 보기</a></div>
  </div>
</div></footer>
<div id="gt-el" aria-hidden="true"></div>
<script src="assets/alt2.js"></script>
</body>
</html>
'''
os.makedirs(os.path.join(ROOT, 'alt2'), exist_ok=True)
open(os.path.join(ROOT, 'alt2', 'index.html'), 'w', encoding='utf-8').write(HTML)
print('built alt2/index.html')
