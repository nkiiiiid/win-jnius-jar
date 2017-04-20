import os
os.environ['CLASSPATH'] = ".\\javaclass.jar"

from jnius import autoclass
javaclass = autoclass('com.test.JavaClass')
print javaclass().javamet()
