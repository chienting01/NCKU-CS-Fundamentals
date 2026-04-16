# Python Roadmap

## 計畫定位

這份 Python 學習路線的目標，不是只停留在語法練習，而是希望在短期內建立：

1. Python 基礎語法能力
2. 資料處理前置能力
3. NumPy / Pandas 入門能力
4. Kaggle 實作前的準備能力

因此，這份 roadmap 的設計邏輯不是單純把語法列一遍，而是以「之後要做資料分析與 Kaggle」為目標，去安排學習順序。

---

## 學習原則

### 1. 先學 Python 本體，再進資料分析工具
如果連變數、條件、迴圈、函數都不熟，就直接進 Pandas 或 Kaggle，通常只會變成抄程式，不會真正理解。

### 2. 每週都要有可執行的 `.py` 檔
不是只寫筆記，也不是只看教學。  
每一週都要留下可以執行的 Python 程式。

### 3. 每個實作資料夾都要有 `README.md`
這樣之後回來看時，才知道這個範例原本在練什麼、怎麼執行、重點是什麼。

### 4. 每個主要主題都要配一份中文 Markdown 筆記
筆記不是裝飾，而是用來沉澱概念、補充理解與記錄常見錯誤。

### 5. 目標是能進 Kaggle，不是只會背語法
所以這份路線會逐步引導到：

- 檔案處理
- CSV 讀取
- NumPy
- Pandas
- Kaggle 資料結構理解

---

## 結構說明

### `notes/`
放理論筆記與概念整理。

### `basics/`
放單一知識點的小範例，每個主題都要有：

- `main.py` 或主程式檔
- `README.md`

### `scripts/`
放較整合型腳本，例如 NumPy、Pandas 的練習。

### `exercises/`
放練習題、解法、錯誤紀錄與重做紀錄。

---

## 四週壓縮版學習路線

# 第 1 週：Python 基礎合併週

## 主題
- Python 是什麼
- 開發環境建立
- `print()`
- `input()`
- 註解
- 變數
- 基本資料型態
  - `int`
  - `float`
  - `str`
  - `bool`
- 算術運算子
- 比較運算子
- 邏輯運算子
- 指派運算子
- `if / elif / else`
- `for`
- `while`
- `break`
- `continue`

## 本週目標
- 能建立並執行 `.py` 檔
- 能輸入資料並印出結果
- 能做簡單數值計算
- 能寫條件判斷
- 能寫基本迴圈
- 盡可能多做基礎練習

## 建議練習
- Hello World
- 自我介紹程式
- 輸入姓名與年齡並輸出結果
- 攝氏轉華氏
- 加減乘除計算器
- 成績等第判斷
- 奇偶數判斷
- 1 到 100 加總
- 九九乘法表

## 建議輸出
- `07_python/basics/01-hello/hello.py`
- `07_python/basics/01-hello/README.md`
- `07_python/basics/02-variables/main.py`
- `07_python/basics/02-variables/README.md`
- `07_python/basics/03-operators/main.py`
- `07_python/basics/03-operators/README.md`
- `07_python/basics/04-conditionals/main.py`
- `07_python/basics/04-conditionals/README.md`
- `07_python/basics/05-loops/main.py`
- `07_python/basics/05-loops/README.md`
- `07_python/notes/01-python-basics-and-flow-control.md`

---

# 第 2 週：函數、模組、Python 容器型別

## 主題
- 函數 `def`
- 參數
- 回傳值 `return`
- 區域變數
- 模組 `import`
- `math`
- `random`
- List
- Tuple
- Dictionary
- Set
- 索引與切片
- 基本字串處理

## 本週目標
- 把重複邏輯包成函數
- 呼叫自己寫的函數
- 匯入模組使用工具
- 使用 list / dict / set / tuple 儲存資料

## 建議練習
- 寫一個加法函數
- 寫一個成績平均函數
- 用 `random` 做抽號器
- 用 `math` 算圓面積與平方根
- 用 list 做待辦清單
- 用 dict 做簡單通訊錄
- 用 set 去除重複資料

## 建議輸出
- `07_python/basics/06-functions/main.py`
- `07_python/basics/06-functions/README.md`
- `07_python/basics/07-modules/main.py`
- `07_python/basics/07-modules/README.md`
- `07_python/basics/08-lists/main.py`
- `07_python/basics/08-lists/README.md`
- `07_python/basics/09-dictionaries/main.py`
- `07_python/basics/09-dictionaries/README.md`
- `07_python/basics/10-sets-and-tuples/main.py`
- `07_python/basics/10-sets-and-tuples/README.md`
- `07_python/notes/02-functions-and-python-containers.md`

---

# 第 3 週：檔案與路徑處理、例外處理、NumPy 入門

## 主題
- `open()`
- 基本讀檔概念
- 相對路徑與絕對路徑
- 為什麼程式找不到檔案
- `try / except`
- 常見錯誤類型
  - `ValueError`
  - `TypeError`
  - `IndexError`
  - `KeyError`
- NumPy 是什麼
- `array`
- 一維 / 二維陣列
- 陣列屬性
- 索引與切片
- 陣列基本運算
- 平均值、最大值、最小值

## 本週目標
- 能處理基本輸入錯誤
- 能理解路徑錯誤的原因
- 能讀取簡單檔案
- 能分辨 list 和 NumPy array
- 能用 NumPy 做簡單數值處理

## 建議練習
- 寫一個含錯誤處理的輸入程式
- 讀取一個簡單文字檔
- 練習相對路徑
- 建立一維、二維 NumPy 陣列
- 做陣列加減乘除
- 計算平均值與總和

## 建議輸出
- `07_python/basics/11-exception-handling/main.py`
- `07_python/basics/11-exception-handling/README.md`
- `07_python/basics/12-file-handling/main.py`
- `07_python/basics/12-file-handling/README.md`
- `07_python/scripts/numpy-basics.py`
- `07_python/notes/03-file-handling-exceptions-and-numpy.md`

---

# 第 4 週：Pandas 入門 + Kaggle 前置準備

## 主題
- Pandas 是什麼
- `Series`
- `DataFrame`
- 建立 DataFrame
- 讀取 CSV
- `head()`
- `info()`
- `describe()`
- 欄位選取
- 列篩選
- 排序
- 基本缺失值概念
- Kaggle 資料集基本結構
  - `train.csv`
  - `test.csv`
  - `submission.csv`

## 本週目標
- 能讀取一份 CSV
- 能理解表格資料的基本結構
- 能做基本篩選與排序
- 知道 Kaggle 入門資料通常怎麼開始看

## 建議練習
- 讀取一份成績 CSV
- 看欄位型態與資料筆數
- 篩出分數大於 80 的資料
- 根據某欄排序
- 計算某欄平均值
- 觀察空值狀況

## 建議輸出
- `07_python/scripts/pandas-basics.py`
- `07_python/notes/04-pandas-basics.md`
- `07_python/notes/05-kaggle-preparation.md`

---

## 四週後的合理程度

完成四週後，合理目標應該是：

- 能看懂大部分基礎 Python 程式
- 能自己寫小型工具程式
- 能使用函數、條件、迴圈、容器、例外處理
- 能處理基本檔案與路徑問題
- 能用 NumPy 做基本數值運算
- 能用 Pandas 讀取與處理簡單表格
- 能理解 Kaggle 入門競賽的資料結構

這時候才適合進入 Kaggle 正式實作。