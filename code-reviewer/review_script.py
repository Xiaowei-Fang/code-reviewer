#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python代码审查脚本
该脚本使用pylint对传入的Python代码进行静态分析，并输出审查报告
"""

import sys
import tempfile
import subprocess
import os

def analyze_code(code):
    """
    使用pylint分析Python代码并返回审查报告
    
    参数:
        code (str): 要分析的Python代码字符串
    
    返回:
        str: pylint生成的审查报告
    """
    # 处理可能存在的代理对字符问题
    try:
        # 尝试规范化字符串，移除或替换无效的代理对
        code = code.encode('utf-8', errors='replace').decode('utf-8')
    except Exception:
        # 如果规范化失败，尝试使用其他方法
        try:
            code = code.encode('utf-8', errors='ignore').decode('utf-8')
        except Exception:
            # 最后的备选方案，使用Latin-1编码
            code = code.encode('latin-1', errors='ignore').decode('latin-1', errors='ignore')
    
    # 创建一个临时文件来存储代码，使用UTF-8编码
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        # 设置环境变量以确保正确的编码
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        # 运行pylint对临时文件进行分析
        # --output-format=text: 指定输出格式为文本
        # --reports=no: 不显示摘要报告，只显示详细问题
        result = subprocess.run([
            'pylint', 
            temp_file_path,
            '--output-format=text',
            '--reports=no'
        ], capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
        
        # 获取审查报告内容
        report = result.stdout
        
        # 如果没有发现问题，pylint可能返回空输出
        if not report.strip() and result.stderr.strip():
            report = result.stderr
        elif not report.strip():
            return "恭喜！Pylint未发现任何问题。代码质量很好！"
        
        return report
    except FileNotFoundError:
        # 如果系统中没有安装pylint，返回错误信息
        return "错误：未找到pylint。请确保已安装pylint (pip install pylint)。"
    except Exception as e:
        # 捕获其他可能的异常
        return f"审查过程中发生错误: {str(e)}"
    finally:
        # 清理临时文件
        try:
            os.unlink(temp_file_path)
        except Exception:
            pass  # 忽略删除临时文件时可能发生的错误

def main():
    """
    主函数：从标准输入读取代码并输出分析结果到标准输出
    """
    # 设置标准输入和输出的编码
    try:
        # 重新配置stdin和stdout以使用UTF-8编码
        sys.stdin.reconfigure(encoding='utf-8', errors='replace')
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        # 在某些Python版本中可能不支持reconfigure方法
        pass
    
    # 从标准输入读取所有代码内容
    try:
        code = sys.stdin.read()
    except Exception as e:
        print(f"读取输入时发生错误: {e}")
        return
    
    # 分析代码
    report = analyze_code(code)
    
    # 将审查报告输出到标准输出
    try:
        print(report, flush=True)
    except UnicodeEncodeError:
        # 如果直接打印失败，尝试编码后打印
        print(report.encode('utf-8', errors='replace').decode('utf-8'), flush=True)

# 当脚本被直接执行时调用主函数
if __name__ == "__main__":
    main()