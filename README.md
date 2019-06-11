# python 学习

python 项目采用[pipenv](http://www.liujiangblog.com/blog/18/)来构建，方便项目依赖管理。
使用它来管理的好处：

1. 将运行环境和系统环境隔离
2. 项目切换时，项目间依赖相互独立，不会影响
3. 方便项目多成员时开发环境 clone。

## 在 ide 中设置 pipenv

### 在 vscode 中设置 pipenv 开发调试环境

1. 先查看 pipenv 虚拟环境

```shell
# e.g. `/Users/mac/.local/share/virtualenvs/pydemo-FdSH9b1B`
pipenv --venv
```

2. 在 vscode 中配置文件添加虚拟环境
   Ctrl + Shift + p
   输入 settings
   在列表中选择 Preferences: Open Settings (JSON)
   在 settings.json 的最后一行
   添加虚拟路径"python.venvPath": "/Users/mac/.local/share/virtualenvs/pydemo-FdSH9b1B"

3. 重启 vscode

## pipenv 项目结构
