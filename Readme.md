## 项目依赖
python3.4 +

## 安装依赖
pip3 install -U pytest

pip3 install -U requests

pip3 install -U allure-pytest

### 打印所需模块
pip3 install termcolor

<!-- 经测试，不要使用以下插件 -->
<!-- pip3 install -U pytest-allure-adaptor -->

## 卸载依赖

pip3 uninstall pytest

pip3 uninstall requests

pip3 uninstall allure-pytest

pip3 uninstall termcolor

<!-- 经测试，不要使用以下插件 -->
<!-- pip3 uninstall pytest-allure-adaptor -->

## 目录结构
root

    - config - 系统级别配置文件存放目录
    - sample - 示例代码
        - allure - 自定义测试报告输出示例
        - assert - 断言示例
        - dubbosample - dubbo调用示例
        - fixtures - fixtures特性介绍示例
        - httpsample - http相关用法
        - mock - 高级特性示例
        - startup - 其它
    - test - 所有测试文件均在此处添加
        - tob_audit - 各项目测试文件，均需建一个自己项目的包，然后在包中添加测试用例
    - util - 工具类存放目录
    - common - 公共工具
        - dubbo - dubbo相关工具

## 基础框架更新摘要
### 2018-11-27
完成项目第一版本的提交：
1. api接口测试
2. dubbo接口测试


## 附：
pytest入门 https://www.jianshu.com/p/c5037bed334a

从0学习python https://blog.csdn.net/u011541946/article/details/62045846

request说明书 http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

allure自定义说明 https://www.cnblogs.com/xiaoxi-3-/p/9492534.html