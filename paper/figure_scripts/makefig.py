import json, sys, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
res = json.load(open(sys.argv[1])); out = sys.argv[2]
BLUE, ORANGE, INK, MUTED, GRID = '#2a78d6', '#eb6834', '#1a1a19', '#6b6a64', '#d9d8d2'
plt.rcParams.update({'font.size': 9, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK, 'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.linewidth': 0.8, 'font.family': 'serif'})
fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.7))
pred = np.array([r['Nb'] for r in res]); r3 = np.array([max(t[3] for t in r['trace']) for r in res]); r8 = np.array([max(t[4] for t in r['trace']) for r in res])
lo, hi = 80, 2000; xs = np.array([lo, hi])
a.plot(xs, xs, color=GRID, lw=1, zorder=0); a.plot(xs, 0.4*xs, color=GRID, lw=1, ls='--', zorder=0); a.plot(xs, 1.5*xs, color=GRID, lw=1, ls='--', zorder=0)
a.scatter(pred, r3, s=26, color=BLUE, edgecolor='white', lw=1, label=r'all but $10^{-3}$', zorder=3)
a.scatter(pred, r8, s=26, marker='s', color=ORANGE, edgecolor='white', lw=1, label=r'all but $10^{-8}$', zorder=3)
a.set_xscale('log'); a.set_yscale('log'); a.set_xlim(lo, hi); a.set_ylim(30, 3000)
a.set_xlabel(r'predicted barrier radius $1/(|\delta|\lambda^{q})$'); a.set_ylabel('largest radius reached')
a.legend(frameon=False, fontsize=8, loc='upper left'); a.set_title('(a) confinement radius, 8 scales', fontsize=9, color=INK)
a.text(1150, 1750, r'$\times1.5$', fontsize=7, color=MUTED); a.text(1150, 330, r'$\times0.4$', fontsize=7, color=MUTED)
r = [x for x in res if abs(x['lam'] - 2.0) < 1e-9 and x['q'] == 5 and abs(x['eta'] - 6e-6) < 1e-12][0]
tr = np.array(r['trace']); t = tr[:, 0]*abs(r['delta'])
b.plot(t, tr[:, 1]/r['Nb'], color=BLUE, lw=2, label='median of $|j|$')
b.plot(t, tr[:, 3]/r['Nb'], color=ORANGE, lw=2, label=r'all but $10^{-3}$')
tt = np.linspace(0, 0.6, 50); b.plot(tt, tt/(abs(r['delta'])*r['Nb'])*r['lam']**(-r['q'])*0+tt*1.0, color=GRID, lw=1, ls='--')
b.set_xlabel(r'time $\times\,|\delta|$'); b.set_ylabel(r'radius $\times\,|\delta|\lambda^{q}$'); b.set_ylim(0, 1.25); b.set_xlim(0, 4)
b.text(2.45, 1.09, r'all but $10^{-3}$', color=ORANGE, fontsize=8); b.text(1.25, 0.06, r'median of $|j|$', color=BLUE, fontsize=8); b.set_title(r'(b) $\lambda=2$, $q=5$, $|\delta|=3\cdot10^{-5}$', fontsize=9, color=INK)
for ax in (a, b):
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False); ax.grid(False)
fig.tight_layout(); fig.savefig(out); fig.savefig(out.replace('.pdf', '.png'), dpi=160)
print('ratios r3/pred', np.round(r3/pred, 2), 'r8/pred', np.round(r8/pred, 2))
