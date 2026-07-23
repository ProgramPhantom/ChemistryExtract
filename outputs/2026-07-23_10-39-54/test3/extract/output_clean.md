<!-- image -->

Contents lists available at

## Journal of Magnetic Resonance

j o urnal homepage:

<!-- image -->

## Improving the accuracy of pulsed field gradient NMR diffusion experiments: Correction for gradient non-uniformity

Mark A. Connell a , Paul J. Bowyer b , P. Adam Bone a , Adrian L. Davis c , Alistair G. Swanson c , Mathias Nilsson a , Gareth A. Morris a, *

- a School of Chemistry, University of Manchester, Oxford Road, Manchester M13 9PL, United Kingdom
- b Magnetic Resonance Systems, Varian Limited, The Magnet Technology Centre, 10 Mead Road, Oxford Industrial Park, Yarnton, Oxfordshire OX5 1QU, United Kingdom

c Pfizer Global Research and Development, Sandwich, Kent CT13 9NJ, United Kingdom

## a r t i c l e i n f o

Article history: Received 16 December 2008 Revised 21 January 2009 Available online 30 January 2009

Keywords: Diffusion Pulsed field gradients Non-uniform field gradients Stejskal-Tanner equation DOSY

## 1. Introduction

The use of pulsed field gradients (PFGs), most commonly in a spin or stimulated echo, is a powerful technique for NMR diffusion studies in liquid samples . In contrast to other experimental methods, such as isotopic tracer techniques , experiments are rapid, economical and flexible. Typically a series of echo spectra is recorded with increasing PFG amplitude, and the resulting decay of the peak area is fitted to the Stejskal-Tanner equation :

h

i

$$S ( G ) = S _ { 0 } \exp \left [ - D \gamma ^ { 2 } G ^ { 2 } \delta ^ { 2 } \Delta ^ { \prime } \right ] & & ( 1 ) & & \stackrel { \ s o n d } { b r a d o n }$$

where S is the signal amplitude, S 0 is the signal amplitude in the absence of diffusion, D is the diffusion coefficient, d is the gradient pulse width, c is the magnetogyric ratio, G is the gradient amplitude and D 0 is the diffusion time corrected for the effects of diffusion during the gradient pulses.

* Corresponding author. Fax: +44 161 275 4598. E-mail address: (G.A. Morris).

## a b s t r a c t

Pulsed field gradient NMR is a well-established technique for the determination of self-diffusion coefficients. However, a significant source of systematic error exists in the spatial variation of the applied pulsed field gradient. Non-uniform pulsed field gradients cause the decay of peak amplitudes to deviate from the expected exponential dependence on gradient squared. This has two undesirable effects: the apparent diffusion coefficient will deviate from the true value to an extent determined by the choice of experimental parameters, and the error estimated by the nonlinear least squares fitting will contain a significant systematic contribution. In particular, the apparent diffusion coefficient determined by exponential fitting of the diffusional attenuation of NMR signals will depend both on the exact pulse widths used and on the range of gradient amplitudes chosen. These problems can be partially compensated for if experimental attenuation data are fitted to a function corrected for the measured spatial dependence of the gradient and signal strength. This study describes a general alternative to existing methods for the calibration of NMR diffusion measurements. The dominant longitudinal variation of the pulsed field gradient amplitude and the signal strength are mapped by measuring pulsed field gradient echoes in the presence of a weak read gradient. These data are then used to construct a predicted signal decay function for the whole sample, which is parameterised as the exponential of a power series. Results are presented which compare diffusion coefficients obtained using the new calibration method with previous literature values.

Ó 2009 Published by Elsevier Inc.

Accurate measurements of diffusion have a wide range of uses

. One of the more recent, and potentially important, uses is in diffusion-ordered spectroscopy (DOSY) . DOSY uses differences in diffusion coefficient to separate the NMR signals of different components in a mixture, presenting the results in the form of a synthetic multidimensional spectrum with diffusion as an added dimension. The widths of the signals in the diffusion dimension are governed by the standard errors estimated in the fitting of the signal attenuation to its theoretical form (e.g. Eq. ), and ideally should be dominated by random errors. Any systematic errors will broaden the peaks constructed in the diffusion domain (although in favourable circumstances this need not necessarily prevent the detection of small differences in diffusion between different species).

As with any experiment, the accuracy and precision of the diffusion coefficient obtained by fitting NMR signals are critically dependent on the quality of the data. Improvements in hardware, such as the use of actively shielded coils to avoid eddy currents, have greatly improvedthequalityoftheexperimentaldataavailable.Advancesin pulse sequences have further reduced systematic sources of error such as those originating from disturbances to the static magnetic field and to the field/frequency lock . Many - but not all - of the remaining deviations from ideal instrumental behaviour, such as inconsistencies in radio frequency pulse amplitude and phase, and lineshape errors, can be corrected for by reference deconvolution . There remain, however, a number of other important factors. Accurate control of sample temperature is critical: diffusion coefficients typically increase by several percent for each degree rise in temperature, so sample temperature calibration, stability and uniformity are all important. Any bulk movement of the sample or probe hardware will confound diffusion measurements, so it is vital either that thermal convection be avoided or that its effects be compensated for . Where very concentrated samples are used, radiation damping can have florid effects; again, appropriate choice of pulse sequence can allow accurate results to be obtained for suchsystems.Afinal,andinmanycasesdominant,sourceofsystematic error is the spatial non-uniformity of the pulsed field gradients used. Gradient non-uniformity has long been known to be a problem in diffusion measurement by NMR ; a clear explanation of its effects, and one effective route to compensating them, was presented some time ago by Damberg, Jarvet and Gräslund (abbreviated below as DJG). This paper gives an extended analysis, describes an alternative and slightly more general approach to compensating for non-uniform gradients that has proved very effective , and examines some of their practical consequences.

In order to measure absolute diffusion coefficients by PFG NMR, a calibration of the pulsed field gradient strength is needed. This is commonly carried out by measuring the experimental attenuation of the echo signal as a function of nominal pulsed field gradient amplitude for a species of known diffusion coefficient (often H2O), and back-calculating the correction factor between the nominal and actual gradient amplitudes. (Holz and Weingärtner have published a very useful collection of data on accurately known diffusion coefficients in different ranges .) Measurement of the frequency width of the spectral profile obtained for a sample of known length under a given read gradient is occasionally put forward as an absolute calibration method, but it suffers from distortion of the spectral profile caused by magnetic susceptibility discontinuities and fails to take into account the effects of gradient non-uniformity, and is only to be recommended for calibration of very high gradients .

Calibrating diffusion measurements by direct comparison between an unknown and a reference is a viable strategy for accurate measurements, but only if (a) the same gradient pulse widths are used for both measurements, (b) the field gradient system is electrically linear (i.e. the actual gradients produced are directly proportional to their nominal strengths) and (c) exactly the same diffusional attenuation is achieved for both measurements. Requirement (c) is needed because the spatial non-uniformity of the field gradients means that the experimental signal decay deviates from the form of Eq. , as explained below. Requirement (b) is a good approximation on most modern spectrometer systems, except where a diode box or similar device is used (see below). Requirement (a) arises because finite gradient pulse rise and fall times mean that the area of a gradient pulse is not directly proportional to its nominal duration. The net effect of (a)-(c) is that accurate measurements by the comparison method require both the availability of a reference material with a diffusion coefficient in the right range , and very careful choice of experimental conditions.

Modern actively shielded gradient coils give excellent performance, but their design inevitably requires compromises to be made between different aspects of their performance. In particular there appears to be a trade-off between the speed and accuracy with which gradients may be switched on and off, the level of gra- dient noise (field fluctuations caused by the gradient amplifier even when quiescent), and the uniformity of the gradients produced. Thus the probe in this study with the most uniform gradient also had the highest level of gradient noise, sufficiently high that the lineshape of high resolution signals was irreproducible and the resolution degraded. The probe manufacturer's recommended solution was to fit a ''diode box', containing crossed diodes, between the gradient amplifier and the probe. This greatly reduces the lineshape disturbances but degrades the electrical linearity of the gradient system severely at low gradients, and is not appropriate for accurate measurements of diffusion.

All probes suffer to a greater or lesser extent from gradient nonuniformity; many show a field gradient that is strongest close to the centre of the active volume of the coil and falls off to either side. One drastic measure to reduce the effects of non-uniformity is to use either slice selection or a very short sample

to restrict the signals measured to a small volume over which the field gradient variation is small. Unfortunately both involve a major sacrifice in signal-to-noise ratio, as well as introducing problems where the diffusion distance is not small compared to the slice thickness, and their use is probably best limited to experiments where the analysis method used requires strict adherence to the exponential attenuation as a function of gradient squared seen in Eq. . Even with the best available susceptibility matching, the use of very short samples also degrades the signal lineshape considerably.

As has been pointed out , most notably by Damberg et al. , the most effective solution to the problems caused by nonuniform gradients is to quantify their effects and to include them explicitly in the analysis of experimental data by modifying the Stejskal-Tanner equation. Modification is necessary because different parts of the sample experience different gradients, and hence their signals attenuate as a function of nominal gradient at different rates, so that the net signal from the sample shows a diffusional attenuation which deviates increasingly from exponential as the attenuation increases. Adapting the fitting function used to determine the diffusion coefficient allows full sensitivity to be retained, which is vital in diffusion-ordered spectroscopy, and removes the severe limitation (c) on accurate diffusion measurements noted above. The net result is a fitting process that returns accurately calibrated diffusion coefficients and standard errors that more closely reflect random, as opposed to systematic, sources of error. Correction for the effects of gradient non-uniformity is particularly important in the use of multiexponential fitting in DOSY, where any experimental deviation from Eq. will appear to the fitting algorithm as a spurious extra component , and in multivariate analysis of DOSY data by methods such as DECRA, CORE or SCORE

.

There are two common approaches to determining the form of modified Stejskal-Tanner equation required. The first, direct, method is simply to measure the diffusional attenuation as a function of the square of nominal gradient strength for a sample of known diffusion coefficient, and then to fit this to an appropriate functional form (for example, the exponential of a power series , or the difference of two error functions ) with sufficient variable parameters to characterise the deviations seen. The second, indirect, method is to map the spatial variation of the signal and gradient strength across the sample, and then to calculate the expected form of the diffusional attenuation for the whole sample, which can then be fitted as in the direct method. The direct method requires great care if accurate parameters are to be obtained, because of the need to eliminate other systematic sources of error such as temperature drift or unwanted coherence transfer pathways, while the indirect method is also time-consuming and requires significantly more programming. Here we concentrate on the indirect method, partly because it allows experimental verifi- cation that the deviations from the Stejskal-Tanner equation seen are indeed dominated by the spatial non-uniformity of the gradients (and not by some other source of error such as electrical nonlinearity) but mostly because the intermediate data obtained on the spatial variation of gradient strength are required for the analysis of results from spatially resolved experiments such as the Zangger-Sterk method for pure shift DOSY .

In this paper, the indirect calibration method above is described in detail, examples of its application are given, and some of the general implications of non-uniform gradient effects for practical DOSY and diffusion measurement experiments are discussed. In particular, it is noted that the correlation between the spatial variation of the radiofrequency field B 1 and that of the pulsed field gradient can make apparent diffusion coefficients measured by NMR vary according to the pulse width calibration used.

## 2. Theory

## 2.1. Effect of gradient non-uniformity on signal attenuation

Diffusion measurements by PFG NMR typically fit the decay of signal amplitude S as a function of gradient pulse area squared to the Stejskal-Tanner equation (Eq. ). For a simple spin or stimulated echo sequence using two rectangular gradient pulses which have duration d and whose midpoints are a time D apart, the corrected diffusion delay D 0 = D  d /3. If shaped pulses , sometimes used to reduce the effects of eddy currents, are employed in the pulse sequence, two modifications are needed to the Stejskal-Tanner equation: the product G d needs to be replaced by the area of the shaped gradient pulse (2 G d / p for a half-sine pulse), and the correction D 0 to allow for diffusion during the gradient pulses changes ( D 0 = D  d /4 for two half-sine pulses).

Unfortunately the pulsed field gradient hardware typically used in NMR does not, as noted above, generate gradients that are perfectly uniform over the active sample volume, and the net experimental signal decay therefore is not accurately described by Eq. . Forcing a fit of such data to Eq. has two major consequences. First, as the signal attenuation increases, so does the deviation from Eq. ; as a result, the diffusion coefficient obtained by fitting the decay to Eq. varies systematically depending on the extent of attenuation used. Second, the error estimate obtained from the fitting process is increased, degrading diffusion resolution in experiments such as DOSY.

If the spatial variation of signal strength S ( r ) in the absence of diffusion and that of gradient strength G ( r ) are both known, then the total signal S total obtained from the sample under given experimental conditions may be found by integrating over r :

Z

$$S _ { t o t a l } = \left | \, S ( \underline { r } ) \exp [ - D \gamma ^ { 2 } G ^ { 2 } ( \underline { r } ) \delta ^ { 2 } \Delta ^ { \prime } ] d \underline { r } \, & & ( 2 ) & \, _ { \ } \text {This point}$$

In practice the gradient strength is defined experimentally in terms of a spectrometer parameter C , a nominal gradient strength that may be defined in gradient units, as a percentage of maximum gradient amplitude, or as a number of DAC points. If the gradient amplifier and coil system is electrically linear, then the gradient at a given point is given by:

$$G ( \underline { r } ) = \beta \Gamma g ( \underline { r } ) & & ( 3 ) & \begin{matrix} \mu \ p n i n { 3 } \\ \mu \ p n i n { 2 } \end{matrix} \\ & & \intertext { G ( \underline { r } ) = \beta \Gamma g ( \underline { r } ) } & & ( 3 ) & \intertext { F o r } & & & & \intertext { F o r }$$

where b is a proportionality constant and g ( r ) a shape factor, both specific to the particular probe used. Substituting Eq. into Eq. gives the total signal as a function of nominal gradient strength C :

Z

$$S _ { t o t a l } ( \Gamma ) = \left \lceil S ( \underline { r } ) \exp [ - D \gamma ^ { 2 } \beta ^ { 2 } \Gamma ^ { 2 } g ^ { 2 } ( \underline { r } ) \delta ^ { 2 } \Delta ^ { \prime } ] d \underline { r } \right \rceil _ { \ } e v e n \text { for }$$

The net effect is that the signal decay is no longer a Gaussian function of C ; the two practical issues are first, how to measure the spa- tial variation of signal and of gradient, and second, how best to represent this decay function in a form suitable for fitting experimental attenuation data to.

## 2.2. Spatial mapping of sample signal and gradient

In principle G ( r ) and S ( r ) can be mapped in 3D by MR imaging techniques, but in practice a 1D mapping along the sample long axis ( z ) suffices for high resolution NMR probes, where the dominant variation both in signal and in gradient is along z . Measuring the attenuation of the signal profile obtained by performing a PFG stimulated echo experiment on a sample of known diffusion coefficient using a weak read gradient during data acquisition gives a series of signal profiles S ( C , f ), where f is the Larmor frequency at position z , which characterises the diffusional decay at different positions z in the sample. These data may then be fitted to Eq. to find the product b g ( f ). This is most conveniently done by choosing a trial value for b (typically based on the spectrometer manufacturer's recommended calibration method), and determining an apparent diffusion coefficient D app for each value of f . The function g ( f ) is then given by ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffi f D app ð f Þ = D o g p , where D o is the known diffusion coefficient of the calibration sample used. A convenient calibrant is a dilute solution of H2O in D2O; this avoids radiation damping effects. Accurate values of D have been reported in the literature for the diffusion coefficients of H2O/D2O mixtures . Because the gradient varies as a function of position, f is not linearly related to position z , but within the active volume of the radiofrequency coil its variation with z is monotonic and the two may be interconverted as follows:

Z

$$\text {pulse} , \quad z ( \zeta ) = \int \frac { 2 \pi } { \gamma g ( \zeta ) } d \zeta \,$$

This allows g ( f ) and S ( f ) to be converted into functions of z if required. This can be useful for characterising and comparing probes, but is not essential for analysing the consequences of non-uniform gradients, since the integral over r in Eq. can be performed over f :

Z

Z

$$\text {radiant} \quad S _ { t o t a l } ( \Gamma ) = \int S ( 0 , \zeta ) \exp \left [ - D \gamma ^ { 2 } \beta ^ { 2 } I ^ { 2 } \delta ^ { 2 } \Delta ^ { \prime } \left ( g _ { o } - \sum _ { n = 1 } ^ { N } g _ { n } \zeta ^ { n } \right ) \right ] d \zeta \quad ( 8 )$$

In principle this information is of course available experimentally, from the integrals of the signal profiles, but in practice for attenuation beyond 100 -the measured signals are significantly distorted by noise and by leakage of signal through unwanted coherence transfer pathways. Calculating the signal decay using data from mapping experiments allows S total ( C ) to be determined reliably even for relatively high levels of attenuation. The two datasets needed for the evaluation of Eq. are the gradient coefficients of Eq. , and the signal profile S (0, f ). The latter is available from the fitting of S ( C , f ) to Eq. , which yields a decay constant and

h

i

$$\text {ined by} \quad S _ { t o t a l } ( \Gamma ) = \left / \, S ( 0 , \zeta ) \exp \left [ - D \gamma ^ { 2 } \beta ^ { 2 } \Gamma ^ { 2 } g ^ { 2 } ( \zeta ) \delta ^ { 2 } \Delta ^ { \prime } \right ] d \zeta$$

On the fringe of the sample active volume the signal is typically too poor to give a reliable estimate of g ( f ). In practice, it is therefore desirable to extrapolate the measured g ( f ) from the region of strong signal to cover the outer edges of signal profile. This can conveniently be done by representing g ( f ) as a power series in f :

$$\exp \bar { - } & \quad g ( \zeta ) = g _ { o } - \sum _ { n = 1 } ^ { N } g _ { n } \zeta ^ { n } \\$$

This power series is useful in the analysis of the results of spatially resolved diffusion experiments .

The decay of the total signal as a function of C can now be evaluated by numerical integration:

"

!

#

an amplitude for each point on the signal profile; in practice a slice through S ( C , f ) at low C , where diffusional attenuation is negligible, serves equally well.

## 2.3. Parameterising experimental signal decay

Having calculated or measured S total ( C ) it remains to approximate this in a functional form convenient for fitting experimental diffusion decays. Here, two related approaches have been proposed, which differ in how the decay function is parameterised. In the model of DJG, the signal strength as a function of relative gradient is represented by a truncated linear distribution defined by minimum and maximum values of the gradient . This approach corresponds to a physically unrealistic form of G ( z ), with a discontinuous slope at z = 0 (see ), but is perfectly practical and gives a good description of the distribution of signal as a function of gradient strength for mild non-uniformity. Integrating over all values of gradient leads to the expression:

$$\frac { S _ { \text {total} } ( \Gamma ) } { S _ { \text {total} } ( 0 ) } = & \frac { \exp ( - \eta \Gamma ^ { 2 } g _ { \min } ^ { 2 } ) - \exp ( - \eta \Gamma ^ { 2 } g _ { \max } ^ { 2 } ) } { 2 \eta \Gamma ^ { 2 } ( g _ { \max } - g _ { \min } ) ^ { 2 } } \\ & - \frac { g _ { \min } \sqrt { \pi } [ erf ( g _ { \max } \Gamma \sqrt { \eta } ) - e r f ( g _ { \min } \Gamma \sqrt { \eta } ) ] } { 2 \Gamma ( g _ { \max } - g _ { \min } ) ^ { 2 } \sqrt { \eta } } \\ \intertext { s u r g . } \frac { S _ { \text {total} } ( \Gamma ) } { S _ { \text {total} } ( 0 ) } = & \frac { \exp ( - \eta \Gamma ^ { 2 } g _ { \min } ^ { 2 } ) - \exp ( - \eta \Gamma ^ { 2 } g _ { \max } ^ { 2 } ) } { 2 \eta \Gamma ^ { 2 } ( g _ { \max } - g _ { \min } ) ^ { 2 } \sqrt { \eta } } \\ \intertext { c o l d e f . } \frac { g _ { \min } \sqrt { \pi } [ e r f ( g _ { \max } \Gamma \sqrt { \eta } ) - e r f ( g _ { \min } \Gamma \sqrt { \eta } ) ] } { 2 \Gamma ( g _ { \max } - g _ { \min } ) ^ { 2 } \sqrt { \eta } } \\ \intertext { s u r g . } \frac { u _ { \ } x y } { u _ { \ } y x }$$

where g = D c 2 d 2 D 0 .

For the past 8 years an alternative method has been used in this laboratory in which net signal decay for the whole sample volume is represented as the exponential of a power series :

"

#

$$\frac { S _ { \text {total} } ( \Gamma ) } { S _ { \text {total} } ( 0 ) } = \exp \left [ - \sum _ { n = 1 } ^ { N } c _ { n } \eta ^ { n } \beta ^ { 2 n } \Gamma ^ { 2 n } \right ] & & \text {ethtype} \\ & & \text {copper} \\ & & \text {of water}$$

The calibration process enables the theoretical form of the signal decay under the mapped gradient shape to be calculated even for very high levels of attenuation. Fitting the signal decay S total ( C ) to Eq. produces probe-specific fit coefficients, just as in the DJG method but with the ability to accommodate more severe gradient non-uniformity. A further minor advantage of Eq. over Eq. is that the coefficient c 1 has a simple physical significance, being the square of the signal-weighted average of g ( f ) over the sample, i.e.

the ratio of the actual gradient averaged over the sample to the nominal gradient strength C . The remaining coefficients characterise the deviation from mono-exponential decay.

## 3. Experimental

Measurements were recorded on three Varian spectrometers; an INOVA 500 and 400, and a UNITY 500. Five different 5 mm probes were used, each with actively shielded gradient coils, to allow comparison between probes of different types. On the INOVA 400, two different probes were used. Probe 1 was a standard Varian broadband indirect detection probe with a gradient coil delivering nominal gradients of up to 30 G cm  1 ; the second was an extensively modified direct detection broadband probe (probe 2) with a picaresque history , equipped with a 60 G cm  1 gradient coil. On the UNITY 500 spectrometer a 1 H/ 13 C/ 15 N triple probe (probe 3) with a gradient coil delivering nominal gradients of up to 30 G cm  1 , and a Nalorac dual broadband/ 1 H probe (probe 4) with a nominally 50 G cm  1 gradient coil, were used. Finally, on the INOVA 500, a triple resonance cryoprobe (probe 5) with a gradient coil delivering nominal gradients of up to 60 G cm  1 was used. All samples were in standard 5 mm NMR tubes filled to depths of 5080 mm. Prior to acquisition, all samples were shimmed using manual xy shimming and automated z -gradient shimming on the solvent deuterium signal . All experiments were carried out without sample spinning, with the sample temperature regulated at 25 ± 1 ° C; the exact temperature produced by the variable temperature unit was calibrated using a standard test sample of pure ethylene glycol. The airflows to the probe were passed through copper pipe filled with lead shot, held within an insulated bucket of water at ambient temperature, to minimise the effects of variation in room temperature .

Signal strength and gradient amplitude were mapped as a function of z for all five probes, using the Oneshot pulse sequence modified to include a read gradient G r during signal acquisition

( a). The spectrometer operating frequency was set to be at exact resonance for the calibrant signal with no read gradient applied; while not necessary for the correction of the effects of gradient non-uniformity on conventional diffusion measurements described here, it is essential if the calibration of the spatial dependence of the gradient is to be used for other purposes such as pure shift DOSY . Much more extensive phase cycling than is usually necessary - or indeed desirable - was performed, in order to avoid the read gradient refocusing unwanted coherence transfer pathways, and care was taken with sequence timing to minimise the need for 1st order phase correction of the signal profiles. In addition, signal and gradient were mapped for probe 1 using a convection-compensated pulsed field gradient double stimulated echo sequence , again with a read gradient during acquisition

Fig. 1. Diffusion measurement pulse sequences, modified to include a weak read gradient G r during acquisition for mapping experiments. (a) Oneshot pulse sequence where D and d are the diffusion delay (the separation between the midpoints of the rectangular gradient pulses) and the net diffusion-encoding gradient pulse width, respectively; here the phase cycling ( ) depends on whether the stimulated antiecho (solid line) or echo (dotted line) version of the sequence is used. (b) Pulsed field gradient double stimulated echo (PFGDSTE) convection-compensated sequence, described in Section , where D 1 and D 2 are the two (equal) diffusion delays and d is the gradient pulse width. Gradient pulses with vertical arrows indicate gradient levels which are changed to vary the amount of diffusion encoding; a delay of up to 2 ms is allowed after each gradient pulse for gradient and field stabilisation.

<!-- image -->

(

b).

These two pulse sequences were chosen as representative of typical sequences used in DOSY and for diffusion measurements. The first is a general-purpose sequence, a more sophisticated form of the bipolar pulse pair stimulated echo (BPPSTE) sequence ; the second is a common (but not always a wise) choice where thermal convection of the sample is either a proven or a potential problem, but requires extensive phase cycling, yields poorer signal lineshapes, and suffers a twofold sensitivity penalty compared to the Oneshot sequence. For each experiment, between 10 and 20 signal profiles were measured for nominal gradient strengths Cb , incremented in equal steps of ( Cb ) 2 , from ca. 0.5 G cm  1 up to the point of 30% signal attenuation. The total diffusion-encoding gradient pulse duration d was 4 ms (i.e. for the Oneshot sequence each individual pulse was of 2 ms duration, and for PFGDSTE 4 ms), and diffusion delays D of between 50 and 300 ms were used. The nominal read gradient G r during acquisition was of 0.05 G cm  1 , corresponding to a signal profile width of approximately 350 Hz for probes which have a sensitive volume about 17 mm high. Data were acquired for probes 1, 3 and 5 using sample 1 (a standard doped water sample containing 1% H2O in D2O, 0.1% sodium 3-(trimethylsilyl)-1-propanesulphonate reference (DSS) and 0.1 mg/ml GdCl3), and for probes 2 and 4 using sample 2 (100% H2O).

Free induction decays were zero-filled once and weighted using a Gaussian function with a time constant of 0.1 s before Fourier transformation. The baselines of the spectra were then corrected using a cubic spline function. Corresponding points (400 in total) at regularly spaced frequency intervals on each profile were fitted to Eq. to give the gradient shape function g ( f ) and the signal distribution S ( f ). The theoretical form of the signal decay for the whole sample was then constructed by numerical integration of Eq. , and parameterised by fitting the power series model of Eq. with two to four terms. All of the above manipulations were carried out using in-house modifications to the spectrometer Vnmr 6.1C software.

In order to compare the measured experimental signal attenuation with that derived from the signal and gradient mapping data, a reference dataset was acquired for probe 1 with the Oneshot sequence, using 100 equal increments in gradient squared for nominal gradient amplitudes from 0.5 to 19.6 G cm  1 . For each gradient amplitude, 16 transients were acquired with a recycle time of 1.2 s; the total diffusion-encoding gradient pulse duration d was 4 ms, and a diffusion delay D of 100 ms was used. The signal integral as a function of gradient squared was tabulated, and again parameterised by fitting to Eq. .

The axial variation B 1( f ) of the radiofrequency field was determined by measuring the free induction decay, recorded under a read gradient of nominal strength 0.05 G cm  1 , following a single pulse with a 20 ° fl ip angle. As a consequence of the reciprocity theorem , the square root of the signal profile is directly proportional to the required function B 1( f ), the constant of proportionality being easily found by comparing profiles obtained with different flip angles. B 1( f ) may be converted into B 1( z ) using the relationship of Eq. . The former was used to simulate shapes of signal profile S ( f ) expected for different nominal pulse flip an- gles for the Oneshot and PFGDSTE convection-compensated pulse sequences of a and b.

A series of diffusion measurements on pure compounds covering a large range of diffusion coefficients was made using probe 1, using the PFGDSTE convection-compensated sequence ( b) with no read gradient. Typically, 10 values of nominal gradient strength between ca. 0.1 and 13.7 G cm  1 were used. The gradient pulse duration d was 4 ms and the maximum diffusion delay D 500 ms. Peak integrals as a function of gradient strength were fitted to Eq. to determine the diffusion coefficient and its estimated standard error. In addition, nine diffusion measurements were made on the doped water sample, varying the nominal flip angle from 70 ° to 110 ° using probe 1 with the Oneshot sequence ( a) with no read gradient. The nominal 90 ° pulse width was calibrated conventionally by assigning a flip angle of 180 ° to the pulse width yielding zero net signal. Ten values of nominal gradient amplitude were used from 0.98 to 9.8 G cm  1 . The gradient pulse duration d was 4 ms and the diffusion delay D was 200 ms. Peak integrals as a function of gradient strength were fitted to a single exponential (Eq. ) and to Eq. to determine the diffusion coefficient D and its estimated standard error.

Gradient mapping experiments are significantly more demanding than normal diffusion measurements. As already mentioned, the potential for the read gradient to refocus unwanted coherence transfer pathways in a series of echoes during the acquisition of the free induction decay necessitates extensive phase cycling, although this requirement can be relaxed somewhat if gradient pulse amplitudes are tailored to minimise potential refocusing. a and b lists the extended phase cycles used for the Oneshot and PFGDSTE experiments, respectively. Because the long, low-level gradient pulse during acquisition dephases the deuterium lock signal, it is not possible to maintain field-frequency lock, making field stability critical. Variations in static field strength B 0 have little impact on the middle part of the gradient map, but the steep decline in signal at either side of S ( f ) means that small changes in B 0 have a big effect on the apparent diffusion coefficient at the edges of the map g ( f ). Using a high read gradient reduces the significance of field/ frequency fluctuations, but maximises the potential for unwanted echoes. The relatively weak signal at the edges of the profile means that any error in spectral baseline will cause a large change in apparent diffusion coefficient, distorting the gradient map obtained. Care must therefore be taken to minimise 1st order phase shifts in the profile by ensuring that the timing of the start of data acquisition is exact. Finally, any discrepancy in the net areas of the diffusion-encoding and -decoding gradient pulses will lead to position-dependent phase errors in the signal profile, and should be corrected for by adjusting the amplitude and or duration of one of the pulses. In the experiments reported here such corrections were typically of the order of 0.1% or less.

Table 1 (a) Phase cycling for the Oneshot pulse sequence of a, and (b) for the PFGDSTE convection-compensated pulse sequence of b. Phases are notated as multiples of 90 ° (0 = 0 ° , 1 = 90 ° , 2 = 180 ° , 3 = 270 ° ), with subscripts denoting repetition.

| (a) Oneshot   |                                            |
|---------------|--------------------------------------------|
| U 1 U 2       | 0 64 1 64 2 64 3 64 0123                   |
| U 3           | 0 4 1 4 2 4 3 4                            |
| U 4           | 0 256 1 256 2 256 3 256                    |
| U 5           | 0 16 1 16 2 16 3 16                        |
| U R           | U 1  2 U 2 + U 3  U 4 + 2 U 5 (solid line) |
| U R           | 2 U 2  U 1  U 3  U 4 + 2 U 5 (dotted line) |
| (b) PFGDSTE   |                                            |
| U 1           | 0 256 1 256 2 256 3 256                    |
| U 2           | 0 16 1 16 2 16 3 16 + 0123                 |
| U 3           | 0123                                       |
| U 4           | 0 4 1 4 2 4 3 4                            |
| U 5           | 0 64 1 64 2 64 3 64 + 0 4 1 4 2 4 3 4      |
| U R           | U 1  U 2  U 3 + U 4 + U 5                  |

Fortunately, where the signal profiles obtained have high signal-to-noise ratio, as is usually the case, it is possible to circumvent the last two requirements, which affect the phases of the signal profiles, by adapting the sequence of to acquire the signal profile data in a whole rather than a half echo, and then to carry out the data analysis using absolute value data. The requirement of high signal-to-noise ratio is necessary because in absolute value display mode the noise is always positive, and hence biases the results slightly. In the work described here the sequences of were used and the analysis carried out in phase sensitive mode to get the highest available accuracy, but for routine use the absolute value approach appears to be simple and robust.

## 4. Results

## 4.1. Gradient mapping

shows the signal profiles recorded as a function of diffusion-encoding gradient for probe 1 using the modified Oneshot sequence of a but with nominal pulse flip angles of 80 ° and 160 ° rather than 90 ° and 180 ° (see Section ). The read gradient G r is used to encode the magnetisation spatially so that signal attenuation as a function of position z can be determined. Assuming that the rate of diffusion is uniform across the sample (in practice, assuming a uniform sample temperature), the gradient strength as a function of z was determined by fitting corresponding points on each profile to the Stejskal-Tanner equation (Eq. ) using the nominal gradient strengths G defined by the manufacturer's initial calibration method (measurement of the signal profile width at 20% amplitude under a known read gradient). This yielded an apparent diffusion coefficient D app( f ) as a function of position z ; dividing D app( f ) by the known diffusion coefficient at 25 ° C for 1% H2O/D2O of 1.91 -10  9 m 2 s  1 gave the relative gradient strength squared g 2 ( f ) shown, together with the signal amplitude S ( f ), in normalised form in .

Fig. 2. Signal profiles for increasing diffusion weighting, measured with the modified Oneshot pulse sequence shown in a. Data were acquired at 400 MHz using a standard doped water sample (1% H2O in D2O, 0.1 mg/ml GdCl3, 0.1% sodium 3-(trimethylsilyl)-1-propanesulphonate) on probe 1, with 10 nominal gradient pulse amplitudes equally spaced in gradient squared between 0.49 and 9.81 G cm  1 . 256 transients of 2048 complex points were averaged for each gradient value, in a total time of 100 min.

<!-- image -->

Fig. 3. Profiles of relative signal S ( f ) (solid line) and gradient strength squared g 2 ( f ) (dashed line) as a function of frequency in Hz calculated from the data of as described in the text.

<!-- image -->

The ''horns' of the measured signal profile arise because the gradient is weaker at the edges of the active region of the sample volume, so the signal from a given slice of sample is compressed into a narrower frequency range. The horns become more pronounced in the lower profiles of because the sample regions with weakest gradient amplitude experience the slowest attenuation. From the data of , the profiles of gradient G ( z ) and signal S ( z ) as a function of position z in were calculated using Eq. . also shows the corresponding variation of gradient strength as a function of position G ( z ) that would be assumed by the DJG model (also used by Zhang ) if the B 1 homogeneity were perfect.

The relative gradient as a function of frequency g ( f ) (the square root of the data of ) was fitted to an 8th order power series in f using Eq. . Numerical integration of Eq. using the gradient coefficients of Eq. and the normalised first signal profile of (which has negligible diffusional attenuation) was used to calculate the signal decay as a function of gradient strength for the whole sample volume down to 10 4 -fold attenuation. This decay was then fitted using the function described by DJG (Eq. ), and using Eq. , in each case yielding two coefficients that are characteristic of the probe and pulse sequence used to acquire the data. The quality of fit of the calculated signal decay obtainable with the two different model functions can be seen in the semilog plot of , which compares pure exponential fitting (Eq. ), the DJG model function (Eq. ), and the exponential 2nd order power series (Eq. ). Also included in are experimental data points for attenuation of the water signal; these agree well with the calculated form of the signal decay over the full range down to 10 3 -fold attenuation (beyond which S/N becomes a limiting factor), mm confirming that the measured z variation of the gradient amplitude is sufficient to explain the observed deviation from the StejskalTanner equation. compares the experimental distribution of signal as a function of relative gradient strength of Eq. , constructed from the data of , with the truncated linear distribution of the DJG model, obtained by fitting the calculated signal decay to Eq. . The experimental distribution of signal strength shows as expected that very little of the sample experiences a weak gradient, and that the central part of the sample experiences a strong uniform gradient, causing the pronounced cusp in . The DJG model of the gradient shape g ( z ) corresponds to a triangular distribution of signal strength as a function of gradient strength, rising linearly from zero at g min to a maximum at g max. This is not physically realistic, but, as shows, it still gives an excellent representation of diffusional attenuation for a typical high resolution probe. In extreme cases of gradient non-uniformity, the more flexible power series model of Eq. should allow much more accurate fitting of experimental data.

Fig. 4. Profiles of relative signal S ( z ) (solid line) and relative gradient strength g ( z ) (short dashed line) as a function of position z in mm, calculated from the data of using Eq. , together with the model described by DJG for g ( z ) (long dashed line).

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Fig. 5. Normalised signal (solid line) and gradient strength (dashed line) as a function of position along the gradient axis z , measured as in for (a) probe 1 (Varian 5 mm 400 MHz indirect detection probe, maximum nominal gradient strength 30 G cm  1 ); (b) probe 2 (Varian 5 mm 400 MHz broadband probe, successively modified for 300 and 400 MHz operation and to include a gradient coil of maximum nominal gradient strength 60 G cm  1 ); (c) probe 3 (Varian 5 mm 500 MHz H/C/N triple probe, maximum nominal gradient strength 30 G cm  1 ); (d) probe 4 (Nalorac 5 mm 500 MHz broadband probe, maximum nominal gradient strength 50 G cm  1 ) and (e) probe 5 (Varian 5 mm cryoprobe, maximum nominal gradient strength 60 G cm  1 ). The midpoint of each signal profile is centred at z = 0.

<!-- image -->

Fig. 6. Plot of relative signal strength against relative gradient strength for the experimental data of (solid line) and for the DJG model, which assumes a triangular distribution for signal strength, with the fitting parameters g min and g max used in .

The mapping process was carried out for five different probes, with the results shown in . Normalised signal (solid line) and gradient (dashed line) profiles are shown for each probe, with z = 0 defined by the midpoint of the signal profile in each case. Probe 4 has the best gradient uniformity, but as noted earlier suffers from significantly worse gradient noise - manifest as field instability when the nominal gradient is zero - than the other probes. For high resolution experiments other than diffusion measurements the probe manufacturer advised the use of a diode box with this probe. Probe 5, a cryoprobe, has good gradient uniformity over most of the active region of the sample, but a very rapid falloff at the edges. This can lead to problems with water suppression, because the field gradient at the fringes of the probe active volume is too weak to give effective signal editing. Probes 1 to 3 share the same basic design of coil, although probe 2 has twice the nominal gradient strength, and hence have very similar gradient shapes g ( z ). Probe 2 is much-modified and has a long and chequered history; the centre of its gradient coil is approximately 2 mm above the centre of the active volume, resulting in a relatively weak gradient at the bottom end of the sample. For this probe, using Eq. to 4th order gives significantly better correction for the effect of non-uniform gradients than either Eq. to 2nd order or the DJG parameterisation of Eq. .

## 4.2. Effect of pulse calibration on diffusion measurements

As explained in Section , different regions of the sample contribute differently to the net signal as the nominal pulse flip angle

<!-- image -->

<!-- image -->

mm

110 o

105 o

100 o

95 o

90 o

85 o

80 o

75 o

70 o

-300

0

100

200

300

-100

-200

Hz

0

100

200

300

-100

-200

-300

Hz

Fig. 8. Experimental profiles of relative signal S ( f ) as a function of frequency, stacked vertically as a function of nominal pulse width for (a) (i) the Oneshot, and (b) (i) the pulsed field gradient double stimulated echo (PFGDSTE) convectioncompensated sequence, together with (a) (ii) and (b) (ii) profiles calculated as described in the text using the calculated B 1( f ) as a function of frequency for the Oneshot and PFGDSTE sequences, respectively.

Fig. 7. Semilog plot of the calculated water signal attenuation from using the mapping experiment for the measured S ( z ) and g ( z ) (filled circles), the fit to a single exponential using Eq. (long dashed line), the fit to the DJG model of Eq. (short dashed line) and the fit to the two parameter power series model of Eq. (solid line), together with the signal attenuation measured experimentally using the pulse sequence of a with a read gradient G r of zero (crosses).

<!-- image -->

changes. To take an extreme example, if pulse widths were chosen to give twice the nominal flip angle at the centre of the active vol-

<!-- image -->

b

ume, the pulses of a and b would have flip angles of 180 ° and 360 ° and the centre of the sample would contribute no signal at all, the maximum signal coming from the wings of the normal signal profile where the radiofrequency field B 1 has fallen to half the value at the coil centre. shows the effect on the signal profile of varying the nominal flip angle used for (a) the Oneshot and (b) the PFGDSTE pulse sequence. Column (i) shows the experimental signal profiles for different nominal flip angles, and column (ii) the expected signal profiles calculated from the measured variation of B 1 with z . The nominal flip angles shown are with respect to the conventional pulse calibration, in which the pulse width yielding zero net signal is assigned a flip angle of 180 ° . In practice the latter criterion means that different regions of the sample contribute equal and opposite signals at their pulse width; the centre of the sample experiences a flip angle greater than, and the fringes of the sample a flip angle less than, 180 ° .

The calculations of the profiles for the two different sequences used the theoretical dependence of signal on actual flip angle h ( z ), sin 7 h for the Oneshot sequence of a and sin 5 h for the convection-compensated PFGDSTE sequence of b. The experimental and calculated profiles are in good agreement, suggesting that it should be possible to parameterise NUG correction accurately for arbitrary pulse sequences using only the experimental data for g ( f ) for a single pulse sequence and the measured B 1( f ). For nominal flip angles in the range 70-90 ° the variation in the shape of signal profile as a function of h is very small; the sine terms restrict the changes to a slight flattening of the top of the profile and widening of the shoulders as 90 ° is approached. Above 90 ° , however, the signal in the middle of the profile begins to fall rapidly and hence the signal contribution made by the fringes of the active volume, where the gradient is weakest, rises. The same general trends apply for both sequences, but the effects are slightly more serious for the Oneshot sequence because of the loss of refocusing by the ''180 ° ' pulses.

The effect of the change in the relative contributions made by the centre and the edges of the sample as the nominal flip angle passes 90 ° is to weaken the overall diffusion weighting imparted by the gradient pulses, as the sample fringes increase in importance. shows the effect on apparent diffusion coefficient of varying the nominal flip angle from 70 ° to 110 ° for (a) the Oneshot and (b) the PFGDSTE pulse sequence. The experimental data were processed twice: once using a mono-exponential fit (triangles)

Fig. 9. Plot of apparent diffusion coefficient D for a standard doped water sample (1% H2O in D2O, 0.1 mg/ml GdCl3, 0.1% sodium 3-(trimethylsilyl)-1-propanesulphonate) measured as a function of nominal pulse width h for (a) the Oneshot and (b) the pulsed field gradient double stimulated echo (PFGDSTE) convection-compensated pulse sequence. Triangles represent a single exponential fit of data to Eq. , and squares show data fitted to a 2nd order exponential power series (Eq. ). Error bars indicate twice the standard error estimated by the Levenberg-Marquardt fitting algorithm.

<!-- image -->

<!-- image -->

with a gradient calibration factor b set using the first term of the power series in Eq. , which gives the correct signal-weighted average gradient, and once using non-uniform field gradient correction by fitting experimental data to Eq. (squares). The error bars indicate twice the standard error estimated by the LevenbergMarquardt fitting algorithm. The data show clearly that the effect

<!-- image -->

4

G 2

δ

2

b

of field gradient non-uniformity is to make apparent diffusion coefficients measured by NMR vary with pulse flip angle; because the sensitivity to flip angle increases markedly above 90 ° nominal flip angle it is prudent to trade a small decrease in signal-to-noise ratio for a reduction in systematic errors by using nominal flip angles about 10% lower than the theoretical optimum, i.e. using 80 ° and 160 ° pulses in place of 90 ° and 180 ° . This is why the calibration data reported earlier were measured with a reduced flip angle, and why the apparent diffusion coefficients found with non-uniform gradient correction in the data of match the literature value at a nominal flip angle of 80 ° .

## 4.3. Effect of signal attenuation range on diffusion measurements

In any measurement of diffusion by PFG NMR a choice has to be made of the gradient pulse widths, diffusion delay and range of pulsed field gradient strengths to be used, and hence of the range of diffusional attenuation observed. Because the contribution to the total signal made by regions of the sample with stronger gradient G decreases as the signal attenuation increases, mono-exponential fitting (Eq. ) of experimental diffusion data will lead to an apparent diffusion coefficient which depends on the choice of attenuation range. shows the apparent diffusion coefficient and its estimated standard error as a function of the range of signal attenuation chosen for a series of measurements with the Oneshot sequence of a. Nine signal measurements in equal increments of gradient squared for each of 11 different choices of maximum nominal gradient varying from 0.49 to 19.6 G cm  1 , corresponding to maximum attenuations of approximately 2- to 2000-fold, were drawn in each case from a total dataset of 100 measurements spanning the full gradient range.

a compares the results of mono-exponential fitting (triangles) with fitting using Eq. to 2nd order (squares). As expected, fitting using Eq. leads to apparent diffusion coefficients which are independent of attenuation range and show very low standard errors. At very low attenuation range the results of mono-exponential fitting converge on the correct diffusion value. This is because the gradient calibration factor b was set, as above, to give the correct value for the signal-weighted average of gradient G over the sample volume. For very low attenuation the exponential decay may be approximated by a straight line, and thus gives the correct value of D . For all but the smallest ranges of attenuation the deviation of the experimental decay from a single exponential increases, which leads both to underestimation of D and to greatly increased estimated errors. b shows the re-

5

(max)

6

7

8

0

1

2

3

-D

4

G 2

δ

2

c

Fig. 10. Apparent diffusion coefficient D as a function of range of diffusional attenuation for experiments on probe 1 using the Oneshot sequence. Data were acquired using a standard doped water sample (1% H2O in D2O, 0.1 mg/ml GdCl3, 0.1% sodium 3-(trimethylsilyl)-1-propanesulphonate) incrementing nominal pulsed gradient amplitude in 100 steps from 0.49 to 19.68 G cm  1 . Triangles represent a single exponential fit of selected sets of 10 datapoints to Eq. , and squares a fit (a) to a 2nd order exponential power series (Eq. ) parameterised by fitting the synthetic diffusional decay (filled circles in ) calculated using the measured signal and gradient profiles, (b) to a 2nd order exponential power series parameterised by fitting the experimental diffusional decay (crosses in ), and (c) to the DJG function of Eq. parameterised by fitting the synthetic diffusional decay.

5

(max)

6

7

8

0

1

2

3

-D

γ

2

'

∆

γ

2

'

∆

Table 2

Experimental and literature values for diffusion coefficients of simple liquids.

|    |                    | Experimental D /10  9 m 2 s  1   | Literature D /10  9 m 2 s  1   |
|----|--------------------|----------------------------------|--------------------------------|
| a  | 4.28m MgCl 2       | 0.472 ± 0.005                    | 0.468 ± 0.008                  |
| b  | Cyclooctane        | 0.55 ± 0.005                     | 0.546 ± 0.006                  |
| c  | Dimethylsulphoxide | 0.73 ± 0.007                     | 0.723 ± 0.008                  |
| d  | 3.21m MgCl 2       | 0.779 ± 0.008                    | 0.768 ± 0.008                  |
| e  | Dioxane            | 1.09 ± 0.007                     | 1.100 ± 0.01                   |
| f  | 2.02m MgCl 2       | 1.203 ± 0.01                     | 1.206 ± 0.01                   |
| g  | 0.995m MgCl 2      | 1.728 ± 0.02                     | 1.753 ± 0.02                   |
| h  | 0.372m MgCl 2      | 2.036 ± 0.02                     | 2.049 ± 0.02                   |
| i  | Water              | 2.299 ± 0.005                    | 2.303 ± 0.02                   |
| j  | Methanol           | 2.42 ± 0.02                      | 2.421 ± 0.03                   |
| k  | Chloroform         | 2.43 ± 0.03                      | 2.432 ± 0.03                   |
| l  | Cyclopentane       | 3.1 ± 0.02                       | 3.147 ± 0.03                   |
| m  | Acetonitrile       | 4.37 ± 0.04                      | 4.370 ± 0.04                   |

sults of fitting the water signal decay to Eq. (squares) parameterised using the directly measured experimental signal decay and c the results fitting to the DJG model (Eq. ) (squares). In each case, the triangles represent the results of fitting to a single exponential (Eq. ) with the gradient calibration factor b set to give the correct value for the signal-weighted average of gradient G over the sample volume. It can be seen that compensating for non-uniform field gradients using any of the methods described leads to a more accurate evaluation of the diffusion coefficient D when fitting for any attenuation range, and that the three methods that compensate for gradient non-uniformity give essentially identical results.

## 4.4. Comparison of measurements with literature data

A wide variety of potential diffusion standards have been proposed for different ranges of diffusion coefficient. Here experimental results are reported comparing the results of experimental measurements made using a single calibration by the method of Section with reported values for a range of common standards. compares experimental measurements of diffusion coefficient, obtained using Eq. as described earlier to correct for the effects of gradient non-uniformity, with the values reported in the literature . Data were acquired using the PFGDSTE convection-compensated pulse sequence (the sequence of b without the read gradient G r), using probe 1 at a nominal temperature of 25 ° C. Signal intensities were, as noted above, quantified by integration, because of the large variations in linewidth caused

5

Fig. 11. Correlation between experimental diffusion coefficients obtained by fitting of experimental data to Eq. and values reported in the literature for the samples of , showing the ellipsoids of uncertainty.

<!-- image -->

by radiation damping. (This approach is effective for pure compounds, but in mixtures, where signal overlap is a potential problem, a more appropriate and equally effective solution is to reduce the flip angle of the first pulse .) The errors quoted for the experimental data are twice the standard error estimated by combining the standard error reported by the Levenberg-Marquardt nonlinear least squares fitting algorithm with the 1% estimated for the effects of uncertainty in sample temperature. The latter source of error dominates, since all the spectra had good S / N ratio. compares the experimental and literature data in a scatter plot, showing the ellipsoids of uncertainty.

## 5. Discussion

The experimental data presented demonstrate that it is possible to explain very satisfactorily the experimentally observed deviations in diffusional attenuation from the expected mono-exponential form of the Stejskal-Tanner equation. The measured deviations match very closely those predicted from an analysis of the measured variations in signal strength and pulsed field gradient with position z in the sample, providing reassurance that other contributions such as electrical nonlinearity and transverse variation of gradient strength are minor. A number of practical consequences follow. First, the effects of non-uniform field gradients on diffusion measurements can be corrected for to high accuracy by modifying the Stejskal-Tanner equation. This requires either very accurate measurements of the diffusional attenuation for a model calibrant, or, preferably, a full signal and gradient mapping, again using a suitable calibrant such as dilute HDO in D2O, followed by the calculation of two or more fitting coefficients for the re-parameterised Stejskal-Tanner equation. The mapping experiments can be quite demanding, but need only be performed once per probe and can be simplified by the use of whole echo transformation and absolute value display. Two methods for the re-parameterisation are in current use, that described by Damberg and co-workers and that described here. Both are based on the same physical principles and both give excellent results with the relatively mild gradient non-uniformity encountered in modern commercial pulsed field gradient probes, while the latter method also allows more severely nonlinear gradients to be catered for. The latter method appears to have been the more widely used to date, with numerous applications . Second, the ability to correct for the effects of non-uniform field gradients greatly reduces the difficulty of ensuring accurate calibration of diffusion measurements, removing (where, as is generally the case, the electrical linearity of the gradient system is good) the need for a separate calibration for each range of diffusion coefficient. Third, the systematic contributions to the estimated standard errors in diffusion coefficient found for typical commercial probes with mild gradient nonlinearity, such as probes b and c above, are greatly reduced, typically to a small fraction of a percent. As an important corollary, the resolution of DOSY experiments improves in proportion. Fourth, all NMR diffusion measurements show a systematic sensitivity to pulse width calibration that appears to have been neglected hitherto, but that can be controlled by careful calibration and/or conservative choice of pulse widths. Fifth, while the exact parameters needed for a modified Stejskal-Tanner equation depend both on the characteristics of the probe and on the particular pulse sequence used, it should be possible to calculate the necessary parameters for any pulse sequence given the results of a single mapping experiment. Sixth, correcting for the gradient non-uniformity can allow accurate measurements to be made using standard high resolution NMR probes, without the need for probes specifically dedicated to diffusion measurement; conversely, the limiting accuracy achievable using the latter may be improved.

## Acknowledgments

This work was generously supported by the EPSRC (Grants GR/ P01373, GR/S90751, EP/D05592X, EP/E057888 and EP/E05899X). M.A.C. and P.J.B. also thank Pfizer Global R&amp;D for CASE awards.

## References

- [1] E.O. Stejskal, J.E. Tanner, Spin diffusion measurements -spin echoes in presence of a time-dependent field gradient, J. Chem. Phys. 42 (1965) 288-292.
- [2] R. Mills, Self-diffusion in normal and heavy-water in range 1-45 degrees, J. Phys. Chem. 77 (1973) 685-688.
- [3] K.E. Price, L.H. Lucas, C.K. Larive, Analytical applications of NMR diffusion measurements, Anal. Bioanal. Chem. 378 (2004) 1405-1407.
- [4] B. Antalek, Using pulsed gradient spin echo NMR for chemical mixture analysis: how to obtain optimum results, Concepts Magn. Reson. 14 (2002) 225-258.
- [5] C.S. Johnson, Diffusion ordered nuclear magnetic resonance spectroscopy: principles and applications, Prog. Nucl. Magn. Reson. Spectrosc. 34 (1999) 203-256.
- [6] G.A. Morris, Diffusion-Ordered Spectroscopy (DOSY), in: D.M. Grant, R.K. Harris (Eds.), Encyclopedia of Nuclear Magnetic Resonance, John Wiley &amp; Sons Ltd., Chichester, 2002, pp. 35-44.
- [7] H. Barjat, G.A. Morris, S. Smart, A.G. Swanson, S.C.R. Williams, High-resolution diffusion-ordered 2D spectroscopy (HR-Dosy) - a new tool for the analysis of complex-mixtures, J. Magn. Reson. Ser. B 108 (1995) 170-172.
- [8] M.D. Pelta, G.A. Morris, M.J. Stchedroff, S.J. Hammond, A one-shot sequence for high-resolution diffusion-ordered spectroscopy, Magn. Reson. Chem. 40 (2002) S147-S152.
- [9] M.D. Pelta, H. Barjat, G.A. Morris, A.L. Davis, S.J. Hammond, Pulse sequences for high-resolution diffusion-ordered spectroscopy (HR-DOSY), Magn. Reson. Chem. 36 (1998) 706-714.
- [10] G.A. Morris, Reference deconvolution, in: D.M. Grant, R.K. Harris (Eds.), Encyclopedia of Nuclear Magnetic Resonance, John Wiley &amp; Sons Ltd., Chichester, 2002, pp. 125-131.
- [11] G.A. Morris, H. Barjat, T.J. Horne, Reference deconvolution methods, Prog. Nucl. Magn. Reson. Spectrosc. 31 (1997) 197-257.
- [12] A. Jerschow, N. Müller, Convection compensation in gradient enhanced nuclear magnetic resonance spectroscopy, J. Magn. Reson. 132 (1998) 13-18.
- [13] M. Nilsson, G.A. Morris, Improving pulse sequences for 3D DOSY: convection compensation, J. Magn. Reson. 177 (2005) 203-211.
- [14] A. Jerschow, N. Müller, Suppression of convection artifacts in stimulated-echo diffusion experiments. Double-stimulated-echo experiments, J. Magn. Reson. 125 (1997) 372-375.
- [15] M.A. Connell, A.L. Davis, A.M. Kenwright, G.A. Morris, NMR measurements of diffusion in concentrated samples: avoiding problems with radiation damping, Anal. Bioanal. Chem. 378 (2004) 1568-1573.
- [16] P. Hodge, P. Monvisade, G.A. Morris, I. Preece, A novel NMR method for screening soluble compound libraries, Chem. Commun. (2001) 239-240.
- [17] P. Damberg, J. Jarvet, A. Gräslund, Accurate measurement of translational diffusion coefficients: a practical method to account for nonlinear gradients, J. Magn. Reson. 148 (2001) 343-348.
- [18] A.R. Bilia, M.C. Bergonzi, F.F. Vincieri, P. Lo Nostro, G.A. Morris, A diffusionordered NMR spectroscopy study of the solubilization of artemisinin by octanoyl-6O -ascorbic acid micelles, J. Pharm. Sci. 91 (2002) 2265-2270.
- [19] M. Nilsson, I.F. Duarte, C. Almeida, I. Delgadillo, B.J. Goodfellow, A.M. Gil, G.A. Morris, High-resolution NMR and diffusion-ordered spectroscopy of port wine, J. Agric. Food. Chem. 52 (2004) 3736-3743.
- [20] M.J. Stchedroff, A.M. Kenwright, G.A. Morris, M. Nilsson, R.K. Harris, 2D and 3D DOSY methods for studying mixtures of oligomeric dimethylsiloxanes, Phys. Chem. Chem. Phys. 6 (2004) 3221-3227.
- [21] M. Nilsson, M.A. Connell, A.L. Davis, G.A. Morris, Multiexponential fitting of diffusion-ordered NMR data: practicalities and limitations, Anal. Chem. 78 (2006) 3040-3045.
- [22] M. Nilsson, G.A. Morris, Correction of systematic errors in CORE processing of DOSY data, Magn. Reson. Chem. 44 (2006) 655-660.
- [23] M. Nilsson, G.A. Morris, Improved DECRA processing of DOSY data: correcting for non-uniform field gradients, Magn. Reson. Chem. 45 (2007) 656-660.
- [24] M. Nilsson, G.A. Morris, Pure shift proton DOSY: diffusion-ordered H-1 spectra without multiplet structure, Chem. Commun. (2007) 933-935.
- [25] M. Nilsson, G.A. Morris, Speedy component resolution: an improved tool for processing diffusion-ordered spectroscopy data, Anal. Chem. 80 (2008) 37773782.
- [26] M. Mobli, M. Nilsson, A. Almond, The structural plasticity of heparan sulfate NA-domains and hence their role in mediating multivalent interactions is confirmed by high-accuracy N-15-NMR relaxation studies, Glycoconjug. J. 25 (2008) 401-414.
- [27] M. Holz, H. Weingärtner, Calibration in accurate spin-echo self-diffusion measurements using H-1 and less-common nuclei, J. Magn. Reson. 92 (1991) 115-125.
- [28] N.N. Yadav, A.M. Torres, W.S. Price, An improved approach to calibrating high magnetic field gradients for pulsed field gradient experiments, J. Magn. Reson. 194 (2008) 25-28.
- [29] M.L. Tillett, L.Y. Lian, T.J. Norwood, Practical aspects of the measurement of the diffusion of proteins in aqueous solution, J. Magn. Reson. 133 (1998) 379-384.
- [30] S.M. Zhang, Quantitative measurement of molecular diffusion coefficients by NMR spectroscopy, J. Am. Chem. Soc. 128 (2006) 4974-4975.
- [31] K. Hayamizu, W.S. Price, A new type of sample tube for reducing convection effects in PGSE-NMR measurements of self-diffusion coefficients of liquid samples, J. Magn. Reson. 167 (2004) 328-333.
- [32] F.D. Doty, G. Entzminger, Y.A. Yang, Magnetism in high-resolution NMR probe design. I: General methods, Concept Magn. Reson. 10 (1998) 133-156.
- [33] H. Kato, T. Saito, M. Nabeshima, K. Shimada, S. Kinugasa, Assessment of diffusion coefficients of general solvents by PFG-NMR: investigation of the sources error, J. Magn. Reson. 180 (2006) 266-273.
- [34] P. Stilbs, K. Paulsen, P.C. Griffiths, Global least-squares analysis of large, correlated spectral data sets: application to component-resolved FT-PGSE NMR spectroscopy, J. Phys. Chem. 100 (1996) 8180-8189.
- [35] P. Stilbs, K. Paulsen, Global least-squares analysis of large, correlated spectral data sets and application to chemical kinetics and time-resolved fluorescence, Rev. Sci. Instrum. 67 (1996) 4380-4386.
- [36] W.S. Price, P.W. Kuchel, Effect of nonrectangular field gradient pulses in the Stejskal and Tanner (diffusion) pulse sequence, J. Magn. Reson. 94 (1991) 133139.
- [37] H. Barjat, P.B. Chilvers, B.K. Fetler, T.J. Horne, G.A. Morris, A practical method for automated shimming with normal spectrometer hardware, J. Magn. Reson. 125 (1997) 197-201.
- [38] P.J. Bowyer, A.G. Swanson, G.A. Morris, Analyzing and correcting spectrometer temperature sensitivity, J. Magn. Reson. 152 (2001) 234-246.
- [39] N.M. Loening, J. Keeler, Measurement of convection and temperature profiles in liquid samples, J. Magn. Reson. 139 (1999) 334-341.
- [40] D.I. Hoult, NMR receiver - description and analysis of design, Prog. Nucl. Magn. Reson. Spectrosc. 12 (1978) 41-77.
- [41] K.R. Harris, H.N. Lam, E. Raedt, A.J. Easteal, W.E. Price, L.A. Woolf, The temperature and density dependences of the self-diffusion coefficient and the shear viscosity of liquid trichloromethane, Mol. Phys. 71 (1990) 1205-1221.
- [42] M. Holz, S.R. Heil, A. Sacco, Temperature-dependent self-diffusion coefficients of water and six selected molecular liquids for calibration in accurate H-1 NMR PFG measurements, Phys. Chem. Chem. Phys. 2 (2000) 4740-4742.
- [43] R. Mills, Intradiffusion and derived frictional coefficients for benzene and cyclohexane in their mixtures at 25 degrees, J. Phys. Chem. 69 (1965) 3116.