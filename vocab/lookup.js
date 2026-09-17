/* nb-lookup — 反白英文 → Google 翻譯 → 加入 GitHub 單字表
 * 同一份程式同時用在筆記站（反白後浮出「譯」按鈕）和 Chrome 插件（右鍵選單觸發）。
 * 設定可由 window.NB_LOOKUP_CONFIG 覆寫（插件用它把 fetch / token 改走 background）。
 */
(function () {
  'use strict';
  if (window.__nbLookup) return;

  var CFG = Object.assign({
    repo: 'mnbvcxz850107/notes',
    branch: 'main',
    path: 'vocab/vocab.json',
    reviewUrl: 'https://mnbvcxz850107.github.io/notes/vocab/',
    trigger: 'selection',            // 'selection'：反白就出按鈕；'external'：等外部呼叫 open()
    fetchJson: defaultFetchJson,     // (url, opts) => Promise<{status, json}>
    getToken: function () { return Promise.resolve(safeGet('nbVocabToken') || ''); },
    setToken: function (t) { safeSet('nbVocabToken', t); return Promise.resolve(); }
  }, window.NB_LOOKUP_CONFIG || {});

  var TOKEN_HELP = 'https://github.com/settings/personal-access-tokens/new';

  /* ---------- 小工具 ---------- */
  function safeGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function safeSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function defaultFetchJson(url, opts) {
    return fetch(url, opts).then(function (r) {
      return r.text().then(function (t) {
        var j = null; try { j = JSON.parse(t); } catch (e) {}
        return { status: r.status, json: j };
      });
    });
  }
  function b64enc(s) { return btoa(unescape(encodeURIComponent(s))); }
  function b64dec(b) { return decodeURIComponent(escape(atob(b.replace(/\n/g, '')))); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 7); }
  function nowIso() { return new Date().toISOString(); }
  function norm(w) { return w.toLowerCase().replace(/[^a-z0-9' -]/g, '').trim(); }

  /* ---------- 翻譯 ---------- */
  function translate(text) {
    var q = encodeURIComponent(text);
    return CFG.fetchJson('https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-TW&dt=t&dt=bd&q=' + q)
      .then(function (r) {
        if (r.status !== 200 || !Array.isArray(r.json)) throw new Error('gtx ' + r.status);
        var j = r.json;
        var main = (j[0] || []).map(function (x) { return x[0] || ''; }).join('');
        var dict = (j[1] || []).map(function (e) { return { pos: e[0], terms: (e[1] || []).slice(0, 6) }; });
        return { translation: main, dict: dict };
      })
      .catch(function () {
        return CFG.fetchJson('https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=zh-TW&q=' + q)
          .then(function (r) {
            var t = Array.isArray(r.json) ? r.json[0] : '';
            if (t && typeof t === 'object') t = t.trans || '';
            if (!t) throw new Error('翻譯服務暫時無法使用');
            return { translation: String(t), dict: [] };
          });
      });
  }

  /* ---------- GitHub 單字表 ---------- */
  function api() { return 'https://api.github.com/repos/' + CFG.repo + '/contents/' + CFG.path; }
  function ghHeaders(token) {
    return { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' };
  }
  function ghGet(token) {
    return CFG.fetchJson(api() + '?ref=' + CFG.branch + '&t=' + Date.now(), { headers: ghHeaders(token), cache: 'no-store' })
      .then(function (r) {
        if (r.status === 404) return { sha: null, data: { version: 1, words: [] } };
        if (r.status === 401) throw new Error('Token 無效或過期');
        if (r.status === 403) throw new Error('Token 沒有這個 repo 的權限');
        if (r.status !== 200 || !r.json) throw new Error('讀取單字表失敗 (' + r.status + ')');
        var data;
        try { data = JSON.parse(b64dec(r.json.content)); } catch (e) { data = { version: 1, words: [] }; }
        if (!Array.isArray(data.words)) data.words = [];
        return { sha: r.json.sha, data: data };
      });
  }
  function ghPut(token, data, sha, message) {
    data.updated = nowIso();
    var body = { message: message, branch: CFG.branch, content: b64enc(JSON.stringify(data, null, 1)) };
    if (sha) body.sha = sha;
    return CFG.fetchJson(api(), { method: 'PUT', headers: Object.assign({ 'Content-Type': 'application/json' }, ghHeaders(token)), body: JSON.stringify(body) })
      .then(function (r) {
        if (r.status === 409 || r.status === 422) return { conflict: true };
        if (r.status === 401) throw new Error('Token 無效或過期');
        if (r.status !== 200 && r.status !== 201) throw new Error('寫入失敗 (' + r.status + ')');
        return { ok: true };
      });
  }
  function cacheWords(words) {
    safeSet('nbVocabCache', JSON.stringify(words.map(function (w) { return w.lower; })));
  }
  function cachedHas(lower) {
    try { return (JSON.parse(safeGet('nbVocabCache') || '[]')).indexOf(lower) >= 0; } catch (e) { return false; }
  }
  // 讀 → 併入 → 寫；遇到別台裝置同時寫入（sha 不符）就重讀再試
  function addWord(token, entry) {
    var attempt = 0;
    function run() {
      return ghGet(token).then(function (cur) {
        var words = cur.data.words;
        var hit = null;
        for (var i = 0; i < words.length; i++) if (words[i].lower === entry.lower) { hit = words[i]; break; }
        var msg;
        if (hit) {
          if (!hit.context && entry.context) hit.context = entry.context;
          if (!hit.url) { hit.url = entry.url; hit.title = entry.title; }
          hit.updated = nowIso();
          msg = 'vocab: touch ' + entry.word;
        } else {
          words.push(entry);
          msg = 'vocab: add ' + entry.word;
        }
        return ghPut(token, cur.data, cur.sha, msg).then(function (res) {
          if (res.conflict) {
            if (++attempt >= 3) throw new Error('單字表剛被其他裝置更新，請再按一次');
            return run();
          }
          cacheWords(words);
          return { existed: !!hit, count: words.length };
        });
      });
    }
    return run();
  }

  /* ---------- 選取 & 例句 ---------- */
  var host, root, pill, card;
  function currentSelection() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || !sel.rangeCount) return null;
    var text = sel.toString().replace(/\s+/g, ' ').trim();
    if (!text || text.length > 120 || !/[A-Za-z]/.test(text)) return null;
    var a = sel.anchorNode;
    if (host && (a === host || host.contains(a))) return null;
    var el = a && (a.nodeType === 1 ? a : a.parentElement);
    if (el && el.closest && el.closest('input,textarea,[contenteditable="true"]')) return null;
    var range = sel.getRangeAt(0);
    return { text: text, rect: range.getBoundingClientRect(), range: range };
  }
  function contextSentence(range, text) {
    if (!range) return '';
    var n = range.startContainer;
    var el = n.nodeType === 1 ? n : n.parentElement;
    var block = el && el.closest && el.closest('p,li,dd,dt,td,th,blockquote,h1,h2,h3,h4,h5,h6,figcaption,summary,label');
    var full = ((block || el || {}).textContent || '').replace(/\s+/g, ' ').trim();
    if (!full) return '';
    var idx = full.indexOf(text);
    if (idx < 0) return full.slice(0, 200);
    var start = idx, end = idx + text.length;
    while (start > 0 && !/[.!?。！？；;]/.test(full[start - 1])) start--;
    while (end < full.length && !/[.!?。！？；;]/.test(full[end])) end++;
    if (end < full.length) end++;
    var s = full.slice(start, end).trim();
    if (s.length > 260) {
      var lo = Math.max(start, idx - 120), hi = Math.min(end, idx + text.length + 120);
      s = (lo > start ? '…' : '') + full.slice(lo, hi).trim() + (hi < end ? '…' : '');
    }
    return s;
  }

  /* ---------- UI ---------- */
  var CSS = '\
:host{all:initial}\
*{box-sizing:border-box}\
.pill,.card{position:fixed;z-index:2147483646;font-family:"Noto Sans TC","PingFang TC","Helvetica Neue",system-ui,sans-serif;color:#e8ecf3;-webkit-font-smoothing:antialiased}\
.pill{display:flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:999px;background:#141922;border:1.5px solid #e5b567;color:#e5b567;font-size:17px;font-weight:700;box-shadow:0 6px 20px rgba(0,0,0,.45);cursor:pointer;user-select:none;-webkit-user-select:none;touch-action:manipulation}\
.pill:active{transform:scale(.95)}\
.pill[hidden]{display:none!important}\
.card{width:min(380px,calc(100vw - 20px));max-height:min(70vh,560px);overflow:auto;background:#141922;border:1px solid #2a3340;border-radius:14px;box-shadow:0 14px 40px rgba(0,0,0,.55);padding:14px 16px 12px;font-size:15px;line-height:1.6;overscroll-behavior:contain}\
.hd{display:flex;align-items:flex-start;gap:10px}\
.word{flex:1;font-size:22px;font-weight:700;color:#6fd3c7;word-break:break-word;line-height:1.3}\
.x{flex:none;width:32px;height:32px;border:0;background:transparent;color:#a3adbd;font-size:22px;line-height:1;cursor:pointer;border-radius:8px;margin:-4px -8px 0 0}\
.x:hover{background:#1b2230}\
.tr{font-size:19px;font-weight:500;margin:6px 0 2px;min-height:1.4em;word-break:break-word}\
.tr.dim{color:#a3adbd;font-size:15px;font-weight:300}\
.dict{margin:2px 0 0;padding:0;list-style:none;font-size:13.5px;color:#a3adbd}\
.dict li{margin:1px 0}.dict b{color:#e5b567;font-weight:500;margin-right:6px}\
.ctx{margin:10px 0 0;padding:8px 10px;background:#0b0e13;border-left:2px solid #2a3340;border-radius:0 8px 8px 0;font-size:13.5px;color:#a3adbd;line-height:1.55}\
.ctx mark{background:transparent;color:#e5b567;font-weight:600}\
.ctxzh{margin-top:6px;color:#e8ecf3;font-weight:300}\
.link{background:none;border:0;padding:0;color:#6fd3c7;font-size:13px;cursor:pointer;text-decoration:underline;text-underline-offset:3px}\
.row{display:flex;gap:8px;align-items:center;margin-top:12px;flex-wrap:wrap}\
.btn{flex:1;min-width:140px;height:42px;border-radius:10px;border:1px solid #e5b567;background:#e5b567;color:#0b0e13;font-size:15px;font-weight:700;cursor:pointer;touch-action:manipulation}\
.btn:disabled{opacity:.55;cursor:default}\
.btn.done{background:#1b2230;color:#6fd3c7;border-color:#2a3340}\
.ghost{flex:none;height:42px;padding:0 14px;border-radius:10px;border:1px solid #2a3340;background:transparent;color:#a3adbd;font-size:14px;text-decoration:none;display:inline-flex;align-items:center;cursor:pointer}\
.st{margin-top:8px;font-size:12.5px;color:#a3adbd;min-height:1.2em}\
.st.err{color:#e88b8b}\
.tok{margin-top:10px;padding:10px;border:1px dashed #2a3340;border-radius:10px;font-size:13px;color:#a3adbd}\
.tok input{width:100%;margin:6px 0;height:38px;padding:0 10px;border-radius:8px;border:1px solid #2a3340;background:#0b0e13;color:#e8ecf3;font-size:14px}\
.tok a{color:#6fd3c7}\
.tok .btn{height:36px;font-size:14px}\
@media (prefers-color-scheme:light){.card,.pill{background:#fff;color:#1a222c;border-color:#d9dee6}.pill{color:#b8862e;border-color:#b8862e}.word{color:#1f8f83}.x,.dict,.ctx,.st,.tok,.ghost{color:#5b6674}.ctx{background:#f3f5f8;border-left-color:#d9dee6}.ctxzh{color:#1a222c}.x:hover{background:#eef1f5}.btn.done{background:#eef1f5;color:#1f8f83;border-color:#d9dee6}.tok input{background:#fff;color:#1a222c;border-color:#d9dee6}}';

  function ensureHost() {
    if (host) return;
    host = document.createElement('div');
    host.id = 'nb-lookup-host';
    host.style.cssText = 'all:initial;position:fixed;top:0;left:0;width:0;height:0;z-index:2147483646';
    root = host.attachShadow ? host.attachShadow({ mode: 'open' }) : host;
    var st = document.createElement('style'); st.textContent = CSS; root.appendChild(st);
    pill = document.createElement('button'); pill.className = 'pill'; pill.textContent = '譯'; pill.hidden = true;
    pill.setAttribute('aria-label', '翻譯選取的文字');
    root.appendChild(pill);
    (document.body || document.documentElement).appendChild(host);

    var pending = null;
    pill.addEventListener('pointerdown', function (e) { e.preventDefault(); e.stopPropagation(); });
    pill.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      if (pending) open(pending.text, pending.context, pending.rect, pending.url);
      hidePill();
    });
    pill.showFor = function (s) {
      pending = { text: s.text, context: contextSentence(s.range, s.text), rect: s.rect, url: location.href };
      place(pill, s.rect, 40, 40, 8);
      pill.hidden = false;
    };
  }
  function hidePill() { if (pill) pill.hidden = true; }
  function place(el, rect, w, h, gap) {
    var vw = window.innerWidth, vh = window.innerHeight;
    var left = Math.min(Math.max(8, rect.left), vw - w - 8);
    var top = rect.bottom + gap;
    if (top + h > vh - 8) top = Math.max(8, rect.top - h - gap);
    el.style.left = left + 'px'; el.style.top = top + 'px';
  }
  function closeCard() { if (card) { card.remove(); card = null; } }

  function open(text, context, rect, url) {
    ensureHost(); closeCard(); hidePill();
    text = (text || '').replace(/\s+/g, ' ').trim();
    if (!text) return;
    var entry = {
      id: uid(), word: text, lower: norm(text), translation: '', dict: [],
      context: context || '', contextZh: '', url: url || location.href, title: document.title || '',
      added: nowIso(), updated: nowIso(), box: 0, due: nowIso(), seen: 0, correct: 0
    };
    card = document.createElement('div'); card.className = 'card'; card.setAttribute('role', 'dialog');
    var ctxHtml = entry.context ? esc(entry.context).replace(new RegExp(esc(text).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i'), function (m) { return '<mark>' + m + '</mark>'; }) : '';
    card.innerHTML =
      '<div class="hd"><div class="word">' + esc(text) + '</div><button class="x" aria-label="關閉">×</button></div>' +
      '<div class="tr dim">翻譯中…</div><ul class="dict"></ul>' +
      (ctxHtml ? '<div class="ctx"><div class="ctxen">' + ctxHtml + '</div><div class="ctxzh" hidden></div><button class="link zh">整句翻譯</button></div>' : '') +
      '<div class="row"><button class="btn add" disabled>＋ 加入單字表</button><a class="ghost" href="' + esc(CFG.reviewUrl) + '" target="_blank" rel="noopener">單字表 ↗</a></div>' +
      '<div class="tokbox"></div><div class="st"></div>';
    root.appendChild(card);
    var w = Math.min(380, window.innerWidth - 20);
    var anchor = rect || { left: (window.innerWidth - w) / 2, top: window.innerHeight * 0.3, bottom: window.innerHeight * 0.3 };
    // 先放在選取文字下方；放不下就放上方；再不行就往上推到看得見為止（高度會隨翻譯載入而變，所以每次更新後重算）
    function fit() {
      var h = card.offsetHeight, vh = window.innerHeight;
      place(card, anchor, w, h, 10);
      var top = parseFloat(card.style.top);
      if (top + h > vh - 8) card.style.top = Math.max(8, vh - 8 - h) + 'px';
    }
    fit();

    var $ = function (s) { return card.querySelector(s); };
    var stEl = $('.st'), addBtn = $('.add'), trEl = $('.tr');
    function status(msg, err) { stEl.textContent = msg || ''; stEl.className = 'st' + (err ? ' err' : ''); fit(); }

    $('.x').addEventListener('click', closeCard);
    card.addEventListener('pointerdown', function (e) { e.stopPropagation(); });

    if (cachedHas(entry.lower)) { addBtn.textContent = '✓ 已在單字表'; addBtn.classList.add('done'); }

    translate(text).then(function (t) {
      entry.translation = t.translation; entry.dict = t.dict;
      trEl.textContent = t.translation; trEl.classList.remove('dim');
      $('.dict').innerHTML = t.dict.map(function (d) { return '<li><b>' + esc(d.pos) + '</b>' + esc(d.terms.join('、')) + '</li>'; }).join('');
      addBtn.disabled = false; fit();
    }).catch(function (e) {
      trEl.textContent = '翻譯失敗'; trEl.classList.remove('dim');
      status(e.message || String(e), true); addBtn.disabled = false;
    });

    var zhBtn = $('.zh');
    if (zhBtn) zhBtn.addEventListener('click', function () {
      zhBtn.disabled = true; zhBtn.textContent = '翻譯中…';
      translate(entry.context).then(function (t) {
        entry.contextZh = t.translation;
        var z = $('.ctxzh'); z.textContent = t.translation; z.hidden = false; zhBtn.remove(); fit();
      }).catch(function () { zhBtn.disabled = false; zhBtn.textContent = '整句翻譯'; });
    });

    function askToken() {
      var box = $('.tokbox');
      box.innerHTML = '<div class="tok">第一次使用：貼上 GitHub Token（只會存在這個瀏覽器）<br>' +
        '<a href="' + TOKEN_HELP + '" target="_blank" rel="noopener">產生 Fine-grained token ↗</a>：Repository access 只選 <b>notes</b>，Permissions 勾 <b>Contents: Read and write</b>' +
        '<input type="password" placeholder="github_pat_…" autocomplete="off"><button class="btn save">儲存並加入</button></div>';
      var inp = box.querySelector('input');
      box.querySelector('.save').addEventListener('click', function () {
        var t = inp.value.trim(); if (!t) { inp.focus(); return; }
        CFG.setToken(t).then(function () { box.innerHTML = ''; doAdd(); });
      });
      fit(); inp.focus();
    }
    function doAdd() {
      CFG.getToken().then(function (token) {
        if (!token) { askToken(); return; }
        addBtn.disabled = true; addBtn.textContent = '儲存中…'; status('');
        return addWord(token, entry).then(function (r) {
          addBtn.textContent = r.existed ? '✓ 已在單字表' : '✓ 已加入'; addBtn.classList.add('done');
          status('單字表共 ' + r.count + ' 個字');
        }).catch(function (e) {
          addBtn.disabled = false; addBtn.textContent = '＋ 加入單字表';
          status(e.message || String(e), true);
          if (/Token/.test(e.message || '')) { CFG.setToken(''); askToken(); }
        });
      });
    }
    addBtn.addEventListener('click', function () { if (!addBtn.classList.contains('done')) doAdd(); });
  }

  /* ---------- 觸發 ---------- */
  if (CFG.trigger === 'selection') {
    var timer = null;
    function check() {
      ensureHost();
      var s = currentSelection();
      if (s) pill.showFor(s); else hidePill();
    }
    function schedule(ms) { clearTimeout(timer); timer = setTimeout(check, ms); }
    document.addEventListener('selectionchange', function () { schedule(350); });
    document.addEventListener('mouseup', function () { schedule(60); });
    document.addEventListener('touchend', function () { schedule(400); }, { passive: true });
    document.addEventListener('keyup', function (e) { if (e.shiftKey || e.key === 'Shift') schedule(60); });
    window.addEventListener('scroll', function () { hidePill(); }, { passive: true });
  }
  document.addEventListener('pointerdown', function (e) {
    if (!card) return;
    var p = e.composedPath ? e.composedPath() : [];
    if (p.indexOf(card) < 0) closeCard();
  }, true);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeCard(); hidePill(); } });

  window.__nbLookup = {
    open: function (text) {
      var s = currentSelection();
      open(text || (s && s.text), s ? contextSentence(s.range, s.text) : '', s ? s.rect : null, location.href);
    },
    close: closeCard,
    config: CFG,
    _translate: translate, _ghGet: ghGet, _addWord: addWord   // 測試用
  };
})();
