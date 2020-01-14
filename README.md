## 自动化越权检测 PVD-HACK

### 强依赖：
* burpsuite -> Proxy -> HTTP history -> Save items  
* 注意不要勾选：base64-encode requests and responses

### 参数说明：
* -w 差异确定字符  
* -f xml文件

### 实现说明：
* GET请求：  
* 原始：http://hack.mimaz.com/index.php?id=2&pid=3&hack=qwer  
* 修改：  
1.http://hack.mimaz.com/index.php?id=1&pid=3&hack=qwer  
2.http://hack.mimaz.com/index.php?id=2&pid=2&hack=qwer  
请求四次：  
两次带着header  两次不带着header

* POST请求:   
* 原始date：id=2&asdp=1&qwe=gfd    
* 修改：  
1.id=1&asdp=1&qwe=gfd  
2.id=2&asdp=0&qwe=gfd  
请求四次：  
两次带着header  两次不带着header

### 特别的：
* 1.支持POST请求的JSON。  
* 2.不支持异常编码的xml文档  
* 3.还会继续修BUG
* 4.这是第一版，后续会陆续增加识别率。