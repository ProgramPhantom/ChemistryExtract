Received: 22 November 2013

Revised: 13 December 2013

(wileyonlinelibrary.com) DOI 10.1002/mrc.4047

## 19 F DOSY NMR analysis for spin systems with n J FF couplings

## Guilherme Dal Poggetto, a Denize C. Favaro, a Mathias Nilsson, b,c Gareth A. Morris c and Cláudio F. Tormena a *

NMR is a powerful method for identi fi cation and quanti fi cation of drug components and contaminations. These problems present themselves as mixtures, and here, one of the most powerful tools is DOSY. DOSY works best when there is no spectral overlap between components, so drugs containing fl uorine substituents are well-suited for DOSY analysis as 19 F spectra are typically very sparse. Here, we demonstrate the use of a modi fi ed 19 F DOSY experiment (on the basis of the Oneshot sequences) for various fl uorinated benzenes. For compounds with signi fi cant n J FF coupling constants, as is common, the undesirable J -modulation can be ef fi ciently suppressed using the Oneshot45 pulse sequence. This investigation highlights 19 F DOSY as a valuable and robust method for analysis of molecular systems containing fl uorine atoms even where there are large fl uorine -fl uorine couplings. Copyright © 2014 John Wiley &amp; Sons, Ltd.

Keywords:

DOSY; 19F

## Introduction

The importance of fl uorine in medicinal chemistry is widely recognized. An increasing number of drugs (antidepressant, immunosuppressant, antibacterial, antiviral drugs, etc.) contain fl uorine atoms, often within a fl uorobenzene system, where the presence of the fl uorine atoms is vital for the drug action. [1 -3]

NMR spectroscopy is by far the most popular technique for structure elucidation in solution, and its application in quality control of medicines is steadily growing. [4] The most informative nuclei are generally 1 H and 13 C, but sometimes, the sheer abundance of signals makes spectra very dif fi cult to interpret. 1D 19 F NMR has recently been shown to reinforce 1 H NMR analysis of commercial formulations containing fl uorine as an active ingredient. [5,6] Using a less common nucleus such as 19 F certainly helps resolution, but in a mixture, it is often dif fi cult to assign signals to speci fi c mixture components. This sometimes necessitates the use of costly and time-consuming puri fi cation procedures before NMR analysis.

However, the advent of DOSY experiments [7 -9] has given the spectroscopist a powerful tool for separating the signals from different compounds on the basis of their diffusion behavior (i.e. according to size in most instances), by spreading out the signals in a second diffusion dimension. A recent example is for the analysis of admixtures of the antibiotic cipro fl oxacin, [5] where 1 H DOSY was used to obtain fi ngerprints for several formulations, allowing characterization of some of the excipients present in the formulations studied. DOSY is at its most powerful when the spectral resonances are well separated. In this situation, differences in diffusion coef fi cients of less that 1% are distinguishable for high-quality data. [10]

When signals do overlap, more advanced processing can be used, but the underlying mathematical dif fi culties only allow the separation of signals with a much larger difference in diffusion coef fi cients and only for a limited, typically 3 -4, number of chemical components. [11 -27] The advantages of avoiding overlap have spurred

Accepted: 1 January 2014

<!-- image -->

Published online in Wiley Online Library: 27 January 2014

the development of several NMR experiments to simplify spectra [28,29] or to reduce the overlap by using multidimensional experiments. [30 -33] The overlap problem is very common in 1 HDOSY, so the use of alternative nuclei can be advantageous. [34 -36] DOSY is most commonly used to assess relative diffusion coef fi cients (i.e. sizes), but with some care, a reasonable estimate of absolute molecule weight can also be obtained. [37]

The direct combination of 19 F NMR and DOSY in a 19 F DOSY experiment has the potential to be very useful for studying drug formulations with fl uorine-containing compounds that are part of a complex mixture. 19 F acquisition ensures that only the compounds of interest are seen (so long as they retain a fl uorine atom), that the chances of overlap are small, and DOSY enables the relative sizes of the species to be assessed. Very recently, a 19 F DOSY experiment [38] using a spin-echo scheme was used to separate the (singlet) fl uorine signals of four molecules containing CF3 groups.

Here, we present an alternative 19 F DOSY pulse sequence, on the basis of the Oneshot sequences, [14,39] with 1 H -19 F decoupling. This stimulated echo sequence allows better lock stability, has more fl exibility in setting the diffusion encoding, and avoids problems with long periods of transverse magnetization (e.g. T2 relaxation and J -modulation) but at a cost of up to a factor of two in signalto-noise ratio (depending on the values of T1 and T2). For coupled

* Correspondence to: Cláudio Tormena, Organic Chemistry, Institute of Chemistry -State University of Campinas, São Paulo CP 6154 -CEP 13083-970, Brazil. E-mail: tormena@iqm.unicamp.br
- a Institute of Chemistry, University of Campinas, Campinas São Paulo, CP 6154 -CEP 13083-970, Brazil
- b Department of Food Science, Faculty of Science, University of Copenhagen, Rolighedsvej 30, DK-1958, Frederiksberg C Denmark
- c School of Chemistry, University of Manchester, Oxford Road, Manchester M13 9PL, UK

spins, a spin-echo-based sequence, as used previously, will suffer from very severe J -modulation and is rarely an appropriate choice for such systems. The Oneshot sequences advocated here should work well in most situations.

Even in a stimulated echo-based sequence, there are problems, although much less pronounced, with J -modulation. The effects of J -modulation due to homonuclear proton -proton couplings can be ef fi ciently suppressed using the Oneshot45 sequence. [14] However, 1 H -1 H couplings constants are relatively small (typically up to 20 Hz), whereas 19 F -19 F can be signi fi cantly larger (up to 200 Hz). Therefore, the problems posed by J-modulation are expected to be signi fi cantly greater for many fl uorine systems. Here, we illustrate the use of 19 F Oneshot and Oneshot45 pulse sequences with 1 H -19 F decoupling and evaluate their use for 19 F DOSY. The sequences are demonstrated using a set of model fl uorinated compounds (Fig. 1) with signi fi cant J FF couplings.

The fl uorinated aromatic compounds of Fig. 1 were chosen as model systems because a number of fl uorine-containing pharmaceuticals, [40] such as sitagliptin, viroconazole, ezetimibe, and fl uconazole, contain aromatic rings with similar substitution patterns to those present in compounds 1 to 4 .

Figure 1. Studied fl uorinated compounds: 2- fl uorophenol ( 1 ), 2fluoroanisole ( 2 ), 1-bromo-2,3-di fl uorobenzene ( 3 ), and 1-bromo-2,4,5tri fl uorobenzene ( 4 ).

<!-- image -->

## Experimental Section

All compounds ( 1 -4 ) were obtained commercially (Sigma-Aldrich, USA.) and were used without further puri fi cation; samples were prepared using 10 mg of compound in 0.8 ml of DMSOd 6 . 19 F{ 1 H} 1D NMR and 19 F{ 1 H} DOSY measurements were carried out nonspinning on an 11.74 Tesla Bruker spectrometer (Bruker, Germany) equipped with a 5mm BBO SmartProbe equipped with a z-gradient coil producing a nominal maximum gradient of 50 G cm  1 , operating at 499.87 and 470.29 MHz for 1 H and 19 F, respectively.

The 19 F{ 1 H} DOSY data were acquired using the Oneshot [39] and Oneshot45 [14] sequences, modi fi ed to add broadband (waltz16) 1 H decoupling (Fig. 2). The total diffusion-encoding pulse duration δ (p30) was 2.0 ms, the delay for gradient recovery (d16) 1.0 ms, and the diffusion delay Δ (d20) 40ms for the Oneshot and Oneshot45 sequences, and ten nominal gradient amplitudes were used ranging from 4.8 to 38.4 G cm  1 . The experiments were carried out at a nominal probe temperature of 25 ° C with standard variable temperature regulation. DOSY spectra were constructed using the DOSY Toolbox [15] using a line broadening of 3 Hz and without zero fi lling. The errors given are the standard errors estimated by the fi tting procedure.

## Results and Discussion

The Oneshot and Oneshot45 DOSY pulse sequences were modi fi ed (Fig. 2) to be suitable for 19 F DOSY experiments by incorporating broadband 1 H decoupling and switching of the quadruple nucleus probe unit to change radiofrequency channel between 1 H and 19 F. The Bruker pulse programs are included in the supporting information.

The results of 1 H and 19 F DOSY experiments using the Oneshot sequence of Fig. 2 (without the 45 ° pulse) for a solution containing 2- fl uorophenol ( 1 ) and 2- fl uoroanisole ( 2 ) are shown in Fig. 3.

<!-- image -->

Figure 2. Stimulated echo Oneshot [39] and Oneshot45 [14] pulse sequences (with the extra 45° pulse for the latter experiment shown in red brackets), adapted for 19 F DOSY by the inclusion of broadband 1 H decoupling and by the addition (top line) of explicit gating between 1 H and 19 F channels. The diffusion delay, is the time between the midpoints of the two diffusion-encoding periods, τ is the time between the midpoints of the antiphase fi eld gradient pulses within a given diffusion-encoding period, δ /2 is the total diffusion-encoding gradient pulse width, and the amplitudes of the diffusion-encoding gradient pulses are unbalanced by a factor α to suppress unwanted coherence transfer pathways.

<!-- image -->

<!-- image -->

Judging by the Oneshot 1 H DOSY spectrum alone (Fig. 3a), there would appear to be several components in the aromatic region. This is not the case: the peaks at intermediate diffusion coef fi cients are attributable to resonance overlap in the 1 H spectrum for hydrogen atoms from 2- fl uorophenol and 2- fl uoroanisole (Fig. 1). Because of this overlap and its effect on apparent diffusion coef fi cients, it is not possible to determine unambiguously how many chemical species are present in the sample.

However, in the 1 H decoupled Oneshot 19 F DOSY spectrum of the same sample, the two resonances for fl uorine in compounds 1 and 2 (Fig. 1) are decoupled from the protons and are well resolved, so two diffusion coef fi cients are clearly observed, showing that two different fl uorinated chemical species are present. These results (Fig. 3) highlight the utility of 19 F DOSY for rapidly and easily determining the number of different fl uorinated species that are present in an unknown sample (provided that they diffuse at different rates).

To demonstrate some of the challenges of 19 F DOSY, the standard Oneshot 19 F experiment was also performed for a solution of 1-bromo-2,3-di fl uorobenzene ( 3 ) in DMSO-d6 (Fig. 4). The two resonances for fl uorine atoms present in benzene ring (Fig. 1) are perfectly decoupled from the protons. However, the J -modulation due to homonuclear vicinal fl uorine couplings distorts the doublets (Fig. 4a). This distortion is due to the 3 J FF coupling, which for compound 3 is 22.6 Hz. During the echo time, the coupling evolves to produce J -modulation, evident even when the echo time was reduced as much as possible. It is well-known [14] that this effect can signi fi cantly affect the diffusion coef fi cients measured when signals overlap; this is not the case here but is the norm for more complex samples.

<!-- image -->

Figure 3. DOSY spectra using Oneshot sequences (Fig. 2) for a sample containing 2- fl uorophenol ( 1 ) and 2- fl uoroanisole ( 2 ) in DMSO-d6. a ) 499.87 MHz 1 H DOSY spectrum, with the least attenuated 1D spectrum shown at the top; b ) 470.29 MHz 19 F DOSY spectrum with 1 H decoupling, again, with the least attenuated 1D spectrum shown at the top.

Figure 4. Least attenuated signals from 19 F DOSY (470.29 MHz) experiments on 1-bromo-2,3-di fl uorobenzene ( 3 ) in DMSO-d6 at 25 °C, using the two pulse sequences from Fig. 2: a ) Oneshot and b ) Oneshot45.

<!-- image -->

Figure 5. 470.29 MHz 19 F DOSY spectrum, with the least attenuated 1D spectrum shown at the top, for 1-bromo-2,3-di fl uorobenzene ( 3 ) in DMSO-d6 using the Oneshot45 sequence (Fig. 2).

<!-- image -->

Figure 6. 470.29 MHz 19 F DOSY spectrum, with the least attenuated 1D spectrum shown at the top, for a mixture containing compounds 3 and 4 in DMSO-d6 using the Oneshot45 sequence.

<!-- image -->

Figure 7. Least attenuated signals from 19 F DOSY (470.29 MHz) experiments on a mixture containing compounds 3 and 4 in DMSO-d6 at 25 °C: a ) using the Oneshot45 pulse sequence and b ) using the Oneshot sequence.

<!-- image -->

<!-- image -->

<!-- image -->

For 1 H DOSY, the effects of J -modulation have been shown to be ef fi ciently suppressed by the Oneshot45 sequence, [14] but this sequence has not hitherto been evaluated for 19 F DOSY, where the problems are expected to be much worse because of the larger coupling constants. To evaluate the utility of the Oneshot45 sequence, it was compared with the Oneshot sequence for compound 3 using identical conditions. As can be seen (Fig. 4b), the J -modulation distortion was completely eliminated using Oneshot45 sequence.

The 19 F DOSY spectrum from the Oneshot45 experiment shows perfect agreement between the signals in the diffusion dimension (Fig. 5), with a diffusion coef fi cient of 5.11 ± 0.02 × 10  10 m 2 s  1 .

To demonstrate the potential of the Oneshot45 sequence for 19 F -19 F coupled systems, a more complex mixture sample containing compounds 3 and 4 was chosen. Compound 4 was chosen because of the range ( 5 J FF =4.4 Hz, 4 J FF =13.6 Hz, and 3 J FF =22.4Hz) of the homonuclear coupling constants between fl uorine atoms and because this fl uorine substitution pattern (2,4,5-) is common in fl uorine-containing pharmaceuticals, for example in sitagliptin. [40]

The Oneshot45 19 F DOSY spectrum for the mixture of compounds 3 and 4 can be seen in Fig. 6. The signals from the two compounds line up as expected in the diffusion dimension, thanks to the well-resolved signals in the 19 F dimension, clearly showing that there are two different fl uorinecontaining compounds present. The diffusion coef fi cients were determined with good statistical con fi dence as 4.58 ± 0.03 × 10  10 m 2

- s  1 for compound 4 and 5.04 ± 0.01 × 10  10 m 2 s  1 for compound 3 .

A closer inspection of the least attenuated 1D 19 F spectrum (Fig. 7a) from the Oneshot45 19 F DOSY present (Fig. 6) shows a slight unexpected distortion in the relative amplitude of multiplet components, but there is no corresponding distortion in the diffusion dimension. For the Oneshot sequence, the distortion is less pronounced (but of course, the J -modulation is obvious).

This amplitude distortion observed in the 19 F DOSY spectra for compounds 3 and 4 (Fig. 7a) can be explained by offresonance effects of the radio frequency pulses and therefore related to the large (compared with proton) spectral width (22 kHz). This explanation can be supported for spectra listed on Fig. 4, where a small spectral width was used (2 kHz), and no amplitude distortion was observed. For the sample containing compounds 3 and 4 , the excitation is not uniform for all resonances, introducing distortion in the relative amplitudes of the signals. The effect is more pronounced when using the Oneshot45 sequence because when the 45 ° pulse is far from its nominal value, some antiphase character is added to the signals, leading to unequal multiplet intensities, although happily, the signal phases remain in pure absorption mode. Off-resonance effects are always a concern in 19 F NMR and can, where necessary, be countered by appropriate use of composite pulses, but it is comforting that even with these amplitude distortions, the Oneshot45 sequence provides reliable 19 F DOSY spectra.

## Conclusion

In the present study, it has been demonstrated that 19 F DOSY NMR can be used as a powerful, simple, rapid, and versatile technique for fl uorinated compounds exhibiting fl uorine -fl uorine couplings ( J FF ). The J -modulation due to homonuclear J FF couplings observed with the Oneshot sequence can be completely removed using the Oneshot45 sequence. Examples of potential uses of 19 F DOSY of both coupled and uncoupled systems include the analysis of mixtures formed during degradation processes and the characterization of fl uorinated contaminants in pharmaceutical formulations.

## Acknowledgements

C. F. T. is grateful to FAPESP for fi nancial support (2013/03477-2) of this work and to CNPq for a fellowship (C. F. T.) and scholarship to G. D. P. and D. C. F. This work was also supported by the UK Engineering and Physical Sciences Research Council (grant number EP/I007989/1).

## References

- [1] S. Purser, P. R. Moore, S. Swallow, V. Gouverneur. Chem. Soc. Rev. 2008 , 37 , 320.
- [2] K. L. Kirk. J. Fluor. Chem. 2006 , 127 , 1013.
- [3] V. Gouverneur, K. Müller, Fluorine in Pharmaceutical and Medicinal Chemistry from Biophysical Aspects to Clinical Applications, vol. 6 , Imperial College Press, London, 2012 .
- [4] U. M. Reinscheid. J. Pharm. Biomed. Anal. 2006 , 40 , 447.
- [5] S. Tre fi , V. Gilard, M. Malet-Martino, R. Martino. J. Pharm. Biomed. Anal. 2007 , 44 , 743.
- [6] S. Tre fi , V. Gilard, S. Balayssac, M. Malet-Martino, R. Martino. J. Pharm. Biomed. Anal. 2008 , 46 , 707.
- [7] C. S. Johnson. Prog. Nucl. Magn. Reson. Spectrosc. 1999 , 34 , 203.
- [8] G. A. Morris, in Encyclopedia of Nuclear Magnetic Resonance, Advances in NMR, vol. 9 , (Eds: D. M. Grant, R. K. Harris), John Wiley &amp; Sons Ltd., Chichester, 2002 , pp. 35 -44.
- [9] Y. Cohen, L. Avram, L. Frish. Angew. Chem. Int. Ed. 2005 , 44 , 520.
- [10] M. A. Connell, P. J. Bowyer, P. A. Bone, A. L. Davis, A. G. Swanson, M. Nilsson, G. A. Morris. J. Magn. Reson. 2009 , 198 , 121.
- [11] B. R. Martini, V. A. Mandelshtam, G. A. Morris, A. A. Colbourne, M. Nilsson. J. Magn. Reson. 2013 , 234 , 125.
- [12] A. A. Colbourne, S. Meier, G. A. Morris, M. Nilsson. Chem. Commun. 2013 , 49 , 10510.
- [13] A. Colbourne, G. A. Morris, M. Nilsson. J. Am. Chem. Soc. 2011 , 133 , 7640.
- [14] A. Botana, J. A. Aguilar, M. Nilsson, G. A. Morris. J. Magn. Reson. 2011 , 208 , 270.
- [15] M. Nilsson. J. Magn. Reson. 2009 , 200 , 296.
- [16] M. Nilsson, G. A. Morris. Anal. Chem. 2008 , 80 , 3777.
- [17] M. Nilsson, G. A. Morris. Magn. Reson. Chem. 2007 , 45 , 656.
- [18] M. Nilsson, G. A. Morris. Magn. Reson. Chem. 2006 , 44 , 655.
- [19] M. Nilsson, M. A. Connell, A. L. Davis, G. A. Morris. Anal. Chem. 2006 , 78 , 3040.
- [20] K. F. Morris, C. S. Johnson. J. Am. Chem. Soc. 1993 , 115 , 4291.
- [21] P. Stilbs. J. Magn. Reson. 2010 , 207 , 332.
- [22] P. Stilbs. Eur. Biophys. J. Biophy. 2013 , 42 , 25.
- [23] P. Stilbs, K. Paulsen, P. C. Grif fi ths. J. Phys. Chem. 1996 , 100 , 8180.
- [24] R. E. Joyce, I. J. Day. J. Magn. Reson. 2012 , 220 , 1.
- [25] L. C. M. Van Gorkom, T. M. Hancewicz. J. Magn. Reson. 1998 , 130 , 125.
- [26] W. Windig, B. Antalek. Chemometr. Intell. Lab. 1997 , 37 , 241.
- [27] J. Zhong, N. DiDonato, P. G. Hatcher. J. Chemometr. 2012 , 26 , 150.
- [28] J. A. Aguilar, S. Faulkner, M. Nilsson, G. A. Morris. Angew. Chem. Int. Ed. 2010 , 49 , 3901.
- [29] M. Nilsson, G. A. Morris. Chem. Commun. 2007 , 933.
- [30] D. H. Wu, A. D. Chen, C. S. Johnson. J. Magn. Reson. A 1996 , 121 , 88.
- [31] A. Jerschow, N. Muller. J. Magn. Reson. A 1996 , 123 , 222.
- [32] M. Nilsson, A. M. Gil, I. Delagadillo, G. A. Morris. Chem. Commun. 2005 , 1737.
- [33] M. Nilsson, A. M. Gil, I. Delagadillo, G. A. Morris. Anal. Chem. 2004 , 76 , 5418.

- [34] A. Botana, P. W. A. Howe, V. Caer, G. A. Morris, M. Nilsson. J. Magn. Reson. 2011 , 211 , 25.
- [35] M. J. Stchedroff, A. M. Kenwright, G. A. Morris, M. Nilsson, R. K. Harris. Phys. Chem. Chem. Phys. 2004 , 6 , 3221.
- [36] D. H. Wu, A. D. Chen, C. S. Johnson. J. Magn. Reson. A 1996 , 123 , 215.
- [37] R. Evans, Z. Deng, A. K. Rogerson, A. S. McLachlan, J. J. Richards, M. Nilsson, G. A. Morris. Angew. Chem. Int. Ed. 2013 , 52 , 3199.
- [38] C. Dalvit, A. Vulpetti. Magn. Reson. Chem. 2012 , 50 , 592.
- [39] M. D. Pelta, G. A. Morris, M. J. Stchedroff, S. J. Hammond. Magn. Reson. Chem. 2002 , 40 , S147.
- [40] S. Swallow, in Fluorine-Containing Pharmaceuticals; in Fluorine in Pharmaceutical and Medicinal Chemistry from Biophysical Aspects to Clinical Applications, vol. 6 , (Eds: V. Gouverneur, K. Müller), Imperial College Press, chapter 5, 2012 , p. 141.

<!-- image -->

## Supporting Information

Additional supporting may be found in the online version of this article at the publisher ' s website.

177

1097458xa, 2014, 4, Downloaded from https:/analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/mrc.4047 by University Of Maryland, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https:/onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the appli