<!-- image -->

pubs.acs.org/ac Article

## The Universal Calibration for Structure- and Solvent-Independent Molar Mass Determinations of Polymers Using Diffusion-Ordered Spectroscopy

[Wolf Hiller * and Bastian Grabe](https://pubs.acs.org/action/doSearch?field1=Contrib&text1=%22Bastian+Grabe%22&field2=AllField&text2=&publication=&accessType=allContent&Earliest=&ref=pdf)

Cite This: Anal. Chem. 2023, 95, 18174-18179

<!-- image -->

## ACCESS

Metrics &amp; More Article Recommendations

<!-- image -->

<!-- image -->

ABSTRACT: It will be shown how diffusion-ordered spectroscopy (DOSY) can produce a universal calibration of molar mass dependences of polymers compared to size exclusion chromatography (SEC) or recently published DOSY methods. Whereas SEC can deliver only structure-independent universal calibrations for a particular solvent, DOSY was used for creating solvent-independent calibrations for a certain polymer. Now, we can demonstrate a universal calibration method that generates both a structureand solvent-independent molar mass calibration. Only one mathematical function describes the structure- and solvent-independent calibrations for DOSY by implementing the Mark -Houwink approach. The derived equation is tested on polystyrene (PS), poly(ethylene oxide), and poly(methyl methacrylate) of different molar masses and in Supporting Information

<!-- image -->

<!-- image -->

different solvents. Altogether, 94 diffusion coefficients representing 16 molar mass calibrations of the diffusion coefficients in 10 different solvents could be perfectly matched to one universal calibration function with an average deviation of just 2.5%. It was also found that the Mark -Houwink parameters calculated by DOSY are very close to the SEC data. In any case, this new approach is a very useful tool for the determination of molar masses and new Mark -Houwink parameters via DOSY.

## ■ INTRODUCTION

The expression universal calibration is very much related to size exclusion chromatography (SEC) in polymer analysis. SEC is the most important method for determining the molar masses of polymers. In order to determine the molar mass and, particularly, the molar mass distribution of a polymer, it is necessary to measure a molar mass calibration curve with polymer standards of the same structure and different molar masses. The SEC equipment and the chromatographic conditions must be kept unchanged for comparison. However, it is not always possible to create a calibration curve for each new polymer. Therefore, it is a very useful tool to create a universal calibration that combines the molar mass calibrations of different polymers into a unique calibration curve in the same solvent. This method is based on the fact that polymers eluting at the same retention time also have the same hydrodynamic volume. According to Flory theory, 1 the intrinsic viscosity [ η ] is related to the hydrodynamic volume V h and the molar mass M by

<!-- formula-not-decoded -->

where N A is the Avogadro constant. Therefore, two polymers of the same hydrodynamic volumes can be described by eq 2: 2

<!-- image -->

<!-- formula-not-decoded -->

The intrinsic viscosity can also be expressed by the Mark -Houwink relation (also called Kuhn -Mark -Houwink -Sakurada equation): 3

<!-- formula-not-decoded -->

where K and a are experimental parameters. Including eq 3 into eq 2, the experimental determination of Mark -Houwink parameters K and a can be performed via SEC.

<!-- formula-not-decoded -->

If K 1 and a 1 are known for one polymer in a certain solvent, then K 2 and a 2 of the other polymer can be easily calculated.

Meanwhile, diffusion-ordered spectroscopy (DOSY) is used quite often in polymer science. It can quantify the sizes of molecules by using the Stokes -Einstein relation: 4

Received:

August 24, 2023

Revised:

November 9, 2023

Accepted:

November 9, 2023

Published:

November 28, 2023

<!-- image -->

<!-- formula-not-decoded -->

where D is the diffusion coefficient, η is the dynamic viscosity, k B is the Boltzmann constant, and T is the absolute temperature. However, DOSY can also be used for the determination of molar masses of polymers by using the power scaling equation for the diffusion coefficient derived from the Rouse -Zimm model 5,6

<!-- formula-not-decoded -->

where b is the Flory parameter and c is a constant. The molar mass determination via DOSY is similar to that via SEC because it also requires a molar mass calibration of the diffusion coefficient with polymer standards of different molar masses. This calibration allows the determination of average molar masses, as well as molar mass distributions of polymers.

The main problem of the molar mass determination is related to the fact that the polymer standards have to be of the same type as the investigated polymer, and the calibration has to be done in the same solvent and also at several other conditions. In other words, the calibrations of the diffusion coefficients are dependent on the structure of the polymer, the viscosity of the solvent, temperature, concentration, and also the experimental NMR setup. Temperature, concentration, and experimental conditions can be easily controlled. The temperature and concentration must be set exactly to a fixed value. The other experimental conditions can also be kept constant. Particularly, the pulsed field gradient strength should be calibrated to a certain diffusion coefficient of a standard compound to allow the accurate determination of hydrodynamic radii at a certain calibrated temperature of the NMR spectrometer. The DOSY experiment should also be robust against convection to eliminate deviations in the diffusion coefficients. Finally, it is necessary to have DOSY calibrations of several polymer standards in different solvents. Meanwhile, many papers are published containing molar mass calibrations of diffusion coefficients for different polymers. 7 -19 Furthermore, Arrabal-Campos et al. 20 and recently Voorter et al. 21 and Ruzicka et al. 22 also showed calibrations of the diffusion coefficients for certain polymer standards by including the viscosity of the solvents. These solvent-independent calibrations were published for polystyrene (PS), 20,21 poly(ethylene oxide) (PEO), 21 and poly(methyl methacrylate) (PMMA), 22 respectively. In these cases, an individual setup for each polymer was given by adjusting the diffusion coefficient with the dynamic viscosity of the solvent. This setup certainly improves the molar mass calibrations of polymers in different solvents. However, this method is only valid for the given polymer, and stronger deviations are expected from the average function if this function is applied to another polymer. We were thinking about the possibility of developing a universal calibration for DOSY that is solventand structureindependent. Such universal calibration would provide the possibilities of both SEC and the current DOSY capabilities together because SEC provides only the structure-independent calibration in a certain solvent, and the current DOSY developments deliver the solvent-independent calibration for a certain polymer.

This paper will show how the calibrations can be further improved regarding accuracy and particularly include other polymers in different solvents as well. This calibration approach will be a more general universal calibration that can be used for both different structures and different solvents as well. One uniform function will be derived representing the structure- and solvent-independent universal calibration.

## ■ EXPERIMENTAL SECTION

The polystyrene, poly(ethylene oxide), and poly(methyl methacrylate) standards were purchased from PSS GmbH (now Agilent Technologies). All samples are summarized in Table S1. The sample solutions were prepared at a constant concentration of 1 mg · mL -1 . The total volume of the polymer solutions was 0.55 mL in 5 mm NMR tubes.

The DOSY experiments were performed on the 600 MHz spectrometers AVANCE NEO and AVANCE III HD from Bruker BioSpin GmbH. Both spectrometers were equipped with helium cooled 5 mm cryoprobes. The DOSY experiments were carried out with the Bruker dstebpgp3s pulse sequence using double stimulated echo for convection compensation and longitudinal eddy current delay (LED) with bipolar gradients for diffusion and three spoil gradient pulses. 23 32 gradient strengths were linearly varying between 3 and 98% of the maximum gradient strength. The maximum gradient strength was calibrated to the so-called doped water test sample (1% H2O in D2O) with a diffusion coefficient of 1.91 × 10 -9 m 2 /s at 298.15 K. The gradient pulse lengths and diffusion delays for each polymer and solvent are displayed in Table S2. The acquisition parameters are acquisition time 1.8 -2.7 s (32 kb data) and spectrum window optimized to the relevant chemical shifts ( ∼ 10 -15 ppm), relaxation delay 2.5 s, 16 scans per gradient strength, and 16 dummy scans. All DOSY experiments were measured twice or three times at the calibrated temperature of 298.15 K. The processing was done with zero filling of 64 kb data points in F2 and 1 kb data points in F1 using an exponential window function with a line broadening of 1 Hz. The diffusion coefficients were calculated by integrating the most unique signals of the polymers and fitting the integrals to the monoexponential Stejskal -Tanner equation 24 with the corrected little and big delta delays given for the pulse sequence dstebpgp3s in Table S2. In this case, between two and six diffusion coefficients could be determined per sample, where the average value was used for the molar mass determination.

## ■ RESULTS AND DISCUSSION

The following theoretical considerations for the universal calibration of DOSY will be described. A general equation for the diffusion coefficient will be derived by including the Mark -Houwink relation.

In order to adopt the Mark -Houwink setup to DOSY, we have to derive an adequate expression of the diffusion coefficient equivalent to eq 2 or (eq 4). In this case, V h in eq 1 will be replaced by

<!-- formula-not-decoded -->

with the hydrodynamic radius r h according to the Stokes -Einstein equation. In the case of DOSY, the size of the two polymers is comparable if both polymers have the same hydrodynamic radius.

The combination of eqs 1, 3, and 7 will yield the following expression

<!-- formula-not-decoded -->

Equation 8 relates the diffusion coefficient to the intrinsic viscosity and therefore to the Mark -Houwink equation and combines it with the dynamic viscosity. Consequently, it is also possible to quantitatively compare two different polymers according to their Mark -Houwink parameters via DOSY in different solvents. In this case, one polymer will act as the reference with the known Mark -Houwink parameters K 1 and a 1 . This is the same approach as in SEC. Finally, the following ratio for two polymers can be derived from eq 8 for a given temperature T :

<!-- formula-not-decoded -->

The index 1 represents the reference polymer, and index 2 belongs to the second polymer with the unknown parameters K 2 and a 2 . In order to use the diffusion coefficients as the only experimental variables for the determination of K 2 and a 2 in eq 9, the remaining variable M has to be replaced by the power scaling of the diffusion coefficient. Thus, including eq 6 into eq 9, the relation of the diffusion coefficients of the two polymers results in the following equation (for details, see the SI):

<!-- formula-not-decoded -->

with

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Equation 10 now allows the determination of the Mark -Houwink parameters K 2 and a 2 of any polymer and in any solvent on the basis of a reference polymer and the molar mass dependences of the diffusion coefficients of both polymers. The parameters b 1 , b 2 , c 1, and c 2 will be obtained from the molar mass dependences of the diffusion coefficients with eq 6. The parameters K 1 and a 1 are used as the reference pair. This can be taken from the literature data. K 2 and a 2 are calculated by fitting eq 10 to the D 2 and D 1 diffusion coefficients of the two molar mass dependences, where D 2 and D 1 are always referring to the same M w values. One molar mass dependence is represented by the reference polymer consisting of D 1i ( M wi ) with known K 1 and a 1 and the other is given by D 2i ( M wi ) with unknown parameters K 2 and a 2 . As a result of the fit, K 2 and a 2 are obtained.

It should be noted that these K 2 and a 2 parameters are primarily relevant for DOSY only. It is not the main issue of this DOSY procedure to create intrinsic viscosity data with DOSY. It is rather the focus of DOSY to improve the molar mass determination via diffusion coefficients by using Mark -Houwink parameters, which were produced by DOSY. Therefore, the accuracy of the universal DOSY calibration will also be dependent on the kind of experiment used for determining the Mark -Houwink parameters. In other words, it might be that Mark -Houwink parameters determined via SEC or viscometry are not providing exactly the same molar mass as that determined via DOSY.

Equation 10 now has two remarkable features: First, the equation will be used for determining Mark -Houwink parameters of polymers of different structures as well as in different solvents, which are valid for DOSY. Second, it will be used now to create the universal molar mass calibration, which is structure- and solvent-independent.

The main goal, however, is the determination of one universal molar mass calibration function for DOSY that is valid for different polymers as well as different solvents. Therefore, the molar mass dependences of the three polymers were measured in several solvents in order to provide one universal calibration function for all diffusion coefficients of these polymers. Figure 1 shows the molar mass dependences of

Figure 1. Diffusion coefficients vs molar masses for PS, PEO and PMMA in different solvents at T = 298.15 K.

<!-- image -->

the diffusion coefficients for polystyrene (PS), poly(ethylene oxide) (PEO), and poly(methyl methacrylate) (PMMA) in several solvents. The details of the polymers and the experimental DOSY conditions are given in the experimental part and Tables S1 and S2 in the SI. The diluted solutions of 1 mg · mL -1 are required for describing the molar mass dependences of the diffusion coefficients by only one slope (Flory parameter) in the range of 0.5 -0.6 depending on the polymer and solvent. Higher concentrations can cause the formation of entanglements of the polymer chains and provide molar mass dependences with two slopes. 19,25,26 However, the individual molar mass dependences of all studied solutions of PS, PEO, and PMMA show the expected linear behavior with only one slope in Figures S1 -S3. The diffusion coefficients of these molar mass dependences were fitted to eq 10 in order to determine the Mark -Houwink parameters. The calculated Mark -Houwink parameters are listed in Table 1. The K 1 and a 1 data were taken from polystyrene in THF as the reference from literature data. 27 Table 1 presents the fitted Mark -Houwink parameters, the parameters of the molar mass dependences of the diffusion coefficients as well as the dynamic viscosities. It should be noted that the calculated Mark -Houwink parameters in Table 1 deliver good agreement with experimental data found in the literature. Table S3 in the SI shows comparisons for the available data. Figure 2 also illustrates the high accuracy of the calculated diffusion data a Determined via equation 10. b Determined via equation 6. c η for CD2Cl2 was not available thus η for CH2Cl2 was used from ref 30

Table 1. Mark -Houwink Parameters K and a , Flory Parameters b , and Constants c of the Molar Mass Dependences Determined via DOSY for PS, PEO, and PMMA as Well as Dynamic Viscosities

| polymer   | solvent      |   K a [mL · g - 1 ] |     a a |      b b |   c · 10 - 8 b [m 2 · s - 1 ] | η [mPa · s]   |
|-----------|--------------|---------------------|---------|----------|-------------------------------|---------------|
| PS        | THF-d8       |            0.014127 |   0.727 | 0.519361 |                       2.20882 | 0.48 21       |
| PS        | CDCl 3       |             0.00732 | 0.74596 | 0.534677 |                       2.34303 | 0.563 21      |
| PS        | C 6 D 6      |             0.01077 | 0.72682 |   0.5283 |                       1.91203 | 0.6067 21     |
| PS        | toluene- d 8 |              0.0098 | 0.73512 | 0.531065 |                       2.13758 | 0.56 21       |
| PS        | CD 2 Cl 2    |             0.01155 | 0.70628 | 0.521453 |                       2.74368 | 0.413 c       |
| PS        | acetone- d 6 |             0.07135 | 0.49819 | 0.452089 |                        2.0934 | 0.295 21      |
| PEO       | CD 3 OD      |             0.03563 | 0.65424 | 0.504105 |                       1.43345 | 0.543 21      |
| PEO       | D 2 O        |             0.02554 | 0.67839 | 0.512155 |                      0.792177 | 1.098 28      |
| PEO       | THF- d 8     |             0.02417 |  0.6831 | 0.513725 |                        1.8457 | 0.48          |
| PEO       | CD 3 CN      |             0.02456 | 0.68948 | 0.515853 |                       2.56919 | 0.343 21      |
| PEO       | acetone- d 6 |             0.06862 | 0.56535 | 0.474477 |                       2.12079 | 0.295         |
| PMMA      | THF- d 8     |             0.01061 | 0.69474 | 0.517608 |                       2.42854 | 0.48          |
| PMMA      | CDCl 3       |             0.00517 | 0.77158 | 0.543219 |                       2.63117 | 0.563         |
| PMMA      | C 6 D 6      |             0.00848 |  0.7331 | 0.530394 |                       2.07035 | 0.6067        |
| PMMA      | CD 2 Cl 2    |             0.00702 | 0.75226 |  0.53678 |                       3.23833 | 0.413         |
| PMMA      | DMSO         |             0.05265 | 0.47463 | 0.444236 |                      0.312052 | 2.19 29       |

Figure 2. Experimental diffusion coefficients vs calculated diffusion coefficients via eq 10 for PS, PEO, and PMMA in different solvents at T = 298.15 K.

<!-- image -->

achieved with eq 10 in comparison with the experimental data. It shows a perfect match of calculated and experimental diffusion coefficients for all samples with an average deviation of the experimental diffusion coefficients of just 2.4% from the average calculated line. The logarithmic scaling of Figure 2 cannot even resolve such differences. These small deviations are only visible if the linear axis is chosen (see Figure S4 of the SI).

Using the relevant parameters of Table 1, the universal calibration curve for structure- and solvent-independent molar mass determinations can be produced. In this case, the diffusion coefficients corrected by the dynamic viscosities will be plotted as the function of the molar masses corrected by the intrinsic viscosities. The intrinsic viscosities are calculated with the Mark -Houwink parameters of Table 1. Figure 3 shows now this universal calibration with eq 11 describing the dependence of the dynamic viscosity corrected diffusion coefficients vs intrinsic viscosity corrected molar masses:

<!-- formula-not-decoded -->

Figure 3. Dynamic viscosity corrected diffusion coefficients vs intrinsic viscosity corrected molar masses with Mark -Houwink parameters for PS, PEO, and PMMA in different solvents at T = 298.15 K.

<!-- image -->

It is evident from Figure 3 that all diffusion data can be described by one unique function. The accuracy of this calibration method significantly improves the data of Figures S5 -S8 where the diffusion coefficients are shown by including only the correction with the dynamic viscosity. The reason for the high precision in Figure 3 is the implementation of the intrinsic viscosity via the Mark -Houwink parameters. The intrinsic viscosity is strongly molar mass dependent and allows for the correction of the molar masses as well. Therefore, one unique calibration function could be obtained from Figure 3 describing all measured diffusion coefficients of the three polymers in 10 solvents. Figure 3 presents a linear correlation of the corrected diffusion coefficients with the corrected molar masses with an average deviation of only 2.5%.

The main benefit of this new universal calibration is the possibility of calculating the molar mass of a polymer from a single diffusion coefficient if the Mark -Houwink parameters and the dynamic viscosity are available at T = 298.15 K. In this case, the calibration function (11) can be resolved to the molar mass M w and is given by eq 12:

<!-- formula-not-decoded -->

This equation can be considered a universal molar mass determination for DOSY because it is solvent-independent and independent from the structure of the polymers. It should be noted that eq 12 should only be used at NMR systems with calibrated pulsed field gradients, convection compensated pulse sequences, T = 298.15 K and the same conditions as mentioned in the experimental part of the SI. Under these conditions it can be expected that the measured diffusion coefficients should also provide the same results at another NMR equipment. Figure 4 shows the molar masses M calc

Figure 4. Calculated molar masses via eq 12 with the parameters of Table 1 vs molar masses of the supplier for PS, PEO, and PMMA in different solvents at T = 298.15 K. The black line represents the molar masses M supplier .

<!-- image -->

calculated with eq 12 for all measured diffusion coefficients in comparison to the molar masses provided by the supplier (the black line in Figure 4 corresponds to the molar masses of the supplier). The average deviation is only 5%. This accuracy is impressive and might be a fantastic addition to SEC.

## ■ CONCLUSIONS

It was the main goal of this work to further improve the solvent-independent DOSY calibrations to a solventand structure-independent molar mass calibration, which is represented by only one function. The implementation of socalled Mark -Houwink parameters representing the intrinsic viscosity enables the derivation of such a universal equation. Therefore, it was possible to derive an equation to determine Mark -Houwink parameters via DOSY measurements, which could be further used to provide one universal function that correlates the diffusion coefficient to the molar mass for all investigated polymers and solvents together. This solvent- and structure-independent equation allows the determination of the molar masses of these polymers in the used solvents with an average error of only 5%. If further polymers with unknown Mark -Houwink parameters will be studied, eq 10 can be used for generating these Mark -Houwink parameters with DOSY if new molar mass dependences are measured. These molar mass dependences should be related to reference pairs of the parameters K and a from Table 1 (preferably for PS in THF). It is also worth mentioning again that the Mark -Houwink parameters determined by DOSY are comparable to those of the intrinsic viscosity measurements. In this respect, DOSY might be a complementary method to SEC for determining molar masses but also for determining Mark -Houwink parameters. It is necessary to note that the derived equations and fitted parameters of DOSY are related to the described experimental conditions of the NMR measurements in the Supporting Information such as calibrated gradient strength, convection compensated pulse sequence, experimental setup, and sample preparation. In this case, it would be welcome to extend the Mark -Houwink database via DOSY to other polymers and solvents, as well, in order to improve the DOSY measurements for molar mass determinations further.

## ■ ASSOCIATED CONTENT

## * sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.analchem.3c03797.

Additional experimental details, figures, and equations (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

Wolf Hiller -Faculty of Chemistry and Chemical Biology, TU Dortmund University, 44227 Dortmund, Germany; orcid.org/0000-0002-4219-4523; Phone: +49 231 7553777; Email: wolf.hiller@tu-dortmund.de; Fax: +49 231755 3771

## Author

Bastian Grabe -Faculty of Chemistry and Chemical Biology, TU Dortmund University, 44227 Dortmund, Germany; orcid.org/0000-0003-4694-1941

Complete contact information is available at: https://pubs.acs.org/10.1021/acs.analchem.3c03797

## Author Contributions

The manuscript was written through contributions of all authors./All authors have given approval to the final version of the manuscript.

## Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

We are grateful for funding the 600 MHz NMR spectrometer AVANCE NEO by the DFG (German Research Foundation: project number -452669688) and the Ministry of Culture and Science of North Rhine-Westphalia. We also thank our coworkers Jan Schonert and Benjamin Kissel for sample preparation. This article is dedicated to Professor Klaus Jurkschat on the occasion of his 70th birthday.

## ■ REFERENCES

- (1) Flory, P. J. Principles of Polymer Chemistry ; Cornell University Press: Ithaka, N. Y., 1953.
- (2) Grubisic, Z.; Rempp, P.; Benoit, H. J. Polym. Sci. B 1967 , 5 (9), 753 -759.
- (3) [Rudin, A.; Johnston, H. K. J. Polym. Sci. B 1971 , 9 (1), 55 -60.](https://doi.org/10.1002/pol.1971.110090109)
- (4) [Einstein, A. Ann. Phys. 1905 , 322 (8), 549 -560.](https://doi.org/10.1002/andp.19053220806)
- (5) [Rouse, P. E. J. Chem. Phys. 1953 , 21 (7), 1272 -1280.](https://doi.org/10.1063/1.1699180)
- (6) [Zimm, B. H. J. Chem. Phys. 1956 , 24 (2), 269 -278.](https://doi.org/10.1063/1.1742462)
- (7) Cherifi, N.; Khoukh, A.; Benaboura, A.; Billon, L. Polym. Chem. 2016 , 7 (33), 5249 -5257.

- (8) Augé, S.; Schmit, P.-O.; Crutchfield, C. A.; Islam, M. T.; Harris, D. J.; Durand, E.; Clemancey, M.; Quoineaud, A.-A.; Lancelin, J.-M.; Prigent, Y.; Taulelle, F.; Delsuc, M.-A. J. Phys. Chem. B 2009 , 113 (7), 1914 -1918.
- (9) Håkansson, B.; Nydén, M.; Söderman, O. Colloid Polym. Sci. 2000 , 278 (5), 399 -405.
- (10) Lewinski, P.; Sosnowski, S.; Kazmierski, S.; Penczek, S. Polym. Chem. 2015 , 6 (24), 4353 -4357.
- (11) Williamson, N. H.; Nydén, M.; Röding, M. J. Magn. Reson. 2016 , 267 , 54 -62.
- (12) [Groves, P. Polym. Chem. 2017 , 8 (44), 6700 -6708.](https://doi.org/10.1039/C7PY01577A)
- (13) Kuz'mina, N. E.; Moiseev, S. V.; Krylov, V. I.; Yashkir, V. A.; Merkulov, V. A. J. Anal. Chem. 2015 , 70 (7), 843 -849.
- (14) Kuz'mina, N. E.; Moiseev, S. V.; Krylov, V. I.; Yashkir, V. A.; Merkulov, V. A. J. Anal. Chem. 2014 , 69 (10), 953 -959.
- (15) Chamignon, C.; Duret, D.; Charreyre, M.-T.; Favier, A. Macromol. Chem. Phys. 2016 , 217 (20), 2286 -2293.
- (16) Li, W.; Chung, H.; Daeffler, C.; Johnson, J. A.; Grubbs, R. H. Macromolecules 2012 , 45 (24), 9595 -9603.
- (17) Vrijsen, J. H.; Thomlinson, I. A.; Levere, M. E.; Lyall, C. L.; Davidson, M. G.; Hintermair, U.; Junkers, T. Polym. Chem. 2020 , 11 (21), 3546 -3550.
- (18) Grabe, B.; Hiller, W. Macromolecules 2022 , 55 (18), 8014 -8020.
- (19) [Hiller, W. Macromol. Chem. Phys. 2019 , 220 (17), 1900255.](https://doi.org/10.1002/macp.201900255)

̃

- (20) Arrabal-Campos, F. M.; On a-Burgos, P.; Fernández, I. Polym. Chem. 2016 , 7 (26), 4326 -4329.
- (21) Voorter, P.; McKay, A.; Dai, J.; Paravagna, O.; Cameron, N. R.; Junkers, T. Angew. Chem., Int. Ed. 2022 , 61 (5), No. e202114536, DOI: 10.1002/anie.202114536.
- (22) Ruzicka, E.; Pellechia, P.; Benicewicz, B. C. Anal. Chem. 2023 , 95 (20), 7849 -7854.

̈

- (23) Jerschow, A.; Mu ller, N. J. Magn. Reson. 1997 , 125 (2), 372 -375.
- (24) Stejskal, E. O.; Tanner, J. E. J. Chem. Phys. 1965 , 42 (1), 288 -292.
- (25) Beckert, S.; Stallmach, F.; Bandari, R.; Buchmeiser, M. R. Macromolecules 2010 , 43 (22), 9441 -9446.
- (26) Zettl, U.; Hoffmann, S. T.; Koberling, F.; Krausch, G.; Enderlein, J.; Harnau, L.; Ballauff, M. Macromolecules 2009 , 42 (24), 9537 -9547.
- (27) Wagner, H. L. J. Phys. Chem. Ref. Data 1985 , 14 (4), 1101 -1106.
- (28) Harris, K. R.; Woolf, L. A. J. Chem. Eng. Data 2004 , 49 (4), 1064 -1069.
- (29) Evans, R.; Deng, Z.; Rogerson, A. K.; McLachlan, A. S.; Richards, J. J.; Nilsson, M.; Morris, G. A. Angew. Chem., Int. Ed. 2013 , 52 (11), 3199 -3202.
- (30) Kennedy, K. G.; Miles, D. T. J. Undergrad Chem. Res. 2004 , 4 , 145 -150.

<!-- image -->

CASBIOFINDERDISCOVERYPLATFORMTM

## STOPDIGGING THROUGHDATA -STARTMAKING DISCOVERIES

CASBioFinderhelps youfind the right biological insights in seconds

Start your search

<!-- image -->

American Chemical Society