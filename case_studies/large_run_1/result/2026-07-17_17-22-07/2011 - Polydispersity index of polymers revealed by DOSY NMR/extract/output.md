See	discussions,	stats,	and	author	profiles	for	this	publication	at:	https://www.researchgate.net/publication/273661066

## [Polydispersity	index	of	polymers	revealed	by DOSY	NMR.](https://www.researchgate.net/publication/273661066_Polydispersity_index_of_polymers_revealed_by_DOSY_NMR?enrichId=rgreq-07ef597b2de148fa652958560d67c3b4-XXX&enrichSource=Y292ZXJQYWdlOzI3MzY2MTA2NjtBUzoyMDc5ODQxMzYzMzEyNjRAMTQyNjU5ODY5MDE1Nw%3D%3D&el=1_x_3&_esc=publicationCoverPdf)

Data ·	March	2015

<!-- image -->

<!-- image -->

Contents lists available at ScienceDirect

## Journal of Magnetic Resonance

[j o u r n a l homepage: www.elsevier.com/locate/jmr](http://www.elsevier.com/locate/jmr)

## Polydispersity index of polymers revealed by DOSY NMR

Justine Viéville a,b , Matthieu Tanty a,b , Marc-André Delsuc a,b, ⇑

- a

Institut de Génétique et de Biologie Moléculaire et Cellulaire (IGBMC), UMR 7104, 1 rue Laurent Fries, BP 10142, 67404 Illkirch cedex, France b NMRTEC, Bioparc B, boulevard Sébastien Brant, 67400 Illkirch, France

## a r t i c l e i n f o

Article history: Received 17 May 2011 Revised 22 June 2011

Available online 1 July 2011

Keywords: Polymer Polydispersity DOSY Fractal dimension Inverse Laplace transform

## 1. Introduction

Polymers are characterized by a distribution of molecular masses. For linear polymers this distribution can be expressed in terms of average chain length and polydispersity of the chain length. The average chain length is routinely measured by NMR spectroscopy by measuring the ratio of the integrals of the main chain signal to the extremity signals.

Self-diffusion, measured by pulsed field gradient NMR (PFGNMR) is sensitive to molecular size and provides an approach to the determination of the distribution of molecular mass. In the case of linear polymer chains, the diffusion coefficient is linked to the molecular mass through the following equation:

$$M \circ D ^ { - d _ { J } } & & ( 1 ) & \quad \text {chain is}$$

where D is the diffusion coefficient of the molecule, M its mass and df its fractal dimension [1-3]. The fractal dimension is a measure of the way the chain extends into the solvent, and is equal to the inverse of the Flory coefficient m : df = 1/ m . It is comprised between 5/3 and 3 [4].

The effect of polydispersity on PFGNMR measurements has already been well studied [5-7] and is known to lead to non exponential decays, even for weak polydispersity [8]. The analysis of non exponential decays requires the use of Inverse Laplace Trans-

⇑ Corresponding author at: Institut de Génétique et de Biologie Moléculaire et Cellulaire (IGBMC), UMR 7104, 1 rue Laurent Fries, BP 10142, 67404 Illkirch cedex, France. Fax: +33 (0)3 68 85 47 18.

E-mail addresses: vieville@igbmc.fr, justine.vieville@nmrtec.com (J. Viéville), tanty@igbmc.fr (M. Tanty), delsuc@igbmc.fr (M.-A. Delsuc).

## a b s t r a c t

The polydispersity of a polymer chain is usually measured by its polydispersity index (PDI). In this study we present a method which allows to estimate the PDI of linear polymers from a simple diffusion experiment.

The approach is based on the differential diffusion profile observed for the main polymer chain signal versus the extremity signal. From this difference, a statistical analysis of the DOSY spectrum allows the PDI to be estimated accurately, to the condition that the Flory coefficient of the polymer chain is known. Alternatively, the mass average molar mass Mw and the number average molar mass Mn can be extracted separately from the same spectrum.

Results on PEO mixes reveal that, using this new method, PDI can be estimated with a very good accuracy. This method can easily be applied to almost any kind of linear polymers.

Ó 2011 Elsevier Inc. All rights reserved.

form (ILT) in order to estimate the molecular mass distribution. This is an ill-posed mathematical problem, to which an approximate solution can only be constructed. This was investigated by Chen et al. using the CONTIN algorithm [1], but due to the approximate reconstruction, it is not possible to extract a useful value of the polydispersity index from this approach.

Polydispersity is commonly measured by the polydispersity index (PDI). For a given polymer sample, it is defined as the ratio of the mass average molar mass ( Mw ) to its number averaged molar mass ( Mn )

$$\lim _ { \text {linked} } \ P D I = \frac { M _ { w } } { M _ { n } }$$

For a homopolymer linear chain, assuming that the mass of the chain is equal to the product of its length by the mass of the monomeric unit M , the average molecular masses Mn and Mw expressions are given in Eqs. (3) and (4),

P

$$\text {measure of} \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$\lim _ { \text {has al-} } \quad M _ { w } = \frac { \sum m _ { i } M _ { i } } { \sum m _ { i } } = \frac { \sum n _ { i } M _ { i } ^ { 2 } } { \sum n _ { i } M _ { i } }$$

where ni is the number of molecules of mass Mi , mi the mass of molecules of mass Mi , and N the averaged chain length.

Mn and Mw are statistical features of the same polymer distribution but with different weightings. Because of this difference, Mw is always greater than or equal to Mn , and PDI is always greater than or equal to 1.

NMR parameters are also obtained as statistical average on the whole sample. Signals measured from the extremity of the chain are weighted by the number of molecules, while signals measured on the whole polymer chain, extremities included, are weighted by mass of the molecules. Thus, the two different weightings used for defining Mn and Mw can be observed in NMR, depending on the measure being performed either on the extremities or on the whole polymer chain.

<!-- image -->

This property applies also to PFGNMR measurement of diffusion coefficients. From Eqs. (1) and (2), it is thus possible to express PDI as follows:





$$P D I = \left ( \frac { \langle D _ { w } \rangle } { \langle D _ { n } \rangle } \right ) ^ { - d _ { f } } & & ( 5 ) & & \ F i g . \\$$

where h Dn i is the mean diffusion coefficient measured from the ILT analysis of the PFGNMR signal of the extremity units, and h Dw i the mean diffusion coefficient measured for the whole polymer.

From this theoretical presentation, it appears that the polydispersity index can be determined from a simple PFGNMR measurement, by comparing the signals originated from the main chain to the signal of the extremities, and applying Eq. (5), given the preliminary knowledge of fractal dimension of the chain.

To confirm this hypothesis, 2D-DOSY spectra were registered for different mixes of poly-ethyleneoxide (PEO) in water with calibrated chain lengths and PDIs. Experimental values were confronted to theoretical ones.

## 2. Results and discussion

## 2.1. 1D NMR

The 1D- 1 H NMR spectrum of mix L is shown in Fig. 1. Very few peaks are observed and are easily assigned. Besides the resonance at 3.7 ppm of the principal chain, other resonances are observed. Four different spin systems can be identified. The signal A corresponds to the chain methylene group, and the signal B to the pen- ultimate methylene. The signal C corresponds to the signal assigned to the terminal methylene group bearing the hydroxy function, and last signals D and E show the 13 C-satellites of the chain protons. As one can see on this example, protons on the PEO's extremities are clearly identified. It is the case for all the mixes which makes the calculation of the average chain length N always possible.

## 2.2. The DOSY experiment

Fig. 2 shows the NMR signal decay for signals A and C from PEO mix L versus the square of the gradient strength. Both curves are columns extracted respectively at 3.69 ppm and 3.63 ppm, from the diffusion experiment performed on mix L after Fourier transform and baseline correction. As expected, being obtained from a quite polydisperse sample (here PDI = 2.51) both curves present a strong non-exponential decay, as can be seen from the non-linearity of the log-plot. The ILT analysis of the decays produces a DOSY spectra with peaks broaden along the diffusion axis. However, despite this broadening, this experiment reveals two different diffusion regimes. Due to marked difference in the diffusion coefficients, the 2D-DOSY spectrum displayed in Fig. 3 unequivocally confirms that two different diffusion profiles can be extracted. In this example, the DOSY peak summit measured for the extremity was found to be D = 1.83 -10 3 l m 2 s  1 , whereas the DOSY peak summit measured for the chain was found to be D = 1.11 -10 3 l m 2 s  1 .

It should be noted that the measure relies on the complete measurement of all the different polymers present in the sample. In consequence, the PFG experiment should be designed to allow a signal attenuation from the longest chains, sufficient for a correct measurement of their diffusion coefficient. In the present case, all experiments have been performed in the same conditions, optimized on the largest monodisperse polymer studied. However, when the composition of the mix is unknown, one should use large enough PFG intensities to ensure the signal attenuation of the heaviest polymers. As a rule of thumb, a final attenuation around 10% on a monodisperse species is usually required to permit a precise determination of the diffusion coefficient. Thus, when studying an unknown polydisperse polymer, one should try to reach at least a 1% attenuation for the main signal.

Fig. 1. 1D- 1 H NMR spectrum of a poly-ethyleneoxide in D2O, mix L. Assignment is given in inset, D and E are the 13 C satellites of A.

<!-- image -->

Fig. 2. Log-plot of the observed decays for varying gradient values squared for mix L. Diamonds are from the signal of the main chain (signal A Fig. 1), dots are from the signal of the extremity (signal C).

<!-- image -->

Table 1 Experimental results compared to theoretical values.

|         | N     | N    | PDI   | PDI   | M n (g mol  1 )   | M n (g mol  1 )   | M w (g mol  1 )   | M w (g mol  1 )   |
|---------|-------|------|-------|-------|-------------------|-------------------|-------------------|-------------------|
| PEO mix | Theo  | Exp  | Theo  | Exp   | Theo              | Exp               | Theo              | Exp               |
| Mix A   | 36.3  | 36.1 | 1.04  | 1.06  | 1615              | 1588.4            | 1679.6            | 1683.7            |
| Mix B   | 49.4  | 53.7 | 1.07  | 1.08  | 2190              | 2362.8            | 2343.3            | 2551.8            |
| Mix C   | 107.5 | 120  | 1.11  | 1.12  | 4750              | 5280              | 5272.5            | 5913.6            |
| Mix D   | 8.7   | 8.7  | 1.12  | 1.12  | 400.6             | 382.8             | 447.5             | 428.7             |
| Mix E   | 8.8   | 9.5  | 1.14  | 1.17  | 403.4             | 418               | 459.7             | 489.1             |
| Mix F   | 23    | 23.8 | 1.26  | 1.31  | 1021              | 1047.2            | 1268.3            | 1371.8            |
| Mix G   | 71.5  | 85.3 | 1.28  | 1.28  | 3165              | 3753.2            | 4051.2            | 4804.1            |
| Mix H   | 44.8  | 47.5 | 1.34  | 1.15  | 1989.3            | 2090              | 2518              | 2403.5            |
| Mix I   | 34.7  | 37   | 1.54  | 1.5   | 1544.3            | 1628              | 2382.7            | 2442              |
| Mix J   | 38.1  | 39.8 | 2.01  | 2.2   | 1696.9            | 1751.2            | 3238.5            | 3852.6            |
| Mix K   | 15.7  | 15.9 | 2.12  | 1.89  | 710.3             | 699.6             | 1332.1            | 1322.2            |
| Mix L   | 19.1  | 19.4 | 2.51  | 2.24  | 858.5             | 853.6             | 2008.2            | 1912.1            |
| Mix M   | 21.4  | 24.8 | 3.3   | 2.41  | 961.7             | 1091.2            | 3062.8            | 2629.8            |
| Mix N   | 22.4  | 23.8 | 3.41  | 2.75  | 1001.7            | 1047.2            | 3328              | 2879.8            |
| Mix O   | 13.5  | 13.9 | 5.23  | 4.48  | 611.3             | 611.6             | 3099.6            | 2740              |

Mega-dalton polymers have already been precisely measured on standard spectrometers [3]. So, the main size limitation for the application of this technique is the possibility to reliably detect signals from the chain extremities. Of course, this is more difficult to achieve on large polymers, as the extremity signals might be too faint to be observed. This was done here for PEO polymers up to 10 kDa, despite the fact that this signal only integrates as a CH2.

The method requires that the extremity of the polymer presents an isolated signal in the NMR spectrum. This condition is not really stringent. On the PEO samples, the small shift of 0.08 ppm observed between the chain and the extremity signals, is sufficient for the study. Given this shift difference, two different diffusion coefficient distributions can be extracted by ILT from one 2D-DOSY spectrum. By integrating over the regions displayed in Fig. 3, the barycenters of these distributions are calculated to estimate the PDI.

Fig. 3. 2D-DOSY spectrum of mix L. The black rectangle on the right is the region over which the integration is made to determine h Dn i . h Dw i is determined by integration over the whole spectral range shown by outer red rectangle. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

<!-- image -->

Fig. 4. Correlations curves for the average chain length N (left) and the PDI (right). Red lines correspond to theo = exp . The PDI was computed with the fractal dimension value df = 1.86 (blue square); df = 1.96 (upper bar); and df = 1.76 (lower bar). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

<!-- image -->

## 2.3. Comparison to theoretical values

Table 1 gathers the expected and measured values of N and PDI for all the different analyzed PEO mixes and Fig. 4 shows the comparison between the theoretical and measured values of N and PDI. The very good correlation between theory and measurement indicates that the quality of the method.

The value of the fractal dimension df is the only free parameter which is needed to extract the PDI for the 2D-DOSY spectrum. From the Flory theory, it is predicted to be 5/3 and 3 for fully solvated and collapsed polymer chains, respectively [4]. In a h solvent, where polymer-polymer interactions are equal to polymer-solvent and solvent-solvent interactions, the polymer behaves as a Gaussian chain and the exponent df is predicted to be 2.

Results presented here have been obtained with a df value of 1.86, as was determined by several studies [3,9]. Are also added in Fig. 4, points showing the impact of varying the df values. It can be observed that while an error on this value may have an impact on the PDI accuracy, this impact is not very important.

## 3. Conclusion

Wehave shown that DOSY NMR can bring valuable information on polydisperse polymers. With the proposed approach the polydispersity index as well as average chain length can readily be determined for linear polymers. To assess the polydispersity index from the 2D-DOSY spectra, the barycenter of diffusion peak is calculated, this is made possible here thanks to the ILT analysis of the DOSY signal, which conserves the properties of the polymer distribution [7]. With this approach, results are independent of the average chain length and only the fractal dimension of the polymer chain df must be known. Experimental average chain length and polydispersity index did not indicate significative difference when compared to supplier data. This technique was shown to equally reliable and accurate for both high (5.23) and low (1.04) polydispersity indexes. This method requires a separate NMR proton sig- nal for the extremity of the studied polymer to be observed. However this condition is not stringent, as it was easily fulfilled here in the case of PEO, where only 0.08 ppm separates both signals. It will be easily extended to polymers with different extremity chemical patterns (for example, a methyl- or amide-group). Moreover, in the case of very large polymers with low extremities signals, a chemical modification of the extremities will allow the use of the method presented here.

Compared to other PDI determination technique such as Mass Spectrometry or Size Exclusion Chromatography, this approach presents the unique advantage of a direct measure which does not require any interaction with a static phase, separation, ionization or dilution of the polymer. It does not require any special calibration, equipment, or preparation and is a rapidly obtained with a diluted polymer sample. NMR as always been a powerful spectroscopy for the study of polymers, with DOSY NMR and the proposed procedure, the range of the physico-chemical parameters which can be accessed by NMR is further extended.

## 4. Experimental

## 4.1. Sample preparation

A set of 17 PEO standards, with masses ranging from 106 Da to 10,730 Da were purchased from American Polymer Standards Corporation (Mentor, OH, USA). Each standard has been dissolved in Milli-Q water to 10% (w/v) solutions. These solutions were used to create 15 mixes with controlled PDI from 1.04 to 5.23 and a concentration range from 0.05% to 1% (w/v). Each mix contains 10% D2O (v/v) and 1% (v/v) of a 1 mM DSS (4,4-dimethyl-4-silapentane-1-sulfonic acid) aqueous solution. The details of the 17 standard PEO as well as the 15 mixes are given in the Supplementary materials.

## 4.2. NMR spectroscopy

1D- 1 H and 2D-DOSY experiments were carried out on each PEO mix at 298 K on a 500 MHz Bruker Avance I NMR spectrometer employing a 5 mm TXI probe equipped with z -gradients delivering up to 53 G/cm.

1D- 1 H experiments were obtained with presaturation of water, 128 scans of 16k data points, and recycle time of 6.1 s. Fourier transform was applied with zerofilling and 0.5 Hz exponential broadening. Careful spline polynomial correction was applied to each 1D- 1 H spectra before integration.

2D-DOSY experiments were acquired using a LED experiment with bipolar pulses [10] and water presaturation. Gradients were linearly sampled from 0.5 G/cm to 45.7 G/cm in 40 points. Thirtytwo scans were acquired on 16k data points, for a total acquisition time of 1 h and 7 min.

The gradient pulse length was d /2 = 1.5 ms and the D diffusion delay was adapted to the sample for values in the 100-180 ms range. The DOSY spectra were obtained by applying an Inverse Laplace Transform (ILT) along the diffusion axis, using the Gifa algorithm [11,12] embedded into the commercial software NMRnotebook (NMRTEC, Illkirch). Careful spline polynomial correction was applied along the F2 dimension before the ILT processing, which was computed on 256 points, using the highest quality available in the algorithm.

## 4.3. Average chain length determination

For each 1D- 1 H spectrum, peaks corresponding to extremity CH2 protons and chain CH2 protons were integrated. There are four protons at the extremities and 4 N  4 protons inside the chain, where N is the number of monomeric units in the polymer chain. The ratio of both integrals allows the average chain length N to be extracted.

## 4.4. PDI determination

For a given sample, the diffusion coefficient distributions given by the 2D-DOSY spectrum were studied over ranges of chemical shift intervals. Mean diffusion coefficients were computed as a barycenter along the diffusion axis by integrated over determined spectral regions of the 2D spectrum. h Dn i was computed as the mean diffusion coefficients measured over the chemical shifts corresponding to the extremity of the chain. h Dw i should be evaluated over the whole polymer chain, thus the averaging was performed over a range of chemical shifts, encompassing all polymer signals, main chain and extremities included.

PDI was then obtained using Eq. (5), using a value of df equal to 1.86 [3,9]. From the average chain length N , the number average molecular mass Mn was computed using Eq. (3), from the values of PDI and Mn , the mass average molecular mass was determined from Mw = PDI Mn .

All the experimental values are given in Table 1. The complete procedure has been programmed into a python script, which can be embedded as a macro into the NMRnotebook software. The python script of this macro is available in the Supplementary materials.

## Acknowledgments

The authors want to thank Marie-Aude Coutouly for her help in developing the NNB macro. J.V. and M.T. also acknowledge NMRTEC for financial support.

## Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at doi:10.1016/j.jmr.2011.06.020.

## References

- [1] A. Chen, D. Wu, C. Johnson, Determination of molecular-weight distributions for polymers by diffusion-ordered NMR, J. Am. Chem. Soc. 117 (1995) 79657970.
- [2] D.K. Wilkins, S.B. Grimshaw, V. Receveur, C.M. Dobson, J.A. Jones, L.J. Smith, Hydrodynamic radii of native and denatured proteins measured by pulse field gradient NMR techniques, Biochemistry 38 (1999) 16424-16431.
- [3] S. Augé, P.-O. Schmit, C.A. Crutchfield, M.T. Islam, D.J. Harris, E. Durand, M. Clemancey, A.-A. Quoineaud, J.-M. Lancelin, Y. Prigent, F. Taulelle, M.-A. Delsuc, NMR measure of translational diffusion and fractal dimension. Application to molecular mass measurement, J. Phys. Chem. B 113 (2009) 1914-1918.
- [4] P. Flory, Principles of Polymer Chemistry, Cornell University Press, Ithaca, NY, 1953.
- [5] E.V. Meerwall, Interpreting pulsed-gradient spin-echo diffusion experiments in polydisperse specimens, J. Magn. Reson. 50 (1982) 409-416.
- [6] P.T. Callaghan, D.N. Pinder, A pulsed field gradient NMR study of self-diffusion in a polydisperse polymer system: dextran in water, Macromolecules 16 (1983) 968-973.
- [7] P. Callaghan, D. Pinder, Influence of polydispersity on polymer self-diffusion measurements by pulsed field gradient nuclear magnetic-resonance, Macromolecules 18 (1985) 373-379.
- [8] G. Fleischer, The effect of polydispersity on measuring polymer self-diffusion with the NMR pulsed field gradient technique, Polymer 26 (1985) 1677-1682.
- [9] K. Chari, B. Antalek, J. Minter, Diffusion and scaling behavior of polymersurfactant aggregates, Phys. Rev. Lett. 74 (1995) 3624-3627.
- [10] D. Wu, A. Chen, C. Johnson, An improved diffusion-ordered spectroscopy experiment incorporating bipolar-gradient pulses, J. Magn. Reson. Ser. A 115 (1995) 260-264.
- [11] M.-A. Delsuc, T. Malliavin, Maximum entropy processing of DOSY NMR spectra, Anal. Chem. 70 (1998) 2146-2148.
- [12] D. Tramesel, V. Catherinot, M.-A. Delsuc, Modeling of NMR processing, toward efficient unattended processing of NMR experiments, J. Magn. Reson. 188 (2007) 56-67.