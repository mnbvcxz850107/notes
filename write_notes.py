import os

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>腹部理學檢查與糞便檢查 (Physical Examination & FOBT) | 高醫臨床技能</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --pri:#2b4b6f; --sec:#3b6998; --bg:#f8f9fa; --txt:#333; --border:#e9ecef;
    --acc:#e83e8c; --hl:#fff3cd; --quiz-bg:#fdfdfe; --quiz-border:#dee2e6;
    --box-key-bg:#e3f2fd; --box-key-border:#90caf9;
    --box-trap-bg:#ffebee; --box-trap-border:#ef9a9a;
    --box-exam-bg:#fff8e1; --box-exam-border:#ffe082;
  }
  body{
    font-family:'Noto Sans TC',sans-serif; background:var(--bg); color:var(--txt);
    line-height:1.7; margin:0; padding:0;
  }
  .hero{
    background:linear-gradient(135deg,var(--pri),var(--sec)); color:#fff;
    padding:3rem 1rem; text-align:center; box-shadow:0 4px 6px rgba(0,0,0,0.1);
  }
  .hero h1{margin:0; font-size:2.2rem; letter-spacing:1px; text-shadow:1px 1px 3px rgba(0,0,0,0.2);}
  .hero p{margin:1rem 0 0; font-size:1.1rem; opacity:0.9;}
  .container{max-width:1200px; margin:0 auto; padding:2rem 1rem;}
  .intro-card{
    background:#fff; border-radius:12px; padding:1.5rem; margin:-3rem auto 2rem;
    max-width:800px; box-shadow:0 8px 16px rgba(0,0,0,0.1);
    display:flex; justify-content:space-around; text-align:center;
    position:relative; z-index:10;
  }
  .stat{display:flex; flex-direction:column; gap:0.5rem;}
  .stat-val{font-size:1.8rem; font-weight:700; color:var(--pri);}
  .stat-lbl{font-size:0.9rem; color:#6c757d;}
  .layout{display:flex; gap:2rem;}
  .sidebar{width:250px; flex-shrink:0;}
  .toc{
    background:#fff; border-radius:8px; padding:1.5rem;
    position:sticky; top:2rem; box-shadow:0 2px 8px rgba(0,0,0,0.05);
  }
  .toc summary{font-weight:700; color:var(--pri); cursor:pointer; list-style:none;}
  .toc summary::-webkit-details-marker{display:none;}
  .toc ul{list-style:none; padding:0; margin:1rem 0 0;}
  .toc li{margin-bottom:0.8rem;}
  .toc a{color:#495057; text-decoration:none; font-size:0.95rem; display:block; transition:color 0.2s;}
  .toc a:hover{color:var(--pri); font-weight:500;}
  .main-content{flex-grow:1; min-width:0;}
  section{background:#fff; border-radius:12px; padding:2rem; margin-bottom:2rem; box-shadow:0 2px 8px rgba(0,0,0,0.05);}
  .sec-head{
    border-bottom:2px solid var(--border); padding-bottom:1rem; margin-bottom:1.5rem;
    display:flex; align-items:baseline; gap:1rem;
  }
  .sec-head h2{margin:0; font-size:1.8rem; color:var(--pri);}
  .sec-head span{color:#6c757d; font-size:0.9rem;}
  p{margin:0 0 1.2rem;}
  mark{background:var(--hl); padding:0.2em 0.4em; border-radius:4px; font-weight:500;}
  
  .box{border-left:4px solid; padding:1rem 1.5rem; border-radius:0 8px 8px 0; margin:1.5rem 0;}
  .box.key{background:var(--box-key-bg); border-color:var(--box-key-border);}
  .box.trap{background:var(--box-trap-bg); border-color:var(--box-trap-border);}
  .box.exam{background:var(--box-exam-bg); border-color:var(--box-exam-border);}
  .box-title{font-weight:700; margin-bottom:0.5rem; display:block;}
  .box.key .box-title{color:#1565c0;}
  .box.trap .box-title{color:#c62828;}
  .box.exam .box-title{color:#f57f17;}

  .tw{overflow-x:auto; margin:1.5rem 0;}
  table{width:100%; border-collapse:collapse; min-width:600px;}
  th,td{padding:1rem; text-align:left; border-bottom:1px solid var(--border);}
  th{background:#f8f9fa; font-weight:700; color:var(--pri); white-space:nowrap;}
  
  .quiz, .q{
    background:var(--quiz-bg); border:1px solid var(--quiz-border);
    border-radius:8px; padding:1.5rem; margin:1.5rem 0;
  }
  .q-no{
    display:inline-block; background:var(--pri); color:#fff;
    padding:0.2rem 0.6rem; border-radius:4px; font-size:0.85rem;
    font-weight:700; margin-right:0.5rem;
  }
  .q-topic{color:#6c757d; font-size:0.9rem; font-weight:500;}
  .q-stem{margin:1rem 0; font-weight:500; font-size:1.05rem;}
  details.rev{margin-top:1rem;}
  summary.toggle{
    cursor:pointer; color:var(--sec); font-weight:500; list-style:none;
    display:inline-flex; align-items:center; gap:0.5rem;
  }
  summary.toggle::before{content:'▶'; font-size:0.8rem; transition:transform 0.2s;}
  details[open] summary.toggle::before{transform:rotate(90deg);}
  .reveal{
    margin-top:1rem; padding:1rem; background:#f8f9fa;
    border-radius:6px; border-left:3px solid var(--acc);
  }
  .ans{font-weight:700; color:var(--acc); margin-bottom:0.5rem; font-size:1.1rem;}
  .src{margin-top:1rem; font-size:0.85rem; color:#adb5bd; text-align:right;}
  
  .yrhead{
    background:var(--sec); color:#fff; padding:0.5rem 1rem;
    border-radius:6px; font-weight:700; margin:2rem 0 1rem;
  }
  .actions{display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem;}
  .btn{
    background:var(--pri); color:#fff; border:none; padding:0.5rem 1rem;
    border-radius:4px; cursor:pointer; font-size:0.9rem; font-family:inherit;
    transition:background 0.2s;
  }
  .btn:hover{background:var(--sec);}
  footer{text-align:center; padding:2rem; color:#6c757d; border-top:1px solid var(--border); margin-top:2rem;}
  
  @media(max-width:768px){
    .layout{flex-direction:column;}
    .sidebar{width:100%;}
    .intro-card{flex-direction:column; gap:1.5rem;}
    .tw table{display:block; width:100%;}
    .tw thead{display:none;}
    .tw tr{display:block; border:1px solid var(--border); margin-bottom:1rem; border-radius:8px;}
    .tw td{display:flex; justify-content:space-between; align-items:center; padding:0.8rem; border-bottom:1px solid #eee;}
    .tw td::before{content:attr(data-label); font-weight:700; color:var(--pri); margin-right:1rem;}
  }
</style>
</head>
<body>

<header class="hero">
  <h1>腹部理學檢查與糞便檢查</h1>
  <p>胡晃鳴老師 | Physical Examination & FOBT</p>
</header>

<div class="container">
  <div class="intro-card">
    <div class="stat"><span class="stat-val">12</span><span class="stat-lbl">歷屆考題</span></div>
    <div class="stat"><span class="stat-val">4</span><span class="stat-lbl">核心步驟 (視聽叩觸)</span></div>
    <div class="stat"><span class="stat-val">FOBT</span><span class="stat-lbl">大腸癌篩檢</span></div>
  </div>

  <div class="layout">
    <aside class="sidebar">
      <details class="toc" id="tocBox" open>
        <summary>目錄導覽</summary>
        <ul>
          <li><a href="#s1">導讀：第一次看診</a></li>
          <li><a href="#s2">診間順序：為什麼得先聽？</a></li>
          <li><a href="#s3">視診：用眼睛說話</a></li>
          <li><a href="#s4">聽診：小腸裡的音樂</a></li>
          <li><a href="#s5">叩診：敲出來的秘密</a></li>
          <li><a href="#s6">觸診：手感的世界</a></li>
          <li><a href="#s7">罕見徵象與出血</a></li>
          <li><a href="#s8">鼻胃管：從鼻孔到小腸</a></li>
          <li><a href="#s9">糞便潛血檢查 (FOBT)</a></li>
          <li><a href="#s10">直腸指診 (DRE)</a></li>
          <li><a href="#s11">一分鐘考前秒殺心法</a></li>
          <li><a href="#exam">歷屆考題全收錄</a></li>
        </ul>
      </details>
    </aside>

    <main class="main-content">
      <section id="s1">
        <div class="sec-head"><h2>導讀：第一次看診病人的第一年生</h2><span>Clinical Scenario</span></div>
        <p>想像你是一位剛穿上白袍的醫學生。今天急診來了一位七十歲的阿公，他弓著身子，雙手捂著肚子，痛苦地說：「醫生，我肚子好痛啊……」家屬在一旁焦急萬分。</p>
        <p>這時候，你要做些什麼？</p>
        <p>在沒有高科技如電腦斷層（CT）或超音波的年代，醫師就像是偵探。我們的武器就是我們的感官：眼睛、耳朵、還有雙手。腹部的器官都隱藏在一層皮膚和肌肉之下，就像一個神秘的黑盒子。要解開阿公腹痛的謎團，你需要一套有系統的檢查方法，那就是<strong>腹部理學檢查 (Abdominal Physical Examination)</strong>。</p>
        <p>腹部理學檢查不僅僅是摸摸肚子而已。它包含了四大步驟：視診（看）、聽診（聽）、叩診（敲）、觸診（摸）。這四個步驟就像是解鎖黑盒子的四把鑰匙。今天，我們就要一步一步帶你了解，如何像神探福爾摩斯一樣，從這些細微的線索中，揪出隱藏在肚子裡的病因。</p>
      </section>

      <section id="s2">
        <div class="sec-head"><h2>診間的順序：為什麼得先聽再觸？</h2><span>Examination Sequence</span></div>
        <p>一般我們做身體檢查，順序通常是「視、觸、叩、聽」（望聞問切）。但<strong>腹部檢查偏偏不一樣，它的順序是：視 (Inspection) → 聽 (Auscultation) → 叩 (Percussion) → 觸 (Palpation)</strong>。</p>
        <p>為什麼要把「聽」放到前面，而把「觸」和「叩」放到後面呢？</p>
        <p>想像一下，腸子是一群正在安靜休息或是規律蠕動的蟲蟲。如果你一開始就用手去「摸（觸診）」或「敲（叩診）」，就像是驚動了這群蟲蟲。腸胃道受到外力的刺激，蠕動就會改變（可能會突然加速，或者因為疼痛而痙攣）。</p>
        <p>所以，如果你先摸了肚子再去聽，你聽到的腸音就<strong>不再是原本真實的狀況了</strong>，而是被你「人為製造」出來的腸音。</p>
        
        <div class="box key">
          <span class="box-title">考試必考重點：腹部理學檢查的黃金順序</span>
          <p>腹部檢查順序必須嚴格遵守：<mark>視 (I) → 聽 (A) → 叩 (P) → 觸 (P)</mark>。<br>
          理由：觸診和叩診會改變腸蠕動的頻率與聲音（Bowel sounds），影響聽診的準確性。而且，觸診如果引起疼痛，病人會產生防衛機制（腹部肌肉緊繃），後續的檢查就很難進行。</p>
          <p>還有一個重要原則：<mark>觸診時，永遠從「最不痛」的地方開始</mark>，把最痛的區域留到最後。這也是為了避免一開始就引發劇痛導致病人肌肉緊繃，影響整體檢查。</p>
        </div>

        <div class="quiz">
          <div class="q-no">Inline Q1</div><span class="q-topic">理學檢查順序與原則</span>
          <p class="q-stem">腹部理學檢查的步驟應如何依序進行？在觸診時，順序又該如何拿捏？</p>
          <details class="rev">
            <summary class="toggle">看解答</summary>
            <div class="reveal">
              <div class="ans">視 → 聽 → 叩 → 觸；從最不痛處開始觸診。</div>
              <p>腹部理學檢查順序與一般身體檢查不同，因為觸壓會改變腸音。觸診從最不痛處開始，是為了避免病患一開始就因為劇痛而產生腹壁肌肉僵硬（Guarding），導致後續檢查無法進行。這也是 [BM111-3] 的考點！</p>
              <a href="#q111-3">前往完整考題 BM111-3</a>
            </div>
          </details>
        </div>
      </section>

      <section id="s3">
        <div class="sec-head"><h2>視診：用眼睛說話</h2><span>Inspection</span></div>
        <p>檢查的第一步，是請病患平躺，掀開衣服露出腹部，雙手放在身體兩側或胸前。千萬不要讓病患雙手抱頭，這會讓腹部肌肉緊繃。同時，要確保患者的隱私（尤其異性檢查時，應有護理師在場陪同）。</p>
        <p>我們用眼睛觀察什麼？</p>
        <ul>
          <li><strong>外觀形狀：</strong>肚子是平的、凹陷的（Scaphoid，像船底，營養不良常見），還是異常膨隆的（Distension）？肚子脹大可能是因為 5 個 F：Fat（脂肪）、Fluid（腹水）、Feces（糞便）、Flatus（氣體）、Fetus（懷孕）。</li>
          <li><strong>表面特徵：</strong>有沒有開刀留下的疤痕（Scar）？這暗示患者可能曾經有過腸沾黏的風險。有沒有妊娠紋（Striae）？如果是紫紅色的妊娠紋，可能是庫欣氏症候群（Cushing's syndrome）。</li>
          <li><strong>血管異常：</strong>肚臍周圍有沒有青筋暴露，像蛇一樣彎曲？這叫做 <mark>Caput medusae（梅杜莎之頭）</mark>，是因為肝硬化導致門脈高壓，血液無法流回肝臟，只好從肚臍周圍的靜脈抄捷徑流回心臟而造成的靜脈曲張。</li>
          <li><strong>蠕動波 (Visible peristalsis)：</strong>在很瘦的病人或腸阻塞（Bowel obstruction）的病人身上，你有時可以直接看到肚皮底下腸子在用力蠕動的波浪。</li>
        </ul>
      </section>

      <section id="s4">
        <div class="sec-head"><h2>聽診：小腸裡面的音樂</h2><span>Auscultation</span></div>
        <p>聽診主要聽兩個東西：腸音（Bowel sounds）和血管雜音（Bruits）。</p>
        <p><strong>1. 腸音 (Bowel sounds)：</strong><br>
        腸子在蠕動推動食物和空氣時，會發出「咕嚕咕嚕」的聲音。我們通常用聽診器的膜面（Diaphragm）放在右下腹（回盲瓣附近，這裡是腸子活動最頻繁的地方）來聽。</p>
        <ul>
          <li><strong>正常：</strong>每分鐘大約 5 到 34 次。</li>
          <li><strong>活性增強 (Hyperactive)：</strong>聲音很大、很頻繁，甚至有高亢的金屬音（High-pitched tinkling）。這發生在<mark>早期腸阻塞</mark>時。想像水管被塞住了，前面的馬達（腸子）就會更用力、更急促地打水，試圖衝破阻塞。</li>
          <li><strong>腸音消失 (Absent)：</strong>要連續聽 2 到 5 分鐘都沒聲音才能判定。這發生在<mark>麻痺性腸喜 (Paralytic ileus)</mark>，例如腹部手術後、嚴重的腹膜炎，腸子「罷工」不動了。</li>
        </ul>
        <p><strong>2. 血管雜音 (Bruits)：</strong><br>
        用聽診器的鐘面（Bell）聽主動脈、腎動脈、髂動脈的位置。如果有像水流過狹窄峽谷的「咻咻」聲，表示血管可能有狹窄或動脈瘤。</p>
      </section>

      <section id="s5">
        <div class="sec-head"><h2>叩診：敲出來的秘密</h2><span>Percussion</span></div>
        <p>叩診是用一隻手的手指平貼在肚子上，用另一隻手的手指去敲擊。敲出來的聲音可以告訴我們肚子底下的東西是「空氣」還是「實心」的。</p>
        <p><strong>鼓音 (Tympany) vs. 濁音 (Dullness)：</strong><br>
        敲打充滿空氣的胃和腸子，會發出像打鼓一樣清脆的<strong>鼓音 (Tympany)</strong>。如果敲到實體的器官（如肝臟、脾臟）、腫瘤、或是液體（腹水），就會發出沉悶的<strong>濁音 (Dullness)</strong>。</p>

        <p><strong>器官大小的測量：</strong></p>
        <ul>
          <li><strong>肝臟 (Liver)：</strong>我們沿著右鎖骨中線 (MCL) 由下往上敲（從鼓音變濁音），再由上往下敲（從肺部的共鳴音變濁音），這樣就能量出肝臟的長度。<mark>正常肝臟在 MCL 的長度約為 6-12 公分</mark>。大於這個範圍就是肝腫大 (Hepatomegaly)。</li>
          <li><strong>脾臟 (Spleen)：</strong>正常情況下，左下胸的 Traube's space（胃泡的位置）應該是鼓音。如果脾臟腫大，這裡就會變成濁音。</li>
        </ul>

        <div class="box exam">
          <span class="box-title">腹水 (Ascites) 的三大檢測法</span>
          <p>當肚子很大，我們懷疑裡面有水（腹水，最常見於肝硬化）時，可以做以下測試：</p>
          <ol>
            <li><strong>移動性濁音 (Shifting dullness)：</strong>這是最常考的！病人仰躺時，水積在兩側，腸子飄在中間。所以中間敲起來是鼓音，兩側是濁音。<mark>請病人側躺</mark>，水會往低處流，空氣往高處跑。如果原本是濁音的地方變成了鼓音，這就是「移動性濁音」，代表肚子裡有游離的腹水。</li>
            <li><strong>液體波動感 (Fluid wave)：</strong>適用於大量腹水。你需要請病人或助手的手刀壓在病人肚臍中線上（阻擋肚皮脂肪的震動）。你一手貼在病人左側腹，另一手彈擊右側腹。如果你左手感覺到波浪傳過來，這就是液體波動。</li>
            <li><strong>水坑徵象 (Puddle sign)：</strong>適用於微量腹水，請病人趴著，讓水積在肚子最前側，然後用聽診器聽。</li>
          </ol>
        </div>

        <div class="quiz">
          <div class="q-no">Inline Q2</div><span class="q-topic">腹水檢查的原理</span>
          <p class="q-stem">如何藉由叩診確認病患是否有腹水 (Shifting dullness)？</p>
          <details class="rev">
            <summary class="toggle">看解答</summary>
            <div class="reveal">
              <div class="ans">自肚臍開始往側腹叩診尋找鼓音變濁音的交界，然後請患者側躺，觀察交界點是否移動。</div>
              <p>腹水會因為重力改變位置。仰躺時水在兩側法蘭克區 (flank)，中間因為腸氣呈現鼓音 (Tympanic)。當側躺時，水流向下方，原本上方的側腹就會從濁音變成鼓音。請參考考題 [BM111-4]。</p>
              <a href="#q111-4">前往完整考題 BM111-4</a>
            </div>
          </details>
        </div>
      </section>

      <section id="s6">
        <div class="sec-head"><h2>觸診：手感的世界</h2><span>Palpation</span></div>
        <p>觸診是理學檢查最關鍵的一步。分為淺觸診（Light palpation）和深觸診（Deep palpation）。<br>
        <strong>淺觸診：</strong>下壓約 1 公分，主要找肌肉的緊繃、表淺的壓痛。<br>
        <strong>深觸診：</strong>下壓約 4-5 公分，用來摸器官的大小（肝、脾、腎）和深層的腫塊。正常的肝臟邊緣，在右肋骨下緣剛好摸得到或在肋骨下緣 1 公分內，質地應該是平滑的（如果像摸到石頭一樣凹凸不平，可能是肝硬化或肝癌）。</p>

        <p><strong>腹膜炎的徵象 (Peritoneal signs)：</strong><br>
        當腹腔內的臟器發炎破裂，感染了整片腹膜時，會產生嚴重的腹膜炎。病人會有幾個經典表現：</p>
        <ul>
          <li><strong>肌肉僵直 (Rigidity/Guarding)：</strong>肚子摸起來像木板一樣硬，這是身體為了保護發炎器官而產生的不自主肌肉收縮。</li>
          <li><strong>反彈痛 (Rebound tenderness / Blumberg sign)：</strong>這是國考常客。<mark>當你深深壓下病人的肚子，停留幾秒，然後「突然放開」，病人在放開的那一瞬間會感覺到比按壓時更劇烈的疼痛。</mark> 這是因為放開的瞬間，發炎的腹膜產生了回彈的拉扯。</li>
        </ul>

        <div class="box exam">
          <span class="box-title">急性闌尾炎 (盲腸炎) 的神聖密碼</span>
          <p>闌尾炎是急診最常見的急腹症。這四個 Sign 你一定要背熟：</p>
          <ol>
            <li><strong>McBurney's point：</strong>這是一個「點」。位置在右髂前上棘 (ASIS) 與肚臍連線的外 1/3 處。這裡是盲腸的解剖位置，闌尾炎時這裡會最痛。</li>
            <li><strong>Rovsing's sign：</strong>這是一個「遠端遙控痛」。<mark>當你用力按壓病人的左下腹 (LLQ) 時，病人卻大喊「右下腹 (RLQ) 痛」！</mark> 這是因為你按壓左邊大腸的空氣，空氣逆推回右邊發炎的盲腸。</li>
            <li><strong>Psoas sign (腰肌徵象)：</strong>請病人向左側躺，你將他的右大腿往後伸展 (Extension)。這個動作會拉扯到腰肌。如果盲腸剛好位在盲腸後方（Retrocecal），發炎的盲腸摩擦到被拉緊的腰肌，就會引起右下腹痛。</li>
            <li><strong>Obturator sign (閉孔肌徵象)：</strong>病人仰躺，右膝與右髖關節彎曲 90 度，然後將小腿往外撥（讓髖關節內旋）。這會牽扯到閉孔內肌，如果闌尾位置較深（Pelvic appendix），就會引發疼痛。</li>
          </ol>
        </div>

        <div class="box key">
          <span class="box-title">急性膽囊炎的招牌：Murphy's sign (墨菲氏徵象)</span>
          <p>將手指深深壓入病人的右上腹（肋骨下緣，膽囊的位置），然後請病人「深吸一口氣」。<br>
          當病人吸氣時，橫膈膜下降，會把肝臟和發炎的膽囊往下推。當發炎的膽囊撞擊到你深壓的手指時，病人會因為劇痛而<strong>突然停止吸氣 (Arrest of inspiration)</strong>。這就叫做 Murphy's sign 陽性，是急性膽囊炎的典型特徵。</p>
        </div>

        <div class="quiz">
          <div class="q-no">Inline Q3</div><span class="q-topic">特殊徵象總複習</span>
          <p class="q-stem">一位疑似闌尾炎的患者，急診醫師說有 "Aaron's sign" (按壓麥氏點引起上腹或心窩痛)，請問下列哪些理學檢查徵象也與闌尾炎強烈相關？<br>
          1. McBurney's point  2. Knocking pain  3. Obturator sign  4. Murphy's sign  5. Rovsing's sign</p>
          <details class="rev">
            <summary class="toggle">看解答</summary>
            <div class="reveal">
              <div class="ans">1, 3, 5</div>
              <p>闌尾炎相關的為 McBurney, Obturator, Rovsing, 以及 Psoas sign。而 Murphy's sign 是膽囊炎的徵象，Knocking pain (叩擊痛) 通常指 CVA knocking pain，是腎盂腎炎的徵象。請參考考題 [BM111-6]。</p>
              <a href="#q111-6">前往完整考題 BM111-6</a>
            </div>
          </details>
        </div>
      </section>

      <section id="s7">
        <div class="sec-head"><h2>罕見但致命的出血徵象</h2><span>Special Signs of Hemorrhage</span></div>
        <p>在腹部理學檢查中，有時會在皮膚上看到奇怪的瘀青，這往往暗示著腹腔深處（後腹腔）發生了嚴重的出血（例如嚴重的出血性胰臟炎、腹主動脈瘤破裂、子宮外孕破裂）。</p>
        <ul>
          <li><strong>Cullen's sign (庫倫氏徵象)：</strong><mark>肚臍周圍</mark>出現藍紫色的瘀斑。血液從後腹腔沿著韌帶滲透到肚臍周圍的皮下。</li>
          <li><strong>Grey Turner's sign (格雷透納氏徵象)：</strong><mark>側腹部 (Flank)</mark>出現藍紫色瘀斑。血液在後腹腔積聚並蔓延到腰側。</li>
        </ul>
        <p>這兩個徵象一旦出現，代表病情非常危急，是急診醫師眼中的「大魔王」。</p>

        <div class="box trap">
          <span class="box-title">Courvoisier's sign (庫瓦濟埃氏徵象) - 不是膽結石！</span>
          <p>如果你在病人的右上腹摸到一顆<strong>腫大、但是「不會痛 (Non-tender)」的膽囊</strong>，而且病人全身黃疸 (Jaundice)。這就是 Courvoisier's sign。<br>
          <mark>它暗示的病因是：胰臟頭癌 (Pancreatic head cancer) 或膽管癌。</mark></p>
          <p><strong>為什麼不是膽結石？</strong><br>
          因為如果是膽結石造成的慢性發炎，膽囊壁會纖維化、萎縮，所以「摸不到腫大的膽囊」，而且結石發炎「一定會痛」。所以不痛又腫大的膽囊，代表膽管被腫瘤慢性、無痛地慢慢阻塞，把膽囊撐得像氣球一樣大。</p>
        </div>
      </section>

      <section id="s8">
        <div class="sec-head"><h2>鼻胃管：從鼻孔到小腸的旅行</h2><span>Nasogastric Tube (NG Tube)</span></div>
        <p>鼻胃管是一根從鼻子插入，經過食道，到達胃部的管子。它在臨床上非常常用。</p>
        <p><strong>為什麼要插鼻胃管 (Indications)？</strong></p>
        <ul>
          <li><strong>減壓 (Decompression)：</strong>腸阻塞時，胃腸裡積滿了氣體和液體，病人會狂吐。插管把這些髒東西抽出來，讓腸胃休息。</li>
          <li><strong>餵食 (Feeding)：</strong>中風吞嚥困難的病人，可以透過管子打入營養品。</li>
          <li><strong>給藥 / 洗胃：</strong>藥物中毒時用來洗胃。</li>
        </ul>

        <p><strong>禁忌症 (Contraindications)：</strong>如果病人臉部嚴重骨折、懷疑食道破裂，或有嚴重的凝血功能障礙，就不能盲插，以免管子插進腦部或引發大出血。</p>

        <p><strong>怎麼放？怎麼知道放對了？</strong></p>
        <ol>
          <li><strong>姿勢：</strong>病人平躺，床頭抬高 30-60 度。</li>
          <li><strong>測量長度：</strong><mark>從鼻尖 → 耳垂 → 劍突下緣 (Xiphoid process)</mark>。這段長度大約就是管子要插入的深度。</li>
          <li><strong>插入：</strong>順著鼻底平行推入。當管子到達鼻咽部時，請病人做<strong>「吞嚥」</strong>動作（可以給一點水喝），順著吞嚥的動作將管子推入食道。千萬不要硬戳，以免刺破食道！</li>
          <li><strong>確認位置：</strong>這是國考必考！怎麼知道管子在胃裡，沒有誤入氣管？
            <ul>
              <li><strong>聽診打氣法：</strong>用空針打入少量空氣，同時聽診器放在胃部（左上腹），如果聽到「咕嚕」氣泡聲，表示在胃裡。</li>
              <li><strong>反抽法：</strong>用空針反抽，看有沒有抽到胃液或未消化的食物。</li>
              <li><strong>X光確認：</strong>這是最準確的黃金標準（Gold standard）。</li>
            </ul>
          </li>
        </ol>
      </section>

      <section id="s9">
        <div class="sec-head"><h2>糞便潛血檢查 (FOBT)：篩檢大腸癌的利器</h2><span>Fecal Occult Blood Test</span></div>
        <p>大腸癌是台灣發生率極高的癌症。早期的腸癌或瘜肉，往往沒有任何症狀，但它們會偷偷地在腸道裡微量出血。這種血量很少，肉眼看不到，大便顏色也正常，這就叫做「潛血 (Occult blood)」。</p>
        <p>目前常用的糞便潛血檢查分為兩種：</p>

        <div class="tw">
          <table>
            <thead>
              <tr>
                <th>比較項目</th>
                <th>化學法 (gFOBT - Guaiac)</th>
                <th>免疫法 (iFOBT / FIT)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>原理</td>
                <td>利用血紅素中的 Heme 具有類似過氧化物酶的作用，加入雙氧水後會變藍色。</td>
                <td>使用抗體，專一性地結合「人類血紅素」(Human Hemoglobin)。</td>
              </tr>
              <tr>
                <td>特異性</td>
                <td>較低。會受食物影響。</td>
                <td><strong>極高。只認得人類的血。</strong></td>
              </tr>
              <tr>
                <td>飲食限制</td>
                <td><strong>檢查前 3 天必須禁食：</strong><br>1. 含血肉類（豬血、紅肉）<br>2. 鐵劑<br>3. 維他命 C</td>
                <td><strong>不需限制飲食。</strong>想吃豬血糕、牛排都可以。</td>
              </tr>
              <tr>
                <td>上消化道出血</td>
                <td>會呈現陽性（因為胃出血的 Heme 來到大腸仍有活性）。</td>
                <td>通常呈現陰性（因為蛋白質抗原在經過胃酸和消化酵素作用後已經被破壞）。</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="box trap">
          <span class="box-title">考題陷阱：偽陽性與偽陰性</span>
          <p><strong>化學法 (gFOBT) 的偽陽性 (沒病卻驗出陽性)：</strong>因為吃豬血糕、紅肉，或是吃阿斯匹靈 (NSAIDs) 導致輕微胃出血。<br>
          <strong>化學法 (gFOBT) 的偽陰性 (有病卻驗不出來)：</strong>大量服用<mark>維他命 C (Vitamin C)</mark>。因為維他命 C 是強抗氧化劑，會阻斷化學呈色反應，導致明明有出血卻驗出陰性！</p>
        </div>

        <p><strong>臨床處置原則：</strong><br>
        只要糞便潛血檢查呈現<strong>陽性</strong>，無論病人有沒有症狀，都<strong>必須安排「大腸鏡檢查 (Colonoscopy)」</strong>。不能說因為吃了什麼就不管它，也不能只叫病人再驗一次糞便。陽性 = 大腸鏡，這是死規定。</p>
        <p>台灣國健署目前提供 50 歲至 74 歲民眾，每 2 年一次免費的「免疫法 (FIT)」大腸癌篩檢。</p>

        <div class="quiz">
          <div class="q-no">Inline Q4</div><span class="q-topic">iFOBT 結果判讀</span>
          <p class="q-stem">60 歲男性收到免疫法糞便篩檢 (iFOBT) 陽性報告，他認為是因為前兩天吃了豬血糕所致，拒絕大腸鏡。請問他的觀念正確嗎？臨床上該如何處置？</p>
          <details class="rev">
            <summary class="toggle">看解答</summary>
            <div class="reveal">
              <div class="ans">觀念錯誤。iFOBT 不受動物血影響。處置：必須安排大腸鏡。</div>
              <p>免疫法 (FIT/iFOBT) 具有物種專一性，只會對「人類血紅素」產生反應，因此吃豬血糕、牛排都不會造成偽陽性。只要檢驗為陽性，就代表腸道有出血點，必須進行大腸鏡找出原因（瘜肉、腫瘤、潰瘍等）。請參考考題 [BM112-8]。</p>
              <a href="#q112-8">前往完整考題 BM112-8</a>
            </div>
          </details>
        </div>
      </section>
      
      <section id="s10">
        <div class="sec-head"><h2>直腸指診：不得不做的檢查</h2><span>Digital Rectal Exam (DRE)</span></div>
        <p>這是很多醫學生覺得最尷尬，但也最不能忽略的檢查。許多直腸下段的癌症，光靠一根手指頭就能摸出來！</p>
        <p><strong>檢查姿勢：</strong>最常用的是<strong>左側臥姿 (Left lateral decubitus)</strong>，雙膝向胸部彎曲。</p>
        <p><strong>我們在摸什麼？</strong></p>
        <ol>
          <li><strong>肛門括約肌張力 (Sphincter tone)：</strong>評估神經功能。</li>
          <li><strong>直腸壁：</strong>有沒有摸到硬塊（直腸癌）、瘜肉。</li>
          <li><strong>攝護腺 (Prostate)：</strong>在男性，直腸前方就是攝護腺。正常摸起來像鼻尖一樣有彈性；如果是攝護腺癌，摸起來會像石頭一樣硬。</li>
          <li><strong>糞便性質：</strong>手指退出後，看看手套上有沒有血（鮮血或黑便），並可以直接取大便去做糞便潛血檢查。</li>
        </ol>
      </section>

      <section id="s11">
        <div class="sec-head"><h2>一分鐘考前秒殺心法</h2><span>Key Takeaways</span></div>
        <ul>
          <li><strong>順序：</strong>視 → 聽 → 叩 → 觸。(避免改變腸音)</li>
          <li><strong>觸診：</strong>從最不痛的地方開始摸。</li>
          <li><strong>Murphy's sign：</strong>吸氣時壓右上腹劇痛中止呼吸 → 急性膽囊炎。</li>
          <li><strong>McBurney's / Rovsing's / Psoas / Obturator：</strong>都是急性闌尾炎。</li>
          <li><strong>腹水叩診：</strong>Shifting dullness (移動性濁音)，翻身看交界線會不會動。</li>
          <li><strong>鼻胃管長度：</strong>鼻尖 → 耳垂 → 劍突下緣。打氣聽胃部確認位置。</li>
          <li><strong>gFOBT 偽陰性：</strong>維他命 C。</li>
          <li><strong>iFOBT 陽性：</strong>不用懷疑豬血糕，直接做大腸鏡。</li>
        </ul>
      </section>

      <section id="exam">
        <div class="sec-head"><h2>歷屆考題全收錄</h2><span>Past Exams</span></div>
        <div class="actions">
          <p>共收錄 12 題 (BM113 - BM111)。請搭配上方內文服用。</p>
          <button id="allBtn" class="btn">全部展開答案</button>
        </div>

        <!-- BM113 -->
        <div class="yrhead">113 學年度 (BM113 期末考) · 3 題</div>
        <div class="q" id="q113-5"><span class="q-no">113-5</span><span class="q-topic">腹痛理學檢查綜合判斷</span>
          <p class="q-stem">5. 60 歲的糖尿病男性病患，因急性上腹部疼痛至急診就醫。醫師問診時，病人說腹痛為廣泛性持續悶痛，而且漸漸往右下腹移動。以下關於後續理學檢查的描述，何者最適當？<br>
          (A) 在進行腹部理學檢查時，病人抱怨右下腹最痛，醫師為了快速確定診斷，應從右下腹開始進行觸診。<br>
          (B) 當醫師懷疑病患有腹膜炎，在輕壓病患的左下腹部時，病患卻說右下腹部會痛，此為 Psoas sign 陽性反應。<br>
          (C) 病患抽血報告發現發炎指數（白血球及 C 反應蛋白）正常，醫師高度懷疑急性闌尾炎可能，於是幫病患進行叩診，以聽取 Tympanic sound 來確診急性闌尾炎。<br>
          (D) 若醫師在病患右下腹進行深觸診後，突然放開雙手，病患表示放開瞬間比按壓時更痛，這稱為 Rebound tenderness，強烈暗示腹膜發炎。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D)</div><p>• (A) 觸診應從最不痛處開始；(B) 壓左邊痛右邊為 Rovsing's sign，而非 Psoas sign；(C) 闌尾炎無法單靠叩診聽 Tympanic sound 確診，且發炎指數通常會升高；(D) 描述的正是 Rebound tenderness (反彈痛)，是腹膜炎的典型徵象。</p><div class="src">出處：BM113 期末考 第5題（胡晃鳴）</div></div></details>
        </div>

        <div class="q" id="q113-6"><span class="q-no">113-6</span><span class="q-topic">鼻胃管置入與確認</span>
          <p class="q-stem">6. 續上題，病患在急診等待期間，突然開始大量嘔吐出墨綠色液體（Bile-stained vomitus），醫師懷疑有腸阻塞的可能，決定放置鼻胃管（Nasogastric tube, NG tube）進行減壓。關於鼻胃管的放置與確認，下列哪一項敘述最正確？<br>
          (A) 為避免病患將嘔吐物吸入氣管，放置鼻胃管時，應請病患平躺，並將頭部完全放平（0 度）。<br>
          (B) 插入鼻胃管的長度估算，是測量從病患鼻尖到耳垂，再往下延伸至肚臍的距離。<br>
          (C) 插入鼻胃管時，當管子前端到達病患鼻咽部，可請病患配合做吞嚥動作，順勢將管子推進食道，千萬不要盲目用力推擠。<br>
          (D) 確認鼻胃管是否成功進入胃部的最佳且唯一方法，是用空針打入空氣並同時在左下腹部聽診。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C)</div><p>• (A) 應將床頭抬高 30-60 度；(B) 測量長度為鼻尖到耳垂再到「劍突下緣 (Xiphoid)」，非肚臍；(C) 正確，需配合吞嚥動作避免硬插；(D) 聽診是臨床常用方法，但最佳標準（Gold standard）是 X 光確認，且聽診位置應在左上腹（胃部）而非左下腹。</p><div class="src">出處：BM113 期末考 第6題（胡晃鳴）</div></div></details>
        </div>

        <div class="q" id="q113-7"><span class="q-no">113-7</span><span class="q-topic">糞便潛血檢查 (FOBT) 比較</span>
          <p class="q-stem">7. 55 歲的張先生平時愛吃紅肉，最近一次健檢時，家醫科醫師建議他做大腸癌篩檢。張先生對糞便潛血檢查（FOBT）感到疑惑。請問下列關於糞便潛血檢查的說明，何者最正確？<br>
          (A) 化學法（gFOBT）是利用抗體專一性結合人類血紅素，因此不受飲食中動物血液的影響。<br>
          (B) 免疫法（iFOBT / FIT）在採檢前三天必須嚴格限制食用豬血糕、牛肉等含血肉類，以免造成偽陽性。<br>
          (C) 若張先生平時有服用大量維他命 C 的習慣，使用化學法（gFOBT）檢查時，可能會干擾化學呈色反應，導致出現偽陰性的結果。<br>
          (D) 如果張先生的糞便潛血檢查結果為陽性，只要他沒有腹痛或大便型態改變，只需三個月後再複檢一次糞便即可，不需急著做大腸鏡。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C)</div><p>• (A) 化學法是利用 Heme 類過氧化物酶反應，會受動物血影響；(B) 免疫法具人類血紅素專一性，不需限制飲食；(C) 正確，維他命 C 是抗氧化劑，會阻斷化學法的氧化呈色，造成偽陰性；(D) 只要 FOBT 陽性，就必須安排大腸鏡檢查，不可只做複檢。</p><div class="src">出處：BM113 期末考 第7題（胡晃鳴）</div></div></details>
        </div>

        <!-- BM112 -->
        <div class="yrhead">112 學年度 (BM112 期末考) · 5 題</div>
        <div class="q" id="q112-4"><span class="q-no">112-4</span><span class="q-topic">特殊腹部徵象</span>
          <p class="q-stem">4. 以下腹部理學檢查的徵象，何者敘述較不正確？<br>
          (A) Grey Turner's sign 是指在兩側腹部(Flank) 出現因為出血造成的瘀斑，可能是出血性胰臟炎造成的。<br>
          (B) Cullen's sign 是指肚臍周圍出現的皮下瘀斑，有可能是子宮外孕破裂造成的。<br>
          (C) Courvoisier's sign 是指在右上腹摸到無痛性的腫塊，加上病患有黃疸的情形，這通常是因為膽結石阻塞造成的發炎。<br>
          (D) Murphy's sign 是在右邊肋骨下緣深壓，請患者吸氣，患者因膽囊往下移動碰到深壓的手指造成疼痛而中止吸氣，這是急性膽囊炎的徵象。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C)</div><p>• Courvoisier's sign (無痛性腫大膽囊伴隨黃疸) 通常暗示惡性腫瘤(如胰臟頭癌)造成的膽管阻塞，而非膽結石。膽結石引發的膽囊炎通常會痛且膽囊可能因慢性發炎而萎縮。</p><div class="src">出處：BM112 期末考 第4題（胡晃鳴 ppt pg. 44）</div></div></details>
        </div>

        <div class="q" id="q112-5"><span class="q-no">112-5</span><span class="q-topic">鼻胃管確認方法</span>
          <p class="q-stem">5. 有關鼻胃管置放後確認鼻胃管是否在胃裡的方法，以下何者是錯誤的？<br>
          (A) 在胃部聽診時，將空氣打入鼻胃管內，若聽到氣泡聲，表示在胃內。<br>
          (B) 將鼻胃管反抽，如果抽到膽汁或是消化過的食物，表示在胃內。<br>
          (C) 照一張胸部或腹部的 X 光片，如果看到管子末端在胃裡，這也是確認的方法。<br>
          (D) 請病患講話，如果講得出來而且沒有咳嗽，就表示管子是在胃內，而沒有放進氣管內。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D)</div><p>• (D) 錯誤：管子誤入氣管時，有些病人不一定會有劇烈咳嗽，且仍能發聲，不能僅靠講話與咳嗽來確認管子位置。正確方法為聽診打氣、反抽胃液或 X 光確認。</p><div class="src">出處：BM112 期末考 第5題（胡晃鳴 ppt pg. 51）</div></div></details>
        </div>

        <div class="q" id="q112-6"><span class="q-no">112-6</span><span class="q-topic">腹膜炎徵象判斷</span>
          <p class="q-stem">6. 在急診有一位病患因為肚子痛而被送來，醫師要分辨是單純的腸胃炎還是因為腸子破裂造成的腹膜炎時，醫師為病患進行理學檢查時，何者不是腹膜炎常見的發現？<br>
          (A) 腹部肌肉緊繃僵硬 (Rigidity)<br>
          (B) 聽診時有金屬聲的腸音 (Tinkling bowel sound)<br>
          (C) 聽不到腸音 (Absent of bowel sound)<br>
          (D) 深壓病患腹部後放開時病患會覺得更痛 (Rebound tenderness)</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(B)</div><p>• Tinkling bowel sound (高頻金屬音) 是機械性腸阻塞 (Mechanical ileus) 的特徵。腹膜炎會導致麻痺性腸阻塞，腸音會減弱或消失(C)。腹膜發炎會引起肌肉僵硬(A)和反彈痛(D)。</p><div class="src">出處：BM112 期末考 第6題（胡晃鳴 ppt pg. 19）</div></div></details>
        </div>

        <div class="q" id="q112-7"><span class="q-no">112-7</span><span class="q-topic">gFOBT 偽陰性原因</span>
          <p class="q-stem">7. 有關化學法糞便潛血檢查(gFOBT)的敘述，何者會造成偽陰性 (有出血但檢查結果是陰性)？<br>
          (A) 吃大量的維他命 C<br>
          (B) 吃大量的豬血<br>
          (C) 吃阿斯匹靈 (Aspirin)<br>
          (D) 吃未煮熟的牛肉</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(A)</div><p>• 維他命 C 是抗氧化劑，會阻斷 gFOBT 的過氧化酶呈色反應，造成偽陰性。BCD 會造成偽陽性。</p><div class="src">出處：BM112 期末考 第7題（胡晃鳴 ppt pg. 52）</div></div></details>
        </div>

        <div class="q" id="q112-8"><span class="q-no">112-8</span><span class="q-topic">iFOBT 糞便潛血判讀</span>
          <p class="q-stem">8. 一位 60 歲男性，收到糞便篩檢(iFOBT)陽性的報告，也接到衛生所的關懷電話，要他去醫院安排大腸鏡檢查。他覺得無排便異常的情形，這結果可能和糞便送檢前兩天有吃豬血糕的關係，所以沒去檢查。但他的太太知道後，覺得先生得了大腸癌，強迫先生就醫，而兩人為了要不要就醫做大腸鏡而吵了起來。他們問了一些朋友，以下的回應，你覺得何者比較正確？<br>
          (A) 排便沒異常，應該是和吃到動物的血有關，別緊張，不用檢查啦。<br>
          (B) 肉眼沒看到血，應該是那個診所有問題，去大醫院再做一次糞便檢查，真的陽性再去安排大腸鏡就好了。<br>
          (C) 這是一種檢測糞便中是否存在癌細胞的檢查，太太說得對，陽性就是得了大腸癌，一定要趕快檢查，不要再拖了。<br>
          (D) 這個檢驗只告訴我們糞便中有血，未必是大腸癌，但還是要接受大腸鏡檢查，找出可能的出血點比較安全。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(D)</div><p>• iFOBT（免疫法）不受飲食中動物血影響；陽性代表腸道有出血，未必是大腸癌，但必須安排大腸鏡排除瘜肉或早期癌。</p><div class="src">出處：BM112 期末考 第8題（胡晃鳴 ppt pg.53）</div></div></details>
        </div>

        <!-- BM111 -->
        <div class="yrhead">111 學年度 (BM111 期末考) · 4 題</div>
        <div class="q" id="q111-3"><span class="q-no">111-3</span><span class="q-topic">理學檢查原則</span>
          <p class="q-stem">9. 一位 75 歲有中風病史的男性因腹痛，腹漲及噁心，在媳婦陪伴下就診，當徵得病患同意進行腹部理學檢查時，以下的敘述哪些較不適當？<br>
          1. 為保護病患隱私，僅醫師與患者在診間進行檢查即可。<br>
          2. 請患者平躺，掀開衣服以露出腹部，雙手置於胸前，雙膝彎曲踩在床上。<br>
          3. 理學檢查的步驟以視(inspection)，聽(auscultation)，叩(percussion)，觸(palpation)依序進行。<br>
          4. 進行觸診時，從最疼痛的地方開始。<br>
          (A) 13　(B) 23　(C) 14　(D) 1</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C) 14</div><p>• 1 不適當（應有女性護理師在場陪同避免爭議）；4 不適當（觸診應從最不痛處開始，最痛處最後觸診）。</p><div class="src">出處：BM111 期末考 第3題（胡晃鳴）</div></div></details>
        </div>

        <div class="q" id="q111-4"><span class="q-no">111-4</span><span class="q-topic">腹水叩診評估步驟</span>
          <p class="q-stem">10. 續上題，在叩診部分，發現肚臍附近都是tympanic的聲音，主治醫師請你評估看是否有腹水，以下步驟何者正確？<br>
          (A) 自肚臍開始進行扣診並往右邊腹部移動，紀錄聲音改變的位置，再請患者向左側躺，從右腹部開始扣診並往肚臍移動，再次紀錄聲音改變的情形。<br>
          (B) 左手掌放在患者的右側腹部上緊貼著，右手則在患者左側腹部彈動，製造波動，看左手掌是否感覺到波動。<br>
          (C) 將手放在肚子正中間，往下壓，再瞬間放開，看肚子震動情形。<br>
          (D) 請患者吐氣後，把手放在右上腹肋骨下緣，再請患者吸氣。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(A) 移動性濁音</div><p>• 移動性濁音 (Shifting dullness) 藉由改變體位觀察鼓音/濁音交界之移動來診斷腹水。(B) 需第三人/病患手掌在腹中線阻隔皮下脂肪震動。</p><div class="src">出處：BM111 期末考 第4題（胡晃鳴）</div></div></details>
        </div>

        <div class="q" id="q111-5"><span class="q-no">111-5</span><span class="q-topic">鼻胃管錯誤細節</span>
          <p class="q-stem">11. 續上題，在腹部理學檢查過程中，病患有嘔吐情形，且嘔吐物中有咖啡色液體，主治醫師請你協助放置鼻胃管以避免病患持續嘔吐而嗆到。放置鼻胃管相關細節，下列何者錯誤？<br>
          (A) 採平躺姿勢，將床頭抬高30～60度。<br>
          (B) 測量鼻孔到耳根的距離加上耳根到劍突末端的距離，作為鼻胃管放入長度的參考。<br>
          (C) 鼻胃管前端朝下，管子的彎度順著鼻孔的底部慢慢插入，到達鼻咽時可請病人同時做吞嚥動作，之後持續插入至頂到東西的感覺，表示前端已到胃部。<br>
          (D) 確定鼻胃管位置是否正確時，先用灌食空針回抽看看是否有胃內容物被抽出來，之後打入少量空氣，同時在胃部用聽診器聽診，如能聽到氣泡音，即表示位置正確。</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(C)</div><p>• (C) 錯誤：鼻胃管不可盲目用力推進直到「頂到東西」，有穿破食道危險；應依照事前測量之標記長度插入。</p><div class="src">出處：BM111 期末考 第5題（胡晃鳴 ppt pg. 49, 50）</div></div></details>
        </div>

        <div class="q" id="q111-6"><span class="q-no">111-6</span><span class="q-topic">闌尾炎 Aaron sign</span>
          <p class="q-stem">12. 一位56歲女性，無特殊病史或手術史，僅有長期便秘使用藥物，但昨天無排便。昨晚因腹脹，上腹悶痛及噁心至急診就診，經藥物治療後返家，但半夜開始有發燒的情形，中午再度來到急診，且疼痛位置變成了右下腹部。急診醫師請你協助執行腹部理學檢查，並說了一句“她疼痛位置的改變很像是Aaron’s sign”。請問你執行腹部理學檢查時，下列哪些是與急診醫師推測的診斷是相關的？<br>
          1. 檢查McBurney’s point　2. Right side frank knocking pain　3. Obturator muscle sign　4. Murphy’s sign　5. Rovsing’s sign<br>
          (A) 123　(B) 135　(C) 245　(D) 1245</p>
          <details class="rev"><summary class="toggle"></summary><div class="reveal"><div class="ans">正確答案：(B) 135</div><p>• 闌尾炎相關徵象為 McBurney 點 (1)、Obturator sign (3) 與 Rovsing sign (5)。</p><div class="src">出處：BM111 期末考 第6題（胡晃鳴 ppt pg. 37）</div></div></details>
        </div>
      </section>
    </main>
  </div>
</div>

<footer>
  <p><b>高醫臨床技能｜胡晃鳴老師 腹部理學檢查與糞便檢查 深入淺出筆記</b>　共 12 題歷屆考題收錄。</p>
</footer>

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

with open("/Users/furyan/.gemini/antigravity/scratch/notes/block7/physical-examination-fobt.html", "w", encoding="utf-8") as f:
    f.write(html_content)
