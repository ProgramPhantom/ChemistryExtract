<!-- image -->

## Rapid Online Analysis of Photopolymerization Kinetics and Molecular Weight Using Di ff usion NMR

<!-- image -->

ACCESS

<!-- image -->

ABSTRACT: Online, high-throughput molecular weight analysis of polymerizations is rare, with most studies relying on tedious sampling techniques and batchwise postanalysis. The ability to track both monomer conversion and molecular weight evolution in real time could underpin precision polymer development and facilitate study of rapid polymerization reactions. Here, we use a single time-resolved di ff usion nuclear magnetic resonance (NMR) experiment to simultaneously study the kinetics and molecular weight evolution during a photopolymerization, with in situ irradiation inside the NMR instrument. As a model system, we used a photoinduced electron transfer reversible addition -fragmentation chain transfer (PET-RAFT) polymerization. The data allow di ff usion coe ffi cients and intensities to be calculated every 14 s from which the polymer size and monomer conversion can be extracted. Key to this approach is (1) the use of

*

s

ı

<!-- image -->

shu ffl ed gradient amplitudes in the di ff usion NMR experiment to access reactions of any rate, (2) the addition of a relaxation agent to increase achievable time resolution and, (3) a sliding correction that accounts for viscosity changes during polymerization. Di ff usion NMR o ff ers a uniquely simple, translatable handle for online monitoring of polymerization reactions.

M onitoring reactions in real time is vital for understanding reaction mechanisms and optimizing synthetic procedures. The achievable time-resolution and use of enclosed vessels enables the online analysis of rapid and highly sensitive processes, where batchwise processing is impractical. For polymerizations, online analysis of kinetics and molecular weight evolution generally requires fl ow reactors coupled with characterization techniques, such as gel permeation chromatography (GPC). The use of GPC limits studies to materials that fully dissolve in common solvents and con fi nes the analysis to batchwise processing, restricting temporal resolution. Nuclear magnetic resonance (NMR) spectrometers are commonplace and are routinely used for kinetic and mechanistic studies. Inline benchtop NMR has even been used for rapid, automated screening of polymerizations. Sometimes the 1 H NMR resonances of polymer chain and end group protons can be used to rmine the apparent number-average molecular weight ( M n ). , However, such analysis is fraught with di ffi culty when used in isolation and is not possible for large polymers or where the relevant NMR signals overlap. In such instances, di ff usion NMR o ff ers an alternative means of establishing polymer size and dispersity ( Đ ).

At in fi nite dilution, the self-di ff usion coe ffi cient ( D ) of any species is intrinsically linked to molecular size, shape, and solvent viscosity ( η 0 ). For the simple case of a spherical particle with e ff ective hydrodynamic radius r , the relationship is given by the Stokes -Einstein equation ( ' stick ' boundary condition):

$$\frac { r _ { - } } { i c } \quad D = \frac { k _ { B } T } { 6 \pi \eta _ { 0 } r }$$

where k B is the Boltzmann constant and T is the temperature. Using the Mark -Houwink relationship for monodisperse, in fi nitely dilute systems, the equation can be expressed in terms of the viscosity-average molecular weight ( M v ):

$$\begin{array} { c c } \text {el} \\ \text {s} & D = \frac { k _ { B } T } { 6 \pi \eta _ { 0 } } \left ( \frac { 1 0 \pi N _ { A } } { 3 K M _ { v } ^ { \alpha + 1 } } \right ) ^ { 1 / 3 } \\ \text {g} \\ \text { )} & \text {where } N _ { A } \text { is A vogadro's number, and } K \text { and } \alpha \text { are the Mark-} \end{array}$$

where N A is Avogadro ' s number, and K and α are the Mark -Houwink coe ffi cients speci fi c to the polymer -solvent system. Simplifyi , an empirical scaling relationship is obtained: ,

$$e ^ { ( 1 ) } = k M _ { v } ^ { a }$$

where k and a are variables speci fi c to the polymer system that encompass the shape and density of the polymers in a given solvent and changes to solution viscosity ( η ) caused by polymer size. This relationship has been extended to the

Received:

November 16, 2021

Accepted:

January 5, 2022

<!-- image -->

weight-average molecular weight ( M w), with calculated molecular weights compari ell with those from GPC for a range of polymer samples. ,

Photoinduced electron transfer -reversible addition -fragmentation chain transfer (PET-RAFT) polymerization is a controlled radical process, now routinely used to prepare vinyl polymers with diverse architectures, such as the reaction shown in a. The method is widely used due to excellent tolerance to oxygen, spatiotemporal control, and chain-end fi delity. Despite examples of online monitoring of kinetics using Fourier transform near-infrared or NMR, no method exists for rapid online molecular weight analysis.

Di ff usion NMR measurements , , are based on the pulsed gradient spin -echo (PGSE) NMR sequence and variation ch as the stimulated echo-based PGSTE sequence, -and can be used to obtain the di ff usion coe ffi cients of polymers. Sometimes the di ff usion NMR data can be presented in a 2D display mode commonly referred to as di ff usion-ordered spectroscopy (DOSY) to accentuate the ability of di ff usion NMR to separate components in mixtures according to their di ff usion coe ffi cients. Di ff usion NMR has been used to monitor the molecular weight evolution during polymerizations via batchwise sampling of the reaction mixture. Online monitoring has been possible using a fl ow reactor or in a single NMR tube, though the methods were limited to polymerizations with rates that are slow compared to the di ff usion NMR measurement time scale. In contrast, timeresolved di ff usion NMR expands the range of reaction rates that can be studied by ensuring changes in concentration and relaxat do not impact the PGSE NMR measurement. , , , The method has been successfully applied to a variety of dynamic systems, including oligomer formation, polymer growth, and polysaccharide degradation.

Herein we describe how time-resolved di ff usion NMR experiments can be used in situ to monitor the kinetics and molecular size evolution during polymerizations. We demonstrate this approach using the PET-RAFT polymerization of methyl acrylate (MA) activated by zinc tetraphenylporphyrin (ZnTPP) photocatalyst as an example system ( a,b). Sample irradiation is achieved in situ using a fi ber optic cable, a ff ording an online analysis technique that is broadly applicable to any polymerization with a low dispersity.

We aimed to simultaneously measure the monomer conversion and polymer molecular weight during a polymerization reaction using a single di ff usion NMR experiment. In a PGSE sequence, the fi rst magnetic gradient pulse (of duration δ and magnitude g ) spatially encodes the transverse magnetization of each species into a helix. Di ff usion in the direction of the gradient attenuates the helix. After a delay Δ , an identical but e ff ectively negative gradient pulse is then applied to unwind the helix. Thus, Δ de fi nes the time scale of the di ff usion measurement. The acquired signal intensity ( I ) of each species will be attenuated by both spin relaxation over the duration of the sequence and by di ff usion during Δ . Denoting the signal that would be acquired in the absence of di ff usion (or equivalently, absence of a gradient pulse) as I 0 , the observed NMR signal intensity for a PGSE sequence is given by the S l -Tanner equation (for a single freely di ff using species): ,

$$\S p c e r s ) . & & \intertext { s p c e r s } I = I _ { 0 } \, \exp \left [ - D ( \gamma \delta g ) ^ { 2 } \left ( \Delta - \frac { \delta } { 3 } \right ) \right ] = I _ { 0 } \, \exp [ - D b ] & & \intertext { m e a s s } ( 4 ) & & \intertext { d i f f u s }$$

Figure 1. PET-RAFT polymerization of methyl acrylate (MA) to poly(methyl acrylate) (PMA) using photocatalyst zinc tetraphenylporphyrin (ZnTPP) and RAFT agent 4-((((2-carboxyethyl)thio)carbonothioyl)thio)-4-cyanopentanoic acid (BM1433) in DMSOd 6 . (a) Reaction scheme and (b) time-dependence of di ff usion NMR spectra ( 1 H, 500 MHz, PGSTE, δ = 6 ms, g = 2.65 G cm -1 , Δ = 50 ms). Reaction conditions: [MA]/[BM1433]/[ZnTPP]: 100:1:0.01, 0.5 M MA, 170 μ M Gd-DTPA, irradiation with 567 nm, 298 K. (c) The PGSTE pulse sequence used for di ff usion NMR experiments, radiofrequency (RF) pulses and gradient pulses ( g ), de fi ning time periods τ 1 and τ 2 , gradient amplitude g , gradient duration δ , and di ff usion time Δ . The relaxation delay (not shown) is the time between the end of one application of the pulse sequence to the start of the next. See for full pulse sequence used in this work.

<!-- image -->

where γ is the gyromagnetic ratio. As shown, all the gradient parameters can be summarized by the di ff usion weighting factor b . In the absence of spin relaxation changes, I 0 is proportional to the concentration of the species.

Normally a series of spectra are collected with b varied monotonically by altering g to achieve a signal attenuation of ∼ 90% with the largest b value used (i.e., bD ∼ 2.3). Estimates for D and I 0 can then be obtained by nonlinear regression of onto the data ( , right). However, for dynamic systems, g should be varied in a shu ffl ed order to reduce any correlation between gradient ordering and nondi ff usion-based intensity cha at is, changes in concentrations or relaxation rates. , , The use of a long shu ffl ed list (e.g., 500 amplitudes) allows a moving fi t ( ' windowing ' ) of to be applied to a contiguously acquired set of spectra ( ). This leads to impro me resolution that is crucial for studying rapid processes. , In this work, a long shu ffl ed list of 512 gradient amplitudes was created ( ), and di ff usion data was processed in windows of 32 b values.

Parameter optimization for di ff usion NMR experiments on static polymer samples has been discussed previously. However, additional considerations are required for in situ measurements. For instance, it is useful to study both the monomer and the polymer during a polymerization, but the di ff usion coe ffi cients of these species may di ff er by orders of magnitude due to the vastly di ff erent molecular sizes. Thus, ∼ 90% attenuation will be unattainable for both species over the same range of gradient amplitudes. To tackle this issue, δ and Δ were chosen such that approximately half of the gradient amplitudes in a processing window (e.g., 4 of 7 gradient amplitudes in ) resulted in a measurable signal for the fast-di ff using species, while the remaining gradient amplitudes resulted in full attenuation and were excluded from processing. The shu ffl ed gradient amplitude list was designed to ensure the di ff usion coe ffi cients of the fast-di ff using species could be accurately determined at all times. The signal for the largest polymer species was attenuated by ∼ 70%, but additional experiments with parameters for optimized attenuation ( bD ∼ 2, for the largest b ) con fi rmed the di ff usion coe ffi cient was accurately estimated ( ).

Figure 2. Principles of time-resolved di ff usion NMR. , Nine gradient slices from a di ff usion NMR experiment acquired with shu ffl ed g values during the PET-RAFT polymerization are displayed (NB only the water peak is shown). A moving fi t to temporally contiguous subsets (three are shown) allows improved timeresolution of the estimated D and I 0 . Shu ffl ing g values removes the correlation between the gradient order and nondi ff usion-based intensity changes in dynamic systems.

<!-- image -->

The polymerization kinetics can be simultaneously measured directly from the calculated intensities ( I 0 ), as long as I 0 is not a ff ected by time-dependent spin-relaxation constants. To avoid interference from such relaxation changes during a reaction, Δ and the relaxation delay must be carefully selected. In the PGSTE NMR experiment, signal is lost to transverse relaxation (time constant T 2 ) during τ 1 and longitudinal ation (time constant T 1 ) during the τ 2 period ( c). , Thus, as Δ encompasses τ 2 , we require conditions of Δ &lt; T 1 for the proton with the shortest T 1 to avoid signal loss. Additionally, the relaxation delay should be 5 × T 1 for the proton with the longest T 1 to ensure su ffi cient relaxation and maximum signal of all protons, simplifying analysis. If a T 1 is long, the required experiment time may be impractical for studying fast processes. To improve time-resolution, a paramagnetic relaxation agent like gadolinium-diethylenetriamine pentaacetic acid (GdDTPA) can be added to reduce the T 1 of all protons in solution, allowing shorter relaxation delays, as we demonstrate here.

We now consider the PET-RAFT polymerization of MA in a. The longest T 1 of interest in the reaction solution prior to irradiation is 5.20 ± 0.01 s for the vinyl MA signal marked a ′ in Figure 1 ( ). Adding 170 μ M Gd-DTPA

reduced this T 1 to 1.94 ± 0.05 s, with no change to the di ff usion coe ffi cient ( ). As such, the relaxation delay was set to 10 s (5 × T 1 ), allowing one gradient slice to be collected every 14 s ( ∼ 7 min to collect 32 gradient slices for the fi rst data point). Similarly, Δ was set to 50 ms after measuring the shortest T 1 of the polymer (formed after 2 h) as 600 ± 10 ms (i.e., T 1 ≫ 50 ms; ). Time-resolved T 1 measurements ( ) during the PET-RAFT reaction con fi rmed these parameters would be suitable throughout the polymerization ( ).

With the di ff usion NMR experiment optimized for the system, the polymerization was carried out in a NMR tube, using a fi ber optic for continuous irradiation in the spectrometer. To disrupt the convective fl ow known to result from heating during in situ irradiation, we used physical obstruction by packing the NMR tube with glass capillaries (see ) to ensure accuracy of the di ff usion coe ffi cients. The measurement was repeated three times to assess reproducibility. The resulting di ff usion coe ffi cients and intensity data obtained during the PET-RAFT polymerization are shown in a,b. The intensity data ( I 0 ) in b are representative of species concentration due to the careful selection of relaxation delay and di ff usion time discussed above (see for full details). Thus, monomer conversion can be calculated during the reaction using the di ff usion NMR data ( c). The fi nal conversion of 66 ± 1% after 2 h of irradiation was veri fi ed with the integrated signal intensity from a standard 1 H NMR experiment (dashed line, ). This monomer conversion is lower than the 83% conversion from a previous report, which used similar experimental conditions. The reduced value may result from the use of capillaries to restrict transport rather than mixing the sample.

Figure 3. Simultaneous (a) di ff usion, (b) intensity ( I 0 ), and (c) conversion results from single di ff usion NMR experiment ( 1 H, 500 MHz, PGSTE δ = 6 ms, Δ = 50 ms, g = 3 -50 G cm -1 , 298 K) during PET-RAFT polymerization with in situ irradiation. Dashed line in (c) corresponds to conversion measured with 1 H NMR spectrum obtained after 2 h of irradiation. Shaded areas indicate the standard deviation over three experiments.

<!-- image -->

The di ff usion coe ffi cient of PMA after approximately 7 min irradiation was 1.2 ± 0.6 × 10 -10 m 2 s -1 and decreased to 3.2 ± 0.1 × 10 -11 m 2 s -1 after 2 h. The decrease is caused by both the increasing polymer size and the increase in solution viscosity. The viscosity change is also evident in the decreased di ff usion coe ffi cients of the monomer and residual solvent (DMSOd 5 ). Both species experience an approximate 10% decrease in their respective di ff usion coe ffi cients over the 2 h experiment, consistent with a 10% increase in solution viscosity.

The di ff usion coe ffi cient of a polymer can be used to estimate its molecular weight using . A suitable calibration curve should be using standards with known molecular weights. , , , , We prepared a calibration curve using poly(ethylene glycol) (PEG) standards with peak molecular weight ( M p) of 1900 -11850 g mol -1 ( ), veri fi ed by GPC ( ). While holds for in fi nitely

Figure 4. Calibration curve of PEG di ff using in DMSOd 6 for estimating the molecular weight of a polymer. M p veri fi ed with GPC and D from di ff usion NMR experiments ( 1 H, 500 MHz, PGSTE, δ = 6 ms, Δ = 50 ms, g = 3 -50 G cm -1 , 298 K). Dashed line corresponds to nonlinear regression of onto the data.

<!-- image -->

dilute systems, the concentration of the polymer is high during the studied reaction, leading to signi fi cant interactions between molecules in solution and, thus, a higher solution viscosity. Hence, it is necessary to correct the di ff usion coe ffi cient for the observed viscosity change. From , the di ff usion coe ffi cient of each species will be equally a ff ected by viscosity ( D ∝ η -1 ), so the change in the di ff usion coe ffi cient of the solvent can be used to correct the di ff usion coe ffi cient of the polymer ( ).

The apparent molecular weight of the PMA polymer was estimated during the reaction for both the raw ( D ) and viscosity-corrected ( D * ) di ff usion coe ffi cients ( a), expressed relative to the equivalent weight of a PEG polymer. After 2 h of irradiation, the apparent molecular weight calculated from the di ff usion coe ffi cient was 11000 ± 600 g mol -1 , which decreased to 8300 ± 500 g mol -1 using the viscosity corrected di ff usion coe ffi cient.

The standards used to create the calibration curve had a Đ &lt; 1.05, so the molecular weight calculated using these standards is only accurate for samples with a similar dispersity. We used GPC to measure Đ of 1.3 after the reaction, with M n of 8800 ± 200 g mol -1 and M w of 11500 ± 200 g mol -1 ( ). Despite the relatively high dispersity of the reaction samples, the di ff usion coe ffi cient provides a good estimate for the molecular weight and, importantly, allows the molecular weight evolution to be tracked during the polymerization.

The molecular weight-conversion plot in b shows a linear relationship, indicative of a living polymerization. The plot indicates the usefulness of the outlined di ff usion NMR

120

Figure 5. Molecular weight evolution during PET-RAFT polymerization. (a) Molecular weight calculated from time-resolved di ff usion coe ffi cient (raw D and viscosity-corrected D * ) using the calibration in . The horizontal lines correspond to the M n and M w from GPC on the same sample after 2 h of irradiation. (b) Molecular weight -conversion plot. The solid black line indicates the theoretical M n calculated by M n(theoretical) = ([MA]0/[BM1433]0) × (% C ) × (MWMA) + (MWBM1433), where [MA]0/[BM1433]0 = initial ratio of monomer to RAFT agent; % C = conversion = I polymer/( I monomer + I polymer ), I n = intensity of 1 H NMR signal for n ; MWMA and MWBM1433 = molecular weight of MA monomer and BM1433, respectively. Experimental parameters: 1 H, 500 MHz, PGSTE δ = 6 ms, Δ = 50 ms, g = 3 -50 G cm -1 , 298 K. Shaded areas indicate the standard deviation averaged over three experiments.

<!-- image -->

experiment, with both molecular weight and conversion data extracted from the same experiment.

To demonstrate the versatility of the proposed method, we have also studied the aqueous RAFT polymerization of acrylic acid, GPC analysis of which is challenging due to the charged systems created by the polyelectrolytes. With our method, the monomer conversion and molecular weight can also be estimated over time (see ).

It is not possible to use the di ff usion coe ffi cient to measure dispersity with our method, although this has been previously demonstrated with di ff usion NMR experiments. Using our di ff usion NMR parameters, the NMR signal for largest polymer formed is attenuated by ∼ 70% and the data are well-described by . To measure the dispersity, a deviation of the experimental data from the fi t of is required to model the distribution of di ff usion coe ffi cients. Such deviations are generally only detectible at very high attenuation. Our methodology might be adapted to achieve these high levels of attenuation for the polymer, while also monitoring the faster di ff using species, by using a spectrometer capable of applying a larger maximum gradient amplitude (note in this work g max = 51 G cm -1 ).

A single di ff usion NMR experiment can be used to monitor polymerization kinetics and molecular weight evolution with high time-resolution (14 s between data points). This versatile method does not require any specialist equipment and can be applied to fast reaction processes in any solvent where NMR

spectra can be collected, including those that are unsuitable for GPC analysis. By eliminating the need for sequential or parallel analysis of properties, data can be e ffi ciently collected to provide insights into highly time-sensitive polymerization reactions.

## * s ı Supporting Information

## ■ ASSOCIATED CONTENT

The Supporting Information is available free of charge at .

Synthetic procedures, NMR experimental data, spectra, and analysis ( )

## ■ AUTHOR INFORMATION

## Corresponding Authors

William S. Price -Nanoscale Group, School of Science, Western Sydney University, Penrith, NSW 2751, Australia; ; Email:

Jonathon E. Beves -School of Chemistry, UNSW Sydney, Sydney, NSW 2052, Australia; ; Email:

## Authors

Lucy L. Fillbrook -School of Chemistry, UNSW Sydney, Sydney, NSW 2052, Australia;

Mitchell D. Nothling -School of Chemistry, UNSW Sydney, Sydney, NSW 2052, Australia;

Martina H. Stenzel -School of Chemistry, UNSW Sydney, Sydney, NSW 2052, Australia;

Complete contact information is available at:

## Author Contributions

The manuscript was written through contributions of all authors.

## Funding

This work was supported by the Australian Research Council (FT170100094 to J.E.B.) and UNSW Australia (L.L.F.).

## Notes

The authors declare no competing fi nancial interest.

## ■ ACKNOWLEDGMENTS

We acknowledge the Mark Wainwright Analytical Centre at UNSW Sydney for access to the NMR facility.

## ■ REFERENCES

(1) Haven, J. J.; Junkers, T.

Eur. J. Org. Chem. 2017 , 2017 , 6474 -6482. (2) (a) Boussie, T. R.; Diamond, G. M.; Goh, C.; Hall, K. A.; LaPointe, A. M.; Leclerc, M.; Lund, C.; Murphy, V.; Shoemaker, J. A. W.; Tracht, U.; Turner, H.; Zhang, J.; Uno, T.; Rosen, R. K.; Stevens, J. C.

J. Am. Chem. Soc. 2003 , 125 , 4306 -4317. (b) Levere, M. E.; Willoughby, I.; O ' Donohue, S.; Wright, P. M.; Grice, A. J.; Fidge, C.; Remzi Becer, C.; Haddleton, D. M.

1753 -1763.

J. Polym. Sci. 2011 , 49 ,

(3) Stenzel, M. H.; Barner-Kowollik, C.

Mater. Horiz. 2016 , 3 , 471 -477. (4) (a) Haddleton, D. M.; Perrier, S.; Bon, S. A. F. Macromolecules 2000 , 33 , 8246 -8251. (b) Obermeier, B.; Wurm, F.; Frey, H. Macromolecules 2010 , 43 , 2244 -2251. (c) Knox, S. T.; Parkinson, S.; Stone, R.; Warren, N. J. Polym. Chem. 2019 , 10 , 4774 -4778. (d) Rubens, M.; Van Herck, J.; Junkers, T. Macro Lett. 2019 , 8 , 1437 -1441. (5) Izunobi, J. U.; Higginbotham, C. L. J. Chem. Educ. 2011 , 88 , 1098 -1104. (6) (a) Callaghan, P. Aust. J. Phys. 1984 , 37 , 359 -388. (b) von Meerwall, E. D. Spectroscopy: NMR, Fluorescence, FT-IR ; Springer: Berlin, Heidelberg, 1984; pp 1 -29. (c) Stilbs, P. Prog. Nucl. Magn. Reson. Spectrosc. 1987 , 19 , 1 -45. (d) Chen, A.; Wu, D.; Johnson, C. S. J. Am. Chem. Soc. 1995 , 117 , 7965 -7970. (e) Walderhaug, H.; Söderman, O.; Topgaard, D. Prog. Nucl. Magn. Reson. Spectrosc. 2010 , 56 , 406 -425. (f) Viéville, J.; Tanty, M.; Delsuc, M.-A. J. Magn. Reson. 2011 , 212 , 169 -173. (g) Hiller, W. Macromol. Chem. Phys. 2019 , 220 , 1900255. (7) (a) Ha ̊ kansson, B.; Nydén, M.; Söderman, O. Colloid Polym. Sci. 2000 , 278 , 399 -405. (b) Gong, X.; Hansen, E. W.; Chen, Q. Macromol. Chem. Phys. 2011 , 212 , 1007 -1015. (c) Röding, M.; Bernin, D.; Jonasson, J.; Särkkä, A.; Topgaard, D.; Rudemo, M.; Nydén, M. J. Magn. Reson. 2012 , 222 , 105 -111. (d) Röding, M.; Williamson, N. H.; Nydén, M. J. Magn. Reson. 2015 , 261 , 6 -10. (e) Urban ́ czyk, M.; Bernin, D.; Czuron ́ , A.; Kazimierczuk, K. Analyst 2016 , 141 , 1745 -1752. (f) Williamson, N. H.; Nydén, M.; Röding, M. J. Magn. Reson. 2016 , 267 , 54 -62. (g) Guo, X.; Laryea, E.; Wilhelm, M.; Luy, B.; Nirschl, H.; Guthausen, G. Macromol. Chem. Phys. 2017 , 218 , 1600440. (h) Williamson, N. H.; Röding, M.; Miklavcic, S. J.; Nydén, M. J. Colloid Interface Sci. 2017 , 493 , 393 -397. (8) (a) Cohen, Y.; Avram, L.; Frish, L. Angew. Chem., Int. Ed. 2005 , 44 , 520 -554. (b) Price, W. S. NMR Studies of Translational Motion: Principles and Applications ; Cambridge University Press: Cambridge, 2009. (9) Rudin, A.; Johnston, H. K.

J. Polym. Sci. B Poly. Lett. 1971 , 9 , 55 -60.

- (10) Flory, P. J. Principles of Polymer Chemistry ; Cornell University
2. Press: Ithaca, N.Y., 1953. (11) Raghavan, R.; Maver, T. L.; Blum, F. D. Macromolecules 1987 , 20 , 814 -818. (12) (a) Mazarin, M.; Viel, S.; Allard-Breton, B.; Thévand, A.; Charles, L. Anal. Chem. 2006 , 78 , 2758 -2764. (b) Barre ̀ re, C.; Mazarin, M.; Giordanengo, R.; Phan, T. N. T.; Thévand, A.; Viel, S.; Charles, L. Anal. Chem. 2009 , 81 , 8054 -8060. (c) Li, W.; Chung, H.; Daeffler, C.; Johnson, J. A.; Grubbs, R. H. Macromolecules 2012 , 45 , 9595 -9603. (d) Chamignon, C.; Duret, D.; Charreyre, M.-T.; Favier, A. Macromol. Chem. Phys. 2016 , 217 , 2286 -2293. (e) Cherifi, N.; Khoukh, A.; Benaboura, A.; Billon, L. Polym. Chem. 2016 , 7 , 5249 -5257. (f) Gu, K.; Onorato, J.; Xiao, S. S.; Luscombe, C. K.; Loo, Y.-L. Chem. Mater. 2018 , 30 , 570 -576. (g) ArrabalCampos, F. M.; Aguilera-Sáez, L. M.; Fernández, I. J. Phys. Chem. A 2019 , 123 , 943 -950. (h) Zhang, C.; Jin, Z.; Zeng, B.; Wang, W.; Palui, G.; Mattoussi, H. J. Phys. Chem. B 2020 , 124 , 4631 -4650. (i) Hou, J.; Pearce, E. Anal. Chem. 2021 , 93 , 7958 -7964. (j) Martínez, C. R.; Pérez, J. M.; Arrabal-Campos, F. M.; Batuecas, M.; Ortun ̃ o, M. A.; Fernández, I. Polym. Chem. 2021 , 12 , 4083 -4092. (13) (a) Stejskal, E. O.; Tanner, J. E. J. Chem. Phys. 1965 , 42 , 288 -292. (b) Gupta, A.; Stait-Gardner, T.; Price, W. S. Adsorption 2021 , 27 , 503 -533. (14) (a) Stilbs, P. Anal. Chem. 1981 , 53 , 2135 -2137. (b) Morris, K. F.; Johnson, C. S. J. Am. Chem. Soc. 1992 , 114 , 3139 -3141. (15) Vrijsen, J. H.; Thomlinson, I. A.; Levere, M. E.; Lyall, C. L.; Davidson, M. G.; Hintermair, U.; Junkers, T. Polym. Chem. 2020 , 11 , 3546 -3550. (16) (a) Price, W. S.; Tsuchiya, F.; Arata, Y. Biophys. J. 2001 , 80 , 1585 -1590. (b) Lewinski, P.; Sosnowski, S.; Kazmierski, S.; Penczek, S. Polym. Chem. 2015 , 6 , 4353 -4357. (17) (a) Oikonomou, M.; Asencio-Hernández, J.; Velders, A. H.; Delsuc, M.-A. J. Magn. Reson. 2015 , 258 , 12 -16. (b) MacDonald, T. S. C.; Price, W. S.; Beves, J. E.

ChemPhy-

- sChem 2019 , 20 , 926 -930. (c) Lee, A. M.; Stait-Gardner, T.; Price, W. S. J. Chem. Phys. 2021 , 155 , 144204. (18) MacDonald, T. S. C.; Feringa, B. L.; Price, W. S.; Wezenberg, S. J.; Beves, J. E. J. Am. Chem. Soc. 2020 , 142 , 20014 -20020. (19) Nothling, M. D.; Fu, Q.; Reyhani, A.; Allison-Logan, S.; Jung, K.; Zhu, J.; Kamigaito, M.; Boyer, C.; Qiao, G. G. Adv. Sci. 2020 , 7 , 2001656. (20) Wu, C.; Jung, K.; Ma, Y.; Liu, W.; Boyer, C. Nat. Commun. 2021 , 12 , 478. (21) (a) Dolinski, N. D.; Page, Z. A.; Eisenreich, F.; Niu, J.; Hecht, S.; Read de Alaniz, J.; Hawker, C. J. ChemPhotoChem. 2017 , 1 , 125 -131. (b) Niu, J.; Page, Z. A.; Dolinski, N. D.; Anastasaki, A.; Hsueh, A. T.; Soh, H. T.; Hawker, C. J. Macro Lett. 2017 , 6 , 1109 -1113. (22) Shanmugam, S.; Xu, J.; Boyer, C. J. Am. Chem. Soc. 2015 , 137 , 9174 -9185. (23) (a) Feldmeier, C.; Bartling, H.; Riedle, E.; Gschwind, R. M. J. Magn. Reson. 2013 , 232 , 39 -44. (b) Mallo, N.; Brown, P. T.; Iranmanesh, H.; MacDonald, T. S. C.; Teusner, M. J.; Harper, J. B.; Ball, G. E.; Beves, J. E. Chem. Commun. 2016 , 52 , 13576 -13579. (c) Seegerer, A.; Nitschke, P.; Gschwind, R. M. Angew. Chem., Int. Ed. 2018 , 57 , 7493 -7497. (d) Ji, Y.; DiRocco, D. A.; Kind, J.; Thiele, C. M.; Gschwind, R. M.; Reibarkh, M. ChemPhotoChem. 2019 , 3 , 984 -992. (e) Nitschke, P.; Lokesh, N.; Gschwind, R. M. Prog. Nucl. Magn. Reson. Spectrosc. 2019 , 114 -115 , 86 -134. (24) The equation is modi fi ed slightly for the pulsed- fi eld gradient stimulated echo (PGSTE) sequence that was used in this work. (25) (a) Price, W. S. Concepts Magn. Reson. 1998 , 10 , 197 -237. (b) Groves, P. Polym. Chem. 2017 , 8 , 6700 -6708. (26) As molecules get larger, T2 decreases much more than T1 (for very large molecules, T1 begins to increase while T2 continues to decrease). Thus, even though τ 1 ≪ τ 2, a lot of signal can be lost during τ 1 due to T2. (27) Strich, G.; Hagan, P. L.; Gerber, K. H.; Slutsky, R. A. Radiology 1985 , 154 , 723 -726. (28) (a) Price, W. S.; Ide, H.; Arata, Y. J. Chem. Phys. 2000 , 113 , 3686 -3689. (b) Swan, I.; Reid, M.; Howe, P. W. A.; Connell, M. A.; Nilsson, M.; Moore, M. A.; Morris, G. A. J. Magn. Reson. 2015 , 252 , 120 -129. (29) Dolinski, N. D.; Page, Z. A.; Discekici, E. H.; Meis, D.; Lee, I.H.; Jones, G. R.; Whitfield, R.; Pan, X.; McCarthy, B. G.; Shanmugam, S.; Kottisch, V.; Fors, B. P.; Boyer, C.; Miyake, G. M.; Matyjaszewski, K.; Haddleton, D. M.; Alaniz, J. R.; Anastasaki, A.; Hawker, C. J.

268 -273.

J. Polym. Sci. 2019 , 57 ,

(30) The system is crowded as the average spacing between molecules is much smaller than the mean-squared displacement from the Einstein equation for the time scale of the experiment. This means the apparent di ff usion coe ffi cients may appear smaller than the true di ff usion coe ffi cient due to obstruction. See reference for more details: Price, W. S.; Tsuchiya, F.; Arata, Y.

J. Am. Chem. Soc. 1999 , 121 , 11503 -11512. (31) (a) Arrabal-Campos, F. M.; On ̃ a-Burgos, P.; Fernández, I.

Polym. Chem. 2016 , 7 , 4326 -4329. (b) Zaccaria, F.; Zuccaccia, C.; Cipullo, R.; Macchioni, A.

Chem.-Eur. J. 2019 , 25 , 9930 -9937.

(32) Voorter, P.-J.; McKay, A.; Dai, J.; Paravagna, O.; Cameron, N. R.; Junkers, T.

Angew. Chem.,

(33) can be modi fi ed to account for higher

Int. Ed. 2021 , . concerntrations. See ref . (34) Braunecker, W. A.; Matyjaszewski, K.

Polym. Sci. 2007 , 32 , 93 -146.

(35) Perrier, S.

Macromolecules 2017 , 50 , 7433 -7447.

(36) (a) Lacík, I.; Beuermann, S.; Buback, M.

Macromolecules 2003 , 36 , 9355 -9363. (b) Lacík, I.; Stach, M.; Kasák, P.; Semak, V.; Uhelská, L.; Chovancová, A.; Reinhold, G.; Kilz, P.; Delaittre, G.; Charleux, B.; Chaduc, I.; D ' Agosto, F.; Lansalot, M.; Gaborieau, M.; Castignolles, P.; Gilbert, R. G.; Szablan, Z.; Barner-Kowollik, C.; Hesse, P.; Buback, M.

mol. Chem. Phys. 2015 , 216 , 23 -37.

Macro-

Prog.

<!-- image -->