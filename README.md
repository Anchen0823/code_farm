# code_farm

《The Farmer Was Replaced》的个人农场自动化脚本与存档，包含作物种植、收获、移动、多无人机协作、迷宫和恐龙路线等练习。

## 运行环境

脚本使用游戏内的类 Python 语言及 `move`、`harvest`、`Entities`、`Items` 等内置 API，需要在游戏编辑器中运行。普通 Python 解释器没有这些接口。

## 使用方式

1. 在游戏中打开自己的存档目录，并备份当前存档。
2. 将需要使用的 `.py` 文件复制到对应存档的脚本目录；工具模块和引用它们的脚本应放在一起。
3. 回到游戏编辑器，检查脚本需要的作物、道具和功能是否已解锁，再运行目标脚本。

`Save0.json` 与 `Save0/save.json` 是存档数据；只使用算法脚本时无需覆盖自己的存档。部分脚本会执行 `clear()` 或持续循环，应先阅读入口代码。

## 脚本导航

| 入口 | 用途 |
| --- | --- |
| [Save0/main.py](Save0/main.py) | 根据能量库存调度向日葵与胡萝卜种植 |
| [Save0/Auto.py](Save0/Auto.py) | 自动种植和逐步解锁流程 |
| [Save0/plant_utils.py](Save0/plant_utils.py) | 作物种植与收获工具 |
| [Save0/move_utils.py](Save0/move_utils.py) | 坐标移动、迷宫与恐龙路线 |
| [Save0/multitask_utils.py](Save0/multitask_utils.py) | 多任务协作工具 |
| [Save0](Save0/) 中的 `*_compete.py` | 按作物或挑战划分的独立策略 |
| [Save0/__builtins__.py](Save0/__builtins__.py) | 游戏内置 API 的声明和说明 |

这些脚本记录个人实验过程，包含不同策略和试错版本。运行结果取决于游戏版本、地图大小、资源与解锁进度；仓库没有独立于游戏的测试环境。
