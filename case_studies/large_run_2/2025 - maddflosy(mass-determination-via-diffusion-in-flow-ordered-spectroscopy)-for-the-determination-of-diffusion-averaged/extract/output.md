<!-- image -->

pubs.acs.org/Macromolecules Article

<!-- image -->

<!-- image -->

<!-- image -->

## MaDDFLOSY(Mass Determination via Diffusion in FLow Ordered SpectroscopY) for the Determination of Diffusion-Averaged Molecular Weight of Polymers in Continuous Motion Using Benchtop NMR

William Pointer, Owen Tooley, Asad Saib, Rowan Radmall, Paul Wilson, Daniel Lester, James Town, Robin J. Blagg, and David Haddleton *

<!-- image -->

[Cite This: Macromolecules 2025, 58, 5201-5207](https://pubs.acs.org/action/showCitFormats?doi=10.1021/acs.macromol.4c03260&ref=pdf)

## ACCESS

Metrics &amp; More Article Recommendations

<!-- image -->

<!-- image -->

ABSTRACT: Real-time determination of the molecular weight of polymers synthesized in continuous flow or indeed in any process is essential for efficient and sustainable process chemistry. Typically achieved through online chromatographic techniques, such methods are often prone to perturbations, require large volumes of solvents, have lengthy acquisition times, and can result in significant process inefficiencies. We demonstrate the use of diffusion-ordered NMR spectroscopy (DOSY NMR) calibration on a 60 MHz benchtop to measure the molecular weight of polymers while in laminar flow. We then utilized this technique to monitor batch polymerization progress in real time.

## ■ INTRODUCTION

<!-- image -->

[Supporting Information](https://pubs.acs.org/doi/10.1021/acs.macromol.4c03260?goto=supporting-info&ref=pdf)

<!-- image -->

The accurate real-time determination of the molecular mass of polymers, macromolecules, and biomacromolecules is highly beneficial within any manufacturing or research setting involved in high-mass molecules and products. This capability becomes increasingly important with the growing trend toward machine learning and automated approaches for conducting and optimizing research. With this trend, the need for robust analytical techniques becomes an ever more critical factor in producing valuable data sets. 1

Currently, the most widely used method for molecular weight determination is gel permeation chromatography (GPC). However, online examples of GPC are rare, requiring highly specialized, complex equipment. 2 -6 Additionally, GPC suffers from several key limitations, namely: often poor compatibility with polymers that are difficult to solubilize, relatively long acquisition times (typically 15 -60 min) and the requirement for rigorous sample filtration. 3 Furthermore, as with any chromatographic technique, there exists a complex array of variables that can perturb a measurement, including baseline inconsistencies, solvent contamination, column fouling, interaction, and multiple instrument-dependent factors.

Alternative techniques have been developed for the monitoring of polymerization reactions, particularly the use of inline and online NMR. 7 -11 Both low-field benchtop and high-field instruments have been used to great effect to monitor polymerization progress by tracking the relative integrals of monomers and polymers, providing monomer conversion data. 12,13 This approach, while insightful for attaining conversion data, struggles to provide adequate data for polymer molecular weight and information about the product molecular characteristics, particularly when end-group fidelity is lost.

<!-- image -->

Online reaction monitoring is an adaptable quantitative approach that can be used to monitor batch reactions without the need for specialized flow reactors, making it independent of scale. In this method, the reaction mixture is continuously pumped from the reaction vessel through a detector region in the spectrometer, then circulated back to the vessel. 7 For benchtop NMR, this often involves a tubular cell fitted through the detector region, where a pump maintains the circulation of the reaction mixture. 14,15

Real-time monitoring is especially effective in reactions carried out under continuous flow conditions, where the product of the reaction is monitored after leaving the reactor. 16 In this way, real-time data can be used to dynamically optimize processes using machine learning to achieve the targeted

Received:

January 3, 2025

Revised:

March 20, 2025

Accepted:

April 9, 2025

Published:

April 16, 2025

<!-- image -->

parameters. 10 This is an effective and sustainable method for all chemical processes.

Diffusion-ordered NMR spectroscopy (DOSY) is a valuable technique that provides facile access to an analyte's diffusion coefficient. This is especially useful to polymer chemists due to the relationship between a polymer's mass and its rate of diffusion in solution. 17 -19 DOSY NMR conducted on samples in flow would therefore be a desirable evolution of the technique, allowing for online monitoring of polymerization reactions without the need for GPC. 18 Examples of this have previously been demonstrated using high-field instruments; however, there is no record of this being accomplished on a low-field instrument. 14,20

Our previous work using a benchtop NMR spectrometer demonstrated the use of a universal mass-determining diffusion-ordered spectroscopy (MaDDOSY) calibration to both accurately determine the molecular weight of a variety of polymers and monitor polymerization reactions in real time. 17,18 However, a limitation of this work was the necessity to stop the flow during diffusion data acquisition, which limits its application in continuous flow regimes. Herein, we present a further development of the MaDDOSY approach for molecular mass determination and detail methodologies to attain molecular weights of polymers in real time while in continuous motion, without the need to stop the flow of the sample whatsoever. 21

The approach of measuring molecular weight via DOSY uses the diffusion coefficient, which is related to the hydrodynamic radius of the analyte through the Stokes -Einstein relationship (eq 1), which is, in turn, related to the molecular weight through an adapted Rouse -Zimm model (eq 2). 19,22

The Stokes-Einstein Relation 23

$$D = \frac { k _ { B } T } { 6 \pi \eta r _ { h } } & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

Modified Rouse-Zimm Model.

$$r _ { h } \approx b M _ { D } ^ { \nu }$$

The mass obtained in this manner is the diffusion-averaged mass, M D. This mass should be viewed as a complementary measurement to the values of M n , M w, and M v obtained through more traditional polymer analysis. Therefore, comparisons made between M D and M n , M w, and M v must be done cautiously, as a separate physical phenomenon is being measured. 24 It is also noted that M D does not provide information about the mass dispersity of the polymer.

While previous work was limited to 'stop-flow' conditions or required complex pulse sequences only available on highfield instrumentation, recent advances in benchtop NMR hardware and software now enable more complex experiments under continuous flow conditions. 25 -27 The advantages of this are 3-fold. First, benchtop hardware allows for more complex reactions under demanding conditions, such as those typical of flow processes, to be monitored without specialized setups in proximity to high-field instrumentation. Second, benchtop NMR instrumentation is often less expensive than traditional spectrometers, through not only the initial purchase price but also the lack of requirement for regular liquid cryogen refills. Third, due to an external lock, it is not a requirement to use deuterated solvents, widening the applicability of the technique to reactions that use any common laboratory solvent.

Additionally, in previous work, a pulsed gradient stimulated echo (PGSE) sequence was used to acquire the DOSY spectra. While an excellent technique, PGSE did not provide adequate signal strength for reliable DOSY measurements in steady-state flow regimes. The J -compensated pulsed gradient spin echo (JPGSE) sequence reduces peak distortions caused by 1 H homonuclear J -coupling by refocusing the J -evolution during the spin echo to provide enhanced sensitivity, which is ideal for steady-state flow analysis under reaction conditions.

## ■ RESULTS AND DISCUSSION

Initial tests of continuous flow DOSY were conducted using a J -PGSE pulse sequence.

Samples of poly(methyl methacrylate) (PMMA), polystyrene (PS/PSTY), and poly(ethylene glycol) (PEG) were flowed through the Oxford Instruments X-Pulse 60 MHz spectrometer using a Masterflex Ismatec Reglo Miniflex Digital (peristaltic) pump. This device was chosen for providing the flow regime, as it is typical of devices used for continuous flow on the laboratory scale. While other devices, such as syringe or piston pumps, could provide a flow regime with lower pulsation, the peristaltic pump offers a more realistic view of how this analysis is likely to perform for researchers in the laboratory, allowing for recirculation. While investigating the effect of pulsation would be academically interesting, we focused our efforts on providing a valuable example using representative experimental setups.

These polymers were chosen as they represent a broad range of solvent compatibilities, molar masses, and dispersity. The masses as determined by conventional GPC are shown in Table 1. In previous work, we have shown the validity of

Table 1. Molecular Weights of Polymers as Determined by GPC/SEC (THF Eluent against a PMMA and b PSTY Narrow Molecular Weight Standards), and by DOSY NMR Experiments from a 500 and 60 MHz NMR Spectrometer with PS, PMMA, and PEG Dissolved in THF-D8, CDCl3, and D2O, Respectively

|        |   M n (GPC) g mol - 1 |   M w (GPC) g mol - 1 |   Dispersity (GPC) |   M D (500 MHz) g mol - 1 |   M D (60 MHz) g mol - 1 |
|--------|-----------------------|-----------------------|--------------------|---------------------------|--------------------------|
| a PMMA |                 18000 |                 45000 |               2.50 |                     22000 |                    37000 |
| b PS   |                 10000 |                 16700 |               1.67 |                     13000 |                     7600 |
| PEG    |                  5100 |                  5500 |               1.08 |                      5500 |                     5400 |

MaDDOSY as a tool for determining molecular masses up to 200 000 g mol -1 . 17 While polymers with masses of that order of magnitude have not been investigated here, they would be expected to perform as previously investigated,

As an additional point of comparison, DOSY experiments were also performed on each sample using a 500 MHz NMR spectrometer using a standard 'ledbpgp2s' pulse sequence. DOSY experiments using the J -PGSE pulse sequence were conducted on the samples while held static within the magnetic field to provide a reference diffusion coefficient. These DOSY experiments were performed using different pulse sequences, which may cause some discrepancy between the values obtained.

As the MaDDOSY calibration is viscosity-corrected and tolerant of any good solvent system, each polymer could have been sampled from any of its respective 'good solvents.' The concentration of each sample is critical and has been thoroughly explored in our previous work; in this case, the samples were made up well beneath the C * values determined previously. 17 Specific details of the polymer/solvent system can be found in the ESI. It is also important to note that nondeuterated solvents can be employed in this experimental setup.

In our original work, we defined a calibration curve relating the diffusion coefficient to molecular weight at 26.5 ° C; however, the magnet temperature in the spectrometer used in this current work is held at 40 ° C. As the temperature of the system is higher than that of the calibration, the measured diffusion coefficient will also be higher (eq 1). 23 In our previous work, we described the benefits of using a solventindependent universal calibration, specifically the ease of obtaining an accurate value without having to create calibrations for each polymer currently known to science. Our philosophy extends to variable temperature measurements; it is impractical to create a set of calibrations comprehensive enough to cover all experiments and spectrometers. Therefore, a simple correction can be performed by calculating the hydrodynamic radius using the Stokes -Einstein equation at the experimental temperature (in this case 40 ° C) using the solvent viscosity at that temperature, 28 and subsequently back-calculating the theoretical diffusion constant at 26.5 ° C. This value can then be used to calculate the mass of the polymer using MaDDOSY. To confirm the validity of this approach, a sample of PEG was measured at both 40 ° C and 26.5 ° C with the same correction applied to the measurement taken at 40 ° C. The resulting diffusion coefficients showed an agreement of 99%, the full details can be found in the Supporting Information. While unorthodox, this correction only requires the use of the Stokes -Einstein equation and does not necessitate the use of expensive analytical time or the creation of an additional calibration curve. It must be noted that this correction may be reliable only for relatively small temperature differences, as is the case here. The masses shown in Table 1 have had this correction applied.

PEG shows a strong correlation between the three mass values, indicating that the M D determined by the benchtop is a valuable measure for this material. Notably, this PEG sample has a low dispersity. The M D determined on the 500 MHz spectrometer shows strong agreement with the 60 MHz, while this is not overly remarkable; it must be remembered that two different pulse sequences have been used, and the strong correlation between these two samples may be due more to the low dispersity of the sample rather than global agreement between the two techniques.

In a vein similar to PEG, the M D for PMMA falls between the M n and M w. This is a particularly interesting sample to analyze as there is a wide distribution of molecular species with different diffusion coefficients present in the sample. GPC analysis of PMMA shows a mass distribution from 1 to 300 kg mol -1 (see Supporting Information). This value emphasizes that the M D should be considered as a complementary mass value rather than as an alternative to the traditionally reported masses. There is some variation in the measurement of M D for PMMA from the 500 and the 60 MHz spectrometers, and this is interesting for a number of reasons, primarily because it indicates that the agreement between high-field and low-field NMRs is not guaranteed and seems to deviate more as the dispersity of the polymer increases. Significantly more work is required to explore in detail how the mass, dispersity, and pulse sequence interplay to fully understand the limits and benefits of this approach. It must also be remembered that M D is neither M n nor M w and may not correlate with either.

When determining M D (60 MHz) for polystyrene (PS), we investigated the use of a nonbackbone hydrogen signal to determine the diffusion coefficient; in this case, the integral of the whole aromatic region was used. The M D value obtained from these peaks was lower than expected, likely due to the increased degrees of motion of these pendant groups. This additional motion affects T1 of the polymer, making the polymer appear to diffuse faster and appear as a smaller polymer. It is useful to understand the limitations of this technique; therefore, PS samples were further tested under continuous flow conditions. For totality, when the diffusion constant was fitted globally, using both the benzyl and backbone peaks, as used for the data acquired at 500 MHz, there is once again near-perfect (Table 1) agreement between GPC and MaDDOSY.

Following this, the samples of each PMMA, PS, and PEG were made up at 50 mg/mL in chloroform, dioxane, and water and were subjected to a range of steady-state laminar flow regimes of 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, and 4.0 mL min -1 , and the diffusion coefficients were determined by J -PGSE experiments. These flow rates have previously been shown to be suitable for diffusion experiments in high-field studies. 20 A master-flex peristaltic pump was used to flow the samples through the cell. The nature of the peristaltic pump results in some degree of pulsatile flow, leading to a variation in sample flow velocities in the active volume during acquisition. This will introduce additional error into the measurement of the diffusion coefficients. As previously stated, a lower pulsation pump could be used, but a peristaltic pump is more representative of real-world conditions, and the investigation of pump type is outside the scope of this communication. 29

The resulting diffusion coefficients for each polymer are listed in Figure 1. Among these samples, only PS demonstrates any correlation between the experimentally determined diffusion constants and the flow rate of the analyte, with a slight increase in diffusion at higher flow rates, though this correlation is weak. In contrast, PMMA and PEG show no correlation between the flow rate and the diffusion coefficient.

Figure 1. Top- Diffusion coefficients of PMMA (Blue), PEG (Red), and PS (Black) as determined in steady-state continuous flow. Bottom- residuals of each measurement compared to the mean value of each data set.

<!-- image -->

Overall, no clear/consistent correlation between the diffusion coefficient and flow rate is observed when considering all three data sets. The PS, PMMA, and PEG measurements had coefficients of variance of 8.82%, 12.5%, and 6.94%, respectively, well within the accepted 10% error range of a typical, conventional GPC experiment (Figure 1). This further demonstrates a lack of correlation across all three data sets with respect to the flow rate. This test has only been used on a limited range of flow rates and only begins to explore this technique's limits. The results suggest that for the flow rates explored here, there is, in principle, no reason for flow to be stopped during measurements, giving credence to the use of the technique in continuous flow systems. To investigate the reliability of this approach, a series of tests were conducted whereby the samples were flowed at a consistent flow rate through the spectrometer for several hours, with a series of DOSY measurements being conducted consecutively. The error bars for the PEG samples in Figure 1 show the standard deviation of 10 repeat measurements for each condition used.

From these diffusion coefficients, the M D value can be determined as previously described (Figure 2). Since there is only a slight variation in the diffusion coefficients across different flow rates, the resulting M D values also show minor variation.

Figure 2. M D values for PMMA (blue), PS (black), and PEG (red) as determined at a range of continuous flow rates.

<!-- image -->

There is again no clear correlation between flow rate and M D, with the measurements for PS and PEG samples falling within a 10% coefficient of variance of the averaged M D. For the PS samples, the use of the pendant benzyl groups led to an underestimation of the mass, which was expected following the initial testing. However, this is a strong indicator that nonbackbone hydrogen signals are unsuitable for analysis with this method, as previously discussed. Additionally, the M D values for PS show a larger spread compared to the other two samples, though still within a 15% coefficient of variance of the averaged M D.

To achieve real-time online monitoring with the sample continuously moving through the detector, a well-studied reaction was conducted: RAFT polymerization of methyl acrylate in batch, with the reaction mixture circulating through the system (Figure 3). Full experimental details are available in the Figure S3. Based on the results shown in Figures 1 and 2, a flow rate of 1 mL min -1 was selected. Both standard 1D 1 H and J -PGSE DOSY spectra were collected, interleaved with the 1D used for conversion calculations and DOSY for molecular weight calculations. While the temperature used in the thermally initiated RAFT process is higher than the temperature within the spectrometer, it was determined that the reaction mixture was cooled sufficiently by passing through the room-temperature tubing to avoid impacting the measurement. Again, this experimental setup was used to demonstrate how this method can be applied in a practical sense. While the reaction mixture in the vessel was warmer than the spectrometer, the passive cooling through approximately 2 m of tubing was more than sufficient to cool the mixture to room temperature. Additionally, later tests showed that a sample at room temperature passing through the spectrometer at flow rates comparable to ours had a temperature of 40 ° C when leaving the spectrometer (see Supporting Information for more details).

The progress of the RAFT reaction was monitored as a function of time (Figure 4). As expected for a living polymerization, we observed an increase in molecular weight over time along with a corresponding increase in monomer conversion. The mass of the polymer continued to increase as the reaction progressed, reaching a maximum of ∼ 7000 Da at the termination of the reaction. Offline verification of the resulting mass of the polymer was conducted by GPC, yielding M n = 4070 and M w = 6470 g mol -1 , based on a differential refractive index (DRI) detector and PMMA calibration with narrow molecular weight standards.

This reaction exhibits the expected kinetics of a typical living radical process, with a first-order rate constant of 1.27 ± 0.21 s -1 , in agreement with literature values. 30 Additionally, the 95% confidence intervals in these data are, throughout, not larger than 15%, similar to the typical uncertainties associated with GPC. This technique, however, is fully online and does not lose any sample during analysis.

We observe a good correlation between monomer conversion and expected product mass (Figure 5). The general trend of the experimentally determined masses matches the expected masses associated with a DP = 100 poly(methyl acrylate) made by RAFT polymerization. As the polymerization reaches completion, there is a degree of variability within the determined mass; however, this theoretical mass is never outside the 95% confidence interval of any other measured value. This rate of monitoring is consistent with traditional online GPC; however, the conditions of these tests are only a start point for further optimization; therefore, it is not unrealistic to assume that the rate of data acquisition could be reduced, in line with stop-flow techniques described previously 17,18

Here, we have demonstrated a method to conduct MaDDOSY analysis under a range of continuous flow rates from 0.1 to 4 mL min -1 , showing no correlation between the flow rate of the analyte and the resulting diffusion coefficient or M D. We also illustrate the application of this approach in monitoring an example of RAFT polymerization.

In this communication, we employed a limited range of polymers, molecular weights, and polymerization techniques, and we believe that this technique retains the universality of the original MaDDOSY calibration. Further work should aim to demonstrate MaDDOSY in continuous flow processes for a broader range of reaction mechanisms. This noninvasive and nondestructive technique shows promise for measuring polymer masses in continuous flow, with relevance to living polymerizations that yield narrow dispersity polymers, especially those that require moistureand oxygen-free conditions. High polydispersity samples remain challenging to analyze accurately with this technique, and work is ongoing to not only provide more useful insight into these polymers but also, more generally, toward the facile determination of polydispersity.

<!-- image -->

Figure 3. Schematic of the RAFT polymerization experimental set up.

Figure 4. Polymerization of MA via thermally initiated RAFT as measured via continuous flow DOSY.

<!-- image -->

Figure 5. Molecular weight versus conversion for the RAFT polymerization of methyl acrylate.

<!-- image -->

This novel technique, which we have named mass acquisition by diffusion-in-flow ordered spectroscopy (MADFLOSY), and additional studies are planned to explore the full capabilities and limits of this approach for measuring molecular weight in the coming months and to demonstrate the broader utility of MADFLOSY for reaction monitoring in continuous flow chemistry.

## ■ ASSOCIATED CONTENT

## * sı Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.macromol.4c03260.

Experimental procedures and spectra, materials and instrumentation (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

David Haddleton -Department of Chemistry, University of Warwick, Coventry CV47AL, U.K.; Polymer 7AL, U.K.; orcid.org/0000-0002-4965-0827;

Characterization RTP, University of Warwick, Coventry CV4 Email: d.m.haddleton@warwick.ac.uk

## Authors

William Pointer -Department of Chemistry, University of Warwick, Coventry CV47AL, U.K.; Polymer

Characterization RTP, University of Warwick, Coventry CV4 7AL, U.K.; orcid.org/0000-0003-4078-0489 Characterization RTP, University of Warwick, Coventry CV4

Owen Tooley -Department of Chemistry, University of Warwick, Coventry CV47AL, U.K.; Polymer 7AL, U.K.; orcid.org/0000-0002-6618-3407

- Asad Saib -Oxford Instruments, Buckinghamshire HP12 3SE, U.K.
- Rowan Radmall -Department of Chemistry, University of Warwick, Coventry CV47AL, U.K.; Polymer Characterization RTP, University of Warwick, Coventry CV4 7AL, U.K.
- Paul Wilson -Department of Chemistry, University of Warwick, Coventry CV47AL, U.K.; Polymer Characterization RTP, University of Warwick, Coventry CV4 7AL, U.K.; orcid.org/0000-0002-9760-899X
- Daniel Lester -Polymer Characterization RTP, University of Warwick, Coventry CV4 7AL, U.K.
- James Town -Polymer Characterization RTP, University of Warwick, Coventry CV4 7AL, U.K.
- Robin J. Blagg -Oxford Instruments, Buckinghamshire HP12 3SE, U.K.

Complete contact information is available at:

[https://pubs.acs.org/10.1021/acs.macromol.4c03260](https://pubs.acs.org/doi/10.1021/acs.macromol.4c03260?ref=pdf)

## Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

The authors would like to acknowledge funding for a studentship (QT through the EPSRC Centre for Doctoral Training in Molecular Analytical Science, EP/L015307/1, AstraZeneca plc, Oxford Instruments PLC for providing access to benchtop NMR equipment, The University of Warwick Polymer Characterization RTP for providing access to NMR and GPC equipment and the Engineering and Physical Sciences Research Council (EP/V036211/1 and EP/ V007688/1) for funding equipment and the EPSRC Prosperity Partnership with The Lubrizol Corporation (EP/V037943/1) and the Royal Society (PW, URF\R1\180274).

## ■ REFERENCES

- (1) Keith, J. A.; Vassilev-Galindo, V.; Cheng, B.; Chmiela, S.; Gastegger, M.; Muller, K. R.; Tkatchenko, A. Combining Machine Learning and Computational Chemistry for Predictive Insights Into Chemical Systems. Chem. Rev. 2021 , 121 (16), 9816 -9872.
- (2) Junkers, T. 4 Polymer synthesis in continuous flow. In Vol. 2 Flow Chemistry -Applications 2ndFerenc, D.; György, D.; Volker, H.; Ley, S. L.De Gruyter2021pp. 99 -134
- (3) Van Herck, J.; Abeysekera, I.; Buckinx, A.-L.; Cai, K.; Hooker, J.; Thakur, K.; Van de Reydt, E.; Voorter, P.-J.; Wyers, D.; Junkers, T. Operator-independent high-throughput polymerization screening based on automated inline NMR and online SEC. Digital Discovery 2022 , 1 (4), 519 -526.
- (4) Knox, S. T.; Parkinson, S. J.; Wilding, C. Y. P.; Bourne, R. A.; Warren, N. J. Autonomous polymer synthesis delivered by multiobjective closed-loop optimization. Polym. Chem. 2022 , 13 (11), 1576 -1585.
- (5) Rosenfeld, C.; Serra, C.; O'Donohue, S.; Hadziioannou, G. Continuous Online Rapid Size Exclusion Chromatography Monitoring of Polymerizations - CORSEMP. Macromol. React. Eng. 2007 , 1 (5), 547 -552.
- (6) Levere, M. E.; Willoughby, I.; O'Donohue, S.; de Cuendias, A.; Grice, A. J.; Fidge, C.; Becer, C. R.; Haddleton, D. M. Assessment of SET-LRP in DMSO using online monitoring and Rapid GPC. Polym. Chem. 2010 , 1 (7), 1086 -1094.
- (7) Maschmeyer, T.; Yunker, L. P. E.; Hein, J. E. Quantitative and convenient real-time reaction monitoring using stopped-flow benchtop NMR. React. Chem. Eng. 2022 , 7 (5), 1061 -1072.
- (8) Giraudeau, P.; Felpin, F.-X. Flow reactors integrated with in-line monitoring using benchtop NMR spectroscopy. React. Chem. Eng. 2018 , 3 (4), 399 -413.
- (9) Knox, S. T.; Parkinson, S.; Stone, R.; Warren, N. J. Benchtop flow-NMR for rapid online monitoring of RAFT and free radical polymerisation in batch and continuous reactors. Poly. Chem. 2019 , 10 (35), 4774 -4778.
- (10) [Rubens, M.; Van Herck, J.; Junkers, T. Automated Polymer Synthesis Platform for Integrated Conversion Targeting Based on Inline Benchtop NMR. ACS Macro Lett. 2019 , 8 (11), 1437 -1441.](https://doi.org/10.1021/acsmacrolett.9b00767?urlappend=%3Fref%3DPDF&jav=VoR&rel=cite-as)
- (11) Vrijsen, J. H.; Thomlinson, I. A.; Levere, M. E.; Lyall, C. L.; Davidson, M. G.; Hintermair, U.; Junkers, T. Online tracing of molecular weight evolution during radical polymerization via highresolution FlowNMR spectroscopy. Polym. Chem. 2020 , 11 (21), 3546 -3550.
- (12) Cortes-Borda, D.; Wimmer, E.; Gouilleux, B.; Barre, E.; Oger, N.; Goulamaly, L.; Peault, L.; Charrier, B.; Truchet, C.; Giraudeau, P.; et al. An Autonomous Self-Optimizing Flow Reactor for the Synthesis of Natural Product Carpanone. J. Org. Chem. 2018 , 83 (23), 14286 -14299.
- (13) Izunobi, J. U.; Higginbotham, C. L. Polymer Molecular Weight Analysis by 1H NMR Spectroscopy. J. Chem. Educ. 2011 , 88 (8), 1098 -1104.
- (14) Marchand, A.; Mishra, R.; VBernard, A.; Dumez, J. N. Online Reaction Monitoring with Fast and Flow-CompatibleDiffusion NMR Spectroscopy. Chem.-Eur. J. 2022 , 28 (52), No. e202201175.
- (15) Hall, A. M. R.; Broomfield-Tagg, R.; Camilleri, M.; Carbery, D. R.; Codina, A.; Whittaker, D. T. E.; Coombes, S.; Lowe, J. P.; Hintermair, U. Online monitoring of a photocatalytic reaction by realtime high resolution FlowNMR spectroscopy. Chem. Commun. 2018 , 54 (1), 30 -33.

́

- (16) Beres , M. A.; Zhang, B.; Junkers, T.; Perrier, S. Kinetic investigation of photoiniferter-RAFT polymerization in continuous flow using inline NMR analysis. Polym. Chem. 2024 , 15 , 3166 -3175.
- (17) Tooley, O.; Pointer, W.; Radmall, R.; Hall, M.; Beyer, V.; Stakem, K.; Swift, T.; Town, J.; Junkers, T.; Wilson, P.; et al. MaDDOSY (Mass Determination Diffusion Ordered Spectroscopy) using an 80 MHz Bench Top NMR for the Rapid Determination of Polymer and Macromolecular Molecular Weight. Macromol. Rapid Commun. 2024 , 45 (8), No. e2300692.
- (18) Tooley, O.; Pointer, W.; Radmall, R.; Hall, M.; Swift, T.; Town, J.; Aydogan, C.; Junkers, T.; Wilson, P.; Lester, D.; et al. Real-Time Determination of Molecular Weight: Use of MaDDOSY (Mass Determination Diffusion Ordered Spectroscopy) to Monitor the Progress of Polymerization Reactions. ACS Polym. Au 2024 , 4 (4), 311 -319.
- (19) Voorter, P. J.; McKay, A.; Dai, J.; Paravagna, O.; Cameron, N. R.; Junkers, T. Solvent-Independent Molecular Weight Determination of Polymers Based on a Truly Universal Calibration. Angew. Chem. Int. Ed. 2022 , 61 (5), No. e202114536.
- (20) Thomlinson, I. A.; Davidson, M. G.; Lyall, C. L.; Lowe, J. P.; Hintermair, U. Fast and accurate diffusion NMR acquisition in continuous flow. Chem. Commun. 2022 , 58 (59), 8242 -8245.
- (21) Torres, A. M.; Zheng, G.; Price, W. S. J-compensated PGSE: an improved NMR diffusion experiment with fewer phase distortions. Magn. Reson. Chem 2010 , 48 (2), 129 -133.
- (22) Kubo, T.; Nose, T. Diffusion of Single Chains in Polymer Matrices as Measured by Pulsed-Field-Gradient NMR: Crossover from Zimm- to Rouse-Type Diffusion. Polym. J. 1992 , 24 (12), 1351 -1361.

̈

- (23) [Einstein, A. U ber die von der molekularkinetischen Theorie der Wa rme geforderte Bewegung von in ruhenden Flu ssigkeiten suspendierten Teilchen. Ann. Phys. 1905 , 322 (8), 549 -560.](https://doi.org/10.1002/andp.19053220806)

̈

- (24) Groves, P. Diffusion ordered spectroscopy (DOSY) as applied to polymers. Polym. Chem. 2017 , 8 (44), 6700 -6708.
- (25) Jacquemmoz, C.; Giraud, F.; Dumez, J. N. Online reaction monitoring by single-scan 2D NMR under flow conditions. Analyst 2020 , 145 (2), 478 -485.

̈

- (26) Castaing-Cordier, T.; B, D.; Farjon, J.; Giraudeau, P. Recent advances in benchtop NMR and its applications. Annu. Rep. NMR Spectrosc 2021 , 103 , 191 -258.
- (27) Gouilleux, B.; Charrier, B.; Danieli, E.; Dumez, J. N.; Akoka, S.; Felpin, F. X.; Rodriguez-Zubiri, M.; Giraudeau, P. Real-time reaction monitoring by ultrafast 2D NMR on a benchtop spectrometer. Analyst 2015 , 140 (23), 7854 -7858.
- (28) Dean, J. Lange's Handbook Of Chemistry , 12th ed.; McGrawHill, 1978.

́

- (29) Saib, A.; Bara-Estau n, A.; Harper, O. J.; Berry, D. B. G.; Thomlinson, I. A.; Broomfield-Tagg, R.; Lowe, J. P.; Lyall, C. L.; Hintermair, U. Engineering aspects of FlowNMR spectroscopy setups for online analysis of solution-phase processes. React. Chem. Eng. 2021 , 6 (9), 1548 -1573.
- (30) [Siqueira, J. S.; Florenzano, F. H.; Reed, W. F. Kinetic analysis of continuous reaction data for RAFT and free radical copolymerization with acrylic and styrenic monomers. Polymer 2021 , 226 , 123798.](https://doi.org/10.1016/j.polymer.2021.123798)

<!-- image -->