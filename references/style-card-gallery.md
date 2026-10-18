# 首屏风格图册

本图册与完整视觉卡一一对应。调用时必须显示每张预览图；图片为已确认方向的代表样张，不是用户原图的最终成品承诺。

渲染时将下列图片相对路径解析为 Skill 根目录下的绝对本地路径，再以图片附件或 Markdown 图片实际展示。按五个风格组由上到下顺序展示，编号必须连续为 01–15；每张图保留对应编号和名称。

## 固定首屏排版

- 每个大类先显示其分类标题（A、B、C、D、E）。
- 同一大类内使用一张横向 Markdown 表格／图格：每个卡片占一列，第一行是“编号｜名称”，第二行是对应预览图。A、C、D 各 4 列，B 为 2 列，E 为 1 列。
- 每一组下方才换行到下一组；禁止把每张预览图单独竖向排列，也不要在图册后再重复罗列全部编号和名称。

输出形态示例（图片路径在输出时换成对应绝对路径）：

```markdown
### A. 清透图纸

| 01｜轻彩留白 | 02｜精密线描构成 | 03｜透明线框光影 | 04｜低饱和扁平色块 |
| --- | --- | --- | --- |
| ![01](<绝对预览图路径>) | ![02](<绝对预览图路径>) | ![03](<绝对预览图路径>) | ![04](<绝对预览图路径>) |
```

## A. 清透图纸

| 编号 | 名称 | 预览资产 |
| --- | --- | --- |
| 01 | 轻彩留白 | `assets/style-previews/01-light-plan.png` |
| 02 | 精密线描构成 | `assets/style-previews/02-precision-line.png` |
| 03 | 透明线框光影 | `assets/style-previews/03-ghost-line.png` |
| 04 | 低饱和扁平色块 | `assets/style-previews/04-flat-blocks.png` |

## B. 投影构成

| 编号 | 名称 | 预览资产 |
| --- | --- | --- |
| 05 | 灰阶投影构成 | `assets/style-previews/05-gray-shadow.png` |
| 06 | 硬影黑白构成 | `assets/style-previews/06-hard-shadow.png` |

## C. 留白气氛

| 编号 | 名称 | 预览资产 |
| --- | --- | --- |
| 07 | 新中式卷轴 | `assets/style-previews/07-chinese-scroll.png` |
| 08 | 景观写实沙盘 | `assets/style-previews/08-landscape-model.png` |
| 09 | 雾白柔影绿植 | `assets/style-previews/09-misty-green.png` |
| 10 | 版式纸感彩平 | `assets/style-previews/10-paper-board.png` |

## D. 立体材质

| 编号 | 名称 | 预览资产 |
| --- | --- | --- |
| 11 | 深线材质图纸 | `assets/style-previews/11-deep-material.png` |
| 12 | 白模空间浮雕 | `assets/style-previews/12-white-model.png` |
| 13 | 暖灰纸感浮雕 | `assets/style-previews/13-warm-paper.png` |
| 14 | 写实深阴影立体 | `assets/style-previews/14-deep-realism.png` |

## E. 手绘表达

| 编号 | 名称 | 预览资产 |
| --- | --- | --- |
| 15 | 松弛马克笔手绘 | `assets/style-previews/15-hand-drawn-marker.png` |
