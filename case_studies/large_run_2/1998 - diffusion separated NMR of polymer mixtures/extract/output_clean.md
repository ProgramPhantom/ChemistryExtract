## Diffusion-Separated Nuclear Magnetic Resonance Spectroscopy of Polymer Mixtures

## Alexej Jerschow † and Norbert Mu 1 ller*

Institut fu ¨ r Chemie, Johannes Kepler University Linz, Altenbergerstrasse 69, A-4040 Linz, Austria, and MR-Center, SINTEF UNIMED, N-7034 Trondheim, Norway

Received February 5, 1998; Revised Manuscript Received June 26, 1998

ABSTRACT: The potential of diffusion-ordered 2D NMR spectroscopy (DOSY) for the analysis of solutions of polymer mixtures and polymers with complex molecular mass distributions is investigated. Diffusion coefficient labeling in NMR is generally achieved by stepwise ramping up of the amplitudes of pairs of pulsed field gradients (PFGs). After Fourier transformation in the acquisition dimension and an inverse Laplace transform (ILT) with respect to the square of the gradient strength, 2D spectra are obtained that show the chemical shift along one dimension and the translational diffusion coefficient along the other. Since polymers may have broad, nonsymmetric or complex (bi- and multimodal) molecular weight distributions (MWDs), the diffusion coefficient distribution should follow the main features of the MWD. However, the calculation of the diffusion coefficient distribution involves a numerically unstable data inversion (ILT), which limits the resolution in the diffusion dimension. The applications of DOSY NMR techniques to the study of polymer blends and for the determination of MWDs of polymers with PFG NMR are assessed. DOSY spectra recorded from industrial polypropylene and polystyrene samples and mixtures are shown and interpreted to illustrate the features of this technique.

## Introduction

NMR spectroscopy of polymer solutions is well established for polymer structure elucidation. 1 -4 The microstructural properties of the polymers ultimately show up in different chemical shifts of the different spin sites. Resolved 13 C chemical shifts permit assignment of different local structural environments, and it is possible to obtain even stereospecific sequence analysis of the polymer chain. 2,5

In contrast, proton spectra of polymers are usually not well resolved, mostly because of fast transverse relaxation, but also because distributions of different molecular species prevail. It is often impossible to determine which signals pertain to different molecular species and which ones to different structural units in the same species. Diffusion-ordered NMR spectroscopy (DOSY), 6 -9 which employs pulsed field gradient (PFG) NMR, bears the potential to solve such kinds of problems. In these spectra chemical shift information in the directly observed ( t 2) dimension is dispersed by translational diffusion coefficients in the indirectly observed dimension. An inverse Laplace transform (ILT) is used to resolve signals with identical chemical shifts but different diffusion coefficients from a gradient strength dependent decay curve.

We used the pulse sequence presented in Figure 1 to obtain DOSY spectra. It is a PFG STE (stimulated echo) sequence employing bipolar gradients 10 and a longitudinal eddy current delay (LED). 9 It was found to be superior to the original monopolar gradient sequence 8 in giving better resolution and sensitivity. The phase cycle is the same as in ref 11 and was found to give fewer artifacts than the one given in ref 10

* To whom correspondence should be addressed at the Johannes Kepler University. E-mail: norbert.mueller@jk.uni-linz.ac.at. Fax: + 43 70 2468 747. Phone: + 43 70 2468 746.

† Present address: Universite ´ de Lausanne, Section de Chimie BCH, CH-1015, Lausanne-Dorigny, Switzerland.

Figure 1. PFG STE sequence with bipolar gradients. The phase cycle is 1 ) x , x , y , y , -x , -x , -y , -y ; 2 ) y , -x , -x , -y , -y , x , x , y ; 3 ) 7 ) x ; 4 ) -x , -x , -y , -y ; 5 ) -y , -y , x , x ; 6 ) -x ; receiver ) 2( x , -x ), 2( -x , x ). The desired coherence order pathway p ( t ) is drawn. Narrow and wide filled rectangles represent the 90 and 180° rf pulses. The other rectangles (unfilled) represent the ramped gradients, and the sine humps represent the spoiler gradients.

<!-- image -->

because of additional cycling of the 180° pulses. This was corroborated by a simulation of the coherence transfer pathway selection steps by means of a program we developed, which will be documented elsewhere. 12

In a diffusion experiment using this pulse sequence, each NMR signal is attenuated with increasing gradient strength and translational diffusion coefficient Dm of the molecular species it belongs to:

$$\text {molecular species} \text { it belongs to} \colon \\ S = \sum _ { m } f _ { m } \exp \left ( - D _ { m } q ^ { 2 } \left ( T + \frac { 2 \delta } { 3 } + \frac { 3 \tau } { 4 } \right ) \right ) \quad ( 1 )$$

where the index m runs over all components in the mixture. The delays T , , and are explained in Figure 1, and q ) G is the effective gradient area. Since the delays T , , and are not negligible, the factors fm , that represent the abundance of the molecular species, are also relaxation weighted. This weighting is constant throughout the experiment (since the delays are not changed) and will be considered separately later.

The multiexponential decay of eq 1 can be transformed into a diffusion coefficient spectrum by an inverse Laplace transform (ILT), which amounts to finding the amplitude factors fm for a certain range of decay components with different Dm .

We illustrate this for one isochromate in a spectrum and use, b ) q 2 ( T + 2 /3 + 3 /4), which can be regarded as a pseudo time domain variable in the terminology of multidimensional NMR. 13 After a Fourier transform in the directly observed dimension, the signal at each frequency can be modeled by

$$S ( b ) = \sum _ { m } f _ { m } \exp ( - D _ { m } b ) + \epsilon ( b ) \quad \quad ( 2 ) \quad \quad \stackrel { \mu } { r a r }$$

with representing the random noise in the experiment.

The ordinary multiexponential least squares problem consists of finding the parameters fm on a grid of Dm values by minimizing the target function:

$$K = | | S ( b ) - \sum _ { m } f _ { m } \exp ( - D _ { m } b ) | | ^ { 2 } & & ( 3 ) & & \max _ { \substack { m = 0 \\ \ m = 1 } } \,$$

When the number of components is 2, this task is easily accomplished by a biexponential least-squares fit. With more components and in the presence of noise, this quickly becomes an ill-posed problem 14,15 as a consequence of the nonorthogonality of the exponential functions.

To handle such cases, regularization techniques are available. The target function of eq 3 is changed to

$$K = | | S ( b ) - \sum _ { m } f _ { m } \exp ( - D _ { m } b ) | | ^ { 2 } + \alpha | | \hat { A } f _ { m } | | ^ { 2 } \quad ( 4 ) \\$$

where R is called the regularization parameter and A can either be the identity operator or the second derivative operator (in the case of Tikhonov regularization 16 ). This procedure stabilizes the inversion problem by adding a well-posed functional to the ill-posed least squares functional 16,17 (i.e., the condition that fm be smooth). Very often this is the only a priori knowledge about the solution that is available. The convergence can be largely improved by supplying additional restrictions, such as moments of the fm distribution. 18 -20

There is still the question of how to choose the regularization parameter R . We used two different algorithms implemented in the programs NLREG 21,22 and CONTIN, 18,19 which differ in the approach for choosing the regularization parameter.

While NLREG employs a self-consistent (SC) method, 22,23 CONTIN uses a probability model to chose R from a range of values for which the solution has been computed. A common assumption of both algorithms is the noise being random Gaussian. For this reason the results are heavily affected by systematic errors or coherent artifacts while a moderate random noise level does not have such a strong impact. NMRspectra often contain non-Gaussian noise due to spectrometer and pulse sequence imperfections. This is an important motivation for the use of a highly optimized pulse sequence, as in Figure 1, as opposed to simple gradient echoes. The optimization comprises the minimization of eddy current effects through the use of bipolar gradient pulses and the longitudinal eddy current delay T e, as well as the elimination of undesired coherence transfer pathways by the phase cycle and orthogonal spoiler gradient pulses, thus avoiding unwanted coherence transfer echoes.

There exists a wide variety of methods for choosing the regularization parameters. 15 -31 The solution produced by one single method has to be treated with great care since it is by no means unique. It is possible s and necessary s in practice to improve the solution by imposing certain physically plausible constraints on the target function (positivity, smoothness, and smooth vanishing at minimal and maximal Dm of fm ). Johnson et al. 32 used additional constraints with the CONTIN program for a precise determination of the MW of polymers with 'monomodal' MWDs. In contrast, our goal is to separate multimodal distributions without prior assumptions concerning the shape of the distribution.

It is very important to cross-check solutions using different algorithms. We always performed the calculations with both programs (CONTIN and NLREG). When significant differences in the results occurred, plausibility criteria (spectral distortions, comparison between slices with different frequencies, etc.) could in most cases be used to rule out one solution. As a further precaution we took care to transform only data with a sufficient signal-to-noise ratio in the frequency dimension. The effects of high noise levels are shown in the simulations of Figure 2. When the ratio of diffusion coefficients of the peaks that have to be resolved is 10, the necessary signal-to-noise ratio is around 100, while it is around 1000 for a ratio of 3 (this number has to be seen relative to the number of input points). However, even if the peaks cannot be resolved, the moments

$$M _ { k } = \sum _ { m } f _ { m } \, D _ { m } ^ { k }$$

of the distributions obtained remain fairly accurate. 33 A diffusion coefficient distribution (DCD) obtained by the procedure described above can be used to get an estimate about the corresponding MWD. For polymers in very dilute solution there exists the empirical law: 34,35

$$D \infty \, M ^ { a }$$

where a ) 0.5 for a £ solvent and 0.6 -0.8 for a good solvent. For quantitative application this relation should be calibrated separately for each polymer/solvent combination and the concentration range used. This formula, however, does not take into account the impact of molecular shape, which may even vary as the molecular mass increases. Another pitfall is the occurrence of microaveraging effects. Polymers in solution interact at a fairly low critical concentration depending on the molecular weight. 32,34,35 This leads to averaging of the DCDin the solution. Implications of these problems for our measurements will be discussed in connection with the results presented below.

## Experimental Section

Sample Preparation. The polymer samples were dissolved in tetrachloroethaned 2 . For homogenization the samples were heated to 373 K for 12 h. The compositions of the samples were (A) 0.2% PP1 + 0.8% n -decane, (B) 0.07% PP1 + 0.04% PS, (C) 0.06% PP2, and (D) 0.07% PP3. The polymers PP1, PP2, and PP3 (polypropylene) have the following characteristics: M w ) 44 000, M w/ M n ) 3.3; M w ) 261 000, M w/ M n ) 16; and M w ) 151 000, M w/ M n ) 21.9, respectively (data from GPC measurements with polystyrene as standard). PP1 is predominantly isotactic, and PP2 and PP3 have additionally atactic low molecular weight components. The PS sample was a standard from Polymer Laboratories and had the following characteristics: M w ) 350 000, M w/ M n ) 1.04.

Figure 2. Regularized inverse Laplace transform of simulated data using the NLREG program. The simulated diffusion coefficient distribution is represented by a dashed line, while the solid line represents the distribution obtained by data inversion. The ratio of the diffusion coefficients of the peak maxima is 10 in (a) and (b) and 3 in (c) and (d). The Gaussian noise level is (a) 1%, (b) 3%, (c) 0.1%, and (d) 1% of the first point in the decay (128 points were calculated). The calculated distribution shows significant deviations from the actual one in (b) and (d) due to the higher noise level.

<!-- image -->

The NMR spectrometer was a Bruker Avance DRX600 with an actively shielded triple gradient probe (5 mm), 90° pulse ( 1 H): 12 s, Acustar gradient power supply.

Typical Parameters of the PFG STE Experiment (Figure 1). T ) 100 -200 ms, ) 2.6 ms, T e ) 24 ms, ) 2 ms, max. G ) 0.63 T m -1 in the z direction (calibrated by D H2O ) 2.3 10 -9 m 2 s -1 at 298 K), homospoil gradients 0.06 T m -1 , 8 ms, orthogonal to diffusion gradients and to each other. The number of scans was 32 or 64, the number of dummy scans was 32 before the first experiment in the 2D series, the number of sampled points in the gradient strength dimension was 64 -128 (with a linear gradient ramp) and 1024 in the spectral dimension (frequency resolution was not a critical factor), and the relaxation delay was 10 s (optimized to give the best time/ performance ratio). The temperature of 298 K was held constant constant via the air conditioning system of the spectrometer room.

Data Transformation. A C program was written to feed the digitally filtered Bruker Xwinnmr spectrum after exponential multiplication (LB ) 7 Hz), and Fourier transformation in F2 into the programs NLREG or CONTIN for the ILT (only columns where the signals exceeded a predetermined threshold were used). The transformed columns were then assembled again to form a 2D Xwinnmr spectrum. The typical parameters for the ILT were (for both programs): number of output points, 32 -64; regularization order, 2 (i.e., A is the operator for the second derivative in eq 4); use of a logarithmic D grid. Additional constraints: positivity, smooth vanishing of the function at minimum and maximum Dm . These parameters were found to be optimal for the type of data investigated. Fitting an additional constant offset was tried, but it reduced the stability of the regularization process and was therefore omitted in the results presented here.

## Results and Discussion

In Figure 3 an example of a well-separated DOSY spectrum is presented, which was acquired from a mixture of n -decane with PP1 (sample A). It can clearly be seen that the two substances have overlapping signals in a normal proton NMR spectrum (as is apparent from the F2 projection in Figure 3), but due to their largely different diffusion coefficients it is possible to separate the two components and thus to obtain separate spectra (slices) for each of them. This sample served as a test sample to optimize the experimental setup as well as the numerical treatment of the data. The spectrum also illustrates some drawbacks inherent to the regularization method. Although the signals from n -decane should have a narrow DCD, the regularization broadens these signals quite significantly in the diffusion dimension, exceeding the broadening due to solution viscosity (for comparison, see also the simulations in Figure 2).

Figure 4 shows a DOSY spectrum of a mixture of PS and PP1 (sample B). Here, the signals also overlap in the diffusion dimension since the average diffusion coefficients of the components differ by a factor of around 2 only and have broad distributions. However, separate 1D slices can be obtained easily (Figure 4b). A factor of 2 in diffusion coefficients appears to be the practical resolution limitation of the use of the regularized Inverse Laplace transform, as can be appreciated from the simulations in Figure 2. The accuracy of the diffusion coefficient dispersion of signals with different chemical shifts is higher (on the order of 10%) since the signals can be separated additionally in the second dimension.

Figure 3. DOSY spectrum of a mixture of polypropylene and n -decane in tetrachloroethaned 2 (sample A), transformed by NLREG. The acquisition parameters were T ) 120 ms, ) 2.4 ms, ) 2 ms, and T e ) 20 ms. The 1D spectra in (b) were obtained by integrating over the range of the logarithms of the diffusion coefficient from -9.5 to -8.9 and from -10 to -9.6.

<!-- image -->

In general, the spectra displayed in a DOSY slice along the frequency dimension is subject to the relaxation weighting imposed by the pulse sequence and minor phase distortions arising from J -coupling evolution.

The spectrum in Figure 5 was obtained by transforming the same experimental data with CONTIN and is of lower quality. The projections show some oscillations, which is a clear sign of undersmoothing (the regularization parameter being chosen too low). The digital resolution has little effect on the quality of the result above a certain minimum value (i.e., the solution would not be improved by increasing the number of points in the diffusion dimension), since the regularization will smooth out additional instabilities introduced by the larger number of degrees of freedom. The PS signals in the region of 1.5 -2.2 ppm (Figure 5) are also shifted toward the PP signals in the diffusion dimension. Except for this example the programs performed equally well for all the spectra presented here.

Examples for the application of DOSY to polymers with bimodal MWDs are represented in Figures 6 and 7. These show DOSY spectra of PP2 and PP3 (samples C and D). The corresponding gel permeability chromatography (GPC) traces are represented in Figures 6c and 7c for comparison. It was possible to obtain separate 1D slices for the two components in both cases (Figures 6b and 7b).

The MWDs are well represented in the DCD, however with some peculiarities:

(1) The components in the DCD are weighted according to relaxation, as was discussed in connection with eq 1. The different relaxation behavior of the signals is a consequence of the differences in mobility and molecular environment (mass, sterical situation). The NMR signal corresponding to the low molecular mass fraction clearly discernible in the GPC trace of Figure 6b disappears under the bigger peak in the DCD (Figure 6a). This is a consequence of the limitations of the ILT

Figure 4. DOSY spectrum of a mixture of polypropylene and polystyrene in tetrachloroethaned 2 (sample B), transformed by NLREG. The acquisition parameters were T ) 250 ms, ) 5 ms, and ) 2 ms. The 1D spectra in (b) were obtained by taking the slices at the indicated positions in (a). Integration was not used since this would result in contamination of the spectra of the two components.

<!-- image -->

Figure 5. Same data as in Figure 4 transformed by CONTIN, which in this case produced a result of lower quality than NLREG. The main features of the spectrum are the same, while the projections show oscillations, which is a clear indication for an undersmoothed solution due to too small a regularization parameter R .

<!-- image -->

Figure 6. (a) DOSY spectrum of the polypropylene sample C and (c) its corresponding GPC trace (smoothed). The transformation was performed by CONTIN. The acquisition parameters were T ) 150 ms, ) 3 ms, and ) 2 ms. The 1D spectra in (b) were obtained by taking the slices at the indicated positions in (a). To emphasize the advantage of the chemical shift dispersion in DOSY spectra, we show the column slices through the 2D spectrum at the indicated positions (dashed and dot -dashed projections) in (a). The two cross-sections obviously belong to different components. Integration was not used for the slices since this would result in contamination of the spectra of the two components.

<!-- image -->

and probably also partly due to microaveraging effects. However, the position of the lower maximum may be determined from signals that occur at a unique chemical shift, as is indicated by the dash -dotted line in Figure 6a.

Since relaxation weighting is usually different for different parts of the same molecule, quantification of the DCD is not straightforward.

(2) The positions of the two peaks in the DCDs of Figures 6a and 7a are closer together than the MWD would suggest (cf. eq 6 with an a of 0.5 -0.8). Since the DCD in Figure 7a is well resolved, we may attribute the deviations of the peak positions solely to microaveraging effects. However, it cannot be ruled out completely that differences in coiling behavior of the different polymer fractions give rise to the deviations from the relationship of eq 6, thus invalidating the assumption of a single exponent a .

Figure 7. (a) DOSY spectrum of the polypropylene sample D and (c) its corresponding GPC trace (smoothed). The transformation was performed by NLREG. The acquisition parameters were T ) 150 ms, ) 3 ms, and ) 2 ms. The 1D spectra in (b) were obtained by integrating over the range of the logarithms of the diffusion coefficient from -9.7 to -9.3 and from -10.2 to -9.8.

<!-- image -->

We have taken the view here that the GPC results were more reliable than the DCD solely due to the fact that the former technique is well established and we therefore used it for reference. However, since the GPC measurements are calibrated with respect to polystyrene as standard, the correct determination of the MWD may be problematic. Furthermore, impurities may bias the results, which can be separated in DOSY experiments. In Figures 6a and 7a impurity signals were found in the region of 2.2 -2.5 ppm, which stem from the production process of the polymer samples and may influence the GPC results (in this particular case, however, the effects are probably negligible due to the low molecular weight). Apart from dynamic light scattering (having limitations of its own) there does not exist any other competitor to GPC that may challenge its results. Thus DOSY represents a method that, while largely supporting GPC results, also produces complementary information through the inclusion of chemical shift labeling and consequently microstructural information.

Both DCD curves in Figures 6a and 7a reveal further that significantly different relaxation processes (transverse and longitudinal) occur in the low and the high molecular weight fractions. This could be used to deduce further structural information of the polymeric materials.

Conclusion. The application of DOSY NMR to the investigation of polymer mixtures and MWDs of polymers has been demonstrated here. Highly overlapping proton spectra can be resolved by dispersion in a diffusion coefficient domain. This should be of particular interest for the investigation of the homogeneity of block, graft, cross-linked, or otherwise reprocessed polymers. This technique is a notable complement to GPC since it provides structural information not available from GPC alone, which also bears other experimental problems. In DOSY spectra one can discriminate between different components of the sample by their chemical shifts and their diffusion behavior at the same time, so that impurities, additives, and plasticizers may be identified easily. Wewould also like to note that the detection of such impurities, which would go unnoticed in GPC, could be very useful in quality assurance of industrial polymer products. Another potential application is the study of the coiling behavior and interaction of polymers in different solution environments by the examination of the relation between the MWDand the DCD. Detailed relaxation studies of the different polymer fractions can be performed by use of an additional relaxation labeling step or by variation of the fixed delays in the pulse sequence. 36,37 Chain dynamics could be studied for narrow, well-defined molecular mass fractions.

The limitations of the DOSY method presented are mainly inherent to the data inversion. Other approaches in this field 38,39 are likely to have very similar problems. Improvements in NMR hardware and development of more sophisticated pulse sequences 40 should make it possible to eliminate still persistent artifacts in the measurements, which is crucial for the success of the unstable numerical data inversion techniques. Diffusion separation can easily be combined with a wide variety of NMR techniques available today. Recently, inverse Laplace transformation algorithms for DOSY have become available in a commercial NMR processing package. 41 Therefore we believe that 2D NMR DOSY spectroscopy and its recently reported three-dimensional extensions 42 -45 will find their way to standard applications in polymer research and quality assurance of advanced polymer materials.

Acknowledgment. This work was funded by the Austrian Science Fund, 'Fonds zur Fo ¨rderung der Wissenschaftlichen Forschung', project P 10633-O ‹ CH. We acknowledge helpful discussions and provision of polymer samples and GPC data by Dr. Eberhard Ernst, PCD Polymere Linz, Austria, Prof. Alois Schausberger and Dr. Christoph Brabec, Department of Physical Chemistry, University of Linz, Austria.

## References and Notes

- (1) Tonelli, A. E. NMRSpectroscopy and Polymer Microstructure: The Conformational Connection ; VCH Publishers: Deerfield Beach, FL, 1989.
- (2) Cheng, H. N. J. Appl. Polym. Sci., Appl. Polym. Symp. 1989 , 43 , 129 -163.
- (3) Cheng, H. N. Macromol. Theory Simul. 1994 , 3 , 979 -1004.
- (4) Randall, J. C. Macromol. Chem. Phys. 1989 , C29 , 201 -317.
- (5) Jerschow, A.; Ernst, E.; Hermann, W.; Mu ¨ller, N. Macromolecules 1995 , 28 , 7095 -7099.
- (6) Morris, K. F.; Stilbs, P.; Johnson, C. S., Jr. Anal. Chem. 1995 , 66 , 211 -215.
- (7) Barjat, H.; Morris, G. A.; Smart, S.; Swanson, A. G.; Williams, S. C. R. J. Magn. Reson. B 1995 , 108 , 170 -172.
- (8) Morris, K. F.; Johnson, C. S., Jr. J. Am. Chem. Soc. 1992 , 114 , 3139 -3141.
- (9) Hinton, D. P.; Johnson, C. S., Jr. J. Phys. Chem. 1993 , 97 , 9064 -9072.
- (10) Wu, D.; Chen, A.; Johnson, C. S., Jr. J. Magn. Reson. A 1995 , 115 , 260 -264.
- (11) Fordham, E. J.; Gibbs, S. J.; Hall, L. D. Magn. Reson. Imaging 1994 , 12 , 279 -284.
- (12) Jerschow, A.; Mu ¨ller, N. J. Magn. Reson. , in press.
- (13) Ernst, R. R.; Bodenhausen, G.; Wokaun, A. Principles of Nuclear Magnetic Resonance in One and Two Dimensions ; Clarendon Press: Oxford, U.K., 1987.
- (14) Clayden, N. J.; Hesler, B. D. J. Magn. Reson. 1992 , 98 , 271 -282.
- (15) Morozov, V. A. Regularization Methods for Ill-posed Problems ; CRC Press: London, 1993.
- (16) Tikhonov, A. N.; Arsenin, V. Y. Solutions of Ill-posed Problems ; Wiley: New York, 1977.
- (17) Press: W. H.; Vetterling, W. T.; Teukolsky, S. A.; Flannery, B. P. Numerical Recipes in C , 2nd ed.; Cambridge University Press: Cambridge, U.K., 1992.
- (18) Provencher, S. W. Comput. Phys. Commun. 1982 , 27 , 229 -242.
- (19) Provencher, S. W. Comput. Phys. Commun. 1982 , 27 , 213 -227.
- (20) CONTIN, Version 2 Users Manual, EMBL Technical Report DA05, European Molecular Biology Laboratory, 1984.
- (21) Weese, J. Comput. Phys. Commun. 1993 , 77 , 429 -435.
- (22) Honerkamp, J.; Weese, J. Rheol. Acta 1993 , 32 , 65 -73.
- (23) Honerkamp, J.; Weese, J. Contin. Mech. Thermodyn. 1990 , 2 , 17 -30.
- (24) Engl, H. W. Surv. Math. Ind. 1993 , 3 , 71 -145.
- (25) Weese, J. NLREG: A program for the solution of nonlinear ill-posed problems, User Manual , obtained from author, 1993.
- (26) Weese, J. Datenanalyse in der Rheologie mit Hilfe von Regularisierungsverfahren . Ph.D. Thesis, Albert-LudwigsUniversita ¨t Freiburg i. Brsg., 1992.
- (27) Provencher, S. W. Makromol. Chem. 1979 , 180 , 201 -209.
- (28) Grabowski, D.; Honerkamp, J. J. Chem. Phys. 1992 , 96 , 2629 -2632.
- (29) Brabec, C. J. Calculation of relaxation time spectra with respect to the conversion to molar mass distributions . Ph.D. Thesis, Johannes Kepler Universita ¨t, Linz, 1995.
- (30) Gregory, R. B. Nucl. Instrum. Methods 1991 , A302 , 496 -507.
- (31) Tang, Z.; Wang, S. J. Nucl. Instrum. Methods 1991 , A355 , 548 -551.
- (32) Chen, A.; Wu, D.; Johnson, C. S., Jr. J. Am. Chem. Soc. 1995 , 117 , 7965 -7970.
- (33) Brabec, C. J.; Ro ¨gl, H.; Schausberger, A. Rheol. Acta 1997 , 36 , 667 -676.
- (34) Cosgrove, T.; Griffiths, P. C. Polymer 1995 , 36 , 3335 -3342.
- (35) Flory, P. Princinples of Polymer Chemistry ; Cornell University Press: New York, 1978.
- (36) Lui, M.; Nicholson, J. K.; Lindon, J. C. Anal. Chem. 1996 , 68 , 3370 -3376.
- (37) Dixon, A. M.; Larive, C. K. Anal. Chem. 1997 , 69 , 2122 -2128.
- (38) Stilbs, P.; Paulsen, K.; Griffiths, P. C. J. Phys. Chem. 1996 , 100 , 8180 -8189.
- (39) Delsuc, M. A.; Malliavin, T. E. Anal. Chem. 1998 , 70 , 2146 -2148.
- (40) Jerschow, A.; Mu ¨ller, N. J. Magn. Reson. 1997 , 125 , 372 -375.
- (41) NMR SUITE 2.1, Bruker Analytische Messtechnik GmbH, 1997.
- (42) Jerschow, A.; Mu ¨ller, N. J. Magn. Reson. A 1996 , 123 , 222 -225.
- (43) Gozansky, E. K.; Gorenstein, D. G. J. Magn. Reson. B 1996 , 111 , 94 -96.
- (44) Wu, D.; Chen, A.; Johnson, C. S., Jr. J. Magn. Reson. A 1996 , 121 , 88 -91.
- (45) Lin, M.; Shapiro, M. J. J. Org. Chem. 1996 , 61 , 7617 -7619.