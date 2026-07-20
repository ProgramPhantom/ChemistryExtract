## Accepted Manuscript

Systematic bias in NMR diffusion measurements on polydisperse systems

Xiaoyue Zhou, Kaipin Xu, Shanmin Zhang

PII:

S1090-7807(15)00005-1

DOI:

Reference:

YJMRE 5587

To appear in:

Journal of Magnetic Resonance

Received Date:

22 November 2014

Revised Date:

5 January 2015

<!-- image -->

Please cite this article as: X. Zhou, K. Xu, S. Zhang, Systematic bias in NMR diffusion measurements on polydisperse systems, Journal of Magnetic Resonance (2015), doi:

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## Systematic bias in NMR diffusion measurements on polydisperse systems

Xiaoyue Zhou, Kaipin Xu, and Shanmin Zhang *

Physics Department and Shanghai Key Laboratory of Magnetic Resonance, East China Normal University, Shanghai, China.

## Abstract

Least-squares fitting of the Stejskal-Tanner equation is a routine process in the measurement of molecular diffusion coefficient (MDC) using Nuclear Magnetic Resonance (NMR) Spectroscopy.   It is simple and elegant.    However, a bias of the MDC is noticed when the system is polydispersed.   This is due to improper accounts of the diffusion coefficient distribution.   Eventually, it leads to a discrepancy between the observed MDC and the statistical mean value of the distribution.   To reveal the discrepancy, an analytical solution is derived when the diffusion data is taken a logarithmic linearization.   Computer simulation is also applied to obtain a non-linear regression result.   For a Gaussian distribution of the MDCs, the bias is proportional to the square of the distribution width (linear regression), but it is also inversely  proportional  to  the  statistical  mean  value  of  the  distribution  (non-linear  regression).   This indicates that the MDC derived from Stejskal-Tanner equation only holds well for narrow distribution of MDCs.   Otherwise, molecular radius derived from the Stokes-Einstein equation needs to be reconsidered due to the incorrect estimation of the MDC.

molecular diffusion coefficient, least-squares fitting, diffusion coefficient distribution,

Keywords: non-linear regression;

* Corresponding author. E-mail: shanminz@hotmail.com.

## Introduction

Molecular diffusion coefficient (MDC), according to the Stokes-Einstein equation, [1] correlates the random Brownian motion with the molecular size (radius). Tremendous applications have sprung out since the first NMR measurement of MDC by Stejskal and Tanner in 1965. [2] They include monitoring the process of protein denaturation, [3] protein and ligand banding, [4-6] chemical reaction, [7] medicine development, [8] etc.    MDC measurement is particularly useful in sorting out various molecules in compounds, such as polymers, [9,10] human body fluids (blood, urine, and cerebrospinal fluid), [11,12] wines, [13] liquid crystals, [14] etc.    Technically, considerable attentions have been paid to improve the NMR diffusion experiments for measuring slower MDCs, [15,16] increasing spectral resolution by multidimensional technique [9,10,17] and quantitative determination of MDCs. [18-21]

In practice, a set of diffusion data are collected as a function of the square of the pulsed field gradient (PFG), leading to a diffusion profile. [2] The  diffusion coefficient can be determined by least-squares fitting of the Stejskal-Tanner equation [2] to  diffusion data where only a single MDC value is assumed.    This is a good  approximation  for  small  molecules.    However,  much  more  attentions  are usually paid to larger and complicated molecules, such as polymers and bio-macromolecules.    Because  of  different  structures,  chain  lengths,  or  molecular weights,  the  diffusion  coefficients  of  these  molecules  are  always  not  the  same  but distributed  around  the  statistical  mean  value.    In  these  cases,  people  still  use  the same  fitting  strategy,  taking  for  granted  that  the  statistical  mean  value  of  the distribution could be derived.    Unfortunately, a systematic bias is introduced in this method which can be large if the distribution is broad.    This probably would lead to a wrong estimation of the molecular size, especially for polymers and bio-macromolecules.

In this paper, an analytical solution of the Stejskal-Tanner equation is derived to account for the discrepancy.    The result is then extended to a non-linear least-squares fitting.    The  MDC bias exists in both linear and non-linear fitting results, showing the phenomenon appearing disregarding the methods utilized.    Computer simulation based on a Gaussian model agrees well with the theoretical prediction.

## Theory

According to the Stokes-Einstein equation, if a molecule can be approximately considered in a sphere shape, the diffusion coefficient ( D ) of the molecule in solution can be expressed by

$$\widehat { V } ^ { \times } = D = \frac { k _ { B } T } { 6 \pi \eta r } \, ,$$

where k B is the Boltzmann constant, T is the temperature in Kelvin, η is the viscosity and r is  the  radius  of  the  molecule.    For  small  molecules  of  the  same  species  in ideally  homogeneous  solution,  the  MDCs  can  be  considered  of  basically  the  same. In this case, the Stejskal-Tanner equation well describes the signal decay in an NMR diffusion experiment

$$I _ { j } = A \exp ( - D \gamma ^ { 2 } \delta ^ { 2 } g _ { j } ^ { 2 } \Delta ^ { \prime } ) \, ,$$

where  the  subscript j ( j  = 1,  2,  ..., n )  represents  the  index  of  Pulse  Field  Gradient (PFG)  strengths used in the experiment, I j and A are the signal intensities corresponding  to  the  PFG  strength  ( gj )  and  in  the  absence  of  any  gradient  pulses, respectively. D is  the  diffusion  coefficient, γ is  the  gyromagnetic  ratio  of  the molecule being measured, δ is  the gradient duration and ∆ ' is  the effective diffusion delay.    The experimental parameters γ , δ , gj and ∆ ' are known while the intensity ( A ) and  the  diffusion  coefficient  ( D )  are  left  to  be  solved.    Conventionally,  a  set  of g values are used and least-squares regression methods, e.g. the Levenberg-Marquardt algorithm [22] , are implemented to determine A and D .

However,  as  mentioned  above,  for  complicated  molecules,  the  corresponding MDCs may not be the same.    It is more likely to have a distribution of the MDCs. Here we assume that the MDCs follow a Gaussian distribution for simplicity.    Thus, the distribution function can be written as

$$h ( D ) = \frac { A _ { 0 } } { c \sqrt { 2 \pi } } e x p ( - \frac { ( D - D _ { 0 } ) ^ { 2 } } { 2 \sigma ^ { 2 } } ) \, ,$$

wh the di ill di her e in stri ustr stri e h nteg ibut rate ibut ( D ) grat tion ed i tion ) re ted n. in F n, w epre int A FIG whic esen tens sch G. 1 ch i nts sity hem , w is ξ the an mat wher ξ = e di nd D tic re ξ = σ stri D 0 c rep ξ de 8 × ibut corr pres enot lo × tion resp sent tes og2 n fu pon tatio the . unct nds on e fu tion to t of ull w n of the a wid f D sta Ga dth , σ atist auss at h is t tica sian half the al m n  d f m sta mean distr maxi anda n v ribu imu ard alu utio um de ue (c on (FW evia cen of WH ation nter) MD HM) n, A ) of DC ) of A 0 i f th Cs  i f th is he is e

FI ξ i G. 1 s the 1. S e fu chem ull w mat width tic re h at epre half esen f ma ntatio axim on o mum of a m an nor d th rmal he cr l dis ross strib poi butio int o on o occu f M urs a MDC at D s, w = 0 wher 0. re D D 0 is the dist tribu utio n ce ente r,

<!-- image -->

Co ons equ uen ntly, , the e si igna al in nte nsit ty c can n be e de erive ed r refe erri ing to E Eqs s. (2 2) a and d (3) ),

$$I _ { j } = \int _ { 0 } ^ { \infty } h ( D ) \exp ( - D b _ { j } ) d D \approx \int _ { \cdot \infty } ^ { \infty } \frac { A _ { 0 } } { c \sqrt { 2 \pi } } e x p ( - \frac { ( D - D _ { 0 } ) ^ { 2 } } { 2 c ^ { 2 } } - D b _ { j } ) d D , \quad ( 4 a )$$

an nd th he i inte egra al r resu ult o of ( 4a) ) is

$$C \Big ( \begin{matrix} U _ { I _ { j } = A _ { 0 } \exp ( - \frac { \sigma ^ { 2 } b _ { j } ^ { 2 } } { 2 } - D _ { 0 } b _ { j } ) } , \end{matrix}$$

wh eq if her qual onl e b l m ly h bj  = ark h ( 0 ) = γ 2 k in ) is 2 δ 2 g Eq mu gj 2 ∆ q. (4 uch ∆ ' is 4a) sm s  th ind mall he p dica er t prep ates than pro s tha n h ( ces at t ( D0 ssed the 0 ). d ex inte xpe egr erim al r men regi ntal ion par fro ram om mete -∞ er. ∞ to T 0 c The can app be pro neg oxim gle mat cted te d Eq. (4b), compared to the original Stejskal-Tanner equation, suggests a systematic bias between the observed diffusion coefficient (from the Stejskal-Tanner equation) and the statistical mean value of the MDCs.    It is not a calculation error but a systematic deviation due to a multi-distribution of the MDCs.

To determine the character of this bias, analytical solution is deduced under the performing of logarithmic linearization on both sides of Eqs. (4b) and (2),

$$\log I _ { j } = \log A _ { 0 } + \left ( \frac { \sigma ^ { 2 } b _ { j } ^ { 2 } } { 2 } - D _ { 0 } b _ { j } \right ) = \log A - D _ { a p r } b _ { j } \\ , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \quad , \$$

$$\left ( \frac { \sigma ^ { 2 } b _ { j } ^ { 2 } } { 2 } - D _ { 0 } b _ { j } \right ) = \left ( \log A - \log A _ { 0 } \right ) - D _ { a p p } b _ { j } \sum \nolimits _ { \substack { \ D \nwarrow \ D \\ \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \ D \colon \$$

Here we use the name 'the apparent diffusion coefficient Dapp ' to denote the diffusion coefficient obtained from  the Stejskal-Tanner equation. For all experimental parameters and data ( h(0)≪h(D 0 ) ), the above equation leads to

$$\frac { 1 } { 1 - b _ { 1 } } \log A - \log A _ { 0 } \right ] = \frac { \sqrt { 2 } } { 2 } - D _ { 0 } b _ { 1 } \right ] 
 \frac { 1 } { 1 - b _ { 2 } } \log A - \log A _ { 0 } \right ] = \frac { \frac { \sigma ^ { 2 } b _ { 1 } ^ { 2 } } { 2 } - D _ { 0 } b _ { 1 } } { 2 } \right ] \colon 
 C 
 O 
 0$$

By solving the above system of linear equations with respect to /g1864/g1867/g1859/g1827 /g3398 /g1864/g1867/g1859/g1827 /g2868 and /g1830 /g3028/g3043/g3043 , the analytical solution becomes

$$\log A - \log A _ { 0 } = \frac { 1 } { 2 } \frac { ( \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } ) ^ { 2 } - \sum _ { j = 1 } ^ { n } b _ { j } \sum _ { j = 1 } ^ { n } b _ { j } ^ { 3 } } { n \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } - ( \sum _ { j = 1 } ^ { n } b _ { j } ) ^ { 2 } } \sigma ^ { 2 } ,$$

$$D _ { s p p } - D _ { 0 } = \frac { 1 } { 2 } \frac { \sum _ { j = 1 } ^ { n } b _ { j } \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } - n \sum _ { j = 1 } ^ { n } b _ { j } ^ { 3 } } { n \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } - ( \sum _ { j = 1 } ^ { n } b _ { j } ) ^ { 2 } } \sigma ^ { 2 } \\ .$$

.

(9)

Since  the  relationship  between  the  standard  deviation σ and  the  FWHM ξ is log2 8 × σ =ξ , Eqs. (8) and (9) can also be expressed by

$$\log A - \log A _ { 0 } = \mu \xi ^ { 2 } \ ,$$

$$D _ { a p p } - D _ { 0 } = \lambda \xi ^ { 2 } \, ,$$

where µ and λ are two factors determined by

$$\mu = \frac { 1 } { 1 6 \times \log 2 } \frac { ( \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } ) ^ { 2 } } { n \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } \hat { \cdot } ( \sum _ { j = 1 } ^ { n } b _ { j } ) ^ { 2 } } \\ ,$$

$$\lambda = \frac { \hat { \Delta } ^ { 1 } } { ( 1 6 \times \log 2 ) } \frac { \sum _ { j = 1 } ^ { n } b _ { j } ^ { \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } - n } \sum _ { j = 1 } ^ { n } b _ { j } ^ { 3 } } { ( n \sum _ { j = 1 } ^ { n } b _ { j } ^ { 2 } - ( \sum _ { j = 1 } ^ { n } b _ { j } ) ^ { 2 } } } \\ C O _ { 1 }$$

The above analytical expressions explicitly reveal the relationship between the MDC bias and the square of the FWHM (or the standard deviation).    It indicates that: (a) a bias is introduced between the observed value and the statistical mean value of the  MDCs;  (b)  the  bias  is  proportional  to  the  square  of  the  FWHM;  and  (c)  the proportionality factor is affected by the experimental parameters.

Nevertheless,  owing  to  the  change  in  statistical  weight  caused  by  taking  a logarithm, this analytical solution derived by linear regression does not give the same result  as  non-linear  regression  of  the  experimental  data  to  an  exponential  function. Besides, it is remarkable that the drawback of the linear regression becomes obvious when  the  experimental  data  are  of  high  levels  of  attenuation.    This  is  because experimental errors in very small signals have little effect on non-linear regression to an  exponential,  but  a  very  large  effect  on  linear  regression.    Thus  the  above analytical solutions are only accurate for data with low attenuation, where the change of the statistical weights of noises does not affect too much.

## Computer Simulations and Discussion

To verify the above analysis results, a set of simulated diffusion data constructed of normally distributed MDCs were generated, where the distribution center ( D 0) was 5.0  ×  10 -11 m 2 /s.    The  corresponding  FWHMs  ( ξ )  was  2.0  ×  10 -11 m 2 /s.    The simulated  experimental  parameters  were δ =  3  ms, ∆ ' =  299  ms, γ =  2.6752  ×  10 4 G -1 s -1 (the gyromagnetic ratio of proton) with 32 gj values equally spaced from 2 to 64 Gauss/cm.    The distributions and the diffusion parameters were set in this way to mimic practical  situations  of  polymers  or  bio-macromolecules.    For  simplicity,  we set the intensity A 0 = 1 for all simulations run in this study.    Afterwards, the data was fitted  by  the  Stejskal-Tanner  equation,  which  is  Eq.  (2),  using  both  linear  and non-linear  regression  method.    The  simulated  data  and  the  regression  lines  are plotted in FIG. 2 .

FIG. 2. A set of simulated diffusion data with center diffusion coefficient 5.0 × 10 -11 m 2 /s and FWHM 2.0  ×  10 -11 m 2 /s  are  shown  in  both  FIG.  (a)  and  (b)  (the  open  circles).    The  corresponding  linear regression line of Eq. (2) (the solid line in FIG. 2-a) and non-linear regression line of Eq. (2) (the solid

<!-- image -->

line  in  FIG.  2-b)  is  also  shown.    The  solid  circles  in  both  FIG.  (a)  and  (b)  are  the  same  simulated diffusion data added with 1% Gaussian white noises, respectively.

As  illustrated  in  FIG.  2,  the  regression  lines  represent  the  best  fit  of  the  data points.    For linear regression fitting of Eq. (2), predictably, the obtained MDC value is  deviated  from  the  distribution  center.    Similarly,  there  also  exists  a  deviation between  the  obtained  MDC  value  and  the  distribution  center  under  non-linear regression fitting.    This can be confirmed from FIG. 2, which the black solid lines representing the best regression lines have a little deflection of the data.    The fitted MDC of Eq. (2) is  4.7472  ×  10 -11 m 2 /s  in  linear  case,  and  4.8897  ×  10 -11 m 2 /s  in non-linear  case.    The  bias  ( Dapp -D 0)  is  -2.5280  ×  10 -12 m 2 /s  in  linear  case,  and -1.1034 × 10 -12 m 2 /s in non-linear case.    The bias by these parameters would lead to about 2% to 5% systematic error in routine MDC measurements, which indicates a non-ignorable  deviation  introduced  by  the  conventional  mono-exponential  fitting method.

It is worth noticing that taking logarithm of the exponential equation carries the risk of noise amplification, especially for low signal to noise ratio (SNR) data.    To represent the impact of the noise, we added 1% Gaussian white noise on the original diffusion  signal  and  took  logarithm  of  the  noise  data  afterwards.    The  black  solid circles in FIG. 2(a) illustrates the effect of the growing  noise by applying logarithmetics, while the black solid circles in FIG. 2(b) reveals a uniform noise level on each diffusion data.    Further noise tests were implemented with noise levels range from 0.01% to 1.0%, and both linear and non-linear regression results were shown in Table  1.    It  says  that  this  systematic  bias  can  be  accurately  estimated  under  0.1% noise level.

Table 1. Noise testing results using both linear and non-linear regression method are listed with 100 repeating  times  for  each  set  of  data.    The  set  of  simulated  diffusion  data  are  of  center  diffusion coefficient 5.0 × 10 -11 m 2 /s and FWHM 2.0 × 10 -11 m 2 /s.

| Noise Level (%)   | Noise Level (%)   |    0.01 |    0.02 |    0.05 |     0.1 |     0.2 |     0.5 |     1.0 |
|-------------------|-------------------|---------|---------|---------|---------|---------|---------|---------|
|                   | Linear            | -2.5293 | -2.5215 | -2.5348 | -2.5089 | -2.5482 | -2.4104 | -1.8477 |
|                   | Non-linear        | -1.1034 | -1.1021 | -1.1030 | -1.1044 | -1.1138 | -1.1138 | -1.1347 |
|                   | Linear            |    0.48 |    0.93 |    2.59 |    5.74 |   11.49 |   24.07 |   61.10 |
|                   | Non-linear        |    0.31 |    0.60 |    1.48 |    3.41 |    7.09 |   15.74 |   35.10 |

These weaknesses of the logarithmetics indicate that non-linear regression could be  a  more  proper  method  to  deal  with  the  experimental  data  than  the  linear  one, because  most  of  the  experimental  data  contain  various  noises  which  lead  to  a relatively low SNR.

As discussed above, an approximation is introduced in Eq. (4a), which indicates that  the  analytical  solution  holds  only  in  cases  where  the  integral  from  -∞ to  0  is ignorable.    To test the performance of this bias with FWHMs, we generated 62 sets of  simulated  data  of  decays  of  normally  distributed  MDCs  using  above  mentioned experimental  parameters.    In  order  to  keep  the  approximation  valid,  the  following situation

$$R = \frac { h \left ( 0 \right ) } { h \left ( D _ { 0 } \right ) } < 0 . 1 \%$$

should  be  satisfied.    Otherwise,  there  would  be  too  many  negative  diffusion coefficients which cannot be ignored.    Hence, all the distributions were centered at 5.0 × 10 -11 m 2 /s while equally spaced FWHMs from 1.0 × 10 -12 to 3.15 × 10 -11 m 2 /s were tested. The maximum ratio of /g1844 is 0.0925%. Afterwards, the Stejskal-Tanner  equation  was  fitted  using  both  linear  and  non-linear  regression method  respectively.    The  corresponding  biases  are  plotted  versus  the  square  of FWHMs in FIG. 3, where a predicted bias relation ( Dapp -D 0 = -6.3199 × 10 9 ξ 2 ) (in linear case) and a regression line ( Dapp -D 0 = -2.8149 × 10 9 ξ 2 ) (in non-linear case) depicted by solid lines are also shown.

1

FIG. 3. Relationship between the diffusion bias and the square of the distribution width are shown. The  biases  are  depicted  by  open  circles  (linear  regression)  and  solid  circles  (non-linear  regression) while the solid line represents the predicted bias relation (linear regression) and the fitted regression line (non-linear regression).

<!-- image -->

From FIG. 3, one can see that, in both linear and non-linear case, the observed diffusion coefficient bias is almost perfectly agrees with the regression line. But the bias is different between linear and non-linear regressions.    This is due to the change of the statistical weight.    Consequently, non-linear regression result gives a smaller deviation between the apparent MDC value and D0 than that of the linear regression. This indicates that non-linear regression method could obtain more acceptable results than the linear one.      Further increase of the FWHM, the observed MDC would have a big deviation on the statistical mean value of the distribution.    This systematic bias would lead to an incorrect estimation on MDC.

Under  these  circumstances,  logarithmetics  would  carry  more  fitting  error  than direct fitting using non-linear regression method.    Similar to Eq. (11), we were able to derive the following relationship of the non-linear form

$$D _ { a p p } - D _ { 0 } = \lambda ^ { \prime } \xi ^ { 2 } \acute { k } \bigvee$$

Unlike  the  linear  regression,  the  proportional  factor /g1351 /g4593 in  non-linear  form  changes slightly  with  D0.    The  MDC    distribution  centers  range  from  5.0  ×  10 -11 m 2 /s  to 1.05 × 10 -10 m 2 /s with 0.5 × 10 -11 m 2 /s step length were tested, while maintaining all the  other  experimental  parameters  to  be  the  same  as  preceding  part  of  the  text. The  MDC biases  were  calculated  for  each  D0  and ξ .    A  three  dimensional  pseudo color  graph  contains  both  linear  (surface  a)  and  non-linear  (surface  b)  results  are shown in FIG. 4.

FIG. 4. Three dimensional pseudo color graph shows the relationship between the diffusion bias, the center  diffusion  coefficient  and  the  square  of  the  distribution  width.    The  biases  are  depicted  by different colors.    Surface (a) represents the linear regression result while surface (b) is the non-linear regression result.    The mark /g2755 and the three marks ( /g2755 /g2778 ′ ,   /g2755 /g2779 ′ ,  /g2755 /g2780 ′ ) in the graph stand for the different slope  of  linear  regression  and  non-linear  regression  results,  respectively.    Their  values  are: /g2755 /g2778 ′ /g3404 /g3398/g2779. /g2785/g2778 /g3400 /g2778/g2777 /g2786 s/m 2 , /g2755 /g2779 ′ /g3404 /g3398/g2778. /g2785/g2785 /g3400 /g2778/g2777 /g2786 s/m 2 , /g2755 /g2780 ′ /g3404 /g3398/g2778. /g2780/g2780 /g3400 /g2778/g2777 /g2786 s/m 2 and /g2755 /g3404 /g3398/g2783. /g2780/g2779 /g3400 /g2778/g2777 /g2786 s/m 2 .

<!-- image -->

The  slightly  twisted  pseudo  color  surface  (surface  b)  suggests  the  dependence between the proportional factor and the center diffusion coefficient making non-linear problem to be more complicated than the linear one.    Analyzing the twisted section, an approximately inverse relationship between the proportional factor and the D0 can be easily derived.

FIG. 5 shows the relationship between D0 and the reciprocal of the proportional factors  fitting  by  non-linear  regression  lines.    It  tells  us  that,  the  MDC  bias  is  not only  proportional  to ξ but  also  has  a  reciprocal  relationship  with  D0  and  the  scale factor is  about /g2009 = -7.1285. This  factor is nearly nothing  to do  with  the experimental parameters as long as the decay curve is complete.

FIG. 5. Relationship between the center diffusion coefficient D0 and the reciprocal of the proportional factor  derived  by  non-linear  regression  (open  circles)  are  shown.  The  solid  line  represents  the regression line of the data.    And the fitted line slope is /g2009 = -7.1285.

<!-- image -->

Thus, we have the relation of the non-linear form

$$D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 } } , \quad \bigotimes \bigcup \intertext { D _ { a r p } - D _ { 0 } = \frac { \xi ^ { 2 } } { \alpha D _ { 0 }$$

$$D _ { 0 } = \frac { 1 } { 2 } \left ( D _ { a p p } + \sqrt { D _ { a p p } ^ { 2 } - \frac { 4 \xi } { \alpha } } \right ) .$$

Because  4 ξ α is  negative,  the  whole  thing  in  square  root  is  always  positive. Eq.  (17)  implies,  when 0 ξ → , 0 0 app D D -→ ,  which  is  obvious  and  agrees  well with  our  previous  model.    Because  this  scale  factor  does  not  depend  on  any experimental  parameters,  it  can  be  considered  as  a  constant.    Thus,  if  the ξ is estimated correctly, the right average MDC value could be obtained.

So far we have given an accurate way to calculate the MDC bias from both linear and non-linear regression methods.    Our study reveals a systematic error that cannot be  simply  eliminated  by  enhancing  only  the  performances  of  the  instrument.    To improve the measurement, some mathematical models based on physical grounds can be applied, e.g. normal distribution as discussed in this paper (Eq. (7), taking A 0 , D 0 and σ as unknowns), stretched/compressed exponential functions, [23-26] etc.

It  should  be  noted  that  the  MDC  bias  in  this  article  refers  to  the  systematic deviation between the apparent diffusion coefficient acquired by least squares fitting using Stejskal-Tanner equation and the statistical mean value of the MDC distribution. This bias should not be confused with the biases among the number-average diffusion coefficient, DN, the weight-average diffusion coefficient, DW, and the most probable diffusion coefficient, DP, which are derived from the MDC  distribution of polymers. [10,27] More explicitly, the statistical mean value of the MDC distribution, D0, can be considered as the number-average diffusion coefficient of a polydisperse systems.    To  those  who  needs  to  know  the  Molecular  Weight  (MW)  distribution, some  regularization  methods,  such  as  Constrained  Regularization  (CONTIN), [28] Maximum Entropy (MaxEnt), [29] Iterative Thresholding Algorithm for Multiexponential  Decay  (ITAMeD), [30] Trust-Region  Algorithm  for  the  Inversion (TRAIn), [31] etc.,  may  be  applied  together  with  the  use  of  a  scaling  law.    The advantages and disadvantages among these methods were discussed by J. Jakes, Iain J. Day and K. Xu, [31-33] which are beyond the scope of this article.

## Conclusion

A  systematic  bias  between  the  apparent  diffusion  coefficient  obtained  by  the Stejskal-Tanner equation and the statistical mean value of the distribution is noticed and illustrated by numerical analysis and simulations.    This systematic bias is caused by improper modeling of the MDC distribution. Under a Gaussian distribution of the MDCs, the bias can be expressed by Dapp -D 0 = λ ξ 2 .

The MDC obtained by the conventional method is deviated from the statistical mean  value  (the  number-average  diffusion  coefficient).    It  requires  us  to  employ appropriate techniques for diffusion data analysis, especially for polydisperse samples. Although our data is derived from a normal distribution, the tendency that the broader the distribution, the larger the bias, remains for most of the distributions.    The bias inevitably  leads  to  discrepancies  in  the  calculation  of  the  molecular  sizes  via  the Stokes-Einstein equation. To make  the measurement more appropriate, the distribution of MDCs rather than a single MDC value needs to be considered.

## Acknowledgements

This  work  was  supported  by  National  Fundamental  Research  Project  of  China (2013CB921800).

We also thank Prof. Gareth Morris for his valuable advices.

## References

- [1] I. N. Levine, Physical Chemistry , 4th ed. ; McGraw-Hill; New York, (1995).
- [2] E. O. Stejskal, J. E. Tanner, Spin Diffusion Measurements: Spin Echoes in the Presence of a Time Dependent Field Gradient , J. Chem. Phys. 42 , 288 (1965).
- [3] J. A. Jones, D. K. Wilkins, L. J. Smith, C. M. Dobson, Characterisation of protein unfolding by NMR diffusion measurements , J. Biomol. NMR. 10 , 199 (1997).
- [4]  T.  S.  Derrick,  E.  F.  McCord,  C.  K.  Larive, Analysis  of  Protein/Ligand  Interactions  with  NMR Diffusion Measurements: The Importance of Eliminating the Protein Background, J. Magn. Reson. 155 , 217 (2002).
- [5] L. H. Lucas, K. E. Price, C. K. Larive, Epitope Mapping and Competitive Binding of HSA Drug Site II Ligands by NMR Diffusion Measurements , J. Am. Chem. Soc. 126 , 14258 (2004).
- [6] N. Salvi, R. Buratto, A. Bornet, S. Ulzega, I. R. Rebollo, A. Angelini, C. Heinis, G. Bodenhausen, Boosting the Sensitivity of Ligand-Protein Screening by NMR of Long-Lived States , J. Am. Chem. Soc. 134 , 11076 (2012).
- [7] H. B. Schwarz, H. Ernst, S. Ernst, J. Kärger, T. Röser, R. Q. Snurr, J. Weitkamp, NM R study of intrinsic diffusion and reaction in CsNaX type zeolites , Appl. Catal. A-Gen. 130 , 227 (1995).
- [8]  P.  Y .  Ghi,  D.  J.  T.  Hill,  A.  K.  Whittaker, PFG-NMR  Measurements  of  the  Self-Diffusion Coefficients of Water in Equilibrium Poly (HEMA-co-THFMA) Hydrogels , Biomacromolecules. 3 , 554 (2002).
- [9] K. F. Morris, C. S. Johnson, Resolution of Discrete and Continuous Molecular Size Distributions by Means of Diffusion-Ordered 2D NMR Spectroscopy , J. Am. Chem. Soc. 115 , 4291 (1993).
- [10] A. Chen, D. Wu, C. S. Johnson, Determination of Molecular Weight Distributions for Polymers by Diffusion-Ordered NMR , J. Am. Chem. Soc. 117 , 7965 (1995).
- [11] M. Liu, J. K. Nicholson, J. A. Parkinson, J. C. Lindon, Measurement of Biomolecular Diffusion Coefficients in Blood Plasma Using Two-Dimensional 1H-1H Diffusion-Edited Total-Correlation NMR Spectroscopy , Anal. Chem. 69 , 1504 (1997).
- [12] A. D. Maher, L. A. Cysique, B. J. Brew, C. D. Rae, Statistical Integration of 1H NMR and MRS Data  from  Different  Biofluids  and  Tissues  Enhances  Recovery  of  Biological  Information  from Individuals with HIV-1 infection , J. Proteome Res. 10 , 1737 (2011).
- [13]  M.  Nilsson,  A.  M.  Gil,  I.  Delgadillo,  G.  A.  Morris, Improving  Pulse  Sequences  for  3D Diffusion-Ordered NMR Spectroscopy: 2DJ-IDOSY , Anal. Chem. 76 , 5418 (2004).
- [14] S. Gaemers, A. Bax, Morphology of Three Lyotropic Liquid Crystalline Biological NMR Media Studied by Translational Diffusion Anisotropy , J. Am. Chem. Soc. 123 , 12343 (2001).
- [15]  F.  Ferrage,  M.  Zoonens,  D.  E.  Warschawski,  J.  L.  Popot,  G.  Bodenhausen, Slow  Diffusion  of Macromolecular Assemblies by a New Pulsed Field Gradient NMR Method , J. Am. Chem. Soc. 125 , 2541 (2003).
- [16] S. Cavadini, J. Dittmer, S. Antonijevic, G. Bodenhausen, Slow Diffusion by Singlet State NMR Spectroscopy , J. Am. Chem. Soc. 127 , 15744 (2005).
- [17]  C.  S.  Johnson, Diffusion  ordered  nuclear  magnetic  resonance  spectroscopy:    principles  and applications , Prog. Nucl. Magn. Reson. Spectrosc. 34 , 203 (1999).

- [18] P. Damberg, J. Jarvet, A. Gräslund, Accurate Measurement of Translational Diffusion Coefficients: A Practical Method to Account for Nonlinear Gradients , J. Magn. Reson. 148 , 343 (2001).
- [19] S. Zhang, Quantitative Measurement of Molecular Diffusion Coefficients by NMR Spectroscopy , J. Am. Chem. Soc. 128 , 4974 (2006).
- [20]  S.  Zhang, Pivotal  Steps  Towards  Quantification  of  Molecular  Diffusion  Coefficients  by  NMR , Chem. Phys. Chem. 8 , 635 (2007).
- [21] M. A. Connell, P. J. Bowyer, P. A. Bone, A. L. Davis, A. G. Swanson, M. Nilsson, G. A. Morris, Improving  the  accuracy  of  pulsed  field  gradient  NMR  diffusion  experiments:  Correction  for gradient non-uniformity , J. Magn. Reson. 198 , 121 (2009).
- [22] D. W. Marquardt, An Algorithm for Least-Squares Estimation of Nonlinear Parameters , SIAM J. Appl. Math. 11 , 431 (1963).
- [23]  X.  Gong,  E.  W.  Hansen,  Q.  Chen, A  Simple  Access  to  the  (Log/Normal)  Molecular  Weight Distribution  Parameters  of  Polymers  Using  PGSTE  NMR ,  Macromol.  Chem.  Phys. 212 , 1007 (2011).
- [24] X. Gong, E. W. Hansen, Q. Chen, Molecular Weight Distribution Characteristics (of a Polymer) Derived from a Stretched-Exponential PGSTE NMR Response Function-Simulation ,  Macromol. Chem. Phys. 213 , 278 (2012).
- [25] X. Gong, E. W. Hansen, Q. Chen, The Scaling Law between Molecular Mass and Diffusivity and its  Influence  on  the  Molecular  Weight  Distribution  as  Derived  from  a  Stretched  Exponential PGSTE NMR Response Curve , Macromol. Chem. Phys. 213 , 2464 (2012).
- [26] E. W. Hansen, X. Gong, Q. Chen, Compressed Exponential Response Function Arising From a Continuous Distribution of Gaussian Decays - Distribution Characteristics ,  Macromol. Chem. Phys. 214 , 844 (2013).
- [27]  K.  F.  Morris,  B.  J.  Cutak,  A.  M.  Dixon,  C.  K.  Larive, Analysis  of  Diffusion  Coefficient Distributions in Humic and Fulvic Acids by Means of Diffusion Ordered NMR Spectroscopy , Anal. Chem. 71 , 5315 (1999).
- [28] S. W. Provencher, A constrained regularization method for inverting data represented by linear algebraic or integral equations , Comput. Phys. Commun. 27 , 213 (1982).
- [29] M. A. Delsuc, T. E. Malliavin, Maximum Entropy Processing of DOSY NMR Spectra , Anal. Chem. 70 , 2146 (1998).
- [30] M. Urba ń czyk, D. Bernin, W. Ko ź mi ń ski, K. Kazimierczuk, Iterative Thresholding Algorithm for Multiexponential Decay Applied to PGSE NMR Data , Anal. Chem. 85 , 1828 (2013).
- [31] K. Xu, S. Zhang, Trust-Region Algorithm for the Inversion of Molecular Di ff usion NMR Data , Anal. Chem. 86 , 592 (2014).
- [32]  J.  Jakes, Testing  of  the  constrained  regularization  method  of  inverting  laplace  transform  on simulated very wide quasielastic light scattering autocorrelation functions, Czech. J. Phys. B 38 , 1305 (1988).
- [33] I. J. Day, On the inversion of diffusion NMR data: Tikhonov regularization and optimal choice of the regularization parameter, J. Magn. Reson. 211 , 178 (2011).

## Graphical abstract

<!-- image -->

## Highlights

- /circle6 Up to 5% underestimation of the MDC is introduced by fitting data of polydisperse systems.
- /circle6 The bias is caused by the change of statistical weight in fitting process.
- /circle6 The bias is increased linearly with the growth of MDC distribution width.

<!-- image -->

<!-- image -->