/* header */
const top_=document.querySelector('.top');
const onS=()=>top_.classList.toggle('solid',scrollY>innerHeight*.7&&!document.body.classList.contains('lock'));
addEventListener('scroll',onS,{passive:true});onS();

/* 전체 화면 메뉴 */
const ov=document.getElementById('overlay'),mb=document.querySelector('.menu-btn');
const setMenu=o=>{ov.classList.toggle('open',o);document.body.classList.toggle('lock',o);mb.setAttribute('aria-expanded',o);mb.querySelector('span').textContent=o?'Close':'Menu';onS();
  ov.querySelectorAll('nav a').forEach((a,i)=>a.style.transitionDelay=o?(.08+i*.06)+'s':'0s')};
mb.addEventListener('click',()=>setMenu(!ov.classList.contains('open')));
ov.querySelectorAll('nav a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
addEventListener('keydown',e=>{if(e.key==='Escape'&&ov.classList.contains('open'))setMenu(false)});

/* 언어: 페이지 안 Google 번역 */
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

/* 등장 */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('v');io.unobserve(e.target)}}),{threshold:.1,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));

/* 히어로 */
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const sls=[...document.querySelectorAll('.hero .sl')],hb=[...document.querySelectorAll('.hero-prog button')];
if(sls.length){let i=0,t;
  const go=n=>{sls[i].classList.remove('on');hb[i].removeAttribute('aria-current');i=(n+sls.length)%sls.length;sls[i].classList.add('on');hb[i].setAttribute('aria-current','true')};
  const play=()=>{clearInterval(t);if(!reduce)t=setInterval(()=>go(i+1),7000)};
  hb.forEach((b,k)=>b.addEventListener('click',()=>{go(k);play()}));go(0);play();}

/* 아카이브 필터, 프로그램 펼치기 */
const fb=document.querySelectorAll('.filters button');
fb.forEach(b=>b.addEventListener('click',()=>{const y=b.dataset.y;fb.forEach(x=>x.setAttribute('aria-pressed',x===b));
  document.querySelectorAll('.year').forEach(el=>el.hidden=!(y==='all'||el.dataset.y===y))}));
document.querySelectorAll('.acc-b').forEach(b=>b.addEventListener('click',()=>{const p=document.getElementById(b.getAttribute('aria-controls'));
  const o=!p.classList.contains('open');p.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.querySelector('span').textContent=o?'프로그램 접기':'프로그램 보기'}));

/* 라이트박스 */
const zs=[...document.querySelectorAll('[data-lb]')];
if(zs.length){
  const lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');
  lb.innerHTML='<figure><img alt=""><figcaption></figcaption></figure><button class="x" aria-label="닫기">×</button><button class="pv" aria-label="이전">‹</button><button class="nx" aria-label="다음">›</button>';
  document.body.appendChild(lb);const im=lb.querySelector('img'),fc=lb.querySelector('figcaption');let c=0;
  const show=k=>{c=(k+zs.length)%zs.length;const el=zs[c];const img=el.tagName==='IMG'?el:el.querySelector('img');im.src=img.src;fc.textContent=el.dataset.cap||img.alt||''};
  const open=k=>{show(k);lb.classList.add('open');document.body.style.overflow='hidden'},close=()=>{lb.classList.remove('open');document.body.style.overflow=''};
  zs.forEach((el,k)=>{el.tabIndex=0;el.addEventListener('click',()=>open(k));el.addEventListener('keydown',e=>{if(e.key==='Enter')open(k)})});
  lb.querySelector('.x').onclick=close;lb.querySelector('.pv').onclick=()=>show(c-1);lb.querySelector('.nx').onclick=()=>show(c+1);
  lb.addEventListener('click',e=>{if(e.target===lb)close()});
  addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(c-1);if(e.key==='ArrowRight')show(c+1)});
}
