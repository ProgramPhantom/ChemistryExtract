<!-- image -->

## Algebraic Reconstruction Technique for Di ff usion NMR Experiments. Application to the Molecular Weight Prediction of Polymers

Francisco M. Arrabal-Campos, Luis M. Aguilera-Sa ́ ez, and Ignacio Ferna ́ ndez

Department of Chemistry and Physics, Research Centre CIAIMBITAL, Universidad de Almería, Ctra. Sacramento, s/n, Almería, E-04120, Spain

<!-- image -->

## 1. INTRODUCTION

In the mid-1960s, Stejskal and Tanner used for the fi rst-time NMR pulsed gradient spin echoes (PGSE) for the calculation of di ff usion coe ffi cients in iso ic media and from these estimated hydrodynamic radii. -Di ff usion NMR methodology holds a special position among the di ff erent experiments available to the NMR spectroscop t While it pro es invaluable information in molecular sizes -pes, , it can also used to stigate polyme , -organometallics, , , ysis, , nanoparticles, -and host -guest systems, -as well as to characterize complex mixtures. Other application tems and pharmaceuticals have been also provided. , , -

The physical constant di ff usion coe ffi cient is estimated by the application of a PGSE technique, which is based on the signal attenuation ( E diff = I / I 0 ) during a corrected di ff usion time Δ ' , which depends on the speci fi c solution of the Stejskal -Tanner partial di ff erential equation applied on a speci fi c sequence, gradient shape and nucleus .

$$E _ { d i f f } = e ^ { - D \gamma _ { \phi } \lambda ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g ^ { 2 } \Delta ^ { \prime } } \\ \quad w i g h e r { ( 1 ) }$$

For a continuous distribution of di ff usion coe ffi cients, A ( D ), could be replaced by the following integral eq that describes the signal decay.

$$E _ { d i f f } ( g ) = \int _ { 0 } ^ { \infty } A ( D ) e ^ { - D \gamma _ { \phi } \lambda ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g ^ { 2 } \Delta ^ { \prime } } \, d D \\$$

could also be converted into discrete space through the inner product of the di ff usion coe ffi cient and the integral matrix of the multiexponential decay, which is named the Hilbert space .

<!-- image -->

$$E _ { d i f f _ { i } } = \sum _ { j = 1 } ^ { n } A _ { j } e ^ { - D _ { j } \gamma _ { c f } ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g _ { i } ^ { 2 } \Delta ^ { \prime } }$$

where Ediffi = Ediff ( g i ), and Aj = A ( Dj ). Subscripts i ( i = 1, 2, ..., m ) and j ( j = 1, 2, ..., n ) label PFG strengths and di ff usion coe ffi cient values, respectively. To simplify the mathematical treatment, could be used as a linear algebraic form described by .

$$- \int _ { S ^ { d i f f } } E _ { d i f f } = d H S \cdot A$$

where Ediff is equal to [ Ediff 1 , Ediff 2 , ..., Ediffm ] T , the term A corresponds to [ A 1 , A 2 , ..., An ] T , and dHS is the m x n coe ffi cient matrix corresponding to the di ff usion Hilbert space de fi ned by

.

$$\ e ^ { \ e } _ { a } \quad d H S _ { i j } = e ^ { - D \gamma _ { j , \theta } ^ { 2 } \delta ^ { 2 } \sigma ^ { 2 } g _ { i } ^ { 2 } \Delta ^ { \prime } }$$

We have recently introduced universal calibration curves (UCC) that allow the estimation of weight-average molecular weights in monodisperse polystyrene samples globular folded proteins with no solvent dependence. , In such samples the iterative thresholding algorithm for multiexponential decay (ITAMeD) method, and conventional least mean square (LMS) routines were successfully applied. In the last two years, Zhang and co-workers have implemented the trust-region algorithm for the inversion method (TRAIn),

Received:

September 3, 2018

Revised:

December 30, 2018

DOI:

which is especially recommended for nonsymmetric distribution of di ff usion coe ffi cients.

In general terms, the distribution of di ff usion coe ffi cients is estimated from experimental data, Ediff ( g ), through the use of the inversion of the Laplace transform (ILT). This ILT is classi fi ed as an ill-posed problem which were originally introduced by Hadamard. Since the initial and boundary conditions are not well-de fi ned, eventually strong vulnerability to noise and numerical instability have induced the emergence of di ff erent approaches. These can be divided in those based on total band shape, known as multivariate methods, and those run by single channel methods. Representatives for multivariate methods are DECRA, MCR, SCORE, and OUTSCORE. As single channel, we can regard Levenberg -Marquardt statistical method and SPLMOD. All these approaches consider the di ff usion coe ffi cient as monodisperse. Instead, other approaches that consider the di ff usion coe ffi cient as a distribution are CONTIN, maximum entropy (MaxEnt) and more recently PALMA. Importantly, most of them can be considered as Tikhonov regularization methods of the following least-squares minimization problem .

$$\left \| d H S \times A - E _ { d i f f } \right \| _ { 2 } ^ { 2 } + \lambda f ( A ) & & ( 6 )$$

where λ is the sparsity promoted parameter and f ( A ( D )) is the function that penalized the over fi t, and in overall constitutes the regularization term. The function f ( A ( D )) may impose the shape and width of the fi nal solution, as is shown below.

Alternatively, instead of a regularization term, one can formulate the minimization problem as constrained, which is comparable to the TRAIn method .

$$\min & f ( A ) & \text {perf} & \quad & \text {perf} \\ & \text {subject to} \colon \left \| d H S \times A - E _ { d i f f } \right \| & < \eta & & \text {furth} \\$$

where η is always higher than zero, and it is based on an estimate of the experimental noise, which is related to the quality of the fi tting.

Regarding the polydispersity index (PDI), which is one of the main variables in polymers science, it has previously been estimated through di ff usion NMR experiments using either di ff erential di ff usion pro fi les or applying gamma or lognormal distribution models. In 2016, Urbancyzk et al. approached the problem of polydispersity by the use of a tailored regularization term, and later on Delsuc and coworkers did the same by the application of the PALMA algorithm, which combines maximum sparsity and maximum entropy.

The algebraic reconstruction technique (ART) is a class of iterative algorithm that can be considered as an iterative solver of a system of linear equations. This algorithm was discovered in the 1930s, and nowadays is extensively used in the fi eld of image reconstruction. The ART does not depend on any regularization parameter in contrast to the above-mentioned techniques, and it is very e ffi cient in terms of computational time. If we consider the di ff usion NMR problem as a linear system , then, dHS is a full rank m × n matrix with m ≤ n and Ediff ∈ R m . This method orthogonally projects on each step the last iterate onto the solution hyperplane of dHS i , A ( D ) = Ediffi and take this as the next iterate. Thus, the algorithm takes the form given in .

$$A _ { k + 1 } = A _ { k } + \frac { E _ { d i f f _ { i } } - \langle d H S _ { i } , A _ { k } \rangle } { \| d H S _ { i } \| _ { 2 } ^ { 2 } } \times d H S _ { i } \\$$

In order to maximize the projection onto the hyperplane j , the distance between the real solution and the value taken from the hyperplane in the iteration k is evaluated through the . Thus, for the next iteration, the j th hyperplane with the largest distance is selected, and therefore the over fi t in the calculation is prevented.

$$e & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

To improve the rate performance of the proposed application RT, Nesterov ' s accelerated method was implemented. , The ART algorithm itself has a rate of convergence proportional to 1/ k , where k is the number of iterations. When Nesterov ' s module is introduced, the rate of convergence is increased up to 1/ k 2 within the same number of iterations. For this reason, the following sequence was executed. Note that γ k ≤ 0.

$$\ e \quad \lambda _ { o } = 0 , \, \lambda _ { k } = \frac { 1 + \sqrt { 1 + 4 \lambda _ { k - 1 } ^ { 2 } } } { 2 } , \, \text { and } \gamma _ { k } = \frac { 1 - \lambda _ { k } } { \lambda _ { k + 1 } } \quad ( 1 0 )$$

Consequently, the ART was restructured following for its application in di ff usion NMR (dART).

$$\text {is} \quad A ^ { \prime } _ { k + 1 } = ( 1 - \gamma _ { k } ) A _ { k + 1 } + \gamma _ { k } A _ { k } \\$$

It is important to mention, that the acceleration component performs a simple step of the maximum projection onto the hyperplane j from Ak +1 to A ′ k +1 , and then it moves a little bit further than Ak +1 in the direction given by the previous Ak .

With the dART algorithm already presented, we envisaged its application in di ff usion NMR and speci fi cally, for the quantitative determination of the di ff usion coe ffi cients and therefore, accurate prediction of molecular weights. The method has been tested on simulated and real samples such as a blend of monodisperse poly(propylene glycol) polymers in the validity range of Flory ' s law (i.e., absence of o ction or concentration e ff ects on di ff usion measurements). , We also present the comparison of the method with commonly applied algorithms such as ITAMeD and TRAIn. It is worth stating that we always referred M w in terms of averages since synthetic polymers have polydispersity.

## 2. EXPERIMENTAL SECTION

Simulations. Several simulated data sets, chosen to represent various analytical situations, were used for the evaluation of the algorithm. Set A consists in three monodisperse components with di ff usion coe ffi cients 0.02127 × 10 -9 ( D 1 ), 0.0638 × 10 -9 ( D 2 ), and 0.2127 × 10 -9 m 2 s -1 ( D 3 ), with respective intensities 1, 3, and 2. Set B is based on a binary mixture of 1:1 ratio. One of the simulated components was fi xed at 0.0213 × 10 -9 m 2 s -1 , and the other one varied from 0.028 × 10 -9 to 0.0521 × 10 -9 m 2 s -1 in 12 steps. Set C is a wide distribution, simulated as a log-normal distribution centered at 0.2123 × 10 -9 m 2 s -1 , and presenting a PDI estimated to 2.30. Set D involves two monodisperse components with di ff usion coe ffi cients of 0.1611 × 10 -9

DOI:

( D 1 ) and 0.3971 × 10 -9 m 2 s -1 ( D 2 ), with respective intensities 5:1.

Processing. The dART algorithm was implemented with the programming language of MATLAB (see ). All computations were performed on a windows 64bit personal computer (PC) with an Intel i7-3770k @ 3.5 GHz and 24 GB of memory.

Samples. Poly(propylene glycol) polymers PPG450, PPG1000, PPG2000, PPG3200, and PPG5000 were purchased from the American Polymer Standards Corporation (Ohio, USA). Their corresponding M w, Mn and PDI values are given in . Benzened 6 was purchased from Eurisotop (SaintAubin, France), dried over CaH 2 , and vacuum transferred onto 3 Å molecular sieves prior to use. All other reagents and solvents were of commercial quality and were used without further puri fi cation. The UCC ( and ) was built by measuring fi ve PPG samples (PPG450, PPG1000, PPG2000, PPG3200, and PPG5000) that were prepared by dissolving 0.6 mg of each of the polymers in 0.6 mL of benzened 6 and then transferring those solutions into ovendried 5 mm NMR tubes. The NMR sample constituted by two PPG polymers was prepared by just adding 0.6 mg of each polymer together with 0.6 mL of benzened 6 in an oven-dried 5 mm J. Young NMR tube.

NMR Spectroscopy. All measurements were performed as previously described. The Δ and δ values varied from 75 to 100 ms and from 2.2 to 5 ms, respectively. The gradient strength was incremented in steps of 4%, so that 23 points could be used for regression analysis. The recovery delay was always set to 10 s. The number of scans per increment were 64 and typical experimental times were around 4 h. All experiments were run without spinning. To check reproducibility and lack of convection, three di ff erent measurements with di ff erent Δ were always carried out. The contribution of convection to the calculated D values seems to be negligible since it remains always constant under the three di ff erent di ff usion times assayed. ITAMeD solutions were obtained by the use of the algorithm provided by Urbanczyk et al. The number of iterations was always set to 10000 and the sparsitypromoting λ to 10 -5 . TRAIn solutions were obtained using the algorithm provided by Xu and Zhang.

## 3. RESULTS AND DISCUSSION

To test the vulnerability to noise of our dART method, we run Monte Carlo simulations on set A. Overall, 30 simulations were performed with random Gaussian noise applied of 0.0, 0.1, 0.5 and 1.0%. presents the results obtained on the simulated experiment A consisting in the superposition of three monodisperse species, separated by less than a factor of 10 in di ff usion coe ffi cients. show the results obtained for ITAMeD and TRAIn alternatives.

The time elapsed in these simulations of 4096 points in the Dspace, were 2 min for dART and 14 and 21 for ITAMeD and TRAIn, respectively. Over fi t was avoided in the case of ITAMed and TRAIn by the introduction of a sparsity promoted value equal to 1e -5 , and an α parameter equal to 1.02, respectively. On the contrary, dART does not need the interplay of such parameters. The fact that ITAMeD uses the L1-norm regularization gives rise to sharper solutions.

All algorithms presented the same accuracy in the reconstruction of D values at the lowest noise level of 0.0 and 0.1%. For levels above 0.5%, the errors obtained were above 5.6% which are comparable to previous results.

<!-- image -->

D (10-9m²/s)

Figure 1. dART processing of the simulated data set with added Gaussian noise levels of 0.0, 0.1, 0.5, and 1.0%. Reference D -values are marked with dotted lines.

presents synthetic results that highlights in bold those algorithms that a ff ord lower errors compared to those originally de fi ned in the set of data. Extensive results are presented in the Supporting Information (see

Table 1. Quality of Reconstruction of Signals of Set A at Di ff usion Coe ffi cients D 1 , D 2 and D 3 , with Di ff erent Algorithms for Various Noise Levels (in %)

|     |   noise level |   dART |   ITAMeD |   TRAIn |
|-----|---------------|--------|----------|---------|
| D 1 |           0.1 |   2.56 |     2.25 |    7.13 |
|     |           0.5 |   5.62 |     2.25 |    7.13 |
|     |           1.0 |   9.16 |     2.25 |    7.30 |
| D 2 |           0.1 |   1.72 |     3.70 |    6.14 |
|     |           0.5 |   4.17 |     3.81 |    6.30 |
|     |           1.0 |   8.22 |     5.44 |    7.83 |
| D 3 |           0.1 |   0.35 |     2.04 |    0.56 |
|     |           0.5 |   0.27 |     2.02 |    0.13 |
|     |           1.0 |   2.92 |     4.77 |    0.12 |

DOI:

Figure 2. Results of dART processing on set B which is based on two peaks at varying ratio of di ff usion coe ffi cients. The vertical lines represent reference values set in the simulation.

<!-- image -->

and ). Interestingly, the solutions for the fi rst peak (large molecule or small D-value) is very narrow whereas the solutions for the second and third peaks (small to medium size molecules) become very broad. This is due to the fact that the fi rst peak contains signal in the whole I / I 0 attenuation, whereas the other two only have signal in the fi rst part of the attenuation and therefore the algorithms have more di ffi culties in locate the solution.

The strength of our algorithm was tested with three more approaches based on simulation. On one hand, we applied the dART method on the di ff erentiation of a binary mixture of 1:1 ratio (set B). One of the simulated components was fi xed at 0.0213 × 10 -9 m 2 s -1 , and the other one varied from 0.028 × 10 -9 to 0.0521 × 10 -9 m 2 s -1 in 12 steps. Each simulation was performed with additional Gaussian noise on the level of 0.1%. Remarkably, the dART method could solve both components with relative errors below Δ D rel = 0.001 × 10 -9 m 2 s -1 , when the separation of D values was above 0.0095 × 10 -9 m 2 s -1 , that is in the second step ( ). TRAIn behaved similarly than the dART algorithm ( ), whereas ITAMeD ( ) showed less component resolution than both of them.

The second approach (set C) was based on the reconstruction of a broad Gaussian line simulating a polydisperse polymer with a PDI of about 2. shows

Figure 3. dART Reconstruction of a polydisperse Gaussian pro fi le. For comparison issues, ITAMeD and TRAIn results are also shown.

<!-- image -->

the reconstruction of this signal pro fi le with the three methods. TRAIn performs reasonably well, being the method of choice for polydisperse distributions. On the contrary, dART and ITAMeD lead to a de fi cient reconstruction of the line-shape with a poor prediction of its width. Nevertheless, the three methods predict exactly the same D coe ffi cient (0.2081 × 10 -9 m 2 s -1 ) with quality values below 2.0%.

As it has been proven, dART is not sensitive to broadness, and although minor distortions are observed, do not a ff ect the fi nal reconstruction which is an important issue when solving polydisperse systems.

In order to prove that the methods analyzed herein, and in particular dART, retrieved the right ratio in their solutions, the data set D involving two monodisperse components in a 5:1 ratio was studied. At the three levels of Gaussian noise of 0.1, 0.5 and 1.0%, the obtained ratio were in all the cases 5.1:1, 4.5:1 and 4.2:1, respectively, what corroborates that when the attenuation I / I 0 contains signal belonging to the two components, i.e. when the components are of similar size or do have similar D -values, the simulated ratio in where they exist fi ts excellently with the real one. It is important to mention, that in contrast to set A, where the D -values were separated by a factor of 10, in the data set D this di ff erence was reduced down to 2. , show the comparison of the methods at the three level of noise of 0.5, 0.1 and 1.0%, respectively. We are currently stretching the scope of our method in these terms and in mixtures based on more than two components. The results from these investigations will be reported in due course.

It is known that experimental data are quite di ff erent from simulated one where usually coexist sharp and large di ff usion distributions, sprinkle with instrumental artifacts and nonstationary noise. To test the behavior of dART on real samples, the technique was fi rst applied on PGSE experiments measured on fi ve poly(propylene glycol) (PPG) polymers in benzened 6 with referenced molecular weight (from PPG450 to PPG 5000) and referenced polydispersity (from 1.07 to 1.16). Detailed information on the PPG-samples studied, which includes their M w, M n , and PDI values, is given in .

presents the D η values of the fi ve polymers samples with respect to their commercial molecular masses in a log -log plot.

The D values employed are in all the cases averages that arise from the monitoring of various resonances ( ). The straight line is the result of fi tting to this data, with slopes of -0.6071 ( R 2 = 0.9989), -0.5894 ( R 2 = 0.9976), -0.5953 ( R 2 = 0.9982) and -0.5970 ( R 2 = 0.9985) for dART, LMS, ITAMeD and TRAIn, respectively. The variables c , f s , N A, and K correspond to size factor, shape factor, Avogadro ' s number, and a proportionality nonde fi ned constant that relates molecular weight with viscosity. Importantly, the spreading around the theoretical curve is in all the cases very weak, with R 2 values between 0.998 and 0.999.

DOI:

<!-- image -->

D (10-9m²/s)

Figure 4. dART, ITAMeD, and TRAIn processing on set D . Thirty di ff usion coe ffi cients distribution were calculated with reference D -values marked with dotted lines. The simulated attenuations were performed with 0.5% of noise level.

<!-- image -->

log (Mw) (Da)

Figure 5. Calibration curve for M w prediction in PPG polymers accessed through the use of diverse algorithms.

$$\frac { \intertext { c o n s c h d u m a g h i n c u s o r d i v e s c a n g o n d a m s . } } { \log ( D \eta ) = - \frac { 1 } { 3 \beta } \log ( M _ { W } ) - \frac { 1 } { \beta } } & & \text {the} \quad & \text {meth} & & \text {devel} & & \text {werr} & & \text {delig} & & \text {exception} & & \text {cont} & & \text {conting} & & \text {algor} & & \text {top} & & \text {top} & & \text {poly} & & \text {poly} \\ & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

The term η β , and thus β , describes structural requirements of the solvent in the presence of certain functional groups of the solute. This liquid structuring and its associated entropy are generally responsi for much of the behavior of macromolecular systems. , The combination of the slope of these curves with yields, as mentioned above, a power law behavior with a β -value of 0.549 (dART), which corresponds to an average fractal dimension d F of 1.647 (1/ α ) in Delsuc nomenclature.

This new relation represents the fi rst calibration curve for weight-average M w prediction of poly(propylene glycol) polymers with no dependence on the solvent used. A similar curve, in this case for polystyrene polymers has been already described, in which the β value found of 0.586 suggested that both type of systems induce a similar structuring pattern of the solvent molecules over these polymer chains.

In addition, to estimate the feasibility of dART, results of PDIs retrieved by the three methods, i.e. dART, ITAMeD, and TRAIn, are illustrated in , showing similar results in all the analyzed PPG samples with di ff erence errors between 1.8 and 12.1%.

The performance of our dART method was additionally analyzed by using a binary blend of monodisperse PPG polymers in benzened 6 . The results a ff orded by the others regularization methods such as ITAMeD and TRAIn are also shown for comparison issues and proves the strength of our approach regarding the accurate calculation on D-values, and eventually the correct prediction of the corresponding molecular weights. We found that the PPG mixture was wellsuited for the tests of multiexponential fi tting methods, because all the protons in the two PPG systems are no-dependent on molecular weight and resonate at the same frequency. Thus, the only way of distinguishing between them using NMR is to perform PGSE experiments and solve their di ff usion coe ffi cients. Analysis of the overall intensity attenuation showed that dART, ITAMeD, and TRAIn work excellently well ( ), though dART recovered both D values with the lowest errors among them, below 1.3%.

## Table 2. Di ff usion Values (10 -9 m 2 s -1 ) at Room Temperature (294 K) and Di ff Errors (%) Calculated through the Di ff erent Methods

|           |   dART |   ITAMeD |   TRAIn |
|-----------|--------|----------|---------|
| PPG450    | 0.7566 |   0.7124 |  0.7157 |
| di ff (%) |    0.4 |      5.4 |     4.9 |
| PPG5000   | 0.1806 |   0.1817 |  0.1808 |
| di ff (%) |    1.3 |      2.4 |     1.8 |

a With respect to D-values of 0.7475 and 0.1831 × 10 -9 m 2 s -1 for PPG450 and PPG5000, respectively.

Assuming the error bars on the ' true ' di ff usion coe ffi cients are of the order of 10%, there is no real di ff erence between methods. The two D-values together with the already developed calibration curve for PPG samples ( ), were employed for the weight-average M w predictions. To our delight, the estimated M w compared to real values fi tted excellently well with errors below 8.0% ( ). On the contrary, when the predictions are intended with alternative algorithms, less accurate weights are obtained ( ), supporting dART as the most reliable for this speci fi c poly(propylene glycol) blend.

Importantly, the time of convergence for the proposed method was evaluated. For this purpose, the data set corresponding to PPG3200 was considered. The algorithm dART allowed the fastest convergence within 0.12 s in 20 iterations, whereas ITAMeD for example, needed fi ve seconds

DOI:

Table 3. dART Di ff usion Values (10 -9 m 2 s -1 ) and UCCPredicted Weight-Average M w

|   PS |      D |   D η (10 - 3 ) |   Av- M w (Da) |   di ff (%) |
|------|--------|-----------------|----------------|-------------|
|  450 | 0.7566 |          0.1275 |            437 |         2.8 |
| 5000 | 0.1806 |          0.0058 |           4380 |         7.3 |

a 1 H PFG-STE measurements were performed at room temperature (294 K). b The viscosity value employed was η 0.646 × 10 -3 kg m -1 s -1 . c Estimated via the dART calibration curve y = -0.6071 x -1.7079 ( R 1 = 0.9989). d Considering commercial values of 450 and 5000 Da.

to reach 1000 iterations with a sparsity promoted parameter of 1 × 10 -5 ( ).

Finally, the concentration of the sample was also evaluated in order to understand if increasing the concentration of the PPG sample would alter the performance of dART. We measure the medium size polymer PPG2000 at three increasing concentrations, i.e., 0.6, 6, and 60 mg in 0.6 mL of benzened 6 , that is at 0.1, 1.0 and 10.0 wt %, respectively. As expected, the algorithm performed excellently regardless of the concentration of the sample. About the results retrieved, the di ff usion coe ffi cients at the two lowest concentrations were almost the same with values of 0.3052 and 0.3043 × 10 -9 m 2 s -1 , respectively, suggesting Flory ' s in fi nite dilution behavior in both cases. At 10.0 wt %, the obtained D -value was 0.2259 × 10 -9 m 2 s -1 , which arises from both and increased viscosity and an aggregation e ff ect. To calculate molecular weights at 1 and 10 wt % we need to know the viscosities of both solutions. To circumvent this problem, we monitor the intensity attenuations of benzene in both samples. Because the rH value for benzene can be determined ( r H = 1.53 Å), the measured D values obtained together with the Stokes -Einstein equation, a ff ord realistic estimates of the benzene PPG-containing viscosities of 0.6462 and 0.7369 × 10 -3 kg m -1 s -1 , respectively. Within these values the predicted M w were calculated with the help of the calibration curve ( ), obtaining values of 1948 and 2635 Da, which clearly indicates that at higher concentration the prediction signi fi cantly deviates with respect to the theoretical value of 2000 Da.

The PDI values retrieved by dART in the three samples of 0.1, 1.0, and 10.0 wt % were 1.030, 1.048, and 1.049, respectively, which strongly support that the algorithm is not a ff ected by any concentration e ff ect.

## 4. CONCLUSIONS

Di ff usion NMR still in development and it is probably on complex mixtures or polymer blends where stretches all his power. In fact, a simple fi t of the data to the basic evolution equations usually fails in providing a faithful analysis of the data or solving the number of components and their molecular masses. For these reasons, one must use the inverse Laplace transform for the analysis. In this work, we have introduced for the fi rst time an algebraic reconstruction technique (dART) in di ff usion NMR to solve the inverse problem. The proposed method does not need sparsity promote parameter neither alpha value and therefore allows to explore largest spaces. This new algorithm has been compared with established methods such as ITAMeD or TRAIn on both simulated and real systems, providing excellent results and with the lowest times of convergence. An additional advantage is its ability to work well with large di ff usion spaces. On the contrary, dART does not provide the best results with highly polydisperse polymers and provide broader solutions that for instance ITAMeD that uses the regularization L1-norm. In addition, we have provided a calibration curve for weight-average M w prediction of polypropylene polymers with no dependence on the solvent used, in which the β value of 0.549 has been established. The model is presented in a desktop application available at

.

## ■ ASSOCIATED CONTENT

## * S Supporting Information

The Supporting Information is available free of charge on the at DOI: .

Experimental section, complete NMR di ff usion data, programming codes, and algorithm solutions ( )

## ■ AUTHOR INFORMATION

## Corresponding Author

.

* (I.F.) E-mail:

## ORCID

Ignacio Ferna ́ ndez:

## Author Contributions

The manuscript was written through contributions of all authors. All authors have given approval to the fi nal version of the manuscript.

## Notes

The authors declare no competing fi nancial interest.

## ■ ACKNOWLEDGMENTS

Financial support was given by Bruker Espan ̃ ola SA, Junta de Andaluc ı ́ a (Spain) under the project number P12-FQM-2668 and Ministerio de Ciencia, Innovacio ́ n y Universidades (Spain) under the Project Number CTQ2017-84334-R.

## ■ REFERENCES

- (1) Stejskal, E. O.; Tanner, J. E. Spin diffusion measurements: Spin echoes in the presence of a time dependent field gradient. J. Chem. Phys. 1965 , 42 , 288 -292.
- (2) Tanner, J. E. Use of the stimulated echo in NMR diffusion studies. J. Chem. Phys. 1970 , 52 , 2523 -2526.
- (3) Chen, A.; Wu, D.; Johnson, C. S. Determination of molecular weight distributions for polymers by diffusion-ordered NMR. J. Am. Chem. Soc. 1995 , 117 , 7965 -7970.
- (4) Johnson, C. S. Diffusion ordered nuclear magnetic resonance spectroscopy: principles and applications. Prog. Nucl. Magn. Reson. Spectrosc. 1999 , 34 , 203 -256.
- (5) Macchioni, A.; Ciancaleoni, G.; Zuccaccia, C.; Zuccaccia, D. Determining accurate molecular sizes in solution through NMR diffusion spectroscopy. Chem. Soc. Rev. 2008 , 37 , 479 -489.
- (6) Li, D.; Kagan, G.; Hopson, R.; Williard, P. G. Formula weight prediction by internal reference diffusion-ordered NMR spectroscopy (DOSY). J. Am. Chem. Soc. 2009 , 131 , 5627 -5634.
- (7) Neufeld, R.; Stalke, D. Accurate molecular weight determination of small molecules via DOSY-NMR by using external calibration curves with normalized diffusion coefficients. Chem. Sci. 2015 , 6 , 3354 -3364.
- (8) Evans, R.; Deng, Z.; Rogerson, A. K.; McLachlan, A. S.; Richards, J. J.; Nilsson, M.; Morris, G. A. Quantitative interpretation of diffusion-ordered NMR spectra: can we rationalize small molecule diffusion coefficients? Angew. Chem., Int. Ed. 2013 , 52 , 3199 -3202.
- (9) Evans, R.; Dal Poggetto, G.; Nilsson, M.; Morris, G. A. Improving the interpretation of small molecule diffusion coefficients. Anal. Chem. 2018 , 90 , 3987 -3994.

- (10) Viel, S.; Capitani, D.; Mannina, L.; Segre, A. Diffusion-ordered NMR spectroscopy: A versatile tool for the molecular weight determination of uncharged polysaccharides. Biomacromolecules 2003 , 4 , 1843 -1847.
- (11) Barrere, C.; Mazarin, M.; Giordanengo, R.; Phan, T.; Thevand, A.; Viel, S.; Charles, L. Molecular weight determination of block copolymers by pulsed gradient spin echo NMR. Anal. Chem. 2009 , 81 , 8054 -8060.
- (12) Li, W.; Chung, H.; Daeffler, C.; Johnson, J. A.; Grubbs, R. H. Application of 1 HDOSY for facile measurement of polymer molecular weights. Macromolecules 2012 , 45 , 9595 -9603.
- (13) Kuz'mina, N. E.; Moiseev, S. V.; Krylov, V. I.; Yashkir, V. A.; Merkulov, V. A. Quantitative determination of the average molecular weights of dextrans by diffusion ordered NMR spectroscopy. J. Anal. Chem. 2014 , 69 , 953 -959.
- (14) Lewinski, P.; Sosnowski, S.; Kazmierski, S.; Penczek, S. Llactide polymerization studied by 1 H NMR with diffusion ordered spectroscopy (DOSY). ' One NMR tube experiment ' providing: Conversion, polymer structure, Mn and Mw. Polym. Chem. 2015 , 6 , 4353 -4357.
- (15) Pregosin, P. S.; Kumar, P. G. A.; Ferna ́ ndez, I. Pulsed gradient spin -echo (PGSE) diffusion and 1 H, 19 F heteronuclear overhauser spectroscopy (HOESY) NMR methods in inorganic and organometallic chemistry: Something old and something new. Chem. Rev. 2005 , 105 , 2977 -2998.
- (16) Avram, L.; Cohen, Y. Diffusion NMR of molecular cages and capsules. Chem. Soc. Rev. 2015 , 44 , 586 -602.
- (17) Schober, K.; Hartmann, E.; Zhang, H.; Gschwind, R. M. 1 H DOSY spectra of ligands for highly enantioselective reactions -a fast and simple NMR method to optimize catalytic reaction conditions. Angew. Chem., Int. Ed. 2010 , 49 , 2794 -2797.
- (18) Horeglad, P.; Litwinska, A.; Zukowska, G. Z.; Kubicki, D.; Szczepaniak, G.; Dranka, M.; Zachara, J. The influence of organosuperbases on the structure and activity of dialkylgallium alkoxides in the polymerization of rac-lactide: the road to stereo diblock PLA copolymers. Appl. Organomet. Chem. 2013 , 27 , 328 -336.
- (19) Kohlmann, O.; Steinmetz, W. E.; Mao, X. A.; Wuelfing, W. P.; Templeton, A. C.; Murray, R. W.; Johnson, C. S. NMR diffusion, relaxation, and spectroscopic studies of water soluble, monolayerprotected gold nanoclusters. J. Phys. Chem. B 2001 , 105 , 8801 -8809. (20) Van Lokeren, L.; Maheut, G.; Ribot, F.; Escax, V.; Verbruggen, I.; Sanchez, C.; Martins, J. C.; Biesemans, M.; Willem, R. Characterization of titanium dioxide nanoparticles dispersed in organic ligand solutions by using a diffusion-ordered spectroscopy-
11. based strategy. Chem. - Eur. J. 2007 , 13 , 6957 -6966.
- (21) Van Lokeren, L.; Cartuyvels, E.; Absillis, G.; Willem, R.; ParacVogt, T. N. Phosphoesterase activity of polyoxomolybdates: diffusion ordered NMR spectroscopy as a tool for obtaining insights into the reactivity of polyoxometalate clusters. Chem. Commun. 2008 , 2774 -2776.
- (22) Marega, R.; Aroulmoji, V.; Dinon, F.; Vaccari, L.; Giordani, S.; Bianco, A.; Murano, E.; Prato, M. Diffusion-ordered NMR spectroscopy in the structural characterization of functionalized carbon nanotubes. J. Am. Chem. Soc. 2009 , 131 , 9086 -9093.
- (23) Marega, R.; Aroulmoji, V.; Bergamin, M.; Feruglio, L.; Dinon, F.; Bianco, A.; Murano, E.; Prato, M. Two-dimensional diffusionordered NMR spectroscopy as a tool for monitoring functionalized carbon nanotube purification and composition. ACS Nano 2010 , 4 , 2051 -2058.
- (24) Canzi, G.; Mrse, A. A.; Kubiak, C. P. Diffusion-ordered NMR spectroscopy as a reliable alternative to TEM for determining the size of gold nanoparticles in organic solutions. J. Phys. Chem. C 2011 , 115 , 7972 -7978.
- (25) de Kort, D. W.; van Duynhoven, J. P. M.; Hoeben, F. J. M.; Janssen, H. M.; Van As, H. NMR nanoparticle diffusometry in hydrogels: enhancing sensitivity and selectivity. Anal. Chem. 2014 , 86 , 9229 -9235.
- (26) Thielemann, D. T.; Wagner, A. T.; Lan, Y.; On ̃ a-Burgos, P.; Ferna ́ ndez, I.; Ro ̈ sch, E.; Ko ̈ lmel, D. K.; Powell, A. K.; Bra ̈ se, S.;
18. Roesky, P. W. Peptoid ligated pentadecanuclear yttrium and dysprosium hydroxy clusters. Chem. - Eur. J. 2015 , 21 , 2813 -2820.
- (27) Cohen, Y.; Avram, L.; Frish, L. Diffusions-NMR-spektroskopie in der supramolekularen und kombinatorischen chemie: Ein alter parameter -neue erkenntnisse. Angew. Chem. 2005 , 117 , 524 -560.
- (28) Cohen, Y.; Avram, L.; Frish, L. Diffusion NMR spectroscopy in supramolecular and combinatorial chemistry: An old parameter -new insights. Angew. Chem., Int. Ed. 2005 , 44 , 520 -554.
- (29) Pastor, A.; Martinez-Viviente, E. NMR spectroscopy in coordination supramolecular chemistry: A unique and powerful methodology. Coord. Chem. Rev. 2008 , 252 , 2314 -2345.
- (30) Han, S.; Ma, Z.; Hopson, R.; Wei, Y.; Budil, D.; Gulla, S.; Moulton, B. Postsynthetic modification of a coordination compound with a paddlewheel motif via click reaction: DOSY and ESR studies. Inorg. Chem. Commun. 2012 , 15 , 78 -83.
- (31) Hamdoun, G.; Guduff, L.; van Heijenoort, C.; Bour, C.; Gandon, V.; Dumez, J.-N. Spatially encoded diffusion-ordered NMR spectroscopy of reaction mixtures in organic solvents. Analyst 2018 , 143 , 3458 -3464.
- (32) Crutchfield, C. A.; Harris, D. J. Molecular mass estimation by PFG NMR spectroscopy. J. Magn. Reson. 2007 , 185 , 179 -182.
- (33) Wang, C. K.; Northfield, S. E.; Swedberg, J. E.; Harvey, P. J.; Mathiowetz, A. M.; Price, D. A.; Liras, S.; Craik, D. J. Translational diffusion of cyclic peptides measured using pulsed-field gradient NMR. J. Phys. Chem. B 2014 , 118 , 11129 -11136.
- (34) Dutta, A. R.; Sekar, P.; Dvoyashkin, M.; Bowers, C. R.; Ziegler, K. J.; Vasenkov, S. Single-file diffusion of gas mixtures in nanochannels of the dipeptide l-ala-l-val: High-field diffusion NMR study. J. Phys. Chem. C 2016 , 120 , 9914 -9919.
- (35) Page ̀ s, G.; Bonny, A.; Gilard, V.; Malet-Martino, M. Pulsed field gradient NMR with sigmoid shape gradient sampling to produce more detailed diffusion ordered spectroscopy maps of real complex mixtures: Examples with medicine analysis. Anal. Chem. 2016 , 88 , 3304 -3309.
- (36) Trefi, S.; Routaboul, C.; Hamieh, S.; Gilard, V.; Malet-Martino, M.; Martino, R. Analysis of illegally manufactured formulations of tadalafil (Cialis) by 1 H NMR, 2D DOSY 1 H NMR and Raman spectroscopy. J. Pharm. Biomed. Anal. 2008 , 47 , 103 -113.
- (37) Balayssac, S.; Gilard, V.; Delsuc, M. A.; Malet-Martino, M. DOSY NMR, a new tool for fake drug analyses. Spectrosc. Eur. 2009 , 21 , 10 -14.
- (38) Vaysse, J.; Balayssac, S.; Gilard, V.; Desoubdzanne, D.; MaletMartino, M.; Martino, R. Analysis of adulterated herbal medicines and dietary supplements marketed for weight loss by DOSY 1 H-NMR. Food Addit. Contam., Part A 2010 , 27 , 903 -916.
- (39) Balayssac, S.; Retailleau, E.; Bertrand, G.; Escot, M.-P.; Martino, R.; Malet-Martino, M.; Gilard, V. Characterization of heroin samples by 1 H NMR and 2D DOSY 1 H NMR. Forensic Sci. Int. 2014 , 234 , 29 -38.
- (40) Smejkalova, D.; Piccolo, L. Host-guest interactions between 2,4-dichlorophenol and humic substances as evaluated by 1 H NMR relaxation and diffusion ordered spectroscopy. Environ. Sci. Technol. 2008 , 42 , 8440 -8445.
- (41) Li, D.; Keresztes, I.; Hopson, R.; Williard, P. G. Characterization of reactive intermediates by multinuclear diffusion-ordered NMR spectroscopy (DOSY). Acc. Chem. Res. 2009 , 42 , 270 -280.
- (42) Lamm, J. H.; Niermeier, P.; Mix, A.; Chmiel, J.; Neumann, B.; Stammler, H. G.; Mitzel, N. W. Mechanism of host-guest complex formation and identification of intermediates through NMR titration and diffusion NMR spectroscopy. Angew. Chem., Int. Ed. 2014 , 53 , 7938 -7942.
- (43) Cao, R.; Nonaka, A.; Komura, F.; Matsui, T. Application of diffusion ordered1 H-nuclear magnetic resonance spectroscopy to quantify sucrose in beverages. Food Chem. 2015 , 171 , 8 -12.
- (44) Ge, W.; Zhang, J. H.; Pedersen, C. M.; Zhao, T.; Yue, F.; Chen, C.; Wang, P.; Wang, Y.; Qiao, Y. DOSY NMR: A versatile analytical chromatographic tool for lignocellulosic biomass conversion. ACS Sustainable Chem. Eng. 2016 , 4 , 1193 -1200.

- (45) Wilkins, D. K.; Grimshaw, S. B.; Receveur, V.; Dobson, C. M.; Jones, J. A.; Smith, L. Hydrodynamic radii of native and denatured proteins measured by pulse field gradient NMR Techniques. Biochemistry 1999 , 38 , 16424 -16431.
- (46) Jones, J. A.; Wilkins, D. K.; Smith, L. J.; Dobson, C. M. Characterisation of protein unfolding by NMR diffusion measurements. J. Biomol. NMR 1997 , 10 , 199 -203.
- (48) Sinnaeve, D. The Stejskal -Tanner equation generalized for any gradient shape -An overview of most pulse sequences measuring free diffusion. Concepts Magn. Reson., Part A 2012 , 40A , 39 -65.
- (47) Arrabal-Campos, F. M.; Aguilera-Sa ́ ez, L. M.; Ferna ́ ndez, I. A diffusion NMR method for the prediction of the weight-average molecular weight of globular proteins in aqueous media of different viscosities. Anal. Methods 2019 , 11 , 142 -147.
- (49) Arrabal-Campos, F. M.; On ̃ a-Burgos, P.; Ferna ́ ndez, I. Molecular weight prediction with no dependence on solvent viscosity. A quantitative pulse field gradient diffusion NMR approach. Polym. Chem. 2016 , 7 , 4326 -4329.
- (50) Urbanczyk, M.; Bernin, D.; Kozminski, W.; Kazimierczuk, K. Iterative thresholding algorithm for multiexponential decay applied to PGSE NMR data. Anal. Chem. 2013 , 85 , 1828 -1833.
- (51) Xu, K.; Zhang, S. Trust-region algorithm for the inversion of molecular diffusion NMR data. Anal. Chem. 2014 , 86 , 592 -599.
- (52) Hadamard, J. Lectures on the Cauchy Problem in Linear Partial Differential Equations ; Yale University Press: New Haven, CT, 1923.
- (53) Antalek, B. Using pulsed gradient spin echo NMR for chemical mixture analysis: How to obtain optimum results. Concepts Magn. Reson. 2002 , 14 , 225 -258.
- (54) Van Gorkom, L. C. M.; Hancewicz, T. Analysis of DOSY and GPC-NMR experiments on polymers by multivariate curve resolution. J. Magn. Reson. 1998 , 130 , 125 -130.
- (55) Nilsson, M.; Morris, G. A. Speedy component resolution: An improved tool for processing diffusion-ordered spectroscopy data. Anal. Chem. 2008 , 80 , 3777 -3782.
- (56) Colbourne, A. A.; Meier, S.; Morris, G. A.; Nilsson, M. Unmixing the NMR spectra of similar species -vive la difference. Chem. Commun. 2013 , 49 , 10510 -10512.
- (57) Press, W. H.; Teukolsky, S.; Vetterling, W.; Flannery, B. P. Numerical recipes: The art of scientific computing ; Cambridge University Press: New York, 1992.
- (58) Provencher, S. W.; Vogel, R. H. Regularization Techniques for Inverse Problems in Molecular Biology. Numerical treatment of inverse problems in differential and integral equations 1983 , 304 -319.
- (59) Provencher, S. W. CONTIN: A general purpose constrained regularization program for inverting noisy linear algebraic and integral equations. Comput. Phys. Commun. 1982 , 27 , 229 -242.
- (60) Delsuc, M. A.; Malliavin, T. E. Maximum entropy processing of DOSY NMR spectra. Anal. Chem. 1998 , 70 , 2146 -2148.
- (61) Cherni, A.; Chouzenoux, E.; Delsuc, M. A. PALMA, an improved algorithm for DOSY signal processing. Analyst 2017 , 142 , 772 -779.
- (62) Tikhonov, A. N. Solution of incorrectly formulated problems and the regularization method. Soviet Math. Dokl. 1963 , 4 , 1035 -1038.
- (63) Vieville, J.; Tanty, M.; Delsuc, M. A. Polydispersity index of polymers revealed by DOSY NMR. J. Magn. Reson. 2011 , 212 , 169 -173.
- (64) Roding, M.; Bernin, D.; Jonasson, J.; Sarkka, A.; Topgaard, D.; Rudemo, M.; Nyden, M. The gamma distribution model for pulsedfield gradient NMR studies of molecular-weight distributions of polymers. J. Magn. Reson. 2012 , 222 , 105 -111.
- (65) Urbanczyk, M.; Bernin, D.; Czuron, A.; Kazimierczuk, K. Monitoring polydispersity by NMR diffusometry with tailored norm regularisation and moving-frame processing. Analyst 2016 , 141 , 1745 -1752.
- (66) Gordon, R.; Bender, R.; Herman, G. T. Algebraic reconstruction techniques (ART) for three-dimensional electron microscopy and x-ray photography. J. Theor. Biol. 1970 , 29 , 471 -481.
- (67) Kaczmarz, S. Angena ̈ herte auflo ̈ sung von systemen linearer gleichungen. Sciences Mathe ́ matiques 1937 , 35 , 355 -357.
- (68) Herman, G. T. Fundamentals of computerized tomography. image reconstruction from projections ; Springer: New York, 2009.
- (69) Zhdanov, A. I. The method of augmented regularized normal equations. Comp. Math. and Math. Phys. 2012 , 52 , 194 -197.
- (70) Nesterov, Y. E. A method for solving the convex programming problem with convergence rate O(1/k2). Soviet Mathematics Doklady 1983 , 27 , 372 -376.
- (71) Nesterov, Y. E. Accelerating the cubic regularization of Newton ' s method on convex problems. Math. Program. 2007 , 112 , 159 -181.
- (72) Flory, P. J. Principles of polymer chemistry ; Cornell University Press: New York, 1953.
- (73) Edwards, S. F.; Doi, M. The theory of polymer dynamics ; Oxford University Press: New York, 1986.
- (74) Arrabal-Campos, F. M.; Alvarez, J. D.; Garcia-Sancho, A.; Ferna ́ ndez, I. Molecular weight prediction in polystyrene blends. Unprecedented use of a genetic algorithm in pulse field gradient spin echo (PGSE) NMR. Soft Matter 2017 , 13 , 6620 -6626.
- (75) Barbosa, T. M.; Rittner, R.; Tormena, C. F.; Morris, G. A.; Nilsson, M. Convection in liquid-state NMR: expect the unexpected. RSC Adv. 2016 , 6 , 95173 -95176.

DOI: