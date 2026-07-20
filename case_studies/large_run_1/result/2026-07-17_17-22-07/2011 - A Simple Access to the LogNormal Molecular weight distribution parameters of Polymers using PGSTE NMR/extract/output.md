<!-- image -->

## A Simple Access to the (Log/Normal) Molecular Weight Distribution Parameters of Polymers Using PGSTE NMR

Xiaoliang Gong, Eddy W. Hansen,* Qun Chen*

A log/normal MWD is characterized by two parameters, its mean molecular weight M 0 and width s . It is demonstrated how these parameters can be obtained by model fitting a stretched exponential function (SEF), as characterized by two parameters b and D S, to the PGSTE response

curve. Based on simulations, two general empirical equations relating b and D S to M 0 and s are found. The model enables the MWD characteristics to be determined if the scaling law between diffusivity and molecular weight is known. The sensitivity and relative error of s and M 0 are discussed and the applicability of the model is illustrated by analyzing experimental NMR response curve of some PEO samples. The numerical robustness, and reliability.

## Introduction

The average molecular weight (MW) and molecular weight distribution (MWD) are two fundamental polymer characteristics that can be determined by, for instance, gel permeation chromatography (GPC), dynamic light scattering (DLS), and viscosity measurements. Also, pulsedgradient spin echo (PGSE) NMR has been demonstrated

X. Gong, Q. Chen

Physics Department and Shanghai Key Laboratory of Magnetic Resonance, East China Normal University, Shanghai 200062,

China

E-mail: qchen@ecnu.cn

E. W. Hansen

Department of Chemistry, UiO, P. O. Box 1033 Blindern, N-0315

Oslo, Norway

E-mail: eddywh@kjemi.uio.no as a potential experimental tool [1-3] for probing these same characteristics and is often complementary to other techniques. Unlike GPC, PGSE NMR is less dependent on thechoiceofsolventandhasstimulatedNMRresearchersto explore the applicability of NMR to probe MWD of various polymeric systems. [4,5]

<!-- image -->

Aparticular challenge is related to the data processing of the PGSE NMR decay curves to obtain reliable relations between the distribution of diffusivity and the MWD, e.g., bi-exponential fitting, [6] sum of one-parameter functions (e.g., convoluted exponentials, as well as pure exponentials) using a program denoted SPLMOD, [7] component resolved (CORE) [8] anddirect exponential curve resolution algorithm (DECRA). [9] When dealing with complex samples showing severe peak overlap with small differences in derived diffusion coefficients, one may apply multivariate curve resolution (MCR), MCR alternating least square (MCR-ALS) analysis, [10] MCR with non-linear least square regression www.mcp-journal.de

(MCR-NLR) [11] and Maximum entropy (MaxEnt) processing techniques. [12] To obtain the MWD of a polymer from PGSE NMR,Johnsonandco-workers [13] usedamodifiedversionof theconstrainedregularizationprogramCONTIN [14] whileB. Hakansson et al. applied a nonlinear least-squares fitting (NLLS) technique to describe the distribution of D . [15] However, these methods are complex and may frequently introduce artificial broadening of the distribution curve because of data smoothing.

Inthecaseofalog/normalmolecularweightdistribution (LNMWD) we present a simple, robust and reliable numerical method in which to derive the MWD from a pulsed-gradient stimulated spin echo (PGSTE) experiment. A model frequently applied in fitting non-exponential decay curves is a stretch exponential function (SEF), which is generally knownasaKohlrausch-Williams-Watts(KWW) function: [16,17] I x ; b ; D S ð Þ ¼ exp ð xD S Þ b h i , where x is proportional to the square of the amplitude of the gradient pulse. Based on simulations, we will present two general empirical equations relating b and D S to the two LNMWD characteristics M 0 and s , respectively. This approach enables the latter two parameters to be derived from PGSTE NMR measurements, if knowing the scaling law D ¼ KM  a ð Þ between the diffusivity D and the molecular weight M where a andKdefine the scaling parameters. The practical applicability of the technique will be illustrated by analyzing three poly(ethylene oxide) (PEO) samples.

## Experimental Part

The reference (R1-R4) PEO samples were purchased from Tosoh in Japan. The sample characteristics will be presented in a later section. In order to obtain a small concentration of 0.5 mg  mL  1 , the polymer samples were dissolved in D2O using a Thermo Finnpipette, ranging from 20 to 200 and from 100 to 1 000 m L, respectively. The solutions were subsequently stirred for 24 h.

The GPC experiments were performed on an Agilent 1100 instrument with a 0.5 mL  min  1 flow speed with H2O as a solvent.

<!-- image -->

Figure 1. The PGSTE pulse sequence applied in this work where D 0 ¼ D  d = 3 D represents the ''apparent'' diffusion time, and d is the duration of the gradient pulse (see text for further details).

<!-- image -->

The PGSTE NMR experiments were preformed at 298 K on a Varian 700MHzspectrometer,equippedwitha5mmstandardprobewith a maximumavailable gradient pulse field of 70 G  cm  1 . The pulse sequence [18] is illustrated on Figure 1 and includes an offsetindependent adiabatic inversion pulse (2 ms duration) in combination with a gradient pulse ( g s ¼ 7.26 G  cm  1 ) for selective excitation of a central sample region (about 0.65 cm). [18] Under these conditions, the molecular diffusion coefficient is quantitatively determined. The recycle time was set to 10 s and gradient pulse duration of 5 ms. The ''apparent'' diffusion time D ' is defined by D 0 ¼ D  d = 3. The gradient pulses were calibrated on a water sample (10% D2O, 90% H2O) under the same experimental conditions as used on the polymer samples.

## PGSTE NMR - The Response Curve

It is often found that an LNMWD gives a reasonable approximation to many MWDs, as for instance anionically polymerized polymers and certain fractions of polyethylenes. The normalized LNMWD distribution d I /d M reads [19]

h

.

i

$$\frac { d I } { d M } = \frac { 1 } { \sqrt { 2 \pi } M \sigma } \exp \left [ - ( \ln ( M / M _ { 0 } ) ) ^ { 2 } / 2 \sigma ^ { 2 } \right ] \quad ( 1 )$$

where M 0 is the median and s is the width of the distribution. For an LNMWD the polydispersity index ( P ) can be expressed by P ¼ M w  M n ¼ exp s 2 ð Þ .

By referring to the well known equation valid for Gaussian random coils, the relation between molecular diffusivity D and molecular weight M [20] can be expressed by:

$$D = K M ^ { - \alpha }$$

Hence, any MWD [d I /d M ; Equation (1)] can be transformed into a corresponding distribution (d I /d D ) in diffusivity D , according to

$$\frac { d I } { d D } = \frac { d M } { d D } \frac { d I } { d M } & & ( 3 )$$

By combining Equation (1-3) and introducing a dimensionless variable z ( ¼ D / D 0) where D 0 ¼ KM  a 0 wecanrewriteEquation(3)in the form (see Appendix)

"

#

$$\frac { d I } { d z } = \frac { 1 } { \alpha \sigma \sqrt { 2 \pi z } } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma ^ { 2 } } \right ]$$

Equation(4)isusefulwhenaimingatsimplifyingtheexpression for the PGSTE response curve R ( x ), as defined by [13]

Z

$$R ( x ) = \int _ { 0 } ^ { \infty } f ( T _ { 1 } , T _ { 2 } ) \frac { d I } { d D } \exp [ - x D ] d D \\$$

where x ¼ g 2 d 2 g 2 D  d = 3 ð Þ , g is the gyromagneic ratio, D the diffusivity (of a molecule of molecular weight M ), d the gradient pulse duration, and D defines the inter-pulse timing between the two successive gradient pulses of strength g . The term f ð T 1 ; T 2 Þ represents the relaxation term and depends on the parameters d and D . For a polymer the relaxation times T 1 and T 2 are generally determined by the segmental motion (local) and are thus expected to be approximately independent of molecular weight. Also, in highly diluted polymer solutions (as in this work) the effect of intermolecular interactions can be excluded. In the following discussion we will assume the relaxation term f ( T 1, T 2) to be constant and independent on molecular weight, an assumption that is consistent with previous experimental reports. [13,19] However, it must be emphasized that this assumption should be checked experimentally for any sample being investigated. Hence, the term f ( T 1, T 2) equals 1 and Equation (5) simplifies to (see Appendix)

<!-- image -->

"

#

$$R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z \\ \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z } { ( 6 ) } \intertext { T o i l l } \intertext { R ( x ) = \sum _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ($$

For any specific s ¼ s 0 and D ¼ D 0, R ( x ) is solved numerically by replacing the integral in Equation (6) by a finite sum of N terms, i.e.,

h

.

i

$$R ( x _ { j } ) = \frac { 1 } { \alpha \sigma \sqrt { 2 \pi } } \sum _ { i = 1 } ^ { N } \frac { 1 } { z _ { i } } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z \quad ( 7 ) \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x _ { j } D _ { 0 } z _ { i } \right ] \right ] \Delta z & ( 7 ) \\ \end{array} \quad \begin{array} { c c } \frac { 1 } { N } \exp \left [ - ( \ln z _ { i } ) ^ { 2 } \Big / 2 \sigma _ { 0 } ^ { 2 } \right ] \exp \left [ - x$$

where D z ¼ ( z max z min)/ N , and z max and z min chosen so that d I /d z is close to 0 at these extreme z -values. A value of N ¼ 1024 was chosen since a further doubling of N did not significantly change the calculated R ( xj ).

Both D 0, s 0, and a [Equation (2)] were varied systematically and will be reported in this work. In order to mimic a real experiment, a

random noise of 1% was added to each R ( xj ) before model fitting by Equation (7) [note that R (0) ¼ 1; Equation(7)]. By choosing a maximum number of gradient pulses j ¼ j max ¼ 128, the resulting parameters derived by model-fitting R ( xj ) revealed a reproducibility better than 1%. The effect of changing j max and the noise level of R ( x ) is presently under investigation.

After generating a synthetic response curve R ( x ), according to the above procedure, an SEF I S ( x ; b , D S) is fitted to the synthetic response curve R ( x ) using Equation (8)

h

i

$$I _ { S } ( x ; \beta , D _ { S } ) = I _ { 0 } \exp \left [ - ( x D _ { S } ) ^ { \beta } \right ] \quad \ \ ( 8 ) \quad \ \ C )$$

The main objective is to explore the dependenceof M 0 and s on b and D S. Dependingonthe concentration of polymer in the solvent, a is expected to have a value between 0.5 and 0.7. [21] For dilute solutions (  1 wt.-%) a is normally found in the region 0.5 &lt; a &lt; 0.6. As a consequence, synthetic response curves were derived for a ¼ (0.2, 0.35), 0.50, 0.55, 0.60, 0.65, and 0.70, D 0 ¼ 1.00, 1.25, 1.58, 2.51, 3.98, 6.30, and 10.00 -10 11 m 2  s  1 and s ¼ 0.10, 0.35, 0.60, 0.85, 1.10, 1.35, and 1.60. If not otherwise stated in the text, the number of gradient pulseswassetto128witharandomnoiseof1% added to R ( x ) before any further analysis.

<!-- image -->

www.MaterialsViews.com www.mcp-journal.de In summary, the procedure applied in this work is illustrated by the following scheme:

- (i) Specify an LNMWD [ M 0 and s ; Equation (1)]
- (ii) Calculate the PGSE response curve R ( x ) [Equation (7)]
- (iii) Add 1% random noise to R ( x )
- (iv) Fit an SEF [Equation (8)] to R ( x ) and derive D S and b .

## Results and Discussion

## Generating PGSTE Response Curves R ( x ) from an LNMWD

To illustrate the technique we start with three randomly chosen distributions d I /d D with a ¼ 0.50, as shown in Figure 2A with D S (m 2  s  1 )// s ¼ 1.02 -10  11 //0.746, 3.95 -10  11 //0.864, and 9.92 -10  11 //0.967. The corresponding response curves R ( x ) were calculated from Equation (7) after adding 1% random noise (Figure 2B). The solid curves represent non-linear least squares fits to Equation (8). The residuals (difference between observed and calculated signal intensity) are shown in Figure 2C.

An important observation is the approximately random error-distribution between the ''observed'' (synthesized) and the fitted response curve, suggesting that a more fundamental relation between the inverse Laplace transform of an SEF and a log/normal function exists. Actually, www.mcp-journal.de this will become more evident from the results presented in later sections.

<!-- image -->

Figure 2. (A) Three randomly chosen distributions of diffusion coefficient with D s (m 2  s  1 )// s ¼ 1.02 -10  11 //0.746, 3.95 -10  11 //0.864, and 9.92 -10  11 //0.967. (B) The synthetic PGSTE NMR response curves. The solid curves represent stretch exponential model fits [Equation (8)] with two adjustable parameters D s (m 2  s  1 ) and s . (C) Residual between synthesized and fitted response curves.

<!-- image -->

## Effect of a , D 0, and s on D S

Figure 3A shows how the stretch exponential parameter D S depends on s , D 0 and a and suggests that D S is independent on both a and s . Actually, by plotting D S versus D 0 for all a and s (Figure 3B) we find that D S equals D 0. An important consequence of these results is that the average molecular weight (or more precisely, the median of the molecular weight distribution) M 0 can simply be expressed by Equation (9), by use of the scaling law, Equation (2)





$$M _ { 0 } = \left ( \frac { K } { D _ { S } } \right ) ^ { 1 / \alpha }$$

Hence, if we know the scaling parameters a and K , the median molecular weight M 0 of the distribution is uniquely defined by the diffusivity D S

## Effect of a , D 0, and s on b

In order to explore the dependence of the stretch exponential factor b in Equation (8) on the parameters a , D 0, and s we notice from Figure 4A that -within experimental error b does not depend on D 0. A closer examination of the data in Figure 4A suggest that for any a the parameter b can be approximated by a Gaussian function with respect to s (as illustrated by the solid curves in Figure 4A) and can be expressed by

Figure 3. (A) The stretch exponential parameter D S as a function of s and a ¼ (0.2, 0.35, 0.50, 0.55, 0.60, 0.65, 0.70). (B) D S as a function of D 0.

<!-- image -->

<!-- image -->

Figure 4. (A) Stretch exponential factor b as a function of s and D 0 ¼ 1.00, 1.25, 1.58, 2.51, 3.98, 6.30, and 10.00 -10 11 m 2  s  1 . (B) Relationship between the constant k and a . The two curves represent polynomial function fits of order 1 ( \_\_ ) and 2 (--), respectively.

<!-- image -->





$$\beta = \exp ( - k \sigma ^ { 2 } )$$

where k is a constant for each a . By extending this analysis and plotting k against a (Figure 4B) we find that k can be well approximated by a polynomial function of order 1 ( \_\_ ) or 2 (- -). In the region 0.2 &lt; a &lt; 0.7, a simple linear relation ( k ¼ -a þ b a ) between k and a is found with a ¼ 0.040  0.003 and b ¼ 0.284  0.006, respectively.

Theseresultsimplythatthedistributionparameter s can be expressed by a and b according to

ffiffiffiffiffiffiffiffiffiffiffi ffi

r

$$\sigma = \sqrt { \frac { \ln \beta } { a - b \alpha } }$$

with a ¼ 0.040 and b ¼ 0.284.

<!-- image -->

Equation (9 and 11) represents the main tools to be used in establishing the LNMWD from an experimental PGSTE response curve. Henceforth, the empirical Equation (9 and 11) will be referred to as the ''Master'' equations.

Amorecomprehensive evaluation of the applicability of the master equations demands for a sensitivity and error analysis and will be addressed next.

## Sensitivity and Error Analysis

## Sensitivity

As pointed out, the MWD characteristics ( s and M 0) of a polymermaybeobtainedbyastretchexponentialmodelfit to its PGSTE response curve by applying the two ''Master'' equations, Equation (9 and 11). In these equations, the parameters K and a are system parameters, as defined by the scaling law [Equation (2)], and are considered constants for a particular polymer. Keeping in mind that the minimumobtainable value of D S depends on instrumental hardware (maximum available gradient pulse power and the duration of gradient pulses) this will, according to the scaling law [Equation (2)], affect the maximum molecular www.mcp-journal.de weight M 0 that can be possibly determined by the NMR technique. Moreover, Equation (9) shows that the maximum accessible value of M 0 becomes larger with increasing K . However, since K is system-dependent (type of polymeranditsconcentrationinsolution) [22-24] it is outside instrumental and operator control. Generally K is found to be of the order of 10  8 . [22] If not otherwise stated in the text we have set K ¼ 2.4 -10  8 in the subsequent calculations (see Experiment Part).

<!-- image -->

Figure 5. (A) The dependence of M 0 on D S with K ¼ 2.4 -10  8 and a ¼ (0.50, 0.60, 0.70). (B) The dependence of s on b with the same K and a as in (A).

<!-- image -->

The dependence of s and M 0 on b and D S are shown in Figure 5A and B and suggest (for a given a and K ) that the sensitivity in M 0 is constant and independent on D S. In contrast, the sensitivity in s increases with increasing b . A morequantitativeevaluationofsensitivitycanbeachieved by calculating the relative change ( ss / s and s M 0 / M 0) in s and M 0ataconstantrelativechange(ofsay10%)in b and D S . The results are plotted in Figure 6 and show that the sensitivity in M 0 (negative because M 0 decreases with increasing D S) is independent on D 0 but dependent on a . It increases slightly from about 14% for a ¼ 0.70 to  20% for a ¼ 0.50.

A corresponding analysis of the distribution width parameter s shows that its sensitivity increases from www.mcp-journal.de about 7% to about 20% when b increases from 0.50 to about 0.80. At larger b the sensitivity increases more dramatically and reaches a value of 100% when b approaches 0.94. Note in particular, that the sensitivity of s with respect to b is independent of a .

<!-- image -->

Figure 6. (A) Relative change in M 0 versus D S and a when assuming a constant relative change in b of 10%. (B) Relative change in s versus b and a whenassuminga constant relative change in b of 10%.

<!-- image -->

In the next section we will evaluate the relative error in s and M 0 by applying the well known ''propagation of error'' technique.

## Relative Error in s and M 0

Due to the inherent noise in the PGSTE response curve this will affect the corresponding error in the derived MWD parameters s and M 0.

Based on Equation (9 and 11) the relative errors s M 0 / M 0 and ss / s of M 0 and s can be determined from the relative errors s D S / D S and sb / b , respectively. The results are plotted inFigure7AandBandshowthattherelativeerrorin M 0and s increases approximately linearly with increasing relative error of D Sand b . In particular we note that the relative error in s is independent on a , which is in contrast to the corresponding relative error in M 0 which decreases with increasing a . In particular, the accelerating relative error in s with increasing b partially outweighs the improved sensitivity of s at high b (Figure 7B). In order to

(%)0/°。

<!-- image -->

Figure 7. (A) Relative error (%) in M 0 as a function of the relative error (%) in D S. (B) Relative error (%) in s as a function of the relative error (%) in b .

<!-- image -->

obtain MWD parameters possessing a relative error of less than 10%, the parameter b must possess a relative error of less than 1%. In contrast, the relative error in M 0 is not that sensitive to error in D S. Actually, a relative error in M 0 of less than 10% is obtained if the relative error in D S is smaller than 5%. This means that to obtain a reliable (less than 10% error) value of the width parameter s of a narrow MWD( b close to 0.95), a relative error in b of less than 1% mustbeobtainedanddemandsforaratherlownoiseinthe PGSTEresponsecurve. However, a relative error in s and M 0 of less than 10% is easily accessible for b &lt; 0.90. A corresponding relative error of less than 10% for b &gt; 0.90 is manageable but requires a somewhat longer experimental time.

We emphasize that the relative error of both s and M 0 decreases with decreasing b and D S , i.e., the relative error of the two former parameters decrease when the width and the average molecular weight of the polymer increase.

## Examples

The simulations presented in this work suggest that any polymer system possessing an LNMWD can be characterized within a 10% relative error in s and M 0 if M w = M n [ ¼ exp( s 2 )]  1.28 [ ¼ exp(0.45 -0.45)]. Experimental work is in progress to evaluate these findings for a broader range of samples. However, for illustration purposes, we will present experimental results obtained on three PEO samples of which two possess relatively narrow MWDs.

InordertodeterminetheMWDitismandatorytoestablish the scaling relation between diffusivity D and molecular mass M , i.e., to identify the parameters K and a inEquation(2). MorethanadecadeagoJohnsonandco-workers [13] used PFG NMR to determine these parameters for PEO and found K ¼ 10  7.5 and a ¼ 0.6. We have rechecked these values by performing similar NMR experiments on four commercial monodisperse PEO samples (R1-R4; Table 1) resulting in a ¼ 0.61  0.05 and K ¼ (2.4  1.2) -10  8 ( ¼ 10  7.6  0.3 ). Hence, these values are - within experimental error - equal to the corresponding numbers presented by Johnson et al. [13] and others. [15,25] We note in particular that the calculated b ( b calc in Table 1), as obtained by applying one of the Master equations [Equation (11)] and assuming an LNMWD [ M w = M n ¼ exp( s 2 )], are in excellent agreement with the observed b ( b obs in Table 1), except for sample 2. The reason for this discrepancy regarding sample R2 is at present not understood.

The MWD characteristics (Table 2) of the three PEO samples S A, S B, and S C as determinedbyGPC,aretabulatedin Table 2 and their distributions shown in Figure 8A. The results demonstrate - by visual inspection - that both the narrow MWD samples deviate from a pure log/normal distribution, sample S B more than sample S A.

<!-- image -->

www.mcp-journal.de

Table 1. GPC and PGSTE NMR results (fitting a stretch exponential model to the observed response curve) obtained on four monodisperse PEO samples obtained from.

| Sample   | GPC   | GPC       | NMR   | NMR   | NMR       | NMR     |
|----------|-------|-----------|-------|-------|-----------|---------|
|          | M w [10  4 g  mol  1 ]       | M w = M n | D S [10 11 m 2  s  1 ]       | b obs | b calc a) | r 2     |
| R1       | 2.37  | 1.03      | 4.376  0.010       | 0.998  0.003       | 0.996     | 0.99994 |
| R2       | 4.30  | 1.03      | 2.863  0.007       | 0.980  0.003       | 0.996     | 0.99993 |
| R3       | 10.1  | 1.07      | 1.936  0.004       | 0.989  0.003       | 0.991     | 0.99993 |
| R4       | 15.0  | 1.04      | 1.296  0.002       | 0.995  0.004       | 0.995     | 0.99990 |

Table 2. Sample characteristics obtained on three PEO samples by GPC and PGSTE NMR analysis.

| Sample   | GPC   | GPC       | NMR   | NMR   | NMR   | NMR   | NMR          |
|----------|-------|-----------|-------|-------|-------|-------|--------------|
|          | M 0 [10  4 g  mol        | M w = M n | D S [10 11 m 2  s  1 ]       | b     | s a)  | M 0 b) [10 4 g  mol  1       | M w = M n c) |
| S A      | 7.9   | 1.2       | 2.02  0.02       | 0.973  0.009       | 0.46  0.07       | 7.98  0.08       | 1.24  0.09              |
| S B      | 1.9   | 1.5       | 5.35  0.03       | 0.942  0.007       | 0.62  0.02       | 1.65  0.02       | 1.56  0.08              |
| S C      | 4.8   | 5.5       | 2.97  0.03       | 0.794  0.008       | 1.31  0.03       | 4.25  0.06       | 5.6  0.4              |

a) Calculated from Equation (9); b) Calculated from Equation (11) c) Calculated by assuming an LNMWD with M w = M n ¼ exp( s 2 ).

<!-- image -->

Figure 8. (A) The MWD of three PEO samples S A, S B, and S C. The solid curves are derived from GPC and the dotted curves are derived from PGSTE NMR as described in the text (see Table 2). Two of the dotted curves were calculated by replacing s with s  ss and M 0 replaced by M 0  s M 0 . (B) PGSTE NMR data of the three PEO samples S A, S B, and S C.

<!-- image -->

In order to obtain the MWD characteristic by NMR, a SEF [Equation (8)] is fitted to the observed PGSTE response curve, as illustrated on Figure 8B. The numerical values are summarized in Table 2 and show that the relative error in both b and D S is less than  1%, which is a requirementforobtainingasmallerrelativeerror of 10% in s for these narrow MWD samples, as discussed in a previous section. The broader MWD sample S C reveals a difference in M 0 of about 10% between the GPC and NMR derived MWDs. One should then keep in mind thatthenormallyexpecteduncertaintyin the GPC derived MWD is  10%.

The dotted curves in Figure 8A are the NMR derived MWD and were calculated from Equation (1). Moreover, by replacing s with s  ss and M 0 with M 0  s M 0 in Equation (1) with s M 0 and ss representing the standard error in s and M 0, respectively, the two dotted curves for each MWD in Figure 8A appear. These ''extreme'' distributions thus represent a kind of confidence region for the calculated MWD. Recalling that the NMR derived MWD [using Equation (1, 9), and (11) with a ¼ 0.61 and K ¼ 2.4 -10  8 ;

<!-- image -->

www.mcp-journal.de

Table 1) is based on the implicit assumption of an LNMWD andthattheGPCderivedMWDsclearlydeviatefromsucha line shape (in particular for sample S B) we consider the overall results to be rather encouraging. In particular when considering the rather good agreement between M 0 and M w = M n, as obtained with the two different experimental techniques (Table 2).

An interesting and important consequence of the above analysis is that the parameters K and a can be determined from Equation (2, 9), and (11) using a non-linear least squaresalgorithm,ifknowingthe''true''MWDofonesingle sample possessing an LNMWD.

In order to evaluate the practical applicability of the present experimental method a testing of a broad range of polymers covering a wider range of MWD characteristics is of importance. Also, the accuracy with which the calibration parameters K and a [Equation (2)] can be reliably determined by combining a single GPC derived MWD and PGSTE NMR is of particular relevance. Also, to what extent an MWD that deviates from a pure LNMWD will affect the analysis results needs to be addressed both by simulation and by experimental work.

## Conclusion

By simulation we have shown how to obtain the two characteristic parameters ( M 0 and s ) of an LNMWD by fitting the pulsed gradient stimulated echo (PGSTE) response curve to a single SEF (defined by the two parameters b and D S). Two explicit and simple empirical equations relating the two set of parameters are derived. A critical sensitivity and error analysis suggests that the present technique represents a fast and reliable alternative (compared to the ill-posed numerical technique of an inverseLaplacetransformation)tocharacterizetheMWDof polymers possessing LNMWD.

## Appendix

Equation (1) can be rewritten in the form













$$\left ( \frac { M _ { 0 } } { M } \right ) ^ { \alpha } & = \frac { D } { D _ { 0 } } \Leftrightarrow \frac { M _ { 0 } } { M } = \left ( \frac { D } { D _ { 0 } } \right ) ^ { 1 / \alpha } \Leftrightarrow M = M _ { 0 } \left ( \frac { D _ { 0 } } { D } \right ) ^ { 1 / \alpha } \\ & \Leftrightarrow d M = - \frac { M _ { 0 } } { \alpha } \, \frac { D _ { 0 } ^ { 1 / \alpha } } { D ^ { 1 / \alpha + 1 } } d D \\$$

<!-- image -->

Hence, by combining Equation (A1) and Equation (1 and 3) in the main text we arrive at

$$\begin{array} { r l } { \text {the} } & { \frac { d I } { d D } = \frac { d I } { d M } \frac { d M } { d D } } \\ { \text {and} } & { \frac { d I } { d D } = \frac { 1 } { \sqrt { 2 \pi } M _ { 0 } \sigma } \left ( \frac { D } { D _ { 0 } } \right ) ^ { 1 / \alpha } \exp \left [ - \frac { [ \ln ( D _ { 0 } / D ) ] ^ { 2 } } { 2 \alpha ^ { 2 } \sigma ^ { 2 } } \right ] \left [ - \frac { M _ { 0 } } { \alpha } \frac { D _ { 0 } ^ { 1 / \alpha } } { D ^ { 1 / \alpha + 1 } } \right ] } \\ { \text {move} } & { \frac { d I } { d D } = \frac { 1 } { \sqrt { 2 \pi } \alpha \sigma } \frac { 1 } { D } \exp \left [ - \frac { [ \ln ( D _ { 0 } / D ) ] ^ { 2 } } { 2 \alpha ^ { 2 } \sigma ^ { 2 } } \right ] } \\ { \text {east} } & { \frac { d I } { 2 \alpha ^ { 2 } \sigma } = } \end{array}$$

For practical reasons Equation (A2) can be written in a more attractive form by introducing a new dimensionless variable z ¼ D = D 0 , d D ¼ D 0d z ð Þ and noting that

"

#

Z





$$\begin{array} { r l } & { \L d } \\ & { \quad \frac { \ D I } { \ D z } = \frac { \ D I } { \ D D } \, \frac { \ D D } { \ D z } = \frac { 1 } { \sqrt { 2 \pi } \sigma \alpha } \left ( \frac { 1 } { D _ { 0 } z } \right ) \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma ^ { 2 } } \right ] D _ { 0 } } \\ & { \quad \L t } \\ & { \quad = \frac { 1 } { \alpha \sigma \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma ^ { 2 } } \right ] } \end{array} \quad ( A 3 )$$

Concerning the response signal R ( x ) from a PGSTE experiment it follows that

$$\text { experiment if follows that } \\ R ( x ) = \int _ { 0 } ^ { \infty } \frac { d I } { d D } \exp ( - x D ) \, d D & = \int _ { 0 } ^ { \infty } \frac { d I } { d z } \frac { d z } { d D } \\ \exp ( - x D ) d D & = \int _ { 0 } ^ { \infty } \frac { d I } { d z } \exp ( - x D _ { 0 } z ) d z \\ & = \int _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma \sqrt { 2 \pi z } } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z \\$$

Hence, for any specified distribution characterized by D ¼ D 0 and s ¼ s 0 we obtain:

"

#

$$R ( x ) = \int _ { 0 } ^ { \infty } \frac { 1 } { \alpha \sigma _ { 0 } \sqrt { 2 \pi } z } \exp \left [ - \frac { ( \ln z ) ^ { 2 } } { 2 \alpha ^ { 2 } \sigma _ { 0 } ^ { 2 } } \right ] \exp ( - x D _ { 0 } z ) d z \quad ( A 5 )$$

Acknowledgements: This work was supported by National Fundamental Research Program (2007CB925200), the Shanghai Leading Talent Training Program , and the Science &amp; Technology Committee of Shanghai Municipality (07DZ22937, 06DZ22922).

Received: November 14, 2010; Revised: January 10, 2011; Published online: March 10, 2011; DOI: 10.1002/macp.201000706

Keywords: diffusion; modeling; molecular weight distribution; NMR; simulations

<!-- image -->

- [1] E. O. Stejskal, J. E. Tanner, J. Chem. Phys. 1965 , 42 , 288.
- [2] C. S. Johnson, Prog. Nucl. Magn. Reson. Spectrosc. 1999 , 34 , 203.
- [3] S. Abrahmen-Alami, P. Stilbs, J. Colloid Interface Sci. 1997 , 189 , 137.
- [4] D. P. Hinton, C. S. Johnson, Jr., J. Phys. Chem. 1993 , 97 , 9064.
- [5] K. Yu, J. Ouyang, Md. B. Zaman, J. Phys. Chem. C 2009 , 113 , 3390.
- [6] M. Nilsson, M. A. Connell, A. L. Davis, G. A. Morris, Anal. Chem. 2006 , 78 , 3040.
- [7] R. H. Vogel, SPLMOD Users Manual, Data Analysis Group, EMBL-DA09, EMBL , Heidelberg, Germany 1988.
- [8] J.-A. Ostlund, M. Nyden, P. Stilbs, Energy Fuels 2004 , 18 , 531.
- [9] B. Antalek, J. M. Hewitt, Magn. Reson. Chem. 2002 , 40 , S60.
- [10] R. Huo, R. Wehrens, J. V. Duynhoven, L. M. C. Buydens, Anal. Chim. Acta 2003 , 490 , 231.
- [11] R. Huo, R. Wehrens, L. M. Buydens, J. Magn. Reson. 2004 , 169 , 257.
- [12] M. A. Delsuc, T. E. Malliavin, Anal. Chem. 1998 , 70 , 2146.

<!-- image -->

www.MaterialsViews.com www.mcp-journal.de

- [13] A. Chen, D. Wu, C. S. Johnson, Jr., J. Am. Chem. Soc. 1995 , 117 , 7965.
- [14] S. W. Provencher, Comput. Phys. Commun. 1982 , 27 , 213.
- [15] B. Hakansson, M. Nyden, O. Soderman, Colloid Polym. Sci. 2000 , 278 , 399.
- [16] R. Kohlrausch, Annal. Phys. Chem. 1854 , 91 , 179.
- [17] M. N. Berberan-Santos, Lecture Series on Computer and Computational Sciences , Vol. 4, Brill Academic Publishes, The Netherlands 2005, 4, p. 70.
- [18] S. Zhang, Chem. Phys. Chem. 2007 , 8 , 635.
- [19] G. Fleicher, Polymer 1985 , 26 , 1677.
- [20] M. Rubinstein, R. H. Colby, Polymer Physics , Oxford University Press, Oxford, UK 2004, p. 309.
- [21] P. T. Callaghan, J. Lelievre, Biopolymers 1985 , 24 , 441.
- [22] G. D. J. Phillies, Macromolecules 1986 , 19 , 2367.
- [23] G. D. J. Phillies, Macromolecules 1998 , 31 , 2317.
- [24] G. D. J. Phillies, Macromolecules 2002 , 35 , 7414.
- [25] M. Xu, Q. Chen, S. Zhang, Colloid Polym. Sci. 2010 , 288 , 85.

<!-- image -->