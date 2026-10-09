# 페이지 본문. 문장 부호: 중간점 대신 쉼표(나열)와 슬래시(성격이 다른 정보)를 쓴다.
P = 'images/photo/'
Q = 'images/poster/'


def fig(src, title, sub, cls):
    return (f'<figure class="{cls} rv" data-lb><img src="{P}{src}" alt="{title} {sub}" loading="lazy">'
            f'<figcaption><b>{title}</b>{sub}</figcaption></figure>')


def prog(groups):
    out = '<div class="prog">'
    for label, items in groups:
        out += f'<div class="grp"><span>{label}</span><ul>'
        for t, s in items:
            out += f'<li><b>{t}</b><small>{s}</small></li>' if t else f'<li><b>{s}</b></li>'
        out += '</ul></div>'
    return out + '</div>'


def facts(rows):
    return '<dl class="facts">' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows) + '</dl>'


def shots(items, cap):
    out = '<div class="shots">'
    for i, s in enumerate(items):
        wide = ' class="wide"' if s.startswith('!') else ''
        s = s.lstrip('!')
        out += f'<div{wide}><img src="{P}{s}" alt="{cap}" data-lb data-cap="{cap}" loading="lazy"></div>'
    return out + '</div>'


def event(eid, year, when, place, title, theme, body, poster, pcap, badge=''):
    b = f'<span class="badge">{badge}</span>' if badge else ''
    return f'''
<article class="event" id="{eid}" data-year="{year}">
  <div class="poster rv"><img src="{Q}{poster}" alt="{title} 포스터" data-lb data-cap="{title} 포스터" loading="lazy"><small>{pcap}</small></div>
  <div class="rv d1">
    <p class="when"><b>{when}</b> / {place}{b}</p>
    <h3>{title}</h3>
    <p class="theme">{theme}</p>
    {body}
  </div>
</article>'''


# ------------------------------------------------------------------ index
SLIDES = [
    ('f2025-stage.jpg', '<b>제5회 국제공공디자인포럼</b> / 문화역서울284 RTO, 서울 / 2025'),
    ('f2024-banner.jpg', '<b>제4회 국제공공디자인포럼</b> / 시안건축과기대학, 중국 시안 / 2024'),
    ('gk2024-group.jpg', '<b>GK 세미나 &amp; Pre-IPDF 2024</b> / GK 디자인그룹, 일본 도쿄 / 2024'),
    ('f2024-hall.jpg', '<b>제4회 국제공공디자인포럼</b> / 포럼 발표 현장 / 2024'),
]
slides = ''.join(f'<div class="slide" data-cap="{c}"><img src="{P}{s}" alt="" {"fetchpriority=high" if i == 0 else "loading=lazy"}></div>'
                 for i, (s, c) in enumerate(SLIDES))
dots = ''.join(f'<button aria-label="슬라이드 {i + 1}"></button>' for i in range(len(SLIDES)))

POSTERS = [
    ('forums.html#f2025', '2025-5th.jpg', '2025. 10. 29', '제5회 국제공공디자인포럼', '서울'),
    ('forums.html#festival2024', '2024-festival.jpg', '2024. 11. 3', '공공디자인 페스티벌 2024', '서울'),
    ('forums.html#f2024', '2024-4th.jpg', '2024. 6. 14', '제4회 국제공공디자인포럼', '중국 시안'),
    ('forums.html#pre2024', '2024-pre-ipdf.jpg', '2024. 1. 19', 'GK 세미나 &amp; Pre-IPDF', '일본 도쿄'),
    ('forums.html#cabanon2023', '2023-cabanon.jpg', '2023. 9. 19', 'PDF X Cabanon Vertical', '서울'),
    ('forums.html#f2023', '2023-3rd.jpg', '2023. 6. 12', '제3회 국제공공디자인포럼', '중국 선양'),
    ('forums.html#f2022', '2022-2nd.jpg', '2022. 12. 10', '제2회 국제공공디자인포럼', '중국, 온라인'),
    ('forums.html#korea2022', '2022-korea-edition.jpg', '2022. 10. 26', 'IPDF 코리아 에디션', '서울'),
    ('forums.html#parking2022', '2022-parkingday.jpg', '2022. 9. 16', '국제 파킹데이', '서울'),
    ('forums.html#f2021', '2021-1st.jpg', '2021. 12. 18', '제1회 국제공공디자인포럼', '서울, 온라인'),
    ('forums.html#founding', '2021-founding.jpg', '2021. 8. 28', '국제공공디자인포럼 발대식', '서울'),
]
poster_items = ''.join(
    f'<li><a href="{h}"><div class="pimg"><img src="{Q}{img}" alt="{t} 포스터" loading="lazy"></div>'
    f'<span class="pd">{d}</span><span class="pt">{t}</span><span class="pp">{pl}</span></a></li>'
    for h, img, d, t, pl in POSTERS)

GOALS = [
    ('공공편의', 'Public Convenience', [('1', 'Safety'), ('2', 'Universal'), ('3', 'Affordable')]),
    ('협력사회', 'Cooperative Society', [('4', 'Equality'), ('5', 'Network'), ('6', 'Community')]),
    ('환경지속', 'Sustainable Environment', [('7', 'Net Zero'), ('8', 'Ecology'), ('9', 'Biophilic')]),
    ('문화창조', 'Creative Culture', [('10', 'Human'), ('11', 'Diversity'), ('12', 'Impact')]),
]
goals = ''.join(
    f'<div class="col rv d{i}"><h3 class="h-item">{k}<span class="en">{e}</span></h3><ul class="ind">'
    + ''.join(f'<li><span class="n">{n}</span>{t}</li>' for n, t in ind) + '</ul></div>'
    for i, (k, e, ind) in enumerate(GOALS))

INDEX = f'''
<section class="hero" aria-label="국제공공디자인포럼 소개">
  {slides}
  <div class="hero-in"><div class="wrap">
    <span class="kicker light">International Public Design Forum</span>
    <h1 class="h-hero">사회를 위한 공공디자인,<br><span style="color:var(--accent-light)">함께하는 공공디자인</span></h1>
    <p class="lead">한국, 중국, 일본, 프랑스의 공공디자인 전문가가 모여 공공가치를 위한 국제적 연대와 교류를 만듭니다.</p>
    <div class="hero-meta"><p class="hero-cap"></p><div class="hero-dots">{dots}</div></div>
  </div></div>
</section>

<section class="sec split-bg">
  <div class="wrap">
    <div class="split">
      <div class="split-text rv">
        <span class="kicker">About IPDF</span>
        <h2 class="h-sec">공공디자인을<br><span class="em">문화적 공공재</span>로 만듭니다.</h2>
        <div class="body">
          <p>공공디자인은 공공의 이익과 안전이라는 공공가치를 추구하며 인류의 삶의 질을 높이는 디자인입니다. 국제공공디자인포럼(IPDF)은 공공환경의 다양한 문제를 찾고, 공공과 민간이 협력하는 전략으로서 공공디자인을 발전시켜 우리 삶의 문제를 해결하는 대안적 가치를 만들어 갑니다.</p>
          <p>2021년 한국, 중국, 일본 3개국으로 시작한 포럼은 2022년 프랑스가 참여하며 4개 회원국의 국제 협력 관계로 자랐습니다.</p>
        </div>
        <a class="link" href="about.html">포럼 소개</a>
      </div>
      <figure class="split-media rv d1"><img src="{P}f2021-founding-speech.jpg" alt="2021년 국제공공디자인포럼 발대식에서 인사말을 하는 모습" loading="lazy"><figcaption>국제공공디자인포럼 발대식 / 문화역서울284 / 2021</figcaption></figure>
    </div>
    <p class="statline rv" style="margin-top:clamp(64px,8vw,104px)"><span class="st">창립 <b>2021</b></span><span class="sep">I</span><span class="st">회원국 <b>4</b></span><span class="sep">I</span><span class="st">국제포럼 <b>5회</b></span><span class="sep">I</span><span class="st">개최 도시 서울, 선양, 시안, 도쿄</span><span class="sep">I</span><span class="st">핵심 지표 <b>12</b></span></p>
  </div>
</section>

<section class="sec dark on-dark">
  <div class="wrap feature">
    <div class="rv">
      <span class="kicker">Latest Forum / 2025</span>
      <span class="bar"></span>
      <p class="muted" style="font-size:15px">제5회 국제공공디자인포럼</p>
      <h2 class="h-sec">지속 가능한 도시를 위한<br>&lsquo;문화적 공공재&rsquo;</h2>
      <p class="theme-sub">공공디자인의 사회적 책임과 미래 비전</p>
      {facts([('Date', '2025년 10월 29일 수요일, 오후 2시~5시'), ('Venue', '문화역서울284 RTO, 서울 중구 통일로 1'), ('Host', '국제공공디자인포럼, 한국공간디자인단체총연합회, 한국공예디자인문화진흥원')])}
      {prog([('Keynote', [('기조발제', '김주연 / IPDF 의장, 홍익대학교 교수')]),
             ('Forum', [('&lsquo;공공디자인 거버넌스&rsquo;를 통한 사회적 가치 실현 전략', '우용호 / 사회공헌센터 소장, 한국'),
                        ('기업의 사회적 책임(S)을 디자인으로 확장하다', '김수민 / 현대자동차 ESG 매니저, 한국'),
                        ('중국의 참여형 공공디자인 정책 실행 사례', '조위지 / 노신미술대학 교수, 중국'),
                        ('사회를 위한 디자인 실험', '이즈미야마 루이 / 일본대학 교수, 일본')])])}
      <p style="margin-top:40px"><a class="link" href="forums.html#f2025">제5회 포럼 자세히 보기</a></p>
    </div>
    <img class="poster rv d2" src="{Q}2025-5th.jpg" alt="제5회 국제공공디자인포럼 2025 포스터" loading="lazy">
  </div>
</section>

<section class="sec tight">
  <div class="wrap"><div class="sec-head rv" style="margin-bottom:48px">
    <span class="kicker">Forum in Pictures</span>
    <h2 class="h-sec">서울에서 선양, 시안, 도쿄까지</h2>
  </div></div>
  <div class="full-bleed">
    <div class="mosaic">
      {fig('f2025-hall.jpg', '제5회 국제공공디자인포럼', '서울 / 2025', 'c8 r2')}
      {fig('f2025-poster-stand.jpg', '포럼 현장', '문화역서울284 RTO / 2025', 'c4 r2')}
      {fig('f2024-group.jpg', '제4회 국제공공디자인포럼', '중국 시안 / 2024', 'c4 r2')}
      {fig('f2024-audience.jpg', '토론 현장', '시안건축과기대학 / 2024', 'c4 r2')}
      {fig('gk2024-seminar.jpg', 'GK 세미나 &amp; Pre-IPDF', '일본 도쿄 / 2024', 'c4 r2')}
      {fig('cab2023-talk.jpg', 'PDF X Cabanon Vertical', '홍익대학교 / 2023', 'c5 r2')}
      {fig('china-group.jpg', '국제 교류 포럼', '중국', 'c7 r2')}
    </div>
  </div>
  <div class="wrap" style="margin-top:36px"><a class="link" href="gallery.html">갤러리 전체 보기</a></div>
</section>

<section class="sec gray">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Vision and Plans</span>
      <h2 class="h-sec">4개 목표와 <span class="em">12개 핵심 지표</span></h2>
      <p class="lead">국제사회가 함께 정한 지속가능발전목표(SDGs)를 바탕으로 사회, 공동체, 환경, 삶, 문화의 문제에 대한 대안을 찾고 디자인으로 해결합니다.</p>
    </div>
    <div class="cols cols-4">{goals}</div>
    <p style="margin-top:56px" class="rv"><a class="link" href="vision.html">비전과 계획</a></p>
  </div>
</section>

<section class="sec" data-strip>
  <div class="wrap strip-ctrl" style="margin-bottom:44px">
    <div class="rv"><span class="kicker">History</span><h2 class="h-sec">2021년부터 이어 온 발자취</h2></div>
    <div class="strip-btns"><button data-dir="-1" aria-label="이전 포스터">‹</button><button data-dir="1" aria-label="다음 포스터">›</button></div>
  </div>
  <div class="strip-wrap"><ul class="posters">{poster_items}</ul></div>
  <div class="wrap" style="margin-top:28px"><a class="link" href="forums.html">포럼 아카이브</a></div>
</section>

<section class="sec gray">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Network</span>
      <h2 class="h-sec">네 나라가 함께 만드는 포럼</h2>
      <p class="lead">각국의 대학, 연구기관, 디자인 기업, 공공기관이 포럼을 함께 주최하고 운영합니다.</p>
    </div>
    <div class="cols cols-4 net">
      <div class="rv"><p class="country">한국<span class="en">IPDF Korea</span></p><ul><li>홍익대학교 공공디자인연구센터<small>사무국</small></li><li>한국공예디자인문화진흥원</li><li>한국공간디자인단체총연합회</li><li>문화역서울284</li></ul></div>
      <div class="rv d1"><p class="country">중국<span class="en">IPDF China</span></p><ul><li>노신미술대학<small>Lu Xun Academy of Fine Arts</small></li><li>칭화대학 미술학원</li><li>중앙미술학원</li><li>시안건축과기대학</li><li>닝보대학</li></ul></div>
      <div class="rv d2"><p class="country">일본<span class="en">IPDF Japan</span></p><ul><li>토요대학<small>Toyo University</small></li><li>GK 디자인그룹</li><li>가고시마대학</li><li>나고야대학</li><li>일본대학</li></ul></div>
      <div class="rv d3"><p class="country">프랑스<span class="en">IPDF France</span></p><ul><li>Cabanon Vertical<small>2022년 참여</small></li><li>주한 프랑스 대사관 문화과</li></ul></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap quote rv">
    <span class="bar"></span>
    <p>우리는 공공디자인의 방향을 제시하고<br><strong>공공디자인 문화를 창조한다.</strong></p>
    <cite>국제공공디자인포럼 헌장 가운데</cite>
  </div>
</section>

<section class="sec dark on-dark">
  <div class="wrap contact">
    <div class="rv">
      <span class="kicker">Join Us</span>
      <h2 class="h-sec" style="font-size:clamp(30px,3.6vw,44px)">공공디자인으로 더 좋은 세상을 만드는 발걸음에 함께해 주십시오.</h2>
    </div>
    <div class="rv d1">
      <dl><dt>Email</dt><dd><a href="mailto:ipdfmanager@gmail.com">ipdfmanager@gmail.com</a></dd><dt>Tel</dt><dd><a href="tel:+8223201237">+82 2 320 1237</a></dd><dt>Office</dt><dd>홍익대학교 공공디자인연구센터<br>서울시 마포구 와우산로 94, 홍문관 1310호</dd></dl>
      <p style="margin-top:32px"><a class="btn" href="about.html#contact">참가 문의</a></p>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------------ about
CHARTER = [
    ('우리는 공공의 이익과 안전의 공공가치를 추구한다.', 'We pursue public value, championing the benefit and safety inherent in public design.'),
    ('우리는 디자인을 통해 인류의 삶의 질 향상에 기여한다.', 'We contribute to the improvement of the quality of human life through design.'),
    ('우리는 공공의 문제를 해결하기 위한 디자인을 통한 협력과 전략을 발전시킨다.', 'We develop design strategies and collaborations to deal with the issues of the public.'),
    ('우리는 공공가치를 실현하는 다양한 연구와 실천을 위한 방안을 협력한다.', 'We collaborate on diverse research and practice aimed at realizing public values.'),
    ('우리는 공공디자인의 방향을 제시하고 공공디자인 문화를 창조한다.', 'We provide strategic direction and cultivate a culture of public design.'),
]
charter = ''.join(f'<li class="rv"><span>하나.</span><div>{k}<em>{e}</em></div></li>' for k, e in CHARTER)

ABOUT = f'''
<section class="phero">
  <img src="{P}f2024-outdoor.jpg" alt="제4회 국제공공디자인포럼 참가자 단체 사진, 중국 시안">
  <div class="wrap">
    <span class="kicker light">About IPDF</span>
    <h1 class="h-hero">포럼 소개</h1>
    <p class="lead">공공의 이익과 안전, 배려, 편의, 품격의 가치를 디자인으로 실현하는 국제 협력의 장입니다.</p>
  </div>
  <span class="cap">제4회 국제공공디자인포럼 / 중국 시안 / 2024</span>
</section>

<section class="sec" id="greeting">
  <div class="wrap portrait">
    <figure class="rv"><img src="{P}chair.jpg" alt="국제공공디자인포럼 의장 김주연" loading="lazy"></figure>
    <div class="rv d1">
      <span class="kicker">Greeting</span>
      <h2 class="h-sec" style="margin-bottom:32px">인사말</h2>
      <div class="body lead">
        <p>안녕하십니까. 국제공공디자인포럼 의장 김주연입니다. 국제공공디자인포럼과 함께하는 모든 분께 깊은 감사의 말씀을 드립니다.</p>
        <p>2021년 발대식을 시작으로 5년 차에 접어든 국제공공디자인포럼은 한국을 비롯한 일본, 중국, 프랑스 등 여러 나라와 공공가치 실현을 위한 국제적 연대와 교류를 펼치고 있습니다.</p>
        <p>많은 변화가 일고 있는 현대 사회에서 공공디자인은 디자인의 선한 영향력을 넓히기 위해 노력하고 있습니다. 국제공공디자인포럼은 지속 가능한 세계를 위한 국제 사회와의 협력을 이어 가겠습니다.</p>
        <p>공공디자인을 통해 더 좋은 세상을 만들기 위한 우리의 발걸음에 함께해 주시기 바랍니다. 감사합니다.</p>
      </div>
      <p class="sign">국제공공디자인포럼 의장<b>김주연</b></p>
    </div>
  </div>
</section>

<section class="sec gray" id="intro">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Introduction</span>
      <h2 class="h-sec">사회를 위한 공공디자인,<br><span class="em">함께하는 공공디자인</span></h2>
    </div>
    <div class="cols cols-2 body">
      <div class="rv"><p>공공디자인은 공공의 이익과 안전의 공공가치를 추구하며 인류의 삶의 질을 높이는 데 기여하는 디자인입니다. 공공디자인은 도시의 삶의 질을 높이고 지속 가능한 도시를 만드는 데 기여합니다. 국제공공디자인포럼은 공공환경의 다양한 문제를 찾고, 공공과 민간의 협력을 위한 전략으로서 공공디자인을 발전시켜 우리 삶의 문제를 해결하는 대안적 가치를 지닌 문화적 공공재가 되고자 합니다.</p>
      <p>이를 바탕으로 포럼은 안전, 배려, 편의, 품격의 공공디자인 가치를 추구하고 국제적 협력 관계를 넓혀 가고 있습니다. 2021년 한국, 중국, 일본 3개국으로 시작한 포럼은 2022년 프랑스의 참가로 현재 4개 회원국의 국제 협력 관계를 이어 오고 있습니다.</p></div>
      <div class="rv d1"><p>국제공공디자인포럼은 공공디자인의 방향을 제시하고, 나아가 공공디자인 문화를 위한 협력의 기초를 마련합니다. 국제적 공공디자인 문화를 창조하는 거점으로서 다양한 매체와 프로그램을 통해 공공디자인의 지식과 지혜를 나누며 사회적 가치를 높이는 데 공헌하고 있습니다.</p>
      <p>공공디자인의 국제적 문화 확산과 미래 비전을 제시하는 자리에 함께해 주셔서 감사합니다.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="founding">
  <div class="wrap split rev">
    <figure class="split-media rv"><img src="{P}f2021-founding-1.jpg" alt="2021년 국제공공디자인포럼 발대식 현장, 문화역서울284" loading="lazy"><figcaption>국제공공디자인포럼 발대식 / 문화역서울284 / 2021. 8. 28</figcaption></figure>
    <div class="split-text rv d1">
      <span class="kicker">Founding Statement</span>
      <h2 class="h-sec">발기문</h2>
      <div class="body">
        <p>한국, 중국, 일본 3개국의 공공디자인 전문가들은 공공디자인을 통해 공공가치를 실현하는 다양한 연구와 실천으로 삶의 질 향상과 지속 가능한 도시를 만드는 데 기여하기 위해 뜻을 모았습니다.</p>
        <p>안전, 배려, 편의, 품격의 공공가치를 공공디자인을 통해 추구하고, 국제적 협력 관계로 공공디자인을 확산하고 발전시키고자 &lsquo;국제공공디자인포럼&rsquo;을 창립합니다. 포럼은 공공디자인의 방향을 제시하고 국제적 공공디자인 문화를 창조하는 시작점이 될 것입니다.</p>
      </div>
      <p class="sign" style="margin-top:28px">2021년 8월 28일<b style="font-size:18px">국제공공디자인포럼 발기인 일동</b></p>
    </div>
  </div>
</section>

<section class="sec deep on-dark" id="charter">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Mission of IPDF</span>
      <h2 class="h-sec">국제공공디자인포럼 헌장</h2>
      <p class="lead">국제공공디자인포럼은 국제사회의 공공가치를 추구하기 위한 교류의 장으로서, 인류의 삶의 질 향상과 공공환경의 다양한 문제를 해결하기 위해 최선을 다하며 다음 원칙을 지킵니다.</p>
    </div>
    <ol class="charter">{charter}</ol>
    <p class="muted rv" style="margin-top:56px;font-size:15px">이와 같은 목표를 이루기 위해 헌장을 정하고 성실히 수행할 것을 굳게 다짐합니다. / 국제공공디자인포럼 위원회 일동</p>
  </div>
</section>

<section class="sec" id="organization">
  <div class="wrap">
    <div class="split">
      <div class="split-text rv">
        <span class="kicker">Organization</span>
        <h2 class="h-sec">With, By, For<br><span class="em">Public Design</span></h2>
        <div class="body"><p>국제공공디자인포럼은 IPDF Korea, IPDF China, IPDF Japan을 중심으로 운영하며, 2022년부터 프랑스가 함께합니다. 각국 위원과 전문가가 긴밀히 교류하며 외교, 문화, 교육, 학술 분야의 세부 사업을 추진하고 공유합니다.</p>
        <p>사무국은 홍익대학교 공공디자인연구센터에 있습니다.</p></div>
      </div>
      <figure class="split-media rv d1"><img src="{P}org-map.jpg" alt="IPDF 조직도: IPDF Korea, IPDF China, IPDF Japan" loading="lazy" style="aspect-ratio:auto"><figcaption>International Public Design Forum Organization</figcaption></figure>
    </div>
  </div>
</section>

<section class="sec gray" id="people">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Founders and Committee</span>
      <h2 class="h-sec">발기인과 위원</h2>
      <p class="lead">포럼을 함께 시작하고 이끌어 온 각국의 발기인과 위원입니다.</p>
    </div>
    <div class="rows">
      <div class="row rv"><div class="lab">한국 / Korea</div><div class="val"><ul class="people">
        <li><b>김주연</b><span class="en">Jooyun Kim</span><span>IPDF 의장 / 홍익대학교 교수, 공공디자인연구센터 소장</span></li>
        <li><b>이현성</b><span class="en">Hyunsung Lee</span><span>자문위원 / 홍익대학교 공공디자인전공 교수</span></li>
        <li><b>김상아</b><span>사무총장 / 홍익대학교 공공디자인연구센터</span></li>
        <li><b>홍태의</b><span>책임연구원 / 홍익대학교 공공디자인연구센터</span></li>
        <li><b>엄지연</b><span>위원 / 이오디 디자인 연구소 대표</span></li>
      </ul></div></div>
      <div class="row rv"><div class="lab">중국 / China</div><div class="val"><ul class="people">
        <li><b>강민</b><span class="en">Jiang Min</span><span>노신미술대학 건축예술디자인학원 교수</span></li>
        <li><b>조덕리</b><span>노신미술대학 건축예술디자인학원</span></li>
        <li><b>주가혜</b><span>노신미술대학 교수</span></li>
      </ul></div></div>
      <div class="row rv"><div class="lab">일본 / Japan</div><div class="val"><ul class="people">
        <li><b>高橋儀平</b><span class="en">Gihei Takahashi</span><span>토요대학 명예교수</span></li>
        <li><b>菅原麻衣子</b><span class="en">Maiko Sugawara</span><span>토요대학 교수</span></li>
        <li><b>川内美彦</b><span class="en">Yoshihiko Kawauchi</span><span>토요대학 교수</span></li>
      </ul></div></div>
      <div class="row rv"><div class="lab">프랑스 / France</div><div class="val"><ul class="people">
        <li><b>Olivier Bedu</b><span class="en">올리비에 브뒤</span><span>Cabanon Vertical 디렉터</span></li>
      </ul></div></div>
    </div>
  </div>
</section>

<section class="sec dark on-dark" id="contact">
  <div class="wrap contact">
    <div class="rv">
      <span class="kicker">Register and Contact</span>
      <h2 class="h-sec">문의 및 참가 신청</h2>
      <p class="lead" style="margin-top:22px">포럼 참가, 발표, 공동 개최와 협력에 관한 문의를 기다립니다.</p>
      <div class="dl-list">
        <a class="link" href="downloads/IPDF-introduction-ko.pdf" download>IPDF 소개자료 다운로드 / 한국어 PDF</a>
        <a class="link" href="downloads/IPDF-introduction-en.pdf" download>IPDF Introduction / English PDF</a>
      </div>
    </div>
    <div class="rv d1">
      <dl><dt>Office</dt><dd>International Public Design Forum Committee<br>서울시 마포구 와우산로 94, 홍문관 1310호 (04066)<br><span class="muted">R1310, 94 Wausan-ro, Mapo-gu, Seoul, Republic of Korea</span></dd>
      <dt>Tel</dt><dd><a href="tel:+8223201237">+82 2 320 1237</a></dd>
      <dt>Email</dt><dd><a href="mailto:ipdfmanager@gmail.com">ipdfmanager@gmail.com</a></dd></dl>
      <p style="margin-top:32px"><a class="btn" href="mailto:ipdfmanager@gmail.com?subject=%5BIPDF%5D%20%EC%B0%B8%EA%B0%80%20%EB%AC%B8%EC%9D%98">이메일로 문의하기</a></p>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------------ vision
DOMAINS = [
    ('Part of Diplomacy', '외교 분야', '국제 공공디자인 연합 포럼 개최', '매년 한 차례 회원국을 돌며 국제공공디자인포럼을 엽니다. 서울, 선양, 시안, 도쿄에서 각국 전문가가 공공디자인의 의미와 가능성을 논의해 왔습니다.', 'f2024-hall2.jpg', '제4회 국제공공디자인포럼 / 중국 시안 / 2024'),
    ('Part of Culture', '문화 분야', '공공디자인 문화 운동 실천', '국제 파킹데이, 공공디자인 페스티벌처럼 시민이 직접 공공공간을 경험하는 문화 운동으로 공공디자인의 가치를 넓힙니다.', 'parkingday-2022.jpg', '국제 파킹데이 / 서울 / 2022'),
    ('Part of Education', '교육 분야', '공공디자인 교육 프로그램 운영', '세미나와 특강, 워크숍을 통해 다음 세대 공공디자이너와 연구자를 기르고 각국의 사례와 방법론을 나눕니다.', 'sem-2.jpg', 'IPDF 세미나 / 홍익대학교 공공디자인연구센터'),
    ('Part of Academic', '학술 분야', '국제 공공디자인 교류전 개최', '연구 성과와 프로젝트를 교류전과 자료집으로 공유하고, 공공디자인의 학술적 기반을 함께 다집니다.', 'china-hall.jpg', '국제 공공디자인 교류 / 중국'),
]
domains = ''.join(f'''
<div class="split{' rev' if i % 2 else ''}" style="margin-top:{0 if i == 0 else 'clamp(72px,9vw,128px)'}">
  <figure class="split-media rv"><img src="{P}{img}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>
  <div class="split-text rv d1"><span class="kicker">{en}</span><h3 class="h-sec" style="font-size:clamp(28px,3.4vw,42px)">{ko}</h3><p class="h-sub" style="font-size:20px;color:var(--accent);margin:-8px 0 16px">{what}</p><div class="body"><p>{desc}</p></div></div>
</div>''' for i, (en, ko, what, desc, img, cap) in enumerate(DOMAINS))

VALUES1 = [
    ('공공안전', 'Public Safety', '유무형 가치의 개선을 통한 안전 증대', '안전한 도시만들기 국제세미나', '안전한 도시를 만들기 위한 연합 세미나', '#CPTED #범죄예방디자인 #공공안전디자인'),
    ('공공배려', 'Public Inclusiveness', '모두를 위한 사용자 중심의 배려', '더 나은 세상을 위한 공유공간 만들기', '국제 네트워크 봉사, 개발도상국 공공환경 개선', '#UD #BarrierFree #포용사회 #초세대놀이터'),
    ('공공협력', 'Public Cooperation', '협력 체계 구성을 통한 사회문제 해결', '콜렉티브 임팩트 국제캠프', '국제 리더 그룹과 시민의 소통, 해커톤을 통한 문제 해결', '#협력적거버넌스 #네트워크 #커뮤니티 #콜렉티브임팩트'),
    ('공공편의', 'Public Convenience', '모두의 편의를 위한 개선 방안', '길찾기 쉬운 아시아', '읽기 쉽고 걷기 편한 아시아 연합 안내체계 디자인 개발', '#InclusiveDesign #Legible #생활SOC'),
]
VALUES2 = [
    ('공공품격', 'Public Dignity', '도시 이미지와 환경 개선', '아시안 도시브랜드 시상식', '아시아 곳곳의 도시가 가진 공공가치를 찾아 수여하는 시상식', '#공공미술 #도시브랜드디자인 #환경개선'),
    ('공공소통', 'Public Communication', '참여를 통한 공공가치 실현과 문제 발견, 해결', '공공디자인 콘텐츠', '더 좋은 사회를 만들기 위한 영상 콘텐츠 공모전', '#거버넌스 #시민참여'),
    ('공공혁신', 'Public Innovation', '새롭고 다양한 시도를 통한 개선과 변화', '사회혁신을 위한 글로벌 타운', '현장에 머물며 문제를 발굴하고 해결 모델을 개발', '#사회혁신 #리빙랩 #플랫폼'),
    ('공공서비스', 'Public Service', '공공영역의 편의와 문제 개선을 위한 프로세스와 계획', '모두를 위한 기초자료 공유', '인지, 행동심리 관측과 비교 분석을 위한 교류의 장', '#공공서비스디자인 #UX #UI #넛지디자인'),
]


def values(vs):
    return '<div class="cols cols-4">' + ''.join(
        f'<div class="col rv d{i}"><h4 class="h-item">{k}<span class="en">{e}</span></h4><p>{d}</p>'
        f'<p style="margin-top:18px;color:var(--ink);font-weight:700;font-size:16px"><span class="sq"></span>{proj}</p><p style="font-size:15px">{pd}</p>'
        f'<p class="tags">{t}</p></div>' for i, (k, e, d, proj, pd, t) in enumerate(vs)) + '</div>'


VISION = f'''
<section class="phero">
  <img src="{P}f2024-hall.jpg" alt="제4회 국제공공디자인포럼 강당">
  <div class="wrap">
    <span class="kicker light">Vision and Plans</span>
    <h1 class="h-hero">비전과 계획</h1>
    <p class="lead">공공의 이익, 협력적 사회, 지속 가능한 환경, 문화적 창조를 목표로 디자인을 통한 공공가치를 실현합니다.</p>
  </div>
  <span class="cap">제4회 국제공공디자인포럼 / 중국 시안 / 2024</span>
</section>

<section class="sec" id="goals">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">IPDF Goals for Pursuing Public Values</span>
      <h2 class="h-sec">공공가치 추구를 위한<br><span class="em">4개 목표, 12개 핵심 지표</span></h2>
      <p class="lead">국제공공디자인포럼은 국제사회가 함께 정한 지속가능발전목표(SDGs)를 바탕으로 사회, 공동체, 환경, 삶, 문화 분야에서 우리가 마주한 문제의 대안을 함께 찾고 디자인으로 해결하고자 합니다. &lsquo;사회를 위한 공공디자인, 함께하는 공공디자인&rsquo;을 의제로 4개 목표와 12개 핵심 지표를 세우고 공공의 삶의 질 향상을 위해 노력합니다.</p>
    </div>
    <div class="cols cols-4">{goals}</div>
  </div>
</section>

<section class="sec gray" id="domains">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Four Fields of Activity</span>
      <h2 class="h-sec">외교, 문화, 교육, 학술 분야의<br>비영리 활동</h2>
      <p class="lead">거버넌스, 연구와 실천, 문화 창조, 삶의 질 증대, 공익 추구를 가치로 삼아 네 분야에서 활동합니다.</p>
    </div>
    {domains}
  </div>
</section>

<section class="sec" id="values">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="kicker">Public Design for Society</span>
      <h2 class="h-sec">사회를 위한 공공디자인</h2>
      <p class="lead">공공안전, 공공배려, 공공협력, 공공편의의 가치와 이를 실현하는 국제 프로젝트입니다.</p>
    </div>
    {values(VALUES1)}
    <div class="sec-head rv" style="margin-top:clamp(96px,11vw,150px)">
      <span class="kicker">Public Design Together</span>
      <h2 class="h-sec">함께하는 공공디자인</h2>
      <p class="lead">공공품격, 공공소통, 공공혁신, 공공서비스의 가치와 이를 실현하는 국제 프로젝트입니다.</p>
    </div>
    {values(VALUES2)}
  </div>
</section>

<section class="sec dark on-dark">
  <div class="wrap quote rv">
    <span class="bar"></span>
    <p>공공디자인은 세계 곳곳에서 새로운 문화를 창조하고<br><strong>인류의 삶의 질을 높이는 중추적인 역할</strong>을 해 나갈 것입니다.</p>
    <cite>제1회 국제공공디자인포럼 개회사 가운데 / 2021</cite>
  </div>
</section>
'''

# ------------------------------------------------------------------ forums (archive)
E = []
E.append(('2025', event('f2025', '2025', '2025. 10. 29', '서울, 문화역서울284 RTO', '제5회 국제공공디자인포럼',
    '지속 가능한 도시를 위한 &lsquo;문화적 공공재&rsquo;<small>공공디자인의 사회적 책임과 미래 비전</small>',
    '<p class="desc">창립 5주년을 맞아 서울에서 열린 포럼입니다. 공공디자인 거버넌스, 기업의 사회적 책임, 참여형 정책을 통해 공공디자인이 도시의 문화적 공공재가 되는 길을 한국, 중국, 일본 연사와 함께 논의했습니다.</p>'
    + facts([('Date', '2025년 10월 29일 수요일, 오후 2시~5시'), ('Venue', '문화역서울284 RTO, 서울 중구 통일로 1'),
             ('Host', '국제공공디자인포럼, 한국공간디자인단체총연합회, 한국공예디자인문화진흥원'),
             ('Organizer', '홍익대학교 공공디자인연구센터, 노신미술대학 건축예술디자인학원 도시재생 및 문화전승 국제교류센터'),
             ('Support', '문화역서울284(장소), 사회공헌센터')])
    + prog([('Keynote', [('기조발제', '김주연 / IPDF 의장, 홍익대학교 교수')]),
            ('Forum', [('&lsquo;공공디자인 거버넌스&rsquo;를 통한 사회적 가치 실현 전략', '우용호 / 사회공헌센터 소장, 한국'),
                       ('기업의 사회적 책임(S)을 디자인으로 확장하다', '김수민 / 현대자동차 ESG 매니저, 한국'),
                       ('중국의 참여형 공공디자인 정책 실행 사례', '조위지 / 노신미술대학 교수, 중국'),
                       ('사회를 위한 디자인 실험', '이즈미야마 루이 / 일본대학 교수, 일본')]),
            ('Seminar', [('소셜벤처와 공공디자인의 역량 강화', '이지영 / 홍익대학교 공공디자인연구센터 연구원'),
                         ('시민 편의성 향상을 위한 중국의 공공디자인', '주가혜 / 노신미술대학 교수'),
                         ('참여를 통한 포용적 소통 공간디자인', '추민아 / 비들 대표')])])
    + shots(['!f2025-stage.jpg', 'f2025-poster-stand.jpg', 'f2025-keynote.jpg', 'f2025-hall.jpg', 'f2025-audience.jpg'], '제5회 국제공공디자인포럼 / 서울 / 2025'),
    '2025-5th.jpg', '포스터 / 2025')))

E.append(('2024', event('festival2024', '2024', '2024. 11. 3', '서울, 문화역서울284 RTO', '공공디자인 페스티벌 2024 / 공공디자인 데이',
    '함께 하실래요?<small>Public Design Day After Party / 사람을 위한 공공공간 디자인</small>',
    '<p class="desc">공공디자인 페스티벌 2024와 함께 열린 공공디자인 데이 프로그램입니다. 공공가치 확산을 위한 참여 프로젝트로 시민과 전문가가 사람을 위한 공공공간을 함께 이야기했습니다.</p>'
    + facts([('Date', '2024년 11월 3일, 오후 2시~5시 30분'), ('Venue', '문화역서울284 RTO'),
             ('Organizer', '홍익대학교 공공디자인연구센터, 국제공공디자인포럼'), ('Support', '한국공예디자인문화진흥원')]),
    '2024-festival.jpg', '포스터 / 2024')))

E.append(('2024', event('f2024', '2024', '2024. 6. 14', '중국 시안, 시안건축과기대학', '제4회 국제공공디자인포럼',
    '도시를 위한 공공디자인<small>Public Design for the City</small>',
    '<p class="desc">시안건축과기대학에서 열린 네 번째 포럼입니다. 시대가 요구하는 가치를 공공디자인으로 구현하는 새로운 방법을 찾고, 아시아 3국에서 공공디자인을 확산하기 위한 기반을 마련했습니다.</p>'
    + facts([('Date', '2024년 6월 14일 금요일, 오전 9시 30분~오후 4시 30분'), ('Venue', '시안건축과기대학, 중국 시안'),
             ('Host', '국제공공디자인포럼'), ('Organizer', '홍익대학교 공공디자인연구센터, 노신미술대학 도시재생 및 문화전승 국제교류센터, 시안건축과기대학'),
             ('Support', '한국공예디자인문화진흥원')])
    + prog([('Keynote', [('기조발제', '인보강 / 시안건축과기대학 예술학원 원장, 중국'), ('기조발제', '김주연 / IPDF 의장, 홍익대학교, 한국')]),
            ('Forum', [('관람은 표현에 앞선다: 공공예술과 도시 갱신', '한유봉 / 시안건축과기대학 예술학원, 중국'),
                       ('Design X: Socio-Value and Effect', '이현성 / 홍익대학교 산업미술대학원, 한국'),
                       ('일본의 토탈디자인 사례', '엄지연 / 이오디 디자인 연구소, 일본')]),
            ('Seminar', [('도시 조각의 치유 기능', '진정이 / 시안건축과기대학'), ('가치를 만드는 디자인', '홍태의 / 홍익대학교 공공디자인연구센터'),
                         ('사회적 처방과 공공서비스 디자인', '주하나 / PSDI 심리사회 디자인연구소'),
                         ('도시 환경에서 빨간색 테마 조각 디자인과 적용', '임자겸 / 시안건축과기대학')])])
    + '<p class="pull">&ldquo;공공디자인이 한국을 넘어 아시아 디자인의 리더로 자리매김할 수 있도록, 더욱 활발한 국제 교류로 공공디자인의 가치를 전파하겠습니다.&rdquo;<small>김주연 IPDF 의장</small></p>'
    + shots(['!f2024-banner.jpg', 'f2024-designx.jpg', 'f2024-group.jpg', 'f2024-hall.jpg', 'f2024-panel.jpg'], '제4회 국제공공디자인포럼 / 중국 시안 / 2024'),
    '2024-4th.jpg', '포스터 / 2024')))

E.append(('2024', event('tachikawa2024', '2024', '2024. 5. 24', '서울, 홍익대학교', 'The Public Design Forum 2024',
    '디자인을 위한 진화사고<small>Evolutional Creativity for Public Design</small>',
    '<p class="desc">NOSIGNER 대표이자 세계디자인기구(WDO) 이사, 일본산업디자인협회(JIDA) 이사장인 에이스케 타치카와를 초청한 특강입니다.</p>'
    + facts([('Date', '2024년 5월 24일 금요일, 오후 4시~6시'), ('Venue', '홍익대학교 제1공학관(K동) 101호'),
             ('Speaker', 'Eisuke Tachikawa / NOSIGNER 대표, WDO 이사, JIDA 이사장'),
             ('Host', '홍익대학교 산업디자인전공, 공공디자인전공, 공공디자인연구센터')]),
    '2024-tachikawa.jpg', '포스터 / 2024', 'Related Program')))

E.append(('2024', event('pre2024', '2024', '2024. 1. 19', '일본 도쿄, GK 디자인그룹', 'GK 세미나 &amp; Pre-IPDF 2024',
    '도시디자인을 통한 공공가치 실현<small>Realizing Public Value through Urban Design</small>',
    '<p class="desc">한국, 중국, 일본의 전문가가 일본 도쿄의 GK 디자인그룹에 모여 공공과 도시의 변화를 만드는 3국의 디자인 프로젝트를 공유했습니다. 제4회 포럼을 준비하는 사전 세미나로 21명이 참석했습니다.</p>'
    + facts([('Date', '2024년 1월 19일 금요일, 오전 10시~12시'), ('Venue', 'GK 디자인그룹 P룸, 일본 도쿄'),
             ('Host', 'GK 디자인그룹, 국제공공디자인포럼, 홍익대학교 공공디자인연구센터, 노신미술대학 국제교류센터, 시안건축과기대학')])
    + prog([('Greeting', [('인사말', '다나카 / GK 디자인그룹 회장'), ('인사말', '김주연 / 홍익대학교 교수')]),
            ('Talk', [('일본 토탈디자인 사례: 우쓰노미야 LRT를 중심으로', '이리에 / GK 디자인그룹 전무, 일본'),
                      ('Urban Design Tomorrow: Insights from Suwon and Incheon', '고은정 / 전 인천광역시 도시디자인과장, 한국'),
                      ('중국 도시 설계 프로젝트의 전형적 사례: 시안 대당불야성', '민신러 / 시안건축과기대학, 중국')])])
    + shots(['!gk2024-group.jpg', 'gk2024-seminar.jpg'], 'GK 세미나 &amp; Pre-IPDF / 일본 도쿄 / 2024'),
    '2024-pre-ipdf.jpg', '포스터 / 2024')))

E.append(('2023', event('cabanon2023', '2023', '2023. 9. 19', '서울, 홍익대학교 공공디자인연구센터', 'PDF X Cabanon Vertical',
    '프랑스 공공디자인 거버넌스<small>Public Design Governance in France</small>',
    '<p class="desc">프랑스 회원 Cabanon Vertical과 함께한 특강입니다. 프랑스의 참여형 어바니즘 접근법과 &lsquo;프랑스의 도시를 만드는 사람들&rsquo;에 관한 이야기를 나눴습니다.</p>'
    + facts([('Date', '2023년 9월 19일 화요일, 오후 7시~8시 30분'), ('Venue', '홍익대학교 홍문관 1310호 공공디자인연구센터'),
             ('Host', '홍익대학교 공공디자인전공, 공공디자인연구센터'), ('Support', '주한 프랑스 대사관 문화과, 프랑스 문화원')])
    + prog([('Talk', [('프랑스의 도시를 만드는 사람들', '추민아 / 비들 대표, 전 Cabanon Vertical 디자이너'),
                      ('프랑스 참여형 어바니즘 접근법', '올리비에 브뒤 / Cabanon Vertical 디렉터'),
                      ('토론: 트랜지셔널 어바니즘', '김상아 / 홍익대학교 공공디자인연구센터')])])
    + shots(['!cab2023-hall.jpg', 'cab2023-book.jpg', 'cab2023-talk.jpg', 'cab2023-room.jpg', 'cab2023-night.jpg'], 'PDF X Cabanon Vertical / 서울 / 2023'),
    '2023-cabanon.jpg', '포스터 / 2023')))

E.append(('2023', event('loud2023', '2023', '2023. 7. 21', '서울, 서소문성지 역사박물관', 'The Public Design Forum X LOUD',
    '사회갈등 예방을 위한 디자인 Vol. 1<small>Public Design for Preventing Social Conflict</small>',
    '<p class="desc">공공소통 관점에서 사회갈등을 찾고, 공공디자인 차원에서 문제를 해결하는 방법을 공공소통연구소 LOUD와 함께 논의했습니다.</p>'
    + facts([('Date', '2023년 7월 21일 금요일, 오후 3시~5시'), ('Venue', '서소문성지 역사박물관 지하 1층 명례방')])
    + prog([('Talk', [('공공소통 관점에서 찾는 사회적 소통 과제', '이종혁 / 광운대학교 교수, 공공소통연구소 LOUD 소장'),
                      ('강남역 토끼굴 흡연 문제 해결 공공디자인 실험실', '이미정 / 강남구청 공공디자인 팀장'),
                      ('사회갈등 예방을 위한 흡연부스 디자인', '문현배 / SEDG 공공디자이너')])]),
    '2023-pdfx-loud.jpg', '포스터 / 2023', 'Related Program')))

E.append(('2023', event('f2023', '2023', '2023. 6. 12', '중국 선양, 노신미술대학', '제3회 국제공공디자인포럼',
    '도시재생과 공공디자인<small>Urban Regeneration and Public Design</small>',
    '<p class="desc">노신미술대학 건축예술디자인대학 학술강당에서 온라인과 오프라인으로 동시에 열린 세 번째 포럼입니다. 도시재생 시대에 공공디자인과 공공미술이 맡을 역할을 논의했습니다.</p>'
    + facts([('Date', '2023년 6월 12일 월요일, 오후 1시~4시'), ('Venue', '노신미술대학 건축예술디자인대학 학술강당, 중국 선양'),
             ('Partner', '노신미술대학, 홍익대학교, 중앙미술학원, 선양항공항천대학, 사천미술학원')])
    + prog([('Talk', [('공공디자인의 시대', '김주연 / 홍익대학교 교수, 공공디자인연구센터 소장, 한국'),
                      ('공공을 위한 디자인', '이현성 / 홍익대학교 공공디자인전공 교수, 한국'),
                      ('공공미술의 공간연출', 'Zhou Yufang / 중앙미술학원 건축학원 부원장, 중국')])])
    + f'<div class="shots"><div><img src="{Q}2023-3rd-cn.jpg" alt="제3회 포럼 중국어 포스터" data-lb data-cap="제3회 국제공공디자인포럼 중국어 포스터" loading="lazy" style="aspect-ratio:1/1.414;object-position:top"></div></div>',
    '2023-3rd.jpg', '포스터 / 2023')))

E.append(('2022', event('f2022', '2022', '2022. 12. 10', '중국 선양, 온라인 생중계', '제2회 국제공공디자인포럼',
    '도시재생과 공공디자인<small>도시를 재생하고, 지속 가능하게 하는 공공디자인</small>',
    '<p class="desc">사람을 중심에 둔 도시재생은 도시가 지닌 잠재력과 자생력을 키웁니다. 중국, 한국, 일본, 프랑스가 경험하고 지향하는 &lsquo;공공디자인을 통한 도시재생의 의미와 가능성&rsquo;을 논의했습니다. 노신미술대학이 주관하고 VooV, Bilibili, Zoom, YouTube로 생중계했으며 영어 동시통역을 제공했습니다.</p>'
    + facts([('Venue', '노신미술대학, 온라인 생중계'), ('Academic Chair', '강민 / 노신미술대학')])
    + prog([('Talk', [('현대 공공디자인 속의 환경의식', '소단 / 중국공예미술관 부관장'),
                      ('미래 생활유산을 통한 지역재생', '권영재 / 상지대학교 교수, 한국'),
                      ('시각디자인과 미디어의 미래 비전', '조로 / 노신미술대학 부원장'),
                      ('공중 건강을 위한 디자인', '조초 / 칭화대학 미술학원 부원장'),
                      ('제3의 공간과 관계자본의 힘', '황석연 / 행정안전부 시민협업팀장, 한국'),
                      ('노신미술대학 캠퍼스 재생 15년', '양엽 / 선양 푸순 개혁혁신시범구 관리위원회'),
                      ('도시, 디자인, 실천', '上田孝明 / NAD Nikken Activity Design Lab, 일본'),
                      ('공공제품 디자인과 도시재생', '설문개 / 노신미술대학 산업디자인학원 학장'),
                      ('외딴 골목길: 행복으로 향한 길', '진외 / 선양시 원림과학연구원'),
                      ('공공디자인 실천', 'Olivier Bedu / Cabanon Vertical, 프랑스'),
                      ('자연, 산업: 도시가구의 혁신', '고양 / 중앙미술학원 도시디자인학원')])])
    + '<p class="note">당초 2022년 10월 29일 개최로 안내되었던 포럼입니다.</p>',
    '2022-2nd.jpg', '포스터 / 2022')))

E.append(('2022', event('korea2022', '2022', '2022. 10. 26', '서울, 문화역서울284 RTO', 'IPDF 2022 코리아 에디션',
    '공공을 치유하고 변화시킨 도시 실험 이야기<small>대한민국 공공디자인 페스티벌 2022</small>',
    '<p class="desc">제2회 포럼이 중국에서 열리는 해에, 공공디자인 페스티벌과 함께 한국에서 연 외전 성격의 행사입니다. 관, 학, 민의 공공디자인 전문가가 모여 공공가치를 만드는 디자인 이야기를 나누고, 한국, 중국, 일본, 프랑스의 공공디자인을 영상으로 소개했습니다.</p>'
    + facts([('Date', '2022년 10월 26일, 오후 2시~5시'), ('Venue', '문화역서울284 RTO'), ('Organizer', 'IPDF 한국지부, 홍익대학교 공공디자인연구센터'),
             ('Partner', '토요대학, 가고시마대학, 나고야대학, 노신미술대학, 칭화대학, 중앙미술학원, 닝보대학, Cabanon Vertical')])
    + prog([('Talk', [('질문을 던지는 공공디자인', '젤리장 대표'),
                      ('Park(ing) Day A to Z: &lsquo;함께&rsquo;의 가치, 다양한 공공디자인 이야기', '홍태의 / 홍익대학교 공공디자인연구센터 책임연구원'),
                      ('사회를 위한 공공디자인 실험, Socio-Public Design Activism', '이현성 / 홍익대학교 교수'),
                      ('IPDF 국제공공디자인포럼 스케치 영상', 'IPDF 위원회')])]),
    '2022-korea-edition.jpg', '포스터 / 2022')))

E.append(('2022', event('parking2022', '2022', '2022. 9. 16~17', '서울', '2022 국제 파킹데이',
    '누구나 쉬어갈 수 있는 사람을 위한 주차장<small>Park(ing) Day in Korea</small>',
    '<p class="desc">도심의 주차 공간을 하루 동안 시민의 쉼터로 바꾸는 국제 문화 운동 파킹데이를 한국에서 열었습니다. 공공공간이 누구를 위한 것인지 시민과 함께 묻는 공공디자인 문화 운동입니다.</p>'
    + shots(['!parkingday-2022.jpg'], '국제 파킹데이 / 서울 / 2022'),
    '2022-parkingday.jpg', '포스터 / 2022')))

E.append(('2021', event('f2021', '2021', '2021. 12. 18', '서울, 홍익대학교 공공디자인연구센터, 온라인', '제1회 국제공공디자인포럼',
    '환경, 사회 그리고 협력(E.S.G)과 공공디자인<small>공공성을 위한 디자인의 가치</small>',
    '<p class="desc">기업의 지속가능경영(ESG)과 공공디자인의 연계 사례와 확장 가능성을 논의한 첫 포럼입니다. 한국, 중국, 일본 전문가가 민관학 협력을 통한 공공디자인의 의미와 가치, 지속 가능성을 발표했고, 코로나19로 YouTube와 Zoom을 통해 온라인으로 중계했습니다.</p>'
    + facts([('Date', '2021년 12월 18일 토요일, 오후 2시~5시'), ('Venue', '홍익대학교 공공디자인연구센터(홍문관 1310호), 온라인 중계'),
             ('Host', '국제공공디자인포럼 위원회, 홍익대학교 공공디자인연구센터')])
    + prog([('Opening', [('개회사', '김주연 / IPDF 한국 의장, 홍익대학교')]),
            ('Talk', [('걷는 의식을 디자인하다', '이소베 타카후미 / GK설계 오사카사무소 소장, 일본'),
                      ('퍼블릭 라이프로부터의 도시디자인', '다케다 시게아키 / 오사카부립대학대학원 교수, 일본'),
                      ('도시문화의 전승과 재편: 선양시 산업건축유산의 재생 실천', '강민 / 노신미술대학 건축예술디자인학원 교수, 중국'),
                      ('How to Incorporate Design into Healthcare Innovation', '조초 / 칭화대학 미술학원 부원장, 중국'),
                      ('ESG 경영의 이해', '박성훈 / 사회적가치연구원 실장, 한국'),
                      ('불확실성 시대 공공성과 시민', '이광재 / 한국매니페스토실천본부 사무총장, 한국'),
                      ('사회적 가치 향상을 위한 기업의 ESG 활용 사례', '안진근 / 백석대학교 교수, 한국')]),
            ('Discussion', [('토론', '좌장 장영호 / 홍익대학교 산업미술대학원 공공디자인전공 교수')])])
    + '<p class="pull">&ldquo;오늘의 첫 포럼은 도시의 삶의 질을 높이기 위한 공공디자인 국제협력의 씨앗이 될 것입니다.&rdquo;<small>김주연 / 제1회 포럼 개회사</small></p>'
    + shots(['!f2021-1st-group.jpg', 'f2021-1st-studio.jpg', 'f2021-1st-speakers.jpg', 'f2021-1st-studio2.jpg'], '제1회 국제공공디자인포럼 / 서울 / 2021'),
    '2021-1st.jpg', '포스터 / 2021')))

E.append(('2021', event('founding', '2021', '2021. 8. 28', '서울, 문화역서울284', '국제공공디자인포럼 발대식',
    '사회를 위한 공공디자인, 함께하는 공공디자인<small>Founding Congregation</small>',
    '<p class="desc">한국, 중국, 일본 3개국의 공공디자인 전문가가 모여 국제공공디자인포럼을 창립한 자리입니다. 발기인을 소개하고 포럼 헌장을 선포했으며, 각국을 온라인으로 연결해 인사말과 보고회를 진행했습니다.</p>'
    + facts([('Date', '2021년 8월 28일 토요일, 오후 2시'), ('Venue', '문화역서울284, 온라인 연결')])
    + prog([('Program', [('인사말', '김주연 / 한국'), ('인사말', '수단 교수 / 중국'), ('인사말', '스가와라 마이코 교수 / 일본'),
                         ('축사', '김태훈 원장'), ('', '발기인 소개, 포럼 보고회, 기념 촬영')])])
    + shots(['!f2021-founding-1.jpg', 'f2021-founding-speech.jpg', 'f2021-mou-1.jpg', 'f2021-founding-2.jpg', 'f2021-online-1.jpg', 'f2021-founding-room.jpg'], '국제공공디자인포럼 발대식 / 문화역서울284 / 2021'),
    '2021-founding.jpg', '포스터 / 2021')))

years = ['2025', '2024', '2023', '2022', '2021']
arch = ''
for y in years:
    arch += f'<p class="yearmark" data-year="{y}" aria-hidden="true">{y}</p>'
    arch += ''.join(h for yy, h in E if yy == y)
tabs = '<button data-y="all" aria-pressed="true">전체</button>' + ''.join(f'<button data-y="{y}" aria-pressed="false">{y}</button>' for y in years)

FORUMS = f'''
<section class="phero">
  <img src="{P}f2024-group.jpg" alt="제4회 국제공공디자인포럼 단체 사진">
  <div class="wrap">
    <span class="kicker light">Forum Archive</span>
    <h1 class="h-hero">포럼 아카이브</h1>
    <p class="lead">2021년 발대식부터 제5회 포럼까지, 국제공공디자인포럼이 걸어온 기록입니다.</p>
  </div>
  <span class="cap">제4회 국제공공디자인포럼 / 중국 시안 / 2024</span>
</section>
<section class="sec" style="padding-top:clamp(56px,7vw,88px)">
  <div class="wrap">
    <p class="statline rv" style="margin-bottom:40px"><span class="st">국제포럼 <b>5회</b></span><span class="sep">I</span><span class="st">사전 세미나와 특별 행사 <b>8회</b></span><span class="sep">I</span><span class="st">개최 도시 서울, 선양, 시안, 도쿄</span></p>
    <div class="tabs" role="toolbar" aria-label="연도별 보기">{tabs}</div>
    {arch}
  </div>
</section>
'''

# ------------------------------------------------------------------ gallery
G = [
    ('제5회 국제공공디자인포럼', '서울, 문화역서울284 RTO / 2025. 10. 29', [
        ('f2025-stage.jpg', '포럼 무대', 'c8 r3'), ('f2025-poster-stand.jpg', '기조발제', 'c4 r3'),
        ('f2025-keynote.jpg', '포럼 발표', 'c6 r2'), ('f2025-hall.jpg', '포럼 현장', 'c6 r2'), ('f2025-audience.jpg', '세미나', 'c12 r2')]),
    ('제4회 국제공공디자인포럼', '중국 시안, 시안건축과기대학 / 2024. 6. 14', [
        ('f2024-banner.jpg', '참가자 단체 사진', 'c7 r3'), ('f2024-designx.jpg', 'Design X 발표', 'c5 r3'),
        ('f2024-group.jpg', '참가자 단체 사진', 'c4 r2'), ('f2024-hall.jpg', '포럼 강당', 'c4 r2'), ('f2024-hall2.jpg', '포럼 강당', 'c4 r2'),
        ('f2024-audience.jpg', '토론', 'c6 r2'), ('f2024-panel.jpg', '참가자', 'c6 r2'), ('f2024-outdoor.jpg', '참가자 단체 사진', 'c12 r3')]),
    ('GK 세미나 &amp; Pre-IPDF 2024', '일본 도쿄, GK 디자인그룹 / 2024. 1. 19', [
        ('gk2024-group.jpg', '참가자 단체 사진', 'c8 r2'), ('gk2024-seminar.jpg', '세미나', 'c4 r2')]),
    ('PDF X Cabanon Vertical', '서울, 홍익대학교 / 2023. 9. 19', [
        ('cab2023-hall.jpg', '특강 현장', 'c6 r2'), ('cab2023-talk.jpg', '토론', 'c6 r2'),
        ('cab2023-room.jpg', '특강 현장', 'c4 r3'), ('cab2023-night.jpg', '연사와 참가자', 'c4 r3'), ('cab2023-book.jpg', 'Cabanon Vertical 자료', 'c4 r3')]),
    ('IPDF 세미나', '서울, 홍익대학교 공공디자인연구센터', [
        ('sem-1.jpg', '세미나 현장', 'c8 r2'), ('sem-5.jpg', '발표', 'c4 r2'), ('sem-3.jpg', '토론', 'c4 r2'), ('sem-4.jpg', '토론', 'c4 r2'),
        ('sem-6.jpg', '발표', 'c4 r2'), ('sem-7.jpg', '사례 발표', 'c6 r2'), ('sem-8.jpg', '토론', 'c6 r2'), ('sem-9.jpg', '단체 사진', 'c12 r3'),
        ('sem-11.jpg', '세미나 기록', 'c4 r2'), ('sem-12.jpg', '세미나 기록', 'c4 r2'), ('sem-10.jpg', '세미나 현장', 'c4 r2')]),
    ('국제 교류와 파킹데이', '중국 / 서울 / 2022~2023', [
        ('china-group.jpg', '국제 교류 포럼', 'c7 r2'), ('china-hall.jpg', '국제 교류 포럼', 'c5 r2'), ('parkingday-2022.jpg', '국제 파킹데이 / 2022', 'c12 r3')]),
    ('제1회 국제공공디자인포럼', '서울, 홍익대학교 공공디자인연구센터 / 2021. 12. 18', [
        ('f2021-1st-group.jpg', '위원 단체 사진', 'c7 r3'), ('f2021-1st-speakers.jpg', '연사', 'c5 r3'),
        ('f2021-1st-studio.jpg', '온라인 중계 스튜디오', 'c6 r2'), ('f2021-1st-studio2.jpg', '온라인 중계 스튜디오', 'c6 r2')]),
    ('국제공공디자인포럼 발대식', '서울, 문화역서울284 / 2021. 8. 28', [
        ('f2021-founding-1.jpg', '발대식 현장', 'c8 r3'), ('f2021-founding-speech.jpg', '인사말', 'c4 r3'),
        ('f2021-mou-1.jpg', '협약 서명', 'c4 r2'), ('f2021-mou-3.jpg', '협약 서명', 'c4 r2'), ('f2021-mou-2.jpg', '협약', 'c4 r2'),
        ('f2021-online-1.jpg', '온라인 발표', 'c6 r2'), ('f2021-online-2.jpg', '온라인 발표', 'c6 r2'),
        ('f2021-founding-2.jpg', '발대식 현장', 'c4 r2'), ('f2021-founding-3.jpg', '발대식 현장', 'c4 r2'), ('f2021-founding-room.jpg', '발대식 현장', 'c4 r2')]),
]
gal = ''
for title, sub, items in G:
    gal += (f'<div class="g-group"><div class="wrap g-head rv"><h2>{title}</h2><span>{sub}</span></div>'
            f'<div class="full-bleed"><div class="mosaic">' + ''.join(fig(s, c, title, cls) for s, c, cls in items) + '</div></div></div>')

GALLERY = f'''
<section class="phero">
  <img src="{P}f2025-stage.jpg" alt="제5회 국제공공디자인포럼 무대">
  <div class="wrap">
    <span class="kicker light">Gallery</span>
    <h1 class="h-hero">갤러리</h1>
    <p class="lead">포럼과 세미나, 교류 현장의 기록입니다. 사진을 누르면 크게 볼 수 있습니다.</p>
  </div>
  <span class="cap">제5회 국제공공디자인포럼 / 서울 / 2025</span>
</section>
<section class="sec" style="padding-bottom:40px">{gal}</section>
'''

PAGES = [
    dict(file='index.html', title='IPDF 국제공공디자인포럼 | International Public Design Forum',
         desc='사회를 위한 공공디자인, 함께하는 공공디자인. 한국, 중국, 일본, 프랑스의 공공디자인 전문가가 함께하는 국제공공디자인포럼(IPDF) 공식 홈페이지입니다.', body=INDEX),
    dict(file='about.html', title='포럼 소개 | IPDF 국제공공디자인포럼',
         desc='국제공공디자인포럼 인사말, 포럼 소개, 발기문, 헌장, 조직과 위원, 참가 문의.', body=ABOUT, og='f2024-outdoor.jpg'),
    dict(file='vision.html', title='비전과 계획 | IPDF 국제공공디자인포럼',
         desc='공공가치 추구를 위한 4개 목표와 12개 핵심 지표, 외교, 문화, 교육, 학술 분야의 활동과 8대 공공가치 프로젝트.', body=VISION, og='f2024-hall.jpg'),
    dict(file='forums.html', title='포럼 아카이브 | IPDF 국제공공디자인포럼',
         desc='2021년 발대식부터 제5회 국제공공디자인포럼까지, 서울, 선양, 시안, 도쿄에서 열린 포럼과 세미나의 기록.', body=FORUMS, og='f2024-group.jpg'),
    dict(file='gallery.html', title='갤러리 | IPDF 국제공공디자인포럼',
         desc='국제공공디자인포럼의 포럼, 세미나, 교류 현장 사진.', body=GALLERY),
]
