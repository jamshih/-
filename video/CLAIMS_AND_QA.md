# Team E｜影片宣稱、來源與驗證（2026-10-10）
**資料分類：** PUBLISHED ORGANIZER BRIEFING／PROJECT FROZEN DECISION／SIMULATED STORYBOARD／PROPOSED ARCHITECTURE／UNVERIFIED. 嚴格區分，不用未核實績效/合作說服評審。

| 內容/宣稱 | 狀態 | 來源與使用界線 |
| --- | --- | --- |
| 題目「不搭車，也打開 yoxi」；隊名「出門再說」、產品「yoxi 隨行」 | PROJECT FROZEN，平台正式企業欄名待核 | [README](../README.md)、[PRODUCT_BRIEF](../docs/PRODUCT_BRIEF.md)、[DECISIONS](../docs/DECISIONS.md)。 |
| 初賽 3 分鐘 Unlisted YouTube 影片＋≤15 頁簡報，影片名 `出題企業_作品名稱_2026 和泰 AI 黑客松`；10/14 13:00 台北提交 | **Team C 認證主辦校園簡報內容（非已登入平台）** | [C #4 source correction](https://github.com/jamshih/-/issues/4#issuecomment-6080393092)、[C at immutable SHA](https://github.com/jamshih/-/blob/b7aca6c7d9ac843485b3580869ff836761054d9d/research/verified-findings.md)、[原來源 PDF](https://drive.google.com/file/d/1y-0-Y5Ha6Qz3ujEGNwXkVUctpE0AFfF1/view)。平台最新格式/附件大小/IP/成功投稿 **UNVERIFIED**。 |
| 現有 yoxi 保留直接叫車、常用旅程 | Published feature, not our innovation | [yoxi official passenger tutorial](https://www.yoxi.app/passenger-tutorial) and C review. |
| 高雄巨蛋 18:30、捷運巨蛋站、雨勢/車資/ETA、通知 | **[模擬]** | Team B #3/PR #7，immutable `9a882e9c2ee82f11135c5587e90a1b21fa27233f`；**沒有**即時天氣/路況/行事曆、捷運/yoxi API/真實派車。18:30 是情境預計抵達，不是現場資料。 |
| 「通知成為同一對話的第一句」、交通卡、雨天偏好重排、確認 | PROPOSED product UX / scripted HTML + handdrawn SVGs | [B storyboard](https://github.com/jamshih/-/blob/9a882e9c2ee82f11135c5587e90a1b21fa27233f/prototype/STORYBOARD.md)；不可稱正式上線/實驗成功。 |
| 延誤改道、讀書去處 | PROPOSED two extra cases (not implemented screens) | B storyboard only; no fabricated UI captures. |
| 使用者授權→hard deny 通知規則→Jev 候選→LLM→可信工具→本人確認 | PROPOSED architecture, **Jev NOT TESTED** | [ARCHITECTURE](../docs/ARCHITECTURE.md) + [D #5](https://github.com/jamshih/-/issues/5)；Jev 應跟 deterministic baseline 做評估，沒有驗證準確率/成本。 |
| ETA、車資、路線/預報需由未來獲授權資料源提供 | UNVERIFIED integrations | C 的 API 授權／可行性調查。沒有 yoxi 官方 dispatch 權限／測試紀錄。 |
| 每週使用天數、非叫車互動、通知關閉率、搭乘轉換 | PROPOSED future KPIs; no improvement data | [PRODUCT_BRIEF](../docs/PRODUCT_BRIEF.md)。不用「提升 X%」。 |
| 吉祥物、商標 logo、Rive | Official assets rights **UNVERIFIED** | [C 品牌調查](https://github.com/jamshih/-/issues/3#issuecomment-6080253589)；影片只用原創/Team B 中性圖片，不複製官方 logo/吉祥物。 |
| 主講由**真人本人** | Owner editorial decision, not established official mandate | [M correction on #8](https://github.com/jamshih/-/issues/8#issuecomment-6094664958)；可片頭片尾露臉＋中段本人旁白。 |

## 靜態驗證通過
- [x] 讀核心 docs、HANDOFF_PROTOCOL、原 Team M V0.1 人類主講修正、C 官方簡報修正、B 4 個 SVG 原件與來源說明。
- [x] 提供完整第一人稱中文口白、七幕分鏡逐字覆蓋文字、字幕 SRT/純文字、真人製作操作指引。
- [x] 模擬標籤、可信資料與人為明確確認均進腳本/剪輯要求；原創 SVG 無授權 logo/吉祥物。
- [x] 計算 7 段靜態發聲字元及反推預估配時（**非真人測速**）；SRT 預排時間 **待真人波形人工對齊**。

## 尚未通過／由人類補證
- [ ] 真人試錄時間及配速、字幕音檔校對、圖像在影片編輯器真實輸出、影片可讀/可聽/ ≤03:00 **NOT VERIFIED**。
- [ ] Team D 後續可能提供新的評估方案（原腳本只說 Jev 尚未實測）；Team C/隊長核對正式企業名與權利。
- [ ] Team A 最終簡報說法與影片一致；Team M 審核後才公布。
- [ ] YouTube「不公開」影片上傳 URL、無痕視窗可看、官方投稿回執 **NOT DONE**。

## 本版編輯決策
1. 真人自己講解，開頭和結尾建議露臉；拒絕 AI 虛擬人口白。
2. 直接使用四幅已有原創 SVG（不是 browser captures），畫面常駐模擬聲明，沒有任何聲稱可派車的假鏡頭。
3. 不等 Team A 簡報、不擴增品牌 Rive/未授權角色；拍攝和剪輯可並行。
4. 應有可操作人機交接，但 AI 不自行製造 ETA/車資，Jev 必須先與簡單硬規則基線獨立對比。
