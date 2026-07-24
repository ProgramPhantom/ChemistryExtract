<!-- image -->

Article

Real-Time Determination of Molecular Weight: Use of MaDDOSY (Mass Determination Diffusion Ordered Spectroscopy) to Monitor the Progress of Polymerization Reactions

<!-- image -->

ABSTRACT: Knowledge of molecular weight is an integral factor in polymer synthesis, and while many synthetic strategies have been developed to help control this, determination of the final molecular weight is often only measured at the end of the reaction. Herein, we provide a technique for the online determination of polymer molecular weight using a universal, solvent-independent diffusion ordered spectroscopy (DOSY) calibration and evidence its use in a variety of polymerization reactions.

<!-- image -->

KEYWORDS: diffusion ordered spectroscopy, NMR, polymerization, reaction monitoring, mass determination, online monitoring

## ■ INTRODUCTION

The molecular weight and dispersity of a polymer largely determine the physical properties of a material. As such, measurement of molecular weight information both of the final product and how it evolves during the reaction is important. However, in most cases, the techniques required for this type of characterization require offline analysis. The modern standard benchmark technique for this in a synthetic laboratory is gel permeation chromatography (GPC) or, in some cases, mass spectrometry. These techniques provide useful information on both molecular weight and dispersity; however, they generally require sample preparation or workup from the reaction mixture before analysis, rendering these techniques particularly challenging for reaction monitoring in real time and any subsequent automative reaction optimization.

This notwithstanding, there have been notable successes in this area; the exemplary review by Haven and Junkers gives an excellent overview of these achievements. The first analyses of polymerizations acquired through mass spectrometry were performed by Santos et al. in 2008 in which the Brookhart polymerization of alkenes was monitored using electrospray ionization (ESI) mass spectrometry. In that work, the authors coupled the reaction vessel directly to the ESI source, in conjunction with inline dilution with acetonitrile before the mass spectrometer. This required no workup, with rapid analysis times of just a few seconds for each measurement.

However, this approach is limited to ionizable polymers and those that produce only low-molecular weight species and is also complicated by multiple charges on any individual polymer, making a complex system even more complex. These are inherent problems pertinent to real-time reaction monitoring. As most high-molecular-weight polymers present difficulties for analysis by ESI due to the combination of multiple charge states, mass discrimination along with the distribution of chemical specials produces a very large number of peaks, leading to complex analysis.

Matrix-assisted laser desorption ionization (MALDI) can be used, which typically has only singly charged species, but this often requires laborious sample preparation, and automation is not trivial. Several matrices are often required to be screened to ensure acceptable ablation and ionization from the MALDI plate, but several orders of magnitude of dilution, combination with a salt or other ionizing agent, and precise spotting on a plate are required to collect data of a desirable quality. MALDI also favours lower mass molecules as both ionization and detection are mass sensitive favouring lower masses. Due to

Received:

March 14, 2024

Revised:

April 27, 2024

Accepted:

April 29, 2024

Published:

May 9, 2024

<!-- image -->

this discrimination against higher masses, the weight average molecular weight is always underestimated which leads to dispersity being significantly underestimated. There have, however, been several reported instances where MALDI has been used to characterize polymerization reactions: Wu et al. used MALDI to study the mechanism of the ring-opening polymerization (ROP) of tetrahydrofuran (THF) using bis(pentafluorophenyl)(phenoxy)borane, and Scherger et al. used the technique to study self-immolative RAFT-polymer end-group modification. However, in both of these cases, sample preparation was performed manually, with analysis being subsequently performed. Automated MALDI analysis has shown some promise since its inception by Meier et al., where a home-built MALDI spotter was integrated with a highperformance liquid chromatography (HPLC) system and applied to study polymer end groups. Its use has become more widespread, evidenced by Pirrone et al., who used it for the rapid screening of poly(ethylene glycol) conjugated cytokines. Indeed, there are now commercially available MALDI spotters capable of integration with existing systems to reduce preparation and analysis time.

Clearly, there still exists a need for online polymer molecular weight analysis in real time. GPC provides many benefits. First, sample preparation is simple, often only requiring dissolution to an appropriate concentration and then filtering. GPC can be readily used for polymers in excess, from very low M wt to &gt;1,000,000 g mol -1 , and is applicable in a wide range of solvents, allowing for analysis of a significantly wide range of polymers. There are, however, some innate drawbacks of GPC; first is that even the best GPC systems are generally accepted to possess an error of up to 10%, largely arising from the use of standards that do not typically match the chemical characteristics of the analyzed polymers. Results from GPC are solvent-dependent, as the hydrodynamic volume, the parameter measured in GPC, can be affected by how well the solvent solvates the polymer. Thus, problems can arise, for example, some polymers, such as PET and nylon, are only soluble in very particular solvents, such as fluorinated acids, or require elevated temperatures, complicating analysis. Other polymers, particularly those that are water-soluble, can cause problems due to interacting with the column, meaning that retention is a result of not only size but also chemical interactions, vastly changing the retention time and therefore the calculated molecular weight. Further complication arises due to GPC being a chromatographic method, and hence, each individual evaluation can take between 5 and 45 min, severely limiting the available time resolution in online analysis and the quality of the result if the analysis time is pushed down.

This notwithstanding, there have been several instances of success of applying GPC for online reaction monitoring. As early as 2004, work was being focused on the online monitoring of controlled radical polymerizations by GPC detector methods, and this is well-exemplified in the work by Mignard et al., in which the authors used light scattering (LS), viscometry, differential refractive index (DRI), and UV detectors to characterize gradient copolymerization reactions. In this work, excellent temporal resolution was achieved, and the groundwork for truly online characterization of polymerization reactions has been described. In this instance, molecular weight was calculated using concentration and light-scattering data, requiring a significant amount of information to be known about the system of interest prior to reaction monitoring being carried out, somewhat limiting universal ap bility to new systems of interest. In 2010, Levere et al. , combined RI and LS detectors using a rapid GPC column to allow for the monitoring of single-electron transfer living radical polymerization (SET-LRP) in close to real time, with a temporal resolution of approximately 4 min. Due to the use of rapid GPC columns, only poor chromatographic resolution was obtained, and in order to obtain higher resolution, more conventional GPC columns are required, often with run times &gt;30 min, which limits the reactions to be monitored to those &gt;3 h in order for meaningful data to be obtained. More t developments by both the Junkers and Warren groups , using online GPC techniques have produced exciting results. In both of these cases, the relative ease of data analysis from online GPC has been used to build self-optimization algorithms for the high-throughput testing of polymerization conditions, thereby reducing the need for multiple, time-consuming batch reactions. This work shows that there is clearly scope and interest for automated online analyses of molecular weight for a multitude of reasons. Indeed, in both of the cases referenced, GPC was used in conjunction with other analysis techniques, notably NMR, to measure conversion.

This use of NMR in automated, online polymer synthesis is increasing due to the availability of benchtop NMR systems, which give increasingly good resolution, allowing NMR to be a much more accessible technique in the synthetic laboratory. NMR has been used to monitor the progress of many polymerizations, usually by performing reactions in a standard NMR tub n within the magnet of a high-field cryogenic instrument , or sampling from a reaction at given time points and subsequently performing the analysis offline. Full online reaction monitoring within a typical laboratory scale in real time has been prohibitive. The reasons for this are plentiful, including the usual requirement for deuterated solvents, the need for specialized flow cells, the need for liquid cryogens for magnet cooling, and the lack of laboratory infrastructure in close proximity to NMR spectrometers. Benchtop NMR systems address the majority of these problems and have been us r 1D NMR experiments for a range of polymerizations. , First, as most employ an external lock to prevent magnetic field drift, deuterated solvents are not required. This provides a significant benefit for reaction monitoring, as experiments can be performed at a standard laboratory scale in conventional solvents, which are often far less expensive than their deuterated counterparts. Benchtop NMR systems require no cryogenic cooling, which vastly reduces the physical space required for the magnet, thus allowing them to be transported around a laboratory on trolleys, making them inherently portable. This much smaller size also means that flow cells can be much smaller and generally composed of standard glass (or plastic) tubing with conventional HPLC flow fittings. These factors combined mean that the NMR spectrometer can be brought into the synthetic laboratory, rather than the other way around. Thus, reactions can be performed under a multitude of conditions, including under an inert atmosphere, at variable temperature, and at scale. The reaction mixture can then be pumped directly through the NMR spectrometer and returned without significant deviation from the required conditions.

A further recent development in benchtop NMR spectroscopy is the advances and application of gradient-based solvent suppression. A particularly useful experiment in polymer science is the diffusion ordered spectroscopy (DOSY)

experiment. The DOSY experiment is becoming increasingly used in polymer science. It shows particular use in the assessment of the success of copolymerization reactions and as a tool to demonstrate an increase in size at the conclusion of a reaction.

The measured diffusion constant can be correlated with the molecular weight of the macr lecule, and indeed, this has been shown in previous works , and further developed into a universal calibration within our groups.

There do exist some limitations of this approach, detailed in our previous work. Briefly, the solvent must act as a 'good' solvent for the system of interest, meaning that it should readily solubilize the polymer. Additionally, the concentration must be carefully controlled, based on the expected final molecular weight of the polymer, to a concentration known as C * ; for polymers in the molecular weight range of 10 -1 -1 ,

100,000 g mol

, this is approximately 20

-

50 mg mL

.

While this does not provide an excessive number of problems for reaction monitoring, a slightly more dilute system than typically used for batch polymerizations is required. Additionally, knowledge of the approximate molecular weight of the final polymer is required, meaning that reasonably wellunderstood chemistries are needed. A further limitation is the requirement to know the bulk viscosity of the solvent of interest. For most common laboratory solvents, this value is known at ambient temperature and can be easily found in literature tables; however, values at elevated temperatures are more of a challenge to find. As such, for some reactions, this value must be recorded experimentally first, either through traditional techniques such as Ostwald viscometry or via the use of an inline viscometer.

Once the viscosity and concentrations are controlled, however, the approach can, in principle, be used to monitor reactions in real time. Indeed, the use of DOSY to monitor reactions of small molecules in flow has been reported by Marchand et al. and its use for polymerizations has been reported by Vrijsen et al. In both cases, high-field NMR instruments were used, and in the instance of the polymerization reaction, no universal calibration was used to determine molecular weight, limiting application to a wider range of polymers and polymerizations.

The use of DOSY with a benchtop NMR system, and our previously reported universal calibration, therefore presents an interesting opportunity as a possible tool for the determination of molecular weight in real time for the monitoring of a wide range of polymerizations of different monomers under different reaction conditions.

## ■ EXPERIMENTAL SECTION

## Materials and Instrumentation

Methyl acrylate, 1,4-dioxane, azobis(isobutyronitrile) (AIBN), ascorbic acid, tert -butyl hydroperoxide, ethyly-2-bromoisobutyrate (EBiB), CuBr2, cyclohexane, tetrahydrofuran, and isoprene were purchased from Merck. The RAFT agent, 2-(((butylthio)carbonothioyl)thio)propanoic acid (PABTC), and tris[2(dimethylamino)ethyl]amine ( en) were synthesized according to previously reported literature. ,

All NMR spectra were acquired on a Magritek Spinsolve 80 Carbon Benchtop NMR spectrometer equipped with a z -axis gradient coil capable of generating a maximum field gradient of 500 mT/m. 1D 1 H NMR spectra were interpreted using Magritek Spinsolve versions 2.1.3 or 2.3.6. DOSY spectra were interpreted using Magritek Spinsolve version 2.3.6 or the GNAT, version 1.3.2, developed by the Manchester NMR Methodology Group. GNAT was used for the anionic and RAFT experiments. Spinsolve was used for the Cu-RDRP experiment.

GPC samples were recorded using an Agilent Infinity II MDS instrument equipped with differential refractive index (DRI), viscometry (VS), dual angle light scatter (LS), and multiple wavelength UV detectors. The system was equipped with 2 × PLgel Mixed C columns (300 × 7.5 mm 2 ) and a PLgel 5 μ m guard column. The eluent was either CHCl3, in the case of polyisoprene, or THF with 0.01% BHT additive, in the case of poly(methyl acrylate). Samples were run at 1 mL/min at 30 ° C. Poly(methyl methacrylate) and polystyrene standards (Agilent EasiVials) were used for calibration. Ethanol was added as a flow rate marker. Analyte samples were filtered through a nylon membrane with 0.22 μ m pore size before injection. Experimental molar mass ( M n , M w, SEC) and dispersity ( Đ ) values of synthesized polymers were determined by conventional calibration using Agilent GPC/SEC software.

## Polymerizations

In the cases of anionic and RAFT polymerizations, the setup used was as shown in . Briefly, this comprises a reaction vessel, from

Figure 1. Polymerization reaction setup 1.

<!-- image -->

which the reaction mixture is pumped out into a glass flow cell/tube within the NMR spectrometer for measurement, after which it is pumped to a fraction collector, which either collects the sample or pumps the solution to waste. 1D 1 H spectra, DOSY spectra, and fractions were collected every 90 min. All instrumental control was performed through an automated script, which is available in the . In each case, the 1D 1 H spectra acquisition

parameters were as follows: number of scans = 4, acquisition time = 6.4 s, repetition time = 15 s, and pulse angle = 90 ° . The DOSY parameters, used in the PGSTE pulse sequence, were optimized for the approximate target molecular weight of each system. This involved the following: number of scans = 4 or 8 (selected to provide a good signal from the polymer peak), number of gradient steps = 8, acquisition time = 6.4 s, repetition time = 15 s, and maximum gradient, big delta, and little delta were optimized to provide good attenuation of the polymer peaks through the gradient steps.

In the case of the Cu-RDRP reaction, the setup outlined in was used. This comprises a similar setup as in , with the omission of the fraction collector and subsequent recirculation of the analyzed mixture back into the reaction vessel.

Figure 2. Polymerization reaction setup 2.

<!-- image -->

Molecular weights were calculated using the calibration detailed in our previous work, using the freely available associated online webtool. For reference, the MaDDOSY calibration equation is shown in

.

$$M _ { w } = 1 0 ^ { ( ( \log D + \log \eta ) + 7 . 7 4 ) / - 0 . 5 9 7 } & & ( 1 ) & & \vartheta ( G )$$

## Redox-Initiated RAFT Polymerization of Methyl Acrylate

Methyl acrylate (28.5 g, 0.33 mol) and RAFT agent (1.58 g, 6.6 mmol) were dissolved in 1,4-dioxane (270 mL) to give an approximately 10 wt % solution. The resultant solution was deoxygenated, brought under nitrogen, and left to equilibrate for 20 min at ambient temperature. The flask was then prepared for reaction monitoring according to , and the solution was pumped through the system for priming. The automated script was started, and after the first system shim was performed, tert -butyl hydroperoxide (148.7 mg, 1.65 mmol) and ascorbic acid (145.3 g, 0.825 mmol) were added. The reaction was allowed to proceed for 720 min at ambient temperature, with spectra and fractions collected as previously described. After the reaction, the resultant fractions were reduced to a yellow viscous oil via gentle warming with a heat gun and subsequently dissolved in THF (1 mL) for GPC analysis. Conversion ( 1 H NMR) 70%, M w (GPC) 2800 g mol -1 , M wt (MaDDOSY) 3600 g mol -1 , Đ (GPC) = 1.11

## Thermally Initiated RAFT Polymerization of Methyl Acrylate

Methyl acrylate (28.5 g, 0.33 mol) and RAFT agent (789 mg, 3.3 mmol) were dissolved in 1,4-dioxane (270 mL) to give an approximately 10 wt % solution. The resultant solution was deoxygenated, brought under nitrogen, and heated to 70 ° C in an oil bath. The flask was then set up for reaction monitoring according to , and the solution was pumped through to prime the system. The automated script was started, and after the first system shim was performed, AIBN (54.2 mg, 0.33 mmol) was added. The reaction was allowed to proceed for 810 min at 70 ° C, with spectra and fractions collected as previously described. After the reaction, the resultant fractions were then reduced to a yellow viscous oil prior to dissolution in THF (1 mL) for GPC analysis. Conversion ( 1 H NMR) 90%, M w (SEC) 7500 g mol -1 , M wt (MaDDOSY) 7400 g mol -1 , Đ (GPC) = 1.36

## Anionic Polymerization of Isoprene

Isoprene (20.43 g, 0.30 mol) was dissolved in cyclohexane (270 mL) to give an approximately 10 wt % solution, both of which had been dried over molecular sieves (3 Å), in a flask under nitrogen to give moisture contents of 8.3 ppm for cyclohexane and 10.7 ppm for isoprene as measured by Karl Fischer titration. The flask was placed in a reflux setup under nitrogen and left to equilibrate for 20 min at ambient temperature. Reaction monitoring was as above. Each collection vessel in the fraction collector had an aliquot of methanol (0.5 mL) in order to quench the reaction following fraction collection. The automated script was started, and after the first system shim was performed, n -butyl lithium solution in hexanes (2.1 mL, 1.4 M) was injected through a rubber septum. The reaction was allowed to proceed for 870 min at ambient temperature, with spectra and fractions collected as previously described. After the reaction, the resultant fractions were then reduced to a colorless, viscous oil with heating and subsequently dissolved in chloroform (1 mL) for GPC analysis. Conversion (NMR) 90%, M w (GPC) 15,400 g mol -1 , M wt (MaDDOSY) 15,200 g mol -1 , Đ (GPC) = 1.43

## Photoinitiated Cu-RDRP Polymerization of Methyl Acrylate

Methyl acrylate (20 mL, 0.222 mol), EBiB (326 μ L, 2.22 mmol), CuBr2 (9.9 mg, 44.4 μ mol), Me6TREN (71 μ L, 0.226 mmol), and DMSO (180 mL), to give an approximately 10 wt % solution, were added to a round-bottom flask that was sealed with a septum and deoxygenated with nitrogen for 15 min. The flask was then set up for reaction monitoring according to and prepared as above. The automated script was started, and after the first system shim was performed, polymerization was started once the reaction mixture was placed inside a custom-made UV box with λ max ∼ 360 nm. The reaction was allowed to proceed for 630 min at room temperature, with spectra collected as previously described. Conversion ( 1 H NMR) 93%, M w (GPC) 10,400 g mol -1 , M wt (MaDDOSY) 13,800 g mol -1 , Đ (GPC) = 1.18

## ■ RESULTS AND DISCUSSION

## Reaction Monitoring Setup

In order to accurately measure the diffusion constant in a DOSY experiment, a time period, Δ , is required. This is commonly referred to as 'big delta' and is a period of time in which diffusion is allowed to freely occur, after which the initial applied gradient is reversed prior to the measurement. The gradient itself can be applied in any Cartesian axis; however, this is often dictated by the hardware in each individual spectrometer. In the case of the spectrometer used in this work (Magritek), the gradient must be applied in the z -axis, which, unfortunately, is the direction in which the flow cell of the magnet resides. The result of this is that for the time period Δ t , the flow must be stopped to allow natural diffusion to take place and to allow the diffusion constant to be accurately measured. This results in a stop-flow setup, whereby for the duration of the DOSY measurement, the flow through the flow cell is stopped and then subsequently restarted once the measurement is complete. For the reactions in this work, this presents no issues; however, for implementation in a full-flow chemistry setup, it is noted that a switching valve would be needed to divert the flow during the stopped measurement phase, which has been shown as a possibility on a high-field spectrometer.

## Viscosity Measurements

For the MaDDOSY calibration to be as accurate as possible, the viscosity of the system must be known. In the cases of dioxane in the redox-initiated RAFT polymerization, the cyclohexane in the anionic polymerization, and the DMSO in t u-RDRP polymerization, literature values were used. -For the dioxane in the thermally initiated RAFT polymerization, temperature literature data were not available due to the increased temperature and the viscosity was therefore determined experimentally using Ostwald's viscometry and was found to be 0.607 mPa · s.

## Redox-Initiated RAFT Polymerization of Methyl Acrylate

To first assess the feasibility of using the MaDDOSY system to monitor a polymerization reaction in real time, the first polymerization mechanism chosen was redox RAFT. This was chosen as the reaction could be carried out at ambient temperature while allowing for the potential of good control of dispersity and, being an RDRP process, should show linear evolution of molecular weight with respect to monomer conversion.

The molecular weight and monomer conversion with respect to reaction time are shown in , with molecular weights calculated online via MaDDOSY, and, for comparison, the molecular weights from conventional GPC analysis are also plotted.

There is excellent agreement between the values obtained from GPC and from the MaDDOSY real-time monitoring. The uncertainties given in the MaDDOSY results are 95% confidence intervals, calculated as described previously.

Figure 3. M wt vs time for redox-initiated RAFT polymerization of methyl acrylate.

<!-- image -->

While these uncertainties seem large, they can be greatly reduced with the use of more scans in the NMR experiment; however, this of course comes at the cost of sampling frequency. It should also be noted that GPC results are often very close to the measured value from the MaDDOSY experiment, and as such, the 95% confidence intervals are very conservative in their approximation. The GPC results were obtained using narrow polystyrene and poly(methyl methacrylate) standards using conventional GPC analysis making use of a differential refractive index detector. There is less good agreement between the two techniques at the lower molecular weights seen early in the reaction likely due to two two factors. First, the MaDDOSY calibration is not as robust at molecular weights &lt;1000 g mol -1 . This is due to lower-molecular-weight polymers having less of a tendency to form ideal coils in solution due to their short chain length. Consequentially, the assumptions used in the MaDDOSY  that in a theta-like solvent the polymer forms idealistic chains and therefore the hydrodynamic radius is predictable  do not apply, and therefore, the predicted molecular weight is inaccurate. Second, the above arguments are also true for GPC, where lower molecular weight standards are often not available. However, once the molecular weights are &gt;1000 g mol -1 and within the MaDDOSY calibration range, the agreement between the two techniques seems to be excellent.

For this reaction, we would expect a linear growth of molecular weight with conversion. This is consistent with living (anionic) and RDRP processes, and this is indeed what was observed in .

In these plots, M w is plotted as the result from the GPC experiment; this is to allow comparison with the DOSY M wt , which most closely approximates M w. In the conversion plots, theoretical M wt therefore assumes monodispersity. While a generally linear increase in M wt with respect to monomer conversion is seen throughout the reaction, the reaction stops at approximately 70% conversion. This is a documented drawback of redox RAFT, which we do not fully understand, and it is noted that this does present challenges in terms of assessing the applicability of the reaction monitoring setup used; therefore, additional reaction mechanisms are required.

Figure 4. M wt vs conversion for redox-initiated RAFT polymerization of methyl acrylate.

<!-- image -->

## Thermally Initiated RAFT Polymerization of Methyl Acrylate

Probably the most common method of conducting a RAFT reaction is through thermal radical initiation, such as with azo initiators such as AIBN. As it is important to deliver radicals at a sufficient rate for the reaction to proceed, e.g., radical initiators with a 10 h half-life of between 50 and 120 ° C, these elevated temperatures can cause problems for reaction monitoring. Diffusion is highly temperature-dependent, , as is viscosity. This results in the higher temperatures used in the MaDDOSY calibration no longer holding true, and as such, the calibration should be used with caution. The effects of this can be somewhat mitigated due to the viscosity correction, provided the viscosity at the given temperature is known and convection correction is accounted for. For the reaction studied here, conducted at 70 ° C, the viscosity of dioxane was determined experimentally. This viscosity of course may not be the true viscosity for the DOSY measurement, as some degree of cooling will have occurred in the tubing; however, it remains a good approximation. Further work is aiming to create a temperature-corrected calibration, and its use would be more appropriate in the future. The M wt increased linearly as a function of time, , and once again, we see an agreement between the values calculated through MaDDOSY and those obtained by conventional, offline, GPC analysis, in all cases with the GPC values being within the uncertainty of the MaDDOSY values.

Figure 5. M wt vs time for thermally initiated RAFT polymerization of methyl acrylate.

<!-- image -->

This agreement between the values obtained suggests that the viscosity correction provides a good approximation to account for the increased diffusion resulting from the higher temperature; thus, provided the viscosity at the experimental temperature is known, the system still performs appropriately. The M wt also increased linearly with respect to monomer conversion; see .

Figure 6. M wt vs conversion for thermally initiated RAFT polymerization of methyl acrylate.

<!-- image -->

Thus, the experimentally derived molecular weight and the expected molecular weight have excellent agreement in this case, and unlike in the redox-initiated RAFT reaction, the reaction reaches a higher conversion of 90%, with the data remaining in agreement throughout the reaction. These two RAFT examples highlight the application of the technique to monitor reactions; however, the application should also be assessed against further mechanisms and monomers.

## Anionic Polymerization of Isoprene

The monitoring of anionic polymerizations in a laboratory presents different challenges to RAFT polymerization due to increased sensitivity to air and moisture. The benefit of the reaction setups described in and is that they can be rendered airtight easily; therefore, molecular weight data can, in principle, be obtained without loss of any reaction mixture in the process. In this example, we used isoprene as the monomer, and during the initiation, an exotherm was observed, increasing the temperature and thus also the viscosity; this was taken into account when calculating the MaDDOSY molecular weights. Molecular weight increased as a function of time ( ), reaching a larger final molecular weight than in other examples and good agreement between the GPC and MaDDOSY, thus demonstrating the applicability for polymers &gt;10,000 g mol -1 . One point of note is that the 95% confidence intervals are much larger at higher molecular weights; this is due to only 4 scans being performed at each gradient step. With more scans, these confidence intervals would become smaller, but in any case, the absolute values are very close to the GPC values, which themselves have a likely error of 10 -20%.

Figure 7. M wt vs time for the anionic polymerization of isoprene.

<!-- image -->

As a living process, this polymerization should also display linearity in the number-average molecular weight vs conversion, and indeed, this is so in the case ( ).

Figure 8. M wt vs conversion for the anionic polymerization of isoprene.

<!-- image -->

Additionally, the high conversion of 90% suggests that the inert atmosphere of the reaction was not compromised as a result of the reaction monitoring setup, and the reaction proceeded as expected. The final dispersity was higher than would be hoped for anionic polymerization; however, this could be further optimized in subsequent experiments. It should be noted that in , the values do not fall as expected. This is likely due to the relatively low molecular weights approaching the limits of the DOSY and GPC calibration.

Throughout these examples, it has been shown that the MaDDOSY reaction monitoring setup has excellent agreement with the result obtained by offline GPC. This gives us confidence about the versatility and robustness of the technique, provided care is taken when choosing the reaction conditions, as previously described. The most limiting of these comprises the comparatively lower concentrations, at or &lt;10 wt %, required when compared to traditional bulk polymerizations.

## Photoinitiated Cu-RDRP Polymerization of Methyl Acrylate

Photoactivated polymerizations are of interest as they typically require considerably less energy than many other processes and can be easily controlled. To monitor a Cu-RDRP reaction, the reaction monitoring setup shown in was used, as the validity of the technique had already been demonstrated, showing good agreement between MaDDOSY and GPC.

shows the increase in molecular weight as a function of time; over the course of the reaction, the change in molecular weight is clear and follows predictable growth.

Figure 9. M wt vs time for photoinitiated Cu-RDRP polymerization of methyl acrylate.

<!-- image -->

An additional change made with this setup was the reduction in the number of times the spectrometer was shimmed. In previous examples, shimming was performed after every DOSY measurement, whereas with this experiment, no shimming was performed, in order to examine the limits of equipment. This benchtop spectrometer has an external lock, meaning no deuterated solvents are required for locking or shimming of the magnet; however, this results in the magnetic field becoming inhomogeneous much faster than a high-field magnet. This leads to a deviation in the molecular weight from the expected molecular weight due to peak broadening, and therefore molecular weight calculation, at higher conversion ( ). This notwithstanding, the expected molecular weight in all cases is within the predicted 95% confidence interval, which further demonstrates the robustness of MaDDOSY as a reaction monitoring technique. In addition, the peak broadening only occurred after approximately 5 h, suggesting that shimming is needed infrequently, potentially increasing the number of data points that can be acquired for a reaction.

## ■ CONCLUSIONS

Building on our existing work of using mass determination diffusion ordered spectroscopy (MaDDOSY) as a tool for the calculation of polymer molecular weight, we have demonstrated its application as a useful and robust tool for reaction monitoring in real time. By using a standard flow cell and peristaltic pump, we have shown that a variety of different polymerization reactions can be monitored to provide close-toreal-time molecular weight information as the reaction proceeds.

Figure 10. M wt vs conversion for photoinitiated Cu-RDRP polymerization of methyl acrylate.

<!-- image -->

RAFT polymerizations using two different methods of initiation at both room temperature and elevated temperature show that when accounting for the viscosity changes present as a result of temperature change, MaDDOSY can provide molecular weights similar to those obtained by conventional offline techniques; additionally, data can be collected much more frequently due to the faster analysis time with reporting in real time when performing a DOSY experiment compared to GPC analysis.

The application of the technique has also been demonstrated in a living anionic polymerization; this has shown that the analysis technique does not compromise the inert reaction conditions required for these polymerizations, making it an attractive option for analysis of complex systems.

A closed analysis system has also been demonstrated through the monitoring of a photoinitiated Cu-RDRP polymerization reaction, in which the reaction mixture is sampled, analyzed, and returned to the reaction mixture. In this setup, no reaction mixture is lost in the analysis, and the final product is unaffected by the analysis. This makes the technique an attractive option for analyzing small-scale reactions using potentially expensive reagents.

The limitations of the technique are discussed, which are primarily in relation to optimizing the reaction solvent and concentration prior to analysis. Additionally, the hardware limits the ability to perform the analysis in continuous flow; however, current work is being focused on resolving this. Future work should aim to test the system against more polymerization types, including step-growth and Ziegler -Natta catalyzed polymerizations, including potentially heterogeneous systems. Additionally, work will focus on using the output data to automate the variation of reaction conditions for fully automated polymer synthesis.

## ■ ASSOCIATED CONTENT

## Data Availability Statement

Raw data is available upon request.

## * sı Supporting Information

The Supporting Information is available free of charge at

.

Representative spectra for each reaction, reaction schemes, and GPC chromatograms for each reaction ( )

## ■ AUTHOR INFORMATION

## Corresponding Authors

Daniel Lester -Polymer Characterization RTP, University of Warwick, Coventry CV4 7AL, United Kingdom ; Email:

David Haddleton -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom; Polymer Characterization RTP, University of Warwick, Coventry CV4 7AL, United Kingdom; ; Email:

## Authors

Owen Tooley -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom

William Pointer -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom

Rowan Radmall -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom

Mia Hall -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom; School of Chemistry, Monash University, Clayton, VIC 3800, Australia

Thomas Swift -Department of Chemistry, University of Bradford, Bradford BD7 1DP West Yorkshire, United Kingdom;

James Town -Polymer Characterization RTP, University of

Warwick, Coventry CV4 7AL, United Kingdom Cansu Aydogan -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom School of Chemistry, Monash University,

Tanja Junkers -Clayton, VIC 3800, Australia;

Paul Wilson -Department of Chemistry, University of Warwick, Coventry CV4 7AL, United Kingdom;

Complete contact information is available at:

## Author Contributions

All authors have given approval to the final version of the manuscript. CRediT: Owen Tooley conceptualization, data curation, formal analysis, investigation, methodology, writingoriginal draft, writing-review &amp; editing; william Pointer data curation, formal analysis, investigation, methodology, writingoriginal draft; Rowan Radmall data curation, formal analysis, methodology; Mia Hall formal analysis, investigation; Thomas Swift data curation, software, supervision; James Town data curation, formal analysis, investigation; Cansu Aydogan data curation, supervision; Tanja Junkers supervision, writingreview &amp; editing; Paul Wilson supervision, writing-review &amp; editing; Daniel W. Lester funding acquisition, investigation, methodology, project administration, supervision, writingreview &amp; editing; David M. Haddleton conceptualization, funding acquisition, project administration, writing-review &amp; editing.

## Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

The authors would like to acknowledge funding for a studentship (O.T. through the EPSRC Centre for Doctoral Training in Molecular Analytical Science, EP/L015307/1), AstraZeneca plc, The University of Warwick Polymer Characterization RTP for providing access to NMR and GPC equipment, the Engineering and Physical Sciences Research Council (EP/V036211/1 and EP/V007688/1) for funding equipment, the EPSRC Prosperity Partnership with The Lubrizol Corporation (EP/V037943/1), and the Royal Society (P.W., URF\R1\180274).

## ■ ABBREVIATIONS

AIBN, azobis(isobutyronitrile); DMF, dimethylformamide; DMSO, dimethyl sulfoxide; DOSY, diffusion ordered spectroscopy; ESI, electrospray ionization; GPC, gel permeation chromatography; HPLC, high-performance liquid chromatography; MaDDOSY, mass determination diffusion ordered spectroscopy; MALDI, matrix-assisted laser desorption ionization; NMR, nuclear magnetic resonance; RAFT, reversible addition -fragmentation chain-transfer; RDRP, reversibledeactivation radical polymerization; ROP, ring-opening polymerization; SEC, size exclusion chromatography

## ■ REFERENCES

(1) Lloyd, P. M.; Suddaby, K. G.; Varney, J. E.; Scrivener, E.; Derrick, P. J.; Haddleton, D. M.

Eur. Mass Spectrom. 1995 , 1 (3), 293 -300. (2) Haven, J. J.; Junkers, T. Eur. J. Org. Chem. 2017 , 2017 (44), 6474 -6482. (3) Santos, L. S.; Metzger, J. O. Rapid Commun. Mass Spectrom. 2008 , 22 (6), 898 -904. (4) Knol, W. C.; Pirok, B. W. J.; Peters, R. A. H. J. Sep. Sci. 2021 , 44 (1), 63 -87. (5) Wu, C.; Liu, Y.; Xiao, C.; Hu, C.; Pang, X.; Chen, X.

Chin. Chem. Lett. 2024 , 35 , No. 109163,

.

H. J.; Nuhn, L.

Macromol. Rapid Commun. 2021 ,

(6)

42

Scherger, M.;

Räder,

(8), No. 2000752.

(7) Meier, M. A. R.; Hoogenboom, R.; Fijten, M. W. M.; Schneider, M.; Schubert, U. S.

J. Comb. Chem. 2003 , 5 (4),

(9)

AccuSpot

tober 20, 2023).

(10) Yau, W. W.; Kirkland, J. J.; Bly, D. D.; Striegel, A. Modern SizeExclusion Liquid Chromatography: Practice of Gel Permeation and Gel Filtration Chromatography ; John Wiley &amp; Sons, 2009.

(11)

Berek, D.

2010 , 33 (3), 315 -335.

369 -374.

(8) Pirrone, G. F.; Munsell, E. V.; Ferguson, H. M.; Al-Sayah, M. A.; Luthra, S. A.; Makarov, A. A.

J. Pharm. Sci.

Case

2023

Studies.

,

112

(11), 2778

-

2782.

(accessed Oc-

-

J. Sep. Sci.

- (12) Bergmann, J. G.; Duffy, L. J.; Stevenson, R. B. Anal. Chem. 1971 , 43 (1), 131 -133. (13) Sanches, N. B.; Dias, M. L.; Pacheco, E. B. A. V. Polym. Test. 2005 , 24 (6), 688 -693. (14) Mignard, E.; Leblanc, T.; Bertin, D.; Guerret, O.; Reed, W. F. Macromolecules 2004 , 37 (3), 966 -975. (15) Levere, M. E.; Willoughby, I.; O'Donohue, S.; Cuendias, A.; de Grice, A. J.; Fidge, C.; Becer, C. R.; Haddleton, D. M. Polym. Chem. 2010 , 1 (7), 1086 -1094. (16) Levere, M. E.; Willoughby, I.; O'Donohue, S.; Wright, P. M.; Grice, A. J.; Fidge, C.; Remzi Becer, C.; Haddleton, D. M. J. Polym. Sci., Part A: Polym. Chem. 2011 , 49 (8), 1753 -1763. (17) Van Herck, J.; Abeysekera, I.; Buckinx, A.-L.; Cai, K.; Hooker, J.; Thakur, K.; Reydt, E. V.; de Voorter, P.-J.; Wyers, D.; Junkers, T. Digital Discovery 2022 , 1 (4), 519 -526. (18) Knox, S. T.; Parkinson, S. J.; Wilding, C. Y. P.; Bourne, R. A.; Warren, N. J. Polym. Chem. 2022 , 13 (11), 1576 -1585. (19) Perrier, S.; Haddleton, D. M. In Situ NMR Monitoring of Living Radical Polymerization. In In Situ Spectroscopy of Monomer and Polymer Synthesis ; Puskas, J. E.; Long, T. E.; Storey, R. F.; Shaikh, S.; Simmons, C. L., Eds.; Springer US: Boston, MA, 2003; pp 125 -146. (20) Obermeier, B.; Frey, H. Bioconjugate Chem. 2011 , 22 (3), 436 -444. (21) Kandelhard, F.; Schuldt, K.; Schymura, J.; Georgopanos, P.; Abetz, V. Macromol. React. Eng. 2021 , 15 (4), No. 2000058. (22) Vargas, M. A.; Cudaj, M.; Hailu, K.; Sachsenheimer, K.; Guthausen, G. Macromolecules 2010 , 43 (13), 5561 -5568. (23) Castaing-Cordier, T.; Bouillaud, D.; Farjon, J.; Giraudeau, P. Annu. Rep. NMR Spectrosc. 2021 , 103 , 191 . (24) Groves, P. Polym. Chem. 2017 , 8 (44), 6700 -6708. (25) Voorter, P.-J.; McKay, A.; Dai, J.; Paravagna, O.; Cameron, N. R.; Junkers, T. Angew. Chem., Int. Ed. 2022 , 61 (5), No. e202114536. (26) Silva, I. W. F.; McKay, A.; Sokolova, A.; Junkers, T. Polym. Chem. 2024 , 15 , 1303. (27) Tooley, O.; Pointer, W.; Radmall, R.; Hall, M.; Beyer, V.; Stakem, K.; Swift, T.; Town, J.; Junkers, T.; Wilson, P.; Lester, D.; Haddleton, D. Macromol. Rapid Commun. 2024 , 45 (8), No. 2300692. (28) Li, W.; Chung, H.; Daeffler, C.; Johnson, J. A.; Grubbs, R. H. Macromolecules 2012 , 45 (24), 9595 -9603. (29) Chamignon, C.; Duret, D.; Charreyre, M.-T.; Favier, A.

Macromol. Chem. Phys. 2016 , 217 (20), 2286 -2293.

- (30) Bärenwald, R.; Achilles, A.; Lange, F.; Ferreira, T. M.; Saalwächter, K.
2. Polymers 2016 , 8 (12), 439.
- (31) Marchand, A.; Mishra, R.; Bernard, A.; Dumez, J.-N.

Chem. -Eur. J. 2022 , 28 (52), No. e202201175.

- (32) Vrijsen, J. H.; Thomlinson, I. A.; Levere, M. E.; Lyall, C. L.; Davidson, M. G.; Hintermair, U.; Junkers, T.

Polym. Chem. 2020 , 11 (21),

3546 -3550.

- (33) Ferguson, C. J.; Hughes, R. J.; Nguyen, D.; Pham, B. T. T.; Gilbert, R. G.; Serelis, A. K.; Such, C. H.; Hawkett, B. S.

Macro-

molecules 2005 , 38 (6), 2191 -2204.

(34) Ciampolini, M.; Nardi, N.

̃

- Inorg. Chem. 1966 , 5 (1), 41 -44. ar, L.; Poggetto, G. D.; Colbourne, A. A.; Morris, G. A.;
- (35) Castan Nilsson, M.

Magn. Reson. Chem. 2018 , 56 (6), 546 -558.

- (36) MaDDOSY (Mass Determination Diffusion Ordered Spectroscopy) Using an 80 MHz Bench Top NMR for the Rapid Determination of Polymer and Macromolecular Molecular Weight.
- (37) PubChem. Dioxane.

(accessed April 28, 2023).

- (38) Dynamic Viscosity of Cyclohexane from Dortmund Data Bank. (accessed April
2. 28, 2023). (39) Dong, T.; Knoshaug, E. P.; Pienkos, P. T.; Laurens, L. M. L.

Appl. Energy 2016 , 177 , 879 -895.

(40) Perrier, S.

- Macromolecules 2017 , 50 (19), 7433 -7447. (41) George Odian, Radical Chain Polymerization. In Principles of Polymerization ; John Wiley &amp; Sons, Ltd., 2004; pp 198 -349. (42) Reyhani, A.; McKenzie, T. G.; Fu, Q.; Qiao, G. G.

Polymer Handbook,

- Aust. J. Chem. 2019 , 72 (7), 479 -489. (43) Brandrup, J.; Immergut, E. H.; Grulke, E. A. 2 Volumes Set ; Wiley, 2003.