<!-- image -->

Polymer Calibration

## Research Articles

<!-- image -->

How to cite: Angew. Chem. Int. Ed. 2022, 61, e202114536 International Edition:

German Edition:

## Solvent-Independent Molecular Weight Determination of Polymers Based on a Truly Universal Calibration

Pieter-Jan Voorter, Alasdair McKay, Jinhuo Dai, Olga Paravagna, Neil R. Cameron, and *

Abstract: Diffusion-ordered NMR spectroscopy (DOSY) allows for accurate molecular weight calibration and determination that can be corrected for solvent influences. Polystyrene and poly(ethylene glycol) standards have been used to calibrate DOSY diffusion data for a variety of solvents, showing a high correlation of data when the bulk viscosity of the solvent is accounted for following the Stokes-Einstein equation. In this way, a type of universal calibration is introduced that allows for determinations of average molecular weight that are at least as accurate as those of traditional size-exclusion chromatography (SEC), if not better. Further, we demonstrate that DOSY calibrations can be used between laboratories, hence removing the need for individual calibration of setups as currently done.

## Introduction

The gold standard of molecular weight determination of polymers around the globe is size-exclusion chromatography (SEC). [1] It is hard to imagine a state-of-the-art polymer chemistry facility without access to SEC, simply because of the basic need to characterize a polymer with respect to its size. It is easy to see why SEC is so prominent: It is overall a reliable technique, runs with reasonable operation cost, and provides comprehensive and accurate molecular weight distribution data. Almost no other characterization method is able to provide a similar level of information, or so it seems. Certainly, this is true when it comes to the determination of the shape of a molecular weight distribution. Even complex mixtures of polymers can be analyzed, and when combined with a second chromatographic dimension an incredible wealth of information is obtained. [2] Yet,

[*] P.-J. Voorter, A. McKay, Prof. T. Junkers Polymer Reaction Design Group, School of Chemistry Monash University 19 Rainforest Walk, Building 23, Clayton, VIC 3800 (Australia) E-mail: tanja.junkers@monash.edu Dr. J. Dai, Dr. O. Paravagna Dulux Australia 1956 Dandenong Road, Clayton, VIC 3168 (Australia) Prof. N. R. Cameron Department of Materials Science and Engineering Monash University 22 Alliance Lane, Clayton, Victoria, 3800 (Australia) and School of Engineering University of Warwick. Coventry CV4 7AL (UK)

Angew. Chem. Int. Ed. 2022 , 61 , e202114536 (1 of 5)

its primary purpose is often the determination of simple average molecular weight information. One might think that a technique that is so powerful in determining weight distributions should also be evenly powerful in providing average molecular mass information. Yet, this is not the case. SEC-depending on the detectors used-is actually not very accurate when it comes to absolute molecular weight determination. Unless an absolute method such as multi-angle laser light scattering (MALLS) is additionally employed (which comes with its own benefits and drawbacks), [3] SEC can be highly inaccurate. [4]

Most of the time, the concept of universal calibration is employed to calibrate SEC instruments. [5] Universal calibration refers here to the universal relation between hydrodynamic volume HV and retention time (or volume) on a given set of columns. HV can be related to the molecular weight of an analyte via its intrinsic viscosity [ η ], which can be either measured directly, or be determined via a simple scaling law, the Mark-Houwink-Kuhn-Sakurada (MHKS) relation (1) (where K and a are arbitrary parameters): [1]

$$\text {use of} \quad [ \eta ] = K M ^ { a } & & ( 1 )$$

Thus, if a system is calibrated with a set of standards with known intrinsic viscosity, any other polymer can be measured as well. However, even if one assumes that this concept is fully valid (which is not necessarily the case), it still ignores that flow rates and temperatures may fluctuate, chromatography columns age and that solvent quality isn't perfectly constant. More severely, the relation between intrinsic viscosity and molecular weight is in the majority of cases not known due to a lack of K and a values being available. SEC is often regarded, even under perfect calibration conditions, to be not more accurate than 1020% (and often enough much less accurate) [6] relative error when measurements of the same sample are compared between different instruments and column sets. [7] On a single given instrument, the repeatability of a mass determination may be better, but this only leads to the erroneous conclusion of a perceived precision that is not really present. [7] Considering that the 10-20% error applies for reasonably well calibrated instruments, for polymers that behave ideally with respect to coil dynamics and solubility and for cases where MHKS parameters are known, it can be safely assumed that the actual precision of determination is often even significantly lower. Almost all SECs operating in apolar solvents rely on polystyrene calibration, accepting that application to any other polymer is inherently difficult.

GDCh

<!-- image -->

It is for this reason that in many publications elugrams rather than molecular weight distributions are shown, exactly because researchers are aware that the apparent molecular weights that the SEC software produces are not necessarily true, or even very wrong. [8] Often enough, though, in an attempt to report an average molecular weight, researchers apply the universal calibration principle despite knowing its shortcomings.

As mentioned above, MALLS presents a solution to the above described dilemma when operated as a detector in SEC or as a stand-alone measurement method. [1, 3] However, MALLS is prone to yield erroneous results if data analysis is not treated with the highest care and requires specialist knowledge to be carried out correctly. Without precise knowledge of the refractive index increment and a critical assessment of Zimm plots, results with very substantial systematic errors may be derived, let alone that the number of angles detected in a light scattering device directly correlates with the precision of the measurement. As a consequence, many laboratories do not have access to MALLS, or do not use it as a routine methodology. Other methods include viscosity measurements, but these are also quite indirect and prone to calibration errors. Interestingly, NMR might be able to show a way out of this dilemma. NMR is reliable, non-invasive and typically available in all modern synthetic chemistry laboratories. NMR can provide molecular weight information via integration of signal intensities of polymer end groups, but this approach only works reliably for low molecular weights where end group peaks have significant intensities. [9] Much more accurate and applicable to a broad mass range is diffusion ordered spectroscopy (DOSY). [10] DOSY allows the determination of the diffusion coefficient of a species with high accuracy. Several groups have shown previously that this can be used to perform a molecular weight calibration, and hence to use DOSY as a tool to determine average molecular weights of polymers. [10,11] The method is, however, not widely used yet, despite its inherently powerful and simple determination. Interestingly, to the best of our knowledge, DOSY has to date only been used with direct calibrations, hence standards of a given molecular weight are required to determine the molecular weight of an analyte relative to the molecular weight standards. [6]

Herein we demonstrate that DOSY is an accurate method to determine polymer average molecular weights, competing favorably with SEC. Further, we demonstrate that even if a standard calibration is applied to a very different type of polymer, a reasonable estimate of molecular weight is made with an accuracy that at least rivals SEC. Figure 1 summarizes the differences between DOSY and SEC, that is that SEC is based on a phenomenological calibration that is highly dependent on the individual columns used for separation, whole DOSY uses fully deterministic models that allow comparison of data between instruments. The main advantage of SEC is, and this should be stated clearly, that it can measure full weight distributions with very high precision.

Most importantly, though, we demonstrate that DOSY calibration is in fact truly universal. Here, universal does not refer to the separation principle as explained above for SEC, but refers to the fact that no individual calibration of instruments is required. In fact, once accurately determined, a single calibration could be used for any NMR spectrometer in any laboratory worldwide, independently of the choice of deuterated solvent. This removes the need for constant re-calibration of instruments, and makes DOSY much more accessible to use as a molecular weight determination tool compared to SEC, the current gold standard.

Figure 1. Principle of universal DOSY calibration for molecular weight determination in comparison to standards SEC detection.

<!-- image -->

<!-- image -->

A detailed description of DOSY is given elsewhere, [10] and a practical guide to performing DOSY for molecular weight determination is given in the Supporting Information. Generally, the diffusion coefficient D correlates with the hydrodynamic radius r h of a species via the StokesEinstein relation, where T is temperature, k B the Boltzman constant and η the solvent bulk viscosity (2):

$$\int \lim i t s _ { \substack { 1 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

r h again can be correlated to the average molecular weight of the polymer via the empirical Rouse-Zimm model (3), [12]

<!-- image -->

$$r _ { h } \sim b M ^ { v }$$

in which b and v are arbitrary parameters, and M the molecular weight. This is not unlike the MHKS relation. Insertion of the above equation into the Stokes-Einstein equation yields (4):

$$D = b ^ { \prime } M ^ { - \nu } & & ( 4 ) & \text {polymme} \\$$

In this relation, b ' is an adjusted proportionality factor. This relation is well established, and has been used in several studies to establish molecular weight calibrations for DOSY experiments in its logarithmic form (see Figure 1). Calibrations for polystyrene, PS, [11a] poly(methyl acrylate), PMA, poly(methyl methacrylate), PMMA, [13] poly(ethylene glycol), PEG, [14] dextrane [10] and pullane [15] have been provided (see Table 1) to date, and DOSY has been used numerous times as a more qualitative tool, especially to prove that two blocks of a block copolymer are joined together chemically. Interestingly, the potential to derive more information than 'just' an average molecular weight has also been explored, and Vieville et al. demonstrated that DOSY can in principle also correctly measure the dispersity of a sample. [16] This initial finding, as promising as it is, will however require further investigation.

Returning to the equations, the relation in Equation (4) can also be expressed as (5) (with c as new proportionality parameter)

$$D \eta = c M ^ { - v } & & ( 5 ) & \text { clear } \, \real$$

or, in its logarithmic form, as (6)

$$\log ( D ) + \log ( \eta ) = \log ( c ) - v \log ( M ) & & ( 6 ) & \text {iffer} & & \\$$

Use of this form allows us to account for the solvent viscosity. A different derivation can be found in literature. Since DOSY is typically performed under highly dilute conditions (typically around 1 mgmL 1 concentrations), influences of the polymer on bulk viscosity can be largely neglected. This opens the possibility to compare DOSY mass calibrations between different solvents. SEC does not offer such a simple correlation, and comparison of SEC data obtained for different solvents is difficult, if not impossible. When analyzing the literature, it is obvious that individual diffusion coefficients can be quite different from each other

Table 1: Literature data on DOSY molecular weight calibrations.

| Polymer   |   lg(b ' /m 2 s 1 ) |    v | Solvent, ref   |
|-----------|---------------------|------|----------------|
| PS        |                7.70 | 0.54 | benzene, [11]  |
| pMA       |                7.72 | 0.50 | toluene, [13]  |
| pMMA      |                7.53 | 0.56 | CDCl 3 , [11]  |
| dextrane  |                8.14 | 0.47 | D 2 O, [11]    |
| pullane   |                 8.2 | 0.49 | D 2 O, [15]    |
| PEG [a]   |                8.39 | 0.47 | D 2 O, [14]    |

Angew. Chem. Int. Ed. 2022 , 61 , e202114536 (3 of 5)

<!-- image -->

for given molecular weights of different polymers. This is unsurprising, as r h will depend on polymer solubility, and the specific ability of a polymer chain to coil in said solvent. On the other hand, though, it is surprising that viscosity effects seem to outweigh the solvent quality influence (see Supporting Information for a comparison of diffusion and viscositycorrected literature values). Table 1 summarizes the literature values discussed above. The variation of different polymers even across solvents is lower than what is typically found for polymers in the MHKS equation. MHKS parameters allow for correlation of hydrodynamic volumes with molecular weight, yet the same principle can be applied to DOSY (due to the resemblance of the MHKS equation to the Rouse-Zimm relation). This indicates that even when an unknown analyte is subjected to DOSY on the basis of a calibration with a different type of standard, a reasonable approximation of molecular weight can be obtained that is as accurate (or inaccurate) as a corresponding SEC analysis. Since DOSY data can be corrected for viscosity influences, it appears reasonable that DOSY can potentially even outperform classical SEC for molecular weight determination. In fact, when, for example viscosity-corrected diffusion coefficients between PMMA and aqueous solutions of PEG are compared, measurement of PEG in water evaluated on the basis of a PMMA calibration in deuterochloroform would yield an error of just 10-15% in the range of 1000 to 100000 Da (determined by the relative gap for any given molecular weight when applying the calibration of the other polymer).

Literature data is, however, too scattered to allow for clear conclusions if viscosity effects are indeed sufficient to explain the differences between various solvents. ArrabalCampos et al. had previously shown that a reasonable molecular weight calibration can be obtained between different NMR solvents, yet this was only shown for two individual samples, which did not yet allow for a conclusion of broad applicability. [11b]

## Results and Discussion

We performed full DOSY calibrations on a series of polystyrene standards in a variety of typical deuterated NMR solvents. When the logarithm of the obtained diffusion coefficient is plotted against molecular weight, linear relationships are obtained in all cases (see top of Figure 2). A first observation is that the linear correlation seems to apply to the whole tested mass range of 1000 to 62000 gmol 1 (for benzene, linearity was confirmed up to 560000 gmol 1 , see Supporting Information).

Slightly different slopes are observed for each solvent, signifying the difference in coiling of the polymers in each solvent. The biggest difference in data is seen for acetone, for which significantly higher diffusion coefficients are obtained. Interestingly though, when the viscosity is accounted for, all plots almost match each other, and even the already small differences between solvents are almost entirely removed (see lower part of Figure 2). Within 95% confidence intervals, all measurements in the various GDCh solvents are practically identical. Table 2 lists all fit results for viscosity-adjusted and direct calibration. The indicated errors are resulting for weighted fits, and are likely to underestimate the true error. While differences (stemming from the slightly different slopes and difference in polymer coiling) become more prominent with increased molecular weight, data on the low molecular weight side (up to 10000 gmol 1 ) are almost indistinguishable. Obviously, a direct calibration for a polymer in each solvent would still yield the best result. Yet, it is remarkable that a polystyrene calibration obtained in acetone-a bad solvent for the polymer-yields reasonable results for the other solvents within close error limits. Thus, this close incidence of plots can be used to obtain a solvent independent calibration in which the error of determination even at 100000 gmol 1 is still not higher than 15% (see bar charts in Supporting Information). This may sound like a considerable error, but again when compared to SEC this is a very reasonable and acceptable deviation overall. Yet, if required, the accuracy can always be increased by using the calibration for the specific solvent alone, in principle allowing for errors below 5% (see error margins given in Table 2).

<!-- image -->

Figure 2. Diffusion coefficients determined via DOSY for polystyrene standards in a series of solvents (top) and viscosity-corrected data for the same measurements (bottom).

<!-- image -->

Table 2: Calibration coefficients obtained for polystyrene for a variety of deuterated solvents.

| Solvent    | lg(b ' /m 2 s 1 )   | lg(c/m 2 s 1 )   | V           |
|------------|---------------------|------------------|-------------|
| benzene-d6 | 7.94 � 0.02         | 8.15 � 0.02      | 0.49 � 0.02 |
| CDCl 3     | 7.97 � 0.01         | 8.22 � 0.01      | 0.46 � 0.01 |
| acetone-d6 | 7.78 � 0.02         | 8.31 � 0.02      | 0.43 � 0.02 |
| toluene-d8 | 7.82 � 0.01         | 8.07 � 0.01      | 0.51 � 0.01 |
| THF-d8     | 8.07 � 0.01         | 8.40 � 0.01      | 0.42 � 0.02 |

Table 3: Calibration coefficients obtained for poly(ethylene glycol) for a variety of deuterated solvents.

| Solvent                      | lg(b ' /m 2 s 1 )   | lg(c/m 2 s 1 )   | v           |
|------------------------------|---------------------|------------------|-------------|
| D 2 O methanol-d4 acetone-d6 | 8.23 � 0.01         | 8.14 � 0.01      | 0.49 � 0.01 |
|                              | 8.06 � 0.01         | 8.32 � 0.01      | 0.45 � 0.01 |
|                              | 7.94 � 0.01         | 8.46 � 0.02      | 0.41 � 0.01 |
| THF-d8                       | 7.94 � 0.01         | 8.26 � 0.02      | 0.46 � 0.01 |
| CDCl 3                       | 8.04 � 0.01         | 8.08 � 0.02      | 0.45 � 0.01 |
| ACN-d3                       | 7.88 � 0.01         | 8.34 � 0.03      | 0.44 � 0.01 |

<!-- image -->

The same observations as for apolar polystyrene can be made for polar poly(ethylene glycol). As before, a series of calibration standards were measured via DOSY in a series of solvents, see Figure 3. Again, individual calibrations are obtained for each solvent, which practically coincide when corrected for solvent viscosity (Table 3). The match between solvents seems to be even better than what is observed for polystyrene. That the principle is applicable to more than one polymer, and also to two very different polymers, is quite remarkable. The difference between polymers, as discussed above for literature data, is indeed relatively small. The slopes of the calibrations are very similar, and also the offset in c is relatively small. This underpins again, that even if a calibration for a specific polymer is certainly desirable, calibrations can be used quite broadly to make a reasonable estimate. The diffusion coefficient of a hypothetical 10000 Da PS sample differs by only 1% from a PEG standard of the same size. Note that the same comparison of polymers by SEC is not even possible, since polar and apolar materials require usually different column setups and cannot be measured on the same chromatography instrument.

Figure 3. Diffusion coefficients determined via DOSY for poly(ethylene glycol) standards in a series of solvents (top) and viscosity-corrected data for the same measurements (bottom).

<!-- image -->

<!-- image -->

## Conclusion

The match of viscosity-corrected calibrations of linear polystyrene and poly(ethylene glycol), and the observation that application of one specific calibration to another polymer still yields reasonable results is highly satisfying. It raises, however, the question how precise is the molecular weight calibration using DOSY in the first place? In our previous work on methyl acrylate polymers we observed already an almost perfect match of datasets in DOSY when comparing pMA standards measured in different labs, on different setups and with different molecular weight ranges. [12,17] Also, the data presented here does correlate very well with literature data (see detailed comparisons in the Supporting Information). [1] This indicates that the interlab variability is indeed very small. This is to be expected since diffusion coefficients should be universal for a given polymer in a given solvent, and differences can only stem from variations in the exact protocol of measurements (already slight increases in polymer concentration may lead to decreased observable diffusion coefficients), and not from differences in the setup. This allows us to use a calibration from one laboratory in other labs. In other words, no tedious individual calibration of setups is required. This sets DOSY apart from SEC beyond just the possibility to correct for solvents, and makes it truly universally applicable. Removing the need to obtain standards for calibration allows for much more universal use of the method. Polymer standards with well-known molecular weights are difficult to obtain, and commercially available only for a small number of polymers. It will be an important task in the future to provide calibrations of the most important polymers, and to benchmark those between laboratories and operators to establish truly universal calibration data. Further, influences of chain architecture, such as block structures, or polymer branching need to be established. We hope that with this report we can give the impulse for such a larger scale interlaboratory study.

## Acknowledgements

The Australian Research Council (ARC) is acknowledged for funding via project DP190103309. The authors further

.

Manuscript received: October 27, 2021

.

<!-- image -->

wish to thank China Lancaster for helping with the table of contents artwork.

## Conflict of Interest

The authors declare no conflict of interest.

## Data Availability Statement

The data that support the findings of this study are available in the Supporting Information of this article.

Keywords: Diffusion ordered spectroscopy · Molecular weight determination · Polymers · Universal calibration

- [1] A. Striegel, W. W. Yau, J. J. Kirkland, D. D. Bly, Modern SizeExclusion Chromatography, Practice of Gel Permeation Chromatography and Gel Filtration Chromatography , Wiley, Hoboken, 2009 .
- [2] H. Pasch,
- [3] P. J. Wyatt,

.

- [4] a) J. Engelke, J. Brandt, C. Barner-Kowollik, A. Lederer, ; b) E. Uliyanchenko, S. van der Wal, P. J. Schoenmakers,

.

- [5] Z. Grubisic, P. Rempp, H. Benoit,

.

- [6] D. Berek,
- [7] D. Berek, IUPAC Round Robin Test, General Assembly of IUPAC, Brisbane 2001 .
- [8] K. Philipps, T. Junkers, J. J. Michels,

.

- [9] J. U. Izunobi, C. L. Higginbotham,

.

- [10] P. Groves,

.

- [11] a) W. Li, H. Chung, C. Daeffler, J. A. Johnson, R. H. Grubbs, ; b) F. M. Arrabal-Campos, P. Oña-Burgos, I. Fernández,

.

- [12] R. Pethrick, Polymer Physics (Eds.: M. Rubinstein, R. H. Colby), Oxford University Press, Oxford, 2004 .
- [13] J. H. Vrijsen, I. A. Thomlinson, M. E. Levere, C. L. Lyall, M. G. Davidson, U. Hintermair, T. Junkers,

.

- [14] R. A. Waggoner, F. D. Blum, J. C. Lang,

.

- [15] S. Viel, D. Capitani, L. Mannina, A. Segre,

.

- [16] J. Viéville, M. Tanty, M.-A. Delsuc,

.

- [17] J. De Neve, J. Haven, S. Harrisson, T. Junkers,

;

.