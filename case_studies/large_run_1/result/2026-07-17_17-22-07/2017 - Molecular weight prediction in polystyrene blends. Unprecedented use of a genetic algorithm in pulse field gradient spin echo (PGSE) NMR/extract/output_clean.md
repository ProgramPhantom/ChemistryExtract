## Soft Matter

## PAPER

<!-- image -->

Cite this: DOI: 10.1039/c7sm01569k

Received 4th August 2017, Accepted 31st August 2017

DOI: 10.1039/c7sm01569k

## Introduction

Diffusion NMR spectroscopy is currently used to study polymers, organometallic complexes, nanoparticles as well as host-guest systems, helicates, grids, and more. 1,2 The physical observable usually derived from the diffusion NMR experiment is the diffusion coefficient, D , 3 which is related to molecular weight ( M w) by using calibration curves built from adequate standards. 2 b ,4 We have recently introduced the first universal calibration curve (UCC) that allows the estimation of weight-average molecular weights in polystyrene (PS) monodisperse samples. 5 In such samples the single frequency ITAMeD algorithm has been successfully applied. 6 Also recently, Zhang and coworkers have presented an alternative iterative regularization method based on TRAIn, whose strength is shown in non-symmetrically distributed diffusion NMR data. 7

In general, the distribution of diffusion coefficients could be deduced from experimental data by the inversion of Laplace Transform (ILT), but its strong vulnerability to noise and

a Department of Chemistry and Physics, Research Centre for Agricultural and Food Biotechnology (BITAL), University of Almerı ´a, Ctra. Sacramento, s/n, 04120, Almerı ´a, Spain. E-mail: ifernan@ual.es

b

Department of Informatics - CIESOL, ceiA3, University of Almerı ´a,

Ctra. Sacramento, s/n, 04120, Almerı ´a, Spain

c Chemical Laboratory, AIMPLAS (Plastic Technology Center), Parque Tecnolo ´gico, C/ Gustave Eiffel 4, 46980, Paterna, Spain

† Electronic supplementary information (ESI) available: Experimental section, algorithm description and solutions (5 full programmed codes, 30 figures and 9 tables). See DOI: 10.1039/c7sm01569k

<!-- image -->

<!-- image -->

## Molecular weight prediction in polystyrene blends. Unprecedented use of a genetic algorithm in pulse field gradient spin echo (PGSE) NMR †

Francisco M. Arrabal-Campos, a Jose ´ D. A ´lvarez, b Amador Garcı ´ a-Sancho c and Ignacio Ferna ´ndez * a

A genetic algorithm that uses boxcar functions (diffGA) has been applied for the first time in PGSE NMR. It reconstructs accurate diffusion coefficients for all the components of the mixture, and therefore predicts correct weight-average molecular weights for all of them. The results reported herein complement those obtained with established methods such as ITAMeD, CONTIN and TRAIn algorithms, and provide a detailed solution picture. Its robustness and limits have been stretched in order to ascertain the minimum separation within diffusion coefficients or relative proportion between components. In addition, the new genetic algorithm has been also applied to a mixture of small molecules, providing excellent results at very low computational times.

numerical instability has induced the appearance of alternative approaches. These are mostly divided in total band shape and single frequency methods. Examples of the former are DECRA, 8 SCORE 9 MCR 10 and OUTSCORE. 11 Regarding the latter, the simplest is the plain curve fitting, such as the LevenbergMarquardt statistical method. 12 Others include CONTIN, 13 SPLMOD, 14 and Maximum Entropy. 15 A recent algorithm based on the combined used of Maximum Entropy and l1 hybrid regularization, called PALMA, has been successfully applied in complex mixtures. 16 The polydispersity index (PDI) has been also estimated through diffusion NMR measurements, either employing the differential diffusion profile observed for main polymer chain signals versus the extremity signals, 17 or with the application of gamma or log-normal distribution models. 18 Urbanczyk et al. have described a new method that uses a tailored regularization term designed to automatically tune to the different polydispersities of the sample, 19 which gave excellent results in the monitorization of polydispersity changes in real time processes.

In recent years, there has been increased interest in using gradient HPLC techniques, for determining the compositional drift of copolymers, the composition of polymer blends, or for the analysis of polymer additives. 20 In this area of polymer blends, the existing NMR methods do not provide accurate D -values and therefore do not predict correctly weight-average molecular weights. Advantages of PGSE NMR techniques over size exclusion chromatography (SEC) are grounded on the lack of column conditioning with no need to optimize and purify the eluent prior to use. The third and probably most important difference is that PGSE NMR affords a higher resolution compared to SEC, where only a limited number of peaks can be resolved showing usually broad peaks of high uncertainty.

We describe herein the first application of a new procedure based on a genetic algorithm that uses boxcar functions (diffGA) for the quantitative determination of the diffusion coefficients and, therefore, accurate prediction of molecular weights. The method has been tested on a ternary blend of monodisperse PS polymers in the validity range of Flory's law ( i.e. absence of obstruction or concentration effects on diffusion measurements). 21 We also present the comparison of the method with commonly applied algorithms such as ITAMeD, CONTIN and TRAIn. It is worth mentioning that we always refer to M w in terms of averages since synthetic polymers have polydispersity. The developed diffGA belongs to the larger class of evolutionary algorithms where a population of randomly generated individuals is created and the fitness function is used to determine the relative merit of each one. 22 These genetic algorithms (GAs) differ from the conventional feature-selection methods in that they tend to concentrate in spectral regions of the greatest relevance 23 instead of selecting single variables scattered throughout the spectrum with the assumption that no correlation exists among them. 24 There are many sources in the literature that describe the inner workings of the GA, and we refer the interested reader to these sources. 25

As mentioned before, the D -values are commonly estimated using the PGSE technique, which is based on the signal attenuation during the diffusion time D 0 , which is corrected by an amount that depends on the specific pulse sequence and the gradient shape used as described by Sinnaeve et al. 26

$$E _ { \text {diff} } = e ^ { - D _ { 7 } e _ { \text {eff} } ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g ^ { 2 } \Delta ^ { \prime } } & & ( 1 ) & & D _ { 2 } \\$$

D is the translational diffusion coefficient of the molecule to which the signal belongs, g eff is a linear combination of the gyromagnetic ratios of the nuclei studied depending on the coherence transfer pathway of the experiment, d is the PFG duration, g is the maximum gradient strength (which corresponds to 50.1 G cm  1 in our spectrometer), and s is the gradient shape factor. For a continuous distribution of diffusion coefficients, A ( D ), eqn (1) could be replaced by the following integral equation to describe the signal decay.

ð

$$E _ { d i r } ( g ) = \int _ { 0 } ^ { \infty } A ( D ) e ^ { - D _ { 7 } e ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g ^ { 2 } \Delta ^ { \prime } } d D & & ( 2 ) & \quad e t \ \ a n d \\$$

Kazimierczuk 6 and Zhang 7 independently, have nicely reviewed the different regularization methods implemented so far, and thoroughly analyzed the numerical difficulties that all of them contains. The GA introduced herein, although never used in PGSE NMR, is an evolutionary approach that has been used in many applications as varied as the conformational analysis of biomolecules, 27 X-ray fluorescence analysis of thin films, 28 near-infrared determinations of glucose in biological mixtures, 29 selection of a multi-stage system for bio solid management, 30 soy sauce classification 31 or in the analysis of Raman spectra. 32

## Experimental methods

## Samples

Polystyrene samples (PS5950, PS60000 and PS1020000) were purchased from Polymer Standards Service (Mainz, Germany). Their corresponding M w, M n and PDI values are given in Table S1 (ESI † ). Benzened 6 (C6D6) and chloroformd 1 (CDCl3) were purchased from Eurisotop (Saint-Aubin, France). C6D6 and CDCl3 were dried over CaH2 and vacuum transferred onto 3 Å molecular sieves prior to use. All other reagents and solvents were of commercial quality and were used without further purification. The NMR sample constituted by the three PS polymers was prepared by just adding 0.6 mg of each polymer together with 0.6 mL of C6D6 in an oven-dried 5 mm J-Young NMR tube. The NMR sample constituted by toluene, chloroform, dicloromethane, acetone, dimethylsulfoxide and acetonitrile was prepared by adding 10 m L of each solvent and 0.6 mL of CDCl3 in an oven-dried 5 mm J-Young NMR tube. The valves were closed and both NMR samples were used without further steps.

## NMR spectroscopy

All measurements were performed on a Bruker Avance III 500 spectrometer equipped with a microprocessor-controlled gradient unit and a third radiofrequency channel using an indirect 5 mm TBI 1 H/ 31 P/BB triple probe with an actively shielded Z -gradient coil. The spectral reference used was internal tetramethylsilane for 1 H. The shape of the gradient pulse was sinusoidal, and its strength varied automatically during the experiments. The calibration of the gradients on the spectrometer was carried out via a diffusion measurement of HDO in D2O at ambient temperature. The D values varied from 100 to 200 ms, and the d values from 3 to 12 ms. The gradient strength was incremented in steps of 4%, so that 23 points could be used for regression analysis. The recovery delay was set to 10 s. The number of scans per increment were 64 and typical experimental times were around 6 h. All experiments were run without spinning. The standard Bruker pulse program, stegp1s, employing a stimulated echo sequence with monopolar pulses and 1 spoil gradient was utilized. Gradient recovery delays were set to 0.2 ms. To check the reproducibility and lack of convection, three different measurements with different D parameters are always carried out. 33 ITAMeD solutions were obtained by the use of the algorithm provided by Urbanczyk et al. 19 The number of iterations was set to 10 000 and the sparsity-promoting l to 10  5 . CONTIN and TRAIn solutions were obtained using the algorithms provided by Provencher, 13 and Xu and Zhang, 7 respectively.

## Results and discussion

We consider first the distribution of A ( D ) as a superposition of boxcar functions (eqn (3)).

X

$$A ( D ) = \sum _ { i = 1 } ^ { n } \Pi _ { D _ { i } \pm \omega } ( d ) _ { i } \quad \quad ( 3 )$$

For our purposes, n is defined as the number of boxcar functions that the diffGA will use to characterize the final number of components we are searching for, d is the feasible domain, Di is the diffusion coefficient, and w is the uncertainty represented as the broadness of the boxcar function solution. These types of functions are currently used in apodization procedures and in medical imaging, 34 and they are obtained from the subtraction of two Heaviside functions H (eqn (4)): 35

$$\Pi _ { a , b } ( d ) = H ( d - a ) - H ( d - b )$$

In our algorithm, the boxcar function needs to be adapted in order to solve diffusion coefficients, and therefore, the function will start at '' a '', that equals D  w /2, and ends at '' b '', that equals D + w /2 (eqn (5)).  

$$( a , b ) = \left ( D - \frac { \omega } { 2 } , D + \frac { \omega } { 2 } \right ) = D \pm \omega & & ( 5 ) & & \text {of} \ t \\$$

This distribution of diffusion coefficients, A ( D ) is zero over the entire domain of diffusion coefficients except for a single interval where it is equal to the estimated self-diffusion coefficient D .

Thus, the fitness function that gives a score for each individual, and is a measure of the goodness of the solution, could be reformulated as eqn (6).

$$\min F ( A ) \equiv f ( D ) = \left \| C \cdot \sum _ { i = 1 } ^ { n } \Pi _ { D _ { i } \pm \omega } ( d ) _ { i } - E _ { d i r } \right \| _ { 2 } \quad ( 6 ) \quad \text {estab} \quad \begin{matrix} A \\ 6 \end{matrix}$$

Methods of optimization such as ITAMeD, CONTIN or TRAIn, use a derivative-based approach, that locally looks to see what direction to move in (based on the gradient of the function at the current iteration) and then calculates the new current solution after deciding how far to move along that path. The regularization term in these cases avoid the overfit. Genetic algorithms are used when no information is available about the gradient of the function at the evaluated points. The function itself does not need to be continuous or differentiable and, compared to purely local methods, genetic algorithms have the advantage that they do not necessarily remain trapped in a suboptimal local maximum or minimum of the target function. Since information from many different regions is used, a genetic algorithm can move away from a local maximum or minimum if the population finds better function values in other areas of the definition domain. 35 The sparsity of the result is guaranteed by the boxcar function, which is itself an indirect way of introducing a regularization term. For this reason, the quadratic distance is sufficient to evaluate the minimization. This new way to solve mixture problems can be established incorporating a natural evolution into an algorithm. Table S10 and Codes S1-S3 (ESI † ) shows the implementation of the diffGA algorithm in PGSE diffusion NMR problems.

The performance of our diffGA is illustrated by analyzing a ternary blend of monodisperse polystyrene (PS) polymers in benzened 6. The results afforded by some other regularization methods are also shown for comparison issues, and it will prove the strength of our approach regarding the accurate calculation on D -values, and eventually the correct prediction of the corresponding molecular weights. We found that the PS mixtures were well-suited for the tests on multi-exponential fitting methods, because all the protons in the three PS systems are notdependent on molecular weight and resonate at the same frequency. Fig. 1 shows a rendering of the raw PGSE data for the blend of PS5950, PS60000 and PS1020000 in a 1 : 1 : 1 w/w ratio. Thus, the only way of distinguishing between them using NMR is to perform PGSE experiments and solve their diffusion coefficients.

Fig. 1 Raw 1 H NMR PGSE (STE) data showing the aromatic region of the ternary blend of polymers in benzened 6.

<!-- image -->

Analysis of the overall intensity attenuation showed how established algorithms such as ITAMeD, CONTIN and TRAIn work well (Table 1). Interestingly, the diffGA recovered, with errors below 4.5%, the three diffusion coefficients reproducing the data obtained from measurements on single components, 5 as shown in Table 1.

Both ITAMeD and CONTIN could recover the diffusion coefficients of the three PS polymers of the blend, although not very accurately. For ITAMeD, the deviations are below 10% for PS5950, whereas for PS60000 and PS1020000 the errors are 12% and 88%, respectively. Interestingly, the TRAIn solution can only ascertain the D -value for the polymer of highest molecular weight.

Fig. 2 illustrates the comparison between methods where the reference diffusion coefficients (dotted lines) were deduced by either monoexponential fitting of the signals obtained for single-compound samples, or by applying ITAMeD, CONTIN or TRAIn. The grey spots correspond to the centroids of the diffGA bars, which overlay the reference dotted lines. Centroid calculation and programming codes are provided in detail in the ESI. † Assuming the error bars on the ''true'' diffusion coefficients are of the order of 10%, there is no real difference between CONTIN and diffGA. In fact, the comparison of the f ( D ) (eqn (6)) for ITAMeD, CONTIN and DiffGA with the real attenuation provides RMS values of 0.001056, 0.001127 and 0.001123, respectively, for the three methods under evaluation. As is deduced from Table 1, the lowest RMS value does not necessarily imply the method achieves the best solution, due to RMS values depending on the parameters tackled in the regularization term, since we are dealing with ill-posed problems. In this sense, when we take the ''converged'' diffGA solution and stick it in as the initial iteration for ITAMeD or CONTIN, the solution moves away from the starting point, indicating that the true source of advantage is the regularization function, which is not the same, and which means different mathematical problems are being solved by the different methods. In contrast, when ITAMeD or CONTIN solutions are given to diffGA, the solutions progressively move to the ''true'' values within iterations.

Table 1 Diffusion values (10  9 m 2 s  1 ) at room temperature (294 K) and diff errors (%) a calculated through the different methods

|            |   ITAMeD |   CONTIN | TRAIn   |   DiffGA |
|------------|----------|----------|---------|----------|
| PS5950     |   0.1801 |   0.1760 | 0.1768  |   0.1975 |
| Diff a (%) |      6.5 |      8.6 | 8.2     |      4.5 |
| PS60000    |   0.0441 |   0.0414 | b       |   0.0507 |
| Diff a (%) |     12.7 |     18.0 | -       |      0.9 |
| PS1020000  |   0.0011 |   0.0101 | b       |   0.0096 |
| Diff a (%) |     88.3 |      7.4 | -       |      2.1 |

Fig. 2 Comparison between ITAMeD (orange line), CONTIN (red line), TRAIn (green line) and diffGA (black line and grey spots). Reference D -values are marked with dotted lines.

<!-- image -->

The employed GA is the one implemented in the global optimization toolbox of MATLAB s , however, a comprehensive computational study was accomplished in order to find the best set of parameters. Thus, for population sizes of ca. 10000, the GA provided values of 0.025 when the fitness function was evaluated. When the population size was increased up to 30000, the value of the fitness function decreased exponentially down to 0.005 (Fig. S24, ESI † ). Moreover, if we observe how the fitness function changes along with the uncertainty over discretization, population size and elite count, the convergence is reached when the function [ U /( D Ps Ec)] is ca. 0.4 (Fig. S25, ESI † ).

Although GAs are relatively immune to the effects of noise in the fitness function, 25 the probabilistic nature of the search could suggest that the GAs may lack robustness in finding solutions in the presence of noise. To prove its robustness, we ran our diffGA four consecutive times employing a population size of 1 000 000 and an elite value of 20. Fig. 3 illustrates these results and reveals standard deviations lower than 0.005 -10  9 m 2 s  1 in the estimation of the three diffusion coefficients (Table S9, ESI † ).

Fig. 3 Overlay of four consecutive solutions of the diffGA (population size of 1 000 000 and elite value of 20).

<!-- image -->

As mentioned before, the number of boxcar functions used in the GA is the main factor in terms of computational cost, where the smaller the number the lower the amount of arithmetic operations per iteration the algorithm needs. When this number is rather small, it may not be enough to cover all the existing components present in the mixture and large errors in the calculation of the D -values are expected. On the other hand, when a large number of boxcar functions is entered, it ensures covering all components in the sample, at the expense of a larger computational cost. A trade-off between these two factors was found in our case by selecting ten as the number of boxcar functions, spending 16 hours for the calculation of the D -coefficients (Table 2). Advanced parallel programming would be one of the possible solutions for minimizing computational times.

The processing time for CONTIN, reimplemented in MATLAB and with the diffusion domain bucketized in ca. 140 points, was of the same order of magnitude as with diffGA. In contrast, for ITAMeD and TRAIn the time elapsed was only seconds. All the calculations were run on a Windows 64-bit computer PC with an intel i7 3.5 GHz processor. The three diffGA D -values together with the recently described universal calibration curve (UCC) for PS samples, 5 were employed for the weight-average M w predictions. To our delight, the estimated M w compared to real values (Table 2), fitted excellently well with errors below 6.0%. In contrast, when the predictions are intended with alternative algorithms, less accurate weights are obtained (Table S17, ESI † ), supporting the diffGA method as the most reliable for this specific polystyrene blend. To test the vulnerability to noise of our diffGA, we run Monte-Carlo simulations on a bimodal

Table 2 DiffGA diffusion values (10  9 m 2 s  1 ) a and UCC-predicted weight-average M w

|      PS |      D |   D Z (10  3 ) b |   Av- M w (Da) c |   Diff d (%) |
|---------|--------|------------------|------------------|--------------|
|    5950 | 0.1975 |           0.1275 |             5372 |          9.7 |
|   60000 | 0.0507 |           0.0322 |            58811 |          0.4 |
| 1020000 | 0.0096 |           0.0058 |          1100199 |          7.8 |

Table 3 Noise vulnerability test. Relative errors between D 1 and D 2 values a and those obtained from the simulated attenuations

|   Noise (%) | D 1 (10  9 m 2 s  1 )   | D 2 (10  9 m 2 s  1 )   |   Diff 1 (%) |   Diff 2 (%) |
|-------------|-------------------------|-------------------------|--------------|--------------|
|         0.1 | 0.067  0.002                         | 0.499  0.005                         |         3.07 |         2.88 |
|         0.5 | 0.071  0.004                         | 0.518  0.012                         |         9.23 |         6.80 |
|           1 | 0.073  0.007                         | 0.553  0.039                         |        12.31 |        14.02 |
|          10 | 0.033  0.038                         | 0.429  0.216                         |        49.23 |        44.54 |

1: 1 ratio Gaussian distribution of diffusion coefficients centred at 0.065 -10  9 and 0.485 -10  9 m 2 s  1 (Fig. S12, ESI † ). We could follow the dependence of the D -values with respect to the amount of experimental noise. Fig. S13-S16 (ESI † ) show the simulated attenuations at the levels of noise of 0.1, 0.5, 1 and 10%. The comparison between the correct D values and those obtained from the simulations are summarized in Table 3. For levels of noise above 0.5% the errors obtained are above 6% which are comparable to compelling methods such as ITAMeD. 19

The strength of our algorithm was tested with two approaches based on simulation. On one hand, we varied the separation within diffusion coefficients on a simulated binary mixture of 1:1 ratio, and applied our diffGA method to solve an overall of ten mixtures. One of the simulated components was fixed at 0.032 -10  9 m 2 s  1 , and the other one varied from 0.032 -10  9 m 2 s  1 in steps of 0.0016 -10  9 m 2 s  1 . Remarkably, with a separation of D -values above 0.0080 -10  9 m 2 s  1 ( n = 5, Fig. 4a) the diffGA method could solve both components with relative errors below D D rel = 0.04 -10  9 m 2 s  1 . Fig. 4a shows the relative errors obtained on each simulation compared to the correct D -values.

The second approach was based on the proportion in which the two components coexist. In this sense, the ratio between the two components of fixed diffusion coefficients (0.032 and 0.113 -10  9 m 2 s  1 ) was varied from 1 : 0.1 to 1 : 1. Fig. 4b shows the errors committed after applying diffGA on these ten mixtures. Interestingly, our method provided excellent results when the two components were at ratios higher than 1: 0.6 ( D D rel o 0.035 -10  9 m 2 s  1 ), and could not solve the mixtures at ratios below this limit.

Fig. 4 Relative errors committed varying (a) the separation within diffusion coefficients on a simulated 1: 1 mixture; and (b) the relative ratio (from 1 : 0.1 to 1:1) on a simulated mixture of two components at fixed diffusion coefficients.

<!-- image -->

Table 4 ITAMeD and diffGA diffusion values (10  9 m 2 s  1 ) a at room temperature (294 K) for a mixture of small molecules

| Molecule   |   D , ITAMeD |   D , diffGA |   Diff (%) |
|------------|--------------|--------------|------------|
| Acetone    |         2.44 |         2.59 |        5.7 |
| Toluene    |         2.26 |         2.37 |        4.4 |
| Chloroform |         2.41 |         2.53 |        4.7 |
| DCM        |         2.93 |         3.07 |        4.5 |
| DMSO       |         1.90 |         1.99 |        4.5 |
| ACN        |         2.71 |         2.87 |        5.5 |

- a 1 HPFG-STE measurements were performed at room temperature (294 K).

In order to examine the scope of our method, the sample was also used in dynamic light scattering (DLS) routine experiments on a Malvern zetasizer instrument, a technique widely used for soft matter. The software enabled collection of particle size distribution data as well as the absolute measurement of intensity. Fig. S26 (ESI † ) is the intensity size distribution obtained from the sample constituted by the three polymers in benzened 6. The analysis showed two z -average radii (the mean radius based upon the intensity of scattered light) of 27.9 and 5.1 nm. The first size fits reasonably well with the hydrodynamic radii of 34.7 nm obtained (through StokesEinstein) 1 when using the D -value of 0.0090 -10  9 m 2 s  1 for PS1020000. The second radius corresponds to the mean value of 4.5 nm, estimated from the two radii deduced for PS5950 ( r H 1.8 nm) and PS60000 ( r H 7.1 nm). This bimodal distribution confirms that DLS routine analysis is not able to find the three components, and reinforces the applicability of diffusion NMR for solving these types of blends, no matter the size of the components.

It is important to mention that when discovering discrete components, the diffGA shows outstanding results, comparable to ITAMeD, and remarkably, with computational times of the order of seconds. In fact, the application of both ITAMeD 6 and diffGA, on a sample constituted of equal amounts of small molecules, provided almost equal results with differences below 5.7% (Table 4 and Fig. S18-S22, ESI † ).

The successful application to discrete resonances enables the use of our diffGA in routine analysis, but no apparent advantage is observed when compared to established methods.

## Conclusions

Mixture analysis is a complex task especially when the polymers have the same nature (comprise identical NMR spectra), and there are only differences in their molecular weight. We have described a genetic algorithm (diffGA) which has been applied to PGSE diffusion NMR for the first time. The results showed that our approach reconstructs satisfactorily diffusion coefficients in a ternary blend of PS polymers. A comparison with established methods such as ITAMeD, CONTIN and TRAIn has been performed, and shows that only diffGA did not fail in the estimation of accurate D -values and, thus, in the prediction of average-weight molecular weights. Similarly, diffGA has proven its strength and rapidity in a mixture of small molecules, showing comparable performance and noise vulnerability to ITAMeD. The number of boxcar functions used in the GA is the main factor in terms of computational cost. In our hands, with ten boxcar functions and selecting three as the number of components, the calculation of the D -coefficients needed 16 hours. The new algorithm outlined in this work is expected to be extremely useful for many applications in the polymer field, and specifically in the area of blends. Current work is focused on the programming of the algorithm towards faster performances, and on its applicability to blends based on similar molecular weights and/or the higher polydispersity of their components.

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

Financial support was given by Bruker Espan ˜ola SA and Junta de Andalucı ´a (Spain) under the project number P12-FQM-2668. J. D. A. thanks the Spanish 'Ramo ´n y Cajal' program for funding. A. G.-S. thanks the European Commission for financial support (FP7-613771). We thank Prof. J. F. Ferna ´ndez-Sa ´nchez from the University of Granada (Spain) for his help on DLS measurements.

## Notes and references

- 1 For applications focused on inorganic and organometallic chemistry, see: ( a ) P. S. Pregosin, P. G. A. Kumar and
- I. Ferna ´ndez, Chem. Rev. , 2005, 143 , 2977-2998;
- ( b ) A. Macchioni, G. Ciancaleoni, C. Zuccaccia and
- D. Zuccaccia, Chem. Soc. Rev. , 2008, 37 , 479-489;
- ( c ) L. Avram and Y. Cohen, Chem. Soc. Rev. , 2015, 44 , 586-602.
- 2 ( a ) D. Smejkalova and L. Piccolo, Environ. Sci. Technol. , 2008, 42 , 8440-8445; ( b ) D. Li, I. Keresztes, R. Hopson and P. G. Williard, Acc. Chem. Res. , 2009, 42 , 270-280; ( c ) G. Canzi, A. A. Mrse and C. P. Kubiak, J. Phys. Chem. , 2011, 115 , 7972-7978; ( d ) J. H. Lamm, P. Niermeier, A. Mix, J. Chmiel, B. Neumann, H. G. Stammler and N. W. Mitzel, Angew. Chem., Int. Ed. , 2014, 53 , 7938-7942; ( e ) R. Cao, A. Nonaka, F. Komura and T. Matsui, Food Chem. , 2015, 171 , 8-12; ( f ) W. Ge, J. H. Zhang, C. M. Pedersen, T. Zhao, F. Yue, C. Chen, P. Wang, Y. Wang and Y. Qiao, ACS Sustainable Chem. Eng. , 2016, 4 , 1193-1200.
- 3 ( a ) E. D. Stejskal and J. E. Tanner, J. Chem. Phys. , 1965, 42 , 288-292; ( b ) First use of a pulsed gradient stimulated echo: J. E. Tanner, J. Chem. Phys. , 1970, 52 , 2523-2526; ( c ) A. Chen, D. Wu and C. S. Johnson, J. Am. Chem. Soc. , 1995, 117 , 7965-7970; ( d ) C. S. Johnson and Progress Nucl. Magn, Reson. Spectrosc. , 1999, 34 , 203-256.
- 4 ( a ) D. Li, G. Kagan, R. Hopson and P. G. J. Williard, J. Am. Chem. Soc. , 2009, 131 , 5627-5634; ( b ) W. Li, H. Chung,

C. Daeffler, J. A. Johnson and R. H. Grubbs, Macromolecules , 2012, 45 , 9595-9603; ( c ) E. Hevia, A. R. Kennedy, R. E. Mulvey, D. L. Ramsay and S. D. Robertson, Chem. - Eur. J. , 2013, 19 , 14069-14075; ( d ) G. Hamdoun, M. Sebban, E. Cossoul, A. Harrison-Marchand, J. Maddaluno and H. Oulyadi, Chem. Commun. , 2014, 50 , 4073-4075; ( e ) R. Neufeld and D. Stalke, Chem. Sci. , 2015, 6 , 3354-3364.

- 5 F. M. Arrabal-Campos, P. On ˜a-Burgos and I. Ferna ´ndez, Polym. Chem. , 2016, 7 , 4326-4329.
- 6 M. Urbanczyk, D. Bernin, W. Kozminski and K. Kazimierczuk, Anal. Chem. , 2013, 85 , 1828-1833.
- 7 K. Xu and S. Zhang, Anal. Chem. , 2014, 86 , 592-599.
- 8 B. Antalek, Concepts Magn. Reson. , 2002, 14 , 225-258.
- 9 M. Nilsson and G. A. Morris, Anal. Chem. , 2008, 80 , 3777-3782.
- 10 L. C. M. Van Gorkom and T. Hancewicz, J. Magn. Reson. , 1998, 130 , 125-130.
- 11 A. A. Colbourne, S. Meier, G. A. Morris and M. Nilsson, Chem. Commun. , 2013, 49 , 10510-10512.
- 12 W. H. Press, S. Teukolsky, W. Vetterling and B. P. Flannery, Numerical Recipes: The Art of Scientific Computing , Cambridge University Press, New York, 1992.
- 13 S. W. Provencher, Comput. Phys. Commun. , 1982, 27 , 229-242.
- 14 F. W. Roush, Math. Social Sci. , 1984, 7 , 298-300.
- 15 M. A. Delsuc and T. E. Malliavin, Anal. Chem. , 1998, 70 , 2146-2148.
- 16 A. Cherni, E. Chouzenoux and M. A. Delsuc, 2016, arXiv: 1608.07055.
- 17 J. Vieville, M. Tanty and M. A. Delsuc, J. Magn. Reson. , 2011, 212 , 169-173.
- 18 M. Roding, D. Bernin, J. Jonasson, A. Sarkka, D. Topgaard, M. Rudemo and M. J. Nyden, Magn. Reson. , 2012, 222 , 105-111.
- 19 M. Urbanczyk, D. Bernin, A. Czuron and K. Kazimierczuk, Analyst , 2016, 141 , 1745-1752.
- 20 R. Guo, P. Mei, Q. Zhong, Y. Yao, Q. Su and J. Zhang, RSC Adv. , 2015, 5 , 31365-31374, and references cited therein.
- 21 ( a ) The concentration of each polymer in the sample was 0.9 mg mL  1 . P. J. Flory, Principles of Polymer Chemistry , Cornell University, New York, 1953; ( b ) S. F. Edwards and M. Doi, The Theory of Polymer Dynamics , Oxford University Press, New York, 1986.
- 22 ( a ) H. Bersini and G. Seront, in Proceedings of the 2nd International Conference on Parallel Problem Solving from Nature, Brussels, Belgium, September 28-30, 1992. ed. R. Ma ¨nner, B. Manderick, Elsevier, Amsterdam, 1992; ( b ) A. Eiben, P. E. Raue ´ and Z. S. Ruttkay, in Proceedings of the 3rd Conference on Parallel Problem Solving from Nature, Jerusalem, Israel, October 9-14, 1994. ed. Y. Davidor,
- H. P. Schwefel, R. Manner, Springer, Berlin, 1994.
- 23 ( a ) R. J. Leardi, J. Chemom. , 2000, 14 , 643-655; ( b ) H. Goicoechea and A. Olivieri, J. Chemom. , 2003, 17 , 338-345.
- 24 ( a ) D. Hibbert, Chemom. Intell. Lab. Syst. , 1993, 19 , 277-293; ( b ) R. Leardi and A. L. Gonzalez, Chemom. Intell. Lab. Syst. , 1998, 41 , 195-207; ( c ) M. Arakawa, Y. Yamashita and
- K. J. Funatsu, J. Chemom. , 2011, 25 , 10-19; ( d ) A. Niazi and
- R. J. Leardi, J. Chemom. , 2012, 26 , 345-351.

- 25 ( a ) D. Goldberg, Genetic Algorithms in Search, Optimization, and Machine Learning , Addison-Wesley, New York, 1989; ( b ) L. C. Karr, D. A. Stanley and B. J. Scheiner, Genetic Algorithm Applied to Least Squares Curve Fitting, Int. Bu. of Mines: Pennsylvania, 1991, Report No. 9339; ( c ) G. J. Debock, Trading on the Edge , John Wiley &amp; Sons, New York, 1994; ( d ) T. Back, Evolutionary Algorithms in Theory and Practice , Oxford University Press, Oxford, 1996.
- 26 D. Sinnaeve, Concepts Magn. Reson. , 2012, 40A , 39-65.
- 27 ( a ) J. Blommers, C. B. Lucasius, G. Kateman and R. Kaptein, Biopolymers , 1992, 32 , 45; ( b ) T. Dandekar and P. Argos, Protein Eng. , 1992, 5 , 637.
- 28 A. D. Dane, P. A. M. Timmermans, H. A. van Sprang and L. M. C. Buydens, Anal. Chem. , 1996, 68 , 2419-2425.
- 29 Q. Ding and G. W. Small, Anal. Chem. , 1998, 70 , 4472-4479.
- 30 Y. Stramer, A. Brenner, S. B. Cohen and G. Oron, Environ. Sci. Technol. , 2010, 44 , 5503-5508, and references cited therein.
- 31 L. Xu, Y. Li, N. Xu, Y. Hu, C. Wang, J. He, Y. Cao and S. J. Chen, J. Agric. Food Chem. , 2014, 62 , 12294-12298.
- 32 N. Tavassoli, Z. Chen, A. Bain, L. Melo, D. Chen and E. R. Grant, Anal. Chem. , 2014, 86 , 10591-10599.
- 33 T. M. Barbosa, R. Rittner, C. F. Tormena, G. A. Morris and M. Nilsson, RSC Adv. , 2016, 6 , 95173-95176.
- 34 J. C. Hoch and A. S. Stern, NMR Data Processing , Wiley-Liss, New York, 1996, ch. 5.
- 35 D. H. Von Seggern, CRC Standard Curves and Surfaces with Mathematica. , CRC, Boca Raton, 2006.