"""Figure: schematic of the time covering in the proof of the upper bound (Lemma covering).

Usage:  python -u fig_covering.py OUT.pdf

A schematic, not data.  Horizontal coordinate: t = log T, not to scale.
For each large T, let q_j be the first denominator with q_j >= K log T, so that
log T lies in (q_{j-1}/K, q_j/K].  Case A (q_j <= T^a/(2 C_D), i.e.
log T >= t_* := a^{-1} log(2 C_D q_j)) uses the per-denominator estimate at q_j.
Case B (log T < t_*) can occur only after a large jump q_{j-1} -> q_j; then
q = q_{j-1} has b_{j-1} >= c and log T lies in the window [d q, B q] of that scale,
where the selected-scale proposition applies (barrier, or slow dynamics plus barrier).
Note d q_{j-1} = q_{j-1}/K, since d = 1/K.  The tick positions below are arbitrary.
Grayscale only.
"""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

out = sys.argv[1]
INK, MUTED = '0.0', '0.35'
plt.rcParams.update({'font.size': 9, 'font.family': 'serif', 'pdf.fonttype': 42,
                     'hatch.linewidth': 0.6})
NL = chr(10)

# schematic positions on the log T axis (arbitrary, not to scale)
s1, s2, tstar, s3, s4 = 0.9, 2.5, 5.7, 7.6, 9.1
Bq = 6.6            # B q_{j-1}, beyond t_*
x0, x1 = 0.0, 10.0

fig, ax = plt.subplots(figsize=(6.4, 2.35))
ax.set_xlim(x0, x1)
ax.set_ylim(0.55, 4.0)
ax.axis('off')

# time axis
yax = 3.35
ax.annotate('', xy=(x1, yax), xytext=(x0, yax),
            arrowprops=dict(arrowstyle='-|>', color=INK, lw=0.9))
ax.text(x1, yax + 0.18, r'$\log T$', ha='right', va='bottom', fontsize=9)
ax.text(x1, 0.62, 'schematic, not to scale', ha='right', va='bottom',
        fontsize=7.5, color=MUTED)
for xt, lab in [(s1, r'$q_{j-2}/K$'), (s2, r'$q_{j-1}/K$'), (s3, r'$q_j/K$'), (s4, r'$q_{j+1}/K$')]:
    ax.plot([xt, xt], [yax - 0.12, yax + 0.12], color=INK, lw=0.9)
    ax.text(xt, yax + 0.18, lab, ha='center', va='bottom', fontsize=8.5)
ax.plot([tstar, tstar], [yax - 0.12, yax + 0.12], color=MUTED, lw=0.9)
ax.text(tstar, yax - 0.2, r'$t_*=\frac{1}{a}\log(2C_Dq_j)$', ha='center', va='top',
        fontsize=7.5, color=MUTED)

# assignment bar
yb, hb = 2.05, 0.55
def seg(xa, xb, hatch=None, label=None, fs=7.5):
    if hatch:
        r = Rectangle((xa, yb), xb - xa, hb, facecolor='white', edgecolor=INK, lw=0.8, hatch=hatch)
    else:
        r = Rectangle((xa, yb), xb - xa, hb, facecolor='0.85', edgecolor=INK, lw=0.8)
    ax.add_patch(r)
    if label:
        ax.text((xa + xb) / 2, yb + hb / 2, label, ha='center', va='center', fontsize=fs,
                bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none') if hatch else None)

seg(s1, s2, label='A: estimate' + NL + r'at $q_{j-1}$')
seg(s2, tstar, hatch='////', label=r'B: window of $q=q_{j-1}$')
seg(tstar, s3, label='A: estimate' + NL + r'at $q_j$')
seg(s3, s4, label='A: estimate' + NL + r'at $q_{j+1}$')
ax.text(s1 - 0.12, yb + hb / 2, r'$\cdots$', ha='right', va='center', fontsize=9)
ax.text(s4 + 0.12, yb + hb / 2, r'$\cdots$', ha='left', va='center', fontsize=9)
ax.text(x0, yb + hb + 0.08, 'estimate used at time $T$', ha='left', va='bottom', fontsize=7.5,
        color=MUTED)

# window of the selected scale q = q_{j-1}
yw = 1.45
ax.annotate('', xy=(s2, yw), xytext=(Bq, yw),
            arrowprops=dict(arrowstyle='|-|', color=INK, lw=0.8, mutation_scale=4,
                            shrinkA=0, shrinkB=0))
ax.text((s2 + Bq) / 2, yw - 0.12,
        r'window $dq\leq\log T\leq Bq$ of the scale $q=q_{j-1}$, which has $b_{j-1}\geq c$',
        ha='center', va='top', fontsize=7.5)
ax.text((s2 + Bq) / 2, yw - 0.62,
        r'barrier if $b_{j-1}<L+2\eta$; slow dynamics and barrier if $b_{j-1}\geq L+2\eta$',
        ha='center', va='top', fontsize=7.5, color=MUTED)

fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
fig.savefig(out)
fig.savefig(out.replace('.pdf', '.png'), dpi=200)
print('wrote', out, flush=True)
