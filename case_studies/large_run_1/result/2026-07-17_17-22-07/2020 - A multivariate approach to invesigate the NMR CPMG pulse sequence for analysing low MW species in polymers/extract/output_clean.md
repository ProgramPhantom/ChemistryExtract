## RESEARCH ARTICLE

## A multivariate approach to investigate the NMR CPMG pulse sequence for analysing low MW species in polymers

## Federica Aiello 1 | Jan Gerretzen 1 | Marcel G. Simons 1 | Paulo Dani 1

1 ECG-MAS, Expert Capability Group -Measurement and Analytical Science, Nouryon Chemicals B.V., Deventer, The Netherlands

2 SERC, Sustainable Environment Research Centre, Faculty of Computing Engineering and Science, University of South Wales, Pontypridd, UK

## Correspondence

Federica Aiello and Paulo Dani, ECGMAS, Nouryon Chemicals B.V.,

Zutphenseweg 10, 7418 AJ Deventer, The Netherlands.

Email:

;

## Present address

Federica Aiello, Consiglio Nazionale delle Ricerche, Istituto per i Processi ChimicoFisici, Via G. Moruzzi 1, 56124 Pisa, Italy.

## Funding information

H2020 Marie Sk ł odowska-Curie Actions, Grant/Award Number: 749083

This is an open access article under the terms of the

the original work is properly cited.

© 2020 The Authors. Magnetic Resonance in Chemistry published by John Wiley &amp; Sons Ltd

## Abstract

Detection and quantification of low molecular weight components in polymeric samples via nuclear magnetic resonance (NMR) spectroscopy can be difficult due to overlapping signal caused by line broadening characteristics of polymers. A way of overcoming this problem could be the exploitation of the difference in relaxation between small molecules and macromolecular species, such as the application of a T 2 filter by using the Carr -Purcell -Meiboom -Gill (CPMG) spin-echo pulse sequence. This technique, largely exploited in metabolomics studies, is applied here to material sciences. A Design of Experiments approach was used for evaluating the effect of different acquisition parameters (relaxation delay, echo time and number of cycles) and samplerelated ones (concentration and polymer molecular weight) on selected responses, with a particular interest in performing a reliable quantitative analysis. Polymeric samples containing small molecules were analysed by NMR with and without the application of the filter, and analysis of variance was used to identify the most influential parameters. Results indicated that increasing the polymer concentration, hence sample viscosity, further attenuates polymer signals in CPMG experiments because the T 2 of those signals tends to decrease with increasing viscosity. The signal-to-noise ratio measured for small molecules can undergo a minimum loss when specific parameters are chosen in relation to the polymer molecular weight. Furthermore, the difference in dynamics between aliphatic and aromatic nuclei, as well as between mobile and stiff polymers, translates into different results in terms of polymer signal reduction, suggesting that the relaxation filter can also be used for obtaining information on the polymer structure.

## KEYWORDS

1 H, CPMG, DoE, NMR, polyethylene glycol, polystyrene, quantitative analysis, spin -spin relaxation

License, which permits use, distribution and reproduction in any medium, provided

Antony N. Davies 1,2

|

<!-- image -->

## 1 | INTRODUCTION

Polymeric materials are present in all kinds of everyday objects, from the obvious plastics to, less obvious, metal coatings and food contact materials; they provide specific functional modification to materials like cardboard or paper.

Small molecules are often found in polymeric materials in the form of stabilisers, additives, residual monomers, residual catalysts or by-products related to the manufacturing process. They can affect the final properties of the product (both physical and chemical), [1] and therefore, knowledge about the polymer composition is critical in selecting the best product based on the detailed target application. [2]

Small molecules embedded into a polymeric matrix often play a key role in the functionality of the end product, such as in contraception devices [3] or photovoltaic systems. [4] Detection of such small molecules could enable, for example, the investigation of their stability profiles in the macromolecular environment, as well as analysis of the interactions between the functional small molecule(s) and the matrix. [5 -7]

Nuclear magnetic resonance (NMR) spectroscopy is a well-established and powerful technique for the analysis of polymeric materials [8 -12] and small molecules in a macromolecular environment. [13 -15] The proton ( 1 H) NMR spectra of polymers in solution are usually characterised by line broadening, signal overlap and loss of signal multiplicity, hampering quantification by peak integration. Improvements in spectrometer sensitivity and resolution have enabled multinuclear correlation experiments and hence a better characterisation of polymer structures, providing information on, for example, stereochemistry, regioisomerism, geometric isomerism, end groups and branching. [16] However, the detection and quantification by NMR of low molecular weight (MW) species present in polymeric materials is often thwarted by the overlap between the polymer signals and those belonging to the small molecules.

One solution to this problem is suppressing the polymers' contribution to the NMR spectrum, enabling a better focus on the signals of the small molecules. This can be done by exploiting the differences in diffusion and relaxation between the species. [17]

Diffusion can be measured in NMR by using for instance diffusion-ordered spectroscopy (DOSY) techniques, some of which use pulsed-field gradients (PFGs) in combination with a spin-echo pulse sequence. [18 -20] The larger the size of the analyte, the smaller the corresponding diffusion coefficient; therefore, if a sample contains low MW compounds together with a bigger component, for example, a polymer, the smaller species are expected to have a larger diffusion coefficient.

FIGURE 1 Schematic representation of the Carr -Purcell -Meiboom -Gill (CPMG) pulse sequence

<!-- image -->

A ' relaxation filter ' can alternatively be exploited for separating different species based on their different spin -spin (or transverse) relaxation time T 2. This filter can be applied by using the Carr -Purcell -Meiboom -Gill (CPMG) multi spin-echo pulse sequence (Figure 1). [21 -23] By properly choosing the echo parameters, 2 τ E and n , broad signals belonging to macromolecules with short T 2 can be attenuated or even eliminated from the NMR spectrum, whereas the resonances from the small molecules are still detectable thanks to their longer relaxation; resonances having intermediate T 2 will be subjected to an intermediate attenuation. [17]

The CPMG pulse sequence has been largely employed for identification and quantification of metabolites in biofluids [24] and in the presence of proteins, [25] as well as for the analysis of impurities in protein-based biopharmaceutical products. [26] In each study, different parameter settings relative to the spin-echo filter have been chosen, spanning from a total echo time (2 τ E * n ) of 30 ms [27] to a much longer time of 269 ms. [24]

A first investigation for evaluating the effect of CPMG acquisition parameters on the detection of small molecule signals was performed by Van et al in 2003. [28] The authors pointed out that increasing the total echo time by varying the number of cycles ( n ) determines a loss of the protein signals; at the same time, the small molecules present in the sample (metabolites) are affected, as they undergo a loss in their signal intensity. This loss is, as expected, less significant compared with the one experienced by the macromolecule, although it has not been quantified in the study; when the total echo time is kept constant, the increase of the echo time ( τ E) determines the occurrence of scalar coupling distortions. The authors also investigated the effect of protein concentration, pointing out that the higher the concentration, the stronger the interaction with the metabolites. Consequently, the metabolites signals have a shorter T 2, and hence, they are more affected by the application of the relaxation filter.

The effect of the T 2 filter on the quantification of metabolites was evaluated in another study, which focused particularly on the impact of the recycle delay (d1). [29] If the small molecules and the internal standard (added to the mixture for enabling quantification) are characterised by different values of T 1 and T 2, the quantitative analysis can still be performed with reliable results as long as these differences are taken into consideration and proper correction factors are introduced in the analysis.

Based on these previous results, it was decided to investigate the use of the CPMG relaxation filter for quantification of small molecules moving from the metabolomics field, in which this tool is widely employed, to the material science. Particular focus was given to the analysis of small molecules present in polymeric samples, with the aim of evaluating whether and how the choice of experimental parameters affects the reliability of the quantitative analysis. Polyethylene glycol (PEG) and polystyrene (PS) were selected as polymeric probes, whereas dimethyl terephthalate (DMT) and 1,3,5-trimethoxybenzene (TMB) were used to mimic the presence of small molecules in the samples. These two compounds were chosen among the standards used for quantitative NMR analysis on the basis of their very similar T 1 (for their methyl protons: 1.8 s for DMT and 2.2 s for TMB in CDCl3), which rules out any interference in quantification due to significantly different spin -lattice relaxation times, and because the expected signals multiplicity, a singlet (for both aromatic and aliphatic protons) avoids any scalar coupling distortion phenomena.

Whereas previous studies focused on varying one single parameter at a time, here, a multivariate approach was adopted, by using Design of Experiments (DoE). The purpose of applying DoE in our work is twofold: first, it allows identifying which of the experimental parameters influence a certain response and second, for the experimental parameters deemed relevant, one may calculate a mathematical model that relates these parameters to the response. This can then be used to predict the value of the response given specific settings of the experimental parameters, which in turn enables optimisation (e.g., less phase distortion and favourable conditions for proper quantitative analysis.). DoE thus systematically examines whether there are correlations between the experimental parameters (i.e., the acquisition parameters and the sample composition) and relevant responses, for example, preservation of quantification conditions after applying the pulse. The advantage of using a DoE-based approach is that the number of experiments (runs) can be kept to a minimum without affecting the level of information that can be obtained from the results, thereby considerably saving experimental time and delivering a more robust solution. [30 -32]

## 2 | EXPERIMENTAL DETAILS

## 2.1 | Materials

PEG with different MW (300, 1,000, 6,000, 11,600, 22,500, and 41,500 Da), DMT, TMB, deuterated chloroform

(CDCl3) and deuterated water (D2O) were purchased from Sigma Aldrich (St. Louis, Missouri, United States). PS with different peak MW (Mp) (30,300 Da, MW/Mn = 1.02; 68,900 Da, MW/Mn = 1.02; 220,500 Da, MW/Mn = 1.02, 629,500 Da, MW/Mn = 1.03) was purchased from Polymer Laboratories (Church Stretton, United Kingdom). Dispex ™ N40 was purchased from BASF (Ludwigshafen, Germany). The samples were prepared by dissolving the polymer in the deuterated solvent to reach a concentration between 5 and 10 wt% and by adding DMT and TMB to reach a concentration between 0.1 and 0.3 wt%.

## 2.2 | NMRmeasurements

NMR measurements were performed on a Bruker AVANCE III HD spectrometer equipped with a 5-mm broadband (BBO) Prodigy ™ cryoprobe operating at 600 MHz for 1 H nuclei. Two sets of one-dimensional 1 H NMR experiments were performed for all the samples analysed: CPMG spin-echo [23] with and without water presaturation and one single-pulse 1 H NMR experiments, recorded over a spectral width of 20 ppm with a free induction decay (FID) acquired into 64 K data points during a 2.7 s acquisition time. Thirty-two scans were collected, and a 90  pulse of 10.25 μ s was used.

The recycle delay d1 was varied from 2 to 20 s; the T 2 filter was obtained by setting the echo time 2 τ E between 200 and 1,280 μ s repeated ( n ) from 120 to 620 times. Resulting data were Fourier transformed after multiplication with an exponential window function using a line broadening function of 0.3 Hz. The following pulse sequences provided by Bruker were used for acquiring proton spectra: zg (one single-pulse), cpmg1d ( T 2 filter) and cpmgpr1d ( T 2 filter and presaturation). The T 1 relaxation measurements were performed on a sample containing the small molecules detected in the analysed commercial polymer and the internal standard. The T1ir pulse sequence, provided by Bruker, was used, and the same acquisition parameters employed in the previously described 1D measurements were used.

## 2.3 | Design of experiments

An I-optimal response surface design was created separately for PEG and PS using Design-Expert 10.0.3.1 (Stat-Ease Inc., Minnesota, United States). Both designs were set up in the same way, using five factors all having only discrete factor levels (Tables 1 and 2). In total, five different responses were studied (see next section). The designs were built to be able to fit a quadratic model for each response, and each design featured five lack-of-fit points and five replicate points, leading to 31 experimental runs per design: 21 points, 5 lack-of-fit and 5 replicates.

<!-- image -->

TABLE 1 List of factors and their levels in the design for PEG

|   MWPEG(Da) |   d1 (s) |   τ E ( μ s) |   n |   wt% |
|-------------|----------|--------------|-----|-------|
|         300 |        2 |          100 | 120 |     5 |
|       1,000 |        5 |          150 | 220 |   7.5 |
|       6,000 |        8 |          200 | 320 |    10 |
|      11,600 |       10 |          250 | 420 |       |
|      22,500 |       15 |          300 | 520 |       |
|      41,500 |       20 |          350 | 620 |       |
|             |          |          400 |     |       |
|             |          |          450 |     |       |
|             |          |          500 |     |       |
|             |          |          550 |     |       |
|             |          |          600 |     |       |
|             |          |          640 |     |       |

Abbreviations: MW, molecular weight; PEG, polyethylene glycol.

TABLE 2 List of factors and their levels in the design for PS

|   MW [a] PS (Da) |   d1 (s) |   τ E ( μ s) |   n |   wt% |
|------------------|----------|--------------|-----|-------|
|           30,300 |        2 |          100 | 120 |     5 |
|           68,900 |        5 |          150 | 220 |   7.5 |
|          220,500 |        8 |          200 | 320 |    10 |
|          629,500 |       10 |          250 | 420 |       |
|                  |       15 |          300 | 520 |       |
|                  |       20 |          350 | 620 |       |
|                  |          |          400 |     |       |
|                  |          |          450 |     |       |
|                  |          |          500 |     |       |
|                  |          |          550 |     |       |
|                  |          |          600 |     |       |
|                  |          |          640 |     |       |

Abbreviations: MW, molecular weight; PS, polystyrene.

a The polydispersity (MW/Mn) is equal to 1 for all PS samples, Mp is approximated with MW.

Runs were performed in a random order to minimise bias. This set-up allowed the estimation of the main effects of the five factors, as well as two-factor interactions and the quadratic factor terms. Optimal settings for any factor were calculated by optimizing the response models.

Contour plots showing the effects of multiple factors simultaneously on the responses were generated using the model that Design-Expert fits.

## 3 | RESULTS AND DISCUSSION

## 3.1 | Analysis methodology

For each experimental run, two proton spectra were recorded: one with and one without application of the

- relaxation filter. From both spectra, the following variables were obtained:
- Signal-to-noise ratio (SNR) for the resonances belonging to DMT and TMB;
- Integrated area of polymer signal(s) compared with that of the small molecule (DMT in this case);
- Area ratio between DMT and TMB signals.

From these variables, the responses for the DoE are expressed as:

- Percentage decrease in SNR for small molecules resonances following the application of the filter (Equation 1);
- Percentage variation of DMT/TMB integral area ratio (Equation 2);
- Percentage of polymer signal left after the application of the filter (Equation 3).

$$& \% d e c r e a s e \, i n \, S N R \, ( s m a l l \, m o l e c u l e ) \\ & = [ ( S N R _ { n o f l t e r } - S N R _ { f l t e r } ) / S N R _ { n o f l t e r } ] \times 1 0 0$$

$$& \quad \% v a r i a t i o n \, i n \, D M T / T M B a r e a \, r a t i o \\ & \quad = [ ( r a t i o _ { n o f l y t e r } - r a t i o _ { f i l t e r } ) / r a t i o _ { n o f l y t e r } ] \times 1 0 0$$

$$& \quad \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \$$

The application of the relaxation filter is expected to affect not only the polymer signals but also (even if to a consistently lesser extent) the resonances belonging to small molecules. The percentage decrease in SNR between the nonfiltered and the filtered signals from the peaks of the small molecules (Equation 1) was examined with the aim to evaluate the impact of the T 2 filter on this variable and to identify conditions in which the deterioration in SNR for peaks of small molecules would be minimised.

However, even when their resonances are attenuated, quantitative analysis may still be possible as long as this attenuation affects the resonances of small molecules to a similar extent. Therefore, changes in the ratio between the integral areas of DMT and TMB after application of the filter (Equation 2) were investigated. As stated previously, the choice of DMT and TMB allows to neglect the effect of different T 1 in the quantitative analysis of the small molecules, thus focusing only on the effect of the relaxation filter.

Finally, the ratio between the integrated areas of polymer and the small molecule was used for estimating how much the signals belonging to the polymers are attenuated by the application of the CPMG sequence. The small molecule signal was used as reference, and the integral area of the polymeric signals was calculated in relation to it (Equation 3). If the filter affects in a similar way both the polymer and the small molecule, then the relative ratio between the two species does not change significantly, and the filter is not useful for our purpose of removing polymeric signals so that small molecules can be better analysed. On the contrary, when the polymer is much more affected by the filter than the small molecule, this ratio changes, and as long as the polymeric signal decreases much more than the small molecule one(s), the analysis is feasible. Ideally, the polymer signal should be completely suppressed after application of the filter, and therefore, this response should be as low as possible.

## 3.2 | Polyethylene glycol

Twelve different samples of PEG were prepared, each of them containing DMT and TMB in concentrations between 1 and 5 wt% with respect to the polymer (Table S1). This variation was not considered as a factor in the DoE as it is not expected to have an influence on the responses. As a matter of fact, in this study, the responses are obtained by comparison between the NMR acquisition with and without the filter performed on the same sample, and because the small molecule concentration changes between samples but not between the compared spectra, this variation does not affect the results.

The concentration of PEG in CDCl3 was varied between 5 and 10 wt% to evaluate the impact of polymer concentration in the analysis. An increase in polymer concentration and/or MW has a direct influence on the viscosity of the sample and hence on the dynamics of the system; therefore, it was included as a factor in the DoE. PEG with an MW ranging from only 300 up to 41,500 Da (Table S1) was included in the study. Even though it is more intuitive to consider a 300 MW PEG as a small molecule rather than a polymer (it contains about five monomeric units), it was decided to include it in the design for estimating the filter effect when analysing oligomers or if, on the contrary, there is a recommended minimum polymeric MW.

FIGURE 2 1 H NMR (600 MHz, CDCl3, 300 K) spectrum of polyethylene glycol (PEG) [molecular weight (MW) 300 Da, 5.3 wt%] with DMT (0.17 wt%) and TMB (0.16 wt%). DMT, dimethyl terephthalate; TMB, 1,3,5-trimethoxybenzene

Figure 2 shows the 1 H NMR spectrum of PEG 300 with DMT and TMB. The aromatic signals of DMT and TMB are centred at 8.10 ppm (H1 DMT) and at 6.08 ppm (H3 TMB), respectively, whereas the methoxy protons resonate at 3.95 ppm (H2 DMT) and at 3.77 ppm (H4 TMB), that is, in the same region where PEG signals are expected (4.40 -2.80 ppm).

The effect of the relaxation filter on the responses (percentage variation of SNR, polymer integrated area and DMT/TMB ratio) is shown in Table 3. The SNR measured for the methoxy groups of DMT is affected by the application of the filter, and apart from a few cases, the signal experiences a loss in intensity between 20% and 70%. The lowest loss in SNR does not seem to be strongly related to the relaxation time (d1 + acquisition time) or to the polymer MW or concentration but rather to the total echo time (2 τ E * n ). The SNR for H2 proton undergoes a loss less than 10% when n and τ E have either comparable numerical values (e.g., n = 420 and τ E = 400 μ s, run 5) or τ E (in μ s) is much higher than the number of cycles (e.g., τ E = 640 μ s and n = 320, run 6).

The decrease in SNR was measured for all DMT and TMB resonances, and a comparable trend was observed. In this work, only the decrease in SNR of H2 protons (see Figure 2) is reported. From the statistical analysis [analysis of variance (ANOVA), Table 4], it can be inferred that the significant main factors for this response are d1 (factor A, although the relaxation time is the sum of d1

<!-- image -->

<!-- image -->

TABLE 3 Responses for PEG samples

| Run #   | Factors   | Factors    | Factors   | Factors    | Factors   | Responses           | Responses                | Responses                   |
|---------|-----------|------------|-----------|------------|-----------|---------------------|--------------------------|-----------------------------|
| Run #   | d1 (s)    | τ E ( μ s) | n         | MWPEG (Da) | PEG (wt%) | SNR H2 (decrease %) | PEG area (signal left %) | DMT/TMB ratio (variation %) |
| 1       | 2         | 640        | 120       | 41,500     | 10        | 35.7                | 99.0                     | - 8.1                       |
| 2       | 8         | 200        | 420       | 22,500     | 5         | 32.5                | 90.5                     | 0.0                         |
| 3       | 8         | 350        | 320       | 300        | 10        | 36.4                | 63.7                     | 5.0                         |
| 4       | 15        | 350        | 120       | 22,500     | 5         | 38.7                | 93.0                     | 2.4                         |
| 5       | 20        | 400        | 420       | 22,500     | 7.5       | 3.5                 | 80.6                     | 2.0                         |
| 6       | 10        | 640        | 320       | 1,000      | 7.5       | 0.1                 | 84.3                     | 1.9                         |
| 7       | 20        | 100        | 220       | 300        | 5         | 45.3                | 87.3                     | 13.9                        |
| 8       | 20        | 640        | 620       | 300        | 5         | 53.3                | 70.7                     | 4.2                         |
| 9       | 2         | 100        | 120       | 41,500     | 5         | 47.9                | 106.2                    | - 0.7                       |
| 10      | 2         | 640        | 120       | 300        | 5         | 49.5                | 99.1                     | 14.4                        |
| 11      | 8         | 350        | 320       | 300        | 10        | 28.8                | 64.5                     | - 1.4                       |
| 12      | 20        | 640        | 120       | 300        | 10        | 42.1                | 66.3                     | - 0.9                       |
| 13      | 20        | 640        | 620       | 41,500     | 10        | 21.5                | 55.5                     | - 3.2                       |
| 14      | 2         | 100        | 620       | 300        | 5         | 50.8                | 100.1                    | 2.6                         |
| 15      | 2         | 100        | 620       | 41,500     | 10        | 45.7                | 97.4                     | - 0.7                       |
| 16      | 20        | 400        | 420       | 22,500     | 7.5       | 23.2                | 82.2                     | 5.2                         |
| 17      | 10        | 100        | 120       | 300        | 7.5       | 63.5                | 74.0                     | 7.6                         |
| 18      | 10        | 640        | 320       | 1,000      | 7.5       | 8.6                 | 82.9                     | 1.4                         |
| 19      | 15        | 400        | 120       | 22,500     | 10        | 23.4                | 93.1                     | - 3.0                       |
| 20      | 20        | 100        | 620       | 300        | 10        | 53.9                | 68.3                     | 0.6                         |
| 21      | 10        | 350        | 620       | 41,500     | 7.5       | 42.6                | 74.6                     | 4.3                         |
| 22      | 2         | 640        | 620       | 300        | 10        | 67.9                | 54.8                     | - 7.0                       |
| 23      | 10        | 640        | 420       | 22,500     | 5         | 33.5                | 79.0                     | - 1.0                       |
| 24      | 20        | 100        | 120       | 41,500     | 10        | 40.3                | 95.8                     | - 6.0                       |
| 25      | 20        | 400        | 420       | 22,500     | 7.5       | 10.7                | 82.4                     | 4.6                         |
| 26      | 2         | 600        | 620       | 41,500     | 5         | 43.6                | 75.2                     | - 4.3                       |
| 27      | 20        | 640        | 120       | 41,500     | 5         | 30.0                | 92.7                     | - 1.2                       |
| 28      | 10        | 350        | 620       | 6,000      | 7.5       | 44.2                | 77.9                     | - 8.6                       |
| 29      | 20        | 100        | 620       | 41,500     | 5         | 41.9                | 89.0                     | 4.6                         |
| 30      | 2         | 100        | 120       | 11,600     | 10        | 46.5                | 106.4                    | - 3.9                       |
| 31      | 10        | 640        | 420       | 22,500     | 5         | 32.5                | 79.0                     | - 2.4                       |

Abbreviations: DMT, dimethyl terephthalate; MW, molecular weight; PEG, polyethylene glycol; TMB, 1,3,5-trimethoxybenzene.

and the acquisition time) and polymer MW (factor D). This means that the two parameters seem to influence the decrease in the small molecules SNR. Furthermore, τ E (factor B) and n (factor C) are significant in the quadratic terms B 2 and C 2 , implying that the square of their setting has a linear relation to the decrease in SNR. There is no statistically significant influence of the polymer concentration (factor E) on the SNR decrease. Only the relevant factors (in this case, those with p value lower than 0.05) are reported in the ANOVA tables (Tables 4, S2, S3, S6, S7, S9 and S10). However, in Table 4, even if the AB, B and C factors have a p value higher than 0.05, they are still included because B 2 ( p value 1.04E-03) and C 2 ( p value 9.75E-05) are significant. The same rationale was applied in all subsequent ANOVA analyses. In general terms, a two-factor interaction effect such as AB can

TABLE 4 Analysis of variance (ANOVA) for response surface reduced quadratic model, analysis of variance table for the response % variation in signal-to-noise ratio (SNR) of H2 proton of dimethyl terephthalate (DMT) in PEG

| Source      |   Sum of squares |   df |   Mean square |   F value | p value Prob > F   |                 |
|-------------|------------------|------|---------------|-----------|--------------------|-----------------|
| Model       |          4698.29 |    8 |        587.29 |     13.15 | 1.93E-06           | Significant     |
| A-d1        |           263.80 |    1 |        263.80 |      5.91 | 0.02               |                 |
| B- τ E      |           172.86 |    1 |        172.86 |      3.87 | 0.06               |                 |
| C- n        |           110.45 |    1 |        110.45 |      2.47 | 0.13               |                 |
| D-MW PEG    |           899.14 |    1 |        899.14 |     20.14 | 2.25 E-04          |                 |
| AB          |           145.87 |    1 |        145.87 |      3.27 | 0.09               |                 |
| A 2         |           204.40 |    1 |        204.40 |      4.58 | 0.04               |                 |
| B 2         |           655.51 |    1 |        655.51 |     14.68 | 1.04E-03           |                 |
| C 2         |          1049.51 |    1 |       1049.51 |     23.51 | 9.75E-05           |                 |
| Residual    |           892.94 |   20 |         44.65 |           |                    |                 |
| Lack of fit |           665.78 |   17 |         39.16 |      0.52 | 0.84               | Not significant |
| Pure error  |           227.16 |    3 |         75.72 |           |                    |                 |
| Cor total   |          5591.23 |   28 |               |           |                    |                 |

Abbreviation: PEG, polyethylene glycol.

be interpreted as follows: the effect that factor A has on the response (here decrease in SNR) depends on the setting of factor B.

The factors listed in Table 4 are used to calculate a mathematical model, relating these factors to the decrease in SNR (this model represents the so-called response surface). This model can then be studied to obtain optimal parameter settings to, for example, have only a small decrease in SNR. The graph in Figure 3a shows for this specific system the best compromise d1 (s)

FIGURE 3 Contour plots of PEG data: decrease % for SNR depending on τ E and polymer molecular weight according to the fitted response model, with n set at 320 and d1 equal to (a) 20 s or (b) 2 s (polymer concentration 5 wt%). Percentage of polymer signal left after the application of T 2 filter: (c) dependence from τ E and MW for d1 = 20 s, n = 620 and concentration equal to 10 wt% and (d) dependence from d1 and MW for τ E = 400 μ s, n = 320 and concentration equal to 10 wt%. In all experiments, the acquisition time is set to 2.7 s. MW, molecular weight; PEG, polyethylene glycol; SNR, signal-to-noise ratio

<!-- image -->

between the four relevant factors: by using a 22.7-s relaxation delay (d1 = 20 s + acquisition time = 2.7 s) and a total echo time falling within 190 and 380 ms for a polymer with an MW higher than 26 kDa, the loss in SNR is lower than 10%. For smaller polymers, the minimum expected loss in SNR is 20%. A smaller relaxation delay equal to 4.7 s (d1 = 2 s + acquisition time = 2.7 s, Figure 3b) implies a larger reduction in SNR throughout the full space of echo time and MW PEG (20% reduction seems to be the lowest reduction possible).

PEG resonances are affected by the filter, but in a rather marginal extent, because reductions in polymer signal of no more than approximately 45% were obtained in the DoE (and hence there is approximately 55% signal left, see runs 13 and 22 in Table 3). The ANOVA analysis (Table S2) highlights the contribution of all factors to the PEG resonance, thus making it difficult to obtain an optimal combination of factor settings to achieve a strong reduction in polymer signal. The data would suggest though that for the studied MW interval (300 -41,500 Da), the efficacy of the T 2 filter is limited. Nevertheless, the best results (i.e., strongest reduction in PEG signal) can be achieved, for the whole MW range analysed, by using the longest relaxation time tested (22.7 s) and a total echo time of at least 300 ms (Figure 3c). In the case of MW lower than 1,000 Da, the same reduction can be obtained with a minimum relaxation delay of 9 + 2.7 s and a total echo time around 250 ms (still in the range of the optimal parameters for a small loss in SNR, Figure 3d). Overall, the reduction of polymer signal seems to be more efficient in those samples where the polymer concentration investigated is the highest (i.e., 10 wt%). This outcome can be explained by the fact that an increase in polymer concentration leads to an increase in sample viscosity, probably reducing the T 2 values of the polymer signals. This translates into shorter relaxation times and consequently higher efficacy of the filter. Because this model has a significant lack-of-fit, it cannot be studied further to examine the exact relations between the input factors and the response.

Ultimately, the quantitative analysis is reliable for almost all the experimental runs. Except for two runs, the difference between the DMT/TMB ratio measured without the filter and with the filter falls within 10% and in 70% of the runs the difference in DMT/TMB ratio is within 5%. This result confirms that the quantitative analysis is not directly dependent on any of the analysed factors (Table S3), and as long as the small molecules have comparable dynamics, there is no need to introduce a correction factor. [29]

## 3.3 | Polystyrene

Eleven different samples of PS were prepared, each of them containing DMT and TMB between 1 and 5 wt% with respect to the polymer (Table S4). The PEG samples analysed had an MW between 300 and 41,500 Da, whereas a higher MW range was investigated with PS, namely, between 30,300 and 629,500 Da. Figure 4 shows the 1 H NMR spectrum of PS 629,500 with DMT and TMB. In this case, the polymer signals are in a different spectral region than those of the small molecules, with only aromatic signal H3 close to the aromatic cluster of the polymer.

In contrast with PEG, the relaxation filter performed better with all PS samples by causing a substantial loss in PS signal intensities (Figure 5), which is expected because of the higher MW range investigated. The resonances belonging to aliphatic protons (low frequency signals) undergo a much larger reduction in intensity compared with the aromatics (high frequency signals) due to shorter relaxation times (Table S5).

This difference is clearly shown in Table 5: the amount of signal left from PS changes depending on the parameter settings, but in every case, the reduction is more significant for the aliphatic region than the aromatic one. In almost 50% of all runs, the aliphatic signal left is less than 10%, and correspondingly, the percentage of aromatic signal left is not higher than 54%.

FIGURE 4 1 H NMR (600 MHz, CDCl3, 300 K) spectrum of polystyrene (PS) [molecular weight (MW) 629,500 Da, 5.0 wt%] with DMT (0.09 wt%) and TMB (0.12 wt%). DMT, dimethyl terephthalate; TMB, 1,3,5-trimethoxybenzene

<!-- image -->

FIGURE 5 1 H NMR (600 MHz, CDCl3, 300 K) spectra of polystyrene (PS) without (bottom spectrum) and with (top spectrum) the relaxation filter: (a) Mp 30,300 (10 wt%), (b) Mp 68,900 (5 wt%), (c) Mp 220,500 (5 wt%) and (d) Mp 629,500 (5 wt%)

<!-- image -->

The contour plots presented in Figure 6 confirm this trend: for example, a filter of 105.6 ms ( τ E = 440 μ s and n =120 cycles) leaves only 20% of polymer signal in the aliphatic region in comparison with 70% still present in the aromatic one (comparison between graphs a and c) for a polymer of approximately 350 kDa. Furthermore, 420 cycles lead to a very efficient reduction for the aliphatic region throughout the whole range of echo times (less than 25% signal left, Figure 6b). On the contrary, reaching the same result for the aromatic region requires 620 cycles and at least 1 ms of echo time (total echo time 620 ms, Figure 6d). In general, the best results (i.e., largest reduction in PS signal) are obtained when using high values of repetition and echo time; the recycle delay does not have a significant influence. The results of the ANOVA analysis are reported in Tables S6 and S7.

It is interesting to compare the effect of the T 2 filter on PEG and PS with the same MW. Figure 7 shows contour plots for both PEG and PS with an MW of 40 kDa, highlighting the influence of echo time and n on the percentage of polymer signal left. From this comparison, it can be inferred that a quite long relaxation filter is required for suppressing the signals belonging to PEG (top right region of Figure 7a), but even in this case, there is at least 60% of polymer left in the 1 H NMR spectrum. On the contrary, for PS, almost all combinations of echo time and repetitions deliver a minimum of 40% reduction in polymer signal, and a much better reduction can easily be achieved by choosing several combinations for the filter.

This difference in response between PEG and PS could be explained by considering the different flexibility of the two polymer chains. PEG is more flexible than PS, and this characteristic influences the viscosity of the solution and hence the relaxation properties as already seen. Solutions of polymers with more rigid molecular chains are expected to have higher viscosity than those with more flexible ones. Accordingly, the graphs reported in Figure 7 show that for PEG, a longer echo time in combination with a large number of repetitions (longer T 2 filter) are required to obtain a reduction in signals, which is in any case not so efficient as for PS. This result indicates that the relaxation filter can be used not only for facilitating the analysis of small molecules but also for having more information on the polymer flexibility and consequently on its possible applications, demonstrating once again the importance of relaxation measurements in polymer characterisation.

Analogously to the PEG case, SNR was measured for DMT and TMB resonances; only the SNR for H3 protons of TMB is reported in Table 5. It is important to underline that in all the measurements performed by applying the T 2 filter, the SNR ratio detected was much higher than 10 (Table S8), which is conventionally indicated as the limit of quantification (LOQ), [33] thus indicating that the detection and quantification of impurities could be performed even when their concentration is 50 times less than what was used for DMT and TMB in these experiments. This means that it is possible to quantify low MW compounds present in polymers in a concentration up to Abbreviations: DMT, dimethyl terephthalate; MW, molecular weight; PS, polystyrene; SNR, signal-to-noise ratio; TMB, 1,3,5-trimethoxybenzene.

TABLE 5 Responses for PS samples

|       | Factors   | Factors    | Factors   | Factors   | Factors   | Responses           | Responses               | Responses               | Responses                   |
|-------|-----------|------------|-----------|-----------|-----------|---------------------|-------------------------|-------------------------|-----------------------------|
| Run # | d1 (s)    | τ E ( μ s) | n         | MWPS(Da)  | PS wt%    | SNR H3 (decrease %) | PS area (signal left %) | PS area (signal left %) | DMT/TMB ratio (variation %) |
| Run # | d1 (s)    | τ E ( μ s) | n         | MWPS(Da)  | PS wt%    | SNR H3 (decrease %) | Arom                    | Aliph                   | DMT/TMB ratio (variation %) |
| 1     | 2         | 100        | 120       | 629,500   | 5         | 58.5                | 96.6                    | 73.5                    | - 3.2                       |
| 2     | 8         | 150        | 120       | 68,900    | 10        | 22.2                | 90.2                    | 61.7                    | 1.2                         |
| 3     | 10        | 300        | 520       | 68,900    | 7.5       | 34.0                | 45.4                    | 5.3                     | 1.2                         |
| 4     | 20        | 100        | 320       | 30,300    | 7.5       | 13.3                | 85.0                    | 46.8                    | 2.0                         |
| 5     | 2         | 400        | 320       | 220,500   | 7.5       | 43.3                | 51.0                    | 6.7                     | 4.3                         |
| 6     | 20        | 400        | 120       | 220,500   | 7.5       | 40.1                | 78.8                    | 31.4                    | - 1.3                       |
| 7     | 15        | 200        | 620       | 220,500   | 10        | 55.7                | 48.4                    | 5.8                     | 20.2                        |
| 8     | 10        | 350        | 320       | 629,500   | 7.5       | 37.5                | 53.9                    | 6.6                     | - 1.6                       |
| 9     | 2         | 550        | 620       | 629,500   | 5         | 70.1                | 20.1                    | 1.4                     | - 6.4                       |
| 10    | 20        | 600        | 320       | 30,300    | 10        | 46.5                | 38.3                    | 3.8                     | - 8.1                       |
| 11    | 10        | 640        | 520       | 220,500   | 7.5       | 55.0                | 18.3                    | 1.3                     | - 20.0                      |
| 12    | 10        | 200        | 420       | 220,500   | 5         | 44.3                | 64.2                    | 17.4                    | 2.7                         |
| 13    | 20        | 640        | 320       | 629,500   | 5         | 66.4                | 35.7                    | 3.0                     | - 5.0                       |
| 14    | 10        | 200        | 420       | 220,500   | 5         | 44.2                | 64.0                    | 17.3                    | 2.4                         |
| 15    | 20        | 400        | 120       | 220,500   | 7.5       | 35.8                | 77.3                    | 30.7                    | - 0.6                       |
| 16    | 8         | 640        | 120       | 30,300    | 5         | 33.7                | 70.2                    | 24.3                    | 1.3                         |
| 17    | 20        | 100        | 220       | 629,500   | 10        | 42.7                | 86.1                    | 43.6                    | - 5.2                       |
| 18    | 20        | 450        | 620       | 30,300    | 5         | 47.2                | 28.6                    | 2.6                     | 1.1                         |
| 19    | 2         | 100        | 620       | 30,300    | 7.5       | 17.8                | 73.1                    | 24.7                    | 8.0                         |
| 20    | 2         | 100        | 520       | 629,500   | 10        | 31.6                | 68.2                    | 16.0                    | 4.3                         |
| 21    | 20        | 100        | 620       | 629,500   | 5         | 46.3                | 71.2                    | 20.6                    | - 4.8                       |
| 22    | 20        | 600        | 620       | 629,500   | 10        | 64.4                | 11.4                    | 1.2                     | - 34.5                      |
| 23    | 10        | 640        | 520       | 220,500   | 7.5       | 49.9                | 18.4                    | 1.4                     | - 18.8                      |
| 24    | 20        | 100        | 620       | 220,500   | 5         | 40.8                | 71.4                    | 22.5                    | - 4.0                       |
| 25    | 15        | 640        | 220       | 68,900    | 7.5       | 40.3                | 47.6                    | 6.6                     | - 4.2                       |
| 26    | 10        | 350        | 320       | 629,500   | 7.5       | 37.0                | 53.4                    | 6.0                     | - 0.2                       |
| 27    | 2         | 400        | 320       | 220,500   | 7.5       | 40.2                | 50.9                    | 6.4                     | 3.7                         |
| 28    | 10        | 250        | 520       | 629,500   | 5         | 23.1                | 50.6                    | 7.1                     | 1.8                         |
| 29    | 2         | 550        | 620       | 30,300    | 10        | 38.3                | 19.0                    | 1.3                     | - 4.1                       |
| 30    | 2         | 640        | 120       | 629,500   | 10        | 41.8                | 59.9                    | 10.5                    | 4.0                         |
| 31    | 2         | 100        | 120       | 30,300    | 5         | 31.0                | 95.1                    | 75.9                    | 6.6                         |

20 mg/kg. This trend has been observed both for PEG and PS measurements.

ANOVA analysis on the SNR (Table S9) indicates that its decrease mainly depends on polymer MW (as already seen in PEG experiments) and echo time: those two factors are the only two main factors that are statistically significant ( p value &lt; 0.05). A minor loss in SNR will likely be obtained by using low values of echo time in combination with a low value of repetitions for cases when MW is lower than 120 kDa. It is worth to note that with a lower polymer MW, a longer relaxation filter is recommended ( τ E = 400 μ s, n = 320).

The variation in the DMT/TMB ratio, that is, the possibility of quantifying the small molecules after applying the relaxation filter, was kept within the reasonable boundaries of less than 5% in most of the experiments. The largest deviations (i.e., &gt;10%) in quantification were observed in the experiments where a long total echo time (&gt;600 ms) was used for analysing the highest MW samples (220,500 and 629,500 Da, runs 11, 22 and 23 with exception of run 7, which applied a shorter total echo time and is not considered further in the analysis due to its strongly deviating result). For these high MW polymers, very different dynamics are expected compared with the small molecules present; therefore, it is in general not necessary to increase the application of the filter to this extent. A total echo time &lt; 300 ms guarantees an error in quantification lower than 5%.

FIGURE 6 Contour plots of PS data: percentage of polymer signal left after the application of T 2 filter for (a and b) the aliphatic and (c and d) the aromatic regions; depending on τ E and MW according to the fitted response model for (a and c) n = 120, (b) n = 420 and (d) n = 620. MW, molecular weight; PS, polystyrene

FIGURE 7 Contour plots of (a) polyethylene glycol (PEG) and (b) polystyrene (PS) polymers with molecular weight (MW) 40 kDa; relaxation delay: 20 s (d1) + 2.7 s (acquisition time), polymer concentration 10 wt%

<!-- image -->

<!-- image -->

## 3.4 | Application to a commercial product

For testing the applicability of the T 2 filter on a real sample, we analysed a commercial polyacrylic dispersing agent (Dispex ™ N40) employed in water-borne systems where signals superimposition is expected. The polymer was dissolved in D2O with a final concentration of 15 wt%, as the study performed on PEG and PS indicated that a high polymer concentration contributes to better results after the application of the filter.

A standard 1 H NMR spectrum was recorded to select an appropriate internal standard based on the spectral profile of the sample. N , N -dimethylformamide (DMF) was chosen, whose methyl signals resonate at 2.94 and 2.78 ppm (Figure 8a). This proton spectrum shows already some low intensity and isolated signals from potentially low MW species, as well as a singlet centred at 1.84 ppm that suffers from a heavy superimposition (Figure S1).

Considering that the MW of the polymer is unknown, the total echo time was set to 420 ms, whereas the d1 was set to 15 s. Two different acquisitions were then performed aiming to better detect and quantify these components: a 1 H NMR spectrum with relaxation filter (Figure 8b), and as there is a considerable amount of water (the very intense singlet centred at 4.71 ppm), a 1 H NMR spectrum with relaxation filter and water presaturation (Figure 8c). It is worth to underline that presaturation should be used carefully in quantitative analysis as several factors may affect the accuracy of the results: proximity of the signals of interest to the suppressed spectral region, presence of labile protons which can exchange with the water ones, indirect saturation of small molecules resonances when interacting with the ones belonging to macromolecules affected by presaturation.

The analysis of the proton spectrum allowed the identification and quantification (Table 6) of the monomer sodium acrylate (set of signals between 6.10 and 5.50 ppm), in addition to isopropanol (CH at 3.94 ppm), methanol (CH3 at 3.27 ppm) and acetic acid (at 1.83 ppm), whose identities were confirmed by spiking the sample with reference compounds. The application of the T 2 filter contributed in reducing the polymer signal intensity and delivered a much-improved quantification of the small molecules present in the sample, especially in the case of acetic acid (overlapped singlet at 1.83 ppm). On the contrary, the presaturation did not improve the results.

The results reported in Table 6 are obtained by comparison of the integral area of the internal standard (DMF) with those of the small molecules, therefore without considering the differences in spin -lattice relaxation time that might occur among the compounds; as already mentioned, this difference can lead to an error in quantification. [29]

Therefore, in order to consider the T 1 contribution and to correct the concentration values calculated, the relaxation times of the small molecules (acetic acid, acrylate, isopropanol and methanol) and of the internal standard were measured (Table S11).

As reported in Table S11, DMF spin -lattice relaxation is comparable with the values measured for acetic acid and acrylate, thus making the quantitative analysis reported in Table 6 reliable for these two compounds. On the contrary, the two alcohols (isopropanol and methanol) have a longer relaxation than the internal standard, and this variation has to be considered in the quantitative analysis by using the equation reported by Bharti et al. [29] By applying this correction factor, the actual concentration for the two species doubles, being 0.01 wt% for methanol and 0.04 wt% for isopropanol.

FIGURE 8 1 H NMR (600 MHz, D2O, 300 K) spectra of Dispex ™ N40 (15 wt%) recorded (a) without T 2 filter, (b) with T 2 filter and (c) with T 2 filter and water presaturation

<!-- image -->

TABLE 6 Comparison of quantitative analysis of impurities obtained by analysing three independent replicates

| (CH 3 1.83 ppm)          |                  |                 |               |               |
|--------------------------|------------------|-----------------|---------------|---------------|
| acid wt%                 | (±4.5E-03)       |                 | (±1.5E-03)    | (±1.5E-03)    |
| wt% (CH 3 3.27 ppm)      | (±4.5E-03) 0.004 | 0.02 (±3.7E-03) | (±4.4E-04)    | (±4.4E-04)    |
| Isopropanol wt% (CH 3.94 | 0.02             | (±2.2E-03)      |               |               |
| Acetic                   |                  |                 |               |               |
|                          | 0.03             | 0.05            |               |               |
|                          |                  |                 | 0.05          | 0.05          |
|                          | (±6.2E-04)       | (±2.8E-04)      | (±1.7E-04)    | (±1.7E-04)    |
| Methanol                 |                  |                 |               |               |
| ppm)                     |                  | 0.005           | 0.005         | 0.005         |
| 5.94 ppm)                |                  |                 | 0.02          | 0.02          |
| wt% (CH                  |                  | (±4.5E-03)      | (±1.5E-03)    | (±1.5E-03)    |
|                          | 0.06             | 0.07            |               |               |
|                          |                  |                 | 0.07          | 0.07          |
| Acrylate                 |                  |                 |               |               |
|                          | (±8.1E-03)       |                 |               |               |
|                          | No               |                 |               |               |
|                          |                  | T               | +             | +             |
|                          |                  | 2               |               |               |
|                          |                  |                 | T 2           | T 2           |
|                          |                  |                 | filter        | filter        |
|                          |                  |                 | presaturation | presaturation |
| Experimental             |                  |                 |               |               |
|                          | filter           |                 |               |               |
|                          |                  | filter          |               |               |
| conditions               |                  |                 |               |               |

Note : Standard deviation is reported in parenthesis.

## 4 | CONCLUSIONS

The present study was performed with the aim of evaluating the influence of different parameters on the effectiveness of a T 2 relaxation filter, which was applied by means of the NMR CPMG pulse sequence, in enabling a reliable quantitative analysis of small molecules present in polymers. The results obtained on model systems (PEG and PS with MW spanning from 300 to 600,000 Da) confirmed that quantitative analysis could be performed, and more reliable results can be obtained where previously the polymer severely interfered with the measurement. The data collected highlight the sensitivity of the NMR technique, as relatively low concentrations of small molecules can be detected.

It can be concluded that quantitative analysis can be performed not only by using an internal standard but also with external standard methods (e.g., ERETIC in TopSpin or qEstimate in VnmrJ) as long as the viscosity of the solution is considered. Another important aspect to keep into consideration is the difference in T 1 and T 2 among the different species detected in the sample under analysis, which can affect the intensity of the integrated signals and hence the quantitative results. This problem can be overcome by measuring the relaxation parameters and then selecting the proper d1 for guaranteeing a complete recovery of the magnetisation for the small molecules analysed. Alternatively, the information on the relaxation properties can be used to apply a correction factor, for a reliable quantitative analysis even when short d1 are used.

The relaxation filter proved to work very well in removing resonances belonging to apolar polymers like PS, for which a polymer signal reduction of at least 80% is achieved. Polymer MW has a negligible influence on the analysed responses in the investigated range for PS (30,300 -629,500 Da) compared with the parameters directly affecting the length of the spin echo filter, namely, echo time and number of cycles. In the case of polar polymers like PEG (MW range investigated 300 -41,500 Da), the reduction is less efficient; the longest relaxation delays used (viz., 12.7 and 17.7 s) and a total echo time of at least 300 ms guarantee the highest signal reduction for the polymers analysed. This different outcome could, in first instance, simply be attributed to the lower MW of the PEG samples investigated, which are expected to respond less to the application of the filter. If this is the case, a longer total echo time is needed to suppress the polymer signal(s), and the CPMG pulse sequence can be replaced with PROJECT or WASTED pulse sequences, in cases when long T2-filter times cannot be achieved safely by the CPMG pulse sequence. [34,35] It is worth to mention that, even in the case that other pulse sequences are more suitable, a multivariate approach similar to the one used here can be followed for selecting a range of optimal parameters.

When the two polymers are analysed at the same MW, there is still a difference predicted in reduction of polymeric signal, which can be mainly explained by the difference in motion between the two polymers. The loss in SNR for the small molecules can be minimised depending on the polymer MW. When very high MW polymers are analysed (as observed for PS), it is recommended to use a quite short total echo time, which will also allow a good reduction in polymer signal. In the case of intermediate MW polymers (PEG), the relative values of echo time and number of cycles proved to be as critical as the length of the total echo time. In particular, when analysing a polymer whose MW is at least equal to 26 kDa, it is recommended to use a total echo time between 190 and 380 ms, being careful in properly choosing the values of τ E and n.

The DoE-based approach yielded good data on the influence of the investigated parameters on the analysed responses and helped in reducing the number of experiments. Without this multivariate approach, the analysis of all the parameters selected and their levels would have required a much higher number of experiments and consequently significantly more experimental time.

## ACKNOWLEDGEMENTS

This project has received funding from the European Union's Horizon 2020 research and innovation programme under the H2020 Marie Sk ł odowska-Curie Grant agreement 749083. The authors thank Dr Bogdan Ibanescu from AkzoNobel Decorative Paints (Slough, UK) for his contribution in setting up the Design of Experiments.

## ORCID

Federica Aiello Paulo Dani

## REFERENCES

- [1] A. A. Parker, A. A. Parker consulting and product development, , 2008 .
- [2] W. Buchberger, M. Stiftinger, in Mass Spectrometry of Polymers -New Techniques , Vol. 248, (Ed: M. Hakkarainen), Springer, Berlin, Heidelberg 2011 , 39.
- [3] R. K. Malcolm, P. J. Boyd, C. F. McCoy, D. J. Murphy, Adv. Drug Delivery Rev. 2016 , 103 , 33.
- [4] S. Masi, A. Rizzo, F. Aiello, F. Balzano, G. Uccello-Barretta, A. Listorti, G. Gigli, S. Colella, Nanoscale 2015 , 7 , 18956.
- [5] Y. Li, C. Gu, J. Gruenhagen, K. Zhang, P. Yehl, N. P. Chetwyn, C. D. Medley, J. Chromatogr. A 2015 , 1393 , 81.
- [6] X. Huang, C. S. Brazel, J. Controlled Release 2001 , 73 , 121.
- [7] K. J. Cash, F. Ricci, K. W. Plaxco, J. Am. Chem. Soc. 2009 , 131 , 6955.
- [8] E. A. Rössler, S. Stapf, N. Fatkullin, Curr. Opin. Colloid Interface Sci. 2013 , 18 , 173.
- [9] H. M. Jensen, F. H. Larsen, S. B. Engelsen, Methods Mol. Biol. 2015 , 1308 , 347.
- [10] A. Adams, TrAC, Trends Anal. Chem. 2016 , 83 , 107.
- [11] H. W. Spiess, Macromolecules 2017 , 50 , 1761.
- [12] M. Oouchi, J. Ukawa, Y. Ishii, H. Maeda, Biomacromolecules 2019 , 20 , 1394.
- [13] B. Davis, in Protein-Ligand Interactions: Methods and Applications , (Eds: M. A. Williams, T. Daviter), Humana Press, Totowa, NJ 2013 , 389.
- [14] S. Maity, R. K. Gundampati, T. K. Suresh Kumar, Nat. Prod. Commun. 2019 , 14, 1934578X19849296.
- [15] M. Pellecchia, Chem. Biol. 2005 , 12 , 961.
- [16] P. A. Mirau, A Practical Guide to Understanding the NMR of Polymers , Wiley-Interscience 2005 .
- [17] H. Tang, Y. Wang, J. K. Nicholson, J. C. Lindon, Anal. Biochem. 2004 , 325 , 260.
- [18] P. Groves, Polym. Chem. 2017 , 8 , 6700.
- [19] G. Pagès, V. Gilard, R. Martino, M. Malet-Martino, Analyst 2017 , 142 , 3771.
- [20] A. Macchioni, G. Ciancaleoni, C. Zuccaccia, D. Zuccaccia, in Supramolecular Chemistry , (Eds: P. A. Gale, J. W. Steed), John Wiley &amp; Sons Inc., Hoboken, NJ 2012 .
- [21] E. L. Hahn, Phys. Rev. 1950 , 80 , 580.
- [22] H. Y. Carr, E. M. Purcell, Phys. Rev. 1954 , 94 , 630.
- [23] S. Meiboom, D. Gill, Rev. Sci. Instrum. 1958 , 29 , 688.
- [24] L. B. Pratima Tripathi, R. Saxena, S. K. Yachha, R. Roy, C. L. Khetrapal, J Gastrointestin Liver Dis 2009 , 18 , 7.
- [25] J. Wallmeier, C. Samol, L. Ellmann, H. U. Zacharias, F. C. Vogl, M. Garcia, K. Dettmer, P. J. Oefner, W. Gronwald, J. Proteome Res. 2017 , 16 , 1784.
- [26] K. Skidmore, D. Hewitt, Y.-H. Kao, Biotechnol. Prog. 2012 , 28 , 1526.
- [27] C. Gayathri, N. V. Tsarevsky, R. R. Gil, Chem. -Eur. J. 2010 , 16 , 3622.
- [28] Q. N. Van, G. N. Chmurny, T. D. Veenstra, Biochem. Biophys. Res. Commun. 2003 , 301 , 952.
- [29] S. K. Bharti, N. Sinha, B. S. Joshi, S. K. Mandal, R. Roy, C. L. Khetrapal, Metabolomics 2008 , 4 , 367.
- [30] K. Alex, A. M. Michael, P. Stephen, in 7th International Conference on Energy Efficiency in Domestic Appliances and Lighting (EEDAL'13).
- [31] K.-C. Mei, Y. Guo, J. Bai, P. M. Costa, H. Kafa, A. Protti, R. C. Hider, K. T. Al-Jamal, ACS Appl. Mater. Interfaces 2015 , 7 , 14176.
- [32] O. A. Mohamed, S. H. Masood, J. L. Bhowmik, M. Nikzad, J. Azadmanjiri, J. Mater. Eng. Perform. 2016 , 25 , 2922.
- [33] S. Sun, M. Jin, X. Zhou, J. Ni, X. Jin, H. Liu, Y. Wang, Molecules 2017 , 22 , 1517.

- [34] J. A. Aguilar, M. Nilsson, G. Bodenhausen, G. A. Morris, Chem. Commun. 2012 , 48 , 811.
- [35] J. A. Aguilar, J. Cassani, F. Probert, J. Palace, T. D. W. Claridge, A. Botana, A. M. Kenwright, Analyst 2019 , 144 , 7270.

## SUPPORTING INFORMATION

Additional supporting information may be found online in the Supporting Information section at the end of this article.

How to cite this article: Aiello F, Gerretzen J, Simons MG, Davies AN, Dani P. A multivariate approach to investigate the NMR CPMG pulse sequence for analysing low MW species in polymers. Magn Reson Chem . 2020;1 -15.