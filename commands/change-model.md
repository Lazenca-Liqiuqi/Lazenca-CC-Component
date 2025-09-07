# Claude Code切换模型

## 1 工作流

### 1.1 首先展示所有的模型选择

给用户提供一个标好序号的有序列表以供挑选。

### 1.1.1 Claude

```powershell
setx ANTHROPIC_BASE_URL "https://api.wentuo.ai"
setx ANTHROPIC_AUTH_TOKEN "sk-hiEi8inFbUOKsjoAxRV7Zdy8hFXF201PsMAcLIFCW1F100z1"
setx ANTHROPIC_MODEL ""
setx ANTHROPIC_SMALL_FAST_MODEL ""
```

### 1.1.2 GLM

```powershell
setx ANTHROPIC_BASE_URL "https://open.bigmodel.cn/api/anthropic"
setx ANTHROPIC_AUTH_TOKEN "43632cc392ed478783266f5c0e4cb330.RebbA38cPxJLSVTr"
setx ANTHROPIC_MODEL "glm-4.5"
setx ANTHROPIC_SMALL_FAST_MODEL "glm-4.5"
```

### 1.1.3 Deepseek

```powershell
setx ANTHROPIC_BASE_URL "https://api.deepseek.com/anthropic"
setx ANTHROPIC_AUTH_TOKEN "sk-8c6697412ccd45b289912efe2ff909d5"
setx ANTHROPIC_MODEL "deepseek-chat"
setx ANTHROPIC_SMALL_FAST_MODEL "deepseek-chat"
```

### 1.1.4 Kimi

```powershell
setx ANTHROPIC_BASE_URL "https://api.moonshot.cn/anthropic/"
setx ANTHROPIC_AUTH_TOKEN "sk-eJ2bFotPeaSjJ6qhx7CtMCJ2hof1xFpv3rNoqhrBqSRkgCY2"
setx ANTHROPIC_MODEL "kimi-k2-turbo-preview"
setx ANTHROPIC_SMALL_FAST_MODEL "kimi-k2-turbo-preview"
```

## 1.2 根据用户的选择

在终端中依次输入上面4条命令。

## 2 备用方案

备用方案用于设置claude code的setting.json

```
Kimi K2
"ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic/",
"ANTHROPIC_AUTH_TOKEN": "sk-eJ2bFotPeaSjJ6qhx7CtMCJ2hof1xFpv3rNoqhrBqSRkgCY2"
"ANTHROPIC_MODEL":"kimi-k2-turbo-preview"
"ANTHROPIC_SMALL_FAST_MODEL":"kimi-k2-turbo-preview"

稳妥
"ANTHROPIC_BASE_URL": "https://api.wentuo.ai",
"ANTHROPIC_AUTH_TOKEN": "sk-hiEi8inFbUOKsjoAxRV7Zdy8hFXF201PsMAcLIFCW1F100z1"

智谱
"ANTHROPIC_BASE_URL":"https://open.bigmodel.cn/api/anthropic" ,
"ANTHROPIC_AUTH_TOKEN":"43632cc392ed478783266f5c0e4cb330.RebbA38cPxJLSVTr",
"ANTHROPIC_MODEL": "glm-4.5"
"ANTHROPIC_SMALL_FAST_MODEL":"glm-4.5"

Deepseek
"ANTHROPIC_BASE_URL":"https://api.deepseek.com/anthropic"
"ANTHROPIC_AUTH_TOKEN":"sk-8c6697412ccd45b289912efe2ff909d5"
"ANTHROPIC_MODEL":"deepseek-chat"
"ANTHROPIC_SMALL_FAST_MODEL":"deepseek-chat"
```