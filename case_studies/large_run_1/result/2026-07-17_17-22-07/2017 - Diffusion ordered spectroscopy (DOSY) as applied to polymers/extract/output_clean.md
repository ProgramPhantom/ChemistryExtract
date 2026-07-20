<!-- image -->

## REVIEW

<!-- image -->

Cite this: Polym. Chem. , 2017, 8 , 6700

Received 13th September 2017, Accepted 25th October 2017

DOI: 10.1039/c7py01577a

<!-- image -->

<!-- image -->

## Di ff usion ordered spectroscopy (DOSY) as applied to polymers

Patrick Groves

Di ff usion ordered spectroscopy (DOSY) is a well established NMR method that reports di ff usion coe ffi cients for individual resonances in NMR spectra. DOSY is primarily used to analyse mixtures of small molecules and the oligomeric state of biomolecules. DOSY has also been used to analyse polymers and investigate micellization properties but di ff erent acquisition and processing parameters are recommended for polymers. In particular, the molecular weight dispersion of polymers and micelles are at odds with the physical limits of DOSY. Con fi dence in the quality of published DOSY data is lowered when critical parameters are poorly optimized or not reported. This tutorial provides a ' top ten ' of DOSY parameters, an explanation of their source and importance, as well as suggested starting parameters and optimization for polymer/micelle samples. By following these guidelines, DOSY can emerge from being an occasional method to con fi rm data obtained from other experimental techniques, to one that provides strong physical evidence in its own right as the originators of DOSY intended.

Di ff usion Ordered Spectroscopy (DOSY) reports di ff usion coe ffi cients for individual resonances in a 1 H NMR spectrum. 1,2 As the di ff usion coe ffi cient is related to the hydrodynamic radius of a molecule, DOSY is complementary to other physical methods used in polymer analyses to measure molecular size/shape. DOSY has been used to measure the average size of a polymer. 3 -5 In the case of measuring poly(ethylene terephthalate) and poly(ethylene furanoate) molecular weights, DOSY is competitive on cost with gel filtration characterization because of the cost of large volumes of hexafluoro-2-propanol and solvent-compatible, chromatography accessories. 6 Copolymers can be readily assessed by DOSY -copolymer signals with di ff erent di ff usion coe ffi cients signify the presence of monomer impurities or a mixture of homopolymers. 7,8 DOSY can also be used as a method to follow the rate of a polymerization reaction. 9,10 Regarding self-aggregation, DOSY has been used to investigate the assembly of reversible polymers, 11 as well as to measure critical micelle concentrations and micelle size. 12 These examples illustrate the wide range of applications of DOSY in the polymer field. However, caution is required when using DOSY because distinct acquisition and processing parameters are needed for each application and the literature is dominated by non-polymer applications.

Department of Biomedicinal Chemistry, University of Gdansk, ul. Wita Stwosza 63, 80-308 Gdansk, Poland. E-mail: p.groves@ug.edu.pl; Tel: +48 58523 5034

|

Several parameters need to be optimized for DOSY experiments in order to obtain valid, consistent and comparable results. These parameters will be explained and described later but the list includes (i) pulse sequence/type of DOSY experiment, (ii) solvent (mixture), which is related to viscosity, (iii) gradient range (in G cm -1 ), (iv) the di ff usion delay, Δ , (v) the di ff usion gradient pulse length, δ , (vi) the number of gradient steps in the F1 dimension and type of gradient spacing that is employed, (vii) the fitting routine used for di ff usion dimension (and software), (viii) number of points used for the display of di ff usion coe ffi cients in the F1 dimension of the 2D plot, (ix) dynamic range of the displayed di ff usion coe ffi cients, (x) estimated errors from multiple samples/experiments. A scan of papers published in some of the top polymer journals that have used DOSY, giving DOSY data in tables and figures, shows that the majority provide, at best, details of the solvent. This tutorial attempts to improve the acquisition, processing, analysis, validation and reporting of DOSY for polymer samples by defining each of these ten terms and suggesting suitable parameters for common cases. Further comments on the use of DOSY to investigate intermolecular interactions and micelle formation will also be given. The majority of DOSY studies used Bruker spectrometers and Bruker software for the acquisition and processing of DOSY data. For this reason, specific names and terms as used on Bruker instruments are given in addition to their generic terms that are applicable to all NMR spectrometers and processing software packages. But first, we will start with a physical overview of the DOSY experiment in order to put the ten parameters mentioned above into context.

## Principals of the DOSY experiment

A pair of gradient pulses is at the heart of the DOSY experiment, whatever additional features are added to aid solvent suppression or compensate for convection. Fig. 1 and 2 describe the action and behaviour of gradient pulses with respect to di ff usion measurements.

Fig. 1 illustrates the most basic DOSY pulse sequence based on a spin-echo. 1,13 The pair of gradient pulses encode and decode the di ff usion information. The first, encoding gradient pulse creates a corkscrew pattern of the magnetization arrows from the previously aligned magnetization, as shown in Fig. 2, while the second, decoding gradient pulse returns and realigns the magnetization to where it started. However, the molecules di ff use during time Δ leading to a mixing of the magnetization so that only part of the magnetization is finally decoded, Fig. 2. DOSY protocols vary the gradient strengths rather than Δ in order to create a series of spectra where the signals decay as a function of the applied gradient power. 14 This approach is chosen as a number of physical mechanisms, like T 1 and/or T 2 relaxation, are in operation during time Δ that would a ff ect DOSY data collected with di ff erent values of Δ . The strength of the corkscrew e ff ect (Fig. 2) depends on the power put into the gradient (a function of gradient shape and % maximum gradient power), as well as gradient pulse length ( δ or δ /2 -see later). Longer and more powerful gradients create tighter corkscrew e ff ects with a greater chance that signals will be lost through di ff usion in time Δ .

The faster the molecules di ff use, the more mixing occurs during the di ff usion time Δ , and less magnetization will be recovered by the second gradient, Fig. 2. The loss of magneti- zation/signal strength is related to the di ff usion coe ffi cient of the molecule. Molecular di ff usion occurring during the di ff usion time Δ helps to di ff erentiate between small and large molecules that have distinct di ff usion coe ffi cients.

Fig. 1 A pictorial description of the simplest DOSY pulse sequence ( pulsed fi eld gradient spin-echo). 1 The fi rst 1 H pulse aligns the magnetization in the x -direction, as illustrated later in Fig. 2A. The fi rst gradient pulse creates the corkscrew e ff ect shown in Fig. 2B -D -the di ff erent gradient powers in Fig. 1 and 2 are matched by color. The second 1 H pulse inverts the magnetization vector in the x -y plane. The second gradient pulse undoes the corkscrew e ff ect of the fi rst gradient pulse. The data is then acquired. The gradient pulses are colour labelled (red = 2%, green = 50%, blue = 95% of the maximum power of the gradient generator).

<!-- image -->

Fig. 2 A standard, 90° x pulse aligns the magnetization in the x -direction of the x -y plane (black arrows). The 1st gradient pulse (encode) twists this magnetization along in the x -y plane and along the z -axis into a corkscrew shape. The degree of the corkscrew e ff ect depends on the strength of the gradient pulse (2%, red; 50%, green; 95%, blue). Samples di ff use vertically during the (translational) di ff usion time (big delta, Δ ) between the two gradient pulses (purple) -the degree of mixing will be greater for higher gradient strengths. As a result, only part of the magnetization (smaller arrows/circles) are recovered by the 2nd, decoding pulse (colour coding matches the gradient strengths of the 1st gradient pulse). This means that higher gradients (green, blue) result in smaller circles/magnetization/detected signals.

<!-- image -->

Fig. 2 explains the basis of how NMR magnetization can be converted into a variable intensity signal that can be quantified for di ff usion. But the accuracy of measuring di ff usion coe ffi cients from a single NMR experiment is low. In practical terms, a series of 1D 1 H NMR experiments are acquired with a 2D DOSY pulse sequence in which the gradient strength of the coding and decoding pulses is increased in tandem. This results in the acquisition of a series of 1D 1 H NMR experiments in which the twist shown in Fig. 2 becomes tighter for consecutive experiments. The result is that the degree of magnetization loss becomes greater during the series of experiments as illustrated in Fig. 3.

How can the corkscrew e ff ect described here measure di ff usion coe ffi cients? The answer lies partly in Fig. 2. The degree of mixing during time Δ depends on how fast the molecules are mixing (or di ff using) in the tube. Small molecules that di ff use quickly will be rapidly mixed and the recovered magnetization will diminish, as a function of gradient strength, more quickly than for larger molecules that di ff use more slowly. A series of experiments can be run with di ff erent gradient powers (the gradient pulse lengths ( δ or δ /2) and delay Δ are normally kept constant during the experiment). This leads to a series of 1D 1 H NMR experiments that can be stacked to reveal decay curves at each frequency of the spectra. The signal intensity of selected resonances in small molecules will decay, as a function of applied gradient strength, faster than large molecules, Fig. 3.

Fig. 3 Increased sampling in the di ff usion dimension provides increased dynamic range. Theoretical di ff usion decays are shown for molecules weighing 10 (circles), 10 3 (triangles) and 10 5 (squares) Da. (A). The 10 -10 5 Da range is adequately sampled with 64 di ff usion experiments with linear gradient spacing (open symbols) but reduced to a smaller range for16 di ff usion experiments (10 3 -10 5 Da, closed symbols). (B) The same traces are plotted with 32 experiments and logarithmic spacing of the gradient range. I is the intensity and I 0 the initial intensity of the selected resonance; g is the applied gradient strength; δ = 4 ms and Δ = 400 ms for the simulation. The red (2%), green (50%) and blue (95%) dots at the top of fi gure represent the gradient strengths applied in Fig. 1 and 2 while the orange dot represents a 25% gradient as discussed in the text. Data modelled using the viscosity of H2O (298 K) as the solvent.

<!-- image -->

A plot of intensity versus gradient strength is given in Fig. 3. The theoretical di ff usion decay curves are clearly distinct for the di ff erent sized molecules and the di ff usion coe ffi cient can be extracted by curve fitting according to eqn (1). 15 It now becomes clear that the values chosen for the di ff usion time ( Δ ), gradient pulse lengths (little delta, δ ), gradient pulse strengths ( g ) and number of acquired 1D 1 H NMR experiments are amongst the most critical acquisition parameters for the acquisition of reliable DOSY data, Fig. 3, and it ' s analysis by eqn (1). In ideal cases, the slowest di ff using molecule should lose &gt;95% of its signal by the end of the experiment (at the highest di ff usion pulse strength).

Molecular shape is an important consideration in interpreting DOSY data as di ff usion coe ffi cients are related to the hydrodynamic radius of a spherical molecule as defined by the Stokes -Einstein equation, eqn (2). We should note that the coded magnetization is not lost by molecular di ff usion in the x -y plane -only in the z -direction. Strictly speaking, DOSY measures translational di ff usion coe ffi cients. The di ff usion coe ffi cients obtained by DOSY can di ff er to di ff usion coe ffi cients measured by other methods for elongated molecules that align with strong magnetic fields. This is an issue, for example, with long strands of duplex DNA but it is unlikely to be a large issue for most polymer samples.

$$I / I _ { 0 } = e ^ { ( - D g ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g ^ { 2 } \Delta ^ { \prime } ) }$$

where D is the translational di ff usion coe ffi cient; g is the gyromagnetic ratios of the studied nuclei; δ is the PFG duration and σ is the gradient shape factor. 15 The di ff usion delay Δ ′ is a corrected value of Δ by an amount that depends on the specific pulse sequence and gradient shape. 15

$$D = k _ { B } T / 6 \pi \eta r _ { H } & & ( 2 )$$

where D is the di ff usion coe ffi cient (m 2 s -1 ); k B is the Boltzman ' s constant; η is the viscosity of the solution, r H is the hydrodynamic radius of the solute.

Now that we have a background to the DOSY experiment, we can explore some of the acquisition and processing parameters that are required to optimize the experimental acquisition, processing and analysis.

## Pulse sequence and basic di ff usion parameters

Fig. 1 illustrates the most basic DOSY pulse sequence but the probability is that you will choose and use a pulse sequence that incorporates additional pulses and improvements. While additional pulses are designed to take care of specific problems and errors, the rule of thumb in NMR pulse design is that more pulses equals lower sensitivity. Therefore, there is a signal : noise/time advantage to avoid very long pulse sequences if their benefits are not required for your samples.

The DOSY pulse sequence shown in Fig. 1 (pulse field gradient spin-echo, PGSE) 1 su ff ers from a number of drawbacks. T 2 relaxation of the sample during Δ significantly lowers the signal intensity and long relaxation delays (between scans) are recommended, which means long experiments. Additionally, eddy currents associated with the gradient pulses produce resonance and baseline distortions. The splitting of the 180° pulse into two separate 90° pulses creates the stimulated echo (STE) building block that is found at the core of many 2D DOSY sequences as it neutralizes both of the mentioned problems. 1

The magnitude of the eddy currents partly depend on the quality of the probe and how well it is shielded. If several probes/NMR instruments are available for your work, it might be the case that the most sensitive 1 H probe, or highest field instrument, is not necessarily the best choice for DOSY -a fact that I can attest to. Probe choice for DOSY is a matter of consultation with your local NMR technician/supervisor/expert.

Experiments incorporating the Longitudinal Eddy current Delay (LED) compensate for eddy currents. 16 However, optimized values for the LED on the order of 100 ms can result in significant signal attenuation. The LED values can be drastically shortened (about 5 ms, or omitted) if bipolar gradients are used as they e ffi ciently compensate for eddy currents. Spoil gradients are also added to provide further artefact suppression.

The BRUKER dstebpgp3s pulse sequence incorporates a double STE segment with three spoil gradients. 17 This sequence is intrinsically much less sensitive than other DOSY pulse sequences but it is optimal with dealing with convection currents in NMR tubes. Convection currents occur in low viscosity, low boiling point solvents like CDCl3. Several additional tricks have been suggested by the NMR community if convection is an issue. A change from the standard 5 mm NMR tube to a 3 mm tube or Shigemi tube changes the sample volume and dimensions to inhibit convection in the tube. Short experiments can be run at ambient temperature without temperature control in order to remove pulsing from the temperature control unit that can induce convection. Conducting the experiments at low temperature, say 283 K, may help as the solvent viscosity should be higher and convection slowed.

For samples in D2O, or other solvents with significant residual solvent peaks, a pulse sequence incorporating solvent suppression should be considered. In general, the high viscosity of H2O, D2O and DMSO samples means that convection compensation is not required at room temperature but should be considered at higher temperatures. For Bruker users, the stebpgp1s19 sequence (without convection compensation) is the only available 2D DOSY pulse sequence in the standard pulse sequence library that incorporates solvent suppression (WATERGATE). DOSY pulse sequences incorporating di ff erent solvent suppression techniques have been described in the literature. 18

With respect to the quality of the DOSY data, the most important aspect is whether bipolar gradients are used for the di ff usion encoding/decoding pulses. Bipolar gradients are set to a time of δ /2 (rather than δ for simple pulses, Fig. 1). On Bruker instruments, the di ff usion gradient is usually defined by the pulse variable, p30. Reporting the value of p30 is not the same as reporting the value of δ unless details of the DOSY pulse sequence are given. This may seem a trivial point but the halving/doubling of δ has a 4-fold e ff ect on eqn (1) and this consequently has a significant impact on the di ff usion dynamic range (see later).

## Gradient range

DOSY experiments are not collected over the full range of the NMR gradient generator because the gradient power delivered at low and high powers are often inaccurate, regardless of calibration procedures. 14 Besides errors in gradient calibration, there are systematic errors that are di ffi cult to correct. Personally, I have collected protein calibration curves (see later, Fig. 4) and calculated the estimated MW of an unknown three times over a 4 month period on a multi-user instrument that experienced weekly probe changes without observing any significant changes in the calculated molecular weight values of my unknown. In my opinion, the use of references and standards are a better way to gauge your samples than relying on continual checking and recalibration of the gradients. However, it is still important to determine the linear range of your gradient generator, for example as described in the BRUKER DOSY manual. 14

Default ranges of 2 -95% of maximal gradient strength are suggested for DOSY experiments, corresponding to the linear range of most gradient synthesizers. What is the e ff ect of changing these values? With respect to Fig. 3, we would observe the complete decay of signal intensity for small molecules in the 10 -1000 Da range with a 2 -25% gradient range. But note that the signals for the large molecules (10 5 Da) decay by only about 10% in this gradient power range. This small decay is almost linear and the processing software may interpret this as a baseline artefact rather than a true NMR signal. Therefore, a choice of 2 -25% gradient range may selectively filter out data from larger molecules. With respect to Fig. 3, what would we observe after choosing a 25 -95% gradient range? This is equivalent to collecting the gradient decay curves from the orange dot above Fig. 3. We would not observe an e ff ect from small molecules because their intensity would have decayed to zero before the first DOSY data point is collected at 25% gradient strength. The di ff usion properties of small molecules would be filtered out and we would only observe molecules in the 10 3 -10 5 Da range with such an experiment. The choice of gradient range has a large impact on polymer samples. In the examples explained above, it is possible to artificially filter out larger or smaller molecules from the DOSY analysis, thus biasing the final result. This is an important point for polymer samples as they have particular molecular weight distributions. DOSY is intrinsically unreliable to provide information on the molecular weight distribution of a sample as it is unwise to collect data over a 0 -100% gradient range and so the di ff usion data will always have some bias over large ranges. Polymer samples with broad molecular weight distributions will give very di ff erent average di ff usion coe ffi cients when the gradient range (and other acquisition parameters) are changed when compared to a sample with a tight molecular weight distribution.

Fig. 4 Plot of log D (total summed di ff usion) versus log MW for a set of ten dextran GPC standards in D2O (kindly donated by Pharmacos, Denmark). The data were collected on a Bruker Avance III 500 MHz with TXI probe and 53.5 G cm -1 maximum gradient generator using the stebpgp1s19 pulse sequence. The least-squared linear fi t gives the equation log D = -0.470 log MW -8.141 with r 2 = 0.998. The number of gradient experiments was 64 over a 2 -98% gradient range (0.68 -33.38 G cm -1 ) with a linear spacing, Δ = 600 ms, δ = 6 ms, F1 di ff usion resolution = 1024 points over 3.0 log units. All other parameters were used at default settings. NMR data were analysed as single exponentials with Topspin 3.1 software. Errors in di ff usion coe ffi cient are smaller than the size of the symbols.

<!-- image -->

The optimal parameters for the gradient range and Δ / δ values are that the smallest molecule should maintain a strong, almost 100% intensity at the lowest sampled gradient strength while the largest (most slowly di ff using) sample should experience a signal decay of &gt;95% by the final gradient strength. These constraints should be maintained across the whole series of DOSY samples, which is roughly 2 -95% of the maximum gradient strength in Fig. 3.

An important note about gradient strength is that the delivered gradient power is modulated by gradient shape. The sinusoidal gradient shape (SINE.100) recommended in DOSY pulse programs in older software from BRUKER lowered the maximum delivered gradient power by ∼ 28%. The latest BRUKER pulse programs suggest the trapezoidal, SMSQ10.100 pulse shape, which lowers the maximum gradient power by only 10%. As higher gradient powers means shorter values of δ and Δ are required, it is better to use SMSQ10.100 pulse shapes if they do not lead to distortions in your spectra. Pure, square gradient shapes, which allow the maximum gradient power to be used, are not recommended as they do not attenuate eddy currents.

## Aqueous samples

Aqueous samples, whether in H2O (or D2O) solutions, should be run with the stebpgp1s19 pulse sequence. However, WATERGATE needs careful optimization for each sample to avoid distortions to the peaks and baseline close to the residual water resonance. These distortions can be attenuated with processing parameters (sfil/qfil parameters for BC\_mod on Bruker helps to further remove unwanted signals from the center of the spectrum -from water but also molecule resonances close to water) but the baseline artefacts can still have an impact on the proper fitting of the di ff usion decay curves. As discussed, a gradient range of 25 -95%, starting from the orange dot in Fig. 3, is suitable for H2O samples in a 5 mm tube. The signals from small molecules, including solvent and monomer units, will be filtered out. This makes H2O an unsuitable solvent for the DOSY analysis of polymer samples where residual monomer species may be present. The baseline distortions can also be reduced by using smaller sample volumes, e.g. I have found that 3 mm tubes can safely be run over a wider, 15 -95% gradient range.

## Acquisition parameters: di ff usion delays

NMR relaxation mechanisms that are active during the di ff usion time ( Δ ) can generate reproducible but inconsistent results in DOSY when acquisition parameters (gradient range, number of gradient experiments, Δ and δ values) are changed. For this reason, it is recommended to use constant values of Δ and δ for experiments. Many reports use variable Δ and/or δ values, while others do not report either value. Optimal values of Δ and δ depend on sample viscosity and the maximum gradient strength of the instrument. Optimization should be carried out for the lowest and highest molecular weight samples to be analyzed. While older guides to DOSY suggest the optimization of δ and Δ for each sample, it is better for polymer samples to choose fixed values to be applied to all samples. This makes it easier to compare datasets obtained on di ff erent samples and days. Fig. 3 and the selection of the number of di ff usion experiments is a better way of controlling the dynamic range that can be sampled than manual parameter optimization of every sample.

On Bruker instruments, 1D pulse sequences are available for some of the 2D DOSY experiments. The advantage of 1D pulse sequences is that two separate experiments can be run with set gradient power values at minimum (2%) and maximum (95%) gradient strength. The processed data can be overlaid in order to judge if other parameters ( Δ and δ ) will provide a &gt;95% signal loss during a 2D DOSY experiment. These two 1D experiments require much less time to acquire than a full 2D DOSY experiment. Starting values may range for Δ = 50 ms and δ = 1 ms for CDCl3 to Δ = 400 ms and δ = 4 ms for DMSO/D2O. Changing δ has a greater e ff ect on the di ff usion result than a similar sized change in Δ (eqn (1)).

The F2 ( 1 H acquired) dimension of a DOSY spectrum has a number of requirements. One critical point is related to the future processing of the data, which includes automatic baseline correction. Baseline correction routines are e ffi cient but it is still worth helping the program by choosing spectral widths larger than the minimum. It is not necessary to collect a long FID with, say, 64k data. The size of the final, processed 2D file will quickly use the available disk space. A more modest FID size of 4 -8k is su ffi cient. The historical use of T 1/ T 2 fitting routines in Bruker software may suggest similar parameter set ups for DOSY as for relaxation measurements but this is not the case.

## Fitting the di ff usion data

A large part of the DOSY literature is dedicated to small molecules, their spectral resolution and multiple component fitting in order to obtain ' pure ' spectra of di ff erent molecules in a mixture that might have overlapping resonances, e.g. ref. 19. In the case of polymers, di ff erent length oligomers have almost identical spectra. Longer polymers might have broader peaks than shorter oligomers and a polymer mixture with a wide molecular weight distribution will produce smiley peaks in 2D DOSY spectra (if the di ff usion coe ffi cients are plotted at good resolution -see later) as the centre of the resonance is biased towards the sharp resonances of the low molecular weight components and the edges of the resonance are biased towards the high molecular weight components. This smiling feature again makes it di ffi cult to estimate di ff usion coe ffi cients directly from 2D spectra and emphasizes the value of the f1sum command, which will be introduced later.

Multiple component fitting requires the components to be di ff erent in mass by at least a factor of two. In other words, the ratio of monomer and dimer species might be estimated using such fitting but the continuum of molecular weights in polymer samples is generally unsuitable for multiple component fitting. Nonetheless, software exists for estimating molecular weight distributions from DOSY data, as well as alternative (to exponential) single component fitting of di ff usion decay curves (see ref. 20 for a summary of fitting methods).

## Acquisition parameters: how many di ff usion experiments?

Accurate di ff usion coe ffi cients can be fitted to eqn (1) from 6 -8 valid di ff usion experiments. The molecular weight dynamic range is limited (from 10 3 -10 5 Da) when a total of only 16 di ff usion experiments are collected with a linear gradient spacing, filled symbols in Fig. 3A: the di ff usion decay for very small molecules (10 Da) is defined by only two, filled, significant datapoints in the 0.9 -0.1 range of I / I 0 (Fig. 3). Accuracy is compromised for fast di ff using compounds and the use of a low molecular weight compound as an internal di ff usion coe ffi cient reference should be used with caution in these circumstances. The acquisition of 32 -64 di ff usion experiments, rather than 16, is recommended to properly sample wide molecular weight ranges (&gt;10 3 dynamic range). This is apparent from the density of the datapoints in Fig. 3A. One problem with collecting 64 experiments, rather than 16, is the 4-fold increase in the experiment time. While this might be undesirable, it is better to collect a complete set of valid data than data compromised with di ff erent acquisition parameters.

A linear spacing of gradient strengths is the default setting on Bruker NMR instruments, leading to Fig. 3A. The ' exponential ' option (on Bruker Topspin software) concentrates more DOSY measurements at lower gradient strengths, leading to Fig. 3B, which was simulated with 32 gradient points. The change in gradient spacing improves the molecular weight dynamic range of the experiment. With optimized values of δ and Δ , 32 exponential steps should allow the analysis of polymers over a 10 4 dynamic range. To analyze a wider dynamic range, longer values of δ and Δ are required and possibly a larger number of gradient steps. While many NMR parameters are selected as a factor of 2 for historical reasons, the number of gradient steps can be set to any integer.

## Processing parameters

The di ff usion coe ffi cients of samples are obtained indirectly by fitting decay curves extracted from a series of 1D 1 H NMR experiments, Fig. 3 and 4. Di ff erent di ff usion fitting routines are available within the Bruker software but the default ' exponential ' fitting records the initial intensity of the di ff usion decay and a calculated di ff usion coe ffi cient with an error. 14 These numbers are visualized as a Gaussian curve centred on the di ff usion coe ffi cient; the volume of the peak is proportional to the initial signal intensity and the peak width represents the calculated error. The number of points representing the Gaussian, di ff usion peak is a matter of display, not experimental, resolution. The appropriate parameter (SI1) that defines the di ff usion resolution is very rarely given. However, it is clear from figures of 2D DOSY spectra that a SI1 value equal to the number of di ff usion experiments has been used in many cases.

The e ff ect of SI1 on the digital resolution of the di ff usion dimension is shown in Fig. 5. The 2D DOSY plot of Fig. 5A was processed with a typical resolution of 32 in the di ff usion dimension and the same data processed with a resolution of 1024 in Fig. 5B. The blocky peaks of Fig. 5A are typical for a DOSY spectrum processed with a low resolution in the di ff usion dimension. The result suggests that the sample consists of one component and it is easier to estimate an average log D value from Fig. 5A than Fig. 5B. However, this is an optical illusion. Fig. 5C and D are obtained with the ' f1sum '

Fig. 5 The e ff ect of variable processing parameters on DOSY. The same DOSY data processed and displayed with (A) 32 and (B) 1024 datapoints in the F1 di ff usion dimension. Panels C and D show the summed di ff usion traces (f1sum) from panels A and B, respectively. The sample is a mixture of two dextran standards dissolved in D2O. Other acquisition and processing parameters are as described in Fig. 4.

<!-- image -->

macro in Bruker Topspin software as applied to Fig. 5A and B, respectively (chose ' calculate sum ' not ' calculate positive projection ' as an option). The summed 1D di ff usion trace of Fig. 5D provides the easiest and most precise estimation of the average di ff usion coe ffi cient weighted for the relative intensity of the whole sample in the di ff usion dimension. The 2D DOSY data tend to look ' worse ' than they really are. The precision and accuracy of the experimental log D results depend on the resolution of the processed data in the di ff usion dimension, as well as the method of estimating log D . Good quality f1sum traces can be obtained for samples in the low micromolar concentration range.

It is worth mentioning the e ff ect of the Bruker DOSY processing parameter LWF (line width factor). LWF = 1 is default and, in my opinion, this leads to 2D DOSY spectra that are very broad in the di ff usion dimension, giving the impression that the di ff usion coe ffi cients are poorly determined. The use of LWF = 0.1 during processing improves the visual representation of 2D DOSY plots and generally makes the di ff usion dimension more representative with respect to the calculated errors in the di ff usion coe ffi cient.

Fig. 5 contrasts di ff erent processing and analytical approaches. It is easier to estimate an average log D from the 2D spectrum if the di ff usion dimension has low resolution. It should be noted that f1sum can be carried out on a spectral range ( e.g. 3 -4 ppm) although summing of the whole spectrum does not usually result in lower signal : noise as columns of data that cannot be fitted are usually zero filled in the processed 2D DOSY matrix rather than containing noise as in standard 2D NMR spectra. The resolution in Fig. 5D better serves the polymer chemist than that in Fig. 5C where the peak maximum is shifted by ∼ 0.1 log D units (in context, a di ff erence of ∼ 0.2 log D units would be expected for polymer samples with a 2-fold di ff erence in length/size). This simple approach to improve signal : noise ratio and the calculation of di ff usion coe ffi cients (Fig. 3D) has consequences on the practical sensitivity of DOSY. An error of less than 0.01 log D units can be readily achieved for a 1 mM or 1 mg ml -1 (whichever is lower) sample in a 5 mm NMR tube, using 8 -16 scans and a NMR probe with a relatively low 1 H sensitivity of ∼ 400 : 1. 21 This translates into a 10 -20 minutes experiment for a sample that is far less concentrated, and viscous, than NMR samples typically used for polymer analyses. These general numbers are from experience on several di ff erent 500 -800 MHz instruments in several di ff erent NMR labs. Estimated errors in di ff usion coe ffi cients are rarely reported. However, a lack of resolution in the di ff usion dimension e ff ectively introduces an artificial error in the DOSY dimension that can mask a 1.5-fold length/size di ff erence between polymer samples.

## Validation of DOSY data through calibration curves

Polymer chemists would not consider publishing gel permeation chromatography (GPC) data that had not been vali- dated with a calibration curve of molecular weight standards. This is not the case with published DOSY data. Calibration curves, using GPC standards, 22 -24 Fig. 4, provide confidence in the sample preparation, NMR operator and the acquisition and processing parameters. The generation of such a calibration curve is worthwhile for anyone performing DOSY for the first time and the calibration curve can later provide a proper estimate of the average molecular weight of a polymer with an error. If appropriate parameters are chosen and consistently used, calibration curves can retain validity over several months.

## Molecular interactions, dimerization and shape changes

GPC is useful for detecting changes in molecular size, shape and the formation of strong/covalent interactions. DOSY can detect all these changes, as well as the formation of weak interactions. The slopes of DOSY calibration curves define log D changes due to dimerization (or doubling in size) at around -0.14 (compact molecules, 3D proteins, dendrimers, micelles) to -0.20 (linear polymers). 22,23,25,26 Neither a shift in log D of &lt; -0.1, nor &gt; -0.2, corresponds to a simple dimerization event. In the former case, the sample might contain a significant degree of monomer species. In the latter case, higher order oligomers are implicated. Conclusions on the oligomeric state of samples should be supported with concentration-dependent titrations and molecular weight calibrations (together with analysis by other techniques).

## Critical micelle concentration (CMC) calculations

Self aggregation of a detergent can be analyzed by DOSY to obtain CMCs and an estimate of micelle size. Some block copolymers have self-aggregating properties that can be studied by DOSY. 11,27,28 CMC estimates can be made from a plot of experimental di ff usion coe ffi cient plotted against detergent concentration. More accurate CMCs, and the estimate of micelle size, require the acquisition of data over at least 20 concentrations in order to define a full aggregation curve that can be analyzed by eqn (3), where the observed self-di ff usion coe ffi cient is a population-weighted average of the ' free ' (monomeric) and ' bound ' (micellized) surfactant. 12 For small micelles (up to 10 monomers per micelle), the di ff usion properties of the monomer and micelle are close enough that no significant errors are transferred from the calculated DOSY parameters. However, the di ff usion coe ffi cient for a large micelle (&gt;50 monomer units) are distinct from that of the monomer. In such a case, we have multiple problems of correctly sampling the two overlapping species in order to obtain a precise, average di ff usion coe ffi cient. Fitting errors for the aggregation curve can be explained away as a concentrationdependent micelle size. For this reason, the data in Fig. 6 is

-10.6

Fig. 6 Calculated di ff usion coe ffi cients from a model ' detergent ' titration to measure CMC and micelle size. The titration was carried out by titrating a 1 kDa dextran sample into the NMR tube (as a monomeric detergent) before adding a 20 kDa dextran above 1 mM to simulate a fi xed sized micelle. The single set of high resolution DOSY data was processed using four di ff erent sets of processing parameters and plotted. The four curves are the results of processing the di ff usion datapoints in the 1 -32 (squares), 17 -48 (triangles), 33 -64 (circles) and 1 -64 (diamonds) ranges. The pulse sequence, instrumentation, acquisition and processing parameters are as described in Fig. 4. The discrepancies in the curves are discussed in the text.

<!-- image -->

obtained by titrating a large polymer standard, acting as the micelle, into a short polymer standard, acting as a monomer. Even though the experimental data were collected in an appropriate way, manipulation of the processing parameters alone leads to di ff erent aggregation curves that will be better or worse fitted by the two-site exchange model described by eqn (3). 12

$$D = D _ { f } + ( ( 1 - C _ { f } / C _ { t } ) ( D _ { b } - D _ { f } ) H ( C _ { t } - C _ { f } ) ) \quad ( 3 ) \quad \stackrel { ( 3 ) } { \ e a c h s c r { o u n } }$$

where D f and D b are self-di ff usion coe ffi cients of free and micellized surfactant, respectively; C t , C f and C b are the concentrations of total, free and micellized surfactant, respectively; H is the Heaviside step function:

$$H ( C ) = 0 \text { if } C _ { t } < \text { cmc} ; \ H ( C ) = 1 \text { if } C _ { t } \geq \text { cmc} .$$

Only one of the curves in Fig. 6, at most, can be fitted accurately by eqn (3). While the DOSY data was correctly acquired for a mixture of small and large molecules, it was processed in di ff erent ways to e ff ectively introduce systematic errors during sampling/processing. As already discussed with respect to Fig. 3, data processed over the early part of the di ff usion decay is biased towards the smaller molecule and the contribution from the larger molecule is filtered out (squares, Fig. 6). The opposite bias towards the larger molecule is apparent when the second half of the DOSY data is processed and plotted (circles, Fig. 6). While these errors are purposely exaggerated, they do illustrate that small changes in acquisition/processing parameters can have a large impact on the calculated di ff usion coe ffi cients, especially when resonances result from molecules with varied di ff usion properties, and even more so for estimates of the micelle size.

12

## Summary of parameter optimization

## Pulse sequence/type of DOSY experiment

Solvent suppression for aqueous samples (stebpgp1s19). Convection compensation for CDCl3 and similar low viscosity solvents, as well as cold/cryo probes (dstebpgp3s). The ledbpgp2s pulse sequence is suitable where convection currents are not expected ( e.g. DMSO).

## Solvent

The main question about solvent is matching its ' properties to the correct DOSY pulse sequence and viscosity to suitable values of δ and Δ , see below.

## Gradient range

The maximum gradient power is typically 50 -60 G cm -1 for standard gradient synthesizers. The gradient range is usually quoted as a % range but gradient pulse shapes can significantly lower the delivered gradient power so it is better to report the actual gradient power range that was delivered during the experiment. On Bruker instruments, this range can be found in the text file ' di ffl ist ' that is associated with the experiment.

## Di ff usion delay, Δ

For small molecules in CDCl3 = 50 ms but 200 -600 ms for larger molecules in more viscous solvents. Try to use a fixed value for each set of experiments.

## Di ff usion gradient pulse length, δ

For small molecules in CDCl3 = 1 ms but 2 -6 ms for larger molecules in more viscous solvents. Try to use a fixed value for each set of experiments.

## Number of gradient steps

32 steps with exponential spacing covers a wide dynamic range in the di ff usion dimension. The study of high molecular weight polymers above 100 kDa may warrant more steps whereas for the regular study of polymers below 10 kDa, 16 -24 steps are su ffi cient.

## Di ff usion fitting routine

The default BRUKER spectrometer software setting of leastsquares, exponential fitting is generally adequate if the suggestions are followed regarding ' zero filling ' in the di ff usion dimension and summing of columns to obtain di ff usion profiles. Bi-exponential fitting etc . should be considered an advanced method and carried out with caution and experience according to the original literature.

## Di ff usion ' zero filling '

The number of points used for display of di ff usion coe ffi cients in the F1 dimension of 2D plot should provide a resolution of at least 0.01 log units. Therefore, the display of DOSY data over 2 di ff usion log units requires at least 200 points. Personally, I fill to 1k points for 2 -3 di ff usion log units.

## Dynamic range of displayed di ff usion coe ffi cients

Display the di ff usion dimension over a suitable dynamic range as a wider than necessary range adversely a ff ects the resolution. Usually, a suitable range is 2 -3 log units (10 2 -10 3 m 2 s -1 ).

## Estimated errors from multiple samples/experiments

Generally, a value of ±0.01 log units is easily achieved but this should be checked with at least one duplicate sample and 2 -3 runs of the same experiment on exemplary samples. Estimated errors cannot be smaller than the resolution in the di ff usion dimension.

## Conclusions

The main criticism of papers published in polymer journals with DOSY data is the lack of reported experimental parameters to validate the reported data. Where parameters are reported, some are more suitable for small molecule analysis than polymer samples. Individual, GPC molecular weight standards are ideal tools to calibrate and validate DOSY data. DOSY is typically used by the polymer chemist as a method to illustrate trends or confirm other data with a minimum of datapoints. However, the use of optimal parameter sets produces better, more valid DOSY data and should also push DOSY from an illustrative method into a more useful, first-line analytical technique in its own right.

## Con fl icts of interest

There are no conflicts of interest to declare.

## Acknowledgements

Funding acknowledgement: grant no. 530-8725-D496-17 (Ministry of Science and Higher Education in Poland).

## Notes and references

- 1 J. E. Tanner, J. Chem. Phys. , 1970, 52 , 2523 -2526.
- 2 B. Nyström, M. E. Moseley, P. Stilbs and J. Roots, Polymer , 1981, 22 , 218 -220.
- 3 L. Abbassi, Y. M. Chabre, N. Kottari, A. A. Arnold, S. André, J. Josserand, H.-J. Gabius and R. Roy, Polym. Chem. , 2015, 6 , 7666 -7683.
- 4 P. Lewinski, S. Sosnowski, S. Kazmierski and S. Penczek, Polym. Chem. , 2015, 6 , 4353 -4357.
- 5 S. Viel, D. Capitani, L. Mannina and A. Segre, Biomacromolecules , 2003, 4 , 1843 -1847.
- 6 J. G. Rosenboom, J. De Roo, G. Storti and M. Morbidelli, Macromol. Chem. Phys. , 2017, 218 , 1 -10.
- 7 S. Viel, M. Mazarin, R. Giordanengo, T. N. T. Phan, L. Charles, S. Caldarelli and D. Bertin, Anal. Chim. Acta , 2009, 654 , 45 -48.
- 8 F. Coumes, C. Y. Huang, C. H. Huang, J. Coudane, D. Domurado, S. Li, V. Darcos and M. H. Huang, Biomacromolecules , 2015, 16 , 3666 -3673.
- 9 N. Cherifi, A. Khoukh, A. Benaboura and L. Billon, Polym. Chem. , 2016, 7 , 5249 -5257.
- 10 W. Li, H. Chung, C. Dae ffl er, J. A. Johnson and R. H. Grubbs, Macromolecules , 2012, 45 , 9595 -9603.
- 11 J. M. Zayed, F. Biedermann, U. Rauwald and O. A. Scherman, Polym. Chem. , 2010, 1 , 1434.
- 12 O. Soderman, P. Stilbs and W. S. Price, Concepts Magn. Reson., Part A , 2004, 23 , 121 -135.
- 13 E. O. Stejskal and J. E. Tanner, J. Chem. Phys. , 1965, 42 , 288 -292.
- 14 R. Kerssebaum and G. Salnikov, Topspin Man., 2.0.0 , 1 -32.
- 15 D. Sinnaeve, Concepts Magn. Reson., Part A , 2012, 40 , 39 -65.
- 16 S. J. Gibbs and C. S. Johnson Jr., J. Magn. Reson. , 1991, 93 , 395 -402.
- 17 N. M. Alexej Jerschow, J. Magn. Reson. , 1997, 375 , 372 -375.
- 18 S. Balayssac, M. A. Delsuc, V. Gilard, Y. Prigent and M. Malet-Martino, J. Magn. Reson. , 2009, 196 , 78 -83.
- 19 M. Foroozandeh, L. Castanar, L. G. Martins, D. Sinnaeve, G. D. Poggetto, C. F. Tormena, R. W. Adams, G. A. Morris and M. Nilsson, Angew. Chem., Int. Ed. , 2016, 55 , 15579 -15582.
- 20 J. C. Cobas, P. Groves, M. Martin-Pastor and A. D. Capua, Curr. Anal. Chem. , 2005, 1 , 289 -305.
- 21 O. Reinstein, M. A. D. Neves, M. Saad, S. N. Boodram, S. Lombardo, S. A. Beckham, J. Brouwer, G. F. Audette, P. Groves, M. C. J. Wilce and P. E. Johnson, Biochemistry , 2011, 50 , 9368 -9376.
- 22 P. Groves, M. Palczewska, M. D. Molero, G. Batta, F. J. Cañada and J. Jiménez-Barbero, Anal. Biochem. , 2004, 331 , 395 -397.
- 23 P. Groves and M. Webba da Silva, Chem. -Eur. J. , 2010, 16 , 6451 -6453.
- 24 G. Moreira, E. Fedeli, F. Ziarelli, D. Capitani, L. Mannina, L. Charles, S. Viel, D. Gigmes and C. Lefay, Polym. Chem. , 2015, 6 , 5244 -5253.
- 25 D. K. Wilkins, S. B. Grimshaw, V. Receveur, C. M. Dobson, J. A. Jones and L. J. Smith, Biochemistry , 1999, 38 , 16424 -16431.
- 26 P. Groves, M. O. Rasmussen, M. D. Molero, E. Samain, F. J. Cañada, H. Driguez and J. Jiménez-Barbero, Glycobiology , 2004, 14 , 451 -456.
- 27 A. Blanazs, S. P. Armes and A. J. Ryan, Macromol. Rapid Commun. , 2009, 30 , 267 -277.
- 28 Y. Bakkour, V. Darcos, S. Li and J. Coudane, Polym. Chem. , 2012, 3 , 2006 -2010.