<!-- image -->

## Polymer Molecular Weights via DOSY NMR

<!-- image -->

ACCESS

ABSTRACT: Diffusion-ordered spectroscopy (DOSY) 1 H nuclear magnetic resonance ( 1 H NMR) has become a powerful tool to characterize the molecular weights of polymers. Compared to common characterization techniques, such as size exclusion chromatography (SEC), DOSY is faster, uses less solvent, and does not require a purified polymer sample. Poly(methyl methacrylate) (PMMA), polystyrene (PS), and polybutadiene (PB) molecular weights were determined by the linear correlation between the logarithm of their diffusion coefficients (D) and the logarithm of their molecular weights based on SEC molecular weights. Here, we emphasize the importance of the preparation needed to generate the calibration curves, which includes choosing the correct pulse sequence, optimizing parameters, and sample preparation. The limitation of the PMMA calibration curve was investigated by increasing the dispersity of PMMA. Additionally, by accounting for viscosity in the Stokes -Einstein equation, a variety of solvents were used to produce a

*

sı

<!-- image -->

'universal' calibration curve for PMMA to determine molecular weight. Furthermore, we place a spotlight on the increasing importance of DOSY NMR being incorporated into the polymer chemist's toolbox.

P olymers are an important class of functional materials that play a key role in society. The properties and performances of polymers are correlated to their molecular weights (MW). Therefore, the determination of molecular weight is vital for synthesizing and designing polymers. Controlled/ 'Living' radical polymerization (CRP) allows the synthesis of polymers with predetermined molecular weights and narrow dispersities. Although there are many various techniques of CRP, such as reversible addition -fragmentation chain transfer (RAFT), atom transfer radical polymerization (ATRP), and nitroxide-mediated polymerization (NMP), they all center around polymers with similar number-average molecular weight ( M n) and weight-average molecular weight ( M w) to produce polymers of narrow dispersity ( Đ ). These techniques are commonly used on mono such as styrene, acrylates, methacrylates, and acrylamides. , The development of sizeexclusion chromatography (SEC) as a rapid method to determine MW and Đ has driven the growth of polymer chemistry and has become the crown jewel in many polymer facilities. Unfortunately, the SEC has many inherent drawbacks: SEC is time-consuming, with the average data retrieval time averaging 40 min; it requires relatively pure samples and consumes copious amounts of solvent; switching to different solvents is difficult and time-consuming; chromatography columns age, thus requiring frequent calibration and replacement; and finally, SEC has been reported to retain a 10 -20% systematic error even with calibration. Many polymer start-up facilities do not have access to the SEC due to the highly specialized investment, while many other types of analytical equipment are typically shared resources. Even with these drawbacks, SEC is still one of the most widely used methods for the determination of polymer molecular weights.

Diffusion-ordered spectroscopy (DOSY) NMR, an alternative to SEC, provide diffusion coefficients of molecules related to their hydrodynamic radius and molecular weights. In the early years, when DOSY was first employed, it was used to determine the diffusion coefficients of small molecules. However, in 1995, Johnson et al. applied DOSY to determine the molecular weight of poly(ethylene oxide) in D2O by creating a calibration curve using monodisperse reference standards and utilizing the linear correlation of the logarithm of the diffusion coefficient (log D) to the logarithm of the molecular weights (log MW).

This method of acquiring MW gives DOSY NMR many advantages over SEC. Due to the low sample concentration, the purity of the polymer is not as essential compared to SEC; thus, reducing preparation time. DOSY also requires minimum amounts of solvent, and the overall process is faster than SEC. DOSY does not require frequent calibration, making the process more robust. Finally, the characterization of polymer molecular weights via DOSY NMR does not require high-end probes or specialized gradient equipment. Therefore, polymer facilities without access or means to SEC are able to analyze polymer MW reliably via a more accessible method.

Received:

December 11, 2022

Accepted:

April 24, 2023

Published:

May 5, 2023

<!-- image -->

Article To determine polymer molecular weights, a calibration curve needs to be generated, and only then, interpolated molecular weights can be produced. Generating the calibration curves is not intuitive, and many factors affect the quality (choosing the correct sample concentration, pulse sequence, pulse parameters, solvent viscosity, and temperature). If these factors are not treated with care, unwanted systematic deviations will arise, producing an unreliable calibration curve. It should be noted that the polymer molecular weights reported throughout this manuscript are weight averages and not number averages.

Theory. The diffusion coefficient is dependent on solvent viscosity ( η ) and absolute temperature. This can be seen in the Stokes -Einstein equation ( ), where the diffusion coefficient is described for a spherical particle with a hydrodynamic radius ( R H), and k is the Boltzmann constant.

$$D = \frac { k T } { 6 \pi \eta R _ { H } } & & \text {eases} & & \text {days} & & \text {days} & & \text {days}$$

R H can be correlated to the molecular weight of the polymer via the Rouse-Zimm model ( ).

$$R _ { H } \sim b M ^ { \alpha } & & ( 2 ) & \quad \text {poly}$$

In which α and b are arbitrary parameters, and M is the molecular weight. Incorporating into , the diffusion coefficient and molecular weight are correlated to produce a new equation ( ), with A being the adjusted proportionality factor.

$$D = A M ^ { - \alpha }$$

can be linearized by taking the logarithm of both sides to transform the equation to produce .

$$\log D = - \alpha \log M + \log A & & ( 4 ) & \quad \text {con}$$

To determine the diffusion coefficient ( D ) via NMR, Stejskal and Tanner developed a specialized DOSY experiment known as the Pulsed Gradient Spin Echo (PGSE) experiment, which measured the diffusion coefficient of a molecule in a host liquid via NMR. They found that the normalized signal amplitude ( E / E 0 ) decays as a Gaussian curve with increasing gradient pulse amplitude, g (G/cm 2 ), to yield .

$$\frac { E } { E _ { 0 } } = \exp \left ( - \gamma ^ { 2 } \delta ^ { 2 } g ^ { 2 } \left ( \Delta - \frac { \delta } { 3 } \right ) D _ { s } \right ) \\ \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

In this equation, γ is the gyromagnetic ratio of the nucleus, δ and Δ are the duration and separation of the gradient pulses, respectively, and Ds is the self-diffusion coefficient of the molecule. To obtain the diffusion coefficient, can be linearly transformed to produce , where the slope is the diffusion coefficient.

$$d i s h i s t h e c o m i c t . & & \text {espe} \\ x = \gamma ^ { 2 } \delta ^ { 2 } g ^ { 2 } ( \Delta - \delta / 3 ) & & \text {cool} \\ y = \ln \left ( \frac { E } { E _ { 0 } } \right ) & & \text {M} \\ y = - D x & & \text {e} \quad ( 6 ) \\ & & \text {is} \ \text {gevly} \ \text {inferred} \ \text {by} \ \text {the} \ \text {acquisition} \\$$

is heavily influenced by the acquisition parameters, such as pulse strength, gradient range, diffusion delay, and pulse programs. This can be overwhelming for polymer chemists unfamiliar with DOSY. utilizes the decay of the polymer signal intensity to determine ( D ). A complete decay of signal intensity would be observed for small molecules in the 10 -1000 Da range with a 5 -25% gradient range, but the signals for the large molecules (10 5 Da) have a small decay, and the processing software may interpret this as a baseline artifact rather than a true NMR signal. No signals would be observed from small molecules with a gradient range of 25 -95% because their intensity would have decayed to zero before the first DOSY data point was collected at 25% gradient strength. However, the diffusion properties of large molecules would be observed. The ideal parameters for the gradient range are that the smallest molecules should maintain a strong, almost 100% intensity at the lowest gradient strength, while the largest molecules should experience a signal decay of &gt;95% by the final gradient strength. Therefore, a typical gradient range used for DOSY experiments is 5 -95%. We used constant values of Δ and δ for our experiments. This made it easier to compare datasets obtained on different samples and days.

Critical Concentration. Polymer chains tend to swell in a good solvent, thus restricting chain motion through physical interactions. These interactions increase with increasing concentration, thus reducing the diffusion coefficient of the polymer. Therefore, the polymer samples should be under sufficiently dilute conditions, where polymer chain interactions have a negligible impact on the diffusion coefficient. Otherwise, this will lead to inconsistent data to estimate polymer molecular weights. Hou et al. reported that polymer concentrations need to be below the critical overlap concentration ( C * ); however, a majority of polymer diffusion studies illustrate that one only needs to be sufficiently dilute or close to C * (typ l etween 0.5 and 4.5 mg/mL) to obtain accurate results. , -In this report, we agree with the majority since reliable data was obtained using sample concentrations of 0.5 mg/mL to accurately estimate polymer molecular weights.

Choice of Solvent and Pulse Program. For our studies, deuterated chloroform (CDCl3) was used as the solvent because of its ability to solubilize a wide variety of polymers. However, due to the inherent properties of chloroform (low viscosity and low boiling point), convection currents were inherent in the NMR tube, which resulted in inconsistent data. Therefore, we used a pulse sequence that minimizes magnetization decay due to translational motion arising from convection currents associated with temperature gradients across the sample, thus providing convection compensation. The BRUKER dstebpg3s pulse sequence incorporates a double stimulated echo (dste) segm ith three spoil gradients to suppress convection currents. , Convection currents occur due to slight variations in temperature and are prevalent in ambient conditions for solvents of low viscosity. This is especially true with instruments employing cryogenically cooled NMR probes. Therefore, this pulse sequence was critical to running diffusion experiments.

## ■ EXPERIMENTAL SECTION

Materials. Poly(methyl methacrylate) (PMMA), polystyrene (PS), and polybutadiene (PB) standards with low dispersity ( Đ ) were purchased from Polymer Laboratories and used as received. Methyl methacrylate (MMA) and styrene were purchased from TCI laboratories and purified through basic alumina prior to polymerization. 4-Cyano-4(phenylcarbonothioylthio)pentanoic acid (CPDB) was purchased from Millipore Sigma and used as received. Dimethylformamide (DMF), methanol, toluene, tetrahydrofur- an (THF), and azobis(isobutyronitrile) (AIBN) were obtained from Aldrich Chemical Co. and used as received.

RAFT Polymerizations. In a Schlenk flask, MMA (2.7 mg), CPDB (5 mg), AIBN (0.587 mg), and 5 mL of DMF were subjected to 4 freeze-pump -thaw cycles and backfilled with nitrogen. The reaction mixture was heated at 65 ° C with stirring. Polymer samples were removed from the heat at various times and precipitated by the addition of methanol. The samples were subjected to centrifugation at 6000 rpm for 5 min. The samples were then redissolved in THF, precipitated again in methanol, and centrifuged at 6000 rpm for 5 min. This process was repeated a total of three times. The samples were then dried overnight in a vacuum oven at 25 ° C to remove residual solvent.

Conventional Free Radical Polymerizations. In a round-bottom flask, MMA (3.37 mg), AIBN (154 mg), and 4 mL of toluene were sparged with argon for 15 min. The reaction mixture was heated at 65 ° C with stirring. Polymer washing was conducted by the same method as described in RAFT polymerization.

NMR. All NMR experiments were performed at 25 ± 0.1 ° C. All NMR samples were stabilized at 25 ° C (uncalibrated) before data collection. Each NMR sample consisted of 0.5 mg of polymer per 1 mL of CDCl3. Each NMR tube contained 0.5 mL of solution to keep convection at a minimum and data consistent. DOSY experiments were performed on a Bruker Avance III-HD 400 MHz spectrometer fitted with a 5 mm o.d. broadband (liquid nitrogen-cooled) Prodigy cryo-probe capable of generating 0.53 T/m with a maximum of 10 A of current. The gradient range and pulse parameters varied for each solvent (see ). 1 H NMR spectra were obtained, phased, and baseline corrected as needed prior to each DOSY experiment. DOSY spectra were processed by Topspin 3.6.1 software. The time domain data was processed with 2 Hz exponential line broadening with 2 × zero filling. Diffusion coefficients were obtained through the inverse Laplace transformation after polynomial baseline correction using the default automatic integration in Topspin 3.6.1. 1 H DOSY measurements were performed at 25 ° C. The pulse program used was the BRUKER double-stimulated echo sequence dstebpg3s, unmodified in Topspin version 3.6.1. All samples were run without spinning. Calibration curves were produced by the correlation of the diffusion coefficient of polymer standards and their respective molecular weights.

SEC Characterization. SEC characterization of PMMA synthesized via RAFT polymerization to determine weight average molecular weights (Mw) and dispersities ( Đ ) was conducted using a gel permeation chromatography system equipped with a Varian 290-LC pump, a Varian 390-LC refractive index detector, and three Styragel columns (HR1, HR3, and HR4 having molecular weight ranges of 100 -5000, 500 -30000, and 5000 -500000, respectively). THF was used as an eluent for SEC at 30 ° C and a flow rate of 1.0 mL min -1 . SEC was calibrated with poly(methyl methacrylate) (PMMA), polystyrene (PS), and polybutadiene (PB) standards obtained from the Polymer Standards Service.

## ■ RESULTS AND DISCUSSION

Sample Concentration and Pulse Program. The first attempt to create a calibration curve from PMMA standards revealed the importance of using the correct parameters, sample preparation, and pulse program. As seen in , the PMMA stock solution of 6 mg/mL was well above the critical concentration. This resulted in chain overlap, producing a non-linear fit. Another problem arose in with the utilization of the improper pulse program: ledbpgp2s (longitudinal eddy current delay experiment using bipolar gradients). Chloroform is a low-viscosity solvent and is susceptible to convection currents. These currents lead to markedly different diffusion coefficients for replicate measurements ( ). Ledbpgp2s does not compensate for convection currents, so a slightly more viscous solvent (Benzene-d6) was employed. An improved calibration curve was created ( ) by utilizing a sufficiently dilute solution

Figure 1. PMMA calibration curve in CDCl3 [6 mg/mL]. Non-linear and irreproducible data is indicative of samples above the critical concentration and evidence of convection currents.

<!-- image -->

Figure 2. PMMA calibration curve in Benzene-d6 [0.5 mg/mL] at sufficiently dilute conditions showing evidence of convection currents by variations of the diffusion coefficient at Log MW = 4.3.

<!-- image -->

(0.5 mg/mL) near the critical concentration and a more viscous solvent (Benzene-d6) to suppress convection. A linear trend was apparent; however, convection was still prominent.

By switching the solvent back to CDCl3 and using the correct pulse program (dstebpg3s), we were able to compensate for convection. depicts a linear calibration curve for PMMA in CDCl3. The value of the Rouse-Zimm scaling parameter α falls in the range of the previo ported literature ( α = 0.47 -0.61) for PMMA in CDCl3. - We have also investigated calibration curves for two other polymers in CDCl3: polystyrene and polybutadiene. The acquisition parameters for these polymers were the same as the parameters for PMMA in CDCl3. Both curves show excellent correlation between SEC and DOSY when measured using the recommendations stated herein (see ).

Figure 3. PMMA calibration curve in CDCl3 near critical concentration (0.5 mg/mL) with negligible convection effects.

<!-- image -->

Dispersity Studies. To test the limitations of the calibration curve, we analyzed PMMA samples with increasing dispersity. Since SEC inherently produces 10 -20% error after calibration, we used this range as our accepted window of error. PMMA samples were synthesized using RAFT polymerization. The MWs of PMMA samples synthesized by RAFT were analyzed through SEC. The samples were then analyzed by DOSY NMR to determine their diffusion coefficients. The molecular weights of the samples obtained by SEC (black squares) were then compared against the calibration curve (green line) produced from the fitted line from .

shows good correlation of the diffusion coefficient for both SEC and DOSY molecular weights for samples in the dispersity range 1.07 -1.19 as the data points align nicely on the calibration curve. It is clear that the difference in the weight-average molecular weight between SEC and DOSY is minimal and below 20% error, producing a reliable determination of MW.

presents similar results for PMMA samples with a dispersity range of 1.2 -1.28 (red) superimposed on the calibration curve (green line) from . The samples have a higher error compared to the previous, but all fall below the 20% error mark, resulting in an agreeable correlation between SEC and DOSY. The samples that deviate farther from the calibration curve are of high MW, and the error may be due to the higher concentration of longer chains in the solution, causing the data to shift below the calibration curve.

The calibration curve becomes unreliable for PMMA samples with a dispersity of 1.3 and greater ( a). Most samples are outside of the accepted error, which can be seen in b. SEC data indicates significant tailing correlated to a high degree of small chains in the polymer sample. The small chains are hypothesized to skew the diffusion data to produce higher diffusion coefficients.

Figure 4. Diffusion coefficients for PMMA samples with a dispersity of 1.07 -1.19 (black squares).

<!-- image -->

Figure 5. Diffusion coefficients for PMMA samples with a dispersity of 1.2 -1.28 (red) compared to the calibration curve (green).

<!-- image -->

Viscosity Correction. An inherent drawback of SEC is the difficulty of switching solvent systems. This is especially problematic for polymers that are not soluble in many of the solvents used for SEC. Recent literature sheds light on creating a universal calibration curve for various deuterated solvents by incorporating solvent viscosity. Due to the dilute sample conditions, the diffusion coefficient of the polymers is heavily dependent on the viscosity of the solvent. By adjusting parameter (A) in to negate the viscosity of the solvent ( ), a universal calibration curve can be created for the polymer in various solvents ( ). It should be noted that each solvent required different processing parameters due to the changes in viscosity (see ).

$$D \eta & = A M ^ { - \alpha } \\ \log D + \log \eta & = \alpha \log M + \log A$$

a depicts the calibration curves of PMMA in benzene-d6, CDCl3, acetone-d6, and DMSOd 6 . The difference in the diffusion coefficients is mitigated when viscosity correction is employed. Differences in slopes may be due to differences in the coiling of the polymers in each solvent as well as the variation in the processing parameters obtained for the experiments (see ). However, when viscosity correction is incorporated, the curves overlay each other ( b). The universal calibration curve is fairly accurate for low to intermediate MW PMMA, but the differences in the slopes become more prominent for high MW (around 214,000 kDa), producing a curve with a higher degree of error.

Figure 6. Diffusion coefficients for PMMA samples with broad dispersities (a, top). Effect of PMMA dispersity ( Đ ) on measurement error (b, bottom). PMMA samples of high dispersity have greater than 20% error, and the calibration curve becomes unreliable.

<!-- image -->

## ■ CONCLUSIONS

We have investigated several critical parameters and pulse programs for the determination of polymer molecular weights using DOSY NMR. The first is the importance of utilizing the proper parameters and pulse programs to create a calibration curve for determining polymer molecular weights using DOSY NMR. Solvents of low viscosity are susceptible to convection currents, which significantly affect the diffusion data. Utilizing convection compensation pulse programs negates the effects of the convection currents and allows the user to retrieve reliable diffusion data to obtain a dependable calibration curve. Further investigations were employed to determine the reliability of the calibration curves by increasing PMMA dispersity. We have shown there is a correlation between the accuracy of the calibration curve and the dispersity, where dispersities greater than 1.3 exhibit significant deviations from the original calibration curve. This is most likely due to a higher concentration of low-molecular-weight chains in the polymer sample, resulting in a higher diffusion coefficient. Therefore, this method should be used only for polymers synthesized via known methods that have been documented to depress the dispersity and ensure reliable accuracy. The application of a viscosity correction to the calibration curve of PMMA in various deuterated solvents provided improved correlations. The curves yield reasonable reliability for low and intermediate molecular weights but deviate at higher molecular weights. This may be due to the probe/system's gradient of only 0.53 T/m which is limited to polymers of intermediate molecular weights. In order to improve the accuracy of the diffusion study with high molecular weight polymers (&gt;200 kDa), specialized gradient equipment should be used. Finally, using the recommendations presented in this study, we obtained calibration curves for polystyrene and further extended the technique to polybutadiene.

Figure 7. Diffusion coefficients determined via DOSY for PMMA standards in a series of deuterated solvents (a, top) and viscositycorrected data for the same measurements (b, bottom).

<!-- image -->

## Analytical Chemistry

This technique is limited to known polymerization methods which produce polymers of low dispersity. However, for the many polymerization methods producing narrowly dispersed polymers, DOSY is a useful alternative to SEC for the determination of polymer MW. This method may find further utility in lowering costs and QC testing of repeat batches when the dispersity characteristics are well documented.

## ■ ASSOCIATED CONTENT

## * sı Supporting Information

The Supporting Information is available free of charge at .

Molecular weights and dispersities for viscosity correction studies, acquisition parameter of PMMA in various solvents, and calibration curves for polystyrene and polybutadiene ( )

## ■ AUTHOR INFORMATION

## Corresponding Author

Brian C. Benicewicz -Department of Chemistry and Biochemistry, University of South Carolina, Columbia, South Carolina 29203, United States; ; Email:

## Authors

Eric Ruzicka -Department of Chemistry and Biochemistry, University of South Carolina, Columbia, South Carolina 29203, United States;

Perry Pellechia -Department of Chemistry and Biochemistry, University of South Carolina, Columbia, South Carolina 29203, United States

Complete contact information is available at:

## Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

This work was supported by the U.S. Department of Energy, Office of Science, Basic Energy Sciences, under Award # DESC0018135.

## ■ REFERENCES

- (1) Grubbs, R. B.; Grubbs, R. H.
- (2) Sharker, K. K.; Takeshima, S.; Toyama, Y.; Ida, S.; Kanaoka, S.; Yusa, S.
- (3) Perrier, S.
- (4) Berek, D.
- (5) Pregosin, P. S.; Kumar, P. G. A.; Fernández, I.
- (6) Chen, A.; Wu, D.; Johnson, C.
- (7) Stejskal, E. O.; Tanner, J. E.
- (8) Groves, P.
- (9) Gong, X.; Hansen, E. W.; Chen, Q.
- (10) Hou, J.; Pearce, E.
- (11) Hiller, W.

̀

- (12) Barre re, C.; Mazarin, M.; Giordanengo, R.; Phan, T. N.; Thevand, A.; Viel, S.; Charles, L.

̊

- (13) Ha kansson, B.; Nydén, M.; Söderman, O.
- (14) Viel, S.; Capitani, D.; Mannina, L.; Segre, A.
- (15) Li, W.; Chung, H.; Daeffler, C.; Johnson, J.; Grubbs, R.
- (16) Jerschow, A.; Muller, N.
- (17) DOSY/Diffusion on Avance III Spectrometers Last Update: 11 Feb 2020 (cgf).
- (18) Ortner, K.; Sivanandam, V.; Buchberger, W.; Muller, N.
- (19) Guo, X.; Laryea, E.; Wilhelm, M.; Luy, B.; Nirschl, H.; Guthausen, G.
- (20) Auge, S.; Schmit, P. O.; Crutchfield, C.; Islam, M.; Harris, D.; Durand, E.; Clemancey, M.; Quoineaud, A. A.; Lancelin, J. M.; Prigent, Y.; et al.
- (21) Von Meerwall, E. D.; Amis, E.; Ferry, J. D.
- (22) Voorter, P. J.; Mckay, A.; Dai, J.; Paravagna, O.; Cameron, N. R.; Junkers, T.

<!-- image -->

CAS BIOFINDER DISCOVERY PLATFORM™M

## BRIDGE BIOLOGY AND CHEMISTRY FOR FASTER ANSWERS

Analyze target relationships, compound effects, and disease pathways

## Explore the platform

<!-- image -->