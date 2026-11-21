# -*- coding: utf-8 -*-
import json,os,shutil,html,datetime
from PIL import Image
from data import CATS,P,FAQ,BLOG
cfg=json.load(open('config.json',encoding='utf-8'))
BASE=cfg['site_url'].rstrip('/')
OUT='dist'; TODAY=datetime.date.today().isoformat()
E=lambda s:html.escape(str(s),quote=True)
def ok(v): return bool(v) and not str(v).startswith('[')
NAME=cfg['name']
shutil.rmtree(OUT,ignore_errors=True); os.makedirs(OUT+'/img/products'); os.makedirs(OUT+'/css'); os.makedirs(OUT+'/js'); os.makedirs(OUT+'/fonts')
CAT={c[0]:dict(slug=c[0],title=c[1],single=c[2],intro=c[3],use=c[4],cover=c[5],kind=c[6]) for c in CATS}
# fonts
for fn in ('DachiLynx.otf','MersadLight.otf'):
    shutil.copy(f'fonts/{fn}',f'{OUT}/fonts/{fn}')
# images
IMG={}
def put_img(key,outname,folder='src_img'):
    src=f'{folder}/{key}.webp' if not key.endswith('.webp') else f'{folder}/{key}'
    if not os.path.exists(src) and folder=='src_img':
        src=f'src_img/{key}.webp'
    dst=f'{OUT}/img/{outname}'
    shutil.copy(src,dst); w,h=Image.open(src).size; IMG[outname]=(w,h); return '/img/'+outname
for p in P:
    p['imgurl']=put_img(p['img'],f"products/eps-{p['cat']}-{p['slug']}.webp"); p['wh']=IMG[f"products/eps-{p['cat']}-{p['slug']}.webp"]
    p['url']=f"/products/{p['cat']}/{p['slug']}/"
for k in ['G-1','G-2','G-3','G-4','G-5']: put_img(k,f'eps-fasadi-{k.lower()}.webp')
# premium architectural photos (Unsplash license) — atmospheric, not claimed as company projects
ARCH=['arch-01','arch-02','arch-03','arch-04','arch-05','arch-07','arch-08','arch-09','arch-10','arch-12','arch-13','arch-14','arch-15','arch-16','arch-17','arch-18']
for a in ARCH:
    src=f'src_img/arch/{a}.webp'
    if os.path.exists(src):
        dst=f'{OUT}/img/{a}.webp'; shutil.copy(src,dst); IMG[f'{a}.webp']=Image.open(src).size
# brand logos + favicon
for logo in ('logo-color.png','logo-white.png','logo-square.jpg'):
    src=f'src_img/brand/{logo}'
    if os.path.exists(src): shutil.copy(src,f'{OUT}/img/{logo}')
for root_asset in ('favicon.ico','favicon-32.png','apple-touch-icon.png','icon-512.png'):
    src=f'src_img/brand/{root_asset}'
    if os.path.exists(src): shutil.copy(src,f'{OUT}/{root_asset}')
# SVG favicon — navy + orange mark matching brand
open(OUT+'/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#0B1F3A"/><path d="M14 20h36l-5 10H19z" fill="#1B3A5C"/><path d="M16 32h32l-5 10H21z" fill="#E8912D"/><path d="M18 44h28l-5 10H23z" fill="#1B3A5C"/></svg>')
# og image from premium hero photo
hero_src='src_img/arch/arch-15.webp' if os.path.exists('src_img/arch/arch-15.webp') else ('src_img/arch/arch-01.webp' if os.path.exists('src_img/arch/arch-01.webp') else 'src_img/G-1.webp')
g=Image.open(hero_src).convert('RGB'); w,h=g.size; t=int(w*630/1200)
g.crop((0,max(0,(h-t)//2),w,max(0,(h-t)//2)+t)).resize((1200,630)).save(OUT+'/img/og-image.jpg',quality=82)
css=open('style.css',encoding='utf-8').read(); open(OUT+'/css/style.css','w',encoding='utf-8').write(css)
js=open('js/site.js',encoding='utf-8').read(); open(OUT+'/js/site.js','w',encoding='utf-8').write(js)
i18n=open('js/i18n.js',encoding='utf-8').read(); open(OUT+'/js/i18n.js','w',encoding='utf-8').write(i18n)

def phone_href(p=None):
    p=cfg['phone'] if p is None else p
    return 'tel:'+''.join(c for c in p if c.isdigit() or c=='+') if ok(p) else '/contact/'
def phones():
    out=[]
    for k in ('phone','phone2'):
        if ok(cfg.get(k,'')): out.append(cfg[k])
    return out
def phones_html(sep='<br>'):
    return sep.join(f'<a href="{phone_href(p)}">{E(p)}</a>' for p in phones())
def org():
    o={"@type":"LocalBusiness","@id":BASE+"/#org","name":NAME,"url":BASE+"/","image":BASE+"/img/og-image.jpg","areaServed":"GE","description":"EPS (გაფართოებული პოლისტირონის) დეკორატიული ფასადის ელემენტების მწარმოებელი საქართველოში."}
    ps=phones()
    if ps: o['telephone']=ps if len(ps)>1 else ps[0]
    if ok(cfg['email']): o['email']=cfg['email']
    if ok(cfg['street']) or ok(cfg['city']):
        ad={"@type":"PostalAddress","addressCountry":"GE"}
        if ok(cfg['street']): ad['streetAddress']=cfg['street']
        if ok(cfg['city']): ad['addressLocality']=cfg['city']
        o['address']=ad
    if cfg['lat'] and cfg['lng']: o['geo']={"@type":"GeoCoordinates","latitude":cfg['lat'],"longitude":cfg['lng']}
    sa=[cfg[k] for k in ('facebook','instagram') if cfg[k]]
    if sa: o['sameAs']=sa
    return o
def crumbs_ld(items):
    return {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}
def crumbs_html(items):
    out=[f'<a href="{u}">{E(n)}</a>' for n,u in items[:-1]]+[f'<span aria-current="page">{E(items[-1][0])}</span>']
    return '<nav class="crumbs wrap" aria-label="ბილიკი">'+' / '.join(out)+'</nav>'
PAGES=[]

def page(path,title,desc,body,ld=None,og=None,noindex=False,typ='website',home=False):
    url=BASE+path; og=og or BASE+'/img/og-image.jpg'
    graph=[org(),{"@type":"WebSite","@id":BASE+"/#site","url":BASE+"/","name":NAME,"inLanguage":"ka"}]+(ld or [])
    cats=''.join(f'<li><a href="/products/{c}/" data-i18n="cat.{c}">{E(CAT[c]["title"])}</a></li>' for c in CAT)
    addr_ka=E(', '.join(v for v in (cfg['street'],cfg['city']) if v))
    nap=f'<strong data-i18n="brand.name">{E(NAME)}</strong><br><span data-i18n-street data-ka="{addr_ka}">{addr_ka}</span>'
    contact=f'<p>{nap}<br>{phones_html()}<br><a href="mailto:{E(cfg["email"])}">{E(cfg["email"])}</a></p>'
    robots='noindex,follow' if noindex else 'index,follow,max-image-preview:large'
    body_cls='is-home' if home else ''
    lang_switch='''<div class="lang-switch" role="group" aria-label="Language"><button type="button" data-lang="ka" aria-pressed="true">KA</button><button type="button" data-lang="en" aria-pressed="false">EN</button><button type="button" data-lang="ru" aria-pressed="false">RU</button></div>'''
    brand=f'''<a class="brand" href="/" aria-label="{E(NAME)}"><img class="brand-logo brand-logo--color" src="/img/logo-color.png" width="150" height="58" alt="{E(NAME)}"><img class="brand-logo brand-logo--white" src="/img/logo-white.png" width="150" height="58" alt="" aria-hidden="true"></a>'''
    html_=f'''<!DOCTYPE html>
<html lang="ka"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="robots" content="{robots}">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#0B1F3A">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" type="image/png" sizes="32x32"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="shortcut icon" href="/favicon.ico">
<meta property="og:type" content="{typ}"><meta property="og:site_name" content="{E(NAME)}"><meta property="og:locale" content="ka_GE"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/fonts/DachiLynx.otf" as="font" type="font/otf" crossorigin><link rel="preload" href="/fonts/MersadLight.otf" as="font" type="font/otf" crossorigin><link rel="stylesheet" href="/css/style.css">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)}</script></head><body class="{body_cls}">
<header class="site-header"><div class="wrap bar">{brand}<button class="nav-toggle" type="button" aria-label="მენიუ" data-i18n="nav.menu" data-i18n-attr="aria-label" aria-expanded="false" aria-controls="site-nav"><span></span></button><nav id="site-nav" class="site-nav" aria-label="მთავარი მენიუ" data-i18n="nav.main" data-i18n-attr="aria-label"><a href="/products/" data-i18n="nav.products">პროდუქცია</a><a href="/blog/" data-i18n="nav.blog">ბლოგი</a><a class="nav-cta" href="/contact/" data-i18n="nav.contact">კონტაქტი</a>{lang_switch}</nav></div></header>
<main class="page-main">{body}</main>
<footer><div class="wrap fgrid"><div><h2 data-i18n="footer.contact">კონტაქტი</h2>{contact}</div><div><h2 data-i18n="footer.products">პროდუქცია</h2><ul>{cats}</ul></div><div class="site-col"><h2 data-i18n="footer.site">საიტი</h2><ul><li><a href="/" data-i18n="footer.home">მთავარი</a></li><li><a href="/products/" data-i18n="footer.catalog">კატალოგი</a></li><li><a href="/blog/" data-i18n="nav.blog">ბლოგი</a></li><li><a href="/contact/" data-i18n="nav.contact">კონტაქტი</a></li></ul></div></div><div class="wrap copy">© {datetime.date.today().year} <span data-i18n="brand.name">{E(NAME)}</span>. <span data-i18n="footer.copy">EPS დეკორატიული ფასადის ელემენტები, საქართველო.</span></div></footer>
<script src="/js/i18n.js" defer></script><script src="/js/site.js" defer></script></body></html>'''
    if path.endswith('.html'): open(OUT+path,'w',encoding='utf-8').write(html_)
    else:
        d=OUT+path; os.makedirs(d,exist_ok=True); open(d+'index.html','w',encoding='utf-8').write(html_)
        if not noindex: PAGES.append(path)
def img(url,wh,alt,lazy=True,cls=''):
    return f'<img src="{url}" width="{wh[0]}" height="{wh[1]}" alt="{E(alt)}"{" loading=\"lazy\"" if lazy else ""}{" decoding=\"async\"" if lazy else ""}{" class=\""+cls+"\"" if cls else ""}>'
def sizesum(p):
    s=p['sizes']
    if len(s)==1: return s[0][1]
    return f'{len(s)} ზომა'
def card(p,i=None):
    c=CAT[p['cat']]
    idx=f'<span class="card-index">{i:02d}</span>' if i is not None else ''
    return f'<a class="card {c["kind"]} reveal" href="{p["url"]}">{idx}<span class="ph">{img(p["imgurl"],p["wh"],p["name"]+" – EPS დეკორატიული ელემენტი")}</span><span class="cap"><b>{E(p["name"])}</b><span>{E(sizesum(p))}</span></span></a>'
CTA=lambda: f'<div class="cta-row"><a class="btn dark" href="/contact/" data-i18n="cta.price">ფასის მოთხოვნა</a>'+(f'<a class="btn line" href="{phone_href()}">{E(cfg["phone"])}</a>' if phones() else '')+'</div>'

# ---------- home
cat_list=list(CAT.keys())
cats_html=''
for i,c in enumerate(cat_list,1):
    first=[x for x in P if x['cat']==c][0]
    count=len([x for x in P if x['cat']==c])
    cats_html+=f'<a class="card {CAT[c]["kind"]} reveal" href="/products/{c}/"><span class="card-index">{i:02d}</span><span class="ph">{img("/img/products/eps-"+c+"-"+first["slug"]+".webp",first["wh"],CAT[c]["title"])}</span><span class="cap"><b data-i18n="cat.{c}">{E(CAT[c]["title"])}</b><span><span class="js-count">{count}</span> <span data-i18n="products.count">პროდუქტი</span></span></span></a>'

# company facade examples + premium architectural atmosphere photos
gal_items=[]
for i in (2,3,4,5):
    gal_items.append(f'<a class="gal-item reveal" href="/products/"><span class="sr">ფასადის მაგალითი</span>{img(f"/img/eps-fasadi-g-{i}.webp",IMG[f"eps-fasadi-g-{i}.webp"],"EPS დეკორით მორთული ფასადის მაგალითი")}</a>')
for a,alt in (('arch-01','თანამედროვე საცხოვრებელი ფასადის არქიტექტურა'),('arch-04','კლასიკური ვილის ფასადი დეკორატიული ელემენტებით'),('arch-09','ისტორიული ფასადის არქიტექტურული დეტალები'),('arch-12','თანამედროვე სახლის ფასადი'),('arch-15','თანამედროვე სახლის ექსტერიერი'),('arch-16','მინიმალისტური ვილის ფასადი'),('arch-14','თანამედროვე არქიტექტურის ფასადი'),('arch-18','ქალაქური საცხოვრებელი ფასადი')):
    if f'{a}.webp' in IMG:
        gal_items.append(f'<a class="gal-item reveal" href="/products/"><span class="sr">{E(alt)}</span>{img(f"/img/{a}.webp",IMG[f"{a}.webp"],alt)}</a>')
gal=''.join(gal_items)

blog_thumbs=[t for t in ('arch-02.webp','arch-03.webp','arch-10.webp','arch-13.webp','arch-17.webp') if t in IMG] or ['eps-fasadi-g-2.webp','eps-fasadi-g-3.webp','eps-fasadi-g-4.webp']
posts=''
for i,(s,t,d,_) in enumerate(BLOG):
    th=blog_thumbs[i%len(blog_thumbs)]
    posts+=f'''<li class="reveal reveal-d{i+1}"><a class="blog-card" href="/blog/{s}/"><span class="thumb">{img('/img/'+th,IMG[th],t)}</span><span class="meta-line" data-i18n="home.blog.meta">სტატია</span><h3>{E(t)}</h3><p>{E(d)}</p><span class="read" data-i18n="home.blog.read">წაკითხვა →</span></a></li>'''

fq=''.join(f'<details class="reveal"><summary>{E(q)}</summary><p>{E(a_)}</p></details>' for q,a_ in FAQ)

hero_img='arch-15.webp' if 'arch-15.webp' in IMG else ('arch-04.webp' if 'arch-04.webp' in IMG else ('arch-01.webp' if 'arch-01.webp' in IMG else 'eps-fasadi-g-1.webp'))
hero_alt='თანამედროვე საცხოვრებელი ფასადის არქიტექტურა' if hero_img.startswith('arch') else 'EPS დეკორით მორთული საცხოვრებელი შენობის ფასადი'
body=f'''<section class="hero" aria-label="მთავარი">
<div class="hero-media" aria-hidden="false">{img(f"/img/{hero_img}",IMG[hero_img],hero_alt,False,"heroimg")}</div>
<div class="hero-shade" aria-hidden="true"></div>
<div class="hero-frame">
  <div class="hero-copy">
    <div class="hero-kicker"><span class="hero-rule" aria-hidden="true"></span><p class="eyebrow" data-i18n="home.kicker">საქართველო · EPS წარმოება</p></div>
    <h1 data-i18n="home.h1">EPS დეკორატიული ელემენტები ფასადისთვის</h1>
    <p class="hero-lead" data-i18n="home.lead">კარნიზები, სვეტები, პანელები და თაღები EPS-ისგან. წარმოება საქართველოშია, მიწოდება მთელ ქვეყანაში.</p>
    <div class="cta-row"><a class="btn" href="/contact/" data-i18n="cta.request">მოითხოვეთ ფასი</a><a class="btn alt" href="/products/" data-i18n="cta.catalog">კატალოგის ნახვა</a></div>
  </div>
  <aside class="hero-rail" aria-label="მოკლე მიმოხილვა">
    <div class="hero-meta"><div><b>12</b><span data-i18n="home.meta.cats">კატეგორია</span></div><div><b>{len(P)}</b><span data-i18n="home.meta.products">პროდუქტი</span></div><div><b>EPS</b><span data-i18n="home.meta.material">მასალა</span></div></div>
  </aside>
</div>
</section>
<section class="sec-stone" id="categories"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow" data-i18n="home.cat.eyebrow">კატალოგი</p><h2 data-i18n="home.cat.h2">პროდუქციის კატეგორიები</h2></div><p class="lead" data-i18n="home.cat.lead">აირჩიეთ კატეგორია, შემდეგ პროდუქტი – მის გვერდზე ნახავთ ხელმისაწვდომ ზომებს.</p></div><div class="cat-grid">{cats_html}</div></div></section>
<section id="gallery"><div class="wrap-wide"><div class="section-head stack reveal"><p class="eyebrow" data-i18n="home.gal.eyebrow">პორტფოლიო</p><h2 data-i18n="home.gal.h2">ფასადის მაგალითები</h2></div><div class="gal">{gal}</div></div></section>
<section class="sec-dark" id="why"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow" data-i18n="home.why.eyebrow">უპირატესობები</p><h2 data-i18n="home.why.h2">რატომ EPS</h2></div></div><div class="facts"><div class="fact reveal"><span class="fact-num">01</span><h3 data-i18n="home.why.1.t">მსუბუქია</h3><p data-i18n="home.why.1.p">ელემენტები ფასადს დიდ დატვირთვას არ უმატებს და მათი აწევა და დამაგრება მარტივია.</p></div><div class="fact reveal reveal-d1"><span class="fact-num">02</span><h3 data-i18n="home.why.2.t">სწრაფი მონტაჟი</h3><p data-i18n="home.why.2.p">დამაგრება ხდება წებოვანი ხსნარით, საჭიროებისამებრ დუბელებით.</p></div><div class="fact reveal reveal-d2"><span class="fact-num">03</span><h3 data-i18n="home.why.3.t">ბევრი ფორმა</h3><p data-i18n="home.why.3.p">პროფილები, სვეტები, კუთხის ქვები, თაღები და ორნამენტული ელემენტები.</p></div><div class="fact reveal reveal-d3"><span class="fact-num">04</span><h3 data-i18n="home.why.4.t">ადგილობრივი წარმოება</h3><p data-i18n="home.why.4.p">ზომებისა და ვადების დაზუსტება შეგიძლიათ პირდაპირ მწარმოებელთან.</p></div></div></div></section>
<section class="sec-stone" id="order"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow" data-i18n="home.order.eyebrow">შეკვეთა</p><h2 data-i18n="home.order.h2">როგორ შევუკვეთოთ</h2></div></div><ol class="steps reveal"><li data-i18n="home.order.1">გამოგვიგზავნეთ ფასადის ფოტო, ნახაზი ან სასურველი მოდელების სია.</li><li data-i18n="home.order.2">დავაზუსტებთ ზომებს, რაოდენობასა და ვადას.</li><li data-i18n="home.order.3">გაგიგზავნით ფასს.</li><li data-i18n="home.order.4">დადასტურების შემდეგ ვამზადებთ და გიგზავნით შეკვეთას.</li></ol>{CTA()}</div></section>
<section id="blog"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow" data-i18n="home.blog.eyebrow">პუბლიკაციები</p><h2 data-i18n="home.blog.h2">ბლოგი</h2></div><p class="lead"><a href="/blog/" data-i18n="home.blog.all">ყველა სტატია →</a></p></div><ul class="blog-grid">{posts}</ul></div></section>
<section class="sec-stone" id="faq"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow" data-i18n="home.faq.eyebrow">კითხვები</p><h2 data-i18n="home.faq.h2">ხშირად დასმული კითხვები</h2></div></div><div class="faq-list">{fq}</div></div></section>
<section id="contact-cta"><div class="wrap"><div class="contact-band reveal"><div><p class="eyebrow" data-i18n="home.cta.eyebrow">კონტაქტი</p><h2 data-i18n="home.cta.h2">ფასის მოთხოვნა</h2><p class="lead" data-i18n="home.cta.lead">გამოგვიგზავნეთ ფასადის ფოტო, ნახაზი ან მოდელების სია და დაგიზუსტებთ ფასს, ზომებსა და ვადას.</p></div><div>{CTA()}</div></div></div></section>'''
page('/',f'EPS ფასადის დეკორი: კარნიზები, სვეტები, პანელები | {NAME}','ფასადის დეკორატიული ელემენტები პოლისტირონისგან (EPS): კარნიზები, სვეტები, კუთხის ქვები, ფასადის პანელები, თაღები. წარმოება საქართველოში.',body,
 [{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a_}} for q,a_ in FAQ]}],home=True)

# ---------- products index
body=crumbs_html([('მთავარი','/'),('პროდუქცია','/products/')])+f'<section><div class="wrap"><div class="page-hero reveal"><p class="eyebrow" data-i18n="products.eyebrow">კატალოგი</p><h1 data-i18n="products.h1">EPS ფასადის დეკორის კატალოგი</h1><p class="lead" data-i18n="products.lead">12 კატეგორია: კარნიზებიდან სვეტებამდე და ფასადის პანელებამდე. თითოეული პროდუქტის გვერდზე ნახავთ ზომებს.</p></div><div class="cat-grid">{cats_html}</div></div></section>'
page('/products/','EPS ფასადის დეკორის კატალოგი – კარნიზები, სვეტები, პანელები | '+NAME,'EPS ფასადის დეკორის სრული კატალოგი: კარნიზები, ფანჯრის საპირეები, სვეტები, კუთხის ქვები, ფასადის პანელები, თაღები და სხვა.',body,
 [crumbs_ld([('მთავარი','/'),('პროდუქცია','/products/')])])

# ---------- category pages
for c,cd in CAT.items():
    ps=[p for p in P if p['cat']==c]
    others=''.join(f'<li><a href="/products/{o}/" data-i18n="cat.{o}">{E(CAT[o]["title"])}</a></li>' for o in CAT if o!=c)
    cr=[('მთავარი','/'),('პროდუქცია','/products/'),(cd['title'],f'/products/{c}/')]
    cards=''.join(card(p,i+1) for i,p in enumerate(ps))
    body=crumbs_html(cr)+f'<section><div class="wrap"><div class="page-hero reveal"><p class="eyebrow" data-i18n="cat.eyebrow">კატეგორია</p><h1 data-i18n="cat.{c}">{E(cd["title"])}</h1><p class="lead">{E(cd["intro"])} EPS (გაფართოებული პოლისტირონი) მსუბუქია და ფასადზე სწრაფად მაგრდება. აირჩიეთ პროდუქტი ზომების სანახავად.</p></div><div class="grid">{cards}</div><h2 class="sub reveal" data-i18n="cat.others">სხვა კატეგორიები</h2><ul class="chiplist">{others}</ul></div></section>'
    page(f'/products/{c}/',f'{cd["title"]} – EPS ფასადის დეკორი | {NAME}',f'{cd["title"]} პოლისტირონისგან (EPS): {len(ps)} პროდუქტი, ზომები და შეკვეთა საქართველოში. {cd["intro"]}'[:300],body,
     [crumbs_ld(cr),{"@type":"CollectionPage","name":cd['title'],"url":BASE+f'/products/{c}/',"inLanguage":"ka"},{"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":i+1,"url":BASE+p['url'],"name":p['name']} for i,p in enumerate(ps)]}])

# ---------- product pages
for p in P:
    cd=CAT[p['cat']]; sz=p['sizes']
    rows=''.join(f'<tr><td>{E(m)}</td><td>{E(s)}</td></tr>' for m,s in sz)
    multi=len(sz)>1
    if multi: szs=f'ხელმისაწვდომია {len(sz)} ზომაში: '+'; '.join(s for _,s in sz)+'.'
    else: szs=f'ზომა: {sz[0][1]}.'
    d1=f'{p["name"]} არის EPS (გაფართოებული პოლისტირონის) დეკორატიული ელემენტი ფასადისთვის. {cd["use"]}'
    if p['note']: d1+=' '+p['note']
    d2='ელემენტი ფასადზე მაგრდება სპეციალური წებოვანი ხსნარით, საჭიროებისამებრ დუბელებით. დამაგრების შემდეგ ზედაპირი იფარება დამცავი ფენით და იღებება. ფასისა და ხელმისაწვდომობის დასაზუსტებლად დაგვიკავშირდით.'
    rel=[x for x in P if x['cat']==p['cat'] and x is not p]
    i=P.index(p); rel=(rel[rel.index(next((x for x in rel if P.index(x)>i),rel[0] if rel else None)):]+rel)[:4] if rel else []
    cr=[('მთავარი','/'),('პროდუქცია','/products/'),(cd['title'],f'/products/{p["cat"]}/'),(p['name'],p['url'])]
    meta=(f'მოდელი: {E(p["code"])} · ' if p['code'] else '')+f'კატეგორია: <a href="/products/{p["cat"]}/">{E(cd["title"])}</a> · მასალა: EPS'
    body=crumbs_html(cr)+f'''<section><div class="wrap"><article class="prod reveal"><div class="pimg">{img(p["imgurl"],p["wh"],p["name"]+" – EPS დეკორატიული ელემენტი ფასადისთვის",False)}</div><div><p class="eyebrow" data-i18n="prod.eyebrow">პროდუქტი</p><h1>{E(p["name"])}</h1><p class="meta">{meta}</p><p>{E(d1)}</p><h2 data-i18n="prod.sizes">ზომები</h2><div class="tw"><table><thead><tr><th data-i18n="prod.model">მოდელი</th><th data-i18n="prod.size">ზომა</th></tr></thead><tbody>{rows}</tbody></table></div><p class="note">{E(szs)} სხვა ზომის საჭიროების შემთხვევაში დაგვიკავშირდით.</p>{CTA()}</div></article>
<h2 class="reveal" data-i18n="prod.desc">აღწერა და გამოყენება</h2><p class="lead reveal">{E(d2)}</p>
<h2 class="sub reveal" data-i18n="prod.related">მსგავსი პროდუქტები</h2><div class="grid">{"".join(card(x) for x in rel)}</div></div></section>'''
    props=[{"@type":"PropertyValue","name":"ზომა ("+m+")","value":s} for m,s in sz]
    prod={"@type":"Product","name":p['name'],"description":d1+' '+szs,"image":BASE+p['imgurl'],"url":BASE+p['url'],"category":cd['title'],"material":"გაფართოებული პოლისტირონი (EPS)","additionalProperty":props,"manufacturer":{"@id":BASE+"/#org"}}
    if p['code']: prod['sku']=p['code']
    if ok(NAME): prod['brand']={"@type":"Brand","name":NAME}
    page(p['url'],f'{p["name"]} – EPS {cd["single"]}{", "+sz[0][1] if not multi and "დაზუსტდება" not in sz[0][1] and "მზადდება" not in sz[0][1] else ""} | {NAME}',(f'{p["name"]}: EPS ფასადის დეკორი. {szs} შეკვეთა და მიწოდება საქართველოში.')[:300],body,[crumbs_ld(cr),prod],og=BASE+p['imgurl'])

# ---------- blog
bl=''.join(f'<li class="reveal"><a href="/blog/{s}/"><b>{E(t)}</b></a><p>{E(d)}</p></li>' for s,t,d,_ in BLOG)
body=crumbs_html([('მთავარი','/'),('ბლოგი','/blog/')])+f'<section><div class="wrap"><div class="page-hero reveal"><p class="eyebrow" data-i18n="blog.eyebrow">პუბლიკაციები</p><h1 data-i18n="blog.h1">ბლოგი: EPS ფასადის დეკორი</h1><p class="lead" data-i18n="blog.lead">რჩევები ფასადის დეკორის არჩევის, გამოყენებისა და მონტაჟის შესახებ.</p></div><ul class="plain big">{bl}</ul></div></section>'
page('/blog/','ბლოგი – EPS ფასადის დეკორის რჩევები | '+NAME,'სტატიები EPS ფასადის დეკორის არჩევის, გამოყენებისა და მონტაჟის შესახებ.',body,[crumbs_ld([('მთავარი','/'),('ბლოგი','/blog/')])])
for s,t,d,b in BLOG:
    cr=[('მთავარი','/'),('ბლოგი','/blog/'),(t,f'/blog/{s}/')]
    body=crumbs_html(cr)+f'<section><div class="wrap narrow"><article class="reveal"><p class="eyebrow">სტატია</p><h1>{E(t)}</h1><p class="meta">გამოქვეყნდა: <time datetime="{TODAY}">{TODAY}</time></p>{b}{CTA()}</article></div></section>'
    page(f'/blog/{s}/',f'{t} | {NAME}',d,body,[crumbs_ld(cr),{"@type":"Article","headline":t,"description":d,"inLanguage":"ka","datePublished":TODAY,"dateModified":TODAY,"mainEntityOfPage":BASE+f'/blog/{s}/',"image":BASE+"/img/og-image.jpg","author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"}}],typ='article')

# ---------- contact
rows=[]
if phones(): rows.append(f'<dt data-i18n="contact.phone">ტელეფონი</dt><dd>{phones_html("<br>")}</dd>')
if cfg['whatsapp']: rows.append(f'<dt data-i18n="contact.whatsapp">WhatsApp</dt><dd><a href="{E(cfg["whatsapp"])}" rel="noopener" data-i18n="contact.write">მოგვწერეთ</a></dd>')
addr=f'{E(cfg["street"])}, {E(cfg["city"])}'
rows.append(f'<dt data-i18n="contact.email">ელფოსტა</dt><dd><a href="mailto:{E(cfg["email"])}">{E(cfg["email"])}</a></dd><dt data-i18n="contact.address">მისამართი</dt><dd data-i18n-street data-ka="{addr}">{addr}</dd><dt data-i18n="contact.hours">სამუშაო საათები</dt><dd data-i18n-hours data-ka="{E(cfg["hours"])}">{E(cfg["hours"])}</dd>')
for k,l in (('facebook','Facebook'),('instagram','Instagram')):
    if cfg[k]: rows.append(f'<dt>{l}</dt><dd><a href="{E(cfg[k])}" rel="noopener">{l}</a></dd>')
mp=f'<div class="map"><iframe src="{E(cfg["map_embed_src"])}" title="რუკა: {E(NAME)}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>' if cfg['map_embed_src'] else ''
body=crumbs_html([('მთავარი','/'),('კონტაქტი','/contact/')])+f'<section class="contact"><div class="wrap"><div class="page-hero reveal"><p class="eyebrow" data-i18n="contact.eyebrow">დაგვიკავშირდით</p><h1 data-i18n="contact.h1">კონტაქტი</h1><p class="lead" data-i18n="contact.lead">გამოგვიგზავნეთ ფასადის ფოტო, ნახაზი ან მოდელების სია და დაგიზუსტებთ ფასს, ზომებსა და ვადას.</p></div><dl class="reveal">{"".join(rows)}</dl>{mp}</div></section>'
page('/contact/',f'კონტაქტი – {NAME} | EPS ფასადის დეკორი','დაგვიკავშირდით EPS ფასადის დეკორის შეკვეთისთვის: ტელეფონი, ელფოსტა, მისამართი და რუკა.',body,[crumbs_ld([('მთავარი','/'),('კონტაქტი','/contact/')]),{"@type":"ContactPage","url":BASE+"/contact/","inLanguage":"ka"}])

# ---------- 404
page('/404.html','გვერდი ვერ მოიძებნა | '+NAME,'მოთხოვნილი გვერდი ვერ მოიძებნა.','<section><div class="wrap"><div class="page-hero reveal"><h1>გვერდი ვერ მოიძებნა</h1><p class="lead">შეიძლება ბმული შეცვლილია. გადადით <a href="/">მთავარ გვერდზე</a> ან <a href="/products/">კატალოგში</a>.</p></div></div></section>',noindex=True)

# ---------- sitemap, robots, llms, vercel
urls=''.join(f'<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>' for u in PAGES)
open(OUT+'/sitemap.xml','w',encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(OUT+'/robots.txt','w',encoding='utf-8').write(f'User-agent: *\nAllow: /\n\nUser-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
ll=[f'# {NAME}','',f'> EPS (გაფართოებული პოლისტირონის) დეკორატიული ფასადის ელემენტების მწარმოებელი საქართველოში: კარნიზები, სვეტები, კუთხის ქვები, ფასადის პანელები, თაღები.','','## კატალოგი']
ll+=[f'- [{CAT[c]["title"]}]({BASE}/products/{c}/): {CAT[c]["intro"]}' for c in CAT]
ll+=['','## ბლოგი']+[f'- [{t}]({BASE}/blog/{s}/): {d}' for s,t,d,_ in BLOG]+['','## კონტაქტი',f'- [კონტაქტი]({BASE}/contact/)']
open(OUT+'/llms.txt','w',encoding='utf-8').write('\n'.join(ll)+'\n')
json.dump({"cleanUrls":True,"trailingSlash":True,"headers":[
 {"source":"/img/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"}]},
 {"source":"/fonts/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=31536000, immutable"},{"key":"Access-Control-Allow-Origin","value":"*"}]},
 {"source":"/css/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=86400"}]},
 {"source":"/js/(.*)","headers":[{"key":"Cache-Control","value":"public, max-age=86400"}]},
 {"source":"/(.*)","headers":[{"key":"X-Content-Type-Options","value":"nosniff"},{"key":"Referrer-Policy","value":"strict-origin-when-cross-origin"},{"key":"X-Frame-Options","value":"SAMEORIGIN"}]}]},open(OUT+'/vercel.json','w'),indent=1)

# sync dist → repo root (parent of generator/)
ROOT=os.path.abspath('..')
SKIP={'generator','.git','.cursor'}
for item in os.listdir(OUT):
    src=os.path.join(OUT,item)
    dst=os.path.join(ROOT,item)
    if os.path.isdir(src):
        if os.path.exists(dst): shutil.rmtree(dst)
        shutil.copytree(src,dst)
    else:
        shutil.copy2(src,dst)

print(len(PAGES),'indexable pages;',len(P),'products; synced to',ROOT)
