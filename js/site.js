(() => {
'use strict';
const menu=document.getElementById('menuButton'), mobile=document.getElementById('mobileNav');
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')==='true';menu.setAttribute('aria-expanded',String(!open));mobile.hidden=open;menu.textContent=open?'☰':'×';});
mobile.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{mobile.hidden=true;menu.textContent='☰';menu.setAttribute('aria-expanded','false');}));
const dialog=document.getElementById('imageDialog'), img=document.getElementById('dialogImage'),cap=document.getElementById('dialogCaption');
document.querySelectorAll('.lightbox-trigger').forEach(button=>button.addEventListener('click',()=>{img.src=button.dataset.image;img.alt=button.querySelector('img').alt;cap.textContent=button.dataset.caption;dialog.showModal();}));
document.getElementById('closeDialog').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
const zSlider=document.getElementById('zRange'),rSlider=document.getElementById('rRange'),dSlider=document.getElementById('dRange');
const canvas=document.getElementById('fieldCanvas'),ctx=canvas.getContext('2d'),w=canvas.width,h=canvas.height;
const output=id=>document.getElementById(id);
const positions=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]].map(v=>v.map(x=>x*22.86));
function distSegment(x,y,z,end){const norm=end[0]*end[0]+end[1]*end[1]+end[2]*end[2];const t=Math.max(0,Math.min(1,(x*end[0]+y*end[1]+z*end[2])/norm));return Math.hypot(x-t*end[0],y-t*end[1],z-t*end[2]);}
function kField(x,y,z){let r=Math.min(1,Math.max(Math.abs(x),Math.abs(y),Math.abs(z))/31.75);const p=14-6*Math.pow(r,1.35),tau=.27+.21*Math.pow(r,1.6);let d=Infinity;for(const end of positions)d=Math.min(d,distSegment(x,y,z,end));const eff=tau+.08*Math.exp(-.22*d),k=2*Math.PI/p,g=Math.sin(k*x)*Math.cos(k*y)+Math.sin(k*y)*Math.cos(k*z)+Math.sin(k*z)*Math.cos(k*x);return {solid:Math.abs(g)<=eff,eff,g};}
function draw(){const z=Number(zSlider.value);const size=220,off=document.createElement('canvas');off.width=size;off.height=size;const context=off.getContext('2d'),data=context.createImageData(size,size);for(let j=0;j<size;j++){const y=31.75-(j+.5)/size*63.5;for(let i=0;i<size;i++){const x=-31.75+(i+.5)/size*63.5;const r=kField(x,y,z),idx=(j*size+i)*4;const colors=r.solid?[77,214,193]:[19,48,62];data.data[idx]=colors[0];data.data[idx+1]=colors[1];data.data[idx+2]=colors[2];data.data[idx+3]=255;}}
context.putImageData(data,0,0);ctx.clearRect(0,0,w,h);ctx.imageSmoothingEnabled=false;ctx.drawImage(off,0,0,w,h);ctx.strokeStyle='rgba(238,251,251,.45)';ctx.lineWidth=2;ctx.strokeRect(1,1,w-2,h-2);output('sliceCaption').textContent=`z = ${z.toFixed(1)} mm`;}
function scalars(){const r=Number(rSlider.value),d=Number(dSlider.value);const p=14-6*Math.pow(r,1.35),tau=.27+.21*Math.pow(r,1.6),k=Math.exp(-.22*d);output('zOut').textContent=Number(zSlider.value).toFixed(1)+' mm';output('rOut').textContent=r.toFixed(2);output('dOut').textContent=d.toFixed(1)+' mm';output('pitchOut').textContent=p.toFixed(2)+' mm';output('tauOut').textContent=tau.toFixed(3);output('kOut').textContent=k.toFixed(3);output('effOut').textContent=(tau+.08*k).toFixed(3);}
zSlider.addEventListener('input',()=>{scalars();draw()});[rSlider,dSlider].forEach(s=>s.addEventListener('input',scalars));output('resetLab').addEventListener('click',()=>{zSlider.value='0';rSlider.value='.50';dSlider.value='5';scalars();draw();});scalars();draw();
})();