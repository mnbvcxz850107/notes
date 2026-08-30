import sys

file_path = '/Users/furyan/.gemini/antigravity/scratch/notes/block7/gi-imaging-diagnosis.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

hint1 = """    <div class="box exam">
      <strong>🎯 老師考訓一級必會點：</strong><br>
      <b>克隆氏症 (Crohn's, CD) vs 潰瘍性結腸炎 (UC) 鑑別：</b><br>
      • CD：節段性/跳躍式 (Segmental/Skip)，直腸約半數侵犯，全層發炎 (Transmural/Deep ulcer)，迴腸末端幾乎一定侵犯，呈現鵝卵石狀 (Cobblestone)，常併發瘻管、膿瘍或狹窄，不對稱結腸袋消失。<br>
      • UC：連續性 (Continuous)，直腸 100% 侵犯，僅限黏膜層 (Mucosal/Shallow)，迴腸末端正常 (少數backwash)，常有假性息肉 (Pseudopolyps)，呈現對稱結腸袋消失或鉛管狀 (Lead pipe)，併發毒性巨結腸 (Toxic megacolon) 或癌變機率較高。
    </div>"""

hint2 = """    <div class="box exam">
      <strong>🎯 老師考訓一級必會點：</strong><br>
      <b>光學內視鏡 vs 虛擬內視鏡 (MDCT)：</b><br>
      光學內視鏡可以直接切片、看到真實色彩且無輻射，但無法精準測量病灶大小（MDCT可），且視野會受限（MDCT無限制）。
    </div>"""

hint3 = """    <div class="box exam">
      <strong>🎯 老師考訓一級必會點：</strong><br>
      <b>Plain film (KUB) 看不出的病變：</b><br>
      結腸炎、胃炎、肝腫瘤、肝膿瘍、脾破裂等軟組織病變，單靠 KUB 是一定看不出來的！
    </div>"""

content = content.replace("    <!-- QUIZ 113-52 -->", hint1 + "\n\n    <!-- QUIZ 113-52 -->")
content = content.replace("    <div class=\"box key\">", hint2 + "\n\n    <div class=\"box key\">")
content = content.replace("    <!-- QUIZ 111-64 -->", hint3 + "\n\n    <!-- QUIZ 111-64 -->")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modification done.")
