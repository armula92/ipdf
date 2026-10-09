/* header: 스크롤하면 강조색 배경 */
const header=document.querySelector('header.site');
const onScroll=()=>header.classList.toggle('solid',window.scrollY>window.innerHeight*0.55||document.body.classList.contains('menu-open'));
window.addEventListener('scroll',onScroll,{passive:true});onScroll();

/* 언어: 페이지 안 Google 번역(웹사이트 번역 도구). translate.goog 주소 방식은 한국 등에서 차단되어 쓰지 않음 */
const gtCookie=()=>{const m=document.cookie.match(/(?:^|;\s*)googtrans=\/ko\/([^;]+)/);return m?decodeURIComponent(m[1]):'ko'};
const setGt=l=>{const host=location.hostname,base=host.replace(/^www\./,'');
  const exp=l==='ko'?';expires=Thu, 01 Jan 1970 00:00:00 GMT':'';const v=l==='ko'?'':'/ko/'+l;
  ['',';domain='+host,';domain=.'+base].forEach(d=>{document.cookie='googtrans='+v+';path=/'+d+exp});};
let curLang=gtCookie();
const qLang=new URLSearchParams(location.search).get('lang');
if(qLang&&qLang!==curLang){setGt(qLang);curLang=qLang;}
document.querySelectorAll('.lang a').forEach(a=>{
  const l=a.dataset.lang;if(l===curLang)a.setAttribute('aria-current','true');
  a.addEventListener('click',e=>{e.preventDefault();if(l===gtCookie())return;setGt(l);
    const u=new URL(location.href);u.searchParams.delete('lang');history.replaceState(null,'',u.pathname+u.search+u.hash);location.reload();});
});
if(curLang!=='ko'){
  document.documentElement.lang=curLang;
  window.gtInit=()=>{new google.translate.TranslateElement({pageLanguage:'ko',includedLanguages:'en,zh-CN,ja',autoDisplay:false},'gt-el')};
  const sc=document.createElement('script');sc.src='https://translate.google.com/translate_a/element.js?cb=gtInit';document.body.appendChild(sc);
}

/* 모바일 메뉴 */
const burger=document.querySelector('.burger'),mm=document.getElementById('mobileMenu');
const closeMenu=()=>{mm.classList.remove('open');document.body.classList.remove('menu-open');burger.setAttribute('aria-expanded','false');onScroll()};
burger.addEventListener('click',()=>{const o=mm.classList.toggle('open');document.body.classList.toggle('menu-open',o);burger.setAttribute('aria-expanded',o);onScroll()});
mm.querySelectorAll('a.m-link').forEach(a=>a.addEventListener('click',closeMenu));

/* 스크롤 등장 */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));

/* 메인 히어로 슬라이드 */
const hero=document.querySelector('.hero');
if(hero){
  const slides=[...hero.querySelectorAll('.slide')],dots=[...hero.querySelectorAll('.hero-dots button')],cap=hero.querySelector('.hero-cap');
  let i=0,t;
  const go=n=>{slides[i].classList.remove('on');dots[i]&&dots[i].removeAttribute('aria-current');
    i=(n+slides.length)%slides.length;slides[i].classList.add('on');dots[i]&&dots[i].setAttribute('aria-current','true');
    if(cap)cap.innerHTML=slides[i].dataset.cap;};
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const play=()=>{clearInterval(t);if(!reduce)t=setInterval(()=>go(i+1),6500)};
  dots.forEach((d,k)=>d.addEventListener('click',()=>{go(k);play()}));
  go(0);play();
}

/* 포스터 띠 좌우 이동 */
document.querySelectorAll('[data-strip]').forEach(box=>{
  const list=box.querySelector('.posters');
  box.querySelectorAll('[data-dir]').forEach(b=>b.addEventListener('click',()=>list.scrollBy({left:+b.dataset.dir*list.clientWidth*.8,behavior:'smooth'})));
});

/* 아카이브 연도 필터 */
const tabs=document.querySelectorAll('.tabs button');
if(tabs.length){
  const apply=y=>{
    tabs.forEach(b=>b.setAttribute('aria-pressed',b.dataset.y===y));
    document.querySelectorAll('[data-year]').forEach(el=>el.hidden=!(y==='all'||el.dataset.year===y));
  };
  tabs.forEach(b=>b.addEventListener('click',()=>apply(b.dataset.y)));
}

/* 라이트박스 */
const zoomables=[...document.querySelectorAll('[data-lb]')];
if(zoomables.length){
  const lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label','사진 크게 보기');
  lb.innerHTML='<figure><img alt=""><figcaption></figcaption></figure><button class="x" aria-label="닫기">×</button><button class="pv" aria-label="이전">‹</button><button class="nx" aria-label="다음">›</button>';
  document.body.appendChild(lb);
  const im=lb.querySelector('img'),fc=lb.querySelector('figcaption');let cur=0;
  const show=k=>{cur=(k+zoomables.length)%zoomables.length;const el=zoomables[cur];const src=el.dataset.lb||el.querySelector('img')?.src||el.src;
    im.src=src;const c=el.dataset.cap||el.closest('figure')?.querySelector('figcaption')?.innerText||el.alt||'';fc.textContent=c.replace(/\s*\n\s*/g,' / ');im.alt=c;};
  const open=k=>{show(k);lb.classList.add('open');document.body.style.overflow='hidden'};
  const close=()=>{lb.classList.remove('open');document.body.style.overflow=''};
  zoomables.forEach((el,k)=>{el.tabIndex=0;el.addEventListener('click',()=>open(k));el.addEventListener('keydown',e=>{if(e.key==='Enter')open(k)})});
  lb.querySelector('.x').onclick=close;lb.querySelector('.pv').onclick=()=>show(cur-1);lb.querySelector('.nx').onclick=()=>show(cur+1);
  lb.addEventListener('click',e=>{if(e.target===lb)close()});
  document.addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1)});
}
