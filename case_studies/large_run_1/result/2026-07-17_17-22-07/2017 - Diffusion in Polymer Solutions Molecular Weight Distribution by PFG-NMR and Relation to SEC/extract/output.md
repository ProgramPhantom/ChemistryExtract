<!-- image -->

## Diffusion in Polymer Solutions: Molecular Weight Distribution by PFG-NMR and Relation to SEC

Xiaoai  Guo,*  Esther  Laryea,  Manfred  Wilhelm,  Burkhard  Luy, Hermann Nirschl, Gisela  Guthausen

Quantification  of  diffusion  coefficient  distribution  (DCD)  and  correlation  with  molecular weight distribution (MWD) of polymers is still an issue in pulsed field-gradient nuclear magnetic  resonance  (PFG-NMR).  The  conventional  scaling  law  utilized  so  far  to  relate  diffusion coefficient and molecular weight only holds true for the determination of MWD at sufficiently low concentrations. To extend measurement limits and to get a good signal-to-noise ratio, an exponential correlation is introduced to describe the effect of polymer concentration on diffusion in PFG-NMR. Two model polymers (polystyrene and poly(methyl methacrylate)) dissolved in deuterated chloroform are studied at different concentrations in the range of 0.16-8 wt%.

The DCDs are determined by modeling the measured signal attenuation  with  three  methods  (gamma  distribution,  log normal  distribution,  and  tailored  norm  regularization).  It  is shown  that  the  proposed  method  applies  to  the  PFG-NMR measurements  on  polymer  solutions  over  a  wide  concentration  range,  providing  almost  the  same  MWDs  as  those obtained  at  low  concentrations.  The  MWDs  retrieved  from NMR  experiments  agree  well  with  those  by  size  exclusion chromatography.

## 1. Introduction

Knowledge of physical polymer properties, e.g., dynamics in solution, is of great importance to predict the behavior in  polymer  study  and  synthesis.  In  the  past  decades

Dr.  X.  Guo,  Prof.  M.  Wilhelm Institute  for  Chemical  Technology  and  Polymer  Chemistry Karlsruhe  Institute  of  Technology  (KIT) Engesserstrasse  18,  76128  Karlsruhe,  Germany E-mail:  xiaoai.guo@kit.edu Dr.  X.  Guo,  Prof.  B.  Luy,  Prof.  H.  Nirschl,  Prof.  G.  Guthausen Pro 2 NMR IBG-4  and  MVM Karlsruhe  Institute  of  Technology  (KIT) Adenauerring  20b,  76131  Karlsruhe,  Germany E.  Laryea Institute  of  Thermal  Process  Engineering Karlsruhe  Institute  of  Technology  (KIT) Kaiserstrasse  12,  76131  Karlsruhe,  Germany

<!-- image -->

various  techniques  have  been  developed  and  utilized  for polymer  characterization  to  get  a  better  knowledge  of polymer molecular mass, structure,  morphology,  and  diffusion in polymer solutions. [1,2]  Among them, for instance, the molecular weight distribution (MWD) and polydispersity index (PDI) reflect the type of polymerization reaction and  thus  affect  the  physical  and  mechanical  properties of  polymer  mixtures. [3]   Size  exclusion  chromatography (SEC),  also  known  as  gel  permeation  chromatography,  is one of the most common methods used to directly determine  MWD  based  on  the  hydrodynamic  volume  of  the dissolved  polymer.  However,  SEC  measurements  require special sample preparation and a large amount of solvent, and they are time consuming. On the other hand, nuclear magnetic resonance (NMR) has proven to be a very useful noninvasive  method  for  characterizing  polymer  microstructures,  understanding  polymerization  mechanisms,

2016WILEY-VC2He

and  studying  polymer  dynamics. [4,5]   Diffusion  ordered spectroscopy (DOSY) NMR, i.e., pulsed field-gradient (PFG-) NMR is  known  to  indirectly  measure  the  molecular  size via  the  diffusion  coefficient D which  is  related  to  molecular weight M .  This  technique has been used for identification  of  different  chemical  components  in  mixtures  via their  chemical  shifts  in  many  fields  from  medical  and biological  sciences  to  material  sciences.  A  more  detailed description  of  the  principles  and  applications  of  DOSY can  be  found  in  reviews. [6,7] As  compared  to  SEC,  pulsed field-gradient nuclear magnetic resonance (PFG-NMR) has several  advantages  concerning  sample  preparation  and amount of solvents. Currently, the measurement time is in the same range as SEC. Simultaneous chemical analysis of polymer mixtures is possible via analysis of chemical shift and J -couplings. Moreover, impurities in the polymer solution do not have a direct interference in determining the self-diffusion of the polymeric species if the peak signals of  the  polymer  under  study  can  be  resolved  in  the  DOSY spectra, whereas the alternative technique, dynamic light scattering,  requires  well-prepared  dust-free  and  diluted samples.

PFG-NMR  measurements  deliver  the  diffusion  coefficient distribution (DCD), which is related to the polymer polydispersity. Historically, only the median values were considered  of  both,  DCD  and  MWD.  The  conventional scaling law expressed in the form of D = KM -α has often been used as the basis for the molecular weight measurement by PFG-NMR, [8]   where K and α are  scaling  parameters  depending  on  the  type  of  the  polymer  system. Based  on  this  empirical  scaling  power  law,  there  have been  numerous  publications  related  to  the  influence  of molecular  weight  polydispersity  on  the  PFG-NMR  measurements  as  well  as  the  determination  of  the  average molecular weight and the MWD from the NMR diffusion experiments. [9-19]  It should be pointed out that the scaling parameters ( K , α )  are  only  constant for polydisperse systems with the same chemical composition at sufficiently low  concentrations.  In  addition,  the  actual  functional form  of  the  DCD  in  PFG-NMR  experiments  is  generally  unknown,  and  different  distribution  functions  are explored to describe the signal decay. Early in the 1960s, a  single  exponential  model  was  derived  by  Stejskal  and Tanner [20] to  model  the  signal  decay  for  a  monodisperse solution with a single self-diffusion coefficient. Later on, Raghavan et al. [21]  studied the self-diffusion of polymers with  the  Schulz  distribution  model,  which  gave  reasonably consistent results with those obtained by the single exponential model. For the polymer systems with higher polydispersity,  however,  a  nonexponential  signal  decay is observed. In this case, the stretched exponential model is  often  applied  to  fit  the  nonexponential  signal  attenuation curves. [16,17] As  pointed out by Röding et al., [22] the relation  between  the  stretch  parameter  and  the  spread of the DCD is complicated, and the stretched exponential model does not correspond to the actual DCD. Apart from the  aforementioned  models  and  the  numerical  inverse Laplace  transform  (ILT) [14,23]   used  in  DOSY  studies  of polydisperse  samples,  log  normal  distribution  has  often been chosen as an alternative to model the experimental signal  decay. [10,15,19] Besides,  gamma  distribution [19,22] or gamma convolution models which are convolutions of n ( n ≥ 1) gamma distributions [24]  have recently been derived and applied for data processing in the PFG-NMR studies, providing  results  similar  to  those  obtained  with  the  log normal model and ILT, respectively. It is worth noting that ILT is often used to extract the DCD from the NMR signal decay but this approach is known for strong vulnerability to  noise  and  numerical  instability  due  to  its  ill-posed nature.  In  addition,  numerous  iterative  regularization methods  have  been  intensively  studied  for  determining the DCD, e.g., iterative thresholding algorithm for multiexponential decay [25]  and tailored norm regularization for monitoring polydispersity by NMR diffusometry. [26]

To the best of our knowledge, these previous PFG-NMR studies  have  mainly  focused  on  the  discussion  on  the effects  of  average  molecular  weight or polydispersity on the experimental results and the scaling theories, but the MWD was  estimated  from  DCD  only  at  low  concentration.  In  this  work,  first  we  investigate  and  compare  the different  models  for  determination  of  DCD  from  PFGNMR  data,  and  second  retrieve  MWD  from  DCD  under consideration  of  the  concentration  dependence  of  diffusion to  extend  the  measurement limits. The approach results  in  a  correlation  between  DCD  and  MWD of polymers in solution and therefore the measurement of MWD by  PFG-NMR.  Two  polymers,  namely  polystyrene  (PS) and  poly(methyl  methacrylate)  (PMMA)  are  used  as  test samples  dissolved  in  deuterated  chloroform  at  different concentrations  in  the  range  of  0.16-8  wt%.  Three  data treatment  models  (gamma  distribution,  log  normal  distribution, and tailored norm regularization) are explored. MWDs  retrieved  from  PFG-NMR  experiments  are  compared with those measured by SEC.

## 2. Experimental Section

## 2.1. Materials and Sample Preparation

PS and PMMA (Table 1) have been used for PFG-NMR experiments. PS samples (PS1K, PS2K, PS28K and PS125K) were obtained  from  PSS  (Polymer  Standards  Service,  Mainz, Germany), and PS263K was synthesized in house and was kindly provided by Tobias Fischer in Prof. C. Barner-Kowollik's laboratory at KIT. PMMA samples were synthesized by free radical polymerization of MMA, which was carried out in solution at 80 ° C in a Taylor-Couette reactor. Xylene

<!-- image -->

Table 1. Properties of the polymers used for PFG-NMR.

| Sample   |   Weight-averaged molecular weight M w [kg mol - 1 ] |   Number-averaged molecular weight M n [kg mol - 1 ] |   Peak molecular weight M p [kg mol - 1 ] |   Polydispersity index Ð M [-] |
|----------|------------------------------------------------------|------------------------------------------------------|-------------------------------------------|--------------------------------|
| PS1K     |                                                 0.71 |                                                 0.64 |                                      0.68 |                           1.10 |
| PS2K     |                                                 1.92 |                                                 1.77 |                                      1.82 |                           1.08 |
| PS28K    |                                                27.50 |                                                26.60 |                                     28.00 |                           1.03 |
| PS125K   |                                               125.00 |                                               120.00 |                                    130.00 |                           1.04 |
| PS263K   |                                               263.02 |                                               162.48 |                                    240.04 |                           1.62 |
| PMMA7K   |                                                 7.59 |                                                 4.36 |                                      7.99 |                           1.74 |
| PMMA12K  |                                                12.09 |                                                 6.61 |                                     11.97 |                           1.83 |
| PMMA29K  |                                                28.99 |                                                15.80 |                                     30.58 |                           1.83 |
| PMMA38K  |                                                38.42 |                                                21.22 |                                     37.46 |                           1.81 |
| PMMA42K  |                                                42.45 |                                                23.35 |                                     49.56 |                           1.82 |
| PMMA52K  |                                                52.15 |                                                28.82 |                                     64.01 |                           1.81 |
| PMMA57K  |                                                56.50 |                                                34.00 |                                     67.41 |                           1.66 |
| PMMA74K  |                                                73.90 |                                                40.44 |                                     80.88 |                           1.83 |

(mixture of isomers) was used as solvent and 2,2-azoisobutyronitrile  as  initiator.  The  initiator  concentration  was varied  from  0.2  to  2  wt%  to  get  samples  with  different molecular  weight  distributions.  The  residual  monomer and  the  solvent  of  the  reaction  mixture  were  eliminated by vacuum evaporation ( &lt; 25 mbar, 150 ° C). Corresponding weight-  and  number-averaged  molecular  weights  ( M w, M n)  and PDI were determined by the SEC instrument (PLSEC  50)  using  tetrahydrofuran  as  eluent.  These  polymer samples  were  dissolved  in  deuterated  chloroform  (CDCl3, 99.5%  D,  EURISO-TOP,  France)  at  different  concentrations in  the  range  of  0.16-8  wt%.  The  polymer  solutions  were filled  into  standard  5  mm  NMR  tubes  (Deutero  GmbH, Kastellaun,  Germany).  To  avoid  solvent  evaporation  and thus  concentration  changes,  the  filled  glass  tubes  were flame-sealed.

## 2.2. PFG-NMR Measurements

The  1 H PFG-NMR experiments were performed at 25 ° C on a  Bruker  Avance  200  MHz  (Bruker,  Germany)  NMR  spectrometer  equipped  with  a  Diff30  diffusion  probe,  which provides a maximum gradient strength g up  to  12  T  m -1 . The  spectra  were  obtained  by  using  a  PFG-STE  sequence with 32 linearly spaced gradient steps and 8-16 scans. The PFG-STE  parameters  for  diffusion  experiments  are:  gradient pulse duration δ = 2 ms, diffusion time ∆ = 40 ms, and repetition time 5 s. The data were acquired within Topspin 1.5 (Bruker, Germany) and processed via phase correction and integration of the corresponding characteristic peaks in the spectra. Further data processing of the signal decay was done with Matlab routines.

<!-- image -->

## 3. Results and Discussion

Figure 1a exemplarily shows the acquired 1 H-PFGSTE  spectra  for  the  sample  PMMA29K.  The  peak  at δ c = 3.59  ppm  is  attributed  to  the  methyl  ester  group  (peak  a in  Figure  1a).  The  peaks  related  to  the  methyl  group  and the  CH2  group  in  PMMA  are  visible  at  smaller  chemical  shifts  (peak  b  and  peak  c  in  Figure  1a),  and  the  peak of chloroform is also identified at 7.26 ppm in the spectra. The signal intensity S changes with the gradient g .  Analysis  of  the  characteristic  peak  a  in  the  spectra  leads  to  a signal decay curve (Figure 1b). For a monodisperse diluted polymer solution with a single self-diffusion coefficient D , the detected signal decay can be expressed by an exponential function [20]

$$\frac { S ( q ) } { S _ { o } } = \exp \left [ - D q ^ { 2 } ( \Delta - \delta / 3 ) \right ] \\$$

where S 0  is the signal intensity at q = 0, and ∆ is the diffusion time. The parameter q is  defined  as  the  product γ g δ , where γ is the proton magnetogyric ratio, g is the gradient amplitude, and δ is the gradient pulse duration.

For  a  polydisperse  solution,  the  detected  signal  intensity  of  a  peak  in  the  spectrum  is  the  integral  over  the NMR-signals of all polymer molecules. Under the assumption that the studied polymers have a certain probability distribution P ( D ) of molecular weight and conformations, Equation (1) can be rewritten as

$$\frac { S ( q ) } { S _ { \circ } } = \bigtriangledown _ { \circ } P ( D ) \exp \left [ - D q ^ { 2 } ( \Delta - \delta / 3 ) \right ] \text {d} D & & ( 2 )$$

2016WILEY-VC2He

2016WILEY-VC2He

(a)

60

50

40

30

20

10

CHCl3

2

g [T/m]

4

[a.u.]

S

8

a

6

δ

b

C

H3C

a

H3C-O-C=O

fC-CH2tn

C

b

4

2

0

[wdd]

C

Figure  1. a) 1 H-PFG-STE-NMR  spectra  for  the  sample  PMMA29K ( c = 3.85  wt%),  b)  signal  attenuation  modeled  with  a  monoexponential function (dot-dashed line), the gamma distribution model (solid line), and the log normal distribution (dashed line). The inset shows the respective diffusion coefficient distributions extracted with gamma and log normal models, having a mean value of ≈ 7.1 × 10 -11 m 2 s -1 . The monoexponential model results in a mean diffusion coefficient of 6.4 × 10 -11 m 2 s -1 .

<!-- image -->

In  this  work,  the  DCDs  of  the  polymers  are  obtained by  modeling  the  acquired  PFG-NMR  signal  decay  with log  normal  distribution P LN( D )  and  gamma  distribution P G( D ) [10,15,19,22]

$$P _ { \ln } \left ( D \right ) = & \frac { 1 } { \sqrt { 2 \pi } D \sigma _ { \ln } } \exp \left [ - \frac { \left ( \ln D - \ln D _ { o } \right ) ^ { 2 } } { 2 \sigma _ { \ln } ^ { 2 } } \right ] & & \sigma _ { G } \text { sh} . & & \text {tr} \text {atio} & & \text {tr} \text {atio}$$

with the mean value D D exp( /2) mean 0 LN 2 σ = , where D 0 is the median value and σ LN is a measure of the width of the DCD

$$P _ { G } \left ( D \right ) = \frac { D ^ { \kappa - 1 } \exp ( - D / \theta ) } { \Gamma ( \kappa ) \theta ^ { \kappa } } & & \quad ( 4 ) & & \quad \top \\$$

with the mean value D mean = θκ and the width of the distribution G σ θ κ = ,  where θ is  a  scale  parameter, κ is  a shape parameter, and Γ is the gamma function.

The  distribution  parameters  of  Equations  (3)  and  (4) can be determined by a nonlinear least-squares fitting of Equations (2), (3) and (4) to the observed decays.

The normalized signal attenuation, S / S 0,  was  modeled with monoexponential function, gamma model, and log normal  distribution  (Figure  1b).  The  monoexponential line describes the data down to approximately S / S 0 = 10%. Below this value, the experimental data deviate from the monoexponential function due to polydispersity. A characteristic of polydisperse solutions is the curvature of S / S 0 observed at larger values for q 2 . Both the gamma and the log normal models describe the experimental data quite well.  The  difference  between the two fit curves is negligibly small on the semilogarithmic scale (Figure 1b) and close  to  the  noise  level  of  the  measurement.  The  corresponding  DCDs  obtained  with  these  two  models  are rather  similar,  too  (Figure  1b).  A  comparison  among  the experimental  results  for  polymers  at  different  molecular  weights  indicated  that  there  is  a  more  pronounced attenuation of the signal intensity for the fast diffusing small species, which is reflected by a steeper slope in the semilogarithmic  plot.  Moreover,  with  increasing  molecular  weight,  the  slope  decreases  and  is  indicative  for smaller diffusion coefficient. Notably, the signal decay is detected over a wide range of intensity (typically two to three orders of magnitudes) in the  1 H PFG-NMR diffusion experiments.

Figure 2 illustrates the apparent concentration dependence  of the DCD  for  the  sample  PMMA29K. With  increasing  polymer  concentration,  the  retrieved DCD  curve  is  shifted  to  smaller  diffusion  coefficients (Figure  2a).  The  characteristic  quantities,  namely  the mean  diffusion coefficient D mean, the width of the gamma distribution σ G,  and  the  coefficient  of  variation (CV = σ G/ D mean),  are  plotted  in  Figure  2b  for  the  sample PMMA29K  at  different concentrations ranging from 0.33 to 7.11 wt%, respectively. It is obvious that the mean diffusion  coefficient D mean  does  not  change  significantly at  low  concentrations  (e.g., c &lt; 2  wt%).  Increasing  the polymer concentration leads to a strong reduction of the mean diffusion coefficient. The width of the distribution σ G  shows a similar tendency when the polymer concentration increases. Moreover, the coefficient of variation CV remains  nearly  constant,  which  indicates  a  good  model fit  at  different  polymer  concentrations.  This  behavior  is, however, of rather unphysical nature but reflects only the limits of the data treatment approaches usually applied. For larger and practically more relevant polymer concentrations, an extension of these approaches is needed.

To further study the influence of macromolecular concentration  on  the  polymer  mobility  in  the  given  CDCl 3 solutions, diffusion coefficient distributions for different PMMA and PS samples at different concentrations  were measured (Figure 3, symbols: D mean and 'error bars': σ G).

<!-- image -->

Figure 2. a) NMR determined diffusion coefficient distributions, b)  mean  diffusion  coefficient D mean,  width  of  the  distribution σ G  and coefficient of variation (CV = σ G / D mean) for  the sample PMMA29K at different concentrations ( c = 0.33  wt%,  0.68 wt%, 1.94 wt%, 3.85 wt%, 5.39 wt%, and 7.11 wt%) obtained from a fit to the data with the gamma model.

<!-- image -->

The  PMMA  samples  with  different  molecular  weights M w ranging from 7.6 to 74 kg mol -1 exhibit  very  similar curves,  showing  the  same  tendency  of  the  concentration dependence in the measured range. Except for a few outliers  a  similar  behavior  has  been  observed  for  the  PS samples with M w of 0.7 to 263 kg mol -1 at  different concentrations  (Figure  3b).  The  outliers  are  probably  due  to the  experimental  error  and  because  the  PS  sample  with a very low molecular weight consists of a few monomer units.  In  the  current  experimental  concentration  range, the diffusion coefficients of these oligomers do not show as  strong  a  concentration  dependence  as  those  of  the others.  Besides,  the  chosen  concentrations  left  a  gap  at low  concentrations  for  PS2K  not  present  in  the  others. As compared to the previous study on diffusion of PS in CDCl3, [27]   in  which  the  mono-/biexponential  model  only gave  apparent  diffusion  coefficients,  now  both  gamma and log normal models describe the data better and provide  more  information  about  the  polymer  diffusion  in solution.  Furthermore,  these  parameters,  i.e.,  the  mean

<!-- image -->

2016WILEY-VC2He

Figure 3. Diffusion coefficient distributions at different concentrations (Symbols: D mean, 'error bars': width of the distributions), a) PMMA samples with molecular weights M w ranging from 7.6 to 74 kg mol -1 , b) PS samples with M w of 0.7 to 263 kg mol -1 .

<!-- image -->

diffusion coefficient D mean,  the  width  of  the  distribution σ G, and the coefficient of variation (CV) can be related to the polydispersity. As derived by Röding et al., [22]  the PDI ĐM for the gamma model is given by

$$\mathcal { D } _ { M } = \left ( 1 + \frac { \sigma _ { G } ^ { 2 } } { D _ { m e a n } ^ { 2 } } \right ) ^ { \frac { 1 } { \alpha ^ { 2 } } } = \left ( 1 + C V ^ { 2 } \right ) ^ { \frac { 1 } { \alpha ^ { 2 } } }$$

where α is  an  empirical  scaling  parameter,  depending on the type and quality of the solvent and the monomer. With the given PDI values from SEC and the distribution parameters for the studied polymer samples in CDCl3, the parameter α in  Equation  (5)  was  estimated  to  be  0.51 ± 0.05. The scaling parameter and the extension of the conventional  scaling  law  to  a  wide  concentration  range  for extracting MWD from DCD will be discussed below.

A  further  comparison  between  the  DCDs  for  PMMA and  PS  samples  obtained  using  the  gamma  model  and the  log  normal  model  is  illustrated  in  Figure  4,  where the solid line with a slope of one reflects the perfect correlation between two methods. It is obvious that almost all  the  data  points  of  the  mean  diffusion  coefficient D

2016WILEY-VC2He

Figure 4. Comparison of DCDs obtained from the gamma model and the log normal model, a) diffusion coefficients D mean, in comparison  with D achieved  with  the  monoexponential  function, b) squared 2-norm of the residuals r Norm, c) coefficient of variation CV.

<!-- image -->

(circular dots in Figure 4a) lie on the solid line, implying that the results obtained with both models correlate well. The diffusion coefficients D monoexp  achieved with a fit of a monoexponential function are also plotted for comparison.  They  are  systematically  underestimated,  resulting in an approximate estimation in contrast to those obtained with gamma and log normal models. This can be attributed to the distribution of diffusion coefficients being obvious in deviation of the measured signal decay from the straight line (Figure 1b). The squared 2-norm of the residuals r Norm and the coefficients of variation CV are also close to the solid line (Figure 4b,c), reflecting the similarity and goodness of fit. The values of CV for the gamma model are  somewhat smaller  than  those  for  log  normal model (Figure  4c).  This  suggests  that  the  gamma  model has somewhat smaller residuals relative to the predicted values, and thus provides a better fit to the experimental data for PMMA and PS samples in CDCl3 solutions in the measured polymer concentration range up to ≈ 8  wt%.  A similar  behavior  has  also  been  observed  in  the  previous study on other polymer solutions, e.g., polyethylene glycol in D2O [22]  and PS in CDCl3 solutions [19]  at very low polymer concentrations ( c ≤ 0.1 wt%). Notably, although in the present work the PFG-NMR experiments were carried out at the  concentration  up  to  8  wt%,  the  concentration  range can be further extended upward for determining DCD.

The above discussion shows that DCDs of the polymer solutions can be determined by modeling and analyzing the  PFG-NMR  signals.  The  experimental  signal  attenuation  depends  on  the  diffusion  of  the  polymer  molecular species present in the solution, which is directly related to the molecular size and polydispersity. Thus, the PFG-NMR measurement  provides  the  possibility  to  retrieve  the MWD from the experimental DCD. For this purpose, the well-known empirical scaling law has often been used to establish the relation between molecular weight M w and mean self-diffusion coefficient D for dilute solutions, typically expressed as [8]

$$D = K \cdot M _ { w } ^ { - \alpha }$$

where K and α are scaling parameters depending on the type of the studied polymer system. This power law only holds true for sufficiently low polymer concentrations.

Figure 5 shows the experimental scaling between diffusion coefficient D and molecular weight M w for PS and PMMA  samples  in  CDCl3  dilute  solutions  ( c ≈ 0.3  wt%) measured  with  PFG-NMR.  The  solid  line  represents  a nonlinear least-squares fit of the experimental data. The scaling D M 2.19 10 8 w 0.52 = × --was  found.  The  value  of  the scaling  parameter  ( α = 0.52)  agrees  fairly  well  with  the values in the range of α = 0.47-0.61 for PS and PMMA in CDCl3 [28,29] as  well  as  in  previous  NMR  diffusion  studies of  other  polymer  solutions  such  as α = 0.52-0.55  for poly(ethylene oxide) (PEO) in D2O, [15] α = 0.55  for  PEO  in water, [30] α = 0.46-0.54  for  PMMA  in  acetone. [28] It  must be  noted  that  the  mapping  of  MWD  onto  DCD  lacks  a firm theoretical background and thus needs to be treated carefully.  For  dilute  polymer  systems,  this  scaling  relation can give accurate prediction of the MWD of polymers with known molecular weights. [15,28]

<!-- image -->

Figure  5. Scaling  between  mean  diffusion  coefficient D and molecular weight M w for PS samples ( ⊕ ) and PMMA samples ( ○ ) in CDCl3 dilute solutions ( c ≈ 0.3 wt%) measured with PFG-NMR.

<!-- image -->

Using this scaling relationship between diffusion coefficient D and molecular weight M w, the diffusion coefficient distribution P ( D ) can be transformed into the weight-averaged molecular weight distribution P M( M ) or the numberaveraged molecular weight distribution P N( M )

$$P _ { M } ( M ) = P _ { N } ( M ) M$$

$$P _ { M } ( M ) = P ( D ) d D / d M$$

With Equations (6) and (8), the molecular weight distribution function P M( M ) M can be determined as

$$P _ { M } ( M ) M = \alpha D P ( D ) = \alpha K M ^ { - \alpha } P ( D )$$

ĐM is defined as the ratio of the medians of the weightaveraged molecular weight M w to  the number-averaged molecular weight M n

$$\mathcal { D } _ { M } = & \frac { \bar { M } _ { w } } { \bar { M } _ { n } } = \frac { \int P _ { M } \left ( M \right ) M d M / \int P _ { M } ( M ) d M } { \int P _ { N } ( M ) M d M / \int P _ { N } ( M ) d M }$$

The  diffusion  coefficient  distribution P ( D )  used  for retrieving the molecular weight distribution can be either a specific distribution function in closed form (e.g., Schulz distribution,  gamma  distribution,  log  normal  distribution) or a general distribution function without analytical form (e.g., a DCD function obtained from the signal decay with numerical algorithms as ILT).

The molecular weight distributions for PMMA29K and PS263K  in  CDCl3  dilute  solutions  ( c ≈ 0.3  wt%)  retrieved from PFG-NMR DCDs show very small differences between  different  methods  in  Figure  6  (PMMA29K:  ĐM 1.91  for  the  gamma  model,  and  1.87  for  the  log  normal model; PS263K: ĐM 1.65 for the gamma model, and 1.66

<!-- image -->

2016WILEY-VC2He

Figure  6. Molecular  weight  distributions  for  PMMA29K  and PS263K in CDCl3 dilute solutions ( c ≈ 0.3 wt%) retrieved from the DCDs determined with  the gamma model and the log normal model, and compared with SEC results.

<!-- image -->

for  the  log  normal  model).  Furthermore,  these  MWDs agree  well  with  those  by  SEC  (PMMA29K:  ĐM  1.83; PS263K: ĐM 1.62) (Figure 7). The parameters of MWDs for

Figure 7. Comparison  between M w and  PDI retrieved  from NMR  diffusion  measurements  on  PMMA  and  PS  samples  in CDCl3 dilute solutions ( c ≈ 0.3 wt%) and those obtained by SEC, a) weight-average molecular weight M w, b) PDI Đ M, two dashed lines indicate a range with a PDI variation of ± 10%.

<!-- image -->

<!-- image -->

2016WILEY-VC2He

Figure 8. Comparison between diffusion coefficients by tailored norm regularization and those by gamma and log normal models.

<!-- image -->

the other samples measured by PFG-NMR and SEC are also illustrated in Figure 7. It is obvious that in the measured range of M w = 0.71-263  kg  mol -1   the  molecular  weights M w  determined  by  PFG-NMR  are  well  correlated  with the  SEC  results,  although  the  results  using  the  gamma model show a slight overestimation as compared to those using the log normal model in Figure 7a. In addition, the PDI values determined from PFG-NMR also show a good agreement with those by SEC. Most of the measurement data lie in the range with a PDI variation of ≈± 10% except for only a few points probably due to measurement errors or deviations of the real distribution shape from the used models.  The  overall  agreement  between  the  results  by PFG-NMR and SEC is quite satisfactory.

Besides  the  gamma  and  log  normal  models  for  processing the signal decay data, a new iterative regularization  method  called  tailored  norm  regularization [26]   has also been explored for determining the DCD and thus the MWD. It is based on the use of ℓ p   -norm (1 ≤ p ≤ 2)  as  a regularization  for  ILT.  Compared  to  the  above-discussed gamma  and  log  normal  models,  however,  the  tailored norm method results  in  an  overestimation  of  the  mean diffusion  coefficients  for  the  studied  samples  (Figure  8). This  could  be  due  to  the  iterative  method  itself  and  the imperfect presetting of some parameters in the available iteration  program apart from the inherent sensitivity to noise and numerical instabilities which are well known for ILT. The retrieved DCD is broader, leading to a broader MWD than those  by  gamma  and  log  normal  models  as well  as  by  SEC.  As  an  example,  MWDs  retrieved  with tailored  norm  regularization  method,  gamma,  and  log normal models for the sample PMMA29K in CDCl3 dilute solution ( c ≈ 0.3  wt%) as well as by SEC are compared in Figure 9. In conclusion, both the gamma and log normal models  utilized  for  the  data  treatment  in  PFG-NMR on  polymers  in  solution  are  capable  of  describing  the experimental data quite well and result in a good prediction of DCDs and thus MWDs of polymer solutions.

Figure  9. MWDs  retrieved  with  tailored  norm  regularization method, gamma, and log normal models for PMMA29K in CDCl3 ( c ≈ 0.3 wt%) as well as by SEC.

<!-- image -->

As  already  stated  (Figures  2  and  3),  the  apparent  diffusion  coefficient  depends  on  the  concentration  of  the polymer  solution.  The  mean  diffusion  coefficient  varies slightly  or  remains  almost  constant  at  low  concentrations. The diffusion coefficient decreases with increasing the  concentration  because  of  the  interaction  of  polymer molecules  in  the  solution.  Masaro  and  Zhu [31]   reviewed different  physical  models  of  diffusion  in  polymer  solutions,  gels,  and  solids  as  well  as  their  limitations.  The underlying physical concepts are obstruction effects, hydrodynamic interactions, and free volume theory, but  their  applicability  varies  widely.  Considering  these different concepts and the experimental observations in this work, it is found that an exponential equation can be employed for good description of the diffusion variation with the concentration in present PFG-NMR experiments. Thus,  the  concentration  dependent  diffusion  coefficient in  terms  of  the  stretched  exponential  equation [32,33] can be simplified to Equation (11)

$$D = D _ { o } \exp \left ( - k c ^ { \nu } \right ) \stackrel { f o r v = 1 } { \Rightarrow } D = D _ { o } \exp ( - k c )$$

where D 0 is  the  diffusion  coefficient  at  very  low  concentrations, c is  the  concentration  of  the  polymer  solution, ν is  the  stretch  parameter  depending  on  the  type of polymer solutions, and k is  a  proportionality constant obtained by a nonlinear least-squares fit on the diffusion data. This model has a simple form and shows a good correlation with the experimental data (Figure 10a). Gao and Fagerness [34]   have employed this model to study the diffusion  in  hydroxypropylmethyl  cellulose  gels  and  determine the drug and water diffusivity by NMR.

To our knowledge, MWD is estimated from DCD based on the scaling law only at very low concentration so far. To  circumvent  this  limitation  and  to  further  extend  the measuring  range,  a  new  facile  method  is  introduced for  retrieving  MWD  from  DCD  for  a  broader  concentration  range.  As  discussed,  at  very  low  concentration  the scaling law in Equation (6) applies the form of D 0 = K ⋅ M -α . Thus, Equation (11) can be rewritten as D K kc M exp ( ) = --α

<!-- image -->

Figure 10. a) D mean, gamma of PMMA29K and PS263K as a function of  concentration  (cf.  Figures  2  and  3),  the  fit  with  Equation  (11) leads to k = 10.9 [-] and 16.9 [-] for PMMA29K and PS263K, respectively,  b)  molecular  weight  distributions  retrieved  from  DCDs determined from the PFG-NMR measurements on PMMA29K at different concentrations with and without applying the correction by Equation (11), c) corresponding results for PS263K at different concentrations.

<!-- image -->

<!-- image -->

(12)

2016WILEY-VC2He

MWD P M( M ) M can  be  correlated  with  the  diffusion coefficient distribution P ( D ) determined from PFG-NMR at different concentrations

$$P _ { M } ( M ) M = \alpha K e x p ( - k c ) M ^ { - \alpha } P ( D )$$

Figure 10 exemplarily depicts the diffusion coefficients of  PMMA29K  and  PS263K  as  a  function  of  concentration and the MWDs retrieved with the method proposed above.  The  experimental  diffusion  coefficients  at  the measured  concentrations  can  be  well  described  with Equation  (11)  (Figure  10a).  The  trend  of  diffusion  with increasing polymer  concentration is similar. Besides, DCDs  determined  from  PFG-NMR  diffusion  measurements at  high  concentration  have  been  used  to  retrieve MWDs.  Without  concentration  correction,  the  resulting MWDs  at  high  concentration  deviate  significantly  from that  at  low  concentration  (cf.  dashed  line  and  solid  line in  Figure  10b,c).  Considering  the  concentration  effect, the MWDs agree perfectly well with that at low concentration (cf. dot-dashed line and solid line in Figure 10b,c). Similar  results  have  been  obtained  for  the  other  molecular weight samples at high concentrations. In summary, PFG-NMR is very suitable for simultaneous quantification of DCDs and MWDs of polymers. The measurements can also be extended to high concentration, greatly improving the  signal-to-noise  ratio  which  improves  accuracy  and applicability of PFG-NMR. Finally, it should be pointed out that,  apart  from  the  studied  polymer  solutions  (PS  and PMMA dissolved in CDCl3), the proposed method in terms of Equations (11) and (13) for determination of MWDs at different  concentrations  can  be  generalized  for  further application to other polymer solutions as follows

$$P _ { M } ( M ) M = \alpha K e x p \left ( - k c ^ { \nu } \right ) M ^ { - \alpha } P ( D )$$

The stretch parameter ν can be determined experimentally,  depending on the type of polymer solutions under study.

## 4. Conclusions

Self-diffusion of two polymers in solution (PMMA and PS in CDCl3) has been investigated at different concentrations in  the  range  of  0.16-8  wt%  by  means  of  the  PFG-NMR. DCDs have been determined by modeling the signal decay with  different  approaches,  namely  the  gamma  model, the  log  normal  model  and  the  numerical  tailored  norm regularization.  Experimental  results  indicate  that  both the gamma and log normal models describe the diffusion data  very  well,  giving  DCDs  comparable  to  SEC,  whereas the tailored norm method results in broader DCDs. Based on the scaling between diffusion coefficient and molecular weight, MWDs of the studied polymers have been retrieved

2016WILEY-VC2He

from  DCDs.  Furthermore,  the  known  dependence  of  the diffusion  coefficient  on  concentration  above  a  certain value  leads  to  an  overestimation  of  the  MWD  when  the conventional scaling law is employed. To release this limitation,  an  exponential function of polymer concentration is introduced into the conventional scaling law for consideration of the influence of concentration on self-diffusion. The MWDs derived with the proposed method agree perfectly  well  with  those  measured  at  low  concentrations, resulting  in  a  very  satisfactory  calculation  of  MWDs  of polymers.  The  retrieved  MWDs  agree  well  with  those  by SEC. As a result, PFG-NMR is a very good analytical tool for simultaneous quantification of  DCDs  and  MWDs of polymers and chemical identification of polymers by spectral analysis. The measurements can now also be extended to higher  and  realistic  concentrations  inherently  improving the  signal-to-noise  ratio,  i.e.,  the  accuracy  and  therefore the applicability of the PFG-NMR in the study of polymer solutions.

Acknowledgements:  The  authors  gratefully  acknowledge  the financial  support  from  the  German  Research  Foundation  (DFG SFB  1176  Project  Q2  as  well  as  Pro²NMR  instrumental  facility at  KIT  and  RWTH  Aachen).  B.L.  acknowledges  support  by  the HGF  program  BIFTM.  The  authors  also  thank  Tobias  Fischer  in Prof. C. Barner-Kowollik's laboratory at KIT for kindly providing the sample PS263K.

Received: September 12, 2016; Revised: October 18, 2016; Published online: November 18, 2016; DOI: 10.1002/macp.201600440

Keywords: diffusion; diffusion coefficient distribution; molecular weight  distribution;  polymer  solutions;  pulsed  field-gradient NMR

- [1]  R. Kimmich, NMR-Tomography Diffusometry Relaxometry , Springer Verlag, Berlin 1997 .
- [2]  D.  Campbell, R. A. Pethrick, J. R. White, Polymer Characterization: Physical Techniques ,  2nd ed., Stanley Thornes, Cheltenham, UK 2000 .
- [3]  M.  Rogosic,  H.  J.  Mencer,  Z.  Gomzi, Eur.  Polym.  J. 1996 , 32 , 1337.
- [4]  F.  A.  Bovey,  P.  A.  Mirau, NMR of Polymers ,  Academic  Press, San Diego 1996 .
- [5]  R. Kimmich,  N.  Fatkullin, in Advances  in  Polymer  Science (Eds:  A.  Abe,  A.-C.  Albertsson,  K.  Dusek,  W.  H.  de  Jeu, S.  Kobayashi,  K.-S.  Lee,  L.  Leibler,  T.  E.  Long,  I.  Manners,
- M.  Möller,  E.  M.  Terentjev,  B.  Voit,  G.  Wegner,  U.  Wiesner, M.  J.  Vicent,  J.  Genzer),  Springer  Verlag,  Berlin  Heidelberg 2004 , p. 1.
- [6]  C.  S.  Johnson, Prog.  Nucl.  Magn.  Reson.  Spectrosc. 1999 , 34 , 203.
- [7]  Y. Cohen, L. Avram, L. Frish, Angew. Chem. Int. Ed. 2005 , 44 , 520.
- [8]  P.  G.  Gennes, Scaling  Concepts  in  Polymer  Physics ,  Cornell Universty Press, Ithaca 1979 .
- [9]  P.  T.  Callaghan,  D.  N.  Pinder, Macromolecules 1981 , 14 , 1334.
- [10]  P. T. Callaghan, D. N. Pinder, Macromolecules 1985 , 18 , 373.
- [11]  G. Fleischer, Polymer 1985 , 26 , 1677.
- [12]  H.  Walderhaug,  F.  K.  Hansen,  S.  Abrahmsen,  K.  Persson, P. Stilbs, J. Phys. Chem. 1993 , 97 , 8336.
- [13]  H. Walderhaug, O. Soderman, D. Topgaard, Prog. Nucl. Magn. Reson. Spectrosc. 2010 , 56 , 406.
- [14]  A. Chen, D. H. Wu, C. S. Johnson, J. Am. Chem. Soc. 1995 , 117 , 7965.
- [15]  B.  Hakansson,  M.  Nyden,  O.  Söderman, Colloid  Polym.  Sci. 2000 , 278 , 399.
- [16]  X.  L.  Gong,  E.  W.  Hansen,  Q.  Chen, Macromol.  Chem.  Phys. 2011 , 212 , 1007.
- [17]  X.  L.  Gong,  E.  W.  Hansen,  Q.  Chen, Macromol.  Chem.  Phys. 2012 , 213 , 278.
- [18]  N.  E.  Kuz'mina,  S.  V.  Moiseev,  V.  I.  Krylov,  V.  A.  Yashkir, V. A. Merkulov, J. Anal. Chem. 2014 , 69 , 953.
- [19]  N.  H.  Williamson,  M.  Nyden,  M.  Röding, J.  Magn.  Reson. 2016 , 267 , 54.
- [20]  E. O. Stejskal, J. E. Tanner, J. Chem. Phys. 1965 , 42 , 288.
- [21]  R.  Raghavan,  T.  L.  Maver,  F.  D.  Blum, Macromolecules 1987 , 20 , 814.
- [22]  M.  Röding,  D.  Bernin,  J.  Jonasson,  A.  Sarkka,  D.  Topgaard, M. Rudemo, M. Nyden, J. Magn. Reson. 2012 , 222 , 105.
- [23]  S. W. Provencher, Comput. Phys. Commun. 1982 , 27 , 229.
- [24]  M.  Röding,  N.  H.  Williamson,  M.  Nyden, J.  Magn.  Reson. 2015 , 261 , 6.
- [25]  M.  Urbanczyk,  D.  Bernin,  W.  Kozminski,  K.  Kazimierczuk, Anal. Chem. 2013 , 85 , 1828.
- [26]  M.  Urbanczyk,  D.  Bernin,  A.  Czuron,  K.  Kazimierczuk, Analyst 2016 , 141 , 1745.
- [27]  M. Cudaj, J. Cudaj, T. Hofe, L. Luy, M. Wilhelm, G. Guthausen, Macromol. Chem. Phys. 2012 , 213 , 1833.
- [28]  S. Auge, P. O. Schmit, C. A. Crutchfield, M. T. Islam, D. J. Harris, E.  Durand,  M.  Clemancey,  A.  A.  Quoineaud,  J.  M.  Lancelin, Y.  Prigent,  F.  Taulelle,  M.  A.  Delsuc, J.  Phys.  Chem.  B 2009 , 113 , 1914.
- [29]  G. Fleischer, O. E. Zgadzai, V. D. Skirda, A. I. Maklakov, Colloid Polym. Sci. 1988 , 266 , 201.
- [30]  K. Chari, B. Antalek, J. Minter, Phys. Rev. Lett. 1995 , 74 , 3624.
- [31]  L. Masaro, X. X. Zhu, Prog. Polym. Sci. 1999 , 24 , 731.
- [32]  G. D. J. Phillies, Macromolecules 1986 , 19 , 2367.
- [33]  G. D. J. Phillies, Macromolecules 1987 , 20 , 558.
- [34]  P. Gao, P. E. Fagerness, Pharm. Res. 1995 , 12 , 955.

<!-- image -->