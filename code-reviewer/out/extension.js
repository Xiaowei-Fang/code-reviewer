"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
const child_process_1 = require("child_process");
const path = require("path");
// 插件激活函数，当插件被激活时调用
function activate(context) {
    // 注册命令，当用户点击按钮或从命令面板调用时执行
    let disposable = vscode.commands.registerCommand('python-code-reviewer.reviewCode', () => {
        // 获取当前活动的文本编辑器
        const editor = vscode.window.activeTextEditor;
        // 检查是否有活动的编辑器以及是否是Python文件
        if (!editor || editor.document.languageId !== 'python') {
            vscode.window.showErrorMessage('请打开一个Python文件进行审查。');
            return;
        }
        // 获取当前打开文件的代码内容
        const code = editor.document.getText();
        // 创建或获取输出面板通道，用于显示审查结果
        const outputChannel = vscode.window.createOutputChannel('Python代码审查报告');
        outputChannel.clear();
        outputChannel.show();
        // 显示初始消息
        outputChannel.appendLine('正在使用Pylint审查代码...\n');
        // 获取插件所在的目录路径
        const extensionPath = context.extensionPath;
        // 构建Python脚本的完整路径
        const scriptPath = path.join(extensionPath, 'review_script.py');
        // 调试信息：显示脚本路径
        outputChannel.appendLine(`脚本路径: ${scriptPath}\n`);
        // 检查脚本文件是否存在
        const fs = require('fs');
        let pythonProcess;
        try {
            if (!fs.existsSync(scriptPath)) {
                outputChannel.appendLine(`错误: 找不到审查脚本文件 ${scriptPath}`);
                // 尝试使用默认路径作为备选方案
                const defaultScriptPath = path.join(__dirname, '..', 'review_script.py');
                outputChannel.appendLine(`尝试默认路径: ${defaultScriptPath}`);
                if (fs.existsSync(defaultScriptPath)) {
                    outputChannel.appendLine('使用默认路径成功');
                    // 启动Python进程来执行审查脚本，设置环境变量确保正确的编码
                    const env = process.env;
                    env.PYTHONIOENCODING = 'utf-8';
                    pythonProcess = (0, child_process_1.spawn)('python', [defaultScriptPath], { env: env });
                }
                else {
                    outputChannel.appendLine('默认路径也找不到文件');
                    return;
                }
            }
            else {
                // 启动Python进程来执行审查脚本，设置环境变量确保正确的编码
                const env = process.env;
                env.PYTHONIOENCODING = 'utf-8';
                pythonProcess = (0, child_process_1.spawn)('python', [scriptPath], { env: env });
            }
        }
        catch (error) {
            outputChannel.appendLine(`检查文件时发生错误: ${error.message}`);
            return;
        }
        // 处理Python脚本的标准输出数据
        pythonProcess.stdout.on('data', (data) => {
            // 将审查结果输出到VSCode的输出面板
            outputChannel.append(data.toString());
        });
        // 处理Python脚本的错误输出
        pythonProcess.stderr.on('data', (data) => {
            // 将错误信息输出到VSCode的输出面板
            outputChannel.appendLine(`错误: ${data.toString()}`);
        });
        // 处理Python进程关闭事件
        pythonProcess.on('close', (code) => {
            if (code === 0) {
                // 进程正常结束
                outputChannel.appendLine('\n代码审查完成。');
            }
            else {
                // 进程异常结束
                outputChannel.appendLine(`\n审查过程出现错误，退出码: ${code}`);
            }
        });
        // 将代码内容写入Python进程的标准输入
        pythonProcess.stdin.write(code);
        // 关闭标准输入，表示数据传输完成
        pythonProcess.stdin.end();
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map