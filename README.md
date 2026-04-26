# Study about Deep Learning

## 1. Introduction 与学习进度

这是一个深度学习初学者的笔记，跟随教程《动手学深度学习》（d2l）学习，并按章节记录理论与实践代码。初衷是记录自己的学习历程与思考并尝试分享，在完整学习完后会进行系统性整理。目前有 Jupyter Notebook 与 Markdown 两种文档格式，方便多种方式阅读。

学习进度：已学完 Ch7，对应笔记已更新到 7.2（VGG）；省略了原书的前两章与（主线关联较弱、且暂不影响后续实践推进的部分内容，后续会按需要回补。）


## 2. 学习资源

- 主线教材：《动手学深度学习》（d2l）
	- https://zh-v2.d2l.ai/
- d2l习题与补充讲解：
	- https://github.com/datawhalechina/d2l-ai-solutions-manual
- 其他d2l学习笔记参考：
	- https://github.com/AccumulateMore/CV
- 书籍资料（鱼书等）：
	《深度学习入门：基于Python的理论与实践》- https://github.com/chapin666/books/tree/master/ai
- 实战与数据：Kaggle 相关比赛与数据集
	- https://www.kaggle.com/

## 3. 文件结构

```text
Study-about-deep-Learning/
├── data/
│   └── FashionMNIST/                    # 练习使用的数据集目录
├── docs/
│   ├── ch3/ ch4/ ch5/ ch6/              # 主要章节 Markdown 笔记
│   ├── *_files/                         # Notebook/页面导出的辅助资源目录
│   ├── 4.8 Kaggle房价预测实战/           # 4.8 扩展文档与配套文件
│   └── .obsidian/                       # Obsidian 工作区配置与索引
├── notebook/
│   ├── 3.x ~ 7.x *.ipynb                # 主线实验 Notebook
│   ├── 4.8 Kaggle房价预测实战/           # 视频课程 Kaggle 房价预测比赛实践代码
│   └── py_proj/                         # 非笔记脚本（训练函数、数据读取等复用代码）
└── README.md
```

非笔记文件（夹）说明：

- `data/FashionMNIST/`：存放原始数据文件，供相关章节直接读取。
- `docs/*_files/`：导出辅助资源目录（图片、页面依赖等），不是主要阅读入口。
- `docs/.obsidian/`：Obsidian 工程配置目录，用于本地笔记管理。
- `docs/4.8 Kaggle房价预测实战/`：章节扩展资料目录，补充主文档之外的实践记录。
- `notebook/4.8 Kaggle房价预测实战/`：Kaggle 房价预测比赛的分支实践目录，包含我的实验代码与提交文件。
- `notebook/py_proj/`：复用型 Python 脚本目录，用来减少 Notebook 中重复代码。

### 学习进度图表

| 章节 | 主题 | 备注 |
| --- | --- | --- |
| Ch3 | 线性神经网络 |  |
| Ch4 | 多层感知机（MLP） |  |
| Ch5 | GPU 计算 |  |
| Ch6 | 卷积神经网络 |  |
| Ch7 | AlexNet / VGG | 更新中 |

## 4. 使用方式

### 4.1 阅读路径

- `docs/` 下的 Markdown 文档可以直接阅读，闲的时候可以在github移动端阅读。
- `notebook/` 下的 ipynb 适合边跑边学，建议和对应章节文档配套阅读。

### 4.2 运行 ipynb 前准备

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install torch torchvision torchaudio
pip install d2l pandas numpy matplotlib jupyter requests ipython
jupyter notebook
```

### 4.3 学习顺序建议

- 建议按原书章节顺序运行：先 3.x，再 4.x、5、6.x，……
- 若只想快速看主线，可先跑每章总览或核心实验（如 3.1、4.0、6.6、7.1、7.2等）。

## 5. FAQ

>以下是我在学习途中遇到的难折腾的问题。（更新中）

### Q1：GPU 不可用怎么办？

问题现象：

- 运行训练代码时出现 CUDA 不可用（如 `torch.cuda.is_available()` 返回 `False`）
- 或出现显卡/驱动相关报错（如找不到 CUDA 设备）

可能原因：

- 显卡驱动未正确安装，或驱动版本过旧
- CUDA 与已安装的 PyTorch 版本不匹配
- Notebook 使用的 Python 环境与终端安装依赖的环境不是同一个
- 当前设备无 NVIDIA GPU，或在远程环境中未分配 GPU

解决步骤：

1. 先确认是否具备可用 NVIDIA GPU，以及系统是否正确识别显卡。
2. 在当前运行环境中检查 PyTorch 与 CUDA 状态：

```python
import torch
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.version.cuda)
```

3. 若 `is_available()` 为 `False`，优先检查驱动和 CUDA，再核对 PyTorch 安装来源是否与目标 CUDA 版本匹配。
4. 若终端可用但 Notebook 不可用，切换 Notebook Kernel 到同一虚拟环境后重启内核再试。
5. 若暂时无法启用 GPU，可先使用 CPU 继续学习与验证流程，后续再补 GPU 环境。

## 结尾

感谢你的阅读。这个仓库会继续按学习进度迭代，欢迎交流建议与改进想法。
