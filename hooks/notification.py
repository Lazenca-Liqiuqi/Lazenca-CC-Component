#!/usr/bin/env python3
"""
Claude Code 用户许可请求语音播报Hook
当需要获得用户许可时，使用系统语音播报提示用户
"""

import json
import sys
import subprocess
import platform
import logging
import datetime
import os

# 语音配置
VOICE_CONFIG = {
    "voice_name": "Microsoft Huihui Desktop",  # 可选: Microsoft Huihui Desktop, Microsoft Zira Desktop, Microsoft Tracy Desktop, Microsoft Hanhan Desktop
    "rate": 2,  # 语音速度 (-10 到 +10)
    "volume": 100,  # 音量 (0 到 100)
}


# 配置日志
def setup_logging():
    """配置事件日志记录"""
    log_dir = r"C:\Users\pc\.claude\logs"

    # 确保日志目录存在
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "notification.log")

    # 配置日志格式
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),  # 同时输出到控制台
        ],
    )

    return logging.getLogger(__name__)


def get_permission_voice_message(hook_data):
    """根据Hook数据生成相应的许可请求语音消息"""

    # 获取事件类型
    event_type = hook_data.get("hook_event_name", hook_data.get("event", "unknown"))

    # 根据事件类型返回不同的语音消息
    message_map = {
        "PreToolUse": "Moss需要你的许可使用工具",
        "Notification": "Moss需要你的许可才能继续操作",
        # 兼容其他可能的事件类型
        "ToolPermissionRequest": "Moss需要你的许可使用工具",
        "ConfirmationRequired": "Moss需要你确认操作",
        "PermissionRequest": "Moss需要你的许可才能继续操作",
    }

    return message_map.get(event_type, "Moss，需要你的许可才能继续操作")


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
    # 设置日志记录
    logger = setup_logging()

    try:
        # 从stdin读取hook数据
        input_data = sys.stdin.read()

        if not input_data.strip():
            return

        hook_data = json.loads(input_data)

        # 获取事件类型
        event_type = hook_data.get("hook_event_name", hook_data.get("event", "unknown"))

        # 记录事件到日志
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"事件触发 - 时间戳: {timestamp}, 事件类型: {event_type}")

        # 处理需要用户许可的事件
        # 支持的事件类型：Notification, PreToolUse, UserPromptSubmit 以及其他可能的许可请求事件
        if event_type in [
            "Notification",
            "ToolPermissionRequest",
            "ConfirmationRequired",
            "PermissionRequest",
        ]:
            message = get_permission_voice_message(hook_data)
            speak_text(message)
            logger.info(f"语音播报执行 - 事件类型: {event_type}, 消息: {message}")
        else:
            logger.info(f"事件已记录但无需处理 - 事件类型: {event_type}")

    except json.JSONDecodeError:
        error_msg = "无法解析hook数据"
        logger.error(error_msg)
        print(error_msg, file=sys.stderr)
    except Exception as e:
        error_msg = f"Hook执行错误: {e}"
        logger.error(error_msg)
        print(error_msg, file=sys.stderr)


if __name__ == "__main__":
    main()
