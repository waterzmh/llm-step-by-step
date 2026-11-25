# llm-step-by-step
边教边学

## 运行

项目环境使用标准目录名 `.venv`。

```bash
.venv/bin/python main.py
```

依赖记录在 `requirements.txt`，安装到本项目环境：

```bash
uv pip install --python .venv/bin/python -r requirements.txt
```

本机已创建 Python 3.13.11 ARM64 环境。重新创建时，应显式选择 ARM64 Python；本机 Intel 版 uv 按版本号自动选择的 x86_64 Python 无法安装这里的 PyTorch 版本。

VS Code 使用 `Python: Select Interpreter`，选择本项目的 `.venv/bin/python`。

## 01｜搭出第一次更新

当前分支：`01_build_first_update`。

本章逐步手敲输入、Embedding、注意力、预测分数、损失、反向传播与一次参数更新。当前 `main.py` 只完成词表、输入张量和内容/形状/类型打印；模型与更新步骤将在学习中继续添加。

讲解在聊天中进行，暂不生成 HTML 课件。老师运行通过仅说明代码可执行，掌握情况依据学习者的回答与实际操作记录。
