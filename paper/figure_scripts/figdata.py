import numpy as np, scipy.sparse as sp, json, sys
from scipy.special import jv
def prop_setup(lam, p, q, eta, theta=0.2137, Tfac=4.0):
    alpha = p/q + eta; delta = q*alpha - p; Nb = 1/(abs(delta)*lam**q)
    half = int(5*Nb) + 200; n = np.arange(-half, half+1)
    v = 2*lam*np.cos(2*np.pi*(theta + n*alpha)); N = len(n)
    H = sp.diags([np.ones(N-1), v, np.ones(N-1)], [-1, 0, 1], format='csr')
    a = 2 + 2*lam + 0.01
    return dict(alpha=alpha, delta=delta, Nb=Nb, half=half, n=n, H=H/a, a=a, Tmax=Tfac/abs(delta))
def cheb_coefs(a, dt):
    K = int(a*dt + 40*(a*dt)**(1/3) + 30)
    return np.array([(1 if k == 0 else 2)*(-1j)**k*jv(k, a*dt) for k in range(K)])
def step(Hs, phi, c):
    T0 = phi; T1 = Hs @ phi; acc = c[0]*T0 + c[1]*T1
    for k in range(2, len(c)):
        T2 = 2*(Hs @ T1) - T0; acc += c[k]*T2; T0, T1 = T1, T2
    return acc
def radius(prob, n, f):
    order = np.argsort(-np.abs(n)); cum = np.cumsum(prob[order]); k = np.searchsorted(cum, f); return int(abs(n[order[k]]))
def run(lam, p, q, eta, npts=160):
    st = prop_setup(lam, p, q, eta); n = st['n']; psi = np.zeros(len(n), complex); psi[st['half']] = 1
    dt = st['Tmax']/npts; c = cheb_coefs(st['a'], dt); out = []
    for i in range(1, npts+1):
        psi = step(st['H'], psi, c); prob = np.abs(psi)**2
        out.append([i*dt, radius(prob, n, 0.5), radius(prob, n, 0.1), radius(prob, n, 1e-3), radius(prob, n, 1e-8), float(prob[np.abs(n) > st['half']-50].sum())])
    return dict(lam=lam, p=p, q=q, eta=eta, delta=st['delta'], Nb=st['Nb'], trace=out)
cases = [(1.5,2,5,1e-4),(1.5,2,5,3e-5),(2.0,2,5,2e-5),(2.0,2,5,6e-6),(3.0,2,5,2e-6),(1.5,3,8,2e-5),(2.0,3,8,4e-6),(1.5,5,13,2e-6)]
res = []
for cs in cases:
    r = run(*cs); res.append(r)
    print(cs, 'Nb=%.1f'%r['Nb'], 'max r1e-3=%d'%max(t[3] for t in r['trace']), flush=True)
    json.dump(res, open(sys.argv[1], 'w'))
print('done', flush=True)
