## Determination of Molecular Weight Distributions for Polymers by Diffusion-Ordered NMR

Aidi Chen, Donghui Wu, and Charles S. Johnson, Jr.*

Contribution  from the  Department of  Chemistry, University of North Carolina, Chapel Hill, North Carolina 27599-3290

Received April 10, I995@

Abstract: Diffusion-ordered NMR spectroscopy (DOSY), a technique based on pulsed field gradient NMR (PFGNMR), was used to characterize molecular weight distributions for samples of poly(ethy1ene oxide) in D2O. The distribution of  diffusion  coefficients  G(D)  was  obtained by  analysis of  PFGNMR  data with  a  modified  version  of  the  wellknown constrained  regularization  program CONTIN.  Regularization was considerably improved for broad distributions by setting the weights c, in C0NTI"s quadrature formula equal to (DlT/om~~m where D , is the diffusion coefficient corresponding to the maximum in G(Dm)Dm and m is an index.  Here Xm varies linearly from +2 to -2 with log(D,) across the distribution.  This amounts to enhancing low amplitude regions of G(D)D during analysis.  The estimated distribution was then converted to the mass weighted distribution of  molecular weights by means of the relation D = M-o.62  (with D in units of  m2 s-l)  obtained from experiments on monodisperse reference standards.  In this  study spin relaxation rates were independent of  molecular weights and intermolecular averaging effects were insignificant. As an illustration, molecular weight distributions were determined for two broadly distributed samples. The number and weight average molecular weights and the polydispersities agreed well with values provided by the manufacturer when the PFGNMR data sets had signal-to-noise ratios greater than 500.

## Introduction

High polymers are characterized by a distribution of molecular weights. Some  information  about  the width  of the distribution  can  be  obtained  by  measuring  different  average molecular  weights  for  a  polymer, e.g. number  average  and weight average.  However, knowledge about the contribution of  each molecular size requires that the full molecular weight distribution (MWD)  be determined.  MWDs are of fundamental importance in polymer science because (a) the distributions give evidence  about the  type  of  polymerization employed and  (b) the distributions determine the physical properties of  polymer mixtures.

The determination of  MWDs has been approached by both chemical and physical methods, but for higher molecular weights (M &gt; 25 000) physical methods  are  more  reliable. Gel permeation chromatography (GW) and dynamic light scattering (DLS) are popular methods for the determination of MWDs.',2 Both  of  these  methods  detect  transport  rates  that  depend  on molecular  size  and  require  calibration  or data  transformation to obtain the MWD. Pulsed field gradient NMR  (PFGNMR) is also  sensitive to  molecular size and provides  a method for the  determination  of  weight  average  molecular  weights  for polymer^.^-^ Through enhancements and extensions of PFGNMR, it is now possible to obtain diffusion ordered NMR (DOSY)  spectra  of  polydisperse  samples  that  display  the complete mass weighted distribution of  tracer diffusion coefficients at  each chemical shifts8

* Author to whom correspondence should be addressed.

@Abstract  published in Advance ACS Abstracts, July  15, 1995.

( 1 )  Yau,  W.;  Kirkland,  J. J.; Bly,  D.  D. Modem  Size  Exclusion Chromatography; Wiley:  New York,  1919.

(2)  Chu,  B. Laser  Light  Scattering: Basic  Principles  and  Practice; Academic Press, Inc.:  Boston, 1991; pp  1-343.

( 3 ) von Meenvall, E. D. J. Magn. Reson. 1982, 50, 409-416.

(4)  Raghavan, R.;  Maver, T. L.;  Blum, F. D. Macromolecules 1987,20, 814-818.

(5) Callaghan,  P. T.; Pinder, D. N. Macromolecules 1983, 16, 968973.

(6) Fleischer, G. Polymer 1985, 26, 1677-1682.

(7) Fleischer, G. Makromol. Chem. 1985, 6,463-467.

In  this  article  we  propose  a  DOSY  based  method  for  the determination of  MWDs.  The constrained regularization program CONTIN9310 is  used  as  in  previous  DOSY  studies  of polydisperse samples,*-'  but special modifications are made to obtain accurate descriptions of broad distributions of  diffusion coefficients.  These modifications give major improvements in the accuracy  of measured  molecular  weight  distributions. Extensive analyses  of  simulated  and experimental PFGNMR data  sets with  various  signal-to-noise (SN) ratios  have  been performed  to  establish  the  range  of  validity  of  the  DOSY/ CONTIN method.  Poly(ethy1ene oxide) (PEO) samples with narrow  and broad  MWDs  were  studied, and  the  scaling law relating  mass  weighted  tracer  diffusion  coefficients  (D)  and molecular weights was determined with standard monodisperse PEO samples.  For  polydisperse  samples the  distributions  of diffusion coefficients were converted to MWDs by means of the  scaling relation.  The MWDs were then used to calculate average molecular weights and polydispersities for comparison with  the  results  of  GPC  and  viscosity  measurements. In  all cases  the  results  were  in  satisfactory  agreement  with  data provided by  the manufacturer.

We note that  the  DOSY  method  is  analogous to  the  DLS method.12 Both  experiments  require the inverse  Laplace transformation (ILT ) of  experimental  data  sets  to  determine distributions of  diffusion coefficients.  Therefore, the improvements reported here in the CONTIN analyses also apply to DLS. In general the DOSY and DLS methods complement each other. Special features of  MWD determinations by  means of  DOSY are the following:  (a) the instrumentation (while expensive) is widely available, (b) different molecular  species in a mixture can bk  distinguished by their chemical shifts, and (c) the signal intensity depends on the number of NMR active nuclei in each molecule,  a  quantity  proportional  to  the  molecular mass. In principle, polymer solutions in heterogeneous systems such as turbid  suspensions  and  porous  media  can  be  studied. The primary requirements are  (a) high S/N ratio (&gt;500), (b) low concentrations  so  that  molecules  act  independently,  and  (c) nuclear relaxation times that are long and not strongly dependent on  molecular  weight. In  contrast  to  this,  the  DLS  method usually gives high S/N ratios for polymers, has signal intensities that  depend  on  the  square  of  the  molecular  mass,  requires transparent  samples,  and  usually  permits  no  resolution  of molecular species.

@)Moms, K. F.; Johnson, C. S., Jr. J. Am. Chem. SOC. 1993,115,42914299.

(9) Provencher, S. W. Comput. Phys.  Commun. 1982, 27, 213-227.

(10)  hovencher, S. W. Comput. Phys.  Commun. 1982, 27, 229-242.

(1 1) Moms, K. F.;  Johnson, C. S.,  Jr.; Wong, T. C. J. Phys. Chem. 1994, 98, 603-608.

(12) Provencher, S. W.;  Hendrix, J.; De Maeyer, L. J. Chem. Phys. 1978, 69, 4213-4216.

## Background

Standard PFGNMR experiments employ two matched gradient  pulses  separated by  the  interval  A -6, each having the effective area q = yg6 where y is the magnetogyric ratio, and g and 6 are the amplitude and duration of the gradient pulses, respe~tive1y.l~ The signal is detected either as a free induction decay (LED experiment) or a half echo (spin echo or stimulated echo experiments).  Fourier transformation with respect to time then yields a spectrum in which the peak intensities are given by:

$$\tilde { f } ( q ) = \int & R ( T _ { 1 } , T _ { 2 } ) \ G ( D ) \exp [ - D q ^ { 2 } ( \Delta - \delta / 3 ) ] \, d D \quad ( 1 )$$

where R(TI ,T2) specifies the attenuation resulting from nuclear spin relaxation and G(D) is the mass weighted distribution of tracer  diffusion  coefficients ( D). For  monodisperse  samples G(D) is a delta function; and a plot of  InRq)] versus q2(A -6/3) yields  a  straight line  with  a  slope equal  to the diffusion coefficient D. With polydisperse samples, however, this type of  plot  shows curvature that depends primarily on the characteristics of  the distribution function G(D).

The  aim  of  the  analysis  of  PFGNMR  data  is  to  obtain  a function G(D) that  can  be  converted  into W(M), the  mass weighted MWD.  This goal may be complicated by two factors. First, the relaxation factor R(Tl,T2) may depend on the molecular weight  so  that  the  product R(Tl,T2)G(D) cannot  be  easily separated.6 In the LED experiment where all the time intervals except 6 are held constant, molecules with small values of TI and T2 are  underrepresented  in  the  integral. In  general  this complication cannot be ignored, and must be evaluated for each type of polymer sample.  However, spin relaxation rates in high polymers  are  often  determined  by  segmental  motion  (local) rather  than  overall  tumbling  rates  so  that R(Tl,T2) is  approximately  independent  of  the  molecular  weight. In  the following we assume that R(Tl,T2) is a constant, an assumption that is consistent with previous experimental ~tudies.'~.'~

The  second complicating factor  arises from intermolecular interactions.  A consequence of these interactions is a 'microaveraging effect'  in  which  the  effective  diffusion coefficient of a molecule depends on the molecular weights of neighboring molecules.6,16  The solute molecules tend to diffuse at the same rate, and the nonlinearity of the semilogflq)  plots is decreased. All physical methods for the measurement of molecular weights require that the molecules contribute independently.' In order to avoid molecular overlap and the resulting averaging effects, the concentrations must be kept low and extrapolation to zero concentration may be required.

(13) Stejskal,  E. 0.; Tanner, J.  E. J.  Chem. Phys. 1965, 42, 288-292. (14)Liu. K.: Ullman. R. J.  Chem. Phvs. 1968. 48. 1158-1168.

(15) Fleischer, G.; Geschke, D.; K&amp;rg.g d r ,   J.; Heink, W. J. Magn. Reson. 1985, 65, 429-443.

(16) Callaghan, P. T.; Pinder, D. N. Macromolecules 1985, 18, 373379.

(17) Flory, P.  J. Principles  of  Polymer  Chemistry; Cornell  University Press:  Ithaca, 1953; Chapter VII.

## Data Transformation

Equation 1  shows that the signalflq) is the Laplace transform of  the  distribution  function G(D) with  respect  to D. The inversion  of  the  Laplace  transform  to  obtain G(D) from  the signal  is  an  ill-posed  problem. This  means  that  the  answer cannot  simply be  extracted from  the  data,  and  strategies  are required to obtain an estimate of G(D). A number of  inverse Laplace  transform  methods  including  exponential  sampling, constrained regularization,  and  maximum  entropy have  been developed for this problem.'*  The constrained regularization program CONTIN is competitive with the other methods, and has the advantage of being widely distributed and extensively tested.Ig  Also, CONTIN offers great flexibility through numerous user defined control variables.I0

According  to  eq  1,  the  experimental  data  set  at  a  given chemical shift can be represented as a set of intensities Yk versus rk, the incremented values of  q2(A -83). With the program CONTIN, the inversion of  eq  1 to obtain G(D) is handled by solving the set of  linear algebraic  equation^,^

$$y _ { k } = \sum _ { m = 1 } ^ { N _ { k } } c _ { m } \, F _ { k } ( \lambda _ { m } , t _ { k } ) \, s ( \lambda _ { m } ) + \sum _ { i = 1 } ^ { N _ { L } } L _ { k i } \beta _ { i } \quad ( 2 )$$

to determine the unknown function s(A) at Ng grid points Am. Here the cm are weights of the quadrature formula, and Fk(Am,tk) are known decay functions.  The second term on the right-hand side of eq 2 permits a background to be included, e.g. a constant background PI results from the choice NL = 1 and Lkl = 1. In the present context, s(A) is  associated with the distribution of diffusion  coefficients  and Fk(Am,tk) = exp(-A,tk), where  A corresponds to D.

Applications of CONTIN to simulated data and cemparisons with other methods have recently been reviewed by SttpBnek.'* The basic problem is to eliminate oscillatory solutions which are not filtered by the IL T , but which have no physical meaning. With CONTIN the solution is constrained by (a) absolute prior knowledge, (b) statistical prior knowledge, and (c) the principle of parsimony.  Of those solutions not eliminated by (a) and (b), parsimony requires that the simplest be chosen.  Essentially this means that  solutions  are  selected  for  smoothness  and  the minimum  number  of  peaks. The  selection  process  can  be implemented by penalizing solutions on the basis of integrated squared second derivatives.

The standard application of  CONTIN is quite successful in recovering  distribution functions  from  simulated data  sets  in the absence of  noise.  But in the presence of  noise CONTIN tends  to  give  smaller  average  diffusion  coefficients  (D)  and reduced standard deviations (SD)/(D)  relative to the true values, especially for broad  distributions. The finding by  JakeS that the  standard  application  of  CONTIN  over-smooths the G(D) distribution  in  the  region  of  small D while  seriously  undersmoothing for large D values is particularly important for the present study.' This effect has to do with the equality of  the penalty for different ranges of D values since standard  CONTIN penalizes the G(D) function on the logarithmic axis.  Note that two separated peaks with identical areas in a plot of G(D) versus D will appear quite asymmetric when G(D) is  plotted versus log(D).  In order to restore the equality of areas, G(D)D instead of G(D) must be plotted with respect to log(D), L e .  G(D) d D = G(D)D d(lnD).  The result of  unequal smoothing is that noise can  produce  a  secondary peak  in  the  large D  region of the G(D)D versus log(D) plot.  When G(D) splits into two peaks, (D)  for  the  main  peak  shifts  to  a  smaller value  and  SD/(D) decreases.

(18) StEpPnek,  P. In Dynamic  Light Scattering; Brown,  W.,  Ed.; Clarendon Press:  Oxford,  1993; pp  177-241.

(19) Stock, R. S . ; Ray, W. H. J. Polym. Sci., Polym. Phys. Ed. 1985,23, 1393-1447.

(20) Jakes, J. Czech. J. Phys. 1988, 838, 1305.

Regularization can be improved by switching to 'integration off' in CONTIN, i.e.  setting the control parameter IQUAD = 1 so  that c,, , = 1. In  this  case  G(D)D rather  than  G(D) is analyzed on the logarithmic axis.  With this modification,  most of  the 'noise peak' disappears in the CONTIN output and the main peak gives more accurate values of (D) and SD/(D).  This choice of cm improves the estimation of  G(D) by means of  eq 2 and provides a clue for further enhancements.  Extending  this idea, we propose that cm be replaced with  ( D m / D m a x ) X m  in eq 2 where xm is incremented from +2 to -2 as log(D) ranges from -12 to -9 in our analyses.  The range of log(D) will, of course, depend on the distribution being studied; and in general it must be  set  as  narrow  as  possible consistent with  the  distribution having zero amplitude at both  limits. Typically at xm = f l , the  amplitude of  G(D)D is about 10% of  the maximum value. With this choice, cm = 1 near the center or maximum of  the distribution  (where D = Dmm)  while providing the necessary amplitude enhancement where the amplitude is  small.  Thus, cm serves as  a  microscope with  adjustable amplification that enhances the  ability  of  CONTIN  to  analyze regions  of  low amplitude, here the wings of the diffusion distribution curve. It should be  noted that  the choice of cm values depends on the function to be fitted  so that  special attention can be  given to the region of interest.  The CONTIN analysis then returns the distribution  G(Dm)Dm/cm, and  G(Dm)  can easily be  extracted.

The final  step in  determining the  distribution of  molecular weights requires that G(D) be transformed into either the number weighted MWD, n(M),  or the mass weighted MWD, W(M), where W(M) = n(M)M.  For example, W(M) can be  obtained with  the  equation W(M) = G(D) IdDldMI if  the  relationship between  D  and M is  known. The  scaling  law  must  be established for each polymer system, but for gaussian random coils we expect a relation of  the form:

$$D = A M ^ { 2 }$$

In  terms  of the  distributions W(M) and  n(M&gt;,  the  number weighted molar mass fin and the mass weighted molar mass MW are given by

$$\bar { M } _ { \mathrm n } = \frac { \int n ( M ) \, M \, d M } { \int n ( M ) \, d M } ; \quad \bar { M } _ { \mathrm w } = \frac { \int W ( M ) \, M \, d M } { \int W ( M ) \, d M } \quad ( 4 ) \quad \begin{array} { c c c } \mathrm { 1 } & \mathrm { 0 } & \mathrm { 1 } \\ \mathrm { 0 } & \mathrm { 3 } & \mathrm { 1 } \end{array} \quad \begin{array} { c c c } \mathrm { 1 } & \mathrm { 0 } & \mathrm { 1 } \\ \mathrm { 0 } & \mathrm { 3 } & \mathrm { 1 } \end{array}$$

and the polydispersity is defined as Mw/Mn.

## Simulations

Simulated MWDs with added noise provide a good test of the analysis methods.  We have chosen the log normal distributi o n to represent W(M) for a typical polymer sample.  Thus2I

$$W ( M ) = \frac { 1 } { M ( \ln \sigma ) \sqrt { 2 \pi } } \exp \left ( - \, \frac { ( \ln M - \ln M _ { 0 } ) ^ { 2 } } { 2 ( \ln \sigma ) ^ { 2 } } \right ) \quad ( 5 ) \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

Values of W(M) were calculated at 128 values of  1nM equally

(21) Hunter, R. J. Foundations of Colloid  Science; Oxford University Press: Oxford, 1987; Vol. I, p 131.

1

<!-- image -->

Figure  1. (D) versus u for  the  simulation  (solid  line),  standard CONTIN analysis (A), CONTIN with cm = 1 (0), and CONTIN with computed cm values (0) (see text).

<!-- image -->

.

.

l

l

Figure 2. Standard deviationl(D) versus u for the  simulation (solid line),  standard  CONTIN  analysis  (A),  CONTIN  with c , = 1 (0) CONTIN with computed c, values (0) (see text).

spaced in the range lnM0 f 4 1 1 1 0 , and MO was set equal to lo5. The calculations  were repeated with a values ranging from 1.25 to 3.25, and W(M&gt; was  converted to  G(D)  according to  the scaling law in eq 3 with A = and a = -0.6  when D is in units of m2  s-l. PFGNMR data sets were then generated by means of  eq 1 for  sets  of 4 values, and Gaussian noise with RMS deviation of relative to the largest signal (smallest 4 value) was added to each data point.

The simulated  data sets were analyzed  by means of CONTIN with three different choices of  weighting factors to obtain (D) and  SD/(D). The  results  are  shown  in  Figures 1 and 2 as functions of a for standard CONTIN (A), CONTIN with c, , , = 1 (0), and CONTIN with computed cm values (0). It  is clear that  for broad distributions  (a &gt; 2),  standard CONTIN loses accuracy.  Both (0)  and SD/(D) are usually  smaller than the input values (solid curves) as a consequence of the appearance of  a  noise  peak  in  the  computed distribution. This  effect  is illustrated  in  Figure 3 which  shows a  simulated distribution G(D)D (solid line) with u = 3.2 for comparison with distribu-

-Q

Figure 3. The normalized distribution G(D)D. Simulated distribution with MO = lo5  and u = 3.2 (solid line), the standard CONTIN estimate (dotted line), and  CONTIN estimate with cm = 1 (dashed line).  The number of grid points Ng in the CONTIN analyses was 3  1, and cubic splines were used to obtain smooth displays.

<!-- image -->

-Q

Figure 4. The simulated distribution G(D)D with MO = lo5  and u = 3.2 (solid line),  computed cm values (dashed line), and the  effective distribution to be estimated by  CONTIN with the computed cm values (dotted line). Cubic splines were used to obtain smooth displays from the 31 cm values.

<!-- image -->

tions obtained with standard CONTIN (dotted line) and CONTIN with cm = 1 (dashed line).

We note that even with noise levels as low as 1 part in  lo3 the results calculated for the main peak returned by  standard CONTIN fluctuate wildly as o changes.  More accurate averages can  be  obtained  from  the  bimodal  distributions by  including both  peaks  in  the  calculation. However, the  secondary peak tends to vanish and the averages show considerable improvement  when cm = 1; and  even  more  accurate  and  consistent results are obtained with computed cm values as described above. In Figure 4 we show the simulated curve G(Dm)Dm (solid line), the cm values (dashed line), and the effective function G(Dm)Dm/ cm analyzed by CONTIN (dotted line).  The actual distribution G(D)D recovered from the CONTIN analysis with a computed cm set is shown in Figure 5 (0) with the simulated log normal distribution (solid line).

After analysis with CONTIN, the G(D) curves are converted to W(M) distributions  and  the  averages an and M, and  the polydispersity fiw/&amp;, are calculated.  The results are displayed in  Figures 6 through  8. In  the  fin  calculation  (Figure  6), standard CONTIN shows unacceptable large errors for o &gt; 2. CONTIN with cm = 1 is better  and CONTIN with computed cm's gives the best estimate.  However, the situation is different for M, (Figure 7) where  larger  molecules  (lower  diffusion coefficients) receive heavier weighting.  Here standard CONTIN, which emphasizes the region of low diffusion coefficients, is more accurate  than the calculation  with cm = 1.  But as before,

-9

Figure  5. The  simulated  distribution G(D)D (solid  line)  and  the estimate obtained by CONTIN with computed cm values (0).

<!-- image -->

Figure 6. The number average molecular weight fin versus the width u of the simulated distribution obtained by standard CONTIN analysis (A), CONTIN with cm = 1 (0), and CONTIN with computed cm values (0). The solid line indicates the input values.

<!-- image -->

the  calculation  with  computed cm's is  clearly  the  best. The calculated polydispersity versus input o plot in Figure  8 also reveals differences in the accuracy of the calculation methods. In all cases examined, the method with computed em's provides the best estimate of G(D) and W(M). Further simulations with different levels of noise show that this method can improve the fitting results for the signals with S/ N ratios greater than 500.

## Experimental Section

Deuterium oxide (D, 99.9%) from Cambridge Isotope Laboratories was  used  as  the  solvent for all  samples. The  poly(ethy1ene  oxide) samples  (PEOlK, PE03K,  PEOSK,  PE027K), kindly  provided  by Professor  J.  M.  DeSimone,  were  prepared  with  the  standard  living anionic  polymerization  technique.22  The  molar  masses  for  these samples  were  obtained by  GPC  on  a  Waters  150-C gel  permeation chromatograph with Ultrastyra-gel columns having pore sizes of  100, 500,  lo3, 104, and IO5 8, and  using  THF  as  eluant. Polystyrene standards  (Showa  Denko) were  used  to calibrate  the  molar  masses. Other PEO samples were purchased from American Polymer Standards Corp.  The samples and their reported molecular weights are listed in Tables 1 and 2.  All PEO samples were used as received without further purification.

(22) Odian,  G. Principles  ofPolymerization; John Wiley &amp; Sons:  New York, 1991.

1

Figure 7. The weight average molecular weight fiw versus the width u of the simulated distribution obtained by standard CONTIN analysis (A), CONTIN with cm = 1 (0), and CONTIN with computed cm values (0). The solid line indicates the input values.

<!-- image -->

Figure 8. The polydispersity  kw/fin versus the width u of the simulated distribution obtained by standard CONTIN analysis (A), CONTIN with cm = 1 (0). and CONTIN with computed cm values (0). The solid line indicates the input values.

<!-- image -->

Table 1. Monodisperse Poly(ethy1ene oxide) Samples

| sample no.   | data source   |   G, (103g mol-') |   M, (103g mol-') |
|--------------|---------------|-------------------|-------------------|
| PEOlK        | GPC           |               1.2 |               1.4 |
| PE03K        | GPC           |               3.4 |               3.8 |
| PEO5K        | GPC           |               5.1 |               5.6 |
| PE027K       | GPC           |              27.3 |              33.4 |
| PEOlOOK      | manufacturer  |               103 |               110 |
| PE0240K      | manufacturer  |               240 |               250 |
| PE05OOK      | manufacturer  |               486 |               510 |

Table 2. Polydisperse Poly(ethy1ene  oxide)

| sample type   |   M n (103g mol-') (manufacturer) |   n;rW (io3g mol-') (manufacturer) |   M" (io3g mol-') (DOSY) |   G W (io3g mol-') (DOSY) |
|---------------|-----------------------------------|------------------------------------|--------------------------|---------------------------|
| PE0200K       |                              47.0 |                                204 |                       46 |                       180 |
| PE0120K       |                              36.5 |                                123 |                       35 |                       110 |

Systems,  Inc.,  with  actively  shielded  gradient  coils  (coil  constants: 0.156 T  m-'A-l and 0.1785 T  m-'A-') were  used  in  these  experiments.26 In all NMR experiments, the probe temperature was maintained at 298 i 1 K by the standard Bruker temperature control unit, and 5 mm sample tubes were used.

From 20 to 40 FIDs, each associated with a different q value (1 x 104 to 3 x lo6  m-'),  were collected with an ASPECT-3000 computer in each ernrhment.  In  each case the maximum  attenuation reduced the  signal % or less of  its original  intensity so that polydisperse polymer samples could be completely characterized.  The LED pulse sequence2'  was employed with diffusion time (A = 105.5  ms) and eddy current delay time (T, = 50 ms). The data files were transferred via Bruknet  from the ASPECT-3000 to a  Silicon Graphics (SGI) workstation; and software package FELIX  (Hare Research, Inc.) was used for Fourier transformations, phasing, and polynomial baseline corrections.  All the analysis programs were written in FORTRAN on SGI workstations, and the diffusion coefficients and their distributions were determined with a version of CONTIN modified in-house.

## Results and Discussion

Microaveraging. In order to test for microaveraging effects under our experimental conditions, a mixture of equal weights of  the PEOSK (Mw = 5000) and PEOlOOK (Mw GZ 100 000) samples at a total concentration of  1 g/L in D2O  was studied with PFGNMR.  The best fit to a plot of InMq)] versus q2(A -6/3) for the methylene peak of PEO was found to contain fast and slow components with the diffusion coefficients 1.3 x 1O-Io and 1.9 x lo-" m2 s-I, respectively.  This result matches within experimental  error the diffusion coefficients obtained  for samples  containing  only  PEOSK  (1.1 x 1O-Io m2 s-l)  and PEOlOOK (1.9 x lo-"  m2  s-')  at the same total weight percent of PEO.  Therefore, we conclude that the microaveraging effect on diffusion coefficients resulting from intermolecular interactions is insignificant at concentrations of  1 g/L or lower.

Scaling  Relation. The  relationship between  the  mass weighted tracer diffusion coefficient D and mass average molar mass M, was  established  for monodisperse  PEO  samples  (1 g/L of  PEO  in  D20)  by  measuring  the  diffusion  coefficients for monodisperse samples with PFGNMR.5  The results shown in Figure 9 verify that log(D) changes linearly with log(MW), and as expected the scaling relationship has the form D = M. Analysis of  the data in Figure 9 shows that A = lod7 62 and a = -0.62 with  D  in  units  of  m2 s-I in  good  agreement  with previous studies.28

Molecular Weight Distribution for PEO.  As a test of  the computed cm method, MWD's  were determined for two polydisperse PEO samples.  The large amplitude of the methylene peak in these samples ensured that signal-to-noise ratios greater than 1000 could easily be achieved with concentrations as low as  1 g/L. The procedure was to analyze theflq)  data set for the methylene signals first with standard CONTIN.  Then based on the computed distribution  function G(D), (D), and SD values, a  set  of c,,, values was generated. A CONTIN analysis was

(25) Boemer, R. M.; Woodward, W. S. J. Magn.  Reson. A 1994, 106, 195-202.

(26)  Gibbs, S. J.; Moms, K. F.;  Johnson, C. S. , Jr. J. Magn. Reson. 1991, 94, 165-169.

The DOSY experiment has been described in detail e l s e ~ h e r e . ~ ~ ~ ~ ~ Instrumentation for the PFGNMR experiments includes a Bruker AC250 spectrometer with computer controlled gradient drivers designed and constructed in-house.25 Two probes custom built by Cryomagnet

(23)Monis, K.  F.; Johnson, C. S., Jr. J. Am.  Chem. SOC. 1992, 114, 3139-3141.

(24)  Hinton, D. P.; Johnson, C. S., Jr. J. Phys. Chem. 1993, 97, 90649072.

(27)Gibbs, S. J.; Johnson, C. S., Jr. J. Magn.  Reson. 1991, 93, 395402.

(28) Brown, W.; Stilbs,  P.; Johnsen, R. M. J. Polym. Sci., Polym. Phys. Ed. 1983.21, 1029-1039.

I

<!-- image -->

Figure  9.  Log(D/m* SKI) versus log(&amp;Jg mol-]) for monodisperse PEO samples.

<!-- image -->

I

Figure 10.  The MWD function W(M)M for PE0200K obtained from CONTIN analysis with computed cm values. The curve is a cubic spline display of 31  data points.

then performed with these weighting factors to obtain a better estimate  of G(D). After  converting  to  MWD,  the  resulting W(M)M for  PE0200K  is  shown  in  Figure 10. Also,  the molecular weights k,, and k , of the two PEO samples obtained from CONTIN analyses with computed em's are listed in the Table 2 along with the data provided by the American Polymer Standards Corp.  The agreement is quite satisfactory for these samples; and when appropriate conditions (described above) are met,  the  DOSYKONTIN technique  may  be  the  method  of choice for the determination of  MWD's.

Diffusion  ordered NMR offers  several  advantages  for  the determination  of  MWD' s compared  with  standard  methods. Sample preparation is  simple and  switching solvents is easy. Dust and impurities in the solution do not interfere as long as any additional signals can be resolved from the polymer peaks. Also, mixtures of polymers can be analyzed simultaneously if their  chemical  shifts  are  different. Finally,  the  relationship between the measured quantity (here diffusion coefficient) and molecular weight is not instrument dependent and can be used universally.

## Conclusion

An improved pulsed field gradient NMR method has been reported for the determination of molecular weight distributions of polymer samples.  This method makes use of the constrained regularization program CONTIN with a set of weighting factors (cm) in the quadrature  formula  that depend explicitly on diffusion coefficients.  With this modification, CONTIN gives a better estimate  of  the  distribution  of  diffusion  coefficients over  the whole diffusion  dimension, especially  at  the  extremes  where the amplitudes are low.  Extensive simulations also show that the mass weighted molecular weight distribution W(M) derived from G(D) gives more accurate estimates  of both weight average and number average molecular weights than can be  obtained with standard applications of CONTIN.  Weighting factors (c,) that are dependent on the decay rate (diffusion coefficient) can also be used to improve CONTIN analyses in other applications, e.g. dynamic light scattering.  Finally, we have demonstrated that  diffusion-ordered NMR with  the  improved  CONTIN analysis can provide accurate molecular weight distributions  for polymers. The success of  this method  depends on good S/N ratios,  relatively  long  (mass  independent)  nuclear  relaxation times,  and  low  concentrations  so that  microscopic averaging effects  can  be  avoided. It  should  be  noted  that  PEO  is  a particularly favorable example.  In addition to mass independent relaxation rates, PEO has a strong 'H  signal and a simple NMR spectrum.  Some other polymers may be less amenable to this type of analysis.  However, sensitivity can be improved by using a  modem  high-field  spectrometer  in  place  of  the  250  MHz system.

Acknowledgments. This work was supported in part under National  Science Foundation Grant No.  CHE 9222590.  The authors thank Dr. Jun Lin in Prof. DeSimone's laboratory at UNC for PEO samples and GPC measurements.

JA95 1 1 50Q