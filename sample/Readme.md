# 模块简介

这个模块主要是用来编写一些示范代码

## 一些基本使用

### fixtures使用 - 一些你需要在方法前，模块前，类加载前初始化的代码的写法，就像java junit里的 @Before 和 @After 注解，但是pytest更细

    <https://www.jianshu.com/p/c4690d9b3af9]>

    <http://www.cnblogs.com/fnng/p/4769020.html>

    pytest -v -s test_fixfures.py

    模块形式----使用setup_module/teardown_module  
    函数形式----使用setup_function/teardown_function
    类形式----使用setup_class/teardown_class
    方法形式---使用setup_method/teardown_method

    pytest -v -s test_fixfures.py::TestClass::test_class_function

### assert使用 - 可以直接使用assert断言，省去好多冗余的文字

    <http://www.cnblogs.com/fnng/p/4774676.html>

    pytest -v template/assert/test_assert:test_template_assert

    pytest -v template/assert/test_assert:test_template_assert1

### mock使用

    <https://www.jianshu.com/p/36128049fefc>

### 测试用例式种运行方式 - 可以运行目录下的所有python文件，也可以运行某个python文件，也可以运行python文件里的某个类以及里面的方法等

    <https://www.jianshu.com/p/60ef272911a5>

    <http://865325772.iteye.com/blog/2403763>

* 选择运行特定的某个类

    pytest -v template/startup/test_startup.py::TestClass

* 选择运行特定的某个测试用例, 适合一开始在调试单个测试用例的时候。

    pytest -v template/startup/test_startup.py::TestClass::test_case4

* 多种组合运行

    pytest -v template/startup/test_startup.py::test_case1 template/startup/test_startup.py::test_case2 template/startup/test_startup.py::TestClass::test_case4

* 用-k进行关键字匹配来运行测试用例名字子串

    pytest -v -k case1 template/startup/test_startup.py

    pytest -v -k case2 template/startup/test_startup.py

    pytest -v -k case3 template/startup/test_startup.py

* 用Marker运行

    pytest -v -k P0 template/startup/test_startup.py

    pytest -v -k P1 template/startup/test_startup.py

* 多进程运行case

    pip3 install -U pytest-xdist

    pytest -v template/startup/test_startup.py -n 3

* 重试运行cases

    pip3 install -U pytest-rerunfailures

    pytest -v -s template/startup/test_startup.py --reruns 2

### 一些常的http api测试方法

### allure美化 - 可以自定义输出自己想要的测试报告

    <https://blog.csdn.net/liuchunming033/article/details/79624474>

    1. pip3 install pytest-allure-adaptor