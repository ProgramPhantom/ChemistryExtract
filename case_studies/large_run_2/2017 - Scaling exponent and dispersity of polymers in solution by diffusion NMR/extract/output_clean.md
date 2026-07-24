<!-- image -->

## Short Communication

## Scaling exponent and dispersity of polymers in solution by diffusion NMR

Nathan H. Williamson , , Magnus Röding , , Stanley J. Miklavcic , Magnus Nydén ,

- a Future Industries Institute, University of South Australia, Mawson Lakes, SA 5095, Australia

b SP Agrifood and Bioscience, Frans Perssons väg 6, 402 29 Göteborg, Sweden

- c School of Energy and Resources, University College London, 220 Victoria Square, Adelaide, SA 5000, Australia
- d Phenomics and Bioinformatics Research Centre, School of Information Technology and Mathematical Sciences, University of South Australia, Mawson Lakes, SA 5095, Australia

## g r a p h i c a l a b s t r a c t

<!-- image -->

## a r t i c l e i n f o

Article history: Received 28 November 2016 Revised 14 January 2017 Accepted 17 January 2017 Available online 18 January 2017

## Keywords:

Pulsed gradient spin echo Pulsed field gradient Nuclear Magnetic Resonance spectroscopy Molecular weight distribution Polymers DOSY Polydispersity Index Self-diffusion Molar mass Flory exponent Lognormal distribution Gamma distribution End-group analysis Scaling law

Corresponding author.

⇑ E-mail addresses: (M. Nydén).

Contents lists available at

## Journal of Colloid and Interface Science

j o u r n a l homepage:

## a b s t r a c t

Molecular mass distribution measurements by pulsed gradient spin echo nuclear magnetic resonance (PGSE NMR) spectroscopy currently require prior knowledge of scaling parameters to convert from polymer self-diffusion coefficient to molecular mass. Reversing the problem, we utilize the scaling relation as prior knowledge to uncover the scaling exponent from within the PGSE data. Thus, the scaling exponenta measure of polymer conformation and solvent quality-and the dispersity (Mw = Mn) are obtainable from one simple PGSE experiment. The method utilizes constraints and parametric distribution models in a two-step fitting routine involving first the mass-weighted signal and second the number-weighted signal. The method is developed using lognormal and gamma distribution models and tested on experimental PGSE attenuation of the terminal methylene signal and on the sum of all methylene signals of polyethylene glycol in D2O. Scaling exponent and dispersity estimates agree with known values in the majority of instances, leading to the potential application of the method to polymers for which characterization is not possible with alternative techniques.

Ó 2017 Elsevier Inc. All rights reserved.

(S.J. Miklavcic),

(N.H. Williamson),

<!-- image -->

<!-- image -->

Synthetic polymers have distributions of molecular masses determined by their synthesis . Measuring the molecular mass distribution rather than its average is important because the dispersity can influence polymer properties . Absolute as opposed to relative measurements are needed when using polymer physics to fully realize the potential applications of a polymer . Only a handful of techniques can measure the absolute molecular mass distribution . The gold standard is size exclusion chromatography (SEC) using universal calibration , which does not always work . New techniques must be developed to aid in the advancement of polymer science.

Pulsed gradient spin echo nuclear magnetic resonance (PGSE NMR) is a powerful technique for obtaining the distribution of polymer self-diffusion coefficients D , from which the distribution of molecular masses M can be obtained by the scaling law

$$D ( M ) & = K M ^ { - \nu } ; \ \ M ( D ) = K ^ { 1 / \nu } D ^ { - 1 / \nu } . & & \quad \text {mass} \ p e q \\ & = \left ( 1 \right ) \quad \frac { ( 1 ) } { \text {diffusion} } \quad \frac { \text {mass} \ p e q } { \ } .$$

Access to chemical shift information and ease of sample preparation give PGSE NMR a competitive edge with respect to SEC. Chemical shift information , e.g. in a diffusion ordered spectroscopy (DOSY) plot , provides the ability to observe chemical heterogeneity and impurity. Sample preparation generally does not require filtration because contaminates from large particles such as dust do not impact the experiment. However, the scaling parameters of Eq. specific to that polymer-solvent system must be found by measuring h D i on fractionated samples of the polymer with known M . Therefore, currently all PGSE NMR-based methods which convert from D to M cannot independently measure the absolute molecular mass distribution .

In this paper we show that m in Eq. can be directly estimated from a single PGSE experiment in which the extremity (end-group) polymer signal can be spectrally resolved by a chemical shift from the polymer main-chain signal. The scaling exponent, m , is a measure of the polymer conformation as well as solvent quality , with bounds of m ¼ 1 = 3 for a perfectly coiled, impenetrable, polymer ball and m ¼ 1 for a perfectly straight polymer rod . The value of m ¼ 3 = 5 for a polymer in a good solvent was first predicted by P.J. Flory by a free energy minimization of the excluded volume and entropic contributions . (For this, m is also known as the Flory exponent.)

The method uses a mathematical framework which we first presented and applied in 2016. The method builds on the work of Viéville et al. who showed that the distribution of polymer self-diffusion coefficients is mass-weighted for the main-chain signal and number-weighted for the end-group signal. The key to directly obtaining the scaling exponent is our use of parametric distribution models to fit these two signals. The molecular mass dispersity, defined as Mw = Mn-the ratio between the mass-average and the number-average molecular masses, (and the molecular mass distribution if given Mn) can then be calculated from the parameter values estimated for the chosen model. To build up directly from the work of Viéville et al. , we prove this method on the same system: mixtures of polyethylene glycol (PEG) molecular mass standards solvated in D2O. In this way, Mn and Mw of each mixture are known. In the following, we introduce PGSE NMR and reproduce equations for the application of the lognormal and gamma distribution models. We then explain sample preparation and outline the procedure for obtaining m ; Mw = Mn ; and the molecular mass distribution. The method is then applied to three PEG samples and the results are compared to the known values.

In a PGSE NMR measurement of the self-diffusion coefficient D , the signal attenuation of a monodisperse species is given by the Stejskal-Tanner equation, where I 0 is the initial signal intensity, and the independent variable b is incrementally increased by stepping up the gradient pulse strength in successive scans . The signal attenuation of a polydisperse species will be multiexponential as a result of the distribution of diffusion coefficients. Such a superposition of exponential decays can be modeled by,

$$\begin{array} { r l } { r \, \text {mass} } & I ( b ) = I _ { 0 } \int _ { 0 } ^ { \infty } w ( D ) \exp ( - b D ) d D , } \\ { \text {always} } & I ( b ) = I _ { 0 } \int _ { 0 } ^ { \infty } w ( D ) \exp ( - b D ) d D , } \end{array}$$

where w ð D Þ is the distribution model of choice. We refer to w ð D Þ as the mass-weighted distribution of diffusion coefficients, and we note that in general the measured distribution is mass-weighted because it is proportional to the total number of protons and therefore, for a polymer, the total number of repeat units. However, the end-group signal can often be spectrally resolved for low molecular mass polymers (roughly less than 10 kDa ). The distribution of diffusion coefficients of the end-group is number-weighted (referred to as n ð D Þ ) because it is proportional to the number of molecules . If an appropriate model for w ð D Þ is chosen, then n ð D Þ can be obtained by the definition (see, e.g., )

$$\text {hetero-} \quad & \quad \ n ( D ) = \frac { w ( D ) / M ( D ) } { \int _ { 0 } ^ { \infty } w ( D ) / M ( D ) d D } \cdot \\ \text {es such} \quad & \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Using Eq. as M ð D Þ brings in m as an additional parameter of n ð D Þ . Note that the parameter K seen in Eq. will always cancel out as a constant in the numerator and denominator of Eq. .

Many distribution models exist, and the estimation of the distribution is an inverse problem for which there is no unique solution. We are physically motivated to use the lognormal distribution

,

$$\i t \text { from } & \quad 1 _ { \substack { D \in \Omega _ { D } ^ { 2 } \sqrt { 2 \pi } \\ \quad D \sigma _ { D } \sqrt { 2 \pi } } } \exp \left ( - \frac { ( \log D - \mu _ { D } ) ^ { 2 } } { 2 \sigma _ { D } ^ { 2 } } \right ) , \\ \text {reachable} & \quad \text {for which}$$

for which

$$\text {ad} \quad . \quad & \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \$$

and

$$\text {for the} \quad M _ { w } / M _ { n } = \exp \left ( \frac { \sigma _ { D } ^ { 2 } } { v ^ { 2 } } \right ) \\ \text {use of} \quad$$

and the gamma distribution

,

$$\text {seen the} \quad w ( D ) = \frac { \beta ^ { \alpha } } { \Gamma ( \alpha ) } D ^ { \alpha - 1 } \exp \left ( - \beta D \right ) , \\ \text {coluted} \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

for which

$$\text {prove this} \\ \text {ol} \left ( \text {PEG} \right ) \quad n ( D ) = \frac { \beta ^ { z + 1 / v } } { \Gamma ( \alpha + 1 / v ) } D ^ { x + 1 / v - 1 } \exp \left ( - \beta D \right ) , \\ \text {and } M _ { w } \\ \text {e PGSSE}$$

and

$$\text {els. We} \quad M _ { w } / M _ { n } = \frac { \Gamma ( \alpha + 1 / v ) \Gamma ( \alpha - 1 / v ) } { \Gamma ( \alpha ) ^ { 2 } } , \\ \text {on. The} \quad \\$$

because both distributions meet the criterion that the probability of negative molecular masses must be zero. The complete derivation of equations and case studies for use of the lognormal and gamma distribution models for estimating molecular mass distributions are presented in our previous publication . We reproduce a few more equations for these models, including the molecular mass distribution functions, in the .

The method for estimating m and Mw = Mn from the PGSE attenuation of the main-chain and end-group signals follows a two-step, least squares fitting routine. Benjamini and Basser found that imposing parameter constraints in a two-step fit of 2-D relaxation and diffusion NMR measurement data restricts the solution set of the second fit and leads to a significant reduction in the amount of data required for a stable fit . By fitting our data in two steps we take advantage of the large signal of the main-chain peak, from which precise parameter estimates are obtained. A global (simultaneous) fit of both signal attenuations is more ill-posed, and thus less accurate. First, the sum of the main-chain and end-group signals is fit with the chosen distribution model. Second, the end-group signal is fit with the associated number-weighted distribution model. Parameter estimates from the first fit are used as constraints such that the only free parameter in the second fit is m . Given that the model choices are appropriate, we take into account the effect which random noise in the data has on the accuracy of the first fit by bounding the constrained parameters to within the value  1 = 2 the standard deviation from the first fit. The Mw = Mn is defined by the estimated parameters. It is well known that the numberaverage molecular mass can be estimated from end-group analysis of a 1-D NMR spectrum . Together, Mn and Mw = Mn define the parameters of the molecular mass distribution function.

The method was tested on three PEG mixtures with Mn ¼ 822g = mol and Mw = Mn ¼ 1 : 81 for mixture 1, Mn ¼ 667g = mol and Mw = Mn ¼ 2 : 49 for mixture 2, and Mn ¼ 441g = mol and Mw = Mn ¼ 1 : 41 for mixture 3. To make each mixture, Polyethylene glycol (PEG) molecular mass standards (Mw = Mn &lt; 1 : 2) (Polymer Standards Services Inc., Germany) were mixed together in defined ratios to create molecular mass distributions which were roughly lognormal in shape (though not continuous). (Refer to the for standard molecular masses and

their fractional makeup of the mixtures.) The designed mixtures were diluted to 0.1% (w/w) PEG in D2O (99.9 atom % deuterium, Sigma-Aldrich, USA) and transferred to 5 mm NMR sample tubes.

To measure PEG self-diffusion, pulsed gradient stimulated echo experiments were performed on the mixtures at 20 ° C using a 600 MHz Avance III HD NMR spectrometer (Bruker BioSpin, Germany) equipped with a Micro5 probe, 5 mm radio frequency coil, and Diff30 (11.7 T/m maximum) gradient set. Sinusoidal gradient pulse shapes were chosen, for which the b in the Stejskal-Tanner equation (Eq. ) is

$$b & = ( \gamma g \delta ) ^ { 2 } \frac { 4 } { \pi ^ { 2 } } \left ( \Delta - \frac { \delta } { 4 } \right ) , \\ \\$$

with proton gyromagnetic ratio c , time lapse D between the leading edges of the gradient pulses, gradient pulse duration d , and gradient strengths g . The experiments used D = 50 ms, d = 1.58 ms, repetition time = 10 s, 16 scans, and 32 gradient points with g varied linearly to 4 T/m for mixture 1 and mixture 2 and 3.2 T/m for mixture 3. Each experiment took 1 1 2 h.

The least-squares fitting routine was implemented in MATLAB R2016a (Mathworks, Natick, USA) and incorporated a Monte Carlo error analysis . The 95% confidence intervals were assessed from the distributions of parameter values obtained from the Monte Carlo steps, in which the data was refit after the addition of Gaussian noise with the same standard deviation as that of the initial fit. Monte Carlo estimates of m incorporated the errors of both fitting steps. The fitting procedure used 100 random parameter initializations and 1000 Monte Carlo steps. The fitting routine and data sets from the three mixtures are available in the

.

We first demonstrate how the method works on PEG mixture 1 and second compare the results of m and Mw = Mn to the known values for all three mixtures. The PGSE experiment measures the signal attenuation of the main-chain methylene peak at 3.7 ppm and the two sets of triplets arising from the two methylenes closest to the hydroxyl group on the PEG extremity. (The proton spectrum from the smallest gradient (or b ) value is shown in a.) We define the mass-weighted signal as the sum of all methylenes (not just the main-chain peak) and the number-weighted signal as the triplet from the terminal methylene. We take the integral values directly from a to obtain Mn ¼ 900 g = mol, compared to the known value of Mn ¼ 820 g = mol. (We do this for simplicity and to point out that all the necessary information is contained within this one PGSE measurement. Weighting effects from spinspin and spin-lattice relaxation , diffusion, and even spectral overlap can be taken into account with more rigorous methods. Using a spectrum from a 1-D free induction decay results in essentially the same Mn value.) Following the methods for use of the lognormal and gamma distribution models outlined above, the experimental results, fits, estimated number and mass-weighted diffusion coefficient distributions, and estimated molecular mass distributions are shown in b-d. The known molecular mass distribution of the mixture is represented by a sum of lognormal distributions, defined by the mass fractions and the reported values of Mn and Mw = Mn of the standards composing the mix. Though the multimodal shape cannot be reproduced, the estimated molecular mass distributions accurately depict the width of the known distribution.

Fig. 1. Results for PEG mixture 1 for the lognormal (red) and gamma (blue) models showing (a) the methylene signal integral definitions on the spectrum from the first PGSE gradient point, (b) the experimental signal attenuation for the mass-weighted signal from the sum of all methylenes (circles) and number-weighted, terminal methylene signal (squares), the mass-weighted and number-weighted lognormal (red dot-dash) and gamma (blue solid) model fits, (c) the estimated mass-weighted (solid) and number-weighted (dashed) distributions of diffusion coefficients, and (d) the molecular mass distribution estimates compared to the molecular mass distributions, individually (dotted black) and as a sum (solid black), arising from the standards composing the mix. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

<!-- image -->

The estimated values of m and Mw = Mn for this mixture (mixture 1) as well as mixture 2 and mixture 3 are shown in . The estimates can be compared to the known values of Mw = Mn and m . The known value of m ¼ 0 : 50  0 : 02 was obtained from a fit of Eq. to the mean diffusion coefficient values of the individual molecular mass standards (see ) and

is comparable to previously published values for PEG in D2O of

521

m ¼ 0 :  ¼  The estimates of m from the lognormal and gamma listed in differ due to strong sensitivity of the method to model choice. This is evident in c where two very similar massweighted diffusion coefficient distributions arise from the first fit, but the constraints lead to drastically different number-weighted diffusion coefficient distributions from the second fit. Certain models in certain instances, such as the gamma for mixture 1 and the lognormal for mixture 2, resulted in accurate m estimates compared to the known value, which then led to better estimates of Mw = Mn than those of the alternative models. Both models accurately estimated Mw = Mn for mixture 3 even though their estimates of m were off, potentially because small values of Mw = Mn are less sensitive to errors in m , as seen by Eqs. . For 8 out of the 12 estimated values of m and Mw = Mn in , the known values are within the 95% confidence intervals.

0

:

011 at 25

°

C

and

m

0

:

539

0

:

003 at 30

°

C

.

Estimates were quite successful considering that the method only assumed that M and D scale by Eq. and that the distribution models were appropriate. A wide range of polymers follow the scaling relation . The universal calibration method by which absolute molecular mass can be obtained with SEC relies on an analogous scaling relation known as the Mark-HouwinkSakurada equation. A major limitation then is the assumption of a distribution shape. Knowledge of the polymerization reaction kinetics can help inform on an accurate model choice. For instance, the gamma-in a parameterization widely known as the Schulz distribution -and lognormal distributions of molecular mass have been derived from certain polymer reaction mechanisms . Relative changes in m for a given model should not depend on model choice and so the method may be useful for measuring the change in solvent quality as a function of system parameters such as solvent or temperature. Another limitation is the capability to resolve an end-group signal, which diminishes with increasing molecular mass due to increasing peak broadness and decreasing signal.

The scaling exponent and absolute molecular mass are fundamental to realizing the full potential of a polymer. Demands for new applications are driving the complexity of new polymers for which traditional characterization methods do not always work. We show a method by which the scaling exponent and absolute molecular mass distribution characteristics can be obtained directly from a single PGSE measurement performed on a polymer without fractionation.

Table 1 Results of m and Mw = Mn, with 95% confidence intervals, compared to the known values for the three PEG mixtures.

|   Mixture | Known     | Lognormal   | Gamma     |
|-----------|-----------|-------------|-----------|
|         1 | m 0 : 50  0 : 02           | m 0 : 54  0 : 05             | m 0 : 50  0 : 11           |
|         2 | 0 : 50  0 : 02           | 0 : 49  0 : 03             | 0 : 41  0 : 07           |
|         3 | 0 : 50  0 : 02           | 0 : 61  0 : 04             | 0 : 58  0 : 14           |
|           | M w = M n | M w = M n   | M w = M n |
|         1 | 1.81      | 1 : 60  0 : 13             | 1 : 71  0 : 42           |
|         2 | 2.49      | 2 : 23  0 : 23             | 3 : 03  1 : 37           |
|         3 | 1.41      | 1 : 38  0 : 05             | 1 : 41  0 : 24           |

## Acknowledgements

This research was funded by the South Australian Government Premier's Research and Industry Grant project 'A Systems Approach to Surface Science', as well as the Australian Government International President's Scholarship (IPS).

## Appendix A. Supplementary material

Supplementary data associated with this article can be found, in the online version, at .

## References

[1]

[2]

[3]

[4]

[5]

[6]

[7]

[8]

[9]

[10]

[11]

[12]

[13]

[14]

[15]

[16]

[17]

[18]

[19]

[20]

[21]

[22]

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

| [23]   |      | [31]      |
|--------|------|-----------|
| [24]   | M n  | [32] [33] |
| [25]   |      | [34]      |
| [26]   |      | [35]      |
|        |      | [36]      |
| [28]   |      | [37]      |
|        | T 1  | [38]      |
| [29]   |      | [39]      |
| [30]   |      | [40]      |

.

.

.

.

.

.

.

.

.

.

.