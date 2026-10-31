# Exact transport and spectral dimensions for the almost Mathieu operator

Seth Douglas and Nidhal Mghirbi

Version 2.0.0, October 2026. DOI: [10.5281/zenodo.23848977](https://doi.org/10.5281/zenodo.23848977). A preprint; it has not been peer reviewed. Version 1.0.0 (titled "Exact transport and packing dimension for the almost Mathieu operator"): [10.5281/zenodo.23830305](https://doi.org/10.5281/zenodo.23830305). Concept DOI (all versions): [10.5281/zenodo.23830304](https://doi.org/10.5281/zenodo.23830304).

## Abstract

For the almost Mathieu operator with coupling λ>1 and irrational frequency α, let β(α)=limsup_n q_n^{-1} log q_{n+1} and γ=max{0,1−log λ/β(α)}, read as 0 if β=0 and 1 if β=∞. For almost every phase, the upper Abel-averaged transport exponent of every positive moment, normalized by its order, the fastest-tail exponent, and both packing dimensions of every nonzero spectral measure equal γ. For finite β the phase set is an explicit set G_α*, invariant under θ↦θ+α, that allows subexponential decay of |sin 2πq_nθ| along resonant scales; for β=∞ the equalities hold at every phase. The lower bounds hold at every phase. Moreover, for fixed c>h>log λ, along scales with b_n=q_n^{-1} log|q_nα−p_n|^{-1}≥c, the Abel-averaged mass beyond distance Te^{−hq_n} from the launch site tends to one, uniformly in the phase, the launch site and e^{hq_n}≤T≤|q_nα−p_n|^{-1}; for a packet launched at the origin and fixed b>0, s∈(0,1), the instantaneous mass within that distance exceeds s at only o(T) times in [0,bT]. For phases in G_α*, and at every phase if β=∞, the upper generalized Rényi dimensions of orders 0<r<1 of the single-site spectral measure equal γ; the lower ones vanish at every phase. For 1<λ<e^β the packing formula replaces the factor two in the bound of Jitomirskaya, Liu and Tcheremchantsev by the sharp factor one. The proof combines an exactly conserved polynomial with elliptic transfer-matrix estimates; its confining barrier holds at every phase. We give explicit finite-time and finite-volume comparison bounds. At coupling 2 and phase 1/4, computable frequencies with eventually odd convergent denominators realize exactly the exponents in [0,1] that are right-c.e. relative to the halting problem. One computable frequency has exponent of Turing degree 0'' for every computable coupling in (1,2^{23/12}), although finite-time predictions at nonzero error tolerance do not determine it.

## Changes in version 2.0.0

- The title is now "Exact transport and spectral dimensions for the almost Mathieu operator".
- Theorem B is stronger: the Abel-averaged fraction of the packet beyond distance T e^{-h q_n} tends to one, uniformly in the phase,
  in the averaging time within the resonant window and in the starting site. Version 1.0.0 gave a fixed fraction 2^{-32}/(1+4 pi lambda).
- A larger, shift-invariant full-measure phase set G_alpha^*, allowing any subexponential decay of |sin 2 pi q_n theta| along the
  resonant scales; the exact law, the packing dimensions, the computability results and the Rényi identities hold on it.
- The spectral barrier now holds at every phase.
- A self-contained section on Rényi dimensions; the coupling interval for the degree-0'' exponent is widened to (1, 2^{23/12}).
- A lower bound at the phase 0 along denominators divisible by four (Remark 13.1).
- Three figures: the exponent as a function of the coupling (proved formulas), a schematic of the covering in time, and a labelled
  numerical illustration of a burst.
- Correction: the outer-barrier lemma needs V_0 > W at the endpoint J = 0; no application is affected.
- The two companion papers are cited with their DOIs, and the text has had an editorial review.

## Contents

The paper is paper/main.pdf (49 pages). Its LaTeX source is paper/main.tex with the section files, paper/references.bib and the three figure PDFs; paper/main.bbl is included. Build with pdflatex and BibTeX. paper/figure_scripts/ regenerates the figures (Python with NumPy and Matplotlib); the burst figure is a numerical illustration and is not used in any proof. No computation is used in any proof.

## Rights

CC BY 4.0. See RIGHTS.md and LICENSE-CC-BY-4.0.txt.

## Related

- "Universality of the transport law for supercritical quasi-periodic operators" (Seth Douglas and Nidhal Mghirbi, 2026), version 1.0.0, [10.5281/zenodo.23830333](https://doi.org/10.5281/zenodo.23830333). It proves the law at almost every phase for supercritical type I analytic potentials.
- "Worst-case transport and light cones for quasi-periodic operators" (Seth Douglas and Nidhal Mghirbi, 2026), version 1.0.0, [10.5281/zenodo.23845228](https://doi.org/10.5281/zenodo.23845228). It treats the worst phase and the light cones of the XY chain.
