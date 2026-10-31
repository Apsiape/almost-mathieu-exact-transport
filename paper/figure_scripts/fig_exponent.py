"""Figure: the exponent picture (plot of proved formulas, no numerics).

Usage:  python -u fig_exponent.py OUT.pdf

Horizontal coordinate x = log(lambda)/beta(alpha) at a fixed finite beta > 0,
so x = 0, 1, 2 correspond to lambda = 1, e^beta, e^(2 beta).

Curves (all closed-form):
  typical law, this paper, theta in G_alpha^*:   gamma(x) = max(0, 1 - x)
  worst-case companion, all-phase upper bound:   F_U(x) = 1 - x/2 (x <= 1), 1/(1 + x) (x > 1)
  worst-case companion, phase 1/4 lower bound
     when beta_e = beta:                         max(0, 1 - x/2)
On 0 < x <= 1 the last two coincide: the worst phase is exactly 1 - x/2 there
(when beta_e = beta).  Grayscale only: identity is carried by line style and
direct labels, never by color.
"""
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = sys.argv[1]
INK, MUTED, BAND = '0.0', '0.35', '0.88'
plt.rcParams.update({'font.size': 9, 'font.family': 'serif', 'axes.edgecolor': MUTED,
                     'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': MUTED,
                     'axes.linewidth': 0.8, 'pdf.fonttype': 42})

XMAX = 2.6
x = np.linspace(0.0, XMAX, 1301)
typ = np.maximum(0.0, 1.0 - x)
low14 = np.maximum(0.0, 1.0 - x / 2.0)
upper = np.where(x <= 1.0, 1.0 - x / 2.0, 1.0 / (1.0 + x))

fig, ax = plt.subplots(figsize=(5.2, 2.95))

# region where the worst phase is not determined (between the companion's bounds)
m = x >= 1.0
ax.fill_between(x[m], low14[m], upper[m], color=BAND, lw=0, zorder=0)

# threshold line lambda = e^beta
ax.plot([1.0, 1.0], [0.0, 0.5], color='0.7', lw=0.8, zorder=0)

# worst-case companion curves
ax.plot(x, low14, color=INK, lw=1.4, ls=(0, (5, 3)), zorder=2)
ax.plot(x[m], upper[m], color=MUTED, lw=1.3, ls=(0, (1, 1.6)), zorder=2)

# typical law (this paper)
ax.plot(x, typ, color=INK, lw=2.2, solid_capstyle='butt', zorder=3)

# open point at x = 0: lambda -> 1 is a limit, critical coupling is outside the theorems
ax.plot([0.0], [1.0], marker='o', ms=6, mfc='white', mec=INK, mew=1.2, zorder=4, clip_on=False)
# closed point at the threshold x = 1 (equality lambda = e^beta is included, exponent 0)
ax.plot([1.0], [0.0], marker='o', ms=5, mfc=INK, mec=INK, zorder=4, clip_on=False)

# direct labels (text in ink, never in series colour)
NL = chr(10)
ax.annotate(r'this paper, $\theta\in G_\alpha^*$:' + NL + r'$\max\{0,1-\log\lambda/\beta\}$',
            xy=(0.33, 0.67), xytext=(0.03, 0.04), fontsize=8, color=INK,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
ax.annotate('worst phase (companion), when' + NL + r'$\beta_e=\beta$: $1-\log\lambda/(2\beta)$',
            xy=(0.62, 0.69), xytext=(0.66, 0.86), fontsize=8, color=INK,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
ax.annotate('all-phase upper bound' + NL + r'(companion): $\beta/(\beta+\log\lambda)$',
            xy=(1.95, 1 / 2.95), xytext=(1.6, 0.5), fontsize=8, color=INK,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
ax.annotate(r'$\theta=1/4$ lower bound' + NL + r'when $\beta_e=\beta$',
            xy=(1.3, 0.35), xytext=(1.04, 0.04), fontsize=7, color=INK,
            arrowprops=dict(arrowstyle='-', color=MUTED, lw=0.6))
ax.text(2.13, 0.2, 'worst phase' + NL + 'not determined', fontsize=7, color=MUTED, va='center')

ax.set_xlim(0.0, XMAX)
ax.set_ylim(0.0, 1.04)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels([r'$\lambda=1$', r'$\lambda=e^{\beta}$', r'$\lambda=e^{2\beta}$'])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xlabel(r'coupling $\lambda$, on the scale $\log\lambda/\beta(\alpha)$, at fixed $0<\beta(\alpha)<\infty$')
ax.set_ylabel('upper transport exponent')
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(out)
fig.savefig(out.replace('.pdf', '.png'), dpi=200)
print('wrote', out, flush=True)
