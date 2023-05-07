# OpenAI-Checker

## 简介
`OpenAI-Checker` 是一个 Python 脚本，用于检查 OpenAI API 密钥的账单和使用情况，并确定是否可以访问 GPT-4 模型。

## 依赖
- Python 3.6+
- requests 模块 (可以通过 `pip install requests` 命令进行安装)
- 可以访问 `api.openai.com`

## 使用
1. 将此仓库克隆或下载至本地。
2. 安装所需的依赖项。
3. 将您的 OpenAI API 密钥添加到一个名为 `apikey.txt` 的文件中，每行一个KEY。
4. 在终端中键入 `python main.py` 命令运行脚本。

## 输出
脚本将输出 `apikey.txt` 文件中每个密钥的总金额、总使用量、剩余金额以及 API 密钥是否可以访问 GPT-4 模型。

## 示例

```shell
$ python main.py
[*]Total amount: 5.00 USD
[*]Total usage: 0.00 USD
[*]Remaining amount: 5.00 USD
[-]API Key:  sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx cannot access GPT-4
```


## 许可证
本项目基于 MIT 许可证发布 - 请参见 LICENSE 文件获取详情。

## 参考文献
本项目包括使用 OpenAI 基于 GPT-3.5 架构开发的语言模型 ChatGPT 的帮助开发的代码。

以下项目在本项目的开发过程中被引用：

- [openai-billing](https://github.com/ClarenceDan/openai-billing) - [用于余额查询代码的参考]