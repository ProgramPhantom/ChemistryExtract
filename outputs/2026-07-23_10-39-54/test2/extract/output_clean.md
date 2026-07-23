<!-- image -->

## Improving the Interpretation of Small Molecule Di ff usion Coe ffi cients

Robert Evans, Guilherme Dal Poggetto, Mathias Nilsson, and Gareth A. Morris

† Aston Institute of Materials Research, School of Engineering and Applied Science, Aston University, Birmingham, B4 7ET, U.K. ‡ School of Chemistry, University of Manchester, Manchester M13 9PL, U.K.

<!-- image -->

M olecular self-di ff usion in a liquid originates from the random, thermal motion of the molecules present. Chemical information, such as the molecular mass of an unknown species, its aggregation, or its association with other species, can in principle be obtained from measurements of di ff usion coe ffi cients. However, in di ff usion-ordered NMR spectroscopy (DOSY), an analytical tool that disperses NMR signals according to di ff usion coe ffi cient, such data are normally only interpreted qualitatively. Quantitative interpretation of such spectra in terms of the sizes of species gives insight into molecular weights and association, including the formation of dimers, trimers, and higher oligomers. However, while there is a rough inverse correlation between molecular mass and the speed at which a species moves through solution, the wide range of possible molecular shapes, mobilities, and solute -solvent interactions, and some fundamental problems with theories of di ff usion, make quantitative interpretation di ffi cult.

One way forward is to use more or less empirical correlations to determine relationships between di ff usion coe ffi cient and molecular mass for chemically cognate systems, for example homologous series in a particular solvent. This has been very successful, particularly in organometallic chemistry where di ff usion NMR has een used to identify organolithiu reactive intermediates and alkali metal cyclopentadienides but is of little use when dealing with the analysis of a mixture of unknown species. The complementary approach that is examined here is to try to fi nd a less accurate but much more general relationship that can be used without prior knowledge of the chemistry involved. If the range of chemical space to be spanned is limited to small to medium-sized organic molecules (&lt; ca . 1 kDa), much of the uncertainty introduced by molec ar fl exibility and composition is avoided. It has been shown that, given these limitations, it becomes possible to derive a general correlation between molecular mass and di ff usion coe ffi cient that works over a wide range of chemistry and in multiple solvents. The method is restricted to dilute solutions (or pure solvents), because of the uncertainties introduced by obstruction e ff ects. Here we test that method, which was originally based on a set of 109 di ff erent combinations of 44 di ff erent solutes in 5 di ff erent deuteriated solvents, against a wide range of di ff usion measurements drawn from the chemical literature, extend it to provide di ff usionmolecular mass relationships for a range of temperatures, and provide software tools in Excel and Matlab for estimating di ff usion coe ffi cients from molecular masses and vice versa .

<!-- image -->

Any discussion of the relationship between di ff u on and molecular size starts with the Stokes -Einstein equation ( ). This equation assumes that the solute acts as a hard sphere with hydrodynamic radius, r H, moving randomly through a continuum solution in response to random bu ff eting from the species around it. The thermal driving force at a temperature T , k B T , is balanced by the frictional force 6 f πη r H that acts on a solute particle of e ff ective radius r H moving through a fl uid with viscosity η , giving the relationship

$$\inf _ { \mathbf h } \quad D = \frac { k _ { B } T } { 6 \pi f r _ { H } }$$

Received:

December 4, 2017

Accepted:

February 26, 2018

Published:

February 26, 2018

DOI:

<!-- image -->

Article where the shape correction factor f is equal to 1 for a spherical particle. While the Stokes -Einstein equation is simple and can give good estimates for the di ff usion coe ffi cients of large species, it is not a good guide to small molecule di ff usion. There are systematic failures in the model as real molecules are not hard spheres, and no solution is a continuum. As a result, attempts to predict di ff usion coe ffi cients using the Stokes -Einstein equation, with hydrodynamic radii estimated from densities, tend to severely underestimate he di ff usion coe ffi cients of molecules smaller than ca . 1 kDa.

There are clear systematic trends in the ways in which the Stokes -Einstein equation fails in dilute solution. Four main reasons for its failure can be identi fi ed: the continuum approximation fails, as real solvents are made of discrete molecules that are not negligibly small compared to solutes; molecules are not spherical, and can adopt a wide range of possible geometries; molecules are not static, and have widely di ff ering ranges of conformational freedom; and molecules can interact and bind with the solvent itself. A further obstacle to establishing a relationship between di ff usion coe ffi cient and molecular mass is that species containing heavy atoms will on balance be denser, and hence show smaller hydrodynamic radii, than those containing only light atoms. Any attempt to generate an accurate universal law would need to take all of these complications into account and is likely to be doomed to failure: molecules are simply too varied.

However, analytical theories do exist that can successfully account for some of th sources of failure. First of all, molecules are not spheres. Perrin analyzed the e ff ects of molecular shape, considering molecules as ellipsoids, and analytical equations do exist for the e ff ect of increasing aspect ratios in ellipsoidal shapes. For molecules that are not long thin rods or wide thin disks, the e ff ects are typically much less than 10% and can often be safely ignored.

More signi fi cantly, a liquid is not a continuum fl uid. It consists of small molecules moving randomly, tumbling as they collide with other molecules in the liquid. The e ff ect of nonnegligible solvent particle size is to change the friction term acting on the solute molecules. This can be represented as a change in he correction factor f and was modeled by Gierer and Wirtz as

$$f _ { G W } = \left ( \frac { 3 \alpha } { 2 } + \frac { 1 } { 1 + \alpha } \right ) ^ { - 1 } & & \text {relative} \\$$

where α is the ratio of th radius of the solute to that of the solvent. Chen and Chen adapted this, using an empirical expression ( ) fi tted to experimental data.

$$f _ { _ { C h e n } } = ( 1 + 0 . 6 9 5 \alpha ^ { 2 . 2 3 4 } ) ^ { - 1 } & & ( 2 . b ) & & a \ d e c { a }$$

This approach is e ff ectively a hybrid between the Gierer and Wirtz model ( ) and power-law fi tting, using two parameters. Using a test set of crown ethers in methanol, a nearly homologous series of structurally very similar molecules, it gave good results. The choice of crown ethers, which are highly fl exible and hence are expected to show in fl ated hydrodynamic radii, was perhaps an unfortunate one, and their attempts to extend the study to crown ethers and alkanes in ethanol and butan-1-ol found the model lacking.

The general approach of using empirically obtained power laws has found wide se in the st y of macromolecules, in particular of polymers and peptides. The di ff usion coe ffi cient or, often, the relative di ff usivity (the measured di ff usion coe ffi cient normalized by an internal reference) can be expressed in terms of the mass of the species, M , raised to some empirical power, α , as in .

$$\begin{matrix} ^ { L } _ { e } & & & D \, \infty \, M ^ { - \alpha } \end{matrix}$$

This use of a power law is reminiscent of the Flory equation where the radius of gyration of a polymer, R g , is related to its mass through a parameter, δ , known as the Flory exponent or the inverse of the fractal dimension, d F , of the molecular chain.

This gives two potential general methods for the estimation of small molecule di ff usion coe ffi cients. One is speci fi c, producing power-law relationships for homologous se similar This is well-established or polymers, , -proteins, , , and large macrocycles, although a twoparameter fi t is required for each structurally distinct polymer type in each di ff erent solvent. While there have been attempts to link the exponent in to the fractal dimension contained within the Flory equation, these have not always proved successful. For spherical species, the fractal dimension is 3 and α = 1/3. In one of the fi rst atte ts to relate di ff usion coe ffi cients to molecular size, Polson found that this cube root relationship held for some large species but was much less useful for smaller molecules.

With the use of internal and external references, methods based on power-law relationships have also found application small molecules, for example in the work of Williard and Li on the characterization of organolithium compounds. Di ff usion measurements of unknown organolithium compounds were acquired in the presence of a number of internal references. An internal calibration curve based on di ff usion measurements of reference compounds within the sample is then produced for each experiment. The method was subseq extended to include 2 H, 6 Li, and 31 P DOSY experiments. -The internal references used in these studies were chosen for a number of properties including inertness and high solubility, and their chemical shifts were typically far from those of the lithiumcontaining species studied. These compounds spanned a range of di ff erent chemical functionalities including, but not limited to, aromatic compounds, ole fi ns, and TMS. It is not always possible to fi nd suitable internal reference materials, so a similar approach used an external calibr n curve to rationalize relative di ff usion coe ffi cients D / D ref . The e ff ect of shape was considered, with di ff erent calibration curves used for three distinct classes of shapes: spheres, ' dissipated spheres ' , and ellipsoids and discs. This method has now been extended to a range of common N R solvents (DMSOd 6 , C6D12, C6D6, CDCl3, and CD2Cl2). Shape-speci fi c calibration curves have been shown to be very accurate for chemically cognate species; a degree of generality can be introduced, at the expense of accuracy, with the use of ' merged ' calibration curves.

The approach investigated here is both more general and necessarily more approximate. Starting again with the Stokes -Einstein equation, the largest source of error that can be treated analytically is the breakdown in the continuum model. Here, the Gierer-Wirtz equation for the correction factor f ( ) is used. This leaves the e ff ects of shape, fl exibility, solvation, and composition, none of which can be treated analytically without prior chemical knowledge. A model is therefore sought that approximates species as hard spheres, with an average e ff ective density ρ eff that is a variable parameter, that obey the GiererWirtz modi fi cation of the Stokes -Einstein law. Restricting the scope of the approach to small to medium-sized (up to ca . 1 kDa) organic molecules with no heavy atoms limits the impact

DOI:

of composition (excluding atoms heavier than chlorine, putting an upper limit on the e ff ective density) and of fl exibility (excluding fl exible high polymers, which can dopt extended conformations with in fl ated hydrodynamic radii ). The residual e ff ects of fl exibility, and the e ff ects of shape and of solvation, all tend to increase hydrodynamic radius and hence to decrease e ff ective density; di ff erent compositions can increase or decrease the density but only to a limited extent. The GiererWirtz equation requires knowledge of the ratio of the solute and the solvent radius, but since the solute radius is being estimated using the hard sphere approximation with an e ff ective density, it is reasonable to apply the same logic to estimating the solvent radius. (Of course the same limitations then apply to the solvent as to the solute -systematic bias will result if the solvent is, for example, a fl exible high polymer.) This then yields the expression in , which links the di ff usion coe ffi cient for a given temperature and solvent viscosity to the solute and solvent molecular masses MW and MWS, through a single adjustable parameter, the e ff ective density ρ eff .

$$\text {single adjustable parameter} , \, \text {the effective density} \, \rho _ { \text {eff.} } \\ D = \frac { k _ { B } T \left ( \frac { 3 \alpha } { 2 } + \frac { 1 } { 1 + \alpha } \right ) } { 6 \pi \eta _ { \sqrt { 3 } } \sqrt { \frac { 3 M W } { 4 \pi \rho _ { \Delta } N } } } \\ \alpha = \frac { r _ { S } } { r } = \sqrt { \frac { M W _ { S } } { M W } } \\ \text {The problem of deriving a usable relationship between} \quad \text {tendend} \\$$

The problem of deriving a usable relationship between molecular mass and di ff usion coe ffi cient then reduces to that of fi nding an optimum value for the e ff ective density ρ eff . Using a set of experimental di ff usion coe ffi cients, D , all measured at 25 ° C, for 109 combinations of 44 solutes an 5 common solvents, gave an e ff ective density of 619 kg m -3 . As expected, this is much smaller than the typical densities of solid or liquid organic materials, because of the e ff ects (in roughly decreasing order of importance) of solvation, fl exibility, and shape. The root-meansquare di ff erence between estimated and experimental di ff usion coe ffi cients for the set of measurements was 14.6%. The model has s s uently found widespread use, in a range of di ff erent areas. -

Here this Stokes -Einstein Gierer-Wirtz Estimation (SEGWE) method is tested against a range of measurements on dilute systems drawn from the literature that span a much wider chemical space than the original data set (formally, the training set), increasing the range of compound masses up to ca . 1.5 kDa, removing the temperature restriction of 25 ° C, and widening the range of solvents covered. The motivation for deriving was to facilitate the quantitative interpretation of results o ed with di ff usion-ordered NMR spectroscopy (DOSY), , but di ff usion coe ffi cients can of course be determined u a variety of techniques, xample tracer measurements , and chronoamperometry. , The di ff usion data studied here are not limited to those measured by NMR in deuteriated solvents but include a range of protiated liquids, widening the range of applicability of SEGWE. The estimation method has been implemented as an Excel spreadsheet and as a Matlab package, as detailed in ; both are available for free download from and

also at doi:10.17632/cxt99xf2d2.2.

## ■ METHOD

Di ff usion Coe ffi cients. In order to test SEGWE against a wider range of samples, containing di ff erent solvents and solutes, a comprehensive review of the literature for a wide range of di ff usion coe ffi cients from a wide range of sources was undertaken. In addition to the original data set in the paper detai further 23 papers have been used, , , -, , , , -to create a literature data set containing a further 558 measurements of di ff usion coe ffi cients of various species in various solvents, spanning a range of molecular weights from 18 to 1273 g mol -1 in 23 di ff erent solvents, both deuteriated and protiated. The single bigg source of additional data is that of Crutch fi eld and Harris, with 200 di ff usion coe ffi cients in two s o di ff erent temperatures. A further fi ve papers , , , , contained variable temperature data, contributing 86 measurements between them. The rest of the data were acquired at 25 ° C. While most of the di ff usion data were acquired using NMR techniques, data were acquired where tracer di ff usio thods were used as a c brating standard in two references, , while a third reference used an electrochemical method.

Not all possible sources of di ff usion data were used in this study. A set of fi ve criteria was used to determine whether literature di ff usion coe ffi cients were to be used in this study.

Scope. Solutes with molecular weights greater than 1.5 kDa were not used. Likewise, long fl exible polymeric species, which tend to adopt extended conformations with in fl ated hydrodynamic radii, were excluded from the literature data set.

Systematic Miscalibration. There are a number of possible so ces of systematic errors in di ff usion NMR experiments. If the relevant paper contained evidence of lack of, or mis-, calibration, the data were excluded from the literature data set. In particular, sets of experimentally acquired di ff usion coe ffi cients with systematically large deviations from prediction in every measurement were excluded.

Inconsistent Di ff usion Coe ffi cients. Related to criterion 2, if a repeated measurement of the same species had inconsistent di ff usion coe ffi cients reported within a single experimental report, it is highly likely that there were signi fi cant problems with the experiments. The data were excluded from the literature data set.

Evidence of Convection. The presence of convection in a sample i ikely to lead to higher di ff usion coe ffi cients than expected. Variable temperature studies, or those in solvents particularly prone to convection, that showed systematically higher di ff usion coe ffi cients than predicted were excluded from the literature data set.

Evidence of Aggregation. Species that form aggregates di ff use more slowly than single molecules. Systems that might be expected to aggregate and that had lower di ff usion coe ffi cients than predicted were therefore excluded from the literature data set.

It is instructive to look at two di ff usion me surements that failed these tests. In the original data set, trimesic acid (benzene-1,3,5-tricarboxylic acid) in DMSOd 6 exhibited a di ff usion coe ffi cient ca . 60% smaller than predicted. Trimesic acid is known to for xtended self-assembled structures both the solid state and at liquid -solid interfaces, producing extended hexagonal networks with either ' chicken wire ' or ' fl ower ' structures. This di ff usion coe ffi cient was, therefore, removed from the original data set.

Experimental di ff usion coe ffi cients much higher than predicted indicate the likely presence of convection. Reference contains a variable temper re study of water, 2ethoxyethanol, and ca ff eine in D2O. At 304.4 K, the measured

di ff usion coe ffi cients for water and ca ff eine were respectively 22

DOI:

and 23% higher than predicted. This increased to over 30% for all three species at 309.8 K. This indicates the probable onset of convection, and hence the di ff usion coe ffi cient measurements in this reference made at higher temperatures were all removed from the literature data set.

The references used in this study (as well as the solvents used for the samples, the nature of the experiments (variable temperature, non-NMR), and whether any measurements of di ff usion within a given reference were excluded) are summarized in . The di ff usion and solvent viscosity data collected from the literature and organized here, although not covering all possible reported data on di ff usion coe ffi cients, may aid future investigations on the prediction of molecular weight from di ff usion coe ffi cients.

Temperature Dependence of Di ff usion Coe ffi cients. The original investigation used only data acquired at 25 ° C. There are two ways in which temperature a ff ects di ff usion coe ffi cients. First, in the numerator of the Stokes -Einstein equation, the thermal energy driving di ff usion is given by k B T . The higher the temperature, the more energy the solute and solvent molecules have and the faster they move through the solution. Second, and much more importantly, in the denominator, the solvent viscosity η depends strongly on temperature. Over the range of temperatures likely to be encountered in NMR di ff usion measurements, this temperature dependence is well represented by an Arrhenius-like equation ( ), with two variable parameters a and b .

$$\eta = a e ^ { \frac { b } { T } } & & ( 5 ) & & \stackrel { 6 2 7 } { \log }$$

In the original study, the viscosities used for the deuteriated solvents were estimated from those of protiated solvents (by multiplying the value for the protio-solvent by the ratio of the deuterio- and protio-molecular masses), at a single temperature (298 K). Here, literature data are used for the viscosities of all solvents, whether protiated or deuteriated. Reported values at di ff erent temperatures are fi tted to obtain Arrhenius parameters a and b , from which viscosities at di ff erent temperatures are calculated. Of all the solvents used, only one had no reported measurements of its viscosity at temperatures away from 298 K. Frustratingly this was the solvent for which the largest number of di ff usion measurements are available, CDCl3. In order to estimate the temperature dependence of the viscosity of CDCl 3 , the value of b for CHCl3 was used, with the value of a determined by the esti ated viscosity of CDCl 3 at 298 K, taken from previous work (5.44 × 10 -4 kg m -1 s -1 ). The experimental viscosity data available for toluened 8 are also limited, with only a few low-temperature measurements in the literature. Literature data for all the solvent viscosities di ff er slightly from the estimates used previously; however, using the new, temperature-dependent values for viscosity has little e ff ect on the root-mean-square deviation for the original data set. A comparison of the viscosities at 298 K used in the original study with those calculated using the literature data and included in references used for both deuteriated and protiated , -solvents are detailed in . summarizes relevant information for each of the solvents used. Protiated solvents which had a deuteriated analogue used in the study are also included. also contains all data used to calculate a and b for each solvent used in this work.

## ■ RESULTS

Testing SEGWE against the Literature. shows the results of plotting experimental versus predicted di ff usion

Figure 1. Measured di ff usion coe ffi cient plotted against di ff usion coe ffi cient calculated using for 108 samples of 44 small molecules in fi ve deuteriated solvents (original data set, fi lled red squares) and 558 samples in 23 solvents, both deuteriated and protiated (literature data set, fi lled blue diamonds), with a solid line of unit slope.

<!-- image -->

coe ffi cients for the set of 558 literature measurements of di ff usion coe ffi cients used, as blue diamonds, alongside the same comparison for 108 of the original measurements, plotted as red squares. (As noted above, the original data set had the outlier point, trimesic acid in DMSOd 6 , removed, and the e ff ective density has been reoptimized, to give a new value of 627 kg m -3 .)

With the approximations made, the model cannot hope to predict the di ff usion coe ffi cients of all the compounds used in this study, but it performs well over 600 individual experimentally acquired di ff usion coe ffi cients.

Gratifyingly, there is no immediately apparent di ff erence between the original data set and the larger literature data set: the latter provides a strong validation of the method. The quality of fi t can be represented and quanti fi ed in a number of ways. Plots of di ff erence in di ff usion coe ffi cient, as a percentage of the calculated di ff usion coe ffi cient, against both solute molecular weight ( .upper) and measured solute di ff usion coe ffi cient ( .lower) give an immediate graphical indication.

For this large set of experimentally measured di ff usion coe ffi cients, the vast majority lie within 25% of the value predicted. shows that there is a slight trend present within the literature data set, with the experimentally measured di ff usion coe ffi cients being on average slightly higher than expected, particularly for lighter molecules and/or higher di ff usion coe ffi cients. The di ff usion coe ffi cient measurements lying above and below the dashed lines are listed in .

The RMS error for SEGWE applied to the larger, literature data set can be calculated and compared with that obtained for the original data set, as shown in . When all of the valid data presented here are included, the RMS error is 14.8%, comparable with that originally reported for the original set of data.

It is instructive to compare histograms, shown in , of the original and literature data that summarize the information contained in and . They show substantial overlap but with a clear tendency for the literature experimental di ff usion coe ffi cients to be slightly (between 10 and 20%) underestimated by . While the original data set

DOI:

Figure 2. Di ff erence between calculated and measured di ff usion coe ffi cients, expressed as a percentage of calculated di ff usion coe ffi cient, plotted against (upper) molecular mass and (lower) experimental di ff usion coe ffi cient for both the original data set ( fi lled red squares) and the literature data set ( fi lled blue diamonds). Dashed lines indicate errors of ± 25%.

<!-- image -->

Table 1. Comparison of RMS Error for Original, Literature, and Combined Data Sets

| data set   |   no. of di ff usion coe ffi cients |   RMS error (%) |
|------------|-------------------------------------|-----------------|
| original   |                                 108 |            14.0 |
| literature |                                 558 |            14.9 |
| combined   |                                 666 |            14.8 |

was acquired with strict temperature control and samples acquired in thick-walled tubes, such precautions were not always taken in the literature measurements. Convection is conventionally seen as an example of a critical phenomenon. NMR tubes are long, narrow tubes made out of thin glass. If a large enough negative temperature gradient forms between the two ends of the tube, then Rayleigh-Bernard convection will spontaneously form, with the warmer fl uid fl owing upward, displacing the colder fl uid above. However, recent studies of convective fl ow in NMR experiments have revealed that some convective fl ow is almost always present in typical di ff usion NMR experiments. The noncritical phenomena of Hadley convection occurs when transverse temperature gradients form around the tube. In a temperature-regulated NMR probe, the air fl ow around the sample is disrupted, and transverse temperature gradients form, making convective fl ow of the sample higher than expected di ff usion coe ffi cients, almost certain. ,

Certain subsets of the data can be studied to obtain further insight into the performance of the estimation method over a range of di ff erent experimental parameters. Of the eight deuteriated solvents used across the literature data, seven have su ffi cient di ff usion coe ffi cients reported to make plotting the individual fi ts worthwhile. plot the experimental di ff usion coe ffi cients acquired in eight common deuteriated solvents against di ff usion coe ffi cients estimated using . It is noteworthy that the solvent for which few viscosity measurements are available in the literature, toluened 8 , shows the most obvious systematic deviation between experimental and estimated di ff usion coe ffi cients. Other solvents show less marked trends, but overall it is perhaps surprising how well the single compromise approach of represents di ff usion measurements in a wide range of very di ff erent solvents. The RMS errors for the four subsets of di ff usion data corresponding to common deuteriated NMR solvents are collected in .

Table 2. Comparison of RMS Error for Subsets of the Combined Data Set Corresponding to the Com n NMR Solvents CDCl3, D2O, DMSOd 6, and Toluened 8

| solvent      |   no. of di ff usion coe ffi cients |   RMS error (%) |
|--------------|-------------------------------------|-----------------|
| CDCl 3       |                                 213 |            12.4 |
| D 2 O        |                                 107 |            11.1 |
| DMSO- d 6    |                                  60 |            17.8 |
| toluene- d 8 |                                  54 |            16.2 |

Extending SEGWE to Di ff erent Temperatures. In order to estimate di ff usion coe ffi cients at di ff erent temperatures, the Arrhenius model of for solvent viscosity has been used with . As explained earlier, two parameters were used to fi t viscosities as an exponential function of temperature for all the solvents used in this study. An assessment of the e ff ectiveness of this extension was made using the data contained in ref , a compilation of 200 di ff usion coe ffi cients measured in two di ff erent solvents at two di ff erent temperatures. compares measured di ff usion coe ffi cients with those estimated

with for both solvents and both temperatures.

Figure 3. Measured di ff usion coe ffi cient plotted against di ff usion coe ffi cient calculated using for 24 small molecules in D2O at 298 K ( fi lled yellow squares), 24 small molecules in D 2 O at 303 K ( fi lled red squares), 76 small molecules in CDCl3 at 298 K ( fi lled blue diamonds), and 76 small molecules in CDCl3 at 303 K ( fi lled purple diamonds). Data are drawn from ref .

<!-- image -->

As with the data in , the quality of the fi t can be represented and quanti fi ed in a number of ways. depicts analogous plots to those in , plotting Δ D (as a percentage of experimental di ff usion coe ffi cient) against both solute di ff usion coe ffi cient ( ) and solute molecular weight ( ) to give an immediate graphical indication of the quality of the fi t and also show how little the scatter in

DOI:

results changes with increasing temperature. While almost all of the experimental data are correctly predicted to within 25%, there is a slight upward trend in the average deviation between estimation and experiment as di ff usion coe ffi cient increases, just as in .

## ■ DISCUSSION

The small but clear systematic trends in and re fl ect the di ffi culty of using a single model, with only one adjustable parameter, for all solvents. One source of such a trend is clear from : in CDCl3, toluened 8 , benzened 6 , and cyclohexaned 12 , there is a small tendency to overestimate D in small species. This is far from surprising: the same factors that lead to a ca . 15% RMS uncertainty in the di ff usion coe ffi cients of individual analytes, and by implication in the estimation of their hydrodynamic radii r , apply to the estimates of the hydrodynamic radii of the solvents. It might be expected that the overall fi t of the data could be improved signi fi cantly by making the hydrodynamic radii of the di ff erent solvents into adjustable parameters. Such an approach can be found applied to the original data set in . While the quality of the fi t is improved, the improvement is only from 14.0% to 12.9%. This method sacri fi ces the simplicity and universality of the SEGWE approach and the improvement in reliability from increasing the number of adjustable parameters from one to six is small, because the approach does not address the other fundamental sources of uncertainty set out in the introduction. It would require a much larger evidence base to give robust results.

A further reason for caution in seeking to improve the prediction accuracy of this, and of other methods for correlating molecular masses with di ff usion coe ffi cients, is, as noted earlier, that experimental measurements of the latter a bject to a source of systematic error, sample convection. , This has historically been underestimated. There are a number of ways in which the e ff ects of convection can be reduced or compensated for. The thermal conductivity sapphire is approximately 25 times that of borosilicate glass, so the use of sapphire NMR tubes will greatly reduce the temperature gradients that drive convection. Narrower bore NMR tubes reduce the convective fl ow that does occur. Convectioncompensated di ff usion NMR pulse sequences are esigned to cancel the e ff ects of laminar fl ow in the sample. However, many of the measurements in the literature data set did not use convection compensation. Since the e ff ect of convection is to increase the apparent di ff usion coe ffi cient, there will be a small but unquanti fi able bias in the great majority of the measurements used here (and, by extension, in many of the measurements that is likely to be called upon to assist in interpreting). As noted earlier, comparing the original and literature results in the histograms of , there is a small but clear shift between the two centroids that may be attributable to the slight bias introduced by convection. It is noteworthy, for example, that many of the measurements exhibiting higher di ff usion coe ffi cients than predicted in

are those made in chloroform. This is not unexpected; the relative ease with which a solvent convects is a function of the parameter χ = βηκ , where β is the volumetric thermal expansion coe ffi cient in K -1 , η is the dynamic vi sity in Pa s, and κ is the thermal conductivity in W m -1 K -1 . For the two solvents compared in ref , χ is nearly 12.5 times larger for CDCl 3 than for D2O.

Instead of using the literature data to validate the result of ref , it is tempting to take advantage of the much larger evidence base available from the literature to reoptimize the parameter ρ eff in . If done, this results in an increase in ρ eff from 627 to 744 kg m -3 , but the RMS error decreases only slightly, from 14.8 to 12.9%. Any marginal bene fi t is outweighed by the extra uncertainty that is introduced by the fact that there is a known but unquanti fi able bias in the literature data set caused by sample convection. The accompanying software therefore uses a default value 627 kg m -3 for ρ eff , which is straightforward for the user to change if wished.

## ■ CONCLUSIONS

NMR measurements of di ff usion coe ffi cient, such as in di ff usion-ordered spectroscopy (DOSY) experiments, are typically used in a qualitative manner only, separating out signals in a manner akin to chromatography. By making pragmatic decisions about the assumptions underlying the Stokes -Einstein equation, a general method for the prediction of small molecule di ff usion coe ffi cients can be constructed for extracting approximate information on molecular mass from such data. For a known molecular mass, a di ff usion coe ffi cient can be estimated (or vice versa , albeit with much greater uncertainty). This, in turn, allows for deductions about whether molecules are associating, or oligomeric species are present, delivering chemical insight from measurements that are often left uninterpreted. The method has been tested against a large body of literature data on di ff usion coe ffi cients, showing a high level of consistency, has been extended to cover both a wide range of NMR solvents and a wider range of temperatures, and has been implemented in freely available soft e, including the very recent General NMR Analysis Toolbox.

## ■ ASSOCIATED CONTENT

## * S Supporting Information

The Supporting Information is available free of charge on the at DOI:

.

Summaries of all references, solvents used, and viscosity measurements, as well as fi gures illustrating subsets of data, as described in text ( )

## ■ AUTHOR INFORMATION

## Corresponding Author

* Phone +44 121 204 5382. E-mail:

ORCID

Robert Evans:

## Notes

The authors declare no competing fi nancial interest.

Additional supporting research data consisting of Excel spreadsheets containing all di ff usion coe ffi cients used in this work and Mathematica notebooks to reproduce every calculation and every image in both the manuscript and Supporting Information, all solvent data used, as well as Matlab GUI and Excel sheets for the prediction of di ff usion coe ffi cient from MW and vice versa for this article may be accessed at both and doi:10.17632/

cxt99xf2d2.2.

DOI:

.

## ■ ACKNOWLEDGMENTS

The authors are most grateful to Drs. C. A. Crutch fi eld and D. J. Harris for giving access to the di ff usion data for ref . This work was supported by the Engineering and Physical Sciences Research Council (grant numbers EP/H024336/1 and EP/ E05899X/1) and by a studentship to GDP from Science Without Borders -Brazil (CNPq reference number 233163/ 2014-0).

## ■ REFERENCES

- (1) Li, D.; Keresztes, I.; Hopson, R.; Williard, P. G. Acc. Chem. Res. 2009 , 42 , 270 -280.
- (2) Bachmann, S.; Gernert, B.; Stalke, D. Chem. Commun. 2016 , 52 , 12861 -12864.
- (3) Evans, R.; Deng, Z.; Rogerson, A. K.; McLachlan, A. S.; Richards, J. J.; Nilsson, M.; Morris, G. A. Angew. Chem., Int. Ed. 2013 , 52 , 3199 -3202.
- (5) Perrin, F. J. Phys. Radium 1936 , 7 , 1 -11.
- (4) Einstein, A. Ann. Phys. (Berlin, Ger.) 1905 , 322 , 549 -560.
- (6) Gierer, A.; Wirtz, K. Z. Naturforsch. 1953 , 8 , 522 -532.
- (7) Chen, H. C.; Chen, S. H. J. Phys. Chem. 1984 , 88 , 5118 -5121.
- (8) Flory, P. J. Principles of Polymer Chemistry ; 1st ed.; Cornell University Press: Ithaca, NY, 1953.
- (9) Chen, A.; Wu, D. H.; Johnson, C. S. J. Am. Chem. Soc. 1995 , 117 , 7965 -7970.
- (10) Wilkins, D. K.; Grimshaw, S. B.; Receveur, V.; Dobson, C. M.; Jones, J. A.; Smith, L. Biochemistry 1999 , 38 , 16424 -16431.
- (11) Auge ́ , S.; Schmit, P.-O.; Crutchfield, C. A.; Islam, M. T.; Harris, D. J.; Durand, E.; Clemancey, M.; Quoineaud, A.-A.; Lancelin, J.-M.; Prigent, Y.; Taulelle, F.; Delsuc, M.-A. J. Phys. Chem. B 2009 , 113 , 1914 -1918.
- (12) Assemat, O.; Coutouly, M.-A.; Hajjar, R.; Delsuc, M.-A. C. R. Chim. 2010 , 13 , 412 -415.
- (14) Arrabal-Campos, F. M.; On ̃ a-Burgos, P.; Ferna ́ ndez, I. Polym. Chem. 2016 , 7 , 4326 -4329.
- (13) Vie ́ ville, J.; Tanty, M.; Delsuc, M. A. J. Magn. Reson. 2011 , 212 , 169 -173.
- (15) Jones, J. A.; Wilkins, D. K.; Smith, L. J.; Dobson, C. M. J. Biomol. NMR 1997 , 10 , 199 -203.
- (16) Bogdan, A. R.; Davies, N. L.; James, K. Org. Biomol. Chem. 2011 , 9 , 7727 -7733.
- (17) Polson, A. J. Phys. Colloid Chem. 1950 , 54 , 649 -652.
- (18) Li, D.; Kagan, G.; Hopson, R.; Williard, P. G. J. Am. Chem. Soc. 2009 , 131 , 5627 -5634.
- (19) Kagan, G.; Li, W.; Hopson, R.; Williard, P. G. Org. Lett. 2009 , 11 , 4818 -4821.
- (20) Kagan, G.; Li, W.; Hopson, R.; Williard, P. G. Org. Lett. 2010 , 12 , 520 -523.
- (21) Guang, J.; Hopson, R.; Williard, P. G. J. Org. Chem. 2015 , 80 , 9102 -9107.
- (22) Neufeld, R.; Stalke, D. Chem. Sci. 2015 , 6 , 3354 -3364.
- (23) Bachmann, S.; Neufeld, R.; Dzemski, M.; Stalke, D. Chem. - Eur. J. 2016 , 22 , 8462 -8465.
- (24) Abet, V.; Evans, R.; Guibbal, F.; Caldarelli, S.; Rodriguez, R. Angew. Chem., Int. Ed. 2014 , 53 , 4862 -4866.
- (25) Poveda, A.; Alonso, I.; Ferna ́ ndez-Iba ́ n ̃ ez, M. A ́ . Chem. Sci. 2014 , 5 , 3873 -3882.
- (26) Giuffrida, M. L.; Rizzarelli, E.; Tomaselli, G. A.; Satriano, C.; Trusso Sfrazzetto, G. Chem. Commun. 2014 , 50 , 9835 -9838.
- (27) Kennedy, S. R.; Miquelot, A.; Aguilar, J. A.; Steed, J. W. Chem. Commun. 2016 , 52 , 11846 -11849.
- (28) Maugeri, L.; Asencio-Herna ́ ndez, J.; Le ́ bl, T.; Cordes, D. B.; Slawin, A. M. Z.; Delsuc, M. A.; Philp, D. Chem. Sci. 2016 , 7 , 6422 -6428.
- (29) Claridge, T. D. W. High-resolution NMR techniques in Organic Chemistry ; 3rd ed.; Elsevier: Amsterdam, 2016.
- (30) Rideau, E.; You, H.; Sidera, M.; Claridge, T. D.; Fletcher, S. P. J. Am. Chem. Soc. 2017 , 139 , 5614 -5624.
- (31) Johnson, C. S. Prog. Nucl. Magn. Reson. Spectrosc. 1999 , 34 , 203 -256.
- (32) Morris, G. A. Di ff usion-Ordered Spectroscopy. In Encyclopedia of Nuclear Magnetic Resonance ; Grant, D. M., Harris, R. K., Ed.; John Wiley &amp; Sons Ltd.: Chichester, 2002; pp 34 -44.
- (33) Mills, R. J. Phys. Chem. 1973 , 77 , 685 -688.
- (34) Evans, D. F.; Tominaga, T.; Davis, H. T. J. Chem. Phys. 1981 , 74 , 1298 -1305.
- (35) Denuault, G.; Mirkin, M. V.; Bard, A. J. J. Electroanal. Chem. Interfacial Electrochem. 1991 , 308 , 27 -38.
- (36) Baur, J. E.; Wightman, R. M. J. Electroanal. Chem. Interfacial Electrochem. 1991 , 305 , 73 -81.
- (37) Crutchfield, C. A.; Harris, D. J. J. Magn. Reson. 2007 , 185 , 179 -182.
- (38) Lucas, L. H.; Otto, W. H.; Larive, C. K. J. Magn. Reson. 2002 , 156 , 138 -145.
- (39) Barjat, H.; Morris, G. A.; Swanson, A. G. J. Magn. Reson. 1998 , 131 , 131 -138.
- (40) Nilsson, M.; Gil, A. M.; Delgadillo, I.; Morris, G. A. Anal. Chem. 2004 , 76 , 5418 -5422.
- (41) Cohen, Y.; Avram, L.; Frish, L. Angew. Chem., Int. Ed. 2005 , 44 , 520 -554.
- (42) Colbourne, A. A.; Meier, S.; Morris, G. A.; Nilsson, M. Chem. Commun. 2013 , 49 , 10510 -10512.
- (43) Nilsson, M.; Gil, A. M.; Delgadillo, I.; Morris, G. A. Chem. Commun. 2005 , 1737 -1739.
- (44) Antalek, B. Concepts Magn. Reson. 2002 , 14 , 225 -258.
- (45) Harmon, J.; Coffman, C.; Villarrial, S.; Chabolla, S.; Heisel, K.
- (46) Lin, M.; Shapiro, M. J. J. Org. Chem. 1996 , 61 , 7617 -7619.
47. A.; Krishnan, V. V. J. Chem. Educ. 2012 , 89 , 780 -783.
- (47) Holz, M.; Heil, S. R.; Sacco, A. Phys. Chem. Chem. Phys. 2000 , 2 , 4740 -4742.
- (48) Schulze, B. M.; Watkins, D. L.; Zhang, J.; Ghiviriga, I.; Castellano, R. K. Org. Biomol. Chem. 2014 , 12 , 7932 -7936.
- (49) Holz, M.; Weinga ̈ rtner, H. J. Magn. Reson. 1991 , 92 , 115 -125.

(50) Hoffman, R. E.; Shabtai, E.; Rabinovitz, M.; Iyer, V. S.; Mullen,

- K.; Rai, A. K.; Bayrd, E.; Scott, L. T. J. Chem. Soc., Perkin Trans. 2 1998 , 1659 -1664.
- (51) Valencia, D. P.; Gonza ́ lez, F. J. J. Electroanal. Chem. 2012 , 681 , 121 -126.
- (52) Swan, I.; Reid, M.; Howe, P. W.; Connell, M. A.; Nilsson, M.; Moore, M. A.; Morris, G. A. J. Magn. Reson. 2015 , 252 , 120 -129.
- (53) Kolotuchin, S. V.; Thiessen, P. A.; Fenlon, E. E.; Wilson, S. R.; Loweth, C. J.; Zimmerman, S. C. Chem. - Eur. J. 1999 , 5 , 2537 -2547.
- (54) Lackinger, M.; Griessl, S.; Heckl, W. A.; Hietschold, M.; Flynn, G. W. Langmuir 2005 , 21 , 4984 -4988.
- (55) Holz, M.; Mao, X. a.; Seiferling, D.; Sacco, A. J. Chem. Phys. 1996 , 104 , 669 -679.
- (57) Weinga ̈ rtner, H.; Holz, M.; Sacco, A.; Trotta, M. J. Chem. Phys. 1989 , 91 , 2568 -2574.
- (56) Dixon, J. A.; Schiessler, R. W. J. Phys. Chem. 1954 , 58 , 430 -432.
- (58) Artaki, I.; Jonas, J. J. Chem. Phys. 1985 , 82 , 3360 -3370.
- (59) Harris, K. R.; Woolf, L. A. J. Chem. Eng. Data 2004 , 49 , 1064 -1069.
- (60) Hardy, R. C.; Cottington, R. L. J. Res. Natl. Bureau Standards 1949 , 42 , 573 -578.
- (61) Exarchos, N. C.; Tasioula-Margari, M.; Demetropoulos, I. N. J. Chem. Eng. Data 1995 , 40 , 567 -571.
- (62) Sovilj, M. N. J. Chem. Eng. Data 1995 , 40 , 1058 -1061.
- (63) Mekhtiev, S. I.; Mamedov, A. A.; Khalilov, S. K.; Aleskerov, M.
- A. Izv. Vyssh. Uchebn. Zaved. Neft Gaz 1975 , 3 , 64 100.
- -
- (64) Zakurenov, V. M.; Konyakhin, V. P.; Nozdrev, V. F. Zh. Fiz. Khim. 1975 , 49 , 548 -549.
- (65) Knapstad, B.; Skjølsvik, P. A.; Øye, H. A. J. Chem. Eng. Data 1989 , 34 , 37 -43.
- (66) Assael, M. J.; Dalaouti, N. K. High Temp. - High Pressures 2000 , 32 , 179 -184.
- (67) Harris, K. R.; Newitt, P. J.; Woolf, L. A. J. Chem. Eng. Data 2004 , 49 , 138 -142.

DOI:

- (68) Marchetti, A.; Preti, C.; Tagliazucchi, M.; Tassi, L.; Tosi, G. J. Chem. Eng. Data 1991 , 36 , 360 -365.
- (69) Bernal-García, J. M.; Guzma ́ n-Lo ́ pez, A.; Cabrales-Torres, A.; Estrada-Baltazar, A.; Iglesias-Silva, G. A. J. Chem. Eng. Data 2008 , 53 , 1024 -1027.
- (70) Akhtar, S.; Omar Faruk, A. N. M.; Saleh, M. A. Phys. Chem. Liq. 2001 , 39 , 383 -399.
- (72) Geddes, J. A. J. Am. Chem. Soc. 1933 , 55 , 4832 -4837.
- (71) Carmen Grande, M. d.; Julia ́ , J. A.; García, M.; Marschoff, C. M. J. Chem. Thermodyn. 2007 , 39 , 1049 -1056.
- (73) Caudwell, D. R.; Trusler, J. P. M.; Vesovic, V.; Wakeham, W. A. Int. J. Thermophys. 2004 , 25 , 1339 -1352.
- (74) Khattab, I. S.; Bandarkar, F.; Fakhree, M. A. A.; Jouyban, A. Korean J. Chem. Eng. 2012 , 29 , 812 -817.
- (75) Rathnam, M. V.; Bhanushali, K. R.; Sayed, R. T.; Kumar, M. S. S. Eur. Chem. Bull. 2013 , 2 , 434 -444.
- (77) Domanska, U.; Laskowska, M. J. Solution Chem. 2009 , 38 , 779 -799.
- (76) Mikhail, S. Z.; Kimel, W. R. J. Chem. Eng. Data 1961 , 6 , 533 -537.
- (78) Mutalik, V.; Manjeshwar, L. S.; Sairam, M.; Aminabhavi, T. M. J. Chem. Thermodyn. 2006 , 38 , 1062 -1071.
- (79) Dymond, J.; Øye, H. J. Phys. Chem. Ref. Data 1994 , 23 , 41 -53. (80) Carvajal, C.; To ̈ lle, K. J.; Smid, J.; Szwarc, M. J. Am. Chem. Soc. 1965 , 87 , 5548 -5553.
- (81) Metz, D. J.; Glines, A. J. Phys. Chem. 1967 , 71 , 1158.
- (82) Byers, C. H.; Williams, D. F. J. Chem. Eng. Data 1987 , 32 , 344 -348.
- (83) Santos, F. J. V.; Nieto de Castro, C. A.; Dymond, J. H.; Dalaouti, N. K.; Assael, M. J.; Nagashima, A. J. Phys. Chem. Ref. Data 2006 , 35 , 1 -8.
- (84) Barbosa, T. M.; Rittner, R.; Tormena, C. F.; Morris, G. A.; Nilsson, M. RSC Adv. 2016 , 6 , 95173 -95176.
- (85) Haynes, W. M. CRC Handbook of Chemistry and Physics ; CRC Press: Boca Raton, FL, 2014.
- (87) Castan ̃ ar, L.; Dal Poggetto, G.; Colbourne, A. A.; Morris, G. A.; Nilsson, M. Magn. Reson. Chem. 2018 , .
- (86) Jerschow, A.; Muller, N. J. Magn. Reson. 1998 , 132 , 13 -18.

DOI: