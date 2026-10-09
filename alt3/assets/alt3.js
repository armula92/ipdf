/* 왼쪽 서랍 메뉴 */
const dr=document.getElementById('drawer'),sc=document.querySelector('.scrim');
const setD=o=>{dr.classList.toggle('open',o);sc.classList.toggle('open',o);document.body.classList.toggle('lock',o);document.querySelector('.menu-open').setAttribute('aria-expanded',o)};
document.querySelector('.menu-open').addEventListener('click',()=>setD(true));
dr.querySelector('.x').addEventListener('click',()=>setD(false));sc.addEventListener('click',()=>setD(false));
dr.querySelectorAll('a.dl').forEach(a=>a.addEventListener('click',()=>setD(false)));
addEventListener('keydown',e=>{if(e.key==='Escape')setD(false)});

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
  const s=document.createElement('script');s.src='https://translate.google.com/translate_a/element.js?cb=gtInit';document.body.appendChild(s);
}

/* 탭 */
document.querySelectorAll('[role=tablist]').forEach(tl=>{
  const tabs=[...tl.querySelectorAll('[role=tab]')];
  tabs.forEach(t=>t.addEventListener('click',()=>{tabs.forEach(x=>{const on=x===t;x.setAttribute('aria-selected',on);document.getElementById(x.getAttribute('aria-controls')).hidden=!on})}));
});

/* 캐러셀 화살표 */
document.querySelectorAll('[data-car]').forEach(box=>{
  box.querySelectorAll('[data-dir]').forEach(b=>b.addEventListener('click',()=>{
    const tr=[...box.querySelectorAll('.track')].find(t=>!t.closest('[hidden]'));tr.scrollBy({left:+b.dataset.dir*tr.clientWidth*.75,behavior:'smooth'})}));
});

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
