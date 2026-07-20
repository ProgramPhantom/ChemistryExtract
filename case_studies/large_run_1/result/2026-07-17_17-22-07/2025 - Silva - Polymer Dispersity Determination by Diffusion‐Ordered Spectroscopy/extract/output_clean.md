## RESEARCH ARTICLE

## Polymer Dispersity Determination by Diffusion-Ordered Spectroscopy (DOSY)

Igor W. F. Silv Alasdair McKa

Tanja Junker

1 School of Chemistry, Polymer Reaction Design group, Monash University, Clayton, VIC, Australia 2 School of Chemistry, Monash University, Clayton, VIC, Australia

Correspondence : Tanja Junkers

Received: 2 April 2025 Revised: 13 June 2025

Funding : General funding from Monash University is acknowledged, specifically in form of a PhD scholarship to IWFS. The authors are further grateful for funding from the Australian Research Council in form of project DP240100120.

Keywords: Dispersity | Molecular weight | PDI | PFG-NMR | Standard deviation

## ABSTRACT

The dispersity ( Ð ) of a polymer is one of its most important characteristics. While the most established technique for dispersity determination is size exclusion chromatography (SEC), Diffusion-ordered NMR spectroscopy (DOSY) has emerged as a rival for routine polymer molar mass determination, even if dispersity remained somewhat elusive in DOSY to date. To expand DOSY to reliable dispersity measurement, we synthesize 26 polystyrenes with Ð ranging from 1.1 to 3.7 and number-average molar mass ( M n ) ranging from 3.0 to 22.4 kg ∙ mol -1 to correlate molar mass distribution (MMD) measurements of SEC to DOSY. We show that the method of inverse Laplace transformation (ILT) fails to represent the shape of the MMD of a polymer when it is not narrowly dispersed. Despite this failure, DOSY does yield the number and weight average molar mass with high accuracy, and thus the dispersity of samples is well accessible from DOSY-ILT. SEC and DOSY-ILT are well correlated up to Ð = 2.0. Interestingly, using the standard deviation ( σ ) and coefficient of variation of the MMD rather than dispersity yields an even better correlation across the entire dispersity and molar mass range covered in this study, underpinning the usefulness of using σ more regularly in polymer characterization.

## 1 Introduction

Afundamental aspect of synthetic polymers is that they typically feature molar mass distributions (MMDs) rather than discrete molar masses. Distributions are a consequence of the statistical nature of polymerizations, and also the majority of natural polymers are associated with MMDs. As a result from that, properties and applications of a polymer depend not only on the chemical makeup of these polymers, but also on the exact shape of the MMD, and its characteristic mean values. While each distribution is individual, MMDs are usually reduced to their moments for the sake of simplicity. From the moments of the distribution, the number average molar mass, M n , the

work is properly cited and is not used for commercial purposes.

©2025 The Author(s). Macromolecular Rapid Communications published by Wiley-VCH GmbH

weight average molar mass, M w, and their quotient, dispersity, Ð = M w / M n are commonly derived and used. While these averages give a generally good overview of polymers, these characteristic numbers are not fully sufficient to describe the full nature and shape of an MMD, yet are common descriptors in literature . Dispersity, as defined above, is an established, easy, and simple description to express the statistical nature of polymers and their associated broadness of distributions. A low dispersity is usually seen as a sign of the quality of a polymer, with respect to synthesis precision, even if a low dispersity is not necessarily superior in properties over polymers with a high dispersity. Regardless, researchers and practitioners alike are used to operate with the term dispersity and compare polymers based on this parameter.

License, which permits use, distribution and reproduction in any medium, provided the original However, as much as Ð is a useful quantity in this sense, it can also be highly misleading. Dispersity expresses the broadness of a distribution as a function of its overall molar mass, and hence two polymers with the same dispersity but different molar mass will feature a different broadness around their mean average. This feature of dispersity is often forgotten in practice. Harrisson discussed this downside of using dispersity for polymers in a noteworthy perspective, pointing to the non-intuitive nature of its values. He proposed to use standard deviation instead to characterize the broadness of a MMD more universally .

<!-- image -->

Many techniques were developed over time to determine either M w or M n (and hence Ð ), or the entire MMD. Some methods have historically been used to acquire number-average molar masses

, such as osmometry, boiling point elevation, and freezing point depression, while others only weight average molar masses, such as ultracentrifugation and light scattering . MMDs can be obtained by some methodologies, for example, field flow fractionation . However, the absolute gold standard in polymer MMD determination is size exclusion chromatography (SEC). SEC is a versatile, and accessible chromatography method that allows to directly measure a distribution, and hence in principle also its M w or M n . Yet, while the method itself is simple, it is often associated with very considerable accuracy issues stemming from complicated calibration issues, or the need to use very expensive mass-sensitive light scattering detectors. In SEC, not the mass of a polymer is in fact measured or separated for, but the hydrodynamic volume ( HV ) of a chain. The HV -mass correlation is, however, far from trivial and requires intricate knowledge on the polymer's intrinsic viscosity. More importantly, each SEC system must be carefully calibrated individually and requires constant maintenance to yield reliable results. Thus, while SEC is arguably the most widespread MMD determination instrument, there is a clear need for other determination methods that are less prone to calibration issues, and which yield more instrument-independent results. In the past, soft ionization mass spectrometry has been postulated to fill this gap due to its ability to measure molar masses accurately. Specifically, matrixassisted laser desorption ionization-time of flight spectrometry (MALDI-TOF)takes a prominent role in this respect, yet has until to date not found widespread use of MMD analysis due to cost, limitations in mass range and the requirement to find suitable matrices for each polymer in question. A more promising method in molar mass determination that emerged in recent years is pulse field gradient NMR (PFG-NMR), also referred to as diffusionordered spectroscopy (DOSY) . DOSY has been used for molar massdeterminations by specialists for decades but gained traction only recently by polymer chemists .

In DOSY, the molar mass of a species is traced via its diffusion coefficient in a fairly straightforward fashion. DOSY is available, at least in universities, to most researchers, and sample preparation is overall simple. Li et al. were amongst the first in synthetic polymer chemistry to apply DOSY for molarmassdeterminationinkinetic studies on controlled styrene polymerizations . In their work, they used average diffusion coefficients directly obtained from DOSY and calibrated those using narrow polymer standards (later referred to as standard DOSY experiment in this article). Arrabal-Campos et al. showed that molar mass determination of polystyrene via DOSY can be corrected in terms of viscosity, independent of the solvent

. Voorter et al. compared the performance of DOSY and SEC for polystyrene and poly(ethylene glycol) in several solvents, expandingtheconceptofauniversalDOSYcalibration , which was refined by the work of Hiller and Grabe, applying KuhnMark-Houwink-Sakurada parameters to enhance the power of the universal calibration via DOSY . Finally, Ruzicka et al. studied the influence of dispersed polymers on the calibration curve, not using only narrowly dispersed polymer distributions ( M w ≈ M n ) . Moreover, fundamental advances to molar mass determination have been made over the past years, such as concentration correction of the calibration curve , use of low-field NMR for DOSY measurements , online mass determination, and many others . However, with only a few notable exceptions, in all these studies only average molar masses were determined. To further complicate matters, with these averages, it isn't even fully clear if the mass determined corresponds to M w, M n , or an arbitrary intensity average that is not derived from the moments of the distribution.

Studies into the actual MMD from DOSY have nonetheless been undertaken. Johnson Jr. and collaborators determined MMDsusing general constrained regularization program applied in DOSY back in the 1990s . Wilhelm and coworkers elegantly described the treatment of DOSY data using log-normal

and gamma function modulations to obtain average molar masses and dispersity values. Yang and collaborators were able to show the indirect influence of Ð on PEG600 by applying a neural network for multi-variate DOSY methods . Further, several reports presented different approaches to contribute to measuring Ð via DOSY. Thus, the potential of DOSY for acquiring information from molar mass distribution is clear, even if dispersity determination is not as obvious as with SEC. Interestingly though, in practically all methods listed above, only relatively narrowly dispersed polymers were investigated, typically in the range of Ð &lt; 1.1. While such dispersities are often the target in contemporary polymer synthesis, most industrial polymers, and arguably also the majority of research-related polymers are of considerably higher dispersity. Polymers under investigation to date had also mostly been monomodal (or a mixture of monomodal narrowly dispersed polymers). It is hence an important question if DOSY is also able to represent MMDs of broadly dispersed polymers, a question we explore in this study.

In order to do so, we synthesized 26 polystyrene samples with a broad range of dispersity and molar mass to correlate results measured by SEC and DOSY. In the following, we first give a brief overview on the theory used to transform a distribution of diffusion coefficients to a molar mass-weighted distribution. Then, we compare the results on MMDs from DOSY and SEC based on the characteristic standard values, such as M w, M n , and Ð . Finally, we take a look at the standard deviation of polymers, as an alternative measure to dispersity.

## 2 Theory

In order to correlate the distributions acquired from SEC and DOSY, it is necessary to demonstrate how to derive the MMD from the respective DOSY experiment. In our work, we used the Inverse Laplace Transformation (ILT) method to determine the distributions and the mathematical procedure is given below

15213927, 2025, 23, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/marc.202500303 by University Of Maryland, Wiley Online Library on [04/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

. Before describing the equations, one must note that ILT is generally an ill-posed solution throughout a computational approach rather than an analytical one. The residual distribution is thus not the result of a direct measurement of its shape, but an approximation fitted to the data. Stejskal and Tanner expressed the (self-)diffusion coefficient, D , of a detected DOSY signal decay, via an exponential function that is given by:

$$\frac { I \left ( q \right ) } { I \left ( q = 0 \right ) } = \exp \left [ - D q ^ { 2 } \left ( \Delta - \delta / 3 \right ) \right ] & & \text {with} \\$$

where I ( q ) is the signal intensity and ∆ is the diffusion time. q is the product γgδ , where γ is the proton magnetogyric ratio, g is the gradient amplitude and δ is the gradient pulse duration. Note that Equation considers a rectangular shape of the gradient pulses; modifications might be required when dealing with different shapes of pulses, however, the equation displayed is the one used by the commercial Bruker software - Dynamic Center 2.8.3. Previous works presented deeper discussions around this topic . However, while this equation is immensely useful and used widely, it presumes monodisperity of the compound under investigation. When considering a dispersed polymer ( M w ≠ M n ), the peak intensities can be expressed with the following Fourier Transformation:

$$\frac { I \left ( q \right ) } { I \left ( q = 0 \right ) } = \int P \left ( D \right ) \exp \left [ - D q ^ { 2 } \left ( \Delta - \delta / 3 \right ) \right ] d D \quad \left ( 2 \right )$$

where P ( D ) is the probability of the diffusion coefficient . It is important to highlight that the molar mass might affect the T 1 and T 2 relation, which leads to assumptions and estimations of P ( D ). For detailed discussions, we direct the reader to specialized reports on this matter . To solve Equation and obtain P ( D ), Inverse Laplace Transformation (ILT) can be used, however, the solution does not have an analytical form

. Therefore, P ( D ) is not extracted from the data, it is approximated only as mentioned already above . Methods have been investigated in literature to estimate the distributions by computational solutions, such as the Tikhonov regularization method , Constrained regularization (CONTIN) , multivariate methods , or others. Most chemists will, however, use commercially available NMR software to process the ILT and the calculation of P ( D ) .

Analog to molar mass distribution handling , we can normalize the P ( D ) obtained from ILT, and correlate each D to its corresponding weight fraction of the polymer.

$$P _ { n o r m } \left ( D \right ) = \frac { P \left ( D \right ) } { \int P \left ( D \right ) d D } \quad \left ( 3 \right ) \quad 3$$

If the last statement is true, then:

$$P _ { n o r m } \left ( D \right ) = \frac { \mathrm d F \left ( D \right ) } { \mathrm d D } \quad \ \ ( 4 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

$$w \ ( M ) = - \frac { \mathrm d F \left ( D \right ) } { \mathrm d M } & & ( 5 ) & \stackrel { 2 2 . 2 } { \mathrm i s }$$

where F ( D ) is the cumulative weight fraction at D and w ( M ) is the molar mass-weighted distribution of the molar mass ( M ) of a given polymer. Combining Equations and , the following

$$w \ ( M ) = \left | \frac { d D } { d M } \right | \, P _ { n o r m } \left ( D \right ) \\ \intertext { s t o k e s - E i n s e i n } \text {Stokes-Einstein equation can be used to correlate D }$$

| | Finally, the Stokes-Einstein equation can be used to correlate D with the hydrodynamic radius ( r h ).

$$D = \frac { k _ { B } T } { 6 \pi \eta r _ { h } }$$

where k B is the Boltzmann constant, T is the temperature, and η is the solvent bulk solvent. Using the empirical Rouse-Zimm model, r h is then correlated to M :

$$r _ { h } \sim b M ^ { \nu }$$

where b and ν are arbitrary parameters depending on the type of the studied polymer system. For diluted systems (polymer concentration below the critical concentration ), Equations and can be combined to the empirical relation between D and M , transforming parameter b in the parameter K , which can be expressed as:

$$D = K M ^ { \nu }$$

Returning to Equation and combining it with the derivative of Equation , one can easily reach Equation , which represents the transformation of the P ( D ) distribution into a classical MMD, which can then be treated as usual to obtain the moments of distribution .

$$w \left ( M \right ) = \nu K M ^ { \nu - 1 } P _ { n o r m } \left ( D \right ) \quad \left ( 1 0 \right )$$

If one does not want to transform the P ( D ) versus D curve to a quick determination of Ð , previous reports showed that can also be done . We can easily apply these equations to any diffusion coefficient distribution acquired by DOSY NMR and estimated by ILT. Notice that the determination of M and consequently w ( M ) might differ depending on the equation one may use, i.e., solvent-correction molar mass determination

, structure and solvent-correction determination , temperature-correction , concentration-correction , or on specific acquisition parameters.

## 3 Results and Discussion

Polystyrenes with variations of dispersity were synthesized using an adaptation of the acid-regulated switchable RAFT agent method from Anastasaski and coworkers . By targeting different degrees of polymerizations, molar equivalents of acid, and reaction times, we achieved 26 different polystyrenes with Ð SEC ranging from 1.10 to 3.73 and an M n ranging from 3.0 to 22.4 kg mol -1 . Full characterization of all individual samples is available in Supporting Information. The 26 polymers were categorized into three groups related to their molar mass distributions: (i) controlled dispersity ( Ð &lt; 1.3), (ii) monomodal distributions with Ð &gt; 1.3 and (iii) bimodal distributions with Ð &gt;

1.3. It should be noted that while one would typically expect only monomodal distributions from the acid-regulated synthesis, yet in our case some distributions showed distinct shoulders. For the sake of this study, we considered this an advantage as it allowed us to study multimodality in more detail without needing to use blends of polymers. All polymers were subjected to full DOSY analysis, followed by an evaluation of distributions as described above using ILT. The ILT algorithm used in all analysis in this work was the commercially available Bruker software-Dynamic Center 2.8.3. Note that this version performs ILT based on the CONTIN algorithm. As aforementioned, Equations and can be modified depending on the shape of the gradient pulses used. Since SMSQ pulses were used for all DOSY analysis, the GNAT software was used to assess variances between the software used to determine D values. No significant differences for this study were found.

Before starting the discussion on the analysis of these samples, we must note that we used not only the ILT method to determine the MMDs from DOSY, but also the established method of using the average diffusion coefficient (standard DOSY experiment a typical overlay of spectra and an attenuation signal profile are showninFigure . Since this value is unlikely to represent M n or M w, we use the designation M DOSY in the following when referring to the molar mass obtained without MMD approximation. It should be noted that DOSY reports often refer to an average diffusion coefficient , and thus the term average molar mass, M avg, could be similarly used. We refrained from doing so to avoid any confusion with the true mass averages that are derived from the moments of the distributions. Figure presents the chromatograms acquired from SEC and distributions obtained by DOSY-ILT for one representative distribution from each of the three sample categories defined above. In Figure a narrowly dispersed polystyrene with Ð SEC = 1.22 and M w SEC = 3.9 kg ∙ mol -1 is compared between SEC and DOSY-ILT. For this polymer, the molar mass distributions derived from both methods are relatively similar regarding the monomodal profile, even though DOSY-ILT yields a slightly shifted distribution compared to SEC ( Ð ILT = 1.08; M w ILT = 2.8 kg ∙ mol -1 ). While not perfect, this approximation is satisfying and is well in line with previous reports on narrowly dispersed polymers analyzed by a similar method . Moreover, the classical DOSY analysis still performed robustly, yielding a M DOSY = 3700 g ∙ mol -1 , thus a value very close to the SEC M n . However, a quite different picture is obtained when the dispersity of the tested polymer is increased. Figure compares the obtained MMDs for a monomodal, yet more broadly dispersed polystyrene with Ð SEC = 1.66 and M w SEC = 31.2 kg ∙ mol -1 . Even though the SEC shows clearly a monomodal profile, the DOSY-ILT distribution results in a bimodal profile. This is a quite worrying observation, since SEC certainly is able to represent the shape of a MMD correctly. One hypothesis for the occurrence of such evaluation artifact is that by increasing the dispersity, ILT interprets the signal of the monomodal polymer as two distinguishable populations, therefore, splitting the MMD. Despite this artifact, the M DOSY (18.5 kg ∙ mol -1 ) that is determined is close to the SEC M n of the sample ( M n SEC = 18.8 kg ∙ mol -1 ). Figure then depicts the case for the third category of polymers, and hence an MMD for a high dispersity polystyrene that shows a clear shoulder ( Ð SEC = 2.02; M w SEC = 31.1 kg ∙ mol -1 ). Also here, the DOSY-ILT method splits the true distribution into two distinct distributions, however, interestingly not a position where one would expect from the occurrence of the shoulder in the SEC distributions. Again, though, M n SEC and M DOSY are matching relatively well. Yet, it can be directly concluded from Figure that the bimodal ILT distributions do not represent real subdistributions, but rather constitute a mathematical artifact. Clearly, these DOSY- ILT profiles are insufficient to describe the MMD of higher Ð polymers, and we consistently found that only if dispersity is low, monomodal ILT distributions are likewise obtained. For any sample with larger dispersity, irrespective of the fact that it features a shoulder or is seemingly monomodal, distribution artifacts are obtained in ILT.

FIGURE 1 Chromatograms from SEC (red) and DOSY-ILT (blue) of three different polystyrenes - the SEC results of each polymer are: a) Ð SEC = 1.22; M n SEC = 3.2 kg ∙ mol -1 ; b) Ð SEC = 1.66; M n SEC = 18.8 kg ∙ mol -1 ; and c) Ð SEC = 2.02; M n SEC = 15.4 kg ∙ mol -1 . Molar mass ( M DOSY ) was determined by conventional DOSY calibration without ILT (dashed line).

<!-- image -->

FIGURE 2 Diffusion coefficients determined via standard DOSY as a function of M w (a), M n (b), and M p (c) obtained from SEC for the various polystyrenes under investigation (polymer standards in black, category (i) in green, category (ii) in blue, and category (iii) samples in pink.

<!-- image -->

While the above examples show that ILT fails to represent the shape of the MMD of more complex polymer samples, the relatively good match in number average molar mass led us to further analyze the moments of the distributions obtained from ILT. Before doing this, we explored further the question in which way M DOSY correlates with the true averages of the samples (we assumed here that SEC gives as accurate values). Usually, to derive M DOSY , the average diffusion coefficient of a sample is calibrated on the MM of the used standards. Since standards are typically very narrowly dispersed, it makes practically here no difference if M n , M w or M p of the standards is used. Note that M p refers to the molar mass at the peak of the log M -weighted distribution, commonly used in SEC. Obviously, once one uses samples with broad MMDs, deviations can be expected. Thus, we constructed calibration curves for our dispersed samples for each MMD descriptor. Figure presents log D DOSY (determined from a standard DOSY evaluation) as a function of either M w, M n , and M p . The data is color-coded to represent the three different sample categories. Figure presents the correlation of DOSY results with M w SEC . Even though category ( i ), the low dispersity polymers ( Ð &lt; 1.3) showed a good correlation, the polymers with higher dispersity ( ii , iii ) deviated significantly from a linear relationship. This deviation from the calibration curve on high dispersity polymers was also recently reported by Benicewicz and collaborators, where they showed increasing errors of molar mass determination via DOSY when M w values of PMMA with Ð &gt; 1.3 were compared to a calibration curve of polymer standards

. Thus, it can be concluded that M DOSY (which is usually directly determined from log D ) does not generally correlate well. Figure presents the same data on M n SEC of the synthesized polystyrenes. Overall, M n correlates better throughout all samples, still a few outliers stand out. Notable outliners were the ones with the highest Ð SEC within group ( ii , Ð SEC 1.71 and 1.97). Even though M p SEC is generally frowned upon since it isn't derived from the moments of the distribution and hence not a true mass average, we nonetheless tested also for its correlation with log D , as shown in Figure as it may be thought that log D also represent an intensity peak maximum rather than a moment of the distribution. Interestingly, the correlation of M p is more comparable to M w, in that it shows very significant deviations for high dispersity polymers.

While Figure might indicate that DOSY-ILT generally yields erroneous results when the dispersity of a polymer is higher, or if distributions are not fully monomodal, average values obtained from the method might still be good representatives of the true averages of the MMDs. Figure thus directly compares the values of M w, M n , and Ð acquired by SEC and the DOSY-ILT method. Interestingly, much better correlations are found in this case, underpinning that M DOSY is not representative of distribution moments. M w and M n (Figure show a fair correlation between DOSY-ILT and SEC, with a slightly stronger correlation for M w measurements (r 2 of 0.96 vs. 0.93). This difference stems from a slightly weaker correlation of M n at higher masses. The dispersity values determined by both methods strongly correlate up to a dispersity of roughly 2.0, and show a good, but slightly reduced correlation at higher dispersity values. This is a remarkable result given the low correlation that the MMDs themselves yielded when ILT was compared to SEC. A direct conclusion can be that ILT fails to reproduce the shape of a distribution (due to its nature to mathematically approximate the distribution rather than measuring it), but at the same time produces results that contain information on the moments of the distribution accurately. This feature could proof to be very useful in future and paves the way to use DOSY-ILT for average molar mass and dispersity measurement as a direct alternative to SEC.

Whilethequality of correlations shown in Figure is overall good, an interesting result is that the slope of the best fit of the data is in all three plots at ≈ 0.9, meaning that ILT systematically yields values that are ≈ 10% below those obtained by SEC. This may represent a true mismatch in the methodologies, but otherwise could also simply result from the different measurement principles that are applied. ILT does not require separation of species in order to measure diffusion coefficients. SEC separates the hydro-

15213927, 2025, 23, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/marc.202500303 by University Of Maryland, Wiley Online Library on [04/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

<!-- image -->

w

n

FIGURE 3 Direct correlation of M w (a), M n (b), and Ð (c) determined from SEC and DOSY-ILT.

<!-- image -->

(σ/M)SEC

FIGURE 4 Comparison of σ (a) and σ / M n (b) obtained by SEC and DOSY-ILT analysis of polystyrene samples.

dynamic volume of the polymer chains through an inert column, which leads to band broadening . Band broadening can absolutely induce errors in measurement amounting to 10% . While it cannot be concluded from the data presented herein alone, it may well be possible that ILT yields the correct moments of the distribution, and that in fact SEC is overestimating the averages and the dispersity systematically.

As mentioned in the introduction, dispersity is a function of the average molar mass. Thus, we further analyzed the data in Figure with respect to their standard deviation, in order to test if the larger deviation we observed at Ð above 2 is significant or not. Harrisson had derived equations to directly correlate the standard deviation of a polymer distribution σ with dispersity in relation to M n .

$$D = 1 + \left ( \frac { \sigma } { M _ { n } } \right ) ^ { 2 } & & \text {dis} \\$$

This equation allows us to convert Ð into σ and hence to resolve it from its molar mass dependency. Figure compares σ and σ / M n of broad-range dispersities of polystyrenes acquired from SEC and DOSY-ILT methods. Figure powerfully demonstrates that the standard deviation of samples correlates better with each other than dispersity does. r2 of the fit increases from 0.93 in case of Figure to 0.97, and the correlation of data is evenly good in the entire dispersity regime. Interestingly, also the slope of the fit gets closer to unity, indicating that the standard deviation is measured almost equally well in ILT and SEC. Figure compares this result by correlating σ / M n , normalizing the standard deviation by the M n acquired by each method. Also, here a better correlation than the ones in Figure is found, yet the same trends become visible (note that Equation correlates the square of σ / M n with dispersity).

## 4 Conclusions

Overall, we demonstrated by applying inverse Laplace transformation to DOSY data on polymer samples, that it is possible to obtain detailed information on the moments of the polymer distribution. While the ILT method does not allow to determine the shape of the MMDs, at least not in a standard calculation as offered in commercial software (CONTIN as an ILT algorithm), when the MMDs feature a significant dispersity or otherwise non-monomodal behavior, it can be very useful to obtain average molar masses and dispersity values. This will have a specifically high value for the analysis of samples that are difficult to analyze in SEC due to solubility issues in standard SEC solvents since DOSY allows for much broader selection of solvents or even solvent mixtures. It also determines M n and M w independently from individual SEC calibrations, since DOSY calibrations are supposed to be much more universal. Further, we show that the standard DOSY method is most likely to yield M DOSY close to the true number average molar mass. Yet, specifically when polymers have a significant dispersity, ILT is required to obtain good estimations from DOSY. We hence recommend making ILT analysis with the following calculation of the moments of the distribution the standard methodology to treat polymer DOSY data. Also, we recommend to use the standard deviation of the mean molar mass σ rather than dispersity to describe the narrowness or broadness of a given distribution, since this parameter correlates much better between NMR and SEC. The high accuracy that we demonstrate here for the determination of average molar masses from DOSY-ILT will further strengthen the DOSY method in molar mass characterization, especially whenconsidering the significant advantages that DOSY generally presents compared to SEC (see solvent, temperature-

, concentrationcorrection, universal calibration , and many other superior features of DOSY). While SEC remains seemingly to be the gold standard for MMD shape determination, it may no longer be that for the determination of M n and M w alone.

## 5 Experimental Section

## 5.1 Materials

Styrene (Sigma-Aldrich, 99%); Polystyrene standards from PSS Laboratories ranging from 0.68 to 2520 kg ∙ mol -1 ; 2-cyanobutan-2yl methyl(piridin-4-yl)carbamodithioate (Boron Molecular, 90%); recrystallized (in cold methanol) azobisisobutyronitrile (AIBN); dimethylformamide (RCI Labscan, 99%); sulfuric acid (RCI Labscan, 98%); methanol (Univar, 99.9%); deuterated chloroform with silver foil (Cambridge Isotope Laboratories, Inc., 99.8%D).

## 5.2 Size Exclusion Chromatography (SEC)

Molar mass distributions were analyzed using SEC. PSS SECcurity2 GPC systems operated by PSS WinGPC software, equipped with an autosampler, an SDV 5.0 µ mguard column (50 × 8 mm), followed by three SDV analytical 5.0 µ m columns with varying porosity (1000, 100 000, and 1 000 000 Å) (50 × 8 mm) coupled to a differential refractive index (RI) detector and viscosity detector using tetrahydrofuran (THF) as the eluent at 40 ◦ Cwithaflowrate of 1 mL ∙ min -1 . Toluene was used as the flow marker. The system wascalibrated using direct polystyrene calibration (K = 14.1 × 10 -5 dL ∙ g -1 and α = 0.70). The distributions were analyzed using the PSS software and Python routines.

## 5.3 Diffusion Ordered Spectroscopy NMR (DOSY)

The experiments were run in Bruker Neo nanobay NMR spectrometer with a 5 mm broadband BB-H/D probe operating at 400.14 MHz for 1 H with ≈ 50 G ∙ cm -1 z-gradient and a BCUII cooling unit. Samples were made up at 1.0 mL at 2.0 mg ∙ mL -1 and placed in 5 mm NMR tubes. Measurements were conducted at 298

K. Samples were kept stationary throughout the measurements. The double-stimulated-echo (dstegp3s) pulse program was used

with a smoothed square-shaped (SMSQ) pulse . Experiments were performed as pseudo-2D with a linear ramping of the gradient from 2% to 98% of maximum intensity in 128 different gradients and 32768 spectral points. The spectral region from 1 to 8 ppm was analyzed. For each step, 8 transients were acquired following 8 dummy transients. The diffusion time, ∆ (d20), was 400 ms, the spoiled gradient (p19) was set to 600 µ s, the recycle delay (d1) was 3 s and the eddy current delay (d21) was 5 ms. The d1 was tested beyond the default, and it did not present any measurable effect, hence, the study proceeded with the chosen parameters for optimal use of available instrument time. The repetition time was assessed to be higher than 5 × T 1 . Thegradient pulse length, δ (p30), was optimized on a per-sample basis, see Supporting Information. The main peak chosen to standardize the analysis throughout the samples was the most intense one of the polymers - aromatic region, at ≈ 7 ppm. The data were processed using the commercially available software Topspin 4.1.4 and for the diffusion coefficient determination, D through the Stejskal-Tanner expression, Equation , using Dynamics Center 2.8.3. The latter was also used to perform the ILT using the default settings of the software: logarithmic grid, second derivative regularization with 0.001 as the regularization parameter, finding alpha automatically, 128 grid points, and applying kernel compression . Comparatively, the opensource software GNAT was also used to acquire robust data and validation of methods. The results were processed and analyzed by Python routines.

## 5.4 Polystyrene Synthesis

In glass vials, styrene (350, 400, and 500 eq.; 1.3735, 1.5697, and 1.9624 g, respectively) was added to the RAFT agent 2cyanobutan-2-yl methyl(piridin-4-yl)carbamodithioate (1.0 eq., 100 mg). AIBN (0.1 eq.) was added to 0.1 mL solution of 6 mg ∙ mL -1 in DMF. The final volume on the vials was 1.2 mL. Based on the method of Anastasaki and coworkers , 18 m sulfuric acid (0, 0.05, 0.20, 0.50, 0.80, 1.10, 1.40, and 4.00 eq.; 0 to 8.4 µ L) was added to achieve different values of Ð . The samples were degassed for 20 min. The reactions were carried out in an oil bath at 65 ◦ C for 72 or 120 h. After the reaction, the polymers were stopped by opening the vials to air and the solutions were left to dry in aluminum pans at room temperature. The dried polymers were redissolved in a minimum of THF, precipitated in cold methanol, and then filtered (centrifugation was used when necessary). The purification was repeated twice or until no monomer trace could be identified in both SEC and 1 HNMR.

## Acknowledgements

General funding from Monash University is acknowledged, specifically in form of a PhD scholarship to I.W.F.S. The authors are further grateful for funding from the Australian Research Council in form of project DP240100120.

Open access publishing facilitated by Monash University, as part of the Wiley Monash University agreement via the Council of Australian University Librarians.

The authors declare no conflicts of interest.

## Data Availability Statement

The data that support the findings of this study are openly available in Polymer Dispersity Determination by Diffusion-Ordered Spectroscopy (DOSY) at reference number 1.

## References

1. D. T. Gentekos and B. P. Fors, 'Molecular Weight Distribution Shape as a Versatile Approach to Tailoring Block Copolymer Phase Behavior,' ACS Macro Letters 7 (2018): 677-682.
2. S. Harrisson, 'The Downside of Dispersity: Why the Standard Deviation Is a Better Measure of Dispersion in Precision Polymerization,' Polymer Chemistry 9 (2018): 1366-1370.
3. W. H. Carothers, 'Polymerization,' Chemical Reviews 8 (1931): 353-426.
4. T. Svedberg, ASourceBookinChemistry,1900-1950 (Harvard University Press, 2013): 35-42.
5. H. W. McCormick, 'Molecular Weight Distribution of Polystyrene by Sedimentation Velocity Analysis,' Journal of Polymer Science 36 (1959): 341-349.
6. B. H. Zimm, 'Apparatus and Methods for Measurement and Interpretation of the Angular Variation of Light Scattering; Preliminary Results on Polystyrene Solutions,' The Journal of Chemical Physics 16 (1948): 1099-1116.
7. R. Beckett, Z. Jue, and J. C. Giddings, 'Determination of Molecular Weight Distributions of Fulvic and Humic Acids Using Flow Field-Flow Fractionation,' Environmental Science &amp; Technology 21 (1987): 289-295.
8. K. F. Morris, and C. S. Johnson Jr, 'Diffusion-Ordered TwoDimensional Nuclear Magnetic Resonance Spectroscopy,' Journal of the American Chemical Society 114 (1992): 3139-3141.
9. W. Li, H. Chung, C. Daeffler, J. A. Johnson, and R. H. Grubbs, 'Application of 1 H DOSY for Facile Measurement of Polymer Molecular Weights,' Macromolecules 45 (2012): 9595-9603.
10. F. M. Arrabal-Campos, P. Oña-Burgos, and I. Fernández, 'Molecular Weight Prediction with no Dependence on Solvent Viscosity. A Quantitative Pulse Field Gradient Diffusion NMR Approach,' Polymer Chemistry 7 (2016): 4326-4329.
11. P. Voorter, A. McKay, J. Dai, O. Paravagna, N. R. Cameron, and T. Junkers, 'Solvent-Independent Molecular Weight Determination of Polymers Based on a Truly Universal Calibration,' Angewandte Chemie 134 (2022): 202114536.
12. W. Hiller and B. Grabe, 'The Universal Calibration for Structureand Solvent-Independent Molar Mass Determinations of Polymers Using Diffusion-Ordered Spectroscopy,' Analytical Chemistry 95 (2023): 1817418179.
13. W. Hiller, B. Grabe, and J. Schonert, 'Molar Mass Determination for Small and Large Molecules Using Diffusion-Ordered Spectroscopy,' Analytical Chemistry 96 (2024): 14902-14908.
14. E. Ruzicka, P. Pellechia, and B. C. Benicewicz, 'Polymer Molecular Weights via DOSY NMR,' Analytical Chemistry 95 (2023): 7849-7854.
15. X. Guo, E. Laryea, M. Wilhelm, B. Luy, H. Nirschl, and G. Guthausen, 'Diffusion in Polymer Solutions: Molecular Weight Distribution by PFGNMR and Relation to SEC', Macromolecular Chemistry &amp; Physics 218 (2017): 1600440.
16. F. M. Arrabal-Campos, M. González-Lázaro, J. M. Pérez, J. A. Martínez Lao, and I. Fernández, 'Concentration-Independent Molecular Weight Determination of Polymers via Diffusion NMR: a Universal Approach across Solvents,' European Polymer Journal 226 (2025): 113710.
17. O. Tooley, W. Pointer, R. Radmall, et al., 'MaDDOSY (Mass Determination Diffusion Ordered Spectroscopy) Using an 80 MHz Bench

Top NMR for the Rapid Determination of Polymer and Macromolecular Molecular Weight,' Macromolecular Rapid Communications 45 (2024): 2300692.

18. O. Tooley, W. Pointer, R. Radmall, et al., 'Real-Time Determination of Molecular Weight: Use of MaDDOSY (Mass Determination Diffusion Ordered Spectroscopy) to Monitor the Progress of Polymerization Reactions,' ACS Polym. Au 4 (2024): 311-319.
19. J. Tratz, M. Gaborieau, M. Matz, M. Pollard, and M. Wilhelm, 'Potential of Benchtop NMR for the Determination of Polymer Molar Masses, Molar Mass Distributions, and Chemical Composition Profiles by Means of Diffusion-Ordered Spectroscopy, DOSY,' Macromolecular Rapid Communications 45 (2024): 2400512.
20. W. Hiller, 'Quantitative Studies of Block Copolymers and Their Containing Homopolymer Components by Diffusion Ordered Spectroscopy,' Macromolecular Chemistry and Physics 220 (2019): 1900255.
21. B. Grabe and W. Hiller, 'Molar Mass Distribution and Chemical Composition Distribution of PS- b -PMMA Block Copolymers Determined by Diffusion Ordered Spectroscopy,' Macromolecules 55 (2022): 8014-8020.
22. K. Watanabe, H. Matsushita, K. Takamatsu, and K. Ute, '1H DOSY Analysis of High Molecular Weight Acrylamide-based Copolymer Electrolytes Using an Inverse-Geometry Diffusion Probe,' Polymer Journal 55 (2023): 591-598.
23. T. F. Nelson and C. P. Ward, 'Diffusion-Ordered Spectroscopy for Rapid and Facile Determination of Consumer Plastic Molecular Weight,' Analytical Chemistry 95 (2023): 8560-8568.
24. P.-J. Voorter, M. Wagner, C. Rosenauer, et al., 'A Fast and Efficient Way of Obtaining the Average Molecular Weight of Block Copolymers via DOSY,' Polymer Chemistry 14 (2023): 5140-5146.
25. B. D. Monnery, V. V. Jerca, R. Hoogenboom, and T. Swift, 'Polymer Conformation Determination by NMR Spectroscopy: Comparative Diffusion Ordered 1 H-NMR Spectroscopy of Poly(2-ethyl-2-oxazoline)s and Poly(ethylene glycol) in D 2 O,' Polymer Chemistry 15 (2024): 3077-3085.
26. A. Agarwal, B. G. Bobay, and M. L. Becker, 'Observation of Dynamic Aggregation Behavior in Thermoresponsive Micro- and Nanoparticles via Diffusion-Ordered NMR Spectroscopy,' Journal of the American Chemical Society 147 (2025): 9386-9395.
27. T. Swift, E. Dyson, N. Koniuch, R. Telford, and S. Rimmer, 'Overcoming 'Diffusion Limits'-Principles Required to Measure High Molar Mass Polymers by Diffusion Ordered NMR,' Analytica Chimica Acta 1352 (2025): 343937.
28. K. F. Morris, and C. S. Johnson Jr, 'Resolution of Discrete and Continuous Molecular Size Distributions by Means of Diffusion-Ordered 2D NMR Spectroscopy,' Journal of the American Chemical Society 115 (1993): 4291-4299.
29. K. F. Morris, C. S. Johnson, and T. C. Wong, 'Polymer-Induced NonNewtonian to Newtonian Transition in the Viscoelastic CTAB/Sodium Salicylate/Water System as Studied by Diffusion-ordered 2D NMR,' The Journal of Physical Chemistry 98 (1994): 603-608.
30. A. Chen, D. Wu, and C. S. Johnson, 'Determination of Molecular Weight Distributions for Polymers by Diffusion-Ordered NMR,' Journal of the American Chemical Society 117 (1995): 7965-7970.
31. E. Lin, N. Zou, Y. Huang, Z. Chen, and Y. Yang, 'Neural Network Method for Diffusion-Ordered NMR Spectroscopy,' Analytical Chemistry 94 (2022): 2699-2705.
32. J. Viéville, M. Tanty, and M.-A. Delsuc, 'Polydispersity Index of Polymers Revealed by DOSY NMR,' Journal of Magnetic Resonance 212 (2011): 169-173.
33. E. O. Stejskal and J. E. Tanner, 'Spin Diffusion Measurements: Spin Echoes in the Presence of a Time-Dependent Field Gradient,' TheJournal of Chemical Physics 42 (1965): 288-292.
34. D. Sinnaeve, 'The Stejskal-Tanner Equation Generalized for any Gradient Shape-An Overview of Most Pulse Sequences Measuring Free Diffusion,' Concepts in Magnetic Resonance Part A 40A (2012): 39-65.

35. P. Groves, 'Diffusion Ordered Spectroscopy (DOSY) as Applied to Polymers,' Polymer Chemistry 8 (2017): 6700-6708.
36. I. J. Day, 'On the Inversion of Diffusion NMR Data: Tikhonov Regularization and Optimal Choice of the Regularization Parameter,' Journal of Magnetic Resonance 211 (2011): 178-185.
37. S. W. Provencher, 'A Constrained Regularization Method for Inverting Data Represented by Linear Algebraic or Integral Equations,' Computer Physics Communications 27 (1982): 213-227.
38. E. Lin, Y. Yang, Y. Huang, and Z. Chen, 'High-Resolution Reconstruction for Diffusion-Ordered NMR Spectroscopy,' Analytical Chemistry 92 (2020): 634-639.
39. M. Gavrilov and M. J. Monteiro, 'Derivation of the Molecular Weight Distributions from Size Exclusion Chromatography,' European Polymer Journal 65 (2015): 191-196.
40. I. W. F. Silva, A. McKay, A. Sokolova, and T. Junkers, 'Towards the Universal Use of DOSY as a Molar Mass Characterization Tool: Temperature Dependence Investigations and a Software Tool to Process Diffusion Coefficients,' Polymer Chemistry 15 (2024): 1303-1309.
41. M.-N. Antonopoulou, R. Whitfield, N. P. Truong, et al., 'Concurrent Control over Sequence and Dispersity in Multiblock Copolymers,' Nature Chemistry 14 (2022): 304-312.
42. L. Castañar, G. D. Poggetto, A. A. Colbourne, G. A. Morris, and M. Nilsson, 'The GNAT: a New Tool for Processing NMR Data,' Magnetic Resonance in Chemistry 56 (2018): 546-558.
43. A. M. Striegel, W. W. Yau, J. J. Kirkland, and D. D. Bly, 'Band Broadening,' in Modern Size-Exclusion Liquid Chromatography (John Wiley &amp; Sons, Ltd, 2009): 49-91.
44. P. Zhang, P. Mazoyer and R. G. Gilbert, 'A Broad-standard Technique for Correcting for Band Broadening in Size-exclusion Chromatography,' Journal of Chromatography A 1443 (2016): 267-271.
45. L. A. Clementi, M. M. Yossen, and J. R. Vega, 'Molar Mass Distributions of Linear Homopolymers by Size Exclusion Chromatography with Light Scattering Detection: a Method for Automatic Band Broadening Correction,' Journal of Chromatography A 1595 (2019): 136-143.
46. D. Held and P. Kilz, 'Size-Exclusion Chromatography as a Useful Tool for the Assessment of Polymer Quality and Determination of Macromolecular Properties,' Chemistry Teacher International 3 (2021): 77-103.
47. D. Held and W. Radke, 'Tips &amp; Tricks GPC/SEC: Separation Range and Resolution,' The Column 17 (2021): 26-30.
48. J. L. Baumgarten, J.-P. Busnel, and G. R. Meira, 'Band Broadening in Size Exclusion Chromatography of Polymers. State of the Art and Some Novel Solutions.' Journal of Liquid Chromatography &amp; Related Technologies 25 (2002): 1967-2001.
49. W. Burchard, Branched Polymers II (Springer, 1999): 113-194.
50. S. J. Gibbs and C. S. Johnson, 'A PFG NMR Experiment for Accurate Diffusion and Flow Studies in the Presence of Eddy Currents,' Journal of Magnetic Resonance 1991 (1969): 395-402.
51. M. Nilsson, 'The DOSY Toolbox: a New Tool for Processing PFG NMR Diffusion Data,' Journal of Magnetic Resonance 200 (2009): 296-302.

## Supporting Information

Additional supporting information can be found online in the Supporting Information section.

SupportingFile1: marc202500303-sup-0001-SuppMat.pdf.