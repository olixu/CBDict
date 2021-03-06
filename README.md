# ClipBoardDictionary
This program monitors the clipboard of the system and translate the word from English to Chinese by YouDao api, especially designed for Students who are working under linux environment where there is no simple translater when you reading papers.

# 项目起源
本人即将成为一名Ph.D，现在在看一些关于强化学习，深度学习，机器学习，控制理论等方面的英文文献，经常会有一些单词不认识．

虽然市面上很多优秀的翻译软件都已经集成了屏幕取词的功能，例如有道词典．但是由于我操作系统或者驱动等一些问题（本人的开发环境为Manjaro），安装了有道词典之后，我无法使用屏幕取词功能，每次都需要复制到网页中查询．

每次切换到浏览器再切换回pdf阅读器，十分影响阅读体验．因此，我写了这么一个小玩具，能够监控剪贴板中的内容，并且自动使用有道词典的api来进行翻译．将结果输出到终端中．

本玩具纯粹是为了方便我读paper．不喜勿喷．

# 使用教程
STEP1 : 安装依赖的包，用于访问剪贴板中的内容
```shell
sudo apt install xclip
```

STEP2 : 在终端中输入以下命令来安装CBDict
```python
pip install CBDict
```

STEP3 : 在终端中输入`CBDict`来启动词典
```shell
CBDict
```

STEP4 : 复制任何你想翻译的内容，翻译的结果会呈现在终端中．

# 更新日志
VERSION 1.0
 - 格式化打印翻译结果

![demo](demo.gif)

VERSION 2.0
 - 通过弹窗的方式将翻译的结果输出到桌面，免去切换到终端的过程

![demo](demo1.gif)