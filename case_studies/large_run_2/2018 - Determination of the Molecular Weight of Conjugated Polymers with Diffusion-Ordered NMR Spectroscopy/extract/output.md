<!-- image -->

[pubs.acs.org/cm](pubs.acs.org/cm)

## Determination of the Molecular Weight of Conjugated Polymers with Di ff usion-Ordered NMR Spectroscopy

Kaichen Gu, † Jonathan Onorato, ‡ Steven Shuyong Xiao, § Christine K. Luscombe, ‡ , ∥ and Yueh-Lin Loo * , † , ⊥

† Department of Chemical and Biological Engineering, Princeton University, Princeton, New Jersey 08544, United States

‡ Materials Science and Engineering Department, University of Washington, Seattle, Washington 98195-2120, United States

§ 1-Material Inc., 2290 Chemin St-Franc ̧ ois, Dorval, Quebec, H9P 1K2, Canada

∥ Department of Chemistry, University of Washington, Seattle, Washington 98195-1700, United States

⊥ Andlinger Center for Energy and the Environment, Princeton University, Princeton, New Jersey 08544, United States

<!-- image -->

## * S Supporting Information

ABSTRACT: Size exclusion chromatography (SEC) is not well suited for characterizing the molecular weight (MW) and MW distribution of conjugated polymers, especially those that absorb strongly at the detection wavelengths, or those that interact with and adsorb on the walls of SEC columns. We demonstrate di ff usion-ordered NMR spectroscopy (DOSY) as a complementary method for characterizing the size and size distribution of conjugated polymers. Starting with four batches of poly(3-hexylthiophene), whose distinct and narrow MWdistributions had been fully characterized, as a model system, we establish a power-law relationship between the weight-average MW and the di ff usion coe ffi cient measured through DOSY. We extend this approach to characterizing poly[4-(4,4-dihexadecyl-4 H -cyclopenta[1,2b :5,4b ′ ]dithiophen-2-yl)alt -[1,2,5]thiadiazolo-[3,4c ]pyridine], whose absorption

<!-- image -->

properties preclude its characterization with light scattering based techniques, including SEC. By applying the same power law on the di ff usion coe ffi cients obtained by DOSY measurements, we extracted P3HT-equivalent MWs and MW distributions for six di ff erent batches of PCDTPT. By circumventing the practical issues in SEC measurements, DOSY shows promise as a versatile complement for determining polymer size.

## ■ INTRODUCTION

The performance of electronic devices comprising conjugated polymers has improved steadily over the past two decades, with polymer solar cells exhibiting record e ffi ciencies over 10%, 1 and polymer thin- fi lm transistors exhibiting mobilities well above 1 cm 2 V -1 s -1 . 2 Previous studies have demonstrated that the physical characteristics of conjugated polymers that serve as electrically active constituents, particularly their molecular weights (MWs) and molecular weight distributions (MWDs), play important roles in determining their optoelectronic properties. 3 -5 It is thus crucial to accurately and precisely determine the molecular weight and molecular weight distribution of conjugated polymers. Size exclusion chromatography (SEC) is commonly used to characterize polymer molecular weight and molecular weight distribution, yet it has many limitations. SEC is particularly ill-suited for characterizing conjugated polymers given their sti ff er backbone and lower solubility because these polymers have a strong tendency to interact with and adsorb on the walls of SEC columns. These interactions alter the elution times of polymers in nontrivial ways, ultimately skewing the extracted molecular weight distribution. More problematically, conjugated polymers typically have optical band gaps in the range of 1.5 -3 eV, 6 so they tend to absorb light that is normally used for SEC detection.

<!-- image -->

Nuclear magnetic resonance (NMR) spectroscopy is a powerful tool for determining the structure, conformation, and dynamics of polymers. 7 End-group analysis by NMR allows quanti fi cation of the number of repeating units, and can thus provide the absolute number-average MW ( M n) of low-MW polymers having chemical shifts that can be distinctly attributed to their backbone and end groups. Di ff usion-ordered NMR spectroscopy (DOSY) can be used to characterize polymers whose MW falls between 10 2 and 10 6 g mol -1 . 8 A 2D NMR technique, DOSY, introduces an additional frequency dimension that measures the translational di ff usion coe ffi cient ( D ) of polymers. The di ff usion coe ffi cient in turn provides a measure of the polymer hydrodynamic radius ( R H) through the Stokes -Einstein equation 9

$$\begin{matrix} \cos \Delta D = \frac { k T } { 6 \pi \eta R _ { H } } \end{matrix}$$

where k is the Boltzmann constant, T is the absolute temperature, and η is the viscosity of the solvent. The di ff usion coe ffi cient can then be correlated with the molecular weight of the polymer ( M ) through 8

Received:

December 5, 2017

Revised:

January 11, 2018

Published:

January 12, 2018

$$M = A D ^ { - \alpha } & & ( 2 ) & \quad \text {where} \quad .$$

where A and α are materials-relevant constants. For a polydisperse batch of polymer, the average di ff usion coe ffi cient is correlated with the weight-average molecular weight ( M w) 10,11

$$M _ { w } = A D ^ { - d _ { f } } & & ( 3 ) & \sum _ { \substack { 1 \leq t _ { s } < 0 \\ 0 \leq t _ { s } < 0 } } ^ { 2 }$$

where d f is the fractal dimension of the polymer chain in the solvent in which it is characterized.

DOSY has been employed to characterize the molecular weight for small molecules, 12 poly oxo-metalates clusters, 13 and commodity polymers and biopolymers. 8,11,14 DOSY has also been used to study the formation of supramolecular graft copolymers containing conjugated poly(3-(2-ethylhexyl)thiophene) blocks. 15

In this paper, we show that DOSY can be a viable and general method for characterizing the size and size distribution of conjugated polymers. DOSY is noninvasive and only requires minimal amounts of material (typically &lt; 1 mg per sample). It correlates chemical identities with translational di ff usion coe ffi cients, making the technique well-suited for studying multicomponent systems or polymer samples having a distribution of molecular weights. Starting with four batches of tailor-made poly(3-hexylthiophene), or P3HT, whose MWD had previously been fully characterized by a combination of SEC and end-group analysis, we demonstrate DOSY as an approach to measure their di ff usion coe ffi cients in chloroform and extract their size distributions. Using the available SEC data, we further determined a correlation between the di ff usion coe ffi cients and the absolute molecular weights for several P3HT samples in chloroform. This correlation has allowed us to extend this approach for determining the P3HT-equivalent molecular weight of poly[4-(4,4-dihexadecyl-4 H -cyclopenta[1,2b :5,4b ′ ]dithiophen-2-yl)alt -[1,2,5]thiadiazolo-[3,4c ]-pyridine], or PCDTPT, a donor -acceptor polymer whose MW and MWD are otherwise challenging to determine given that its absorption coincides with the detection wavelengths normally used in SEC.

## ■ EXPERIMENTAL SECTION

Materials. PCDTPT was obtained from 1-Materials Inc. and fractionated into six batches as detailed in the Supporting Information. P3HT was synthesized per literature procedure, 16 with minor modi fi cations, as detailed in the Supporting Information. The four regioregular P3HT samples (P3HT\_5, P3HT\_10, P3HT\_20, and P3HT\_40) had been characterized by SEC and NMR end-group analysis separately, and their absolute molecular weights and dispersities are provided in Table S1 in the Supporting Information.

Optical Absorption Measurements. Absorption spectra were recorded using an Agilent Technologies Cary 5000 spectrophotometer. PCDTPT solutions in chloroform (ca. 0.01 mg mL -1 ) were measured in quartz spectrophotometer cells having a 10 mm path length.

DOSY Experiments. Polymer samples were dissolved in CDCl3 (ca. 0.5 mg mL -1 ). DOSY experiments were performed at 25 ° C on a Bruker AVANCE III with a probe of type PA BBO 500 S1 BBF-H-D05. All experiments were run without spinning to minimize convection. The maximum gradient strength was 50 G cm -1 . The number of linear gradient steps was set to be 32. The standard Bruker pulse program, ' ledbpgp2s ' , was used. The gradient recovery delay time was 0.5 ms and the eddy-current delay is 5 ms. For P3HT samples, di ff usion times were between 50 and 70 ms and the gradient durations were between 2.0 and 2.6 ms. For PCDTPT samples, di ff usion times were between 50 and 100 ms and the gradient durations were between 1.5 and 3.2 ms. The resulting NMR spectra were processed by Mestrelab MNova, and DOSY maps were generated using MNova Bayesian transformation. 17

## ■ RESULTS AND DISCUSSION

To evaluate DOSY ' s capability for characterizing polymer size and size distribution, we started our experiments with polymer samples with well-de fi ned MW and MWD. We used four batches of regioregular P3HT with distinct MWs ( M n of 5, 10, 20, and 40 kg mol -1 ) and narrow MWD, hereafter referred to as P3HT\_ X , where X represents the sample ' s M n in kg mol -1 . In DOSY experiments, di ff usion coe ffi cients are measured through the attenuation of NMR signals under di ff erent pulsed fi eld gradient strengths. Figure 1a shows an example of 1 H 1D

Figure 1. (a) Stacked 1D 1 H NMR spectra of P3HT\_5 in CDCl3 at concentrations ca. 0.5 mg mL -1 . The signal decays with increasing magnetic fi eld gradient strength. (b) 2D DOSY map of the sample after Bayesian transformation. The map correlates the chemical identities of the di ff erent species with their translational di ff usion coe ffi cients.

<!-- image -->

NMR signal attenuation of P3HT\_5 in CDCl3 with increasing magnetic fi eld gradient strength, g . We observe a chemical shift at 7.26 ppm, attributable to residual hydrogenated chloroform in the solution, and a shift at 1.56 ppm, attributable to traces of water. All other chemical shifts can be assigned to the protons of P3HT; a complete chemical shift assignment for P3HT is provided in the Supporting Information. As the gradient strength is increased from 1.0 to 47.5 G cm -1 in 32 increments, the intensities associated with the chemical shifts of P3HT\_5, chloroform, and water exponentially decay. This decay is related to the di ff usion coe ffi cient of the species and is described by eq 4: 18

$$I = I _ { 0 } \exp ( - D Z )$$

Here, Z is a parameter that encodes the magnetic fi eld gradient amplitude, g , the gyromagnetic ratio, γ , the duration of each pulse, δ , and the interval between pulses, Δ . We used the ' ledbpgp2s ' pulse sequence (longitudinal eddy-current delay sequence with bipolar gradient pulse pair with 2 spoil gradients) in these experiments, in which Z is de fi ned as 19

$$\begin{array} { c c c } & & & \text {gradients} \end{array} \text { in these experiments, in which $Z$ is defined as} ^ { 2 } \\ \intertext { y } T \quad & Z = \gamma ^ { 2 } g ^ { 2 } \delta ^ { 2 } \left ( \Delta - \frac { \delta } { 3 } - \frac { \tau } { 2 } \right ) \\ \intertext { s } \intertext { t } \end{array} ( 5 )$$

This pulse sequence minimizes the e ff ect of eddy current and doubles the e ff ective gradient. 20 We observed that the signal

Figure 2. (a) Stejskal -Tanner plot of intensity signal attenuation at δ = 0.91 ppm of the four batches of P3HT in CDCl3. (b) Absolute weightaverage molecular weight of P3HT as a function of di ff usion coe ffi cient. (c) Di ff usion coe ffi cient distributions obtained from DOSY analysis. (d) Absolute molecular weight distributions (solid lines) and calculated distributions from DOSY analysis (dotted lines) for the four batches of P3HT.

<!-- image -->

associated with chloroform protons decays faster than that associated with P3HT protons, consistent with the fact that chloroform is much smaller and thus has a larger di ff usion coe ffi cient compared to its polymer solute.

The stacked spectra were processed via Bayesian transformation to yield the 2D DOSY map that is shown in Figure 1b. The DOSY map shows three well-separated peaks along the di ff usion dimension, corresponding to the presence of trace amounts of water, hydrogenated chloroform, and P3HT\_5. In view of its ability to spectroscopically isolate distinct chemical species, DOSY is also referred to as ' NMR chromatography ' . 21

Figure 2a shows the Stejskal -Tanner plot tracking the attenuation of intensity of the chemical shift at 0.91 ppm, attributable to the methylene protons at the end of the hexyl side chains of P3HT, for the four batches of P3HT in CDCl3. In all cases, the intensity decays exponentially with Z. Per eq 4, the absolute value of the slope of each fi t corresponds to the di ff usion coe ffi cient of the respective batch of P3HT. Increasing the polymer molecular weight from P3HT\_5 to P3HT\_40 leads to larger hydrodynamic radii; we should thus expect to measure progressively smaller di ff usion coe ffi cients per the Stokes -Einstein Equation. The extracted di ff usion coe ffi cients of the di ff erent batches of P3HT are tabulated in Table S2 in the Supporting Information.

The power-law relationship in eq 3 correlates the weightaverage molecular weight that is separately obtained through a combination of SEC and end-group analysis, with the di ff usion coe ffi cient that is obtained by DOSY. This equation can be linearized by taking the logarithms on both sides, yielding

$$\log ( M _ { w } ) = - d _ { f } \log ( D ) + \log ( A ) & & \quad ( 6 ) & & \quad \stackrel { \text {diff} } { \log }$$

The observation that log( M w) varies linearly with log( D ) for P3HT in chloroform, per eq 6, indicates that P3HT exhibits comparable hydrodynamic behavior over the experimentally accessed MW range. From the fi t in Figure 2b, we obtained a quantitative relationship of log( M w) = -1.78 log( D ) -6.29, in which M w and D adopt units of g mol -1 and cm 2 s -1 , respectively. By assessing the maximum and minimum slopes to the fi ts of the data set, we obtain d f = 1.78 ± 0.04 and log( A ) = -6.29 ± 0.25. This power-law relationship provides a calibration for future P3HT samples. Given samples with known D , we can predict their M w, and vice versa. Importantly, this relationship also lends insight into the interactions between P3HT and chloroform. The prefactor indicates a fractal dimension of 1.78 for P3HT in chloroform. This observation suggests that chloroform is a moderately good solvent for P3HT. 8 Were chloroform a theta-solvent in which P3HT adopts Gaussian-like conformation because polymer -polymer and polymer -solvent interactions are comparable, the fractal dimension would have been 2. Were chloroform a good solvent in which P3HT chains are fully solvated because polymer -solvent interactions are more favorable, the fractal dimension would have been 1.70. 8

We also investigated the di ff usion coe ffi cient distributions (DCDs) obtained from DOSY analysis, shown in Figure 2c. The DCDs of P3HT\_5, P3HT\_10, P3HT\_20, and P3HT\_40 progressively shift toward smaller values. Using the M w -D relationship above, we converted the DCDs to MWDs and compared these with the experimentally obtained absolute molecular weight distributions, shown in Figure 2d. Here, the absolute MWDs were extracted from SEC measurements, with an overall M n determined by NMR end-group analysis. Generally, we observe qualitative agreement between the MWDs extracted from DCDs and the experimentally obtained MWDs. Increasing the molecular weight of P3HT increases the hydrodynamic radius of P3HT, resulting in a decrease in the di ff usion coe ffi cient per the Stokes -Einstein Equation. We observe that the DCD-derived MWDs are generally narrower than those experimentally determined by SEC and NMR endgroup analysis. This discrepancy likely results from the need to inverse Laplace transform frequency-domain data, a process that is mathematically ill-posed. 10,22 Further exacerbating this discrepancy is the fact that we only have a limited number of data points for this DOSY transformation. Though microscopic averaging e ff ects in which solute molecules tend to di ff use at the same rate as its neighboring molecules due to intermolecular interactions could also play a role in peak narrowing, this e ff ect is not signi fi cant at the low polymer concentrations used in our study. 10

The DCD of P3HT\_20 shown in Figure 2c has a shoulder to the left of the main peak. This shoulder is reminiscent of the bimodal feature in the MWD of P3HT\_20 that is captured by SEC analysis, as shown in Figure 2d. The DCD indicates the shoulder portion of P3HT has a larger di ff usion coe ffi cient compared to the minority population in P3HT\_20. This observation correlates well with the SEC-obtained MWD that reveals the majority population of P3HT\_20 to be higher in molecular weight. The main peak and shoulder, however, are closer to each other in the DCD-derived MWD compared to the experimentally obtained MWD. This observation is consistent with those made on polypropylene with bimodal MWDs. 22 We attribute this di ff erence to issues associated with inverse Laplace transformation, not di ff erent from the peak narrowing issues highlighted above.

$$\begin{array} { r l } & { d e p e n d e n c o r l s r a d u s o l g y r a c h o r ( K _ { g } ) o n m o l e c u r a w e n t } & { d i f f e e r } \\ & { p e r e q 7 ^ { 2 3 } } & { \quad } \\ & { \frac { R _ { g } ^ { 2 } } { M } = \frac { L _ { p } } { 3 m _ { L } } - \frac { L _ { p } ^ { 2 } } { M } + \frac { 2 L _ { p } ^ { 3 } m _ { L } } { M ^ { 2 } } \left ( 1 - \frac { L _ { p } m _ { L } } { M } } & { \text {using} } \\ & { \frac { 1 - \exp \left ( - \frac { M } { L _ { p } m _ { L } } \right ) \right ) \right ] } { ( 7 ) } } \\ & { w h e r e M i s t h e m o l e c u r a w e n t a n d m _ { L } i s t h e m o l e c u r a w e n t } & { \quad } \\ & { \quad } & { \quad } \\ & { w h e r e M i s t h e m o l e c u r a w e n t a n d m _ { L } i s t h e m o l e c u r a w e n t } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \quad } \\ & { \quad } & { \qu$$

π -Conjugation along the polymer backbone tends to promote chain rigidity. The DOSY-derived di ff usion measurements allow us to quantify the extent of chain rigidity because R H, related to the di ff usion coe ffi cient by the Stokes -Einstein equation, is a function of chain conformation as well as molecular weight. Assuming the wormlike chain (WLC) model, we estimated the persistence length ( L p) of P3HT from the dependence of its radius of gyration ( R g) on molecular weight per eq 7 23

where M is the molecular weight and mL is the molecular weight per unit contour length of 0.39 nm. 24 We fi rst estimated the value of R g from R H by the Kirkwood -Riseman theory: 25

$$R _ { g } = \frac { 3 } { 2 } R _ { H } & & \text {num} \\ & & \text {single}$$

This theoretical framework for calculating persistence length was originally developed for monodisperse systems. 23 To account for the polydispersity in these P3HT samples, we used ensemble-average values to approximate the MWs in the model. We estimated the persistence length of P3HT to be 2.32 nm using M w and 3.15 nm using M n , in good agreement with experimental values obtained by light scattering (2.4 ± 0.3 nm) 26 and neutron scattering (3.0 ± 0.1 nm), respectively. 27 Regioregularity will necessarily a ff ect chain conformation. In fact, the persistence length of regiorandom P3HT is estimated to only be approximately one-third that of its regioregular counterpart. 27 Given its sensitivity to chain conformation, DOSY should be able to shed light on the impact regioregularity has on the hydrodynamic behavior of P3HT; this study is the subject of a future publication.

To assess the general applicability of DOSY for quantifying size and size distribution of conjugated polymers, we applied this analysis to PCDTPT, a low-band-gap donor -acceptor semiconducting polymer, whose chemical structure is shown in Figure 3a. PCDTPT is a copolymer comprising cyclopenta[2,1-

<!-- image -->

H

Figure 3. (a) Chemical structure of PCDTPT used in this study. (b) Absorption spectra of the six batches of PCDTPT solutions (ca. 0.01 mg mL -1 in chloroform) at room temperature. (c) Maximum absorbance wavelength of the original sample (empty square) and the fractionated aliquots (solid circles) as a function of PCDTPT hydrodynamic radius.

b :3,4b ′ ]dithiophene (CDT) as its donor moiety and pyridal[2,1,3]-thiadiazole (PT) as its acceptor moiety. 28 Characterization of PCDTPT with SEC is challenging because PCDTPT strongly absorbs light at the incident wavelength of the laser used for detection.

We fractionated as-received PCDTPT based on solubility di ff erences imparted by MW di ff erences via Soxhlet extraction. To induce selective fractionation, we varied the solvent quality using binary solvent mixtures of chloroform and methanol. Chloroform is a good solvent, whereas methanol is an antisolvent for PCDTPT. Increasing chloroform content in these mixtures thus increases the solvent quality for PCDTPT and induces selective extraction of less soluble portions, i.e., the higher-MW component. Because methanol -chloroform mixtures form a positive azeotrope, 29 the starting composition is not representative of the composition in the extracting reservoir. To quantify the composition in the extracting reservoir, we calculated the instantaneous vapor composition, or the instantaneous condensate composition, from methanol -chloroform vapor -liquid equilibrium. Then we performed numerical integrations based on the Rayleigh equation for single-stage batch distillation to estimate the average e ff ective composition for each solvent mixture used in this study. The solvent mixtures used and estimation of the reservoir compositions are detailed in Table S3 in the Supporting Information. We started with a solvent mixture with 80 vol % methanol and extracted the most soluble portions of PCDTPT, which presumably has the lowest MW in the batch. Using solvent mixtures with increasing chloroform content, we yielded six distinct batches of PCDTPT, which we refer to as PCDTPT\_1 through PCDTPT\_6 in the order of decreasing solubility, and presumably increasing molecular weight.

Figure 3b shows the optical absorption spectra of all six batches of PCDTPT in chloroform at ca. 0.01 mg mL -1 . The absorption spectra of PCDTPT \_1 through PCDTPT\_6 show a progressive red shift; the wavelengths at maximum absorbance are quanti fi ed in Figure 3c as a function of the hydrodynamic radius of the samples in chloroform, as quanti fi ed from the di ff usion coe ffi cients obtained from DOSY experiments. Plotting the absorbance wavelength as a function of the hydrodynamic radius reveals a monotonic relationship; this observation is expected since increasing the polymer size increases its conjugation length, which in turn decreases its optical band gap, resulting in a red shift in its absorption spectrum. 30 -33

Figure 4a shows the Stejskal -Tanner plot displaying the attenuation of the integrated intensity of the chemical shifts

Figure 4. (a) Stejskal -Tanner plot of intensity signal attenuation integrated over δ = 0.5 -1 ppm and (b) di ff usion coe ffi cient distributions obtained from DOSY analysis for the six batches of PCDTPT, PCDTPT\_1 through PCDTPT\_6. (c) P3HT-equivalent molecular weight distributions of the six batches of PCDTPT, calculated from the respective di ff usion coe ffi cient distributions with the power-law relationship in eq 3.

<!-- image -->

between 0.4 and 0.9 ppm for the six batches of PCDTPT in CDCl3. Due to its more complicated chemical structure and overlapping chemical shifts, we chose to quantify the integrated intensity of chemical shifts over the fi nite range of 0.4 -0.9 ppm for PCDTPT. Because eq 4 is only valid for the quanti fi cation of intensity attenuation of chemical shifts belonging to a single species, we veri fi ed that the chemical shifts in this range are all attributable to PCDTPT, and not to the solvent or any impurities in solution. This chemical shift range does not overlap with the chemical shift of water at 1.56 ppm or that of chloroform at 7.26 ppm. The rate at which the signal decays decreases progressively in the Stejskal -Tanner plot of PCDTPT\_1 to PCDTPT\_6. The extracted di ff usion coeffi cients of the di ff erent batches of PCDTPT are tabulated in Table S4 in the Supporting Information.

Figure 4b shows the di ff usion trace for each batch of PCDTPT obtained from DOSY analysis. Consistent with an increase in conjugation length that we expected given the progressive red shift in the optical absorbance, we observe a decrease in di ff usion coe ffi cients from sample PCDTPT\_1 to PCDTPT\_6.

We were not able to determine the absolute molecular weight of PCDTPT by end-group analysis because the intensities of the chemical shifts associated with the end groups of PCDTPT are negligible and the chemical shifts associated with the bulky alkyl side chains on the donor -acceptor repeating units convolute chemical shifts from other portions of the polymer. This transformation would have allowed us to quantify the absolute number-average molecular weight of PCDTPT. To determine the relative molecular weights of PCDTPT samples, we borrowed a framework commonly used in SEC analysis. We converted the DCD of the six batches of PCDTPT to MWDs, based on the M w -D correlation we determined for P3HT. The P3HT-equivalent MWDs for PCDTPT are shown in Figure 4c. To fi rst order, this method of assessing P3HT-equivalent MW gives us a relative estimate of the size of the polymer. From the estimated MWs, we believe the fi rst three batches of PCDTPT (PCDTPT\_1, PCDTPT\_2, and PCDTPT\_3) to be oligomeric in nature, with P3HTequivalent M w of 1340, 2270, and 5840 g mol -1 , respectively. The P3HT-equivalent M w for PCDTPT\_4, PCDTPT\_5, and PCDTPT\_6 are 27 200, 29 700, and 73 500 g mol -1 . The same analysis carried out on the as-received, unfractionated PCDTPT, in comparison, reveals a P3HT-equivalent M w of 32 500 g mol -1 . The molecular weight increase across the series of PCDTPT samples is consistent with the progressive red shift in their optical spectra. That the M w of unfractionated PCDTPT falls between those of PCDTPT\_5 and PCDTPT\_6 is further consistent with its optical spectra, with its maximum absorbance located at a wavelength between those of PCDTPT\_5 and PCDTPT\_6. A critical assumption we have made with this framework is that P3HT and PCDTPT exhibit the same hydrodynamic characteristics in chloroform. Given that PCDTPT has a larger MW per unit contour length (approximately 600 g mol -1 nm -1 ) 34 compared to P3HT (approximately 400 g mol -1 nm -1 ) 24 , the P3HT-equivalent M w ' s we extracted for the PCDTPT samples are likely to underestimate their actual molecular weights. Nonetheless, this approach has provided important relative size information about these samples that would otherwise be challenging to obtain.

## ■ CONCLUSIONS

We demonstrate DOSY as a complement to SEC for characterizing the size of conjugated polymers. DOSY analysis is particularly useful and relevant to conjugated polymers whose molecular weight characterization by SEC is limited by their absorption characteristics.

We determined a power-law relationship between M w and D for regioregular P3HT dissolved in chloroform, from which we extracted the fractal dimension of P3HT to be 1.78. The fractaldimension analysis provides a viable platform to probe the interactions of di ff erent pairs of solvent and conjugated polymers. Further, the M w -D calibration curve can be used to interconvert M w and D of future P3HT samples on an absolute basis, or other polymers on a relative basis. Unlike the molecular weight, the di ff usion coe ffi cient is dependent on temperature and the solvent used. To ensure accuracy for M w -D conversion, experiments should be carried out under the same conditions. We also demonstrated that di ff usion coe ffi cient distributions obtained by DOSY qualitatively agree with the molecular weight distributions yielded by a combination of SEC and end-group analysis. Quantitative agreement between them is di ffi cult given that the data inversion process can inherently result in artifacts, such as peaknarrowing.

Complementary to conventional SEC, DOSY, a 2D NMR technique, o ff ers a facile way for determining polymer size. It uniquely addresses molecular weight determination for polymers, particularly conjugated polymers, that absorb at SEC detection wavelengths and those that interact with SEC columns. Owing to its ability to measure a wide range of molecular weights and separate chemically distinct species, DOSY shows promise toward becoming a standard method for determining polymer size.

## ■ ASSOCIATED CONTENT

## * S Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.chemmater.7b05063.

P3HT synthesis and characterizations, DOSY operating procedures, PCDTPT solvent-antisolvent Soxhlet extraction, and summary of di ff usion coe ffi cients (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

* E-mail: lloo@princeton.edu.

## ORCID

<!-- image -->

Christine K. Luscombe: 0000-0001-7456-1343

Yueh-Lin Loo: 0000-0002-4284-0847

## Author Contributions

The manuscript was written through contributions of all authors. All authors have given approval to the fi nal version of the manuscript.

## Notes

The authors declare no competing fi nancial interest.

## ■ ACKNOWLEDGMENTS

This work was supported by ExxonMobil through its membership in the Princeton E- fi lliates Partnership of the Andlinger Center for Energy and the Environment. C.K.L. acknowledges NSF DMR 1708317. The P3HT samples were synthesized in part upon work supported by the State of Washington through the University of Washington Clean Energy Institute and via funding from the Washington Research Foundation.

## ■ REFERENCES

- (1) Zhao, J.; Li, Y.; Yang, G.; Jiang, K.; Lin, H.; Ade, H.; Ma, W.; Yan, H. Efficient Organic Solar Cells Processed from Hydrocarbon Solvents. Nat. Energy 2016 , 1 , 15027.
- (2) Sirringhaus, H. 25th Anniversary Article: Organic Field-Effect Transistors: The Path beyond Amorphous Silicon. Adv. Mater. 2014 , 26 , 1319 -1335.
- (3) Koch, F. P. V.; Rivnay, J.; Foster, S.; Mu ̈ ller, C.; Downing, J. M.; Buchaca-Domingo, E.; Westacott, P.; Yu, L.; Yuan, M.; Baklar, M.; Fei, Z.; Luscombe, C.; McLachlan, M. A.; Heeney, M.; Rumbles, G.; Silva, C.; Salleo, A.; Nelson, J.; Smith, P.; Stingelin, N. The Impact of Molecular Weight on Microstructure and Charge Transport in Semicrystalline Polymer Semiconductors-poly(3-Hexylthiophene), a Model Study. Prog. Polym. Sci. 2013 , 38 , 1978 -1989.
- (4) Gasperini, A.; Sivula, K. Effects of Molecular Weight on Microstructure and Carrier Transport in a Semicrystalline Poly(thieno)thiophene. Macromolecules 2013 , 46 , 9349 -9358.
- (5) Himmelberger, S.; Vandewal, K.; Fei, Z.; Heeney, M.; Salleo, A. Role of Molecular Weight Distribution on Charge Transport in Semiconducting Polymers. Macromolecules 2014 , 47 , 7151 -7157.
- (6) Strobl, G. The Physics of Polymers , 3rd ed.; Springer-Verlag: Berlin, 2007.
- (7) Spiess, H. W. 50th Anniversary Perspective: The Importance of NMR Spectroscopy to Macromolecular Science. Macromolecules 2017 , 50 , 1761 -1777.
- (8) Auge ́ , S.; Schmit, P.-O.; Crutchfield, C. A.; Islam, M. T.; Harris, D. J.; Durand, E.; Clemancey, M.; Quoineaud, A.-A.; Lancelin, J.-M.; Prigent, Y.; Taulelle, F.; Delsuc, M.-A. NMR Measure of Translational Diffusion and Fractal Dimension. Application to Molecular Mass Measurement. J. Phys. Chem. B 2009 , 113 , 1914 -1918.
- (9) Einstein, A.; Furth, R.; Cowper, A. D. Investigations on the Theory of the Brownian Movement ; Courier Dover Publications: Mineola, NY, 1956.
- (10) Chen, A.; Wu, D.; Johnson, C. S. Determination of Molecular Weight Distributions for Polymers by Diffusion-Ordered NMR. J. Am. Chem. Soc. 1995 , 117 , 7965 -7970.
- (11) Li, W.; Chung, H.; Daeffler, C.; Johnson, J. A.; Grubbs, R. H. Application of 1H DOSY for Facile Measurement of Polymer Molecular Weights. Macromolecules 2012 , 45 , 9595 -9603.
- (12) Crutchfield, C. A.; Harris, D. J. Molecular Mass Estimation by PFG NMR Spectroscopy. J. Magn. Reson. 2007 , 185 , 179 -182.
- (13) Floquet, S.; Brun, S.; Lemonnier, J. F.; Henry, M.; Delsuc, M. A.; Prigent, Y.; Cadot, E.; Taulelle, F. Molecular Weights of Cyclic and Hollow Clusters Measured by DOSY NMR Spectroscopy. J. Am. Chem. Soc. 2009 , 131 , 17254 -17259.
- (14) Viel, S.; Capitani, D.; Mannina, L.; Segre, A. Diffusion-Ordered NMR Spectroscopy: A Versatile Tool for the Molecular Weight Determination of Uncharged Polysaccharides. Biomacromolecules 2003 , 4 , 1843 -1847.
- (15) Hardeman, T.; Willot, P.; De Winter, J.; Josse, T.; Gerbaux, P.; Shestakova, P.; Nies, E.; Koeckelberghs, G. Study on the Formation of a Supramolecular Conjugated Graft Copolymer in Solution. J. Polym. Sci., Part A: Polym. Chem. 2014 , 52 , 804 -809.
- (16) Bronstein, H. A.; Luscombe, C. K. Externally Initiated Regioregular P3HT with Controlled Molecular Weight and Narrow Polydispersity. J. Am. Chem. Soc. 2009 , 131 , 12894 -12895.
- (17) Cobas, C.; Sy ́ kora, S. Poster Presentation. Bayesian Dosy : A New Approach To Di ff usion Data Processing. In SMASH Small Molecule NMR 2008 Conference 2008 , Santa Fe, NM, Sept 7 -10, 2018; SMASH NMR Conference, 2018.
- (18) Stejskal, E. O.; Tanner, J. E. Spin Diffusion Measurements: Spin Echoes in the Presence of a Time-Dependent Field Gradient. J. Chem. Phys. 1965 , 42 , 288 -292.
- (19) Johnson, C. S., Jr. Diffusion Ordered Nuclear Magnetic Resonance Spectroscopy: Principles and Applications. Prog. Nucl. Magn. Reson. Spectrosc. 1999 , 34 , 203 -256.
- (20) Cohen, Y.; Avram, L.; Frish, L. Diffusion NMR Spectroscopy in Supramolecular and Combinatorial Chemistry: An Old Parameter New Insights. Angew. Chem., Int. Ed. 2005 , 44 , 520 -554.
- (21) Gounarides, J. S.; Chen, A.; Shapiro, M. J. Nuclear Magnetic Resonance Chromatography: Applications of Pulse Field Gradient Diffusion NMR to Mixture Analysis and Ligand-Receptor Interactions. J. Chromatogr., Biomed. Appl. 1999 , 725 , 79 -90.
- (22) Jerschow, A.; Mu ̈ ller, N. Diffusion-Separated Nuclear Magnetic Resonance Spectroscopy of Polymer Mixtures. Macromolecules 1998 , 31 , 6573 -6578.

- (23) Teraoka, I. Polymer Solutions: An Introduction to Physical Properties , 1st ed.; John Wiley &amp; Sons: New York, 2002; Vol. 3 .
- (24) Brinkmann, M.; Wittmann, J.-C. Orientation of Regioregular Poly(3-Hexylthiophene) by Directional Solidification: A Simple Method to Reveal the Semicrystalline Structure of a Conjugated Polymer. Adv. Mater. 2006 , 18 , 860 -863.
- (25) Kirkwood, J. G.; Riseman, J. The Intrinsic Viscosities and Diffusion Constants of Flexible Macromolecules in Solution. J. Chem. Phys. 1948 , 16 , 565 -573.
- (26) Heffner, G. W.; Pearson, D. S. Molecular Characterization of Poly(3-Hexylthiophene). Macromolecules 1991 , 24 , 6295 -6299.
- (27) Mcculloch, B.; Ho, V.; Hoarfrost, M.; Stanley, C.; Do, C.; Heller, W. T.; Segalman, R. A. Polymer Chain Shape of Poly(3Alkylthiophenes) in Solution Using Small-Angle Neutron Scattering. Macromolecules 2013 , 46 , 1899 -1907.
- (28) Ying, L.; Hsu, B. B. Y.; Zhan, H.; Welch, G. C.; Zalar, P.; Perez, L. A.; Kramer, E. J.; Nguyen, T.; Heeger, A. J.; Wong, W.; Bazan, G. C. Regioregular Pyridal[2,1,3]thiadiazole π -Conjugated Copolymers. J. Am. Chem. Soc. 2011 , 133 , 18538 -18541.
- (29) Nagata, I. Isobaric Vapor-Liquid Equilibria for the Ternary System Chloroform-Methanol-Ethyl Acetate. J. Chem. Eng. Data 1962 , 7 , 367 -373.
- (30) Meier, H.; Stalmach, U.; Kolshorn, H. Effective Conjugation Length and UV/vis Spectra of Oligomers. Acta Polym. 1997 , 48 , 379 -384.
- (31) Klaerner, G.; Miller, R. D. Polyfluorene Derivatives : Effective Conjugation Lengths from Well-Defined Oligomers. Macromolecules 1998 , 31 , 2007 -2009.
- (32) Izumi, T.; Kobashi, S.; Takimiya, K.; Aso, Y.; Otsubo, T. Synthesis and Spectroscopic Properties of a Series of B-Blocked Long Oligothiophenes up to the 96-Mer: Re-Evaluation of Effective Conjugation Length. J. Am. Chem. Soc. 2003 , 125 , 5286 -5287.
- (33) Wohlgenannt, M.; Jiang, X. M.; Vardeny, Z. V. Confined and Delocalized Polarons in Pi-Conjugated Oligomers and Polymers: A Study of the Effective Conjugation Length. Phys. Rev. B: Condens. Matter Mater. Phys. 2004 , 69 , 241204.
- (34) Tseng, H. R.; Phan, H.; Luo, C.; Wang, M.; Perez, L. A.; Patel, S. N.; Ying, L.; Kramer, E. J.; Nguyen, T. Q.; Bazan, G. C.; Heeger, A. J. High-Mobility Field-Effect Transistors Fabricated with Macroscopic Aligned Semiconducting Polymers. Adv. Mater. 2014 , 26 , 2993 -2998.