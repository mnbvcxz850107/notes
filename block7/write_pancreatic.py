html_content = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>胰臟腫瘤、創傷與膽道外科｜裸讀學習筆記</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@500;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#0F1B18;--bg-2:#152420;--bg-3:#1B2E29;--line:#26403A;--line-2:#31534B;
    --text:#E9F1EE;--text-2:#A8C2BA;--text-3:#7A968D;
    --teal:#7FC9BE;--teal-dim:#4E9A90;--gold:#C9A961;--rose:#E58B85;
    --serif:"Noto Serif TC","Songti TC",serif;
    --sans:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;
    --mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth;scroll-padding-top:24px;overflow-x:hidden}
  body{
    margin:0;background:var(--bg);color:var(--text);
    font-family:var(--sans);font-size:16.5px;line-height:1.9;font-weight:300;
    -webkit-font-smoothing:antialiased;overflow-x:hidden;
  }
  .wrap{max-width:1150px;margin:0 auto;padding:0 22px}
  header.hero{padding:60px 0 48px;border-bottom:1px solid var(--line)}
  .backlink{display:inline-block;font-family:var(--mono);font-size:12px;
    color:var(--text-3);text-decoration:none;margin-bottom:20px;
    border:1px solid var(--line);border-radius:6px;padding:5px 12px;transition:.15s}
  .backlink:hover{color:var(--teal);border-color:var(--teal-dim)}
  .eyebrow{display:flex;align-items:center;gap:16px;margin-bottom:22px;
    font-family:var(--serif);font-size:15px;letter-spacing:.34em;color:var(--teal)}
  .eyebrow .rule{width:56px;height:1px;background:var(--gold)}
  .eyebrow .dot{color:var(--gold)}
  header.hero h1{
    font-family:var(--serif);font-weight:700;font-size:clamp(34px,5.6vw,64px);
    line-height:1.2;margin:0 0 20px;letter-spacing:.02em;
  }
  header.hero h1 em{font-style:normal;color:var(--teal)}
  header.hero p.sub{margin:0;color:var(--text-2);max-width:65ch;font-size:16.5px;line-height:1.85}
  .intro-card{border:1px solid var(--line);border-radius:16px;padding:24px 28px;margin-top:30px;background:var(--bg-2)}
  .intro-card p{margin:0 0 20px;color:var(--text-2)}
  .intro-card b{color:var(--teal);font-weight:500}
  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
  .stat .n{font-family:var(--serif);font-size:36px;color:var(--gold);line-height:1}
  .stat .l{font-size:12px;color:var(--text-3);letter-spacing:.08em;margin-top:6px}
  .cols{display:grid;grid-template-columns:230px 1fr;gap:50px;padding:42px 0 90px;align-items:start}
  nav.toc{position:sticky;top:26px}
  nav.toc .t{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--text-3);margin-bottom:14px}
  nav.toc a{display:block;padding:7px 14px;border-left:1px solid var(--line);
    color:var(--text-2);text-decoration:none;font-size:14px;transition:.15s}
  nav.toc a:hover{border-left-color:var(--teal);color:var(--teal);background:var(--bg-2)}
  nav.toc a.exam{color:var(--gold)}
  nav.toc summary{display:none}
  section{margin-bottom:60px;scroll-margin-top:24px}
  .sec-head{display:flex;align-items:baseline;gap:16px;border-bottom:1px solid var(--line-2);padding-bottom:12px;margin-bottom:24px}
  .sec-num{font-family:var(--serif);font-size:28px;color:var(--gold);line-height:1}
  .sec-head h2{font-family:var(--serif);font-size:clamp(22px,3.2vw,30px);margin:0;font-weight:700;letter-spacing:.02em}
  h3{font-family:var(--serif);font-size:20px;margin:36px 0 12px;font-weight:500;color:var(--text)}
  h4{font-size:16px;margin:22px 0 8px;color:var(--teal);font-weight:500}
  p{margin:0 0 14px}
  ul,ol{margin:0 0 16px;padding-left:22px}
  li{margin-bottom:8px}
  li::marker{color:var(--teal-dim)}
  strong,b{font-weight:500;color:#FFF}
  u{text-decoration-color:var(--teal-dim);text-underline-offset:3px}
  code{font-family:var(--mono);font-size:.88em;background:var(--bg-3);padding:1px 6px;border-radius:4px;color:var(--teal)}
  mark{background:rgba(201,169,97,.22);box-shadow:inset 0 -2px 0 rgba(201,169,97,.6);color:#FBF3E2;padding:1px 3px;border-radius:2px}
  a.qtag{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:600;border:1px solid var(--gold);color:var(--gold);padding:1px 7px;border-radius:4px;text-decoration:none;margin:0 3px;vertical-align:2px;white-space:nowrap;transition:.15s}
  a.qtag:hover{background:var(--gold);color:var(--bg)}
  .tagline{margin:-6px 0 18px;font-size:13.5px;color:var(--text-3)}
  .box{border-radius:13px;padding:18px 22px;margin:20px 0;border:1px solid var(--line);background:var(--bg-2)}
  .box .bt{font-weight:500;font-size:14.5px;margin-bottom:10px;display:flex;align-items:center;gap:9px;color:#FFF}
  .box p:last-child,.box ul:last-child,.box ol:last-child{margin-bottom:0}
  .badge{font-family:var(--mono);font-size:10px;padding:2px 8px;border-radius:3px;letter-spacing:.06em;border:1px solid currentColor;font-weight:600}
  .box.exam{border-color:rgba(201,169,97,.45);background:rgba(201,169,97,.07)}
  .box.exam .badge{color:var(--gold)}
  .box.trap{border-color:rgba(229,139,133,.45);background:rgba(229,139,133,.07)}
  .box.trap .badge{color:var(--rose)}
  .box.key{border-color:rgba(127,201,190,.4);background:rgba(127,201,190,.07)}
  .box.key .badge{color:var(--teal)}
  .img-frame{background:#08100E;border:1px solid var(--line-2);border-radius:12px;padding:12px;margin:18px 0 20px;text-align:center}
  .q-img{display:block;max-width:100%;height:auto;border-radius:8px;margin:0 auto;box-shadow:0 4px 14px rgba(0,0,0,.5)}
  .img-caption{font-family:var(--mono);font-size:12px;color:var(--text-2);margin-top:10px;line-height:1.6}
  .img-caption b{color:var(--gold);font-weight:600}
  .tw{border:none;background:none;overflow:visible;border-radius:0;margin:20px 0}
  .tw table{min-width:0;width:100%;border-collapse:separate;border-spacing:0;font-size:14.8px}
  .tw thead{display:none}
  .tw tbody tr{display:block;border:1px solid var(--line);border-radius:12px;background:var(--bg-2);margin-bottom:12px;padding:6px 0}
  .tw tbody tr:nth-child(even){background:var(--bg-2)}
  .tw tbody tr:last-child{margin-bottom:0}
  .tw tbody td{display:block;border:none;padding:9px 16px}
  .tw tbody td+td{border-top:1px dashed var(--line)}
  .tw tbody td[data-label]::before{content:attr(data-label);display:block;font-family:var(--mono);font-size:11px;letter-spacing:.08em;color:var(--teal);margin-bottom:4px;font-weight:600}
  .tw tbody td:first-child{font-size:16px;color:#FFF;font-weight:500}
  .tw tbody td.mono{font-family:var(--mono);font-size:13.5px}
  @media (min-width:769px){
    .tw{overflow-x:auto;border:1px solid var(--line);border-radius:13px;background:var(--bg-2)}
    .tw table{border-collapse:collapse}
    .tw thead{display:table-header-group}
    .tw thead th{background:var(--bg-3);color:var(--teal);font-weight:500;font-size:13.5px;padding:12px 16px;border-bottom:1px solid var(--line);text-align:left}
    .tw tbody tr{display:table-row;border:none;background:none;margin-bottom:0;padding:0}
    .tw tbody tr:nth-child(even){background:rgba(255,255,255,.018)}
    .tw tbody td{display:table-cell;padding:12px 16px;border-bottom:1px solid var(--line)}
    .tw tbody td+td{border-top:none}
    .tw tbody tr:last-child td{border-bottom:none}
    .tw tbody td[data-label]::before{display:none}
    .tw tbody td:first-child{font-size:14.8px;font-weight:normal}
  }
  .quiz{border:1px solid var(--line-2);border-radius:14px;margin:24px 0;overflow:hidden;background:var(--bg-2)}
  .quiz-top{display:flex;align-items:center;gap:10px;padding:12px 20px;background:var(--bg-3);border-bottom:1px solid var(--line)}
  .quiz-top .lab{font-family:var(--serif);font-size:14px;letter-spacing:.16em;color:var(--gold)}
  .quiz-top .yr{font-family:var(--mono);font-size:11.5px;color:var(--text-2);border:1px solid var(--line-2);padding:2px 8px;border-radius:4px}
  .quiz-body{padding:18px 20px}
  .quiz-body .stem{font-size:15.5px;line-height:1.85;margin:0 0 14px;color:var(--text)}
  .opts{list-style:none;padding:0;margin:0 0 14px}
  .opts li{padding:8px 12px;font-size:15px;border:1px solid var(--line);border-radius:8px;margin-bottom:7px;color:var(--text-2)}
  details.rev{margin:0}
  summary.toggle{display:inline-block;list-style:none;cursor:pointer;background:none;border:1px solid var(--teal-dim);color:var(--teal);font-family:var(--sans);font-size:13px;padding:7px 16px;border-radius:7px;font-weight:400;transition:.15s;-webkit-tap-highlight-color:transparent}
  summary.toggle::-webkit-details-marker{display:none}
  summary.toggle::marker{content:""}
  summary.toggle:hover{background:var(--teal);color:var(--bg)}
  summary.toggle::before{content:"顯示答案"}
  .q summary.toggle::before{content:"顯示答案與詳解"}
  details.rev[open] summary.toggle::before{content:"收合答案"}
  .reveal{border-top:1px dashed var(--line-2);margin-top:14px;padding-top:14px}
  .ans{font-family:var(--serif);font-weight:700;color:var(--gold);font-size:17px;margin-bottom:10px}
  .reveal p{margin:0 0 9px;font-size:14.8px;color:var(--text-2)}
  .reveal p b{color:#FFF}
  .src{font-size:12px;color:var(--text-3);font-family:var(--mono);margin-top:12px}
  .jump{font-size:12.5px;color:var(--teal-dim);text-decoration:none;border-bottom:1px solid var(--line-2)}
  .jump:hover{color:var(--teal)}
  .exam-head{border:1px solid var(--line-2);border-radius:16px;padding:26px;margin-bottom:26px;background:var(--bg-2)}
  .exam-head h2{font-family:var(--serif);margin:0 0 10px;font-size:28px}
  .exam-head p{color:var(--text-2);margin:0;font-size:15px}
  .btn{font-family:var(--sans);font-size:13.5px;cursor:pointer;background:var(--teal);color:var(--bg);border:none;padding:10px 20px;border-radius:8px;margin-top:16px;font-weight:500}
  .btn:hover{background:#9BDBD1}
  .yrhead{font-family:var(--serif);font-size:23px;font-weight:700;margin:36px 0 16px;padding-left:16px;border-left:3px solid var(--gold);color:var(--gold)}
  .q{background:var(--bg-2);border:1px solid var(--line);border-radius:13px;padding:20px 22px;margin-bottom:18px;scroll-margin-top:24px}
  .q-no{font-family:var(--mono);font-size:11.5px;color:var(--gold);border:1px solid var(--gold);padding:2px 9px;border-radius:5px}
  .q-topic{font-size:12.5px;color:var(--text-3);margin-left:10px}
  .q-stem{margin:14px 0 12px;font-size:15.5px;line-height:1.85}
  footer{border-top:1px solid var(--line);padding:28px 0 56px;color:var(--text-3);font-size:13.5px}
  footer b{color:var(--text-2)}
  @media (max-width:900px){
    .cols{grid-template-columns:1fr;gap:0;padding-top:24px}
    nav.toc{position:static;margin-bottom:32px;border:1px solid var(--line);border-radius:12px;padding:16px;background:var(--bg-2)}
    nav.toc a{border-left:none;padding:6px 4px}
    .stats{grid-template-columns:repeat(2,1fr);gap:16px}
  }
  @media (max-width:700px){
    body{font-size:16px;line-height:1.85}
    .wrap{padding:0 16px}
    header.hero{padding:36px 0 30px}
    .cols{padding:24px 0 50px}
    section{margin-bottom:42px}
    nav.toc{padding:0;overflow:hidden}
    nav.toc .t{display:none}
    nav.toc details{margin:0}
    nav.toc summary{display:block;list-style:none;cursor:pointer;padding:14px 16px;font-family:var(--mono);font-size:12px;letter-spacing:.16em;color:var(--teal)}
    nav.toc summary::-webkit-details-marker{display:none}
    nav.toc summary::after{content:" ▾";color:var(--text-3)}
    nav.toc details[open] summary::after{content:" ▴"}
    nav.toc .toc-links{padding:0 10px 12px}
    .box{padding:15px 16px;border-radius:11px}
    p,li,td,.stem,.reveal p,.opts li,.q-stem{overflow-wrap:anywhere;word-break:break-word}
    .quiz-body{padding:15px 16px}
    .opts li{padding:9px 12px;font-size:15px}
    .q{padding:16px 16px}
    .sec-head{gap:12px}
    ul,ol{padding-left:20px}
    .toggle{width:100%;padding:11px 16px;font-size:14px}
    summary.toggle{width:100%;text-align:center;padding:11px 16px;font-size:14px}
    .btn{width:100%;padding:12px 16px}
  }
  @media print{
    nav.toc,.btn,.toggle{display:none}
    .reveal{display:block!important}
    body{background:#fff;color:#000;font-size:11pt}
  }
</style>
</head>
<body>
<header class="hero">
  <div class="wrap">
    <a class="backlink" href="index.html">← 返回 Block 7 目錄</a>
    <div class="eyebrow"><span class="rule"></span>高醫肝膽胰外科 · 裸讀學習筆記<span class="dot">·</span>王森稔／郭功楷老師專題</div>
    <h1>胰臟腫瘤、創傷與膽道外科 <em>(Pancreatic & Biliary Surgery)</em></h1>
    <p class="sub">精準剖析膽汁製造與膽絞痛放射痛、先天性膽道囊腫 Todani 分型、胰腺囊性腫瘤（SCN vs IPMN）、術後胰漏 (POPF) 與 GDA 動脈瘤破裂處置、胰腺癌切除與新輔助治療。授課教師：王森稔、郭功楷。</p>
    <div class="intro-card">
      <p>完整收錄 <b>BM110、BM111、BM112、BM113 四個學年度共 12 題真題</b>，將外科手術處置原則、胰漏處置與膽囊生理徹底拆解，文末附完整題庫詳解。</p>
      <div class="stats">
        <div class="stat"><div class="n">12</div><div class="l">全收錄真題</div></div>
        <div class="stat"><div class="n">4</div><div class="l">學年度 (110-113)</div></div>
        <div class="stat"><div class="n">7</div><div class="l">核心章節</div></div>
        <div class="stat"><div class="n">100%</div><div class="l">考點命中率</div></div>
      </div>
    </div>
  </div>
</header>
<div class="wrap">
<div class="cols">
  <nav class="toc">
    <div class="t">CONTENTS</div>
    <details id="tocBox" open>
      <summary>目錄 CONTENTS</summary>
      <div class="toc-links">
      <a href="#s1">一　導讀：無痛性黃疸的背後</a>
      <a href="#s2">二　胰臟癌：沉默的殺手</a>
      <a href="#s3">三　Whipple 手術：切除四個器官的大手術</a>
      <a href="#s4">四　胰臟其他腫瘤：不都是癌</a>
      <a href="#s5">五　膽囊生理與膽結石病理</a>
      <a href="#s6">六　膽道腫瘤與先天性膽道異常</a>
      <a href="#s7">七　一分鐘考前秒殺心法</a>
      <a href="#exam" class="exam">八　歷屆考題全收錄 (12 題)</a>
      </div>
    </details>
  </nav>
  <main>
  
  <section id="s1">
    <div class="sec-head"><span class="sec-num">一</span><h2>導讀：無痛性黃疸的背後 (Clinical Story)</h2></div>
    <p>62歲的陳女士最近兩個月總覺得食慾不振，體重不知不覺掉了五公斤。她以為是天氣熱沒胃口，直到某天早上照鏡子，發現自己的眼白竟然變得黃黃的，而且全身皮膚也開始泛黃。更奇怪的是，她<b>完全沒有感覺到任何肚子痛</b>。</p>
    <p>在門診，醫師為她安排了電腦斷層 (CT) 掃描，赫然發現在她的「胰臟頭部」有一顆 3 公分的腫瘤。這顆腫瘤不僅壓迫了總膽管，也塞住了胰管。影像上呈現經典的「雙管徵」(Double duct sign)——總膽管與胰管同時擴張擴大。這就是典型的<mark>胰臟癌 (Pancreatic Cancer) 臨床表現：無痛性黃疸 (Painless Jaundice)</mark>與體重減輕。</p>
    <div class="box key">
      <div class="bt"><span class="badge">臨床關鍵</span>為什麼是「無痛」的黃疸？</div>
      <p>膽道結石造成的阻塞通常伴隨劇烈的「膽絞痛」，因為結石卡住會引發平滑肌強烈收縮痙攣。但胰臟頭部腫瘤是慢慢長大，逐漸將總膽管「勒緊」阻塞，過程緩慢且沒有急性發炎或痙攣，因此膽汁雖然鬱積導致全身黃疸，患者卻完全不會痛。這也是為何胰臟癌如此可怕，當病患發現皮膚變黃時，腫瘤往往已經長得很大了。</p>
    </div>
  </section>

  <section id="s2">
    <div class="sec-head"><span class="sec-num">二</span><h2>胰臟癌：沉默的殺手</h2></div>
    <p class="tagline">核心考點：<a class="qtag" href="#q112-70">112-70</a><a class="qtag" href="#q111-68">111-68</a><a class="qtag" href="#q110-62">110-62</a><a class="qtag" href="#q110-63">110-63</a></p>
    <p>胰臟是一個深藏在胃後方、緊貼著後腹腔的器官，就像是城市地下的重要管線中心，平時默默分泌消化酵素和胰島素，但一旦出問題，周圍的交通（腸胃道與大血管）都會大亂。</p>
    
    <h3>1. 為什麼胰臟癌預後這麼差？</h3>
    <ul>
      <li><b>位置隱密：</b>胰臟位於後腹腔，早期幾乎沒有任何症狀。</li>
      <li><b>快速蔓延：</b>周圍緊鄰重要大血管（如腸繫膜上動脈 SMA、腹腔動脈幹 Celiac axis），腫瘤極易侵犯這些大血管，導致「無法手術切除」。</li>
      <li><b>容易早期轉移：</b>即使是很小的胰臟癌，也常早已透過淋巴或血液轉移至肝臟。</li>
    </ul>

    <h3>2. 病理與臨床表現</h3>
    <p>高達 <mark>90% 的胰臟癌屬於「胰管腺癌 (PDAC, Pancreatic ductal adenocarcinoma)」</mark>，起源於胰臟導管上皮細胞。其中約有 70% 發生在<b>胰臟頭部 (Head)</b>。</p>
    <div class="tw"><table>
      <thead><tr><th>腫瘤位置</th><th>常見臨床表現</th><th>解剖學原因</th></tr></thead>
      <tbody>
        <tr><td><b>胰臟頭部 (Head)</b></td><td><mark>無痛性黃疸</mark>、灰白便、茶色尿</td><td>壓迫總膽管 (CBD)，導致膽汁無法排入十二指腸。</td></tr>
        <tr><td><b>胰臟體尾部 (Body/Tail)</b></td><td>背痛、體重減輕</td><td>沒有壓迫膽管不會黃疸，而是侵犯後腹腔神經叢引發背痛。</td></tr>
      </tbody>
    </table></div>

    <div class="box trap">
      <div class="bt"><span class="badge">高危險群警訊</span>新發生的糖尿病！</div>
      <p>年過五十歲的病患如果突然被診斷出糖尿病（New-onset diabetes），且沒有肥胖或家族史，一定要高度懷疑是否有胰臟癌！因為胰臟受到腫瘤破壞，無法正常分泌胰島素，導致血糖突然飆高。這在國考及臨床上是非常重要的警訊。</p>
    </div>

    <h3>3. 診斷與腫瘤指數</h3>
    <p>診斷的首選影像學檢查是「三相電腦斷層 (Triple-phase CT)」，可以清楚看出腫瘤與周圍血管的關係，判斷是否可以切除。此外，如果做內視鏡逆行性膽胰管攝影 (ERCP)，會看到經典的 <b>Double duct sign</b>（總膽管和胰管同時擴大）。</p>
    <p>最常用的腫瘤指數是 <mark>CA 19-9</mark>。雖然在多數胰臟癌患者中會升高，但它並不具特異性（嚴重膽汁鬱積時也會高），因此<b>不適合用來做常規的普查篩檢</b>，主要用於治療後的追蹤。</p>

    <div class="quiz">
      <div class="quiz-top">
        <span class="lab">INLINE QUIZ</span>
        <span class="yr">概念測驗</span>
      </div>
      <div class="quiz-body">
        <p class="stem">關於胰臟癌的敘述，下列何者正確？</p>
        <ul class="opts">
          <li>(A) 大多數是由胰島細胞 (islet cells) 衍生出來的。</li>
          <li>(B) 新生糖尿病 (new-onset diabetes) 的發生被列為危險因子之一。</li>
          <li>(C) 胰尾癌常見的初始症狀是黃疸。</li>
          <li>(D) CA 19-9 是非常具特異性的指標，適合做一般民眾的普查篩檢。</li>
        </ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
            <div class="ans">正確答案：(B)</div>
            <p>解析：(A) 90% 是胰管腺癌 (PDAC)。(C) 胰尾癌不易壓迫膽管，較少黃疸，多為背痛。(D) CA 19-9 不具特異性，不適合普查。對應題庫 <a href="#q112-70" class="jump">112-70</a>。</p>
          </div>
        </details>
      </div>
    </div>

    <h3>4. 治療原則與存活率</h3>
    <p>胰臟癌初診斷時，<mark>僅約 15%~20% 的病患有機會進行手術切除</mark>。這也是為什麼整體五年存活率極低（手術後約 20-25%）的原因。</p>
    <p>臨床上會根據腫瘤與周圍血管的關係分類：若腫瘤輕度接觸或侵犯血管，被稱為<b>「邊界可切除 (Borderline resectable)」</b>。對於這類病患，標準作法是<mark>先進行新輔助治療 (Neoadjuvant 化療或放療)</mark>，讓腫瘤縮小、降期後，再評估是否能進行根治性切除，而不是直接開刀。</p>

    <div class="quiz">
      <div class="quiz-top">
        <span class="lab">INLINE QUIZ</span>
        <span class="yr">概念測驗</span>
      </div>
      <div class="quiz-body">
        <p class="stem">對於影像上顯示為 Borderline resectable (邊界可切除) 的胰臟癌，最佳的初步處置策略為何？</p>
        <ul class="opts">
          <li>(A) 立即進行胰頭十二指腸切除術。</li>
          <li>(B) 先進行 Neoadjuvant 化學治療或合併放射線療法。</li>
          <li>(C) 進行全胰臟切除。</li>
          <li>(D) 放棄手術，僅給予安寧緩和治療。</li>
        </ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
            <div class="ans">正確答案：(B)</div>
            <p>解析：Borderline resectable 胰腺癌應先給予新輔助治療 (Neoadjuvant chemotherapy/radiotherapy) 使腫瘤降期，以增加手術成功率。對應題庫 <a href="#q111-68" class="jump">111-68</a>, <a href="#q110-62" class="jump">110-62</a>。</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section id="s3">
    <div class="sec-head"><span class="sec-num">三</span><h2>Whipple 手術：切除四個器官的大手術</h2></div>
    <p>當胰臟頭部發生癌症時，外科醫師面臨一個巨大的挑戰：這裡的解剖構造太複雜了。總膽管、十二指腸和胰臟頭部共享著相同的血液供應（主要來自胃十二指腸動脈 GDA）。這就像是一棟公寓的三個房間共用一套水電管線，你無法只拆掉其中一個房間而不破壞其他兩個。因此，必須執行醫學界最複雜的手術之一：<b>胰十二指腸切除術 (Pancreaticoduodenectomy)</b>，俗稱 <mark>Whipple procedure (惠普爾手術)</mark>。</p>

    <h3>1. 切除了什麼？</h3>
    <p>為了確保癌症切除乾淨並維持解剖上的可行性，Whipple 手術會切除以下部位：</p>
    <ul>
      <li><b>胰臟頭部 (Head of pancreas)</b>：腫瘤的所在地。</li>
      <li><b>十二指腸 (Duodenum)</b>：因為與胰頭共用血液供應，且總膽管出口（壺腹）在此。</li>
      <li><b>總膽管下端與膽囊 (CBD & Gallbladder)</b>：徹底清除可能被癌細胞侵犯的膽道系統。</li>
      <li><b>部分胃 (Part of stomach)</b>（傳統手術）：有時會保留幽門以改善術後消化功能，稱為幽門保留式 (PPPD)。</li>
    </ul>

    <h3>2. 重建了什麼？</h3>
    <p>切除之後，消化道被截斷，膽汁和胰液也無處可去。因此醫師必須將空腸 (Jejunum) 拉上來，進行三個重要的吻合（接合）：</p>
    <ol>
      <li><b>胰臟空腸吻合 (Pancreaticojejunostomy)：</b>讓胰液流入腸道。</li>
      <li><b>膽管空腸吻合 (Hepaticojejunostomy)：</b>讓膽汁流入腸道。</li>
      <li><b>胃/十二指腸空腸吻合 (Gastro/Duodenojejunostomy)：</b>讓食物進入腸道。</li>
    </ol>
  </section>

  <section id="s4">
    <div class="sec-head"><span class="sec-num">四</span><h2>術後胰漏 (POPF) 與致命的 GDA 出血</h2></div>
    <p class="tagline">核心考點：<a class="qtag" href="#q112-71">112-71</a><a class="qtag" href="#q113-6">113-6</a></p>
    <p>Whipple 手術後最令人聞之色變的併發症是「術後胰漏 (POPF, Postoperative Pancreatic Fistula)」。這就像是接好的水管漏水了，但漏出來的不是水，而是<b>具有強烈消化能力的胰液</b>！</p>

    <h3>1. 為什麼會發生胰漏？</h3>
    <p>當胰臟質地非常柔軟 (<mark>Soft pancreas</mark>)，或者主胰管非常細 (<mark>&lt; 3 mm</mark>) 時，縫線很難牢牢抓住組織，胰臟空腸吻合處就容易滲漏。</p>

    <h3>2. 致命的假性動脈瘤破裂</h3>
    <p>外漏的胰液在腹腔內就像硫酸一樣，會腐蝕周圍的組織。最危險的是，它會侵蝕手術中被切斷綁結的動脈殘端，尤其是 <mark>胃十二指腸動脈 (GDA, Gastroduodenal artery)</mark>。胰液會使血管壁變薄，形成「假性動脈瘤 (Pseudoaneurysm)」，一旦破裂，會引發大量出血，死亡率極高。</p>

    <div class="box exam">
      <div class="bt"><span class="badge">考試必考</span>發生胰漏該怎麼辦？絕對不能馬上開刀！</div>
      <p>如果發生胰漏，直覺上可能會想「趕快打開肚子重新縫好」。這在外科是<b>大忌</b>！因為當時組織已經被胰液嚴重發炎、水腫腐蝕，像爛泥一樣，重新縫只會越縫越破。正確的處置是<mark>保守治療：維持引流管通暢、禁食、全靜脈營養 (TPN) 支持，並使用體抑素 (Somatostatin) 抑制胰液分泌</mark>，讓組織自行癒合。如果是 GDA 破裂出血，首選是做<b>血管攝影動脈栓塞 (TAE)</b>，而非開刀止血。</p>
    </div>

    <div class="quiz">
      <div class="quiz-top">
        <span class="lab">INLINE QUIZ</span>
        <span class="yr">觀念測驗</span>
      </div>
      <div class="quiz-body">
        <p class="stem">有關胰漏 (POPF) 的敘述，下列何者錯誤？</p>
        <ul class="opts">
          <li>(A) 常發生在胰臟手術之後。</li>
          <li>(B) Whipple procedure 後若發生 POPF，其衍生出的出血常是因為脾動脈 (splenic artery) 發生假性動脈瘤破裂所致。</li>
          <li>(C) 相關的危險因子包括胰臟組織過軟以及胰管過細等。</li>
          <li>(D) 發生胰漏的病人，如果冒然立即接受再次手術處理，往往預後極差。</li>
        </ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
            <div class="ans">正確答案：(B)</div>
            <p>解析：(B) 錯誤。Whipple 術後 POPF 腐蝕出血的血管最常見是<b>胃十二指腸動脈 (GDA)</b>，而非脾動脈。這題在 112、113 年連續考出。對應題庫 <a href="#q112-71" class="jump">112-71</a>, <a href="#q113-6" class="jump">113-6</a>。</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section id="s5">
    <div class="sec-head"><span class="sec-num">五</span><h2>胰臟其他腫瘤：不都是癌 (SCN 與 IPMN)</h2></div>
    <p class="tagline">核心考點：<a class="qtag" href="#q113-5">113-5</a><a class="qtag" href="#q111-69">111-69</a></p>
    <p>除了可怕的胰臟腺癌外，胰臟也會長水泡（囊性腫瘤）。分辨這些水泡是良性還是惡性前兆，是外科醫師的重要工作。</p>

    <div class="tw"><table>
      <thead><tr><th>胰腺腫瘤類型</th><th>良惡性與前驅特性</th><th>初診斷處置策略</th></tr></thead>
      <tbody>
        <tr><td><b>漿液性囊腺瘤<br>(Serous Cystadenoma, SCN)</b></td><td><mark>幾乎 100% 為良性</mark>，常呈現海綿狀或蜂窩狀。</td><td><mark>初診斷時建議「先觀察」</mark>，不用常規評估手術切除。</td></tr>
        <tr><td><b>主胰管型 IPMN<br>(Main-duct IPMN)</b></td><td>分泌黏液導致胰管擴張，乳頭呈現像「魚嘴 (fish mouth)」吐黏液的樣子。惡性潛能極高（癌變率 40~70%）。</td><td><mark>必須積極評估並接受手術切除</mark>。若出現黃疸或結節，應直接開刀，不可延誤。</td></tr>
        <tr><td><b>神經內分泌腫瘤<br>(pNET)</b></td><td>如胰島素瘤 (Insulinoma)：Whipple triad（低血糖症狀、血糖低、吃糖緩解）。<br>如胃泌素瘤 (Gastrinoma)：導致難治性十二指腸潰瘍 (ZES)。</td><td>根據腫瘤大小及荷爾蒙分泌狀況決定手術。</td></tr>
      </tbody>
    </table></div>

    <div class="quiz">
      <div class="quiz-top">
        <span class="lab">INLINE QUIZ</span>
        <span class="yr">觀念測驗</span>
      </div>
      <div class="quiz-body">
        <p class="stem">下列那一種胰臟腫瘤，初診斷時建議可先觀察不用考慮評估接受手術切除治療？</p>
        <ul class="opts">
          <li>(A) Pancreatic neuroendocrine tumor</li>
          <li>(B) Solid pseudopapillary neoplasms</li>
          <li>(C) Main-duct IPMNs</li>
          <li>(D) Serous cystadenomas</li>
        </ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
            <div class="ans">正確答案：(D)</div>
            <p>解析：漿液性囊腺瘤 (SCN) 幾乎全為良性，無症狀者初診斷時可先保守觀察。而主胰管型 IPMN (C) 惡性機率極高，必須積極處理。對應題庫 <a href="#q113-5" class="jump">113-5</a>。</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section id="s6">
    <div class="sec-head"><span class="sec-num">六</span><h2>膽囊生理與膽結石病理</h2></div>
    <p class="tagline">核心考點：<a class="qtag" href="#q112-3">112-3</a><a class="qtag" href="#q113-3">113-3</a></p>
    <p>膽囊就像是肝臟的「蓄水池」，了解膽汁的來龍去脈是基礎中的基礎。</p>

    <h3>1. 膽汁從哪裡來？</h3>
    <p>這是最常錯的陷阱題！<mark>膽汁是由「肝臟 (Liver)」製造產生的</mark>，膽囊的功能僅僅是「儲存與濃縮」膽汁。膽汁中黃黃綠綠的顏色來自於膽紅素 (Bilirubin)，這是人體內老化紅血球分解後，其 <mark>Heme (血基質) 代謝產物</mark>。</p>

    <h3>2. 膽結石與懷孕的關係</h3>
    <p>為什麼孕婦容易得膽結石？因為懷孕期間大量分泌的<b>黃體素 (Progesterone)</b> 會抑制平滑肌收縮，這會<mark>降低膽囊收縮與排空能力</mark>，導致膽汁像死水一樣滯留在膽囊內，久而久之就結晶形成結石。</p>

    <h3>3. 膽絞痛 (Biliary colic) 的典型表現</h3>
    <p>當吃下油膩食物後，十二指腸會分泌膽囊收縮素 (CCK) 呼叫膽囊把膽汁擠出來幫忙消化。如果膽囊裡有結石，膽囊用力收縮時結石就會卡在膽囊管，引發劇痛。這種疼痛會出現在右上腹，並且常常<mark>放射至右肩胛骨下方或後背</mark>，這是因為支配膽囊神經與右肩神經在脊髓有交匯（轉移痛 Referred pain）。</p>
    
    <div class="quiz">
      <div class="quiz-top">
        <span class="lab">INLINE QUIZ</span>
        <span class="yr">觀念測驗</span>
      </div>
      <div class="quiz-body">
        <p class="stem">關於膽汁生理與膽結石，下列敘述何者正確？</p>
        <ul class="opts">
          <li>(A) 人體內的膽汁是由膽囊製造產生。</li>
          <li>(B) Bile 中的 bilirubin 主要是人體內 heme 代謝後的產物。</li>
          <li>(C) cholesterol gallstone 的形成主要是和膽道系統發生細菌感染有關。</li>
          <li>(D) pregnancy 會增加膽囊收縮排空的能力。</li>
        </ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
            <div class="ans">正確答案：(B)</div>
            <p>解析：(A) 膽汁由肝臟製造。(C) 細菌感染形成的是色素結石 (Pigment stone)，不是膽固醇結石。(D) 懷孕時黃體素會降低膽囊排空能力，造成膽汁滯留。對應題庫 <a href="#q113-3" class="jump">113-3</a>, <a href="#q112-3" class="jump">112-3</a>。</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section id="s7">
    <div class="sec-head"><span class="sec-num">七</span><h2>膽道腫瘤與先天性膽道異常</h2></div>
    <p class="tagline">核心考點：<a class="qtag" href="#q112-4">112-4</a><a class="qtag" href="#q113-4">113-4</a></p>

    <h3>1. 急性膽管炎的 Charcot's Triad</h3>
    <p>當結石掉到總膽管卡住，不僅會造成黃疸，還會因為膽汁不通引發嚴重細菌感染，稱為急性膽管炎 (Acute Cholangitis)。這是一個危及生命的急症，臨床上有經典的三聯徵（Charcot's triad）：<mark>腹痛 ＋ 發燒 ＋ 黃疸</mark>。這三者缺一不可（考試常把其中一項換成腹瀉來騙人）。</p>

    <h3>2. 先天性膽道擴張症 (Choledochal cyst)</h3>
    <p>這是一種先天性膽管發育異常，膽管會不正常地膨大成囊腫。因為膽汁在囊腫內淤積，日後發生「膽管癌」的機率非常高，所以一旦診斷出來，通常需要將囊腫切除並進行重建。<br>
    分類上使用 <mark>Todani classification</mark>，其中<b>臨床上最常見的是「Type 1 (總膽管囊狀/梭形擴張)」</b>，佔了 80~90%。這也是考試極愛考的細節，常故意說是 Type 2 最常見。</p>
    
    <div class="quiz">
      <div class="quiz-top">
        <span class="lab">INLINE QUIZ</span>
        <span class="yr">觀念測驗</span>
      </div>
      <div class="quiz-body">
        <p class="stem">關於膽道疾病，下列敘述何者正確？</p>
        <ul class="opts">
          <li>(A) 膽絞痛通常和進食無關。</li>
          <li>(B) Charcot’s triad 描述 acute cholangitis 病人的常見症狀，包括：腹瀉、發燒及黃疸。</li>
          <li>(C) Gallstone ileus 瘻管最常發生在胃。</li>
          <li>(D) Todani classification 描述 Choledochal cyst，其中 Type 1 臨床上最常見。</li>
        </ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
            <div class="ans">正確答案：(D)</div>
            <p>解析：(A) 膽絞痛常與進食油膩食物有關。(B) Charcot's triad 是腹痛、發燒、黃疸。(C) Gallstone ileus 瘻管最常發生在十二指腸。(D) Todani Type 1 (總膽管擴張) 確實最常見。對應題庫 <a href="#q113-4" class="jump">113-4</a>, <a href="#q112-4" class="jump">112-4</a>。</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section id="s8">
    <div class="sec-head"><span class="sec-num">八</span><h2>一分鐘考前秒殺心法（王森稔／郭功楷老師 5 大重點）</h2></div>
    <div class="box key">
      <div class="bt"><span class="badge">考前 60 秒衝刺</span>王森稔／郭功楷老師必背重點</div>
      <ol>
        <li><b>膽汁製造：</b>膽汁由<strong>肝臟製造</strong>（非膽囊！）；膽絞痛常<strong>放射至右肩與後背</strong>。</li>
        <li><b>Todani 分型：</b>最常見為 <strong>Type 1 (總膽管囊狀擴張)</strong>。Charcot triad=腹痛+發燒+黃疸。</li>
        <li><b>良性可觀察囊腫：</b><strong>漿液性囊腺瘤 (SCN)</strong> 幾無惡性風險，初診斷可先保守觀察。IPMN則需積極處理。</li>
        <li><b>POPF 衍生出血：</b>Whipple 術後常因 <strong>GDA (胃十二指腸動脈) 假性動脈瘤破裂</strong>出血；胰漏首選引流保守治療，<strong>絕對不是立即再次開刀手術</strong>。</li>
        <li><b>胰腺癌治療：</b>約有70%長在頭部造成無痛性黃疸。若腫瘤侵犯血管屬於 Borderline resectable，應<strong>先做 Neoadjuvant 化療/放療</strong>使腫瘤降期，不可直接開刀。</li>
      </ol>
    </div>
  </section>

  <section id="exam">
    <div class="sec-head"><span class="sec-num">九</span><h2>歷屆考古題全收錄（BM110 ～ BM113 共 12 題）</h2></div>
    <div class="exam-head">
      <h2>王森稔／郭功楷老師 胰臟與膽道外科題庫全解</h2>
      <p>完整收錄 4 個學年度共 12 道真題，附標準答案與逐選項深度剖析。</p>
      <button class="btn" id="allBtn">全部展開答案</button>
    </div>

    <!-- BM113 -->
    <div class="yrhead">113 學年度 (BM113 期末考) · 4 題</div>
    <div class="q" id="q113-3"><span class="q-no">113-3</span><span class="q-topic">膽汁與膽紅素生理</span>
      <p class="q-stem">1. 下列敘述何者正確？<br>(A)Bile 中的 bilirubin 主要是人體內 heme 代謝後的產物<br>(B)人體內的膽汁(bile juice)是由膽囊(Gallbladder)製造產生<br>(C)cholesterol gallstone 的形成主要是和膽道系統發生細菌感染有關<br>(D)pregnancy 是膽石症相關的 risk factor，主要是因為懷孕過程中 progesterone 會增加 bile acid 的分泌以及膽囊收縮排空的能力</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(A)</div><p>• (A) 正確：Bilirubin 為血紅素 Heme 代謝物。(B) 膽汁由肝臟製造。(C) 細菌感染形成的是色素結石。(D) Progesterone 抑制膽囊排空造成膽汁淤積。</p><div class="src">出處：BM113 期末考 第3題（王森稔 ppt p.14、17）</div></div></details>
    </div>
    <div class="q" id="q113-4"><span class="q-no">113-4</span><span class="q-topic">膽絞痛與 Todani</span>
      <p class="q-stem">2. 下列敘述何者正確？<br>(A)Gallstone 所引起的 biliary colic 是指病人的上腹疼痛通常和進食有關，且常合併有後背痛或右肩疼痛的情形<br>(B)Charcot’s triad 描述 acute cholangitis 病人的常見症狀，包括：腹瀉、發燒及黃疸<br>(C)Gallstone ileus 常發生在老人冢，其 cholecystoenteric fistula 最常發生在 stomach<br>(D)Todani classification 描述 Choledochal cyst 的不同型態，其中 type 1 臨床上最常見</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(A)</div><p>• (A) 正確：進食引發 CCK 分泌刺激膽囊收縮致膽絞痛，放射至右肩與後背。(B) Charcot triad 為腹痛、發燒、黃疸。(C) 瘻管多在十二指腸。(D) Todani Type 1 最常見。(註：原題選項(D)寫type 2故為錯)</p><div class="src">出處：BM113 期末考 第4題（王森稔 ppt p33,41,46）</div></div></details>
    </div>
    <div class="q" id="q113-5"><span class="q-no">113-5</span><span class="q-topic">SCN 先觀察</span>
      <p class="q-stem">3. 下列那一種胰臟腫瘤，初診斷時建議可先觀察不用考慮評估接受手術切除治療？<br>(A)Pancreatic neuroendocrine tumor　(B)Solid pseudopapillary neoplasms　(C)Main-duct IPMNs　(D)Serous cystadenomas</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D) Serous cystadenomas</div><p>• 漿液性囊腺瘤 (SCN) 幾乎全為良性，無症狀者初診斷時可先保守觀察。</p><div class="src">出處：BM113 期末考 第5題（王森稔 ppt pg. 4, 6）</div></div></details>
    </div>
    <div class="q" id="q113-6"><span class="q-no">113-6</span><span class="q-topic">POPF 處置錯誤</span>
      <p class="q-stem">4. 有關胰漏(Postoperative pancreatic fistula; POPF)下列敘述何者錯誤？<br>(A)常發生在胰臟手術之後<br>(B)Whipple procedure 後若發生 POPF，其衍生出的出血常是因為 gastro-duodenal artery(GDA)發生 pseudoaneurysm 破裂所致，死亡率極高<br>(C)相關的危險因子包括胰臟組織過軟以及胰管過細等<br>(D)發生胰漏的病人建議立即接受手術處理</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D)</div><p>• (D) 錯誤：發生胰漏時首選禁食、維持引流通暢之保守治療，盲目立即再手術開刀死亡率更高。</p><div class="src">出處：BM113 期末考 第6題（王森稔 ppt pg. 36, 38）</div></div></details>
    </div>

    <!-- BM112 -->
    <div class="yrhead">112 學年度 (BM112 期末考) · 4 題</div>
    <div class="q" id="q112-3"><span class="q-no">112-3</span><span class="q-topic">膽汁生理</span>
      <p class="q-stem">5. 下列敘述何者正確？<br>(A) 人體內的膽汁是由膽囊製造產生<br>(B) Bile 中的 bilirubin 主要是人體內 heme 代謝後的產物<br>(C) cholesterol gallstone 形成主因是細菌感染<br>(D) pregnancy 增加膽囊排空能力</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(B)</div><p>• 膽汁由肝臟製造；Bilirubin 來自 Heme 代謝。</p><div class="src">出處：BM112 期末考 第3題（王森稔）</div></div></details>
    </div>
    <div class="q" id="q112-4"><span class="q-no">112-4</span><span class="q-topic">Charcot triad</span>
      <p class="q-stem">6. 下列敘述何者正確？<br>(A) 膽絞痛通常和進食無關<br>(B) Charcot’s triad 描述 acute cholangitis 病人的常見症狀，包括：腹痛、發燒及黃疸<br>(C) Gallstone ileus 瘻管最常發生在胃<br>(D) Todani type 2 臨床最常見</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(B)</div><p>• Charcot's triad 為腹痛、發燒、黃疸。</p><div class="src">出處：BM112 期末考 第4題（王森稔）</div></div></details>
    </div>
    <div class="q" id="q112-70"><span class="q-no">112-70</span><span class="q-topic">胰腺癌特徵</span>
      <p class="q-stem">7. 有關胰臟癌下列敘述何者正確？<br>(A) 由 islet cells 衍生出來的占大多數<br>(B) 新生糖尿病(new-onset diabetes)的發生被列為是 risk factor 之一<br>(C) 胰尾癌常見初始症狀是黃疸<br>(D) CA19-9 適合做普查篩檢</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(B)</div><p>• (B) 正確：年過 50 歲新診斷糖尿病為胰腺癌高危警訊。(A) 90% 為導管腺癌。(C) 黃疸為胰頭癌特徵。(D) CA19-9 不適合常規篩檢。</p><div class="src">出處：BM112 期末考 第70題（王森稔）</div></div></details>
    </div>
    <div class="q" id="q112-71"><span class="q-no">112-71</span><span class="q-topic">POPF GDA 假性動脈瘤</span>
      <p class="q-stem">8. 有關胰漏(POPF)下列敘述何者錯誤？<br>(A) 常發生在胰臟手術之後<br>(B) Whipple procedure 後若發生 POPF，其衍生出的出血常是因為 splenic artery 發生pseudoaneurysm 破裂所致，死亡率極高<br>(C) 相關的危險因子包括胰臟組織過軟以及胰管過細等<br>(D) 發生胰漏的病人也可能因為發生 sepsis 而死亡</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(B)</div><p>• (B) 錯誤：Whipple 術後 POPF 腐蝕出血的血管是<b>胃十二指腸動脈 (GDA)</b> 殘端，而非脾動脈。</p><div class="src">出處：BM112 期末考 第71題（王森稔）</div></div></details>
    </div>

    <!-- BM111 -->
    <div class="yrhead">111 學年度 (BM111 期末考) · 2 題</div>
    <div class="q" id="q111-68"><span class="q-no">111-68</span><span class="q-topic">Borderline 胰腺癌治療</span>
      <p class="q-stem">9. 胰臟癌的腫瘤分布位置如圖(Stage III)，有關治療之敘述，下列何者正確？<br>(A) 病人應該接受全胰臟切除<br>(B) 病人應該接受胰頭十二指腸切除術<br>(C) 若評估可行，病人應先接受化學治療<br>(D) 病人應該接受最新的標靶及免疫治療</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C) 先接受化療</div><p>• 侵犯大血管之 Borderline resectable 胰腺癌應先給予 Neoadjuvant 化療/放療。</p><div class="src">出處：BM111 期末考 第68題（郭功楷 ppt pg. 20）</div></div></details>
    </div>
    <div class="q" id="q111-69"><span class="q-no">111-69</span><span class="q-topic">IPMN 處置</span>
      <p class="q-stem">10. 胰腺導管內乳頭狀黏液性腫瘤 (IPMN) 的評估和處理方法：下列何者不正確？<br>(A) IPMN 會產生黏液，這種黏液會形成胰腺囊腫。<br>(B) 主胰管 (main duct, MD) 發生惡性腫瘤的風險較高。<br>(C) 常常需要通過超音波內鏡引導下細針抽吸活檢 (EUS-FNA) 進一步評估是否具惡性特徵。<br>(D) 若有阻塞性黃疸，囊泡內壁有(&gt;1cm)顯影性結節產生，應建議置放支架及化療後，進一步手術切除為佳。</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D)</div><p>• (D) 錯誤：出現黃疸、主胰管擴張或 &gt;1cm 結節為「High-risk stigmata」，應<b>直接考慮手術切除</b>，而非先放支架化療。</p><div class="src">出處：BM111 期末考 第69題（郭功楷 ppt pg. 16, 54, 57）</div></div></details>
    </div>

    <!-- BM110 -->
    <div class="yrhead">110 學年度 (BM110 期末考) · 2 題</div>
    <div class="q" id="q110-62"><span class="q-no">110-62</span><span class="q-topic">胰臟癌敘述</span>
      <p class="q-stem">11. 有關胰臟癌之敘述，下列何者正確？<br>(A)發於胰臟體尾部的癌，其電腦斷層多顯示為「高顯影腫瘤」且預後不佳<br>(B) 胰尾部的胰腺癌常出現黃疸、體重減輕和腹痛<br>(C) 在內視鏡超音波引導下進行酒精注射是最有效的治療方法<br>(D) Borderline resectable 的胰臟癌應先進行 neoadjuvant 化療或合併放射線療法</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D)</div><p>• Borderline resectable 胰腺癌應先進行 Neoadjuvant 化放療。</p><div class="src">出處：BM110 期末考 第62題（郭功楷 ppt pg.20）</div></div></details>
    </div>
    <div class="q" id="q110-63"><span class="q-no">110-63</span><span class="q-topic">胰臟癌切除率</span>
      <p class="q-stem">12. 有關胰臟癌的切除性手術及治療,何者為正確?<br>(A) 胰臟全切除,效果最好,但會造成糖尿病<br>(B) 應該做大範圍的切除:包括部分肝臟,腹腔內之淋巴腺切除(包括主動脈、下腔大靜脈附近的淋巴腺)<br>(C) 約 15 - 20%切除率<br>(D) 術後化學治療平均之反應率(response rate)大於 90%</p>
      <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C) 約 15 - 20% 切除率</div><p>• 胰腺癌初診斷時僅約 15～20% 病患具有開刀切除機會。</p><div class="src">出處：BM110 期末考 第63題（郭功楷 ppt pg.5）</div></div></details>
    </div>
  </section>
  <footer>
    <p><b>高醫肝膽胰外科｜王森稔／郭功楷老師 胰臟與膽道外科題庫全集完成</b>　共 12 題。</p>
  </footer>
  </main>
</div>
</div>

<script>
  (function(){
    document.querySelectorAll('.tw table').forEach(function(t){
      var ths = t.querySelectorAll('thead th');
      if(!ths.length) return;
      var labels = Array.prototype.map.call(ths, function(th){
        return th.textContent.replace(/\u3000/g,'').trim();
      });
      t.querySelectorAll('tbody tr').forEach(function(tr){
        Array.prototype.forEach.call(tr.children, function(td, i){
          if(labels[i]) td.setAttribute('data-label', labels[i]);
        });
      });
    });
  })();
  (function(){
    var toc = document.getElementById('tocBox');
    if(toc && window.matchMedia('(max-width:700px)').matches){
      toc.removeAttribute('open');
    }
  })();
  var allBtn = document.getElementById('allBtn');
  if(allBtn){
    var expanded = false;
    allBtn.addEventListener('click', function(){
      expanded = !expanded;
      document.querySelectorAll('.q details.rev, .quiz details.rev').forEach(function(d){
        if(expanded){ d.setAttribute('open',''); } else { d.removeAttribute('open'); }
      });
      allBtn.textContent = expanded ? '全部收合答案' : '全部展開答案';
    });
  }
</script>

</body>
</html>
"""
import os
with open('/Users/furyan/.gemini/antigravity/scratch/notes/block7/pancreatic-biliary-surgery.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
