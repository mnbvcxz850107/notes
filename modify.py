import sys

file_path = '/Users/furyan/.gemini/antigravity/scratch/notes/block7/small-bowel-disease.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

hint1 = """
    <div class="box exam">
        <strong>🎯 老師考訓一級必會點：</strong><br>
        梅克爾憩室是卵黃管未完全閉合所致，屬於<b>真性憩室 (True diverticulum)</b>，包含腸壁全層構造，這是必考陷阱！它的 Rule of 2s：是胃腸道最常見先天異常，男女比為 2:1，距離迴盲瓣 2 英呎，長 2 英吋，而且成人大多沒有症狀。
    </div>"""

hint2 = """
    <div class="box exam">
        <strong>🎯 老師考訓一級必會點：</strong><br>
        GIST 最常見的突變點位為 <b>KIT gene exon 11</b>。次要的突變點位則為 KIT exon 9 以及 PDGFRA exon 18/12，務必熟記。
    </div>"""

target1 = "這就是為什麼年輕人如果出現無痛性的大量血便，一定要懷疑它。</p>"
content = content.replace(target1, target1 + "\n" + hint1)

target2 = "<li><strong>治療：</strong>除了手術切除，標靶藥物 <strong>Imatinib (Gleevec)</strong> 對晚期 GIST 有奇效。</li>\n    </ul>"
content = content.replace(target2, target2 + "\n" + hint2)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Modified.")
