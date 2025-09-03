**该插件由两个主要部分组成：**
1. TypeScript 插件 (src/extension.ts):
* 注册一个命令，该命令会作为按钮显示在 Python 文件的编辑器标题栏。
* 读取当前活动 Python 文件的内容。
* 启动一个 Python 子进程来执行审查脚本。
* 通过 stdin/stdout (标准输入/输出) 处理与 Python 脚本的通信。
* 在 VSCode 的输出面板中显示结果。

2. Python 审查脚本 (review_script.py):
* 通过 stdin (标准输入) 接收 Python 代码。
* 将代码写入一个临时文件。
* 对该临时文件运行 pylint。
* 通过 stdout (标准输出) 返回 pylint 报告。
* 处理涉及国际字符的各种编码问题。

**测试插件**
1.  按下 F5 键在一个新的 VSCode 窗口中启动插件。
2.  在测试窗口中打开任何 Python 文件。
3.  点击编辑器标题栏中的“审查 Python 代码”按钮。

**项目结构**
*   `src/extension.ts` - 插件主代码
*   `review_script.py` - 执行 pylint 分析的 Python 脚本
*   `out/extension.js` - 编译后的 JavaScript 输出
*   `package.json` - 插件清单和脚本配置

**依赖项**

*   VSCode 插件 API
*   Node.js 的 child_process 模块
*   Python 3.x 并已安装 pylint (`pip install pylint`)
