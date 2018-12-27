Python 入門與 Matplotlib 繪圖入門  
# 第一部份：Python簡介
* 高階程式語言
* 設計哲學：可讀性與簡潔的語法  
* 直譯式語言 （interpreted language）  
	* -> 說一句做一件事 -> 互動模式讓你快速測試與除錯👍🏻  
	* <->編譯語言（ Compiled language ）需要先將腳本（Script）完整編譯成機器語言後再執行，較有效率（如 C, Fortran等）  
* 動態型別，使用方便。（初始化時不需指定型別）  
* 兼容並蓄，擴充性強。（可用不同語言撰寫套件給Python用）  
* 使用：科學運算、GIS系統、網路爬蟲等等  

## Anaconda：Python 發行版
![Anaconda Picture](./img/Anaconda.png)

* 為了科學運算特別包裝的套裝發行版。
* 已經預先安裝許多科學運算用的套件。
* 有專屬的 IDE: **Spyder** 方便快速Coding。
![Spyder app](./img/Spyder.png)
* CONDA：Python 的套件管理工具，方便安裝各類套件。
	* 安裝： ```conda install --channel conda-forge boltons```
	* 更新套件：```conda update scipy```
	* 更新conda：```conda update conda```
	* 其他應用請參考：[Conda官網](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)

***

## 型別介紹：
* 文字 String  ```a=apple```
* 整數 integer ```b=1```
* 浮點數 float ```c=3.14```
* 清單 list    ```d=[]```
* 元組 tuple   ```e=()```


### 替變數命名限制：
* 不可以和保留字重複（語法相關）
* 不可以用數字開頭
* 不可以含有空格

Let's try！  
創造一個「List」，名為 「bag」，裡面放一個「apple」

來看看包包有什麼：
```print(bag)```

很好！讓我們在包包加入一些東西！
## 物件的方法  
* 所有建立的物件都是 Python Object，Python會自動分辨其型別。  
* 方法：每格型別有特別的「方法」（Method）可以呼叫，用「.」的方式標於物件後，用以傳回特定值或有特別操作。  
比如說： ``` list.append( x )```  
就會在「list」裡面加入「x」。  
**請在包包裡加入「banana」與「lemon」**
[參考資料](https://docs.python.org/3.6/tutorial/datastructures.html)

***

## 容器類索引  

* 容器類包含：List、Tuple、Dictionary 等。
* 取用容器內容（元素elements）時，可以使用「索引」（index）將其取出。
* 索引夾在中括號中，置於容器型別後面。  
* 注意：第一個內容索引從 「0」 開始。  
* 舉例： 購物清單中第二個內容是什麼？```print( bag[1] )```
* 若要取一段，可以用「:」來取出，如：
```n = [1,2,3,4,5]print( n[1:3] )```

***

## 文字的方法
* 初始化文字：使用單引號「’’」、雙引號「””」將文字括住。  
* 長字串或長註解（包含換行）使用前後各使用三個引號括住。  

```”””. . .  註解. . .  ”””```
### 格式化文字方法： format方法  
``` [[fill]align][sign][#][0][width][grouping_option][.precision][type]```  
請你試試：  
```”購物車第一項是 {0}，第二項是 {1}”.format( bag[0],bag[1] )```  

```”3.1415取到第二位是{:.3}”.format(3.1415)```

[更詳細的說明可以點這邊](https://docs.python.org/3.6/library/string.html#format-string-syntax)

***

##for 迴圈

* 對一陣列內物件做相同處理時非常好用。
* 語法：  
```
for element in container:  
    do something
```
* **element** 在每一次的循環中，都會被帶換成 container 內的物件。  
舉例：  
```
for item in bag:  
    print( item )
```  
另一種寫法：  
```for i in range( len( bag ) ):
    print( bag[i] )
```

	* range( x ) ：產生 0 到 x-1 的（清單）
	* len( x ) ：傳回容器的長度。


***

## 撰寫與呼叫函式（Function）

* 函式是預先定義好的一些操作，Python 3.6 內建68種函式可以使用，如 print() 。
* 有些和資料型別相同的內建函式可幫我們轉換型別。
* 呼叫函式時，請直接打上函式的名字，並將引數置於小括號內。```print(“Hello world”)```  
* 定義一個自己的函式：使用「def」關鍵字。請看下面範例：

```
def avg(a,b):
    c = (a+b)/2
    return c
```
這邊解釋一下上面的語法：  

* def ：跟直譯器說我要開始定義新的函式了！
* avg ：函式的名字，跟變數一樣的命名限制。
* (a,b)：這格函式要接受幾格變數，並幫他們取小名「a」與「b」。
* 「:」：表示本行宣告結束，下面是函式的內容。
* **冒號後面代表要換下一階**，Python有個很嚴格的要求，就是「**階級分明**」！每個階級前面一定要有「**四個空格**」或「**一個tab**」。這邊將使用四個空格的撰寫習慣。
* c = (a+b)/2：將變數**c**指派為**(a+b)/2**的結果
	* Python 會先乘除後加減，()可以提高計算優先度
	* 補充：命名空間（Namespace）:程式在搜尋你指定的變數名稱時，會由內而外搜尋變數名稱。
		* 區域變數：定義在函式內部的變數，外部無法取用的參數。
		* 全域變數：定義在根層的變數，基本上在全部的位置都可以取用或更改。若要在函式裡面使用全域變數，需要加關鍵字 ```global```。  
* return：指定函式的回傳值。

函式定義好了以後，並不會自己執行！所以我們要呼叫函式：  
```
avg(2,8)
```  
若我們想要把結果指派給一個變數，可以這樣做：  
```
c = avg(2,8)
```
請你試試看！

***

## 引入函式庫

* 將一些函式打包給其他的腳本使用。多數的Python函式庫由Python寫成，使用其他語言的要經過特殊的編譯。（如Cyhton）
* 使用「```import```」關鍵字。  
* 在相同的工作資料夾下，不用打「.py」。比如要引入「lib.py」的檔案，則輸入：  ```import lib```
	* 引入 lib.py 後，我們變可以呼叫裡面的函式及其他物件。
	* 比如筆記本外面的資料夾有個 lib.py，裡面有個變數叫做「**version**」，有個函式叫做**now()**，讓我們呼叫看看:  
	```lib.version```  
	```lib.now()```  

* 使用conda安裝的套件：直接 import 函式庫名：  
```import numpy```
