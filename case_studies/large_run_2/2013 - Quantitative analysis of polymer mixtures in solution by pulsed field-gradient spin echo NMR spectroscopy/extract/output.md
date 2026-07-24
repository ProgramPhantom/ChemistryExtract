<!-- image -->

Contents lists available at SciVerse ScienceDirect

## Journal of Magnetic Resonance

j o u r n a l homepage: www.elsevier.com/locate/jmr

<!-- image -->

## Quantitative analysis of polymer mixtures in solution by pulsed field-gradient spin echo NMR spectroscopy

Luk Van Lokeren a,c , Hanen Ben Sassi a , Guy Van Assche c , François Ribot a,b, ⇑

- a UPMC, Chimie de la Matière Condensée de Paris (UMR 7574), Collège de France, 11, Place Marcelin Berthelot, 75231 Paris cedex 05, France
- b CNRS, Chimie de la Matière Condensée de Paris (UMR 7574), Collège de France, 11, Place Marcelin Berthelot, 75231 Paris cedex 05, France
- c Vrije Universiteit Brussel, Department of Materials and Chemistry, Research Unit Physical Chemistry &amp; Polymer Science, Pleinlaan 2, 1050 Brussel, Belgium

## a r t i c l e i n f o

Article history: Received 18 November 2012 Revised 5 March 2013 Available online 15 March 2013

## Keywords:

Pulsed Field-Gradient Spin Echo (PGSE) NMR Double stimulated echo (DSTE)

Mixture analysis Diffusion Relaxation Polystyrene Quantification

## 1. Introduction

Pulsed Field-Gradient Spin Echo NMR spectroscopy (PGSE NMR) [1-4] has become a popular technique to investigate species in solution according to their diffusive behaviour. The growing application of PGSE NMR to a wide variety of systems, like nanoparticles [5,6], micelles [7,8], and both natural (proteins [9], DNA [10]) and synthetic [11] polymer systems, illustrates its high potential. The additional resolution in the diffusion domain, together with the high resolution in the spectral domain makes PGSE NMR a powerful tool to analyze complex mixtures. Moreover, as an estimate of the molecular weight can be obtained from the diffusion coefficient [12,13], PGSE NMR can result in a virtual and molecular weight based separation of the mixture compounds in the diffusion domain and simultaneously provide detailed structural information in the spectral domain. It is especially valuable for the in situ investigation of reaction mixtures [14,15], chemical equilibria [16-18], and surface chemistry [19,20], where the real separation of the different compo-

⇑ Corresponding author. CMCP (UMR 7574), Collège de France, 11, Place Marcelin Berthelot, 75231 Paris cedex 05, France. Fax: +33 1 4427 1504.

E-mail address:

[francois.ribot@upmc.fr (F. Ribot).](mailto:francois.ribot@upmc.fr)

## a b s t r a c t

Pulsed Field-Gradient Spin Echo (PGSE) NMR, which associates to a spectral dimension the measure of diffusion coefficients, is a convenient technique for mixture analysis. Unfortunately, because of relaxation, the quantification of mixtures by PGSE NMR is far from straightforward for mixtures with strong spectral overlap. Antalek (J. Am. Chem. Soc. 128 (2006) 8402-8403) proposed a quantification strategy based on DECRA analysis and extrapolation to zero of the diffusion delay. More recently, Barrère et al. (J. Magn. Reson. 216 (2012) 201-208) presented a new strategy based also on DECRA and on the renormalization of the intensities using estimates of the T 1 and T 2 relaxation times. Here we report an alternative quantification approach in which the fractions are obtained by analyzing the PGSE attenuation profile with a general Stejskal-Tanner equation that explicitly includes the relaxation effects. The required values of T 1 and T 2 relaxation times are either independently measured with conventional sequences or determined, along with the fractions and the diffusion coefficients, from the simultaneous analysis of up to 6 PGSE data sets recorded with different diffusion delays. This method yields errors lower than 3% for the fractions, even for complete spectral overlap, as demonstrated on model binary and ternary mixtures of polystyrene in the case of a convection compensating double stimulated echo (DSTE) sequence.

Ó 2013 Elsevier Inc. All rights reserved.

nents present in the mixture might modify the system. PGSE NMR can be a worthy alternative to High Performance Liquid Chromatography (HPLC) or Gel Permeation Chromatography (GPC), since PGSE NMR allows to determine, in optimal experimental conditions, the molecular weight [21,22] or the polydispersity [23] of a polymer.

However, the applicability of PGSE NMR in analytical science totally depends on the separation level and thus on the accuracy of the diffusion coefficients obtained [24-26]. For systems with only single-component decays, very small errors are observed on the diffusion coefficients when optimized experimental conditions are used. For systems containing single-component and multicomponent decays, diffusion coefficients can generally be obtained with good accuracy from multivariate analyses that take profit of the results extracted from single-component decays to analyze the decays of overlapping signals. However, when the spectrum only contains partially or even totally overlapping resonance peaks (i.e. all the attenuation profiles contain more than one component), considerable errors on diffusion coefficients are reported. As a consequence lots of guidelines to obtain optimal results have been published in literature throughout the years [25,26], either through optimization of the experimental conditions, through enhancement of the processing algorithm or through increase of the separation limit (e.g. lanthanide shift reagents [27] and matrixassisted diffusion-ordered spectroscopy [28]).

Although the requirements for optimal discrimination between diffusion coefficients are rarely achieved in solutions of small molecules, they are easily met while probing ligands bound on the surface of a nanoparticle and the ones free in solution [29] or monitoring monomer and polymer fractions during a chain growth polymerization.

Besides the separation along the diffusion axis, the fractions of the mixture components are also of interest in analytical science. Unfortunately, since PGSE NMR is an echo-based technique, its quantitative analysis is not straightforward [30]. Indeed, relaxation during the diffusion delay contributes to the echo intensity. Of course, the relaxation effects are only problematic for strongly overlapping spectra (a case encountered for lots of polymer systems), because as soon as a component shows an isolated well-resolved NMR signal, integration of its 1D spectrum yields a simple and direct measurement of its fraction in the mixture [1,25].

In 2006, Antalek published the quantitative direct exponential curve resolution algorithm (qDECRA) as a methodology to take into account relaxation effects in PGSE NMR, aiming to obtain the correct component fractions by extrapolation towards a zero diffusion delay [30]. In Antalek's approach, the times during which the magnetization is along the z axis or in the xy plane are simultaneously varied and kept proportional. Accordingly, such a methodology can introduce errors related to homonuclear scalar couplings evolution when the time spent in the xy plane becomes too long [30,31].

More recently, Barrère et al. discussed another acquisition strategy to obtain quantitative diffusion NMR data [31]. It is based on the integrals of the different components, extracted with DECRA algorithm [32], which are renormalized by taking explicitly into account the relaxation effects. In this strategy, diffusion coefficients and relaxation times are measured with the same modified PGSE pulse sequence in which an initial CPMG block has been added. Mixture fractions are obtained with a good overall accuracy (better than 2.5%, with some constraints on T 2) using only three PGSE experiments and a processing with DECRA. However, the efficiency of this strategy was only reported with model mixtures that exhibit no or only partial overlapping of the spectral signatures of the components. Indeed, the presence of isolated and well-resolved signals for each component of the mixture can help multivariate analyses of PGSE experiments such as DECRA. Moreover, the two different diffusion delays ( D min and D max) used for the estimation of T 1 are associated with a unique gradient pulse length ( d ). Therefore, in the case of overlapping components they cannot be too different to avoid a loss of resolution in the diffusion dimension [33]. However, a too small difference between the two diffusion delays can be a problem for a correct estimation of long T 1's.

In the present study, taking mixtures of polymers as examples, we report on the use of PGSE NMR to quantitatively analyze mixtures where there is a complete overlap of all the signals. The chosen model systems are binary and ternary mixtures of polystyrene (PS) standards of different molecular weights. The points of inter- est for PS standards are a very low polydispersity ( Mw / Mn ca. 1.01) and a total overlap of their NMR signals. In order to check our strategy, the following points must be verified:

-  The fractions obtained for the mixture compounds should correspond to the weight fractions determined upon mixture preparation.
-  The diffusion coefficients obtained for the mixture compounds should be similar to the ones found for the pure compounds in solution.

To obtain quantitative results, the relaxation phenomena are explicitly taken into account by implementation of their effects on the attenuation in the general Stejskal-Tanner equation [25,30]:

X

$$\begin{smallmatrix} \text {user} & \text {sys-} \\ \text {vell-rel} & \text { } I = I _ { 0 } \sum _ { i } f _ { i } \exp ( - D _ { i } q ^ { 2 } \Delta ^ { \prime } - R _ { i } ) . & \\ \text {simple} & \end{smallmatrix} ( 1 )$$

In this equation, I 0 is the intensity at zero gradient strength, f i the fraction and Di the diffusion coefficient of the i th component, q equals cd G with c the gyromagnetic ratio of the nucleus, d is the gradient pulse length, G the gradient strength, D 0 the corrected diffusion delay and R a relaxation factor, taking into account T 1 and T 2 relaxation effects.

## 2. Experimental section

## 2.1. PS samples

Appropriate amounts of five commercially available PS GPCstandards (Aldrich) with different molecular weight (Table 1) were dissolved in 500 l l of chloroformd (100%) in order to obtain the desired mixtures (Table 2). The samples were deliberately very diluted (below 1.2% by weight) to avoid a possible modification of the diffusion behavior caused by interactions in between polymers.

## 2.2. NMR

All measurements were performed without spinning at 298 K on a Bruker Avance III 300 MHz spectrometer using a 5 mm BBFO probe equipped with a z -gradient coil providing a maximum gradient strength of 49.8 G cm  1 . For all experiments, the recycling delay was always five times larger than the longest T 1.

T 1 relaxation times were determined using the inversion recovery (IR) pulse sequence (32 increments) and T 2 relaxation times using the Carr-Purcell-Meiboom-Gill (CPMG) pulse sequence (32 increments). Relaxation measurements were analyzed (relaxations times and fractions, when relevant) by fitting the appropriate function to the data (integrals of resonance peaks) using a least squares algorithm as implemented in Topspin 3.0 (Bruker).

A convection compensating double stimulated echo pulse sequence with longitudinal eddy current delay ( Te = 5 ms), bipolar sine-shaped gradient pulses of amplitude G (from 2% to 90% with 32 increments) and pulse length d was used for PGSE NMR exper- iments. 32 transients were acquired for each gradient increment. For each studied sample, different values of the diffusion delay D were used (100-800 ms). The associated gradient pulse length d was fixed as follow. For D equals 200 ms, d was optimized in order to obtain a residual intensity of ca. 3% at 90% gradient strength. For the other D values, d was calculated so Dd 2 is kept constant for all the ( D , d ) pairs. With such pairs, the echo decays are always well described.

Table 1 Characteristics of polystyrene GPC standards (polydispersity 1.01): molecular weight Mw , calculated gyration radius r g and diffusion coefficient D calc ( g chloroformd 0.539 cP), experimental T 1 and T 2 relaxation times and diffusion coefficient D exp. Relaxation times and diffusion coefficients are reported for the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring.

| PS   |   M w (g mol  1 ) |   r g (nm) |   D calc (10  10 m 2 s  1 ) |   T 1 (s) |   T 2 (s) | D exp (10  10 m 2 s  1 )   | D exp (10  10 m 2 s  1 )   |
|------|-------------------|------------|-----------------------------|-----------|-----------|----------------------------|----------------------------|
|      |                   |            |                             |           |           | D = 200 ms                 | D = 800 ms                 |
| A    |              3700 |       0.52 |                        7.77 |      1.06 |      0.59 | 2.99                       | 3.05                       |
| B    |             29300 |       1.48 |                        2.76 |      1.10 |      0.36 | 1.06                       | 1.05                       |
| C    |            212400 |       3.98 |                        1.03 |      1.08 |      0.34 | 0.27                       | 0.27                       |
| D    |            382000 |       5.33 |                        0.77 |      1.06 |      0.31 | 0.20                       | 0.19                       |
| E    |           1880000 |      11.83 |                        0.35 |      1.08 |      0.24 | 0.09                       | 0.09                       |

Table 2

Weight fractions of polystyrene standards from Table 1 used to prepare 500 l l of polystyrene mixture and corresponding relative weight fractions.

|   Mixture | Components   |   Weight fractions (%) |   Weight fractions (%) |      |   Relative weight fractions (%) |   Relative weight fractions (%) |      |
|-----------|--------------|------------------------|------------------------|------|---------------------------------|---------------------------------|------|
|         1 | A/D          |                   0.29 |                   0.19 |      |                            60.1 |                            39.9 |      |
|         2 | A/D          |                   0.86 |                   0.19 |      |                            82.1 |                            17.9 |      |
|         3 | A/C/E        |                   0.54 |                   0.35 | 0.27 |                            46.4 |                            30.1 | 23.5 |
|         4 | A/B/D        |                   0.17 |                   0.16 | 0.22 |                            29.9 |                            29.2 | 40.9 |

PGSE NMR data were analyzed with a single-channel (univariate) process by fitting the appropriate attenuation function (see text) to the data (integrals of resonance peaks extracted with Topspin 3.0) using a least squares algorithm. As the effects of relaxation effects (see Eq. (5)) could not be easily implemented in standard processing packages used to analyze PGSE NMR experiment (ex. Topspin or DOSYToolbox [34]), the fitting was performed with Excel, a common and easily available software. SCORE [35], a multivariate method that does not require a quadratic spacing of the gradients intensities, was also used, as implemented in the DOSYToolbox by Nilsson [34], to analyze PGSE experiments. SCORE was only used to compare the results of a multivariate algorithm with those of a univariate process, when relaxation effects are not taken into accounts (Fig. 2, left panel).

## 3. Results and discussion

Before studying the polymer mixtures, the different PS samples were studied separately. In this paper, only the relaxation and diffusion results obtained for the resonance peak representing the para and meta protons of the phenyl ring (7.25-6.89 ppm) are reported. Similar results were found for the ortho protons (6.896.30 ppm).

## 3.1. Pure PS in solution

In NMR relaxometry, a single compound should theoretically result in only one relaxation time per resonance, but a varying

1

0.5

0

-0.5

-1

degree of mobility for instance might cause a distribution of T 2 relaxation times along the polymer backbone. In that case, instead of a mono-exponential decay the relaxation decay will look more like a bi- or even multi-exponential decay [36,37]. Such a distribution of relaxation times can be caused on the one hand by a distribution of chain length or molecular mass of the polymer chains (i.e. the polydispersity) or on the other hand by mobility variations along the polymer backbone (i.e. the position in the backbone). Therefore T 1 and T 2 relaxation times were first measured on the individual polymers in solution to check for the possibility of such an effect.

Despite the fact that the analyzed signal corresponds to two different types of protons (para and meta), inversion recovery experiments resulted in a single T 1 for each individual polymer, as illustrated in Fig. 1 (left panel) for polymer B. Moreover, comparison of T 1 values for the different molecular weights shows that all T 1 values are identical within experimental error (Table 1). Fitting a mono-exponential function to the relaxation decay measured by a CPMG pulse sequence for the signal associated to the para and meta protons of the phenyl ring showed good to excellent results indicating that per individual polymer a single T 2 sufficed to describe the spin-spin relaxation behavior (Fig. 1, right panel). The very low polydispersity of the PS standards, the choice of chloroform, which is a good solvent for PS, and the dilute solutions ([PS] 6 5 g l  1 ) likely contribute to the mono-exponential T 2 relaxation decay. Contrarily to T 1, T 2 values (Table 1) show a dependency to the molecular weight: they decrease when Mw increases.

A single compound should also theoretically result in only one diffusion coefficient and, accordingly, in a mono-Gaussian intensity attenuation of its signals in a PGSE experiment. However, in polymer systems, polydispersity may result in a distribution of diffusion coefficients. Therefore, diffusion coefficients for the individual PS samples were measured on dilute solutions using two diffusion times D (200 ms and 800 ms). Not only did a monoGaussian decay suffice to fit the intensity attenuations, but the results also showed an excellent agreement for the individual

<!-- image -->

4

5

Time (s)

Fig. 1. T 1 and T 2 relaxation times measurements, respectively by inversion recovery (left panel) and CPMG (right panel), on the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring of polystyrene standard B ( Mw = 29300 g mol  1 , 1 mg in 1 ml CDCl3). Fitting results in T 1 = 1.10 s and T 2 = 0.36 s. The upper half of each graph pictures the sampled intensities ( h ) and fitted curve (-) on the left axis, the lower half pictures the residuals ( j ) of the least squares fit (right axis).

Intensity (a.u.)

0

1

2

3

6

7

8

9

0.0015

0.0005

-0.0005

-0.0015

Residuals (a.u.)

Fig. 2. Relative weight fractions of the diffusion regimes of PS A (LS h , SCORE +) and PS D (LS 4 , SCORE -) in mixture 1 (A/D 60/40) as a function of the diffusion delay D , without (left panel) and with (right panel) taking into account relaxation effects. These values were obtained from the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring.

<!-- image -->

resonance peaks in the spectrum, as well as for the two diffusion delays D (Table 1). As the diffusion coefficient D is related to the hydrodynamic radius rH of the random polymer coils by the Stokes-Einstein equation:

$$D = \frac { k _ { B } T } { 6 \pi \eta r _ { H } } & & ( 2 ) & \frac { \frac { \ M i x t { u } } { 1 } } { 2 }$$

with kB the Boltzmann constant, T the temperature and g the viscosity of the sample (0.539 cP for chloroformd at 298 K [38]), and since the random coil size is related to the molecular mass, lower diffusion coefficients directly indicate a higher molecular mass. More specifically in a h -solvent, a solvent where the random polymer coil is ''undisturbed'' in solution, the hydrodynamic radius should equal the radius of gyration r g of the polymer [39], which can be estimated by:

ffiffiffiffiffiffi

s

$$r _ { g } = \sqrt { \frac { n l ^ { 2 } } { 6 } } & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

with n the number and l the length of the backbone bonds (C-C 1.52 Å [40]). Chloroform being a good solvent for PS, rH is expected to be larger than r g and consequently the measured diffusion coefficient will be smaller than the calculated one.

## 3.2. Binary PS/PS mixtures in solution

Two binary mixtures of polymers A and D (Table 2) were then studied. Since all the individual polymers exhibit an identical T 1 relaxation time, within experimental error, for the resonance peak representing the para and meta protons of the phenyl ring (Table 1), a single T 1 relaxation time was also measured on the same resonance for both mixtures (Table 3). As a consequence, mixture analysis by T 1 relaxometry is absolutely impossible for these samples. The small difference in T 2 relaxation times that were measured for polymers A and D alone (Table 2), a factor of 1.90, is a priori not well suited for mixture analysis either, since a factor of at least two is generally given as a condition for correctly fitting bi-exponential decays. Nonetheless, the T 2 measurements performed on mixtures 1 and 2 clearly showed two relaxation regimes for the resonance peak associated to the para and meta protons of the phenyl ring. The extracted T 2 values (Table 3) match well the one determined separately on polymers A and D, and, moreover, the fractions obtained from these T 2 measurements were in good agreement with the real sample fractions (Table 3).

Table 3 Relaxation times (s) and corresponding relative weight fractions ( x in%) for binary PS/ PS mixtures measured on the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring.

|   Mixture | T 1 ( x )   | T 2 ( x )   |             |
|-----------|-------------|-------------|-------------|
|         1 | 1.07 (100)  | 0.56 (63.6) | 0.34 (36.4) |
|         2 | 1.06 (100)  | 0.56 (84.4) | 0.31 (15.6) |

In strong contrast with the small difference in relaxation times, the diffusion coefficients of the individual polymers A and D do differ by a factor of 15. Consequently a diffusion-based technique like PGSE NMR should be more appropriate for mixture analysis. Unfortunately, PGSE NMR might be non-quantitative and result in incorrect fractions due to relaxation effects. To take these effects into account and get meaningful fractions, the attenuation related to relaxation has to be introduced in the general Stejskal-Tanner equation. For a convection compensating double stimulated echo pulse sequence, with rectangular gradient pulses and longitudinal eddy current delay, the attenuation is expressed as [41]:









X

$$I = & I _ { 0 } \sum _ { i } f _ { i } \exp \left [ - D _ { i } ( \gamma \delta G ) ^ { 2 } \left ( T + \frac { 4 \delta } { 3 } + \frac { 5 \tau _ { 1 } } { 4 } + \frac { \tau _ { 2 } } { 4 } \right ) \right ] \\ & \exp \left [ - 4 \frac { \delta + \frac { \tau _ { 1 } + \tau _ { 2 } } { 2 } } { T _ { 2 , i } } - \frac { T + \frac { \tau _ { 1 } - \tau _ { 2 } } { 2 } + T _ { e } } { T _ { 1 , i } } \right ]$$

where the first exponential represents the intensity attenuation related to diffusion and the second exponential represents the intensity attenuation related to relaxation. s 1 and s 2 are gradient recovery delays and T is the diffusion delay during which the magnetization is longitudinal, as defined by Jerschow and Müller [41]. For sine-shaped gradient pulses, as used in this work, the intensity attenuation function takes the following form [42]









X

$$0 , \, \text {is a} \quad \\ \text {actor of} \quad & 1 = I _ { 0 } \sum _ { i } f _ { i } \exp \left [ - D _ { i } ( \gamma \delta G ) ^ { 2 } \frac { 4 } { \pi ^ { 2 } } \left ( \Delta - \frac { 5 \delta } { 8 } - \frac { \tau _ { 1 } } { 2 } - \frac { \tau _ { 2 } } { 2 } \right ) \right ] \\ \text {its per-} \quad \\ \text {gimes} \quad & \exp \left [ - 4 \frac { \delta + \frac { \tau _ { 1 } + \tau _ { 2 } } { 2 } } { T _ { 2 , i } } - \frac { \Delta - 3 \delta - \tau _ { 1 } - \tau _ { 2 } + T _ { e } } { T _ { 1 , i } } \right ] \\$$

where D is the diffusion time and the other parameters keep the same meaning as above.

According to the different T 2 relaxation times that were observed for the different PS standards, common PGSE NMR data analyses that only implement the attenuation factor related to diffusion and not the attenuation factor related to relaxation result in erroneous fractions that, moreover, vary with the diffusion delay D used (Fig. 2, left panel). In the present systems, where both components have the same T 1 but different T 2 relaxation times, the observed variation of the fractions with the diffusion delay D arises from our methodology in which Dd 2 is kept constant. Extrapolation of these fractions towards D = 0, to eliminate relaxation effects as proposed by Antalek in the qDECRA methodology [30], yields values which agree well with the real fractions, especially for the single channel analysis. The origin of the small bias observed for the SCORE analysis, which however remains low (&lt;1%), is unclear.

On the contrary, when the relaxation attenuation factor is explicitly introduced in the Stejskal-Tanner equation (Eq. 5), analyses of the PGSE NMR data, using the relaxation times that were directly measured on the mixtures (vide supra and Table 3), now yield fractions independent of the diffusion time used (Fig. 2, right panel). A direct implementation of the effects of relaxation into multi-channel methods is difficult and was not attempted because each resonance has its own relaxation times. However, a renormalization of the integrals of the components extracted by SCORE, similarly to the approach presented by Barrère et al. [31], should also yield fractions independent of the diffusion delay.

The diffusion coefficients and corresponding fractions, extracted with Eq. (5) for two different PS/PS mixtures, are compiled into Table 4. The diffusion coefficients obtained for mixtures 1 and 2 are in good agreement with each other and with the ones measured for the individual polymers. The corresponding fractions, which do not vary anymore with the diffusion delay D , are in very good agreement with the real fractions of the prepared samples. As a consequence the extrapolation towards D = 0 (Fig. 2, left panel), as in qDECRA [30] can be avoided using this approach and a single experiment with a given D is needed for quantification once T 1 and T 2 relaxation times have been measured or are known.

The main drawback of this strategy is the need to measure or at least to estimate accurately the relaxation times of the system. These measurements,whichyetbringvaluableinformationonthesystem, can be time consuming and difficult, especially when, as in our case, all signals of the individual mixture compounds totally overlap. Alternatively to independent measures of the relaxation times, the PGSEexperimentscanalsobeusedtoextractthesedataastheintensity of the echoes also depends on relaxation times (Eq. (1)). Therefore, the attenuation profiles of the resonance peak representing the para and meta protons of the phenyl ring (integral of resonance peak) that were extracted from six PGSE experiments with varying diffusion delays (and gradient pulse lengths) were simultaneously analyzed as one big data set, with the diffusion coefficients, the weight fractions and the T 1 and T 2 relaxation times as parameters. The results obtained by this processing strategy on mixture 1 were in very good agreement with the ones individually measured (diffusion coefficients of 2.92 and 0.21 -10  10 m 2 /s, weight fractions of 60.2% and 39.8%, T 1 of 1.01 and 1.01 s, and T 2 of 0.55 and 0.34 s, to be compared with values presented in Tables 3 and 4).

Table 4 Diffusion coefficients ( D -10  10 m 2 s  1 ) and corresponding relative weight fractions ( x in%) for binary PS/PS mixtures. The reported values were obtained by fitting the PGSE NMR data of the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring with Eq. 5, using the relaxation times reported in Table 3.

|              | Mixture 1   | Mixture 1   | Mixture 2   | Mixture 2   |
|--------------|-------------|-------------|-------------|-------------|
|              | D           | x           | D           | x           |
| D = 100 ms   | 2.89        | 60.7        | 2.92        | 85.9        |
|              | 0.21        | 39.3        | 0.24        | 14.1        |
| D = 200 ms   | 2.91        | 60.5        | 2.93        | 85.7        |
|              | 0.21        | 39.5        | 0.24        | 14.3        |
| D = 300 ms   | 2.94        | 60.3        | 2.91        | 85.8        |
|              | 0.21        | 39.7        | 0.23        | 14.2        |
| D = 400 ms   | 2.94        | 60.6        | 2.91        | 85.6        |
|              | 0.21        | 39.4        | 0.23        | 14.4        |
| D = 500 ms   | 2.92        | 60.4        | 2.91        | 85.7        |
|              | 0.21        | 39.6        | 0.23        | 14.3        |
| D = 600 ms   | 2.92        | 60.2        | 2.91        | 85.9        |
|              | 0.21        | 39.8        | 0.23        | 14.1        |
| Average ± SD | 2.92 ± 0.02 | 60.5 ± 0.2  | 2.92 ± 0.01 | 85.8 ± 0.1  |
|              | 0.21 ± 0.01 | 39.5 ± 0.2  | 0.23 ± 0.01 | 14.2 ± 0.1  |

To check the possibility of diminishing the total time needed for the measurements and make our approach more valuable, the simultaneous analysis was then again performed but with a reduced number of different diffusion delays taken into account in the data set. For our system that exhibits a total overlap of all the resonances, we obtained satisfying to good weight fractions (59.4/40.6, 59.6/40.4, or 59.7/40.3 instead of 60.1/39.9) by processing three, four, or five PGSE experiments, respectively. A processing with only three PGSE experiments represents a measuring load equivalent to the one reported by Barrère et al. [31].

## 3.3. Ternary PS/PS/PS mixtures in solution

As was the case for the binary mixtures, a single T 1 relaxation time was found for the resonance peak representing the para and metaprotons of the phenyl ring in the ternary mixtures. CPMG measurements, performed on the same resonance for the ternary mixtures, did not allow extracting different T 2 relaxation times (and their corresponding fraction) as could be expected from the fairly small differences in the T 2 values determined on the individual polymers(Table 1). Nonetheless, as the relaxation times measured in the binary mixtures agreed very well with the ones measured on isolated polymers, the relaxation times of the isolated polymers (Table 1) were used in the general Stejskal-Tanner equation (Eq. 5) to analyze the PGSE NMR experiments of the ternary mixtures. The results of these analyses (diffusion coefficients and corresponding fractions) are presented in Figs. 3 and 4. For mixture 3 (Fig. 3), the results averaged over the various diffusion delays are 2.77 ± 0.1 10  10 , 0.16 ± 0.01 10  10 and0.04 ± 0.03 10  10 m 2 s  1 for the diffusion coefficients and 49.2 ± 1.7, 29.7 ± 0.9 and 21.2 ± 0.9 for the relative weight fractions. For mixture 4 (Fig. 4), the averaged values are 2.91 ± 0.1 10  10 , 0.84 ± 0.05 10  10 and 0.20 ± 0.01 10  10 m 2 s  1 for the diffusion coefficients and 29.8 ± 1.0, 28.9 ± 1.0 and 41.3 ± 1.0 for the relative weight fractions.

For both ternary mixtures, the diffusion coefficients found for the different diffusion delays are in good agreement with each other. Furthermore they match reasonably well the diffusion coefficients of the individual polymers, although they are all systematically a little lower for the mixture than for the individual solutions.

Concerning the fractions, no significant trend with the diffusion delay can be found and the experimental scatter on the fractions remains small (about 3%). More importantly, the fractions found are in very good agreement with the real fractions of the prepared samples, indicating that a quantitative mixture analysis by PGSE NMRis possible when the complete Stejskal-Tanner equation, taking into account relaxation effects, is used.

The processing strategy, in which the diffusion coefficients, fractions, and relaxation times ( T 1 and T 2) are all extracted from the simultaneous analysis with Eq. (5) of several PGSE experiments with different diffusion delays, was also applied to ternary systems. It resulted in good results on both diffusion coefficients and weight fractions, for instance 47/28/25 for mixture 3. However, since 12 parameters have to be optimized ( T 1, T 2, f and D for each component), the method demands longer calculation times, becomes more sensitive to the starting values of the parameters and the estimated errors on the fit are larger (about 5%).

Fig. 3. Diffusion coefficients (left panel) and relative weight fractions (right panel) of PS A ( s ), PS C ( 4 ) and PS E ( h ) in mixture 3 (A/C/E 46/30/24) as a function of the diffusion delay D . These values were obtained from the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring.

<!-- image -->

Fig. 4. Diffusion coefficients (left panel) and relative weight fractions (right panel) of PS A ( s ), PS B ( 4 ) and PS D ( h ) in mixture 4 (A/B/D 30/29/41) as a function of the diffusion delay D . These values were obtained from the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring.

<!-- image -->

## 4. Conclusions

Implementation of relaxation effects in the Stejskal-Tanner equation for a convection compensating bipolar gradient pulse sequence enabled determining quantitatively both diffusion coefficients and fractions in binary and ternary mixtures of polymers for which a total overlap of the spectra of the different components prevents the use of integration. The possibilities of such analysis have been illustrated on mixtures of PS with different molecular weights.

Using the general Stejskal-Tanner equation to analyze the experimental data requires the measurement of relaxation times, which can be time consuming and/or delicate, but only one PGSE experiment is then needed to extract quantitative fractions. When a direct measurement of the different relaxation times is not possible on the mixture because of too small differences, as for the ternary PS mixtures reported here, using relaxation times measured on the individual polymer solutions proved to be a good alternative and afforded a quantitative analysis of these ternary mixtures. Fig. 5 summarizes the overall good agreement, observed in the presented methodology, between the measured and prepared relative weight fractions.

Fig. 5. Relative weight fractions, determined by PGSE NMR, as a function of the prepared relative weight fractions for mixtures 1 ( h ), 2 ( s ), 3 ( } ) and 4 ( 4 ). These values were obtained from the signal (7.25-6.89 ppm) associated to the para and meta protons of the phenyl ring. The dotted line represents the identity (measured relative weight fractions = prepared relative weight fraction).

<!-- image -->

Alternatively to independent measures of the relaxation times, a series of attenuation profiles extracted for a given resonance from several PGSE experiments with varying diffusion delays and gradient pulse lengths, can be globally analyzed as a unique data set to yield diffusion coefficients, relaxation times, and fractions. For binary mixtures of polymers with totally overlapping signals, a series of three PGSE experiments yields good fractions (±3%). For ternary mixtures, this simultaneous analysis of several PGSE experiments yields also good results for the fractions (±5%) but demands longer calculation times and becomes more sensitive to the initial guesses.

Compared to qDECRA, the time during which the magnetization is in the xy plane can be kept reasonable and, therefore, J-modulation effects are less an issue. Furthermore, since the presented processing strategy is only based on the use of the correct general Stejskal-Tanner equation, including both diffusionand relaxation-induced attenuation effects, the use of the Oneshot45 experiment [43], specifically designed to suppress J-modulation effects in PGSE NMR, should be perfectly possible.

For the investigated systems all T 1 relaxation times were identical within experimental error. Although the methodology is applicable to all kinds of systems, large differences in T 1 relaxation times might create interferences in its applicability. Since T 1 effects occur during the time the magnetization is stored along z , which is of the order of the diffusion delay D (100-800 ms), while T 2 effects occur when the magnetization is transversally oriented (i.e. during the gradient pulses d and the recovery delays s 1 and s 2) a total attenuation due to T 1 relaxation effects might occur for very short T 1 values. According to the total attenuation obtained after 5 T 1, special care is therefore needed for T 1 relaxation times shorter than 100 ms. NMR probes able to deliver much stronger gradients (  1000 G cm  1 ), and therefore shorter D and d , are a possible response to these relaxation issues.

In the present work, the polymers used exhibited a low polydispersity. Accordingly, the diffusive behavior of each one was well described by a single diffusion coefficient. A single T 1 and a single T 2 relaxation times were also observed for each polymer. Systems with a (large) distribution of diffusion coefficients or relaxation times might be difficult to quantify by PGSE NMR. However, in the present study the same T 1 was observed for polymers with molecular weights spanning almost over three orders of magnitude and the T 2 values were not highly sensitive to the molecular weight (Table 1). Accordingly broad distributions of T 1 and T 2 are not to expect. For species with a (large) distribution of their molecular weight, modeling the distribution of diffusion coefficients with the gamma distribution, as recently proposed by Röding et al. [44], might be interesting to consider.

## Acknowledgment

This work has been supported by the French National Agency (ANR) in the frame of its program of nanosciences and nanotechnologies (EVALON Project No. ANR-08-NANO-026).

## Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at http://dx.doi.org/10.1016/j.jmr.2013.03.003.

## References

- [1] P.T. Callaghan, Translational Dynamics and Magnetic Resonance - Principles of Pulsed Gradient Spin Echo NMR, Oxford University Press, Oxford, 2011.
- [2] G.A. Morris, Diffusion ordered spectroscopy, in: R.K. Harris, R.E. Wasylishen (Eds.), Encyclopedia of Magnetic Resonance, Wiley, Chichester, 2009.
- [3] W.S. Price, NMR Studies of Translational Motion, Cambridge University Press, Cambridge, 2009.
- [4] P. Stilbs, Fourier transform pulsed-gradient spin-echo studies of molecular diffusion, Prog. Nucl. Magn. Reson. Spectrosc. 19 (1987) 1-45.
- [5] L. Van Lokeren, G. Maheut, F. Ribot, V. Escax, I. Verbruggen, C. Sanchez, J.C. Martins, M. Biesemans, R. Willem, Characterization of titanium dioxide nanoparticles dispersed in organic ligand solutions by using a diffusionordered spectroscopy-based strategy, Chem. Eur. J. 13 (2007) 6957-6966.
- [6] R. Gomes, A. Hassinen, A. Szczygiel, Q.A. Zhao, A. Vantomme, J.C. Martins, Z. Hens, Binding of phosphonic acids to CdSe quantum dots: a solution NMR study, J. Phys. Chem. Lett. 2 (2011) 145-152.
- [7] D. Smejkalova, A. Piccolo, Aggregation and disaggregation of humic supramolecular assemblies by NMR diffusion ordered spectroscopy (DOSYNMR), Environ. Sci. Technol. 42 (2008) 699-706.
- [8] P.S. Denkova, L. Van Lokeren, R. Willem, Mixed Micelles of Triton X-100, sodium dodecyl dioxyethylene sulfate, and synperonic L61 investigated by NOESY and diffusion ordered NMR spectroscopy, J. Phys. Chem. B 113 (2009) 6703-6709.
- [9] C. Pascal, F. Paté, V. Cheynier, M.-A. Delsuc, Study of the interactions between a proline-rich protein and a flavan-3-ol by NMR: residual structures in the natively unfolded protein provides anchorage points for the ligands, Biopolymers 91 (2009) 745-756.
- [10] A. Ambrus, D. Yang, Diffusion-ordered nuclear magnetic resonance spectroscopy for analysis of DNA secondary structural elements, Anal. Biochem. 367 (2007) 56-67.
- [11] H. Walderhaug, O. Söderman, D. Topgaard, Self-diffusion in polymer systems studied by magnetic field-gradient spin-echo NMR methods, Prog. Nucl. Magn. Reson. Spectrosc. 56 (2010) 406-425.
- [12] C.A. Crutchfield, D.J. Harris, Molecular mass estimation by PFG NMR spectroscopy, J. Magn. Reson. 185 (2007) 179-182.
- [13] D. Li, G. Kagan, R. Hopson, P.G. Williard, Formula weight prediction by internal reference diffusion-ordered NMR spectroscopy (DOSY), J. Am. Chem. Soc. 131 (2009) 5627-5634.
- [14] L. Van Lokeren, E. Cartuyvels, G. Absillis, R. Willem, T.N. Parac-Vogt, Phosphoesterase activity of polyoxomolybdates: diffusion ordered NMR spectroscopy as a tool for obtaining insights into the reactivity of polyoxometalate clusters, Chem. Commun. (2008) 2774-2776.
- [15] F. Périneau, S. Pensec, C. Sassoye, F. Ribot, L. Van Lokeren, R. Willem, L. Bouteiller, C. Sanchez, L. Rozes, New hybrid core-shell star-like architectures made of poly(n-butyl acrylate) grown from well-defined titanium oxoclusters, J. Mater. Chem. 21 (2011) 4470-4475.
- [16] T.E. Malliavin, V. Louis, M.-A. Delsuc, The DOSY experiment provides insights into the protegrin-lipid interaction, J. Chim. Phys. 95 (1998) 178-186.
- [17] M.L. Liu, H.C. Toms, G.E. Hawkes, J.K. Nicholson, J.C. Lindon, Determination of the relative NH proton lifetimes of the peptide analogue viomycin in aqueous solution by NMR-based diffusion measurement, J. Biomol. NMR 13 (1999) 2530.
- [18] E.J. Cabrita, S. Berger, P. Brauer, J. Karger, High-resolution DOSY NMR with spins in different chemical surroundings: influence of particle exchange, J. Magn. Reson. 157 (2002) 124-131.
- [19] I. Moreels, Y. Justo, B. De Geyter, K. Haustraete, J.C. Martins, Z. Hens, Sizetunable, bright, and stable PbS quantum dots: a surface chemistry study, ACS Nano 5 (2011) 2004-2012.
- [20] D. Grosso, F. Ribot, C. Boissiere, C. Sanchez, Molecular and supramolecular dynamics of hybrid organic-inorganic interfaces for the rational construction of advanced hybrid nanomaterials, Chem. Soc. Rev. 40 (2011) 829-848.
- [21] P.T. Callaghan, D.N. Pinder, Self-diffusion of ramdon-coil polystyrene determined by pulsed field gradient nuclear magnetic-resonance -dependence on concentration and molar mass, Macromolecules 14 (1981) 1334-1340.
- [22] S. Augé, P.O. Schmit, C.A. Crutchfield, M.T. Islam, D.J. Harris, E. Durand, M. Clemancey, A.A. Quoineaud, J.-M. Lancelin, Y. Prigent, F. Taulelle, M.A. Delsuc, NMR measure of translational diffusion and fractal dimension. Application to molecular mass measurement, J. Phys. Chem. B 113 (2009) 1914-1918.
- [23] J. Vieville, M. Tanty, M.-A. Delsuc, Polydispersity index of polymers revealed by DOSY NMR, J. Magn. Reson. 212 (2011) 169-173.
- [24] M.D. Pelta, G.A. Morris, M.J. Stchedroff, S.J. Hammond, A one-shot sequence for high-resolution diffusion-ordered spectroscopy, J. Magn. Reson. Chem. 40 (2002) S147-S152.
- [25] M. Nilsson, M.A. Connell, A.L. Davis, G.A. Morris, Biexponential fitting of diffusion-ordered NMR data: practicalities and limitations, Anal. Chem. 78 (2006) 3040-3045.
- [26] B. Antalek, Using pulsed gradient spin echo NMR for chemical mixture analysis: How to obtain optimum results, Concept. Magn. Reson. 14 (2002) 225-258.
- [27] A.K. Rogerson, J.A. Aguilar, M. Nilsson, G.A. Morris, Simultaneous enhancement of chemical shift dispersion and diffusion resolution in mixture analysis by diffusion-ordered NMR spectroscopy, Chem. Commun. 47 (2011) 7063-7064.
- [28] C.F. Tormena, R. Evans, S. Haiber, M. Nilsson, G.A. Morris, Matrix-assisted diffusion-ordered spectroscopy: application of surfactant solutions to the resolution of isomer spectra, Magn. Reson. Chem. 50 (2012) 458-465.
- [29] F. Ribot, V. Escax, C. Roiland, C. Sanchez, J.C. Martins, M. Biesemans, I. Verbruggen, R. Willem, In situ evaluation of interfacial affinity in CeO2-based hybrid nanoparticles by pulsed field gradient NMR, Chem. Commun. (2005) 1019-1021.
- [30] B. Antalek, Accounting for spin relaxation in quantitative pulse gradient spin echo NMR mixture analysis, J. Am. Chem. Soc. 128 (2006) 8402-8403.

- [31] C. Barrère, P. Thureau, A. Thévand, S. Viel, Acquisition strategy to obtain quantitative diffusion NMR data, J. Magn. Reson. 216 (2012) 201-208.
- [32] W. Windig, B. Antalek, Direct exponential curve resolution algorithm (DECRA): A novel application of the generalized rank annihilation method for a single spectral mixture data set with exponentially decaying contribution profiles, Chemomet. Intell. Lab. Syst. 37 (1997) 241-254.
- [33] For D max = kD min ( k &gt; 1), the diffusion related attenuation ( W = I / I 0) for D max and G max equals [ W ( D min, G max)] k or, alternatively, W ( D min, G max) = W ( D max, G max/ p k ). Therefore, when combined with the quadratic increase of the gradient values required by DECRA, it results that, if d is optimized for D min and G max, the number of experiments, which cover the same optimum range with D max, is divided by k . Such a decrease in the number of experiments that can be analyzed might indeed reduce the resolution in the diffusion dimension.
- [34] M. Nilsson, The DOSY Toolbox: A new tool for processing PFG NMR diffusion data, J. Magn. Reson. 200 (2009) 296-302.
- [35] M. Nilsson, G.A. Morris, Speedy component resolution: an improved tool for processing diffusion-ordered spectroscopy data, Anal. Chem. 80 (2008) 37773782.
- [36] E. Von Meerwall, T. Stone, Network fraction and molecular motion in polymer composites - an NMR relaxation and self diffusion study, J. Polym. Sci., Part B: Polym. Phys. 27 (1989) 503-522.
- [37] L. Van Lokeren, N.A. Gotzen, R. Pieters, G. Van Assche, M. Biesemans, R. Willem, B. Van Mele, Phase behavior in blends of ethylene oxide-propylene oxide
8. copolymer and poly(ether sulfone) studied by modulated-temperature DSC and NMR relaxometry, Chem. Eur. J. 15 (2009) 1177-1185.
- [38] M. Holz, X. Mao, D. Seiferling, A. Sacco, Experimental study of dynamic isotope effects in molecular liquids: detection of translation-rotation coupling, J. Chem. Phys. 104 (1996) 669-679.
- [39] P.T. Callaghan, Principles of Nuclear Magnetic Resonance Microscopy, Oxford University Press, Oxford, 1991. pp. 341-344.
- [40] D.R. Lide (Ed.), Handbook of Chemistry and Physics, 82nd ed., CRC Press, Florida, 2001.
- [41] A. Jerschow, N.J. Muller, Suppression of convection artifacts in stimulated-echo diffusion experiments. Double-stimulated-echo experiments, J. Magn. Reson. 125 (1997) 372-375.
- [42] D. Sinnaeve, The Stejskal-Tanner equation generalized for any gradient shape - an overview of most pulse sequences measuring free diffusion, Concepts Magn. Reson. Part A 40A (2012) 39-65.
- [43] A. Botana, J.A. Aguilar, M. Nilsson, G.A. Morris, J-modulation effects in DOSY experiments and their suppression: the Oneshot45 experiment, J. Magn. Reson. 208 (2011) 270-278.
- [44] M. Röding, D. Bernin, J. Jonasson, A. Särkkä, D. Topggard, M. Rudemo, M. Nydén, The gamma distribution model for pulsed-field gradient NMR studies of molecular-weight distributions of polymers, J. Magn. Reson. 222 (2012) 105-111.