import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Use a clean font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1, 1, figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

# Color palette — warm professional
colors = {
    'start':   '#10b981',  # green
    'input':   '#3b82f6',  # blue
    'action':  '#8b5cf6',  # purple
    'result':  '#f59e0b',  # amber
    'copy':    '#ef4444',  # red
    'save':    '#06b6d4',  # cyan
    'arrow':   '#64748b',  # slate
    'text':    '#1e293b',  # slate-800
    'white':   '#ffffff',
    'border':  '#e2e8f0',
    'shadow':  '#cbd5e1',
}

def draw_box(ax, x, y, w, h, color, title, desc, icon_text):
    """Draw a rounded box with title and description."""
    # Shadow
    shadow = FancyBboxPatch(
        (x + 0.08, y - 0.08), w, h,
        boxstyle="round,pad=0.15", facecolor=colors['shadow'],
        edgecolor='none', alpha=0.3, zorder=0
    )
    ax.add_patch(shadow)

    # Main box
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.15", facecolor=colors['white'],
        edgecolor=color, linewidth=2.5, zorder=1
    )
    ax.add_patch(box)

    # Color bar on left
    bar = FancyBboxPatch(
        (x, y + 0.1), 0.12, h - 0.2,
        boxstyle="round,pad=0.05", facecolor=color,
        edgecolor='none', alpha=0.85, zorder=2
    )
    ax.add_patch(bar)

    # Icon circle
    circle = plt.Circle((x + w/2, y + h - 0.45), 0.3,
                        facecolor=color, edgecolor='white', linewidth=2, zorder=3)
    ax.add_patch(circle)
    ax.text(x + w/2, y + h - 0.45, icon_text, ha='center', va='center',
            fontsize=13, fontweight='bold', color='white', zorder=4)

    # Title
    ax.text(x + w/2, y + h - 1.0, title, ha='center', va='center',
            fontsize=14, fontweight='bold', color=colors['text'], zorder=4)

    # Description
    ax.text(x + w/2, y + 0.65, desc, ha='center', va='center',
            fontsize=9.5, color='#475569', zorder=4, linespacing=1.5)

def draw_number_circle(ax, x, y, num):
    """Draw a numbered step indicator."""
    circle = plt.Circle((x, y), 0.28, facecolor='#1e293b',
                        edgecolor='white', linewidth=2.5, zorder=5)
    ax.add_patch(circle)
    ax.text(x, y, str(num), ha='center', va='center',
            fontsize=12, fontweight='bold', color='white', zorder=6)

def draw_arrow(ax, x1, y1, x2, y2, color='#94a3b8'):
    """Draw a connecting arrow."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                               lw=2.5, connectionstyle='arc3,rad=0'),
                zorder=0)

def draw_arrow_down(ax, x1, y1, x2, y2, color='#94a3b8'):
    """Draw a downward connecting arrow."""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                               lw=2.5, connectionstyle='arc3,rad=0'),
                zorder=0)

# ============================================================
# Layout: top row (3 boxes) → middle row (1 box) → bottom row (2 boxes)
# ============================================================

bw, bh = 3.6, 2.6  # box width and height

# Row 1: Steps 1, 2, 3
y1 = 6.8
x1, x2, x3 = 0.6, 6.2, 11.8

# Step 1: 用户打开网页
draw_box(ax, x1, y1, bw, bh, colors['start'],
         '打开网页', '用户在浏览器中输入网址\n打开AI文本生成器工具界面',
         'S')
draw_number_circle(ax, x1 + 0.5, y1 + bh - 0.3, 1)

# Step 2: 输入开头文字 + 提示
draw_box(ax, x2, y1, bw, bh, colors['input'],
         '输入内容', '输入开头文字作为故事起点\n设置风格、长度、温度等参数',
         'I')
draw_number_circle(ax, x2 + 0.5, y1 + bh - 0.3, 2)

# Step 3: 点击生成
draw_box(ax, x3, y1, bw, bh, colors['action'],
         '点击生成', '点击"生成"按钮发送请求\nAI模型开始处理并生成文本',
         'G')
draw_number_circle(ax, x3 + 0.5, y1 + bh - 0.3, 3)

# Arrows between Row 1
draw_arrow(ax, x1 + bw, y1 + bh/2, x2, y1 + bh/2)
draw_arrow(ax, x2 + bw, y1 + bh/2, x3, y1 + bh/2)

# Row 2: Step 4 — center box (wide)
y2 = 3.5
x_center = 4.2
bw_wide = 7.6

draw_box(ax, x_center, y2, bw_wide, bh, colors['result'],
         'AI 返回多个版本结果',
         'AI根据输入内容生成多个不同风格的续写版本\n用户可以预览、对比、选择最满意的版本',
         'R')
draw_number_circle(ax, x_center + 0.5, y2 + bh - 0.3, 4)

# Arrow from Step 3 down to Step 4 (center)
draw_arrow(ax, x3 + bw/2, y1, x_center + bw_wide/2, y2 + bh, '#94a3b8')

# Row 3: Steps 5, 6
y3 = 0.3
x5, x6 = 2.0, 9.6

# Step 5: 复制/重新生成/调整
draw_box(ax, x5, y3, bw + 0.8, bh, colors['copy'],
         '复制 / 重新生成 / 调整参数',
         '一键复制生成结果到剪贴板\n不满意可调整参数重新生成\n或修改输入提示获取新结果',
         'C')
draw_number_circle(ax, x5 + 0.5, y3 + bh - 0.3, 5)

# Step 6: 保存生成记录
draw_box(ax, x6, y3, bw + 0.8, bh, colors['save'],
         '保存生成记录',
         '满意的文本可保存到本地\n方便日后回顾和使用',
         'V')
draw_number_circle(ax, x6 + 0.5, y3 + bh - 0.3, 6)

# Arrows from Step 4 down to Steps 5 & 6
draw_arrow(ax, x5 + (bw+0.8)/2, y3 + bh, x5 + (bw+0.8)/2, y2 + 0.1 - 0.3, '#94a3b8')
# Down arrow from step 4 to step 5
ax.annotate('', xy=(x5 + (bw+0.8)/2, y3 + bh), xytext=(x_center + bw_wide*0.35, y2),
            arrowprops=dict(arrowstyle='->', color='#94a3b8', lw=2.5,
                           connectionstyle='arc3,rad=0.15'),
            zorder=0)

# Down arrow from step 4 to step 6
ax.annotate('', xy=(x6 + (bw+0.8)/2, y3 + bh), xytext=(x_center + bw_wide*0.65, y2),
            arrowprops=dict(arrowstyle='->', color='#94a3b8', lw=2.5,
                           connectionstyle='arc3,rad=-0.15'),
            zorder=0)

# Loop back arrow from Step 5 back to Step 2 (re-generate loop)
ax.annotate('', xy=(x2 + bw*0.3, y1), xytext=(x5 + (bw+0.8)*0.7, y3 + bh),
            arrowprops=dict(arrowstyle='->', color='#f87171', lw=2,
                           connectionstyle='arc3,rad=-0.35', linestyle='dashed'),
            zorder=0)
ax.text(2.0, 5.45, '重新生成', fontsize=9, color='#f87171', fontweight='bold',
        rotation=75, zorder=5)

# Title
ax.text(8.0, 9.65, 'AI Text Generator — 用户流程图', ha='center', va='center',
        fontsize=22, fontweight='bold', color='#0f172a')
ax.text(8.0, 9.25, 'User Flow Diagram', ha='center', va='center',
        fontsize=13, color='#64748b', style='italic')

# Footer
ax.text(8.0, -0.35, 'github.com/Eliot954/ai-text-generator-demo', ha='center', va='center',
        fontsize=10, color='#94a3b8')

plt.tight_layout(pad=2)
plt.savefig('user_flow.png', dpi=200, bbox_inches='tight', facecolor='#f8f9fa', edgecolor='none')
plt.close()
print("Done: user_flow.png saved.")
