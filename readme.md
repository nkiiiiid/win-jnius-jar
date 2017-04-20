---
windows安装jnius和jnius调用jar
---

![](https://img.shields.io/travis/rust-lang/rust.svg) ![](https://img.shields.io/badge/python-2.7-brightgreen.svg) ![](https://img.shields.io/badge/cython-0.23-brightgreen.svg) ![](https://img.shields.io/badge/pyjnius-%2F%3D%20__%20%3D%2F-orange.svg) ![](https://img.shields.io/badge/jnius-%2F%3D%20__%20%3D%2F-orange.svg) ![](https://img.shields.io/badge/powered%20by-海森堡不确定面包-brightgreen.svg) 

 
### 0x01 Windows安装jnius

#### 安装cython

这里我使用0.23的cython是因为根据kivy版本确定的，我的kivy是191，当然如果你没有使用kivy就不需要关心cython的版本问题。

    pip install cython==0.23
 
#### 安装pyjnius和jnius

    pip install pyjnius
    pip install jnius

#### 安装jdk并设置环境变量

我把jdk安装在D:\Program Files (x86)\java

设置JAVA_HOME=D:\Program Files (x86)\java

JDK_HOME=D:\Program Files (x86)\java

#### Path追加jdk的jre的jvm.dll所在目录，%JDK_HOME%\jre\bin\server

然后在Python中运行import jnius会提示Could not reserve enough space for 716800KB object heap，这里还要增加一个环境变量，_JAVA_OPTIONS=-Xmx512M

现在就可以正常使用jnius了。


### 0x02 jnius调用jar

下面代码保存到jnius-jar\com\test\JavaClass.java

```java
//JavaClass.java
package com.test;
public class JavaClass{
    public String javamet(){
        return "from java world!";
    }
}
```

#### 生成class

    javac JavaClass.java

#### 生成jar，切换到jnius-jar目录

    jar -cvf javaclass.jar com

这样就可以在jnius-jar目录下看到javaclass.jar

#### 在jnius-jar目录下使用下面的代码调用jar

```python
import os
os.environ['CLASSPATH'] = ".\\javaclass.jar"

from jnius import autoclass
javaclass = autoclass('com.test.JavaClass')
print javaclass().javamet()
```

因为在java调用jar里本来也是要设置classpath，这里如法炮制。

例子已经上传到本repo，欢迎大家测试和反馈问题，如果你觉得我写的好的话，记得star哦（´∀｀*)  

