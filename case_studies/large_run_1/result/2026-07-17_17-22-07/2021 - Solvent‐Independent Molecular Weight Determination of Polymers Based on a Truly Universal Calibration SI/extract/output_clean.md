<!-- image -->

## Supporting Information

## Solvent-Independent Molecular Weight Determination of Polymers Based on a Truly Universal Calibration

P.-J. Voorter, A. McKay, J. Dai, O. Paravagna, N. R. Cameron, T. Junkers*

## Table of Contents

## Experimental Procedures

## Materials

All components as well as reagents and solvents were used as received without further purifications, unless stated otherwise. Benzened6 (99.6%), CDCl3 (99.8%), D2O (99.9%) and methanol-d4 (99.8%) are obtained from Merck. Acetone-d6 (99.9%), toluene-d8 (99.5%), tetrahydrofuran-d8  and  acetonitrile-d3 (99.8%)  are  obtained  from  Cambridge  Isotope  Laboratories.  Polystyrene  (PS) standards  are purchased from PSS. The following molecular weights were used: 1200 g/mol, 3200 g/mol, 9000 g/mol, 18000 g/mol, 33000 g/mol, 62000 g/mol. The following molecular weights for poly(ethylene glycol) (PEG) were used: 1960 g/mol , 3020 g/mol, 6690 g/mol, 12300 g/mol, 26100 g/mol and 44000 g/mol .

## NMR experiments

All NMR tubes were dried in an oven at 130  C overnight in advance. The polystyrene standards were prepared with 1 mg polystyrene and 1 mL of a deuterated solvent (benzene-d6, chloroform-d, acetone-d6, toluene-d8 and tetrahydrofuran-d8). All experiments were run without spinning to avoid convection.  1 H DOSY NMR spectra were recorded at 298 K with an air flow of 400 L h -1  on a Bruker Avance III nanobay NMR spectrometer equipped with a 9.4 T magnet, GAB/2 gradient amplifier and 5 mm BBFO probe with z-gradient coil with maximum gradient strength of 50 G cm -1 , operating at 400.20 MHz ( 1 H).

The standard Bruker pulse program, ledbpgp2s, employing a stimulated echo sequence with longitudinal eddy current delay and 2 spoil gradients was utilized. Pulse gradients were used with a total duration of 5-10 ms. Gradient recovery delays were 2 μs. The diffusion time is 200 ms. The number of gradient steps was set to be 12. Bruker software, TopSpin 4.1.3 and Dynamics Center 2.7.3, were used for data acquisition and processing.

## Results and Discussion

## A practical guide for measuring diffusion coefficients via DOSY

For the preparation of a DOSY measurement, a traditional 5mm NMR tube can be used, filled with 1 mL of the desired deuterated solvent containing roughly 1 mg of the sample. Lower quantities will lead to increased noise ratios and hence increased errors in the deduced diffusion coefficients. Higher concentration can lead to an underestimation of the diffusion coefficient due to hindered diffusion of macromolecules. Hence, ideally a concentration series is carried out to determine the optimal sample concentration from which on the obtained diffusion coefficient remains constant, and hence can be assumed to be accurate. If lower concentration that 1 mg/mL are required, smaller diameter sample tubes can be used to compensate.

(Please note the importance of using the same concentrations as used here to assure the correct use of the calibration curve)

Before starting the actual DOSY 2D experiment, a regular proton spectrum is taken to identify if the characteristic polymer peaks are clearly identifiable. The DOSY variables of every sample have to be tested, depending on the size and the solvent used. The main variables to focus on are the diffusion delay time (Δ) and the diffusion gradient pulse length (δ). Smaller faster-diffusing polymers need less  time  to  diffuse  and  therefore  are  associated  with  a  smaller  Δ.  δ  is  also  increased  with  the  size  of  the  polymer.  A  DOSY  2D experiment consists out of a series of spectra under variation of the gradient pulse. Every gradient pulse exhibits different degrees of the so-called corkscrew effect. A larger gradient pulse creates less aligned magnetizations which therefore yields less signal that can be detected. A good DOSY 2D experiment thus needs a well-fitted attenuation of these different gradient pulses. This fit is important to obtain the correct diffusion coefficient out of all the different segments (most common 32 segments). Two separate experiments are measured with the set gradient pulse at minimum (2%) and maximum (98%) gradient strength. The processed data is overlapped to judge if the parameters (Δ &amp; δ) chosen are sufficient to provide the 95-98% signal loss expected during the DOSY 2D experiment. After this test is done, the DOSY experiment can be started.

## Step for step protocol - poly(styrene)

Following is the protocol followed in how the calibration curves are created. The sample of polystyrene with a molecular weight of 18.000 g/mol dissolved in chloroform was chosen at random. The thought process for every polystyrene sample is the same. First a  1 H NMR spectrum is taken an analysed using Topspin and Dynamics Center.

1H NMR spectrum and DOSY spectrum of polystyrene reaction mixture Looking at the DOSY spectrum, as expected the diffusion coefficients obtained from all the different peaks are aligned and are in the same range. It was chosen to follow the peaks of the aromatic ring to be consistent in all the measurements to make the calibration curve. It was also noticed that the solvent peak, in this case CDCl3, was observed with a much higher diffusion coefficient which was expected.

Figure 1 .  1 H NMR spectrum of 18000 g  mol -1 poly(styrene) in CDCl3

<!-- image -->

<!-- image -->

Figure 2. DOSY spectrum of 18000 g  mol -1  poly(styrene) in CDCl3

<!-- image -->

Dynamics Center was used to analyse the DOSY spectrum. Following the peak of the aromatic ring in styrene at 6.6 ppm. The following values are obtained:

Table 1. Diffusion coefficient and error of 18000 g  mol -1 poly(styrene) in CDCl3

| D /m 2  s -1   | Error   |
|-----------------|---------|

To create the curves, the logarithm is taken of the diffusion and the molecular weight that is measured. To calculate the error on the logarithmic scale a simple mathematic calculation is done:

$$E r r o r _ { g r a p h } = \log ( D + e r r o r ) - \log ( D )$$

After the calculation, this gives the following values that are used in the graphs:

Table 2. Logarithm of D of 18000 g  mol -1 poly(styrene) in CDCl3 and calculated error

| log( D /m 2  s -   |   log( M / g  mol -1 ) |   Error |
|---------------------|-------------------------|---------|
| 1 )                 |                         |         |
| -9.91               |                    4.26 |    0.04 |

These values can be obtained for all the different molecular weights. These data points will have a linear relationship. The next step is to  take  viscosity  into  account  for  the  diffusion.  Looking  at  the Stokes-Einstein  equation we see the following relationship between diffusion ( D ), hydrodynamic radius (molecular weight, rH ) and viscosity (  ):

$$D = \frac { k _ { B } T } { 6 \pi \eta r _ { H } }$$

There is an inverse relationship between the diffusion and the viscosity. To create the diffusion calibration curves that are independent from the viscosity, and therefore to a big extend the solvent, are created by multiplying the viscosity by the diffusion obtained via the DOSY experiment.

$$D _ { v i s c o s i t y \ c a l i b r a t e d } = D \cdot \eta$$

The viscosity of chloroform is 0.563 mPa  s at 25  C. The logarithm can be taken from the viscosity independent diffusion coefficient. The logarithmic of the molecular weight stays the same and the error needs to be recalculated using the above formula.

Table 3. Logarithm of D (viscosity) of 18000 g  mol -1 poly(styrene) in CDCl3 with error

|   log( D /m 2  s -1 ) + log( / mPa  s) | log( M / g  mol -1 ) Error   |
|------------------------------------------|-------------------------------|
|                                   -10.02 | 4.26 0.07                     |

These values can be obtained for all the different molecular weights. These data points will also have a linear relationship that overlap with data obtained from other solvents.

## Average calibration curve

Using the values obtained from all the different molecular weights and different solvents, an average calibration curve can be obtained. This is possible because viscosity is now taking into account into the calculations. b' and v are given in table.

Table 4. b' and v values for the average calibration curve of poly(styrene)

| b' /m 2  s -1   | v   |
|------------------|-----|

Because this calibration curve is created using all the data from the different solvents, this gives the perfect estimation what a universal calibration would look like. The next graphs show the variation between all the data points obtained with the different solvents and the average calibration curve. The deviation between the average and the data points are 15% or lower. Therefore, this can be seen as an accurate calibration, especially in comparison with deviations observed in SEC.

Figure 3. Average calibration curve of poly(styrene)

<!-- image -->

Figure 4. Difference data points with poly(styrene) average calibration curve

<!-- image -->

Step for step protocol - poly(ethylene glycol)

The  protocols  for  poly(styrene)  and  poly(ethylene  glycol)  are  identical  but  for  completion  this  is  also  showed.  The  sample  of poly(ethylene glycol) with a molecular weight of 12.300 g/mol dissolved in D2O was chosen at random. First a  1 H NMR spectrum is taken an analysed using Topspin, the dosy spectrum is analysed with Dynamics Center.

1 H NMR spectra and DOSY spectrum of poly(ethylene glycol) reaction mixture The backbone of poly(ethylene glycol) will be used to follow the change of diffusion with changing the molecular weight. The solvent peak, in this case D2O, is again observed with a much a higher diffusion coefficient. Using Dynamics Center, the diffusion coefficient and error were obtained. Using the same formulas as with polystyrene all the needed values are obtained.

Figure 4. 1 H NMR spectrum of 12300 g  mol -1 poly(ethylene glycol) in D2O

<!-- image -->

Figure 5. DOSY spectrum of 12300 g  mol -1  poly(ethylene glycol) in D2O

<!-- image -->

Table 5. All variables of 12300 g  mol -1 poly(ethylene glycol)

| D /m 2  s -1                          | Error                 |       |
|----------------------------------------|-----------------------|-------|
| 5.91 E-11                              | 2.57E-12              |       |
| log( D /m 2  s -1 )                   | log( M / g  mol -1 ) | Error |
| -10.23                                 | 4.09                  | 0.02  |
| log( D /m 2  s -1 ) + log( / mPa  s) | log( M / g  mol -1 ) | Error |
| -10.13                                 | 4.09                  | 0.02  |

## Average calibration curve

Same as with polystyrene, using all the values from all the different molecular weights and different solvents an average calibration can be obtained.

Table 4. b' and v values for the average calibration curve of poly(ethylene glycol)

|   b' /m 2  s -1 |       v |
|------------------|---------|
|           -8.327 | -0.4466 |

Figure 6. Average calibration curve of poly(ethylene glycol)

<!-- image -->

Again, a comparison can be made with collected data points and the created average calibration curve. It can be seen that the difference for the majority of the samples doesn't go over 10%. Therefore, this can be seen as an accurate calibration.

Figure 7. Difference data points with poly(ethylene glycol) average calibration curve

<!-- image -->

## Comparison with literature

The accuracy of the data was checked against data found in literature that worked with the same range of molecular weights as in this work. This is important because diffusion is related to hydrodynamic radius. It is often seen that for example coiling is very different for small or large molecular weights, which can lead to inconsistent results.

## Poly(styrene)

A paper published by Grubbs and coworkers in Macromolecules (DOI: 10.1021/ma301666x) was used in comparison with our data. An comparable set of molecular weights is important, therefore we chose to measure more samples up to 560.000 g/mol top cover the same range.

Figure 8 . Comparison calibration curve for poly(styrene) in benzene-d6 and literature

<!-- image -->

## Poly(ethylene glycol)

A paper published by Waggoner et al. in Macromolecules (DOI: 10.1021/ma00112a010) was used in comparison with the poly(ethylene glycol) data. Again, to compare results it is important to have comparable molecular weights. Therefore the range of 2960 g/mol to 15100 g/mol is used. Using this new range, a new curve and error margin was fitted for Waggoner.

Table 7. Logarithm of D (viscosity) of poly(ethylene glycol) in D2O with error, Waggoner

|   b' /m 2  s -1 |       v |   Error |
|------------------|---------|---------|
|           -8.391 | -0.4737 | -0.3458 |

Figure 9. Comparison calibration curve for poly(ethylene glycol) in D2O and literature

<!-- image -->

## Viscosity of solvents (25  C)

Table 8. Viscosities of used deuterated solvents

| Solvent             |    (mPa  s) |
|---------------------|---------------|
| benzene-d 6         |        0.6076 |
| CDCl 3              |         0.563 |
| D 2 O               |        1.2314 |
| methanol-d 4        |         0.543 |
| acetone-d 6         |         0.295 |
| toluene-d 8         |          0.56 |
| tetrahydrofuran-d 8 |          0.48 |
| acetonitrile-d 3    |         0.343 |

## Author Contributions

The manuscript was written through contributions of all authors. PJV was responsible for conducting all experiments. TJ conceptualized the work and wrote the first draft of the manuscript. All authors have given approval to the final version of the manuscript.