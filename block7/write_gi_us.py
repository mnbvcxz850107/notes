# coding=utf-8
import os

html_content = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>消化系超音波學｜裸讀學習筆記</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@500;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#0F1B18;
    --bg-2:#152420;
    --bg-3:#1B2E29;
    --line:#26403A;
    --line-2:#31534B;
    --text:#E9F1EE;
    --text-2:#A8C2BA;
    --text-3:#7A968D;
    --teal:#7FC9BE;
    --teal-dim:#4E9A90;
    --gold:#C9A961;
    --rose:#E58B85;
    --serif:"Noto Serif TC","Songti TC",serif;
    --sans:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;
    --mono:"JetBrains Mono",ui-monospace,Menlo,monospace;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth;scroll-padding-top:24px;overflow-x:hidden}
  body{
    margin:0;background:var(--bg);color:var(--text);
    font-family:var(--sans);font-size:16.5px;line-height:1.9;font-weight:300;
    -webkit-font-smoothing:antialiased;
    overflow-x:hidden;
  }
  .wrap{max-width:1150px;margin:0 auto;padding:0 22px}
  header.hero{padding:66px 0 52px;border-bottom:1px solid var(--line)}
  .backlink{display:inline-block;font-family:var(--mono);font-size:12px;color:var(--text-3);text-decoration:none;margin-bottom:22px;border:1px solid var(--line);border-radius:6px;padding:5px 12px;transition:.15s}
  .backlink:hover{color:var(--teal);border-color:var(--teal-dim)}
  .eyebrow{display:flex;align-items:center;gap:16px;margin-bottom:26px;font-family:var(--serif);font-size:15px;letter-spacing:.34em;color:var(--teal)}
  .eyebrow .rule{width:56px;height:1px;background:var(--gold)}
  .eyebrow .dot{color:var(--gold)}
  header.hero h1{font-family:var(--serif);font-weight:700;font-size:clamp(38px,7vw,74px);line-height:1.15;margin:0 0 22px;letter-spacing:.02em;}
  header.hero h1 em{font-style:normal;color:var(--teal)}
  header.hero p.sub{margin:0;color:var(--text-2);max-width:62ch;font-size:17px;line-height:1.85}
  .intro-card{border:1px solid var(--line);border-radius:16px;padding:26px 30px;margin-top:34px;background:var(--bg-2);}
  .intro-card p{margin:0 0 22px;color:var(--text-2)}
  .intro-card b{color:var(--teal);font-weight:500}
  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
  .stat .n{font-family:var(--serif);font-size:38px;color:var(--gold);line-height:1}
  .stat .l{font-size:12.5px;color:var(--text-3);letter-spacing:.08em;margin-top:6px}
  .cols{display:grid;grid-template-columns:220px 1fr;gap:52px;padding:46px 0 90px;align-items:start}
  nav.toc{position:sticky;top:26px}
  nav.toc .t{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--text-3);margin-bottom:14px}
  nav.toc a{display:block;padding:7px 14px;border-left:1px solid var(--line);color:var(--text-2);text-decoration:none;font-size:14px;transition:.15s}
  nav.toc a:hover{border-left-color:var(--teal);color:var(--teal);background:var(--bg-2)}
  nav.toc a.exam{color:var(--gold)}
  nav.toc summary{display:none}
  section{margin-bottom:64px;scroll-margin-top:24px}
  .sec-head{display:flex;align-items:baseline;gap:16px;border-bottom:1px solid var(--line-2);padding-bottom:12px;margin-bottom:26px}
  .sec-num{font-family:var(--serif);font-size:30px;color:var(--gold);line-height:1}
  .sec-head h2{font-family:var(--serif);font-size:clamp(23px,3.4vw,31px);margin:0;font-weight:700;letter-spacing:.02em}
  h3{font-family:var(--serif);font-size:21px;margin:38px 0 12px;font-weight:500;color:var(--text)}
  h4{font-size:16.5px;margin:24px 0 8px;color:var(--teal);font-weight:500}
  p{margin:0 0 15px}
  ul,ol{margin:0 0 17px;padding-left:22px}
  li{margin-bottom:8px}
  li::marker{color:var(--teal-dim)}
  strong,b{font-weight:500;color:#FFF}
  u{text-decoration-color:var(--teal-dim);text-underline-offset:3px}
  mark{background:rgba(201,169,97,.22);box-shadow:inset 0 -2px 0 rgba(201,169,97,.6);color:#FBF3E2;padding:1px 3px;border-radius:2px}
  a.qtag{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:600;border:1px solid var(--gold);color:var(--gold);padding:1px 7px;border-radius:4px;text-decoration:none;margin:0 3px;vertical-align:2px;white-space:nowrap;transition:.15s}
  a.qtag:hover{background:var(--gold);color:var(--bg)}
  .tagline{margin:-8px 0 18px;font-size:13.5px;color:var(--text-3)}
  .box{border-radius:13px;padding:20px 24px;margin:22px 0;border:1px solid var(--line);background:var(--bg-2)}
  .box .bt{font-weight:500;font-size:14.5px;margin-bottom:10px;display:flex;align-items:center;gap:9px;color:#FFF}
  .box p:last-child,.box ul:last-child,.box ol:last-child{margin-bottom:0}
  .badge{font-family:var(--mono);font-size:10px;padding:2px 8px;border-radius:3px;letter-spacing:.06em;border:1px solid currentColor;font-weight:600}
  .box.exam{border-color:rgba(201,169,97,.45);background:rgba(201,169,97,.07)}
  .box.exam .badge{color:var(--gold)}
  .box.trap{border-color:rgba(229,139,133,.45);background:rgba(229,139,133,.07)}
  .box.trap .badge{color:var(--rose)}
  .box.key{border-color:rgba(127,201,190,.4);background:rgba(127,201,190,.07)}
  .box.key .badge{color:var(--teal)}
  .quiz{border:1px solid var(--line-2);border-radius:14px;margin:26px 0;overflow:hidden;background:var(--bg-2)}
  .quiz-top{display:flex;align-items:center;gap:10px;padding:12px 20px;background:var(--bg-3);border-bottom:1px solid var(--line)}
  .quiz-top .lab{font-family:var(--serif);font-size:14px;letter-spacing:.16em;color:var(--gold)}
  .quiz-top .yr{font-family:var(--mono);font-size:11.5px;color:var(--text-2);border:1px solid var(--line-2);padding:2px 8px;border-radius:4px}
  .quiz-body{padding:20px 22px}
  .quiz-body .stem{font-size:15.5px;line-height:1.85;margin:0 0 14px;color:var(--text)}
  .opts{list-style:none;padding:0;margin:0 0 14px}
  .opts li{padding:8px 12px;font-size:15px;border:1px solid var(--line);border-radius:8px;margin-bottom:7px;color:var(--text-2)}
  details.rev{margin:0}
  summary.toggle{display:inline-block;list-style:none;cursor:pointer;background:none;border:1px solid var(--teal-dim);color:var(--teal);font-family:var(--sans);font-size:13px;padding:7px 16px;border-radius:7px;font-weight:400;transition:.15s;-webkit-tap-highlight-color:transparent;}
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
  .exam-head{border:1px solid var(--line-2);border-radius:16px;padding:30px;margin-bottom:28px;background:var(--bg-2)}
  .exam-head h2{font-family:var(--serif);margin:0 0 10px;font-size:29px}
  .exam-head p{color:var(--text-2);margin:0;font-size:15px}
  .yrhead{font-family:var(--serif);font-size:24px;font-weight:700;margin:40px 0 18px;padding-left:16px;border-left:3px solid var(--gold);color:var(--gold)}
  .q{background:var(--bg-2);border:1px solid var(--line);border-radius:13px;padding:22px 24px;margin-bottom:16px;scroll-margin-top:24px}
  .q-no{font-family:var(--mono);font-size:11.5px;color:var(--gold);border:1px solid var(--gold);padding:2px 9px;border-radius:5px}
  .q-stem{margin:14px 0 12px;font-size:15.5px;line-height:1.85}
  footer{border-top:1px solid var(--line);padding:30px 0 60px;color:var(--text-3);font-size:13.5px}
  footer b{color:var(--text-2)}
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <a class="backlink" href="index.html">← 返回 Block 7 目錄</a>
    <div class="eyebrow"><span class="rule"></span>裸讀學習筆記<span class="dot">·</span>由淺入深</div>
    <h1>消化系超音波學</h1>
    <p class="sub">急診室的第三隻眼 —— 探頭放下去，黑白世界裡的脂肪肝、水泡與結石。授課教師：王志文老師。</p>

    <div class="intro-card">
      <p>這份筆記將 <b>BM112、BM113</b> 學年度超音波的必考題型，<b>融入到各個基礎觀念段落中</b>。讀完每個觀念，順手就能用考古題驗證自己是否真正懂了。</p>
      <div class="stats">
        <div class="stat"><div class="n">5</div><div class="l">總題數</div></div>
        <div class="stat"><div class="n">3</div><div class="l">BM112</div></div>
        <div class="stat"><div class="n">2</div><div class="l">BM113</div></div>
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
      <a href="#s1">一　導讀：急診室的第三隻眼</a>
      <a href="#s2">二　超音波基礎語言：黑白世界的秘密</a>
      <a href="#s3">三　肝臟超音波：脂肪肝、水泡與腫瘤</a>
      <a href="#s4">四　膽道系統：結石與發炎</a>
      <a href="#s5">五　一分鐘考前秒殺心法</a>
      <a href="#exam" class="exam">六　考古題全收錄</a>
      </div>
    </details>
  </nav>

  <main>

  <!-- ============ 01 ============ -->
  <section id="s1">
    <div class="sec-head"><span class="sec-num">一</span><h2>導讀：急診室的第三隻眼</h2></div>
    <p>想像一下這個情境：半夜兩點的急診室，一位五十歲的病患被推了進來，痛得在床上打滾，右手一直壓著右上腹。抽血報告要等一小時，電腦斷層（CT）排隊還要更久。這時，值班醫師推著一台像是大型電腦的機器過來，在病人肚子上塗滿冰涼的凝膠，探頭一放，螢幕上閃爍著黑白相間的畫面。不到一分鐘，醫師便自信地說：「是急性膽囊炎，膽囊裡面有結石卡住了。」</p>

    <p>這台機器，就是<strong>超音波（Ultrasound）</strong>，臨床醫師在急診室和病房裡最依賴的「第三隻眼」。</p>

    <div class="box key">
      <div class="bt"><span class="badge">核心觀念</span>為什麼超音波這麼重要？</div>
      <p>超音波有三大無可取代的優勢：<b>即時（Real-time）</b>、<b>無游離輻射（No radiation）</b>、<b>床邊操作（Bedside）</b>。它利用聲波在不同組織間反射的原理成像，對於<mark>肝臟、膽囊、腎臟等實質器官或充滿液體的構造</mark>特別擅長。不過，超音波最大的天敵是「空氣」和「骨頭」，因此腸胃道裡的氣體常常會遮蔽後方的影像。</p>
    </div>
  </section>

  <!-- ============ 02 ============ -->
  <section id="s2">
    <div class="sec-head"><span class="sec-num">二</span><h2>超音波基礎語言：黑白世界的秘密</h2></div>
    <p>看超音波就像在看一幅黑白水墨畫。不同的組織密度，反射聲波的能力不同，在螢幕上就會呈現出不同層次的灰階。我們用「<b>回音性（Echogenicity）</b>」來描述這些影像。</p>

    <h3>1. 回音性的定義（相較於周邊組織）</h3>
    <ul>
      <li><strong>高回音（Hyperechoic）：</strong>組織緻密、反射強，畫面上看起來是<mark>偏白色、亮亮的</mark>。例如：骨骼表面、結石、血管瘤、甚至脂肪肝裡的脂肪顆粒。</li>
      <li><strong>等回音（Isoechoic）：</strong>和周邊正常組織或參考器官的亮度差不多。一般健康的肝臟和皮質層的亮度通常很相近。</li>
      <li><strong>低回音（Hypoechoic）：</strong>反射較弱，看起來是<mark>偏暗、灰黑色的</mark>。例如：某些實質腫瘤、正常的腎臟髓質。</li>
      <li><strong>無回音（Anechoic）：</strong>聲波完全穿透，沒有反射，畫面上是<mark>純黑色的</mark>。最典型的代表就是<b>純粹的液體</b>，例如：尿液、膽汁、單純性囊腫（水泡）、血管內的血液。</li>
    </ul>

    <h3>2. 兩大經典的「假影（Artifacts）」</h3>
    <p>超音波的假影有時是干擾，但更多時候是我們診斷疾病的「神隊友」。</p>

    <ul>
      <li><strong>後方音波增強（Posterior acoustic enhancement）：</strong>當聲波穿過「純液體」（無回音的囊腫或膽囊）時，因為幾乎沒有能量消耗，剩下的聲波打到液體後方的組織時，反射回來的能量反而比旁邊沒穿過液體的組織還強。結果就是：<mark>水泡的正後方會出現一道「異常明亮」的光帶</mark>。這告訴我們：「前面這團黑黑的東西是水！」</li>
      <li><strong>後方音響陰影（Posterior acoustic shadowing）：</strong>當聲波撞到「極度堅硬」的物體（如結石、骨頭、鈣化灶），聲波會被完全反射或吸收，無法穿透過去。結果就是：<mark>結石的正後方會出現一道「純黑」的陰影</mark>。這告訴我們：「前面這個白亮亮的東西是硬石頭！」</li>
    </ul>

    <div class="box trap">
      <div class="bt"><span class="badge">易錯陷阱</span>水泡 vs 結石 的黃金組合</div>
      <p>考試常把這兩者搞混。請牢記：<br>
      <b>單純囊腫（Simple cyst）：</b>本身是黑的（Anechoic），後方是亮的（Enhancement）。<br>
      <b>結石（Stone）：</b>本身是亮的（Hyperechoic），後方是黑的（Shadowing）。</p>
    </div>
  </section>

  <!-- ============ 03 ============ -->
  <section id="s3">
    <div class="sec-head"><span class="sec-num">三</span><h2>肝臟超音波：脂肪肝、水泡與腫瘤</h2></div>
    <p class="tagline">本節考點：<a class="qtag" href="#q112-58">112-58</a><a class="qtag" href="#q112-59">112-59</a><a class="qtag" href="#q113-63">113-63</a></p>

    <p>肝臟就像人體的一座大型化學工廠。在超音波下，正常的肝臟呈現均勻的中等灰度，它的亮度通常和旁邊的右腎皮質差不多（或稍微亮一點點）。但當工廠出問題時，畫面就會說話了。</p>

    <h3>1. 脂肪肝（Fatty Liver）</h3>
    <p>當肝臟細胞內囤積了過多的三酸甘油酯，這些脂肪小顆粒會讓超音波產生大量的散射。因此，脂肪肝的經典表現是：<mark>肝臟整體變得很白、很亮（Diffuse hyperechoic）</mark>。</p>
    <p>臨床上怎麼判斷到底多亮才算脂肪肝？醫師會拿旁邊的「腎臟」當比例尺。正常情況下，肝臟和腎皮質的亮度相近；但如果是脂肪肝，<b>肝臟的亮度會明顯大於右腎皮質</b>（Liver-kidney contrast 變大）。嚴重的脂肪肝，超音波的穿透力會變差，導致肝臟深部的影像變得模糊看不清。</p>

    <div class="quiz">
      <div class="quiz-top"><span class="lab">考古題</span><span class="yr">112 學年度 · 第 58 題</span></div>
      <div class="quiz-body">
        <p class="stem">關於脂肪肝在超音波下的特徵，下列何者正確？</p>
        <ul class="opts"><li>(A) 肝臟實質回音度下降，比右腎皮質還暗。<br>(B) 肝臟實質呈現瀰漫性高回音（瀰漫性變亮），明顯比右腎皮質亮。<br>(C) 肝內血管的輪廓會變得更加清晰銳利。<br>(D) 超音波對深部組織的穿透力會增加。</li></ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
          <div class="ans">答案：(B)</div>
          <p>脂肪肝因為脂肪堆積，超音波反射增加，導致肝臟呈現<b>瀰漫性高回音（Hyperechoic）</b>，且會跟右腎產生明顯的明暗對比（肝比腎亮）。同時，脂肪會造成超音波衰減，使得深部穿透力變差，血管輪廓反而會變得模糊。</p>
        </div>
        </details>
      </div>
    </div>

    <h3>2. 單純性肝囊腫（Simple Hepatic Cyst）</h3>
    <p>這就是俗稱的「肝臟水泡」。它是一個充滿清澈液體的泡泡，所以符合「純液體」的所有特徵：<mark>內部完全無回音（純黑，Anechoic）</mark>，邊界非常平滑清晰，而且必定伴隨<mark>後方音波增強（Posterior enhancement）</mark>。</p>
    
    <h3>3. 肝血管瘤（Hemangioma）</h3>
    <p>血管瘤是肝臟最常見的良性腫瘤，本質上是一團糾結的微血管網。因為微血管壁與血液之間有著無數的小界面，強烈反射超音波，所以典型的血管瘤在超音波下是一顆<mark>高回音（Hyperechoic，亮白）的均勻腫塊</mark>，且邊界通常很清楚。</p>

    <div class="quiz">
      <div class="quiz-top"><span class="lab">考古題</span><span class="yr">112 學年度 · 第 59 題</span></div>
      <div class="quiz-body">
        <p class="stem">在肝臟超音波中，如果要區分「單純性囊腫（Cyst）」與「典型血管瘤（Hemangioma）」，下列何項描述最為正確？</p>
        <ul class="opts"><li>(A) 囊腫內部呈現高回音；血管瘤呈現無回音。<br>(B) 兩者皆會有明顯的後方音響陰影（shadowing）。<br>(C) 囊腫內部為無回音（anechoic）且具後方音波增強；血管瘤通常呈現高回音（hyperechoic）實質腫塊。<br>(D) 血管瘤內部會充滿液體，且伴隨後方增強。</li></ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
          <div class="ans">答案：(C)</div>
          <p>這是最經典的對比。水泡（Cyst）是純液體，所以內部全黑（Anechoic）且後方增強（Enhancement）；血管瘤是微血管網交織，反射強烈，所以通常是一團白亮的實質腫塊（Hyperechoic）。</p>
        </div>
        </details>
      </div>
    </div>

    <h3>4. 肝細胞癌（Hepatocellular Carcinoma, HCC）</h3>
    <p>肝癌的長相千變萬化，可以是低回音、等回音、甚至高回音或混合型。但它有一個非常有名的典型特徵：<mark>周邊暈環徵（Peripheral halo sign）</mark>。這是一圈包圍在腫瘤外圍的「暗色帶（低回音環）」，主要是因為腫瘤快速生長，壓迫周邊正常的肝組織，或者腫瘤本身有一層纖維包膜所造成。如果在 B 型或 C 型肝炎、肝硬化的患者肝臟中看到帶有 halo sign 的腫塊，一定要高度懷疑是肝癌。</p>

    <div class="quiz">
      <div class="quiz-top"><span class="lab">考古題</span><span class="yr">113 學年度 · 第 63 題</span></div>
      <div class="quiz-body">
        <p class="stem">一位患有 B 型肝炎及肝硬化的 60 歲男性接受例行超音波檢查，發現肝臟右葉有一顆 3 公分的腫瘤。腫瘤內部回音不均勻，且外圍有一圈明顯的「低回音暈環（Hypoechoic halo）」。最可能的診斷為何？</p>
        <ul class="opts"><li>(A) 典型血管瘤（Hemangioma）<br>(B) 單純性囊腫（Simple cyst）<br>(C) 局部結節性增生（FNH）<br>(D) 肝細胞癌（HCC）</li></ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
          <div class="ans">答案：(D)</div>
          <p>在慢性肝炎或肝硬化的背景下，發現有「Halo sign（暈環徵）」的實質腫瘤，是 <b>肝細胞癌（HCC）</b> 的強烈暗示。血管瘤通常是高回音，而囊腫則是無回音。</p>
        </div>
        </details>
      </div>
    </div>

  </section>

  <!-- ============ 04 ============ -->
  <section id="s4">
    <div class="sec-head"><span class="sec-num">四</span><h2>膽道系統：結石與發炎</h2></div>
    <p class="tagline">本節考點：<a class="qtag" href="#q112-60">112-60</a><a class="qtag" href="#q113-62">113-62</a></p>

    <p>膽囊就像一個儲存膽汁的水球。因為裡面充滿了膽汁（液體），所以正常的膽囊在超音波下是一個無回音（全黑）的囊狀物，壁很薄（小於 3 mm）。這讓膽囊成為超音波極佳的觀察對象。</p>

    <h3>1. 膽結石（Gallstones）</h3>
    <p>石頭非常堅硬，超音波打不穿。所以膽結石在超音波下有三個黃金診斷標準：</p>
    <ol>
      <li><strong>高回音病灶（Hyperechoic focus）：</strong>在黑色的膽汁中，結石是一顆明亮發白的構造。</li>
      <li><strong>後方音響陰影（Acoustic shadowing）：</strong>聲波被石頭擋住，後方留下一道長長的純黑陰影。</li>
      <li><strong>重力依賴性移動（Mobility）：</strong>請病人翻身，石頭會因為重力跟著滾動到膽囊較低的位置。這可以區分結石和長在膽囊壁上的息肉（息肉是黏在壁上，不會動的）。</li>
    </ol>

    <div class="quiz">
      <div class="quiz-top"><span class="lab">考古題</span><span class="yr">112 學年度 · 第 60 題</span></div>
      <div class="quiz-body">
        <p class="stem">下列何者是膽囊結石在超音波下的典型特徵？</p>
        <ul class="opts"><li>(A) 膽囊內的高回音病灶，後方伴隨音響陰影（Acoustic shadowing），且會隨體位改變而移動。<br>(B) 膽囊內的無回音病灶，伴隨後方音波增強。<br>(C) 固定在膽囊壁上的高回音病灶，無後方陰影。<br>(D) 膽囊整體呈現瀰漫性高回音。</li></ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
          <div class="ans">答案：(A)</div>
          <p>結石的黃金三特徵：高回音（亮）、後方陰影（Shadowing）、會隨重力移動。(C) 描述的其實是「膽囊息肉」。</p>
        </div>
        </details>
      </div>
    </div>

    <h3>2. 急性膽囊炎（Acute Cholecystitis）</h3>
    <p>當結石卡在膽囊管，膽汁排不出去，膽囊就會脹大並引發嚴重發炎。急診醫師用超音波診斷急性膽囊炎，會尋找以下經典跡象：</p>
    <ul>
      <li><mark>膽囊壁增厚（Gallbladder wall thickening）：</mark>發炎水腫會讓壁厚度超過 3 mm。</li>
      <li><mark>膽囊周圍積水（Pericholecystic fluid）：</mark>發炎滲出液在膽囊外圍形成一圈黑色的無回音暗帶。</li>
      <li><mark>超音波墨菲氏徵（Sonographic Murphy's sign）：</mark>這是最關鍵的動態理學檢查！當醫師用超音波探頭直接壓迫畫面上膨脹的膽囊時，病人會因為劇痛而突然停止吸氣。這比傳統用手壓更精準，因為你是「看著膽囊直接壓上去」。</li>
      <li>通常也會同時看到膽囊裡面有結石（Gallstone）。</li>
    </ul>

    <div class="quiz">
      <div class="quiz-top"><span class="lab">考古題</span><span class="yr">113 學年度 · 第 62 題</span></div>
      <div class="quiz-body">
        <p class="stem">一名 45 歲肥胖女性因右上腹劇痛掛急診。超音波檢查發現膽囊內有多顆結石。下列哪一項超音波發現，最強烈支持她目前併發了「急性膽囊炎」？</p>
        <ul class="opts"><li>(A) 結石後方出現明顯的音響陰影（Acoustic shadowing）<br>(B) 病患翻身時結石會移動<br>(C) 超音波探頭壓迫膽囊時出現局部劇痛（Sonographic Murphy's sign），且膽囊壁厚度達 6 mm<br>(D) 肝臟整體亮度明顯大於右腎皮質</li></ul>
        <details class="rev">
          <summary class="toggle"></summary>
          <div class="reveal">
          <div class="ans">答案：(C)</div>
          <p>單純發現結石（A、B）只能證明有膽結石症，並不能代表「正在急性發炎」。急性發炎的證據在於：<b>膽囊壁增厚（>3mm）、周圍積液、以及 Sonographic Murphy's sign 陽性</b>。(D) 描述的是脂肪肝。</p>
        </div>
        </details>
      </div>
    </div>
  </section>

  <!-- ============ 05 ============ -->
  <section id="s5">
    <div class="sec-head"><span class="sec-num">五</span><h2>一分鐘考前秒殺心法</h2></div>
    <div class="box exam">
      <div class="bt"><span class="badge">考前大補帖</span>黑白對決一覽表</div>
      <ul>
        <li><b>看到「脂肪肝」：</b>反射動作找「比腎臟亮（高回音）」。</li>
        <li><b>看到「單純水泡 Cyst」：</b>反射動作找「黑（無回音）」＋「後方變亮（Enhancement）」。</li>
        <li><b>看到「結石 Stone」：</b>反射動作找「白（高回音）」＋「後方變黑（Shadowing）」＋「會滾動」。</li>
        <li><b>看到「血管瘤 Hemangioma」：</b>反射動作找「高回音均勻腫塊」。</li>
        <li><b>看到「Halo sign 暈環」：</b>在國考與段考的世界裡，這往往是「HCC（肝癌）」的代名詞。</li>
        <li><b>看到「急性膽囊炎」：</b>尋找「壁厚 > 3mm」＋「探頭壓下去會痛（Murphy's sign）」。</li>
      </ul>
    </div>
  </section>

  <!-- ============ EXAM ============ -->
  <section id="exam">
    <div class="exam-head">
      <h2>考古題全收錄</h2>
      <p>前面讀懂了？這裡直接不看詳解盲測一次，驗證你的直覺反應。</p>
    </div>

    <div class="yrhead">113 學年度</div>

    <div class="q" id="q113-62">
      <span class="q-no">Q62</span>
      <div class="q-stem">一名 45 歲肥胖女性因右上腹劇痛掛急診。超音波檢查發現膽囊內有多顆結石。下列哪一項超音波發現，最強烈支持她目前併發了「急性膽囊炎」？</div>
      <ul class="opts">
        <li>(A) 結石後方出現明顯的音響陰影（Acoustic shadowing）</li>
        <li>(B) 病患翻身時結石會移動</li>
        <li>(C) 超音波探頭壓迫膽囊時出現局部劇痛（Sonographic Murphy's sign），且膽囊壁厚度達 6 mm</li>
        <li>(D) 肝臟整體亮度明顯大於右腎皮質</li>
      </ul>
      <details class="rev"><summary class="toggle"></summary><div class="reveal">
        <div class="ans">答案：(C)</div>
        <p>急性發炎的指標為膽囊壁增厚與超音波墨菲氏徵。只有結石與陰影不足以診斷發炎。</p>
      </div></details>
    </div>

    <div class="q" id="q113-63">
      <span class="q-no">Q63</span>
      <div class="q-stem">一位患有 B 型肝炎及肝硬化的 60 歲男性接受例行超音波檢查，發現肝臟右葉有一顆 3 公分的腫瘤。腫瘤內部回音不均勻，且外圍有一圈明顯的「低回音暈環（Hypoechoic halo）」。最可能的診斷為何？</div>
      <ul class="opts">
        <li>(A) 典型血管瘤（Hemangioma）</li>
        <li>(B) 單純性囊腫（Simple cyst）</li>
        <li>(C) 局部結節性增生（FNH）</li>
        <li>(D) 肝細胞癌（HCC）</li>
      </ul>
      <details class="rev"><summary class="toggle"></summary><div class="reveal">
        <div class="ans">答案：(D)</div>
        <p>Halo sign 是 HCC 在超音波上非常有代表性的特徵之一。</p>
      </div></details>
    </div>

    <div class="yrhead">112 學年度</div>

    <div class="q" id="q112-58">
      <span class="q-no">Q58</span>
      <div class="q-stem">關於脂肪肝在超音波下的特徵，下列何者正確？</div>
      <ul class="opts">
        <li>(A) 肝臟實質回音度下降，比右腎皮質還暗。</li>
        <li>(B) 肝臟實質呈現瀰漫性高回音（瀰漫性變亮），明顯比右腎皮質亮。</li>
        <li>(C) 肝內血管的輪廓會變得更加清晰銳利。</li>
        <li>(D) 超音波對深部組織的穿透力會增加。</li>
      </ul>
      <details class="rev"><summary class="toggle"></summary><div class="reveal">
        <div class="ans">答案：(B)</div>
        <p>脂肪堆積會讓整體肝臟變亮（高回音），並且造成聲波衰減，深部穿透力變差。</p>
      </div></details>
    </div>

    <div class="q" id="q112-59">
      <span class="q-no">Q59</span>
      <div class="q-stem">在肝臟超音波中，如果要區分「單純性囊腫（Cyst）」與「典型血管瘤（Hemangioma）」，下列何項描述最為正確？</div>
      <ul class="opts">
        <li>(A) 囊腫內部呈現高回音；血管瘤呈現無回音。</li>
        <li>(B) 兩者皆會有明顯的後方音響陰影（shadowing）。</li>
        <li>(C) 囊腫內部為無回音（anechoic）且具後方音波增強；血管瘤通常呈現高回音（hyperechoic）實質腫塊。</li>
        <li>(D) 血管瘤內部會充滿液體，且伴隨後方增強。</li>
      </ul>
      <details class="rev"><summary class="toggle"></summary><div class="reveal">
        <div class="ans">答案：(C)</div>
        <p>囊腫是水泡，內部全黑並伴隨後方增強；血管瘤是微血管網，通常是白亮的高回音實質腫塊。</p>
      </div></details>
    </div>

    <div class="q" id="q112-60">
      <span class="q-no">Q60</span>
      <div class="q-stem">下列何者是膽囊結石在超音波下的典型特徵？</div>
      <ul class="opts">
        <li>(A) 膽囊內的高回音病灶，後方伴隨音響陰影（Acoustic shadowing），且會隨體位改變而移動。</li>
        <li>(B) 膽囊內的無回音病灶，伴隨後方音波增強。</li>
        <li>(C) 固定在膽囊壁上的高回音病灶，無後方陰影。</li>
        <li>(D) 膽囊整體呈現瀰漫性高回音。</li>
      </ul>
      <details class="rev"><summary class="toggle"></summary><div class="reveal">
        <div class="ans">答案：(A)</div>
        <p>結石會擋住聲波，所以自己是亮的，後方是黑的（陰影），且在膽囊液中會隨重力移動。</p>
      </div></details>
    </div>

  </section>

  </main>
</div>
</div>

<footer>
  <div class="wrap">
    <p><b>裸讀學習筆記</b> · 專為醫學生打造的國考與區段重點整理。<br>
    版權所有，未經授權請勿轉載。但你可以把網址分享給正在痛苦掙扎的同學。</p>
  </div>
</footer>

<script>
  // 手機版目錄點擊收合
  document.querySelectorAll('.toc-links a').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 700) {
        document.getElementById('tocBox').open = false;
      }
    });
  });
</script>
</body>
</html>
"""

# write file
os.makedirs("/Users/furyan/.gemini/antigravity/scratch/notes/block7", exist_ok=True)
with open("/Users/furyan/.gemini/antigravity/scratch/notes/block7/gi-ultrasound.html", "w", encoding="utf-8") as f:
    f.write(html_content)
