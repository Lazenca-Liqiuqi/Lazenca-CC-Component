#!/usr/bin/env python3
"""
Claude Code 对话开始语音播报Hook
当对话/会话开始时，使用系统语音播报欢迎信息
"""

import json
import sys
import subprocess
import platform

# 语音配置
VOICE_CONFIG = {
    "voice_name": "Microsoft Huihui Desktop",  # 可选: Microsoft Huihui Desktop, Microsoft Zira Desktop, Microsoft Tracy Desktop, Microsoft Hanhan Desktop
    "rate": 3,  # 语音速度 (-10 到 +10)
    "volume": 100,  # 音量 (0 到 100)
}


def get_greeting_message():
    """生成打招呼消息"""
    return "我是MOSS——你也可以叫我小苔藓"


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
            subprocess.Popen(
                ["powershell", "-Command", powershell_cmd],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
                if hasattr(subprocess, "CREATE_NO_WINDOW")
                else 0,
            )

        elif system == "Linux":
            # Linux尝试使用espeak或festival
            try:
                subprocess.run(["espeak", text], check=True, capture_output=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    subprocess.run(
                        ["festival", "--tts"],
                        input=text.encode(),
                        check=True,
                        capture_output=True,
                    )
                except (subprocess.CalledProcessError, FileNotFoundError):
                    print(
                        "警告: 未找到espeak或festival，请安装语音合成软件",
                        file=sys.stderr,
                    )

    except subprocess.CalledProcessError as e:
        print(f"语音播报失败: {e}", file=sys.stderr)
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

        # 获取事件类型
        event_type = hook_data.get("hook_event_name", hook_data.get("event", "unknown"))

        # 处理对话开始事件
        # 可能的事件类型：SessionStart, startup
        if event_type in [
            "SessionStart",
            "startup",
        ]:
            message = get_greeting_message()
            speak_text(message)

    except json.JSONDecodeError:
        error_msg = "无法解析hook数据"
        print(error_msg, file=sys.stderr)
    except Exception as e:
        error_msg = f"Hook执行错误: {e}"
        print(error_msg, file=sys.stderr)


if __name__ == "__main__":
    main()
