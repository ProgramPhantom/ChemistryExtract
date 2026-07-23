<!-- image -->

[pubs.acs.org/ac](pubs.acs.org/ac?ref=pdf)

<!-- image -->

<!-- image -->

## Diffusion-Ordered Spectroscopy for Rapid and Facile Determination of Consumer Plastic Molecular Weight

Taylor F. Nelson * and Collin P. Ward *

<!-- image -->

Cite This: https://doi.org/10.1021/acs.analchem.3c00655

## ACCESS

<!-- image -->

Metrics &amp; More Article Recommendations

<!-- image -->

ABSTRACT: Molecular weight (MW) is a key control of plastic polymer properties and their fate in the environment. However, the primary tool used to determine plastic MW, gel permeation chromatography (GPC), has major limitations, such as low precision and accuracy, requirements for dedicated instrumentation, production of high volumes of hazardous waste, and large sample sizes. In this study, we describe, validate, and apply a diffusion-ordered spectroscopy (DOSY) method for polymer MW determinations, with a focus on applications for consumer plastics. Several experimental conditions were systematically optimized and tested to validate the DOSY method, including the selection of pulse sequences, the effect of sample concentration, crossvalidation with multiple sets of external standards, and long-term Supporting Information

<!-- image -->

<!-- image -->

instrumental stability. Validation was performed for a wide range of polymers, solvents, and temperatures, highlighting its potential for broad applicability. A preliminary screening of polystyrene and polyethylene terephthalate consumer products revealed widely varying MWs (up to two-fold) for products made of the same polymer type. A preliminary experiment was also conducted to track the decrease in polystyrene MW via photochemical chain scission reactions, finding a 20% reduction in MW after less than 1 week of irradiation. Collectively, our results demonstrate the potential for DOSY to provide high-throughput, accurate, and precise measures of polymer MW, as well as the evolution of polymer MW during environmental weathering processes, such as photochemical degradation. We conclude with a discussion of (i) the many advantages of DOSY compared to GPC, (ii) future developments to enhance the depth of information obtained from DOSY, and (iii) approaches to broaden the accessibility of this promising analytical method to the research community.

## ■ INTRODUCTION

Molecular weight (MW) is a key control of polymer properties and their fate in the environment. For instance, the average values and dispersity of MWs have large influences on the physical properties of synthetic polymer resins. 1,2 A single homopolymer (meaning, of one chemical structure) may be synthesized with different MWs, which are then used for different applications based on the resulting thermal or mechanical properties. When leaked into the environment, only low MW constituents of polymers (even water-soluble ones) 3 are available for biodegradation, 4 and MW is expected to decrease upon exposure to sunlight via chain scission reactions. 5 -8 Therefore, polymer MW is expected to be a controlling factor for their environmental fate. These collective roles that MW plays call for analytical approaches for polymer MWthat are efficient, accurate, and precise.

Typically, polymer MW is determined using gel permeation chromatography (GPC; a category of size-exclusion chromatography), which separates analytes dissolved in water or organic solvents based on their hydrodynamic radii. 9 GPC measurements of polymers can be disadvantaged by low precision and accuracy especially when baseline uncertainties are present, and demand dedicated instrumentation with high maintenance and calibration requirements. 10,11 Furthermore, many consumer plastic products are made from poorly solvable thermoplastics such as polyethylene (PE), polypropylene (PP), or polyethylene terephthalate (PET), which require halogenated solvents, often in combination with high temperatures, to dissolve. Analysis of these polymers using GPC requires specialized infrastructure to mitigate health and safety concerns and creates large amounts of hazardous and costly solvent waste. While these drawbacks may be acceptable for polymer MW estimations during synthesis, more efficient, accurate, and precise methods are desirable for other applications (e.g., analysis of environmental samples, consumer plastic products, or samples from polymer degradation experiments).

<!-- image -->

Received:

February 13, 2023

Accepted:

May 15, 2023

Diffusion-ordered spectroscopy (DOSY) is a nuclear magnetic resonance (NMR) technique that can be applied to determine polymer MWs. This determination relies on an empirical relationship between diffusivity and MW of dissolved polymers. 12 MWs of unknowns can be determined using external calibration against standards of known MWs. Just as GPC columns separate solubilized polymer chains by hydrodynamic radii ( r ; unit m), DOSY experiments indirectly determine r as it relates to their measured diffusivity ( D ; m 2 s -1 ) value, according to the Stokes -Einstein equation:

$$D = \frac { k _ { B } \, T } { 6 \, \pi \, \eta \, r } & & \begin{matrix} \sigma \\ \sigma \\ \sigma \end{matrix} \\$$

where k B is the Boltzmann constant (= 1.38 × 10 -23 kg m 2 s -2 K -1 ), T is the temperature (K), and η is the dynamic solution viscosity (kg m -1 s -1 ). Therefore, measurements using external calibration are best when unknowns are compared with standards with the same or similar chemical structure, as they will most closely match in terms of three-dimensional shape in solution, and therefore hydrodynamic radius per unit chain length.

While DOSY has been applied for some applications in macromolecular (esp., polymer) science, such as determining extents of polymerization reactions or final MWs of synthesized samples, 11,13,14 measuring ligand exchange in colloids, 15 and elucidating the size and shape of other supermolecules, 16 its capabilities have not been fully explored. DOSY has mainly been applied thus far to a limited number of polymer types (e.g., polymers with corresponding standards for GPC such as polystyrene, or those with well-defined end groups to compare to NMR measurements), but its application is theoretically universal for different polymers. For example, DOSY has recently been applied to determine the MW of natural polymers such as lignin and heparin, relating 1 H and DOSY spectra to GPC-determined MWs using multivariate correlations. 17,18 DOSY should therefore be a suitable alternative method to GPCfor the analysis of plastic consumer products, which span a wide range of polymer types and presumably MWs. Furthermore, the potential for DOSY as a method to determine polymer MWs for experimental work (e.g., degradation of polymers in engineered or environmental systems) has only recently been introduced 6 and not yet fully validated. To verify the applicability of this analytical approach requires an investigation of the methodological considerations that control accuracy and precision of MW assessments via DOSY.

The aim of this work is to develop and validate procedures for determining MWs of various polymers using DOSY. This includes investigating the effects of certain analytical parameters (e.g., pulse sequence and sample concentration) and validating the approach for polymers with different chemical structures as well as different requirements for solubility (e.g., solvent and temperature). Furthermore, we demonstrate applications of the method through rapid and simple determinations for consumer plastic products of unknown MW and by tracking MW changes upon photoinduced chain scission. We conclude with an indepth discussion about the many advantages of DOSY in comparison to traditional GPC approaches for MW determination, as well as future outlooks for advancing the development and applications of DOSY for the fields of polymer and environmental chemistry.

## ■ MATERIALS AND METHODS

Materials. Polymer Standards. Analytical standards of welldefined MWs for different polymers were used directly as received. We took the weight-averaged molecular weight ( M w) reported by each manufacturer (determined using GPC) as the known value for MW of each standard. Manufacturer-reported M w and M n values are shown in Section S1 of the Supporting Information. Polystyrene (PS) and dextran standards were from Sigma-Aldrich (USA), while PE, PET, and a second set of PS standards were from Polymer Standards Service (USA).

Consumer Plastic Products. PS packing peanuts were obtained from Uline (USA), foam cups and foam clamshells were obtained from WebstaurantStore (USA), and foam cooler was obtained from a local convenience store (Massachusetts, USA). PET workout shirt was a Hanes brand item obtained online, and cola and water drinking bottles were obtained from local stores (Massachusetts, USA). All materials were rinsed with ultrapure water and dried with a stream of N 2 prior to use.

Solvents. Heavy water (D2O; ≥ 99.9 atom% D) and uniformly deuterated forms of chloroform (CDCl3; ≥ 99.8 atom% D), dimethyl sulfoxide (DMSOd 6 ; ≥ 99.8 atom% D), and 1,1,2,2-tetrachloroethane (CD 2 Cl4; ≥ 99.5 atom% D) were from Sigma-Aldrich (USA). Deuterated trifluoroacetic acid (TFAd ; ≥ 99.5 atom% D) was from Cambridge Isotope Laboratories (USA). CD2Cl4 was kept under inert atmosphere, and all solvents were used as received.

NMR Experiments. Sample Preparation for NMR Analyses. Polymer standards and products were prepared for NMR analysis by dissolving in an appropriate deuterated solvent. Unless otherwise stated, samples were weighed out and then dissolved in deuterated solvent at a concentration of 10 mg mL -1 at room temperature, and then 0.5 mL of each solution was added to a 4 mm diameter NMR tube (solution height of 35 mm). To determine the effect of polymer concentration on the DOSY measurement, solutions of different PS MW standards were prepared at 40 mg mL -1 CDCl3, from which lowerconcentration solutions were prepared by serial dilution. For each PE sample, 5 mg of the polymer was added to an NMR tube, which was then sealed with a septum cap. The tube was flushed with N 2 for 2 min, and then 0.5 mL of N2-purged CD2Cl4 was added through the septum with a cannula.

DOSY Experiments. All NMR experiments were performed on a Bruker Avance NEO spectrometer equipped with an Ascend 400 MHz magnet and a 4 mm BBO H&amp;F CryoProbe. Most DOSY experiments were performed using a double stimulated spin echo diffusion pulse sequence with bipolar phasing and three spoiler gradients (Bruker pulse program 'dstebpgp3s'), with the following exceptions. For comparison of different pulse sequences, PS standards were also analyzed using a longitudinal echo delay diffusion pulse sequence with bipolar phasing and two spoiler gradients (Bruker pulse program 'ledbgpg2s') and a stimulated spin echo diffusion pulse sequence with bipolar phasing and one spoiler gradient (Bruker pulse program 'stebpgp1s'). Dextran standards in D2O and DMSOd 6 were analyzed using the 'ledbpgp2s' pulse sequence. For PE, experiments were performed at 393 K (samples were pre-heated in the NMR probe at 393 K for 20 min before each experiment); for all other polymers, experiments were performed at 298 K. Experiments were performed without sample spinning.

DOSY parameters were adjusted for each polymer/solvent system. Notably, T 1 relaxation values were determined for each polymer, and the recycle delays were set to 2 -3 × the T1 time, while diffusion times ( Δ ) were kept shorter than the T 1 time. Diffusion gradient pulse lengths ( δ ) were varied depending on the MW of each sample to optimize the signal attenuation during the gradient pulses. These parameter values for each specific polymer can be found in Section S2 of the Supporting Information. Unless otherwise stated, all experiments were performed with 16 gradient steps with gradient strengths ( g ) varied linearly from 1.05 to 51.56 G cm -1 . Each experiment was performed by collecting 16 scans per gradient step.

Figure 1. Effect of polymer concentration on measured diffusivity. Panel A: measured diffusivity vs concentration (log -log scale) of five PS standards of varying weight-averaged MWs as indicated by labels in the panel. One sample was prepared per standard per concentration and measured in duplicate; low measurement variability often results in overlapping diamonds per sample. Long-dashed lines show the linear interpolation between points and are shown to guide the eye. Panel B: points show measured diffusivity vs MW (log -log scale) of samples at eight PS concentrations; same data as shown in panel A. Dashed lines show the linear least-squared models fit to measurements (all R 2 &gt; 0.99).

<!-- image -->

To calculate polymer diffusivities from DOSY experiments, the collected spectra were analyzed using the T1/T2 package of TopSpin. The integration region was designated in the first slice of each experiment (example spectra and integration regions are shown in Section S3 of the Supporting Information). Then, the relative intensity ( I / I 0 ) of each step was plotted vs the gradient strength, and the diffusivity ( D , m 2 s -1 ) was calculated according to

$$I / I _ { 0 } = e ^ { ( - D \cdot ( 2 \pi \, \gamma \, g \, \delta ) ^ { 2 } \cdot ( \Delta - \frac { \delta } { 3 } ) \cdot 1 0 ^ { 4 } } & & \text {diff} \\ & & ( 2 ) \\ & & 2 5 \, ^ { \circ }$$

where γ is the gyromagnetic ratio for 1 H (= 4258 Hz G -1 ).

All NMR spectra and data were analyzed using Bruker TopSpin (version 4.1.0). Additional calculations were performed using R (version 4.1.1) via RStudio.

Photoirradiation Experiment. A PS reference material (0.19 mm thick film containing minimal additives) was obtained from Goodfellow (UK). This film was cut into 1.5 × 1.5 cm square coupons for the photoirradiation experiment.

The photoirradiation setup involved an array of 81 (arranged in a 9 × 9 array) light-emitting diode (LED) chips (total max optical power 3.4 W) resting on a wooden stand with a hole shielded by a thin quartz disc. Approximately 15 cm below the array, the PS coupons were arranged on a black anodized aluminum sheet, cooled to approximately 25 ° Cfrom below by a water-cooled plate. The irradiance (measured at four points at the distance samples were kept below the LED array) was on average 54 W m -2 with a maximum at 312 nm. See Supporting Information Section S4 for the measured irradiance spectrum.

Samples were collected after 0, 2, 4, 6, 8, and 10 days of irradiation (during each time period, the samples were flipped such that each side was exposed for half of the total irradiation time) and prepared for NMR analysis, as described above. The D for each sample was measured using the DOSY procedure described above, and the MW of each sample was calculated using a linear relationship between log( D ) and log(MW) established using PS MW standards.

## ■ RESULTS AND DISCUSSION

Pulse Program Comparison. Different NMR pulse sequences have been developed for the determination of molecular diffusivity using DOSY. Given that different pulse sequences offer unique advantages and disadvantages (e.g., additional delays or pulses can be added to account for noise and convection effects but create longer overall sequences), selecting an optimal pulse sequence is often not obvious.

To evaluate the effect of pulse sequence choice on measured diffusivity, we measured a PS standard of given MW in CDCl 3 at 25 ° C using three spin echo diffusion pulse sequences available in TopSpin, stimulated echo ('STE'), longitudinal echo delay ('LED'), and double stimulated echo ('DSTE'), and applied different diffusion times for each sequence. When comparing changes in measured D values when different diffusion times were applied, the STE and LED programs showed increases in measured D of 15 and 10%, respectively, when increasing the applied diffusion time from 400 to 800 ms (Figure S7; see Supporting Information Section S5 also for measured signal intensities versus gradient strength for each pulse program). On the other hand, the DSTE sequence showed a negligible change ( ≤ 1%) in measured D with the same increase in diffusion time. The increases in measured D with longer diffusion times for both the STE and LED sequences result from registering additional movement due to convection. In contrast, the negligible change for the DSTE sequence shows adequate convection correction. Therefore, we found the DSTE sequence to give the most accurate results for PS in CDCl3 and chose it for remaining experiments herein.

Overall, this analysis demonstrates the importance of evaluating the influence of pulse sequences on diffusivity measurements for given polymer/solvent systems. For the used system herein (i.e., PS at 25 ° C in CDCl3 analyzed using a CryoProbe), we found it necessary to apply convection correction; however, this may not be necessary for more viscous solvents, faster diffusing polymers, operating temperatures further from the solvent boiling point, or even different types of probes. The choice of pulse sequence may also be influenced by the desired length of the applied gradient pulses. The relatively slow diffusion of polymers generally calls for long gradient pulses to obtain proper signal attenuation with increasing gradient strength in a normal DOSY experiment. Pulse sequences with fewer gradient pulses may therefore be desirable as they allow for longer individual pulses. Here, we prioritized the improved accuracy through convection correction over the need to apply shorter gradient pulses using the DSTE pulse sequence and despite the resulting loss of overall signal intensities.

Concentration Dependence. Molecular diffusivity is inversely related to solution viscosity (eq 1), which for dissolved polymers depends on the polymer, solvent, and concentration. It has been demonstrated previously that measured diffusivities indeed vary with changes in polymer concentration. 12,14,19 However, it remains unclear how sensitive the linear relationship between D and MW is across a wide range of polymer concentrations.

To investigate the effect of concentration on measured D , we prepared and analyzed five PS standards, each at eight concentrations ranging from 0.32 to 40 mg mL -1 . Figure 1 shows the log of the measured D against the log of the PS concentration (panel A) and the log of the reported average MW of each standard (panel B). Measured log( D ) values decreased exponentially with increasing PS concentration and thus solution viscosity. The decrease was less drastic for lower MW standards (e.g., 10 -9.72 at 0.32 mg mL -1 vs 10 -9.88 at 40 mg mL -1 for 12 kDa) than for higher MW standards (e.g., 10 -10.64 at 0.32 mg mL -1 vs 10 -11.45 at 40 mg mL -1 for 450 kDa standard). Despite the changes in log( D ) across PS concentrations, the relationship between log( D ) and log(MW) remained linear with excellent linear least squares regression fits ( R 2 &gt; 0.99 for any given concentration). Therefore, any concentration chosen in the tested range with the tested DOSY experiment gives a strong calibration curve and can be used to determine MWs of samples.

The use of different concentrations has unique advantages: more concentrated samples will result in more intense signals, meaning shorter overall experiment times or better resolution of small peaks in chemically heterogeneous samples, while lower concentrations may be needed if sample amounts are limiting. In any case, the dependence of measured D on sample concentration shows that standard and sample concentrations must be well-controlled to maintain a singular linear relationship between log( D ) and log(MW).

Deconvoluting Different MW Distributions. DOSY experiments have previously been used to describe MW distributions for polymers. One described approach involves performing an inversion of Laplace transformation (ILT) on DOSY data to construct MW distribution curves. Here, we used this approach on different MW standards of PS, both measured individually and as a mixture. Figure 2 shows the resulting calculated MW distributions, measured using 64 gradient steps. Weadditionally measured the MW distributions using the same procedure but only 16 gradient steps (see Supporting Information Section S6).

Figure 2. MWdistributions of PS standards determined using DOSY. Measured signal intensities vs calculated log(MW) for five individual PS standards of well-defined MWs (diamonds and dashed traces) or for one sample containing a mix of the five standards in equal mass amounts (stars and solid trace). DOSY experiments were performed using 64 gradient steps, and distributions were calculated by performing an inversion of Laplace transformation on the resulting DOSY data.

<!-- image -->

The individual standards showed Lorentz-type distributions, which may be expected for radical polymerizations. These distributions showed accurate average values and were wellresolved when measured using 64 gradient steps. Comparatively, the distributions were less obviously normally distributed, inaccurate, and not resolvable from each other when measured with only 16 gradient steps. Furthermore, when measured using 64 gradient steps, the mixture of the different standards in one tube showed a multi-model distribution with two distant maxima at 14 and 120 kDa, as well as a shoulder toward higher MWs. In contrast, when the number of gradient steps was lowered to 16, the mixture showed a monomodal distribution, with an average value close to the calculated number-averaged MWfrom the mixture of the five polymers.

This simple test demonstrates the potential of DOSY to resolve heterogeneous distributions of polymer MW within one sample. In particular, the resolution of different MWs is much clearer for a multimodal distribution when two average MWs are further apart (i.e., 12 vs 100 kDa, or roughly one order of magnitude). This resolution implies that DOSY may be used to differentiate between high and low MW polymers of the same identity, for instance, during polymer degradation where mixed distributions of polymer chain lengths may be formed. Finally, a higher number of gradient steps may be necessary to increase the resolution for calculating the MW distributions; here, changing the number of gradient steps improved the resolution for ILT analysis but had a minimal effect on the determination of average MW values (see Supporting Information Section S7 for more information).

MW Standards of Different Polymers. In the literature, polymer MWs measured using GPC are often reported relative to PS standards, even when PS is not the sample polymer of interest. Similarly, in past DOSY applications, polymer MWs have been reported relative to a limited number of polymer standards. 11,14,19 Because NMR solvents are self-contained during analysis (i.e., no solvent mobile phase required as for GPC), different solvents can be readily analyzed in the same instrument. This suggests DOSY as a generally more universal MWdetermination method as compared to GPC.

| polymer (solvent)   | polymer (solvent)   | slope          | y-intercept   |   R² |
|---------------------|---------------------|----------------|---------------|------|
| 口                  | PS (CDCl{3)         | -0.79 (± 0.02) | -6.47 (±0.09) | 0.99 |
|                     | PE (C2D_2Cl{4})     | -0.51 (± 0.04) | -7.7 (±0.2)   | 0.96 |
| O                   | PET (TFA-d)         | -0.68 (± 0.01) | -7.18 (±0.07) |  660 |
|                     | dextran (D2O)       | -0.55 (± 0.01) | -7.84 (±0.02) | 0.99 |
|                     | dextran (DMSO-d₆)   | -0.55 (± 0.01) | -8.13 (±0.06) | 0.99 |

Figure 3. Relationships between measured diffusivities and weight-averaged MWs for various polymers. All standards were dissolved in the indicated deuterated solvent at concentrations of 10 mg mL -1 . Points in the plot show replicate measurements for single samples prepared per standard (each sample was measured in duplicate for dextran and PE samples or triplicate for PS and PET samples). Low measurement variability often results in overlapping symbols per sample treatment. Lines show the linear least-squared models fit to measurements, with equations and R 2 values for each model listed in the table.

<!-- image -->

To demonstrate the universal applicability of DOSY for MW measurement of different polymers, we determined log( D ) vs log(MW) relationships for four different polymers: three thermoplastics (PS, PE, and PET) and one polysaccharide (dextran) that we additionally analyzed in two different solvents (DMSOd 6 and D2O). The values of signal intensity versus increasing gradient strength measured for the standards of the different polymers are presented in the Supporting Information (Section S8). Figure 3 shows the measured D data plotted against reported MWs from the manufacturers of individual polymer MW standards. Included are lines showing the linear least squares regression fits of the data, as well as their equations and coefficients of determination ( R 2 ) in the table to the right of the plot.

All of the log( D ) vs log(MW) relationships showed linear fits with excellent R 2 values ( ≥ 0.99 for all polymers except PE, which showed an R 2 of 0.96). Therefore, each measurement would serve as a strong calibration curve for the determination of MW for unknowns in each polymer/solvent system. Each calibration curve shows a different response of D to changes in reported MW, with different slopes and y -intercepts for each. Interestingly, two calibration curves for dextran show the same slope, but different y -intercepts, when measured in D2O or DMSOd 6 . This result implies that differences in y -intercepts are strongly influenced by the use of different solvents, which changes only the intrinsic viscosity of the solutions. On the other hand, differences in slopes for the calibration curves are more likely influenced by differences in chemical structures, which cause different diffusivities for each polymer due to their shape in solution.

The strong and validated calibrations demonstrate the applicability of the DOSY method to various thermoplastics and water-soluble polymers. Considering that average MWs of soluble polymers and the plastics in consumer products are generally not reported, DOSY offers a rapid and facile way to assess the MW of a wide range of such materials accurately and precisely.

Further Method Validation. To further evaluate the accuracy of this method, we determined the MW for a second set of PS MW standards (treated as unknowns) and compared these values with those reported by the manufacturer. The GPCdetermined MWs for the standards were 58.9, 133.0, and 239.0 kDa (provided by the manufacturer). Relative to the PS calibration curve in Figure 3, we determined MW values of 52 ( ± 3), 130 ( ± 2), and 253 ( ± 7) kDa, corresponding to measurement errors of 11 ( ± 5), 3 ( ± 2), and 6 ( ± 3) %, respectively. Therefore, the determined MW values agree with the reported values, serving as an additional validation for the accuracy of determining the unknown MW of samples using DOSY. In addition, comparisons between DOSY and GPC determinations have been previously verified for polymers such as PS and PET. 11,14

While the short-term reproducibility of the method was already well-established (see Figures 1 and 3, which contain duplicate or triplicate measurements of MW standards of different polymers), we additionally evaluated the reproducibility of the method over longer periods of time. To this end, we compared the calibration curves of the same PS samples measured four times over a period of 6 months (see Supporting Information Section S9). These four calibration curves show very similar relationships between log( D ) and log(MW) when measured repeatedly over this time period. Notably, significant changes in the slope and intercept of the calibrations occurred only when the CryoProbe used for DOSY experiments was uninstalled and subsequently reinstalled to the spectrometer. These results indicate that the calibrations of the DOSY method used herein are stable over time and may only need to be updated periodically or when changes to the instrumentation or measuring conditions are made.

Application: Initial Screening of the MW of Plastic Consumer Products. As a first demonstration of the use of DOSYtoscreen average MWs of consumer plastics, we analyzed a few selected products made from two different polymers: PS (specifically foam products, i.e., expanded polystyrene (EPS)) and PET (see Supporting Information Section S10 for a table of the measured values). The MWs for the four tested EPS products ranged from 100 to 175 kDa, almost a factor of 2. Overall, MWs for the four tested PET products were lower than those of EPS products, ranging from 56 to 80 kDa. Notably, one PET product (workout shirt) was comprised of PET fibers and had a lower MW compared to the other three products, which were all single-use drinking bottles made from PET films and showed more similar MWs. The values measured for EPS and PET products agree with other published values of similar products, such as consumer products made from EPS and EPS waste, 20 -22 as well as PET drinking bottles and fibers. 14,23 Moreover, the standard deviations from the mean MW value measured for triplicate samples did not exceed 3% of the mean, showing good agreement between individual samples (i.e., separately collected pieces) from a single product. These low relative standard deviations are meaningful for screening or experimental applications where a high number of samples may be analyzed, demonstrating that a low number of replicates should be able to capture heterogeneity of a single sample.

The finding of varying MWs for products made of the same polymer type further supports the arguments that plastics should be treated as a complex contaminant class 24 and that plastic formulation impacts environmental fate. 6,25 -29 To date, the community has primarily focused on differences in formulation related to polymer type and additive content. Based on the findings presented here, we hypothesize that large differences in MWs,such as those seen in our analysis of PS and PET, may also translate into notable differences in their environmental behavior. DOSY thus represents a promising, high-throughout, accurate, and precise approach for testing our hypothesis across a wide range of consumer plastics and environmental conditions.

Application: Tracking MW Changes of Plastics upon Photoirradiation. To demonstrate the applicability of DOSY for experimental work, we tracked the MW of a PS film with increasing photoirradiation exposure (Figure 4). The MW of PS decreased steadily for the first 6 days of exposure, from a starting value of 195 ( ± 4) kDa to an average value of 160 ( ± 5) kDa at day 6: a roughly 20% decrease from that of the initial value. After this time, the average MW remained constant, with a final measured value of 160 ( ± 3) kDa after 10 days of exposure. Here, larger standard deviations in the data or errors in the accuracy of the measurements could have been introduced by changes in the MW distribution upon photoirradiation. To investigate these changes, we subjected the acquired DOSY data of the time series samples to the same ILT data treatment used in Deconvoluting Different MW Distributions section for the PS standards (see Supporting Information S11). Overall, we saw an increase in lower MW constituents in the estimated distribution, consistent with the decrease in average MW. We observed this shift early in the irradiation (day 2), with minimal shifts in the estimated distribution afterward. Collectively, these initial findings successfully demonstrate the potential of using DOSY to track changes in the MW of consumer plastics as they are degraded by sunlight, a widely recognized yet incompletely constrained fate of plastics in the environment. 6 -8,26,27,29 -33

Comparison to GPC. In this study, we described, validated, and applied a DOSY method for polymer MW determinations, with a focus on applications for consumer plastics. Our results demonstrate the potential for DOSY to provide high- throughput, accurate, and precise measures of polymer MW, as well as the evolution of polymer MW during environmental weathering processes, such as photochemical degradation. Below, we describe distinct advantages of using DOSY over GPC, in terms of instrument versatility, methodological advantages, adaptability to user needs, and sample preparation.

Figure 4. Determined average MW of PS samples with increasing UVB irradiation time. Diamonds and error bars represent the mean values and one standard deviation from the mean, respectively, for triplicate samples at each time point, with each sample being measured one time. Dashed lines represent the linear interpolations between points and are shown to guide the eye.

<!-- image -->

The three following advantages highlight the versatility of the NMR instrument, for DOSY measurements and beyond, as compared to GPC instrumentation. First, when conducting DOSY experiments, the samples are isolated within a single NMR tube, as opposed to introduction of the sample into a chromatographic system. This self-containment means that different solvents that may be required for dissolving different polymers can be easily measured on the same instrument and probe, even back-to-back. This stands in contrast to GPC analysis, where dedicated instrumentation is optimized for a select polymer class at a time, given the need to match chromatographic column properties with polymer type and properties. Second, unlike GPC, performing the DOSY method does not require a dedicated NMR to perform experiments. Instead, users can share instrumentation, e.g., at an NMR facility, thereby distributing maintenance costs across a broader user base. This leads to the third advantage: because the samples are being analyzed on an NMR spectrometer, additional information about the polymer chemical composition (such as functional group identification 7,8 or observing chain branching in polyolefins 34,35 ) can be determined with alternative experiments (e.g., 1 H and 13 C, total correlation spectroscopy (TOCSY), or heteronuclear multiple-bond correlation spectroscopy (HMBC), etc.). Furthermore, when polymer end groups are known and produce resolvable NMR signals with sufficiently high S/N, number-averaged MW ( M n) can be determined using NMR by quantifying end-group integrals to those of the bulk polymer. 36 -38

Next, we identified two main methodological advantages of DOSY over GPC. Because DOSY measures a physical phenomenon, it offers higher accuracy and precision as compared to GPC. Herein, we have shown high reproducibility in repeated measures of the same sample (Figures 1 and 3). This stability also allows for infrequent calibration of the DOSY method. 39 A second methodological advantage of DOSY is the ability to analyze sample mixtures, 40 -42 while GPC can only separate samples based on retention time (i.e., MW) but not by structure.

An additional advantage is the adaptability of DOSY parameters to the user's analysis needs. The time of the DOSY experiment is mostly controlled by the number of individual gradient steps with varying intensities, the number of scans used per gradient step, and the diffusion time per scan. Here, we performed most experiments using 16 gradient steps with 16 scans each and long diffusion times (approaching the measured T1 relaxation times for each polymer), given that most experiments were at room temperature, which resulted in experiments of roughly 20 min per sample. While this time is on the order of typical GPC separation runs, the DOSY experiment time can be optimized by reducing the scan number or diffusion time accordingly. On the other hand, in cases where more sensitivity is needed, the scan number can be increased to improve signal-to-noise without having to further concentrate samples.

Finally, there are numerous sample preparation advantages for the DOSY vs GPC method. NMR requires much lower solvent volumes ( ∼ 0.5 mL) compared to GPC (tens of mL) per sample, lowering consumable costs and production volumes of hazardous waste. Moreover, samples for NMR can be prepared at the same concentration (Figure 1), independent of MW, whereas GPCrequires specific concentrations to be used for specific MW ranges. Additionally, DOSY offers an advantage over GPC in terms of sample size. Here, we have demonstrated the use of DOSYatconcentrations down to at least 0.3 mg mL -1 (i.e., ≤ 0.2 mg of the polymer needed), with the potential to run samples at even lower concentrations. These low sample requirements enable possibilities for sample analysis using DOSY that may not be feasible for GPC, such as analysis of natural samples. For example, in one study, ∼ 25% of plastic particles sampled from the North Atlantic weighed &lt;2.5 mg; the abundance of smaller particles may even be underestimated due to the use of 335 μ m mesh during sampling. 43 In such cases, validation work would be required to show that diffusion measurements of the polymer(s) can be distinguished from those of natural organic matter. The sample requirements demonstrated herein for DOSY (and further NMR analyses) of polymers could thus facilitate indepth characterization of microand nano-plastic particles collected from the environment.

## ■ CONCLUSIONS AND FUTURE OUTLOOKS

Summary of Methods and Applications. Our evaluation herein of applying DOSY to consumer plastics involved systematically assessing the effects of some methodology parameters (e.g., applied pulse sequence and polymer solution concentration and solvent composition) on the accuracy of DOSY measurements. These determinations demonstrated the importance for optimization of the method for each sample type. For instance, samples may require analysis using convection compensation, depending on the solvent. Also, solution concentration can be varied (e.g., to account for viscosity effects, sample size limitations, or desired signal intensities) but should be well-controlled throughout a sample set. Signal intensity can further be controlled by adapting the scan number, while diffusivities can be shifted by changing the analysis temperature. Changes to these parameters can be further optimized to minimize analysis time and therefore increase sample throughput. We also demonstrated the potential of DOSY to determine polydispersity of polymer samples, as well as to analyze polymer mixtures, which may have heterogeneous MWdistributions. We then demonstrated the use of DOSY to determine MWs of various polymers in different solvents. These polymers included standards of different thermoplastics used in consumer products, as well as water-soluble polymers. We complemented measurements of polymer standards with an initial screening of MWs for consumer products composed of two commercially important polymers: PS and PET. This screening highlights the potential use of DOSY for MW analysis of a variety of consumer plastic products. Finally, we demonstrated another specific application for rapid and facile MW determinations using DOSY by following decreases in polymer MW during photodegradation.

Opportunity for Further Developments. To further develop this approach, future work should focus on pushing forward the depth of information obtained from DOSY and the efficiency of performing the measurements. DOSY has been used previously to analyze sample mixtures, and this application can be further explored to differentiate co-polymer or mixedpolymer samples. 44,45 For instance, disperse or irregularly spaced functional groups, introduced intentionally or through transformation processes, may be identified preferentially on different polymer chain lengths. Moreover, while we demonstrated that MW distributions can be observed using DOSY, this particular aspect of the approach can be further developed, taking advantage of previously developed DOSY data processing techniques. 40,42,46 Finally, while we have performed our work on a 400 MHz NMR with an installed cryogenic probe, such equipment need not be limiting for the application of DOSY. Transferring this approach to smaller magnets, including benchtop NMRs, is feasible and could serve to broaden the accessibility of this promising analytical method. 47 While the work herein just scratches the surface of the potential for this approach, we propose that it is an important part of the polymer analytics toolbox, particularly for the analysis of plastic consumer products and other polymers in the environment, including monitoring their degradation over space and time.

## ■ ASSOCIATED CONTENT

## * sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.analchem.3c00655.

(S1) Data for polymer molecular weight standards. (S2) Selected parameter values for DOSY experiments. (S3) 1 H NMR spectra of polymer standards. (S4) Irradiance data of the photoirradiation setup. (S5) Effect of pulse program and Δ on measured diffusivity. (S6) Determination of molecular weight distributions using 16 gradient steps. (S7) Effect of gradient steps on the measured average molecular weight. (S8) Signal attenuation curves for different polymers. (S9) Stability over time of DOSY calibration for polystyrene. (S10) Measured MW values for consumer plastic products. (S11) Molecular weight distribution data for photoirradiated PS (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Authors

- Taylor F. Nelson -Department of Marine Chemistry and Geochemistry, Woods Hole Oceanographic Institution, Woods Hole, Massachusetts 02543, United States; Present
- Address: Department of Chemistry, University of Konstanz, 78457 Konstanz, Germany ; orcid.org/00000003-0719-4402; Email: taylor-frederick.nelson@uni.kn
- Collin P. Ward -Department of Marine Chemistry and Geochemistry, Woods Hole Oceanographic Institution, Woods Hole, Massachusetts 02543, United States; orcid.org/ 0000-0003-2979-0280; Email: cward@whoi.edu

Complete contact information is available at: https://pubs.acs.org/10.1021/acs.analchem.3c00655

## Author Contributions

T.F.N. conducted experiments and data analysis. T.F.N. and C.P.W. jointly conceived the concept and experimental plan and wrote the manuscript.

## Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

We thank Carl Johnson (WHOI) for assistance with NMR operation and maintenance, Anna Walsh (WHOI) for assistance with the radiometry measurements, and Christopher Reddy (WHOI) for constructive feedback on the findings. We thank Pauline Béziat for designing the TOC graphic. We acknowledge funding from the US National Science Foundation (MRI-OCE1828581 and CAS-MNP-2202621) and The Seaver Institute.

## ■ REFERENCES

- (1) Nunes, R. W.; Martin, J. R.; Johnson, J. F. Polym. Eng. Sci. 1982 , 22 , 205 -228.
- (2) Whitfield, R.; Truong, N. P.; Messmer, D.; Parkatzidis, K.; Rolland, M.; Anastasaki, A. Chem. Sci. 2019 , 10 , 8724 -8734.
- (3) Zumstein, M.; Battagliarin, G.; Kuenkel, A.; Sander, M. Acc. Chem. Res. 2022 , 55 , 2163 -2167.
- (4) [Mueller, R. J. Process Biochem. 2006 , 41 , 2124 -2128.](https://doi.org/10.1016/J.PROCBIO.2006.05.018)
- (5) Grause, G.; Chien, M.-F.; Inoue, C. Polym. Degrad. Stab. 2020 , 181 , No. 109364.
- (6) Walsh, A. N.; Mazzotta, M. G.; Nelson, T. F.; Reddy, C. M.; Ward, C. P. Environ. Sci. Technol. 2022 , 56 , 13810 -13819.
- (7) Meides, N.; Menzel, T.; Poetzschner, B.; Löder, M. G. J.; Mansfeld, U.; Strohriegl, P.; Altstaedt, V.; Senker, J. Environ. Sci. Technol. 2021 , 55 , 7930 -7938.
- (8) Maurer-Jones, M. A.; Monzo, E. M. ACSAppl. Polym. Mater. 2021 , 2021 , 1003 -1011.
- (9) Meunier, D. M.; Wade, J. H.; Janco, M.; Cong, R.; Gao, W.; Li, Y.; Mekap, D.; Wang, G. Anal. Chem. 2021 , 93 , 273 -294.
- (10) Tchir, W. J.; Rudin, A.; Fyfe, C. A. J. Polym. Sci. Polym. Phys. Ed. 1982 , 20 , 1443 -1451.
- (11) Li, W.; Chung, H.; Daeffler, C.; Johnson, J. A.; Grubbs, R. H. Macromolecules 2012 , 45 , 9595 -9603.
- (12) [Groves, P. Polym. Chem. 2017 , 8 , 6700 -6708.](https://doi.org/10.1039/c7py01577a)
- (13) Lewinski, P.; Sosnowski, S.; Kazmierski, S.; Penczek, S. Polym. Chem. 2015 , 6 , 4353 -4357.
- (14) Rosenboom, J.-G.; De Roo, J.; Storti, G.; Morbidelli, M. Macromol. Chem. Phys. 2017 , 218 , 1600436.
- (15) Zhou, X.; Pang, Z.; Cao, W.; Cao, Z.; Zhu, J.; Qi, Y.; Peng, X.; Kong, X. Anal. Chem. 2022 , 95 , 792 -801.
- (16) Cohen, Y.; Avram, L.; Frish, L. Angew. Chem., Int. Ed. 2005 , 44 , 520 -554.
- (17) Monakhova, Y. B.; Diehl, B. W. K.; Do, T. X.; Schulze, M.; Witzleben, S. J. Pharm. Biomed. Anal. 2018 , 149 , 128 -132.
- (18) Burger, R.; Rumpf, J.; Do, X. T.; Monakhova, Y. B.; Diehl, B. W. K.; Rehahn, M.; Schulze, M. ACS Omega 2021 , 6 , 29516 -29524.
- (19) [Hou, J.; Pearce, E. Anal. Chem. 2021 , 93 , 7958 -7964.](https://doi.org/10.1021/acs.analchem.1c00793?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
- (20) Gutiérrez, C.; García, M. T.; Gracia, I.; de Lucas, A.; Rodríguez, J. F. Waste Biomass Valoriz. 2013 , 4 , 29 -36.
- (21) Zhuang, G.-L.; Tseng, H.-H.; Wey, M.-Y. Chem. Eng. Res. Des. 2016 , 111 , 204 -217.
- (22) Mumbach, G. D.; Bolzan, A.; Machado, R. A. F. Polymer 2020 , 209 , No. 122940.
- (23) Farah, S.; Kunduru, K. R.; Basu, A.; Domb, A. J. Molecular Weight Determination of Polyethylene Terephthalate. In Poly(Ethylene Terephthalate) Based Blends, Composites and Nanocomposites ; Visakh, P. M., Liang, M., Eds.; William Andrew Publishing: Oxford, 2015; pp. 143 -165. DOI: 10.1016/B978-0-323-31306-3.00008-7.
- (24) Rochman, C. M.; Brookson, C.; Bikker, J.; Djuric, N.; Earn, A.; Bucci, K.; Athey, S.; Huntington, A.; McIlwraith, H.; Munno, K.; De Frond, H.; Kolomijeca, A.; Erdle, L.; Grbic, J.; Bayoumi, M.; Borrelle, S. B.; Wu, T.; Santoro, S.; Werbowski, L. M.; Zhu, X.; Giles, R. K.; Hamilton, B. M.; Thaysen, C.; Kaura, A.; Klasios, N.; Ead, L.; Kim, J.; Sherlock, C.; Ho, A.; Hung, C. Environ. Toxicol. Chem. 2019 , 38 , 703 -711.
- (25) Khaled, A.; Richard, C.; Jaber, F.; Sleiman, M. Phototransformation of Plastic Containing Brominated Flame Retardants: Enhanced Fragmentation and Release of Photoproducts to Water and Air. Environ. Sci. Technol. 2018, 52 , 11123 -11131, DOI: 10.1021/ acs.est.8b03172.
- (26) Ward, C. P.; Armstrong, C. J.; Walsh, A. N.; Jackson, J. H.; Reddy, C. M. Environ. Sci. Technol. Lett. 2019 , 6 , 669 -674.
- (27) Zhu, L.; Zhao, S.; Bittar, T. B.; Stubbins, A.; Li, D. J. Hazard. Mater. 2020 , 383 , No. 121065.
- (28) Nelson, T. F.; Reddy, C. M.; Ward, C. P. Environ. Sci. Technol. 2021 , 55 , 8898 -8907.
- (29) Walsh, A. N.; Reddy, C. M.; Niles, S. F.; McKenna, A. M.; Hansel, C. M.; Ward, C. P. Environ. Sci. Technol. 2021 , 55 , 12383 -12392.
- (30) Gewert, B.; Plassmann, M.; Sandblom, O.; Macleod, M. Environ. Sci. Technol. Lett. 2018 , 5 , 272 -276.

̈

- (31) De Hoe, G. X.; Zumstein, M. T.; Getzinger, G. J.; Ru egsegger, I.; Kohler, H. P. E.; Maurer-Jones, M. A.; Sander, M.; Hillmyer, M. A.; McNeill, K. Environ. Sci. Technol. 2019 , 53 , 2472 -2481.
- (32) Hebner, T. S.; Maurer-Jones, M. A. Environ. Sci. Process. Impacts 2020 , 22 , 398 -407.
- (33) Song, Y. K.; Hong, S. H.; Eo, S.; Han, G. M.; Shim, W. J. Environ. Sci. Technol. 2020 , 54 , 11191 -11200.
- (34) Jung, M.; Lee, Y.; Kwak, S.; Park, H.; Kim, B.; Kim, S.; Lee, K. H.; Cho, H. S.; Hwang, K. Y. Anal. Chem. 2016 , 88 , 1516 -1520.
- (35) Zhou, Z.; Paradkar, R.; Cong, R.; Qiu, X.; Fan, L.; Kuemmerle,
6. [R.; Moreno, A.; Czarniecki, B. Anal. Chem. 2020 , 92 , 8350 -8355.](https://doi.org/10.1021/acs.analchem.0c00834?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
- (36) Izunobi, J. U.; Higginbotham, C. L. J. Chem. Educ. 2011 , 88 , 1098 -1104.
- (37) Viéville, J.; Tanty, M.; Delsuc, M. A. J. Magn. Reson. 2011 , 212 , 169 -173.
- (38) Wackerly, J. W.; Dunne, J. F. J. Chem. Educ. 2017 , 94 , 1790 -1793.
- (39) Mazarin, M.; Viel, S.; Allard-Breton, B.; Thévand, A.; Charles, L. Anal. Chem. 2006 , 78 , 2758 -2764.
- (40) Chen, A.; Wu, D.; Johnson, C. S. J. Am. Chem. Soc. 1995 , 117 , 7965 -7970.
- (41) Van Gorkom, L. C. M.; Hancewicz, T. M. J. Magn. Reson. 1998 , 130 , 125 -130.
- (42) Antalek, B.; Hewitt, J. M.; Windig, W.; Yacobucci, P. D.; Mourey, T.; Le, K. Magn. Reson. Chem. 2002 , 40 , 60 -71.
- (43) Morét-Ferguson, S.; Law, K. L.; Proskurowski, G.; Murphy, E. K.; Peacock, E. E.; Reddy, C. M. Mar. Pollut. Bull. 2010 , 60 , 1873 -1878. (44) Hiller, W. Macromol. Chem. Phys. 2019 , 220 , 1900255.
- (45) [Grabe, B.; Hiller, W. Macromolecules 2022 , 55 , 8014 -8020.](https://doi.org/10.1021/acs.macromol.2c01505?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
- (46) Cobas, J. C.; Groves, P.; Martin-Pastor, M.; Capua, A. D. Curr. Anal. Chem. 2005 , 1 , 289 -305.

- (47) Lindner, S.; Burger, R.; Rutledge, D. N.; Do, X. T.; Rumpf, J.; Diehl, B. W. K.; Schulze, M.; Monakhova, Y. B. Anal. Chem. 2022 , 94 , 3997 -4004.

<!-- image -->