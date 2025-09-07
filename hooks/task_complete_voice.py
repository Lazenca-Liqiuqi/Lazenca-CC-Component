#!/usr/bin/env python3
"""
Claude Code Stop事件语音播报Hook
当Claude会话结束时，使用系统语音播报提示用户
"""

import json
import sys
import subprocess
import platform

# 语音配置
VOICE_CONFIG = {
    "voice_name": "Microsoft Huihui Desktop",  # 可选: Microsoft Huihui Desktop, Microsoft Zira Desktop, Microsoft Tracy Desktop, Microsoft Hanhan Desktop
    "rate": 2,  # 语音速度 (-10 到 +10)
    "volume": 100,  # 音量 (0 到 100)
}


def get_voice_message():
    return "Moss已经完成你的任务"


def speak_text(text):
    """根据操作系统使用语音播报"""
    system = platform.system()

    try:
        if system == "Windows":
            # Windows使用PowerShell的SpeechSynthesizer，支持音色配置
            voice_name = VOICE_CONFIG["voice_name"]
            rate = VOICE_CONFIG["rate"]
            volume = VOICE_CONFIG["volume"]

            powershell_cmd = f'''
            Add-Type -AssemblyName System.Speech
            $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
            try {{
                $synth.SelectVoice("{voice_name}")
            }} catch {{
                Write-Host "指定语音不存在，使用默认语音"
            }}
            $synth.Rate = {rate}
            $synth.Volume = {volume}
            $synth.Speak("{text}")
            '''
            # 使用Popen异步执行，不等待完成，避免阻塞主进程
            subprocess.Popen(
                ["powershell", "-Command", powershell_cmd],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
                if hasattr(subprocess, "CREATE_NO_WINDOW")
                else 0,
            )

        elif system == "Linux":
            # Linux尝试使用espeak或festival（异步执行）
            try:
                subprocess.Popen(
                    ["espeak", text],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except FileNotFoundError:
                try:
                    # 使用Popen启动festival进程
                    process = subprocess.Popen(
                        ["festival", "--tts"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
                    # 异步发送输入并立即关闭stdin，不等待完成
                    process.stdin.write(text.encode())
                    process.stdin.close()
                except FileNotFoundError:
                    print(
                        "警告: 未找到espeak或festival，请安装语音合成软件",
                        file=sys.stderr,
                    )

    except Exception as e:
        print(f"语音播报错误: {e}", file=sys.stderr)


def main():
    """主函数"""
    try:
        # 从stdin读取hook数据
        input_data = sys.stdin.read()

        if not input_data.strip():
            return

        hook_data = json.loads(input_data)

        # 获取事件类型 (Claude Code使用hook_event_name字段)
        event_type = hook_data.get("hook_event_name", hook_data.get("event", "unknown"))

        # 处理Stop事件（会话结束时触发）
        if event_type == "Stop":
            message = get_voice_message()
            speak_text(message)

    except json.JSONDecodeError:
        error_msg = "无法解析hook数据"
        print(error_msg, file=sys.stderr)
    except Exception as e:
        error_msg = f"Hook执行错误: {e}"
        print(error_msg, file=sys.stderr)


if __name__ == "__main__":
    main()
