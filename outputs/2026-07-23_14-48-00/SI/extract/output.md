## SUPPORTING INFORMATION

Towards universal use of DOSY as a molar mass characterization tool: Temperature dependence investigations and a software tool to process diffusion coefficients

Igor W. F. Silva, a Alasdair McKay, b  Anna Sokolova c and Tanja Junkers *,a

a  Polymer Reaction Design group, School of Chemistry, Monash University, Clayton VIC 3800, Australia;

b  School of Chemistry, Monash University, Clayton VIC 3800, Australia;

c  ACNS, ANSTO, Lucas Heights, NSW 2234, Australia

## Contents

| 1. Materials ..................................................................................................................3   |
|------------------------------------------------------------------------------------------------------------------------------------|
| 2. Diffusion-ordered NMRspectroscopy (DOSY-NMR) procedure ..........................4                                              |
| 3. Temperature dependence of viscosity ...................................................................12                       |
| 4. Small Angle Neutron Scattering (SANS)..............................................................14                           |
| 4.1 Equations definition.............................................................................................14            |
| 4.2 SANS data collection procedure and analysis.....................................................16                             |
| References..................................................................................................................22     |

## 1. Materials

Polystyrene (PS) standards, obtained from PSS, were used to gather calibration curves in different temperatures. The molar mass range studied was 1200 to 280000 g ∙ mol -1 , Table S1 presents  all  materials  and  their M n, M w, M p  and Ð .  The  samples  were  prepared  in  a concentration of 2 mg ∙ mL -1 on toluened 8.

Table S1: Polystyrene standard in a molar mass range of 1200 to 280000 g ∙ mol -1 .

| Sample   |   M n (g ∙ mol -1 ) |   M w (g ∙ mol -1 ) |   M p (g ∙ mol -1 ) |    Ð |
|----------|---------------------|---------------------|---------------------|------|
| PS1200   |                1120 |                1220 |                1306 | 1.09 |
| PS3200   |                3350 |                3510 |                3500 | 1.05 |
| PS9k     |                8420 |                8670 |                8680 | 1.03 |
| PS18k    |               16900 |               17300 |               17600 | 1.03 |
| PS33k    |               32700 |               34000 |               34800 | 1.04 |
| PS62k    |               59300 |               62500 |               66000 | 1.05 |
| PS120k   |              120000 |              125000 |              130000 | 1.04 |
| PS280k   |              282000 |              294000 |              304000 | 1.04 |

## 2. Diffusion-ordered NMR spectroscopy (DOSY-NMR) procedure

The experiments were run in Bruker Neo nanobay NMR spectrometer with a 5 nm broadband BB-H/D probe operating at 400.14 MHz for 1 H with a ~50 G ∙ cm -1 z-gradient and a BCUII cooling unit. Samples were made up at 0.5 mL and placed in 5 mm NMR tubes. A reduced  volume  was  used  for  3  mm  NMR  tubes.  Measurements  were  conducted  in  10  K increments in the range 273-343 K. Sample were kept stationary (not rotating) throughout the measurement unless otherwise stated. The gas flow was set to 550 L ∙ h -1 to minimise convection artefacts. Samples were maintained at the desired temperature inside the magnet for at least 20 min for the sample to reach thermal equilibrium before any measurements were conducted. Measured temperature values from the thermocouple in the probehead were corrected utilising the temperature-dependent chemical shifts, of the OH group in 99.8% perdeuterated methanol. 1

The bipolar pulse longitudinal eddy current delay (ledbgp2s) pulse program or the double-stimulated-echo  (dstebpgp3s)  pulse  program  were  used, 2 with  a  smoothed  square shaped (SMSQ) pulse. 3 Experiments were performed as pseudo-2D with a linear ramping of the gradient from 2 to 98% of maximum intensity in 32 steps. For each step, 8 transients were acquired  following  8  dummy  transients.  The  diffusion  time, Δ (d20),  was  100  ms,  unless otherwise stated, the spoil gradient (p19) was set to 600 µs, the recycle delay (d1) was 3 s and the eddy current delay (d21) was 5 ms. The gradient pulse length, the δ /2 (p30), was optimized on a per-sample basis, see Table S2. i

The data were processed using Topspin 4.1.4 and the peak areas, I , were used to fit the  Stejskal-Tanner  formula,  Eq.  (1),  as  single-component  fits,  to  determine  the  diffusion coefficient, D , using Dynamics Center 2.8.3.

$$\frac { I } { I ( 0 ) } = e ^ { - D \gamma ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g ^ { 2 } \Delta ^ { \prime } }$$

As discussed in the main text, convection is caused by temperature gradients within the sample, thus leading to the overestimation of diffusion coefficients. 4  Methods have been proposed to minimise these effects, such as collecting data at ambient temperature without temperature  control  to  remove  pulsing  from  the  temperature  control  unit  that  can  induce convection. 5 Conducting the experiment with optimised flow rate of the VT gas, rotating the sample, utilising sapphire NMR tubes, utilising shaped or Shigemi tubes rather than regular NMR tubes, decreasing the sample size by employing smaller inner diameter NMR tubes, inserting a small capillary contain D2O to provide a physical barrier to convection flows, or using triaxial field gradients. 6-11 Alternatively, pulse sequences that are designed to compensate for the effects of flow on the signals measured can be employed. These sequences are typically designed to refocus the effects of a constant velocity of flow along a field gradient direction, usually  by  splitting  the  diffusion  weighting  sequence  element  into  two  symmetrical  halves generating equal and opposite flow effects, the so-called double-stimulated-echo experiment.

i Caution: care was taken such that the p30 setting did not exceed the manufacturer's recommendations in terms of the overall length of all gradients applied during a repetition period, as this may damage the NMR probe. This is particularly relevant for the dstebpgp3s pulse program. Please seek further guidance from your NMR specialist and instrument manufacturer, before undertaking these experiments.

The data discussed in the main text about the ledbpgp2s acquisition can be check in the  following  Figures.  Figure  S1  shows  the  viscosity-corrected  calibration  data  of  the ledbpgp2s pulse sequence of polystyrene standards at several temperatures. Figure S2 presents the 3D calibration of viscosity-corrected diffusion coefficients as a function of temperature and molar mass of polystyrene standards, same data acquired on Figure S1.

The methods applied to decrease convection effects in DOSY experiments: acquiring diffusion data whilst rotating the sample and using 3 mm NMR tubes (instead of 5 mm usual tubes).  Figure  S3  compares  the  molar  mass  estimation  curves  acquired  by  ledbpgp2s,  no rotation  of  the  sample  (S3a),  ledbpgp2s,  rotating  the  sample  (S3b),  ledbpgp2s,  no  rotation, using 3 mm NMR tubes (S3c) and dstebpgp3s, no rotation, using 5 mm NMR tubes (S3d). Figure S4 compares the viscosity-corrected calibration of diffusion coefficients determined via DOSY using ledbpgp2s and dstebpgp3s pulse programs for polystyrene standards at 293 K (20 °C).

Figure S5 compares the logarithmic DOSY signal intensities of the polymer signals against the square of gradient strength acquired by ledbpgp2s, no rotation of the sample (S5a), ledbpgp2s, rotating the sample (S5b), ledbpgp2s using 3 mm NMR tubes (S5c) and dstebpgp3s no rotation and using 5 mm NMR tubes (S5d) in temperatures, where convection artefacts are present in the diffusion data.

log (D/m2.s-1+ η/mPa·s)

Figure S1. Viscosity-corrected calibration data of polystyrene standards at several temperatures measured using ledbpgp2s pulse sequence.

<!-- image -->

Figure S2. 3D calibration fit of viscosity-corrected diffusion coefficients (obtained using ledbpgp2s) as a function of temperature and molar mass of polystyrene standards.

<!-- image -->

■

Figure S3. Calibration curves between molar mass and diffusion coefficient acquired by the using the following conditions: ledbpgp2s, no rotation of the sample (a), ledbpgp2s, rotating the sample (b), ledbpgp2s, no rotation, 3 mm NMR tubes (c) and dstebpgp3s, no rotation, 5 mm NMR tubes (d). Data was acquired in temperatures between 273 and 343 K (0 and 70 °C).

<!-- image -->

Figure S4. Viscosity-corrected calibration of diffusion coefficients determined via DOSY (acquired by ledbpgp2s (grey) and dstebpgp3s (red) pulse programs) for polystyrene standards at 293 K (20 °C).

<!-- image -->

Figure S5. Logarithmic DOSY signal intensities of the polymer signals against the square of gradient strength acquired by ledbpgp2s, no rotation of the sample (a), ledbpgp2s rotating the sample (b), ledbpgp2s using 3 mm NMR tubes (c) and dstebpgp3s no rotation and using 5 mm NMR tubes (d) in temperatures, which demonstrate convection artefacts.

<!-- image -->

Table S2. Gradient pulse lengths ( δ /2; p30, µs) for standard PS samples in different temperatures ( ledbpgp2s ).

| Samples   | 273 K   | 283 K   | 288 K   | 293 K   | 295 K   |   298 K |   301 K |   303 K |   308 K |   313 K |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| PS1200    | 800     | 800     | 800     | 800     | 800     |     800 |    1000 |    1000 |     800 |     800 |
| PS3200    | 800     | 1000    | 1000    | 1000    | 1000    |    1000 |    1000 |    1000 |     800 |     800 |
| PS9k      | 1000    | 1000    | 1200    | 1200    | 1200    |    1000 |    1000 |    1000 |     800 |     800 |
| PS18k     | 1000    | 1000    | 1200    | 1400    | 1400    |    1200 |    1200 |    1200 |    1000 |    1000 |
| PS33k     | -       | 1200    | 1400    | 1400    | 1400    |    1400 |    1200 |    1200 |    1000 |    1000 |
| PS62k     | -       | -       | -       | 1600    | 1600    |    1400 |    1200 |    1200 |    1000 |    1000 |
| PS120k    | -       | -       | -       | -       | 1600    |    1600 |    1600 |    1600 |    1200 |    1200 |
| PS280k    | -       | -       | -       | -       | -       |    1600 |    1600 |    1600 |    1200 |    1200 |

| Samples   |   273 K |   283 K |   293 K |   303 K |   313 K |   323 K |   333 K |   343 K |
|-----------|---------|---------|---------|---------|---------|---------|---------|---------|
| PS1200    |     900 |     900 |     900 |     900 |     900 |     800 |     800 |     800 |
| PS3200    |    1000 |    1000 |    1000 |    1000 |    1000 |    1000 |    1000 |    1000 |
| PS9k      |    1600 |    1600 |    2000 |    1600 |    1600 |    1600 |    1600 |    1400 |
| PS18k     |    1600 |    1600 |    2000 |    1800 |    1800 |    1800 |    1600 |    1600 |
| PS33k     |    1600 |    1600 |    2000 |    2000 |    2000 |    1800 |    1600 |    1600 |
| PS62k     |    1600 |    2000 |    2000 |    2000 |    2000 |    1800 |    1800 |    1600 |
| PS120k    |    2000 |    2200 |    2200 |    2200 |    2200 |    2000 |    2000 |    2000 |
| PS280k    |    2200 |    2200 |    2200 |    2200 |    2200 |    2200 |    2200 |    2200 |

## 3. Temperature dependence of viscosity

Figure S6 shows temperature dependence data of viscosity 12 (solid squares) used to build a third-order polynomial fitting function of η ( T ) ( r 2 = 0.99997). The values used in this work (open squares) were taken from this fitting function. The exact values of η used for each temperature can be checked in Table S4 (on the right).

Figure S6. Viscosity ( η )  of  toluene in the function of temperature (T), where solid squares are data from the reference 12 , open squares are the temperatures used in DOSY-NMR, and the red line is 3-order polynomial fitting of the reference data.

<!-- image -->

Table S4. Values of viscosity ( η ) and temperature (T) from the reference 12 and used in this work.

| Reference 12   | Reference 12   | Values for this work   | Values for this work   |
|----------------|----------------|------------------------|------------------------|
| T (K)          | η ( mPa∙s )    | T (K)                  | η ( mPa∙s )            |
| 270            | 0.8087         | 273                    | 0.7738                 |
| 275            | 0.7508         | 283                    | 0.6740                 |
| 280            | 0.6994         | 288                    | 0.6301                 |
| 285            | 0.6535         | 293                    | 0.5901                 |
| 290            | 0.6124         | 295                    | 0.5752                 |
| 295            | 0.5753         | 298                    | 0.5541                 |
| 300            | 0.5418         | 301                    | 0.5344                 |
| 305            | 0.5113         | 303                    | 0.5220                 |
| 310            | 0.4835         | 308                    | 0.4939                 |
| 315            | 0.4581         | 313                    | 0.4698                 |
| 320            | 0.4348         | 323                    | 0.4207                 |
| 325            | 0.4133         | 333                    | 0.3819                 |
| 330            | 0.3935         | 343                    | 0.3467                 |
| 335            | 0.3751         | -                      | -                      |
| 340            | 0.3581         | -                      | -                      |
| 345            | 0.3423         | -                      | -                      |

## 4. Small Angle Neutron Scattering (SANS)

## 4.1 Equations definition

Scheme S1 shows neutrons, with a wavelength λ ,  interacting  with  the  sample  and scattering from it. The incident neutrons on the sample have a momentum 𝑘𝑘 𝚤𝚤 � � �⃗ and the scattered neutrons  by  the  sample  have  a  momentum 𝑘𝑘 𝑓𝑓 � � � � ⃗ .  The  angle  between  the  two  vectors  is  the scattering angle, 2 θ . 13

Scheme S1. Definition of the momentum transfer ( 𝑞𝑞 ⃗ ) in Small-Angle Neutron Scattering measurements.

<!-- image -->

Considering only elastic scattering, it is possible to assume:

$$\| \overrightarrow { k _ { \iota } } \| = \| \overrightarrow { k _ { f } } \| = \frac { 2 \pi } { \lambda }$$

SANS data are acquired as a function of the momentum transfer:

$$\vec { q } = \overrightarrow { k _ { f } } - \overrightarrow { k _ { l } }$$

,which the magnitude of the momentum transfer is defined by:

$$\| \vec { q } \| = q = \frac { 4 \pi } { \lambda } \sin \left ( \frac { 2 \theta } { 2 } \right )$$

The scattering intensity of the polymer coils was modelled (' poly\_gauss\_coil ' from SASView) via 14,15 :

$$I ( q ) = \phi _ { p } \cdot V _ { p } \cdot \Delta S L D ^ { 2 } \cdot \ P ( q ) + I _ { b k g }$$

Where I coil( q )  is  the  scattering  intensity  of  a  polymer  coil  with  excluded  volume effects, I bkg  the  incoherent  background,  and ϕ p  and V p  the  volume  fraction  and  molecular volume of the polymer, respectively. V p can be defined as 𝑉𝑉 𝑝𝑝 = 𝑀𝑀 𝑁𝑁𝐴𝐴 𝛿𝛿 , where M is the molar mass of the polymer, N A is the Avogadro's Number, and δ is the bulk density of the polymer. The polymer coil form factor 16 P ( q ) is described as:

$$P ( q ) = 2 \left [ \frac { ( 1 + U Z ) ^ { - 1 / U } + Z - 1 } { ( U + 1 ) Z ^ { 2 } } \right ]$$

where

$$Z = \frac { ( q R _ { g } ) ^ { 2 } } { 1 + 2 U }$$

$$U = \mathfrak { E } - 1$$

The relation between the scattering intensity and the characteristic of a particle is also given by the Fourier transformation 17 :

$$I ( q ) = 4 \pi \int _ { 0 } ^ { \infty } p ( r ) \frac { \sin ( q r ) } { q r } \, d r$$

Where the distribution of interatomic distances, p ( r ), is calculated as 𝑝𝑝 ( 𝑟𝑟 ) = 𝛾𝛾 ( 𝑟𝑟 ) ∙ 𝑟𝑟 2 where γ ( r ) is a spherically averaged autocorrelation function of the excess scattering density. The distribution becomes zero at r = 0 and r = D max.

$$p ( r ) = \frac { r ^ { 2 } } { 2 \pi ^ { 2 } } \int _ { 0 } ^ { \infty } q ^ { 2 } I ( q ) \, \frac { \sin q r } { q r } \, \text {d} q$$

R g has been calculated using Primus software using the following relation:

$$R _ { g } ^ { 2 } = \frac { \int _ { V } \, p ( r ) r ^ { 2 } d r } { \int _ { V } \, p ( r ) d r }$$

## 4.2 SANS data collection procedure and analysis

The  SANS  experiments  were  performed  in  the  Bilby  SANS  instrument  at  the Australian  Centre  for  Neutron  Scattering  (ACNS),  ANSTO.  The  temperatures  used  in  the experiments were of 279, 283, 292, 295, 298 and 308 K. The polymer samples used for this experiment  were  the  PS9k,  PS33k,  PS62k  and  PS120k  (see  Table  S1).  The  samples  were carried out on toluene-d8 at the concentration of 2 mg ∙ mL -1 .  The measurement time for the polymers solutions was 3600 s, and that for the toluene of the matching temperatures was 1500 s. Instrument has been set-up in a time-of-flight mode. Data has been reduced on wavelength interval from 4 Å to 12 Å covering q-range from 0.003 Å -1 to -0.52 Å -1 . Rear detector has been placed 18 m away from the samples, vertical curtains were 1 m away, and vertical ones are 2 m, with 0.3 m, 0.35 m, 0.075 m and 0.15 m separation from the beam for the left, right, top and vertical  ones,  correspondingly.  Backgrounds  has  been  considered  and  data  placed  on  the absolute  scale  using  standard  Bilby  procedures,  implemented  in  Mantid 18,19 software. Scattering from the solvent has been carefully subtracted.

The software used to process the data were the SASview 5.0.6 (https://www.sasview.org) 20 . The data were fitted using ' poly\_gauss\_coil ' model. The dispersity was adjusted to the values of Table S1, and the scale was kept constant for each given polymer. To assess the overall structural  properties,  Primus 21 software  from  ATSAS  suit  has  been  used  to  calculate p ( r ) functions  and R g  values  based  on p ( r ),  and  also  create  Kratky  plots  to  estimate  level  of folding/unfolding for each polymer.

Figure S7. SANS data of standard polystyrene (average molar mass of 9 (a), 33 (b), 62 (c), and 120 (d) kg ∙mol -1 ) in  different  temperatures.  The  squares  represent  the  experimental  data  and  the  lines  represent  the  Gaussian polymer coil fits for each temperature.

<!-- image -->

Figure  S8. SANS  data  of  standard  polystyrene  (average  molar  mass  of  9,  33,  62,  and  120  kg ∙mol -1 )  at  the temperatures of 279 (a), 295 (b), and 308 (c) K. The squares represent the experimental data and the lines represent the Gaussian polymer coil fits for each temperature.

<!-- image -->

Figure S9. Kratky plots of SANS data of standard polystyrene (average molar mass of 9, 33, 62, and 120 kg ∙mol -1 ) at the temperatures of 279 (a), 295 (b), and 308 (c) K. The squares represent the experimental data and the lines represent the Gaussian polymer coil fits for each temperature.

<!-- image -->

Figure S10. p(r) curves of SANS data of standard polystyrene (average molar mass of 33 (a), 62 (b), and 120 (c) kg ∙mol -1 ) in different temperatures.

<!-- image -->

Figure S11. p(r) curves of SANS data of standard polystyrene (average molar mass of 33, 62, and 120 kg ∙mol -1 ) at the temperatures of 279 (a), 295 (b), and 308 (c) K.

<!-- image -->

## References

- 1  A. L. Van Geet, Anal. Chem. , 1968, 40 , 2227-2229.
- 2  S. J. Gibbs and C. S. Johnson, Journal of Magnetic Resonance (1969) , 1991, 93 , 395-402.
- 3,  DOI:10.1002/cmr.a.21223.
- 4  G. H. Sørland and D. Aksnes, Magnetic Resonance in Chemistry , 2002, 40 , S139-S146.
- 5  P. Groves, Polym. Chem. , 2017, 8 , 6700-6708.
- 6  I. Swan, M. Reid, P. W. A. Howe, M. A. Connell, M. Nilsson, M. A. Moore and G. A. Morris, Journal of Magnetic Resonance , 2015, 252 , 120-129.
- 7  P. Kiraly, I. Swan, M. Nilsson and G. A. Morris, Journal of Magnetic Resonance ,  2016, 270 , 24-30.
- 8  C.  R.  Pope,  M.  Kar,  D.  R.  MacFarlane,  M.  Armand,  M.  Forsyth  and  L.  A.  O'Dell, ChemPhysChem , 2016, 17 , 3187-3195.
- 9  K. Hayamizu and W. S. Price, Journal of Magnetic Resonance , 2004, 167 , 328-333.
- 10  N. Esturau, F. Sánchez-Ferrando, J. A. Gavin, C. Roumestand, M.-A. Delsuc and T. Parella, Journal of Magnetic Resonance , 2001, 153 , 48-55.
- 11  J. Lounila, K. Oikarinen, P. Ingman and J. Jokisaari, Journal of Magnetic Resonance, Series A , 1996, 118 , 50-54.
- 12  F. J. V. Santos, C. A. Nieto De Castro, J. H. Dymond, N. K. Dalaouti, M. J. Assael and A. Nagashima, Journal of Physical and Chemical Reference Data , 2006, 35 , 1-8.
- 13  W. T. Heller, Biomolecules , 2022, 12 , 1591.
- 14  P. Debye and A. M. Bueche, Journal of Applied Physics , 2004, 20 , 518-525.
- 15  A. Guinier, G. Fournet, C. B. Walker and G. H. Vineyard, Physics Today , 1956, 9 , 38-39.
- 16  B. Hammouda, in Polymer Characteristics , Springer, Berlin, Heidelberg, 1993, pp. 87-133.
- 17  O. Glatter, J Appl Cryst , 1977, 10 , 415-421.
- 18  Mantid Project, Mantid: Manipulation and Analysis Toolkit for Instrument Data 2013.
- 19  O. Arnold, J. C. Bilheux, J. M. Borreguero, A. Buts, S. I. Campbell, L. Chapon, M. Doucet, N. Draper, R. Ferraz Leal, M. A. Gigg, V. E. Lynch, A. Markvardsen, D. J. Mikkelson, R. L. Mikkelson, R. Miller, K. Palmen, P. Parker, G. Passos, T. G. Perring, P. F. Peterson, S. Ren, M. A. Reuter, A. T. Savici, J. W. Taylor, R. J. Taylor, R. Tolchenov, W. Zhou and J. Zikovsky, Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment , 2014, 764 , 156-166.
- 20  NSF project, SasView.
- 21  K. Manalastas-Cantos, P. V. Konarev, N. R. Hajizadeh, A. G. Kikhney, M. V. Petoukhov,
- D. S. Molodenskiy, A. Panjkovich, H. D. T. Mertens, A. Gruzinov, C. Borges, C. M. Jeffries,
- D. I. Svergun and D. Franke, J Appl Cryst , 2021, 54 , 343-355.