'use strict';
const present = document.getElementById('present');
present.setAttribute('aria-pressed','false');
present.addEventListener('click', () => {
  const active = document.body.classList.toggle('focus-mode');
  present.textContent = active ? '기본 화면으로' : '수업 집중 모드';
  present.setAttribute('aria-pressed', String(active));
});
document.getElementById('back-top').addEventListener('click', () => window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'}));
const links = [...document.querySelectorAll('nav a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) links.forEach(link => {
        const active = link.hash === '#' + entry.target.id;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current','step'); else link.removeAttribute('aria-current');
      });
    });
  }, {rootMargin:'-15% 0px -55% 0px',threshold:0});
  links.forEach(link=>observer.observe(document.querySelector(link.hash)));
}
const clock = document.getElementById('clock');
const duration = document.getElementById('duration');
const toggle = document.getElementById('timer-toggle');
const status = document.getElementById('timer-status');
let remaining=60000, deadline=0, interval=null;
function draw(){const seconds=Math.ceil(remaining/1000);clock.textContent=String(Math.floor(seconds/60)).padStart(2,'0')+':'+String(seconds%60).padStart(2,'0');}
function stop(){clearInterval(interval);interval=null;toggle.textContent='시작';duration.disabled=false;}
function tick(){remaining=Math.max(0,deadline-Date.now());draw();if(remaining===0){stop();status.textContent='시간이 끝났어요. 다음 친구의 이야기를 들어 봅시다.';}}
toggle.addEventListener('click',()=>{if(interval!==null){remaining=Math.max(0,deadline-Date.now());stop();draw();status.textContent='잠시 멈췄어요. 시작을 누르면 이어집니다.';}else{if(remaining<=0)remaining=Number(duration.value)*1000;deadline=Date.now()+remaining;duration.disabled=true;toggle.textContent='일시정지';status.textContent='친구의 이야기를 끝까지 들어 주세요.';interval=setInterval(tick,200);tick();}});
function reset(){stop();remaining=Number(duration.value)*1000;draw();status.textContent='발언 준비가 되면 시작하세요.';}
duration.addEventListener('change',reset);
document.getElementById('timer-reset').addEventListener('click',reset);
