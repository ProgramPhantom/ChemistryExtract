Received: 2 September 2015

Revised: 16 March 2016

(wileyonlinelibrary.com) DOI 10.1002/mrc.4454

## 19 F DOSY diffusion-NMR spectroscopy of fluoropolymers

Chenglong Xu, a Yingbo Wan, a Dongxue Chen, a Chun Gao, b Hongnan Yin, a Daniel Fetherston, b Eriks Kupce, c Gerald Lopez, d Bruno Ameduri, d Eric B. Twum, b,f Faith J. Wyzgoski, g Xiaohong Li, a Elizabeth F. McCord e * and Peter L. Rinaldi a,b *

ABSTRACT A new pulse sequence for obtaining 19 F detected DOSY (diffusion ordered spectroscopy) spectra of fluorinated molecules is presented and used to study fluoropolymers based on vinylidene fluoride and chlorotrifluoroethylene. The performance of 19 F DOSYNMRexperiments(and ingeneral anytype ofNMR experiment) on fluoropolymers creates some unique complications that very often prevent detection of important signals. Factors that create these complications include: (1) the presence of many scalar couplings among 1 H, 19 F and 13 C; (2) the large magnitudes of many 19 F homonuclear couplings (especially 2 JFF); (3) the large 19 F chemical shift range; and (4) the low solubility of these materials (which requires that experiments be performed at high temperatures). A systematic study of the various methods for collecting DOSY NMR data, and the adaptation of these methods to obtain 19 F detected DOSY data, has been performed using a mixture of low molecular weight, fluorinated model compounds. The best pulse sequences and optimal experimental conditions have been determined for obtaining 19 F DOSY spectra. The optimum pulse sequences for acquiring 19 F DOSY NMR data have been determined for various circumstances taking into account the spectral dispersion, number and magnitude of couplings present, and experimental temperature. Pulse sequences and experimental parameters for optimizing these experiments for the study of fluoropolymers have been studied. Copyright © 2016 John Wiley &amp; Sons, Ltd.

Keywords:

DOSY; Fluoropolymers; Diffusion; NMR; Fluorine

## Introduction

The advent of DOSY (diffusion ordered spectroscopy) [1] has made NMR a powerful tool for performing structural studies on components of mixtures, based on their size and molecular weight (MW). It not only aids in spectral dispersion and resonance assignments, but also provides structural information based on the sizes and shapes of structures. [2 -11] It has been widely used to study the molecular weights of polymers, [12 -17] and for molecular weight and structure studies of supramolecules, [7,18 -20] pharmaceuticals [21] and organometallic complexes. [22,23] In addition, with some care, it is possible to measure the molecular weights and sizes of small molecules. [24 -26]

Because of convenience and relatively high receptivity, 1 H-detection is most commonly used for the performance of DOSY experiments. However, several other nuclei serve as excellent candidates for measuring diffusion via DOSY NMR detection. These include 7 Li, 6 Li (with isotopic enrichment), [27 -30] and 19 F. [31,32]

Fluoropolymers are very important because of their unique chemical, mechanical and physical properties. [33,34] In particular, copolymers containing vinylidene fluoride (VDF) [35] or 1-chloro-1,2,2trifluoroethylene (CTFE), [36] have excellent high temperature stability, resistance to oxidation, resistance to chemical attack by a variety of solvents and corrosive chemicals and a variety of useful commercial properties. [37,38] NMR studies of these and other fluoropolymers are very exciting and useful. [39] The presence of three NMR active nuclei, the high natural abundance of both 1 H and 19 F and the unique NMR properties of 19 F produce NMR spectra

Accepted: 20 April 2016

<!-- image -->

Published online in Wiley Online Library: 9 June 2016

with an amazing amount of information. Recently, it has been shown that 19 F detected DOSY experiments could be used to distinguish between the resonances of polymer chain-ends and other branching structures in a series of fluoropolymers. [40 -42]

* Correspondence to: Peter L. Rinaldi, Department of Chemistry, University of Akron, Akron, Ohio 44325-3601. E-mail: rinaldi@uakron.edu
- ** Correspondence to: Elizabeth F. McCord, E. I. Du Pont de Nemours and Co, Experimental Station, Wilmington, DE 19880-0402, USA. E-mail: Elizabeth.F. McCord@dupont.com
- a College of Chemistry, Chemical Engineering and Materials Science, Soochow University, Suzhou, 215123, China
- b Department of Chemistry, University of Akron, 190 East Buchtel Commons, Akron, OH, 44325-3601, USA
- c Agilent, Current address: Bruker BioSpin, Coventry CV4 9GH, UK
- d Ingénierie and Architectures Macromoléculaires, Institut Charles Gerhardt, École Nationale Supérieure de Chimie de Montpellier, 8 Rue de l ' École Normale, 34296, Montpellier, France
- e E. I. Du Pont de Nemours and Co, Experimental Station, Wilmington, DE, 198800402, USA
- f Indiana University, Department of Chemistry, 800 E. Kirkwood Ave., Bloomington, IN, 47405-7102, USA
- g Department of Chemistry and Biochemistry, The Ohio State University, 1760 University Drive, Mansfield, OH, 44906, USA

Generally, the performance of 19 F NMR experiments on fluoropolymers creates some unique complications that often interfere with detection of important signals. [39] These factors include: (1) the presence of many scalar couplings among 1 H, 19 F and 13 C; (2) the large magnitudes of many 19 F homonuclear couplings (especially 2 J FF ); (3) the large 19 F chemical shift range; and (4) the low solubility of these materials (which requires that experiments be performed at high temperatures).

When both 1 H and 19 F are present in a structure the presence of many large, long-range homoand hetero-nuclear couplings broadens the multiplets observed. This results in lower signal-tonoise levels and more severe overlap of resonances. Both factors make it difficult to resolve separate signals from all the unique chemical structures which are present in many polymers.

In 19 F NMR experiments of small molecules 4 J FF couplings can be as large as 5 -10Hz, and resolvable 5 J FF couplings can often be observed. In the spectra of polymers, the latter couplings are not usually resolved; however, they broaden the resonances and reduce signal-to-noise levels. When CF2 groups are attached to branch points, the fluorines are diastereotopic and often exhibit chemical shift non-equivalence. Under these circumstances, large 2 J FF couplings, on the order of 200 -300Hz, are observed. These large couplings create circumstances which can prevent the detection of resonances in many 2D-NMR experiments, including DOSY experiments.

The large 19 F chemical shift range often makes it difficult to uniformly excite the entire chemical shift range with relatively long 180° refocusing pulses. This is especially a problem when CF, CF2 and CF3 resonances are all present in the spectrum, because the resonances of these three groups occur in very different spectral regions which are well-separated.

Finally, when high temperature diffusion NMR experiments are performed, convective flow of the solution leads to additional translational motion. This motion gives rise to higher apparent diffusion coefficients. In severe cases, the convective contribution to the apparent diffusion coefficient can mask small differences in the diffusion of slightly different molecular species in solution.

Many methods for performing 1 H detected DOSY experiments have been reported in the literature. [2 -6,8] Because of the complications listed above, these methods sometimes fail to produce detectable signals in 19 F detected DOSY spectra, especially when studying the weak signals from fluoropolymer chain-ends and branch structures, which are often the most important components to characterize. These complicating interactions may prevent general applications of existing DOSY methods (which were typically developed using 1 H detection) to the collection of DOSY spectra with detection of heteronuclei such as 19 F. This present study discusses methods of collecting 19 F DOSY NMR spectra which minimize problems from these complicating factors. The methods should also be applicable to collection of DOSY NMR spectra obtained with detection of other heteronuclei.

Heteronuclear couplings like n JHF can easily be removed by incorporating broadband 1 H decoupling during the acquisition period of the DOSY experiment. Although these couplings can evolve during delays when the magnetization is in the transverse plane, they are removed by 180° 19 F inversion pulses in the middle of these delays, and so are not a problem in the DOSY experiment. The presence of 1 JCF and 2 JCF couplings produces weak 13 C satellite resonances on either side of strong signals. These are often confused with the weak resonances from low concentrations of polymer chain-end and defect structures. Interfering signals from these couplings are removed in the same way that complicating resonances from n JHF heteronuclear couplings are removed. However, n J FF homonuclear couplings create problems, especially when 2 J FF couplings (typically 250 -300 Hz) are present. When significant n J FF couplings are present, because of either large two-bond couplings or because of broad multiplets from many intermediate (10 -30 Hz) couplings, undesirable J-modulation can cause phase distortions and significant loss of signal intensity. Dal Poggetto et al. [32] devised an 19 F Oneshot-45 DOSY experiment that suppresses the J-modulation when the couplings are on the order of 50 Hz or less. However, in their work this sequence was not tested on spectra with n JFF =200 -300 Hz.

<!-- image -->

The large 19 F NMR chemical shift dispersion often creates complications because of the large resonance offsets from the transmitter. Severe phase and amplitude distortions for the peaks in the outer parts of the 19 F spectra greatly limit the ability to collect DOSY spectra of the entire chemical shift range of many compounds. To alleviate this problem, pulse sequences using composite pulses were evaluated. Because the low solubility of many fluoropolymers requires data collection at high temperature, a convection compensating pulse sequence [43] was evaluated for suppressing contributions to the measured diffusion coefficient (D) from convective flow.

The first reports of using 19 F DOSY to study fluoropolymer chainend and branching structures involved poly(VDF) homopolymer [40] and poly(vinylidene fluorideco -tetrafluoroethylene) (poly(VDFco -TFE)) copolymers. [41] These spectra were devoid of the aforementioned problems because the resonances were dispersed over the relatively narrow (50 ppm) CF2 region of the 19 F chemical shift range, and almost all of the CF2 fluorines were chemically equivalent. However, problems were encountered in later attempts to study copolymers and terpolymers of VDF containing hexafluoropropylene (HFP). [37,42] The latter monomer introduces CF and CF3 resonances into the spectrum, expanding the chemical shift range of polymers ' resonances to 150 ppm. HFP units also create stereogenic centers from CF3 branch sites along the polymer backbone, thus introducing large 2 J FF couplings from the adjoining diastereotopic CF2 fluorine atoms.

Here a systematic study of the various methods for obtaining DOSY NMR data, and the adaptation of these methods to obtain 19 F detected DOSY spectra has been performed using a mixture of low molecular weight, fluorinated model compounds. The best pulse sequences and optimal experimental conditions for obtaining good quality 19 F DOSY spectra have been determined for various circumstances, taking into account the spectral dispersion, number and magnitude of couplings present, and experimental temperature. Pulse sequences and experimental parameters for optimizing these sequences for the study of fluoropolymers have been determined. The utility of these optimized experiments is illustrated with various fluoropolymers including poly(vinylidene fluorideter -tetrafluoroethyleneterhexafluoropropylene) (poly(VDFter -TFEter -HFP)) terpolymer, poly(chlorotrifluoroethyleneco -vinylidene chloride) (poly (CTFEcoVDC)) copolymer and poly(vinylidene fluorideco -α , β -difluoroacrylic acid) (poly(VDFco -DFAA)) copolymer. Using these experimental conditions, it is possible to study the diffusion of polymeric structure elements whose weak NMR signals were previously undetectable in simple DOSY experiments.

1097458xa, 2017, 5, Downloaded from https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/mrc.4454 by University Of Maryland, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by t

<!-- image -->

## Experimental

## Materials

A mixture of 2,2,3,4,4,4-hexafluoro-1-butanol (HFB, Aldrich Chemical Co., 0.03 mL of a solution with 0.062 g/mL), 1-chloro2,6-dinitro-4-trifluoromethylbenzene (TFMB, 0.009 g of solution with 0.013 g/mL) and 3,3,4,4,5,5,6,6,7,7,8,8,8-tridecafluorooctanol (FO, Alfa Aesar, 0.01 mL of solution with 0.02 g/mL) in 0.7 mL of CDCl3 (Cambridge Isotope Laboratories) was used as a model sample for small molecule studies. All of the above materials were obtained from commercial sources and were used as received. The synthesis, characterization and preparation of NMR samples of poly(VDFco -HFP), [40,42] poly(VDFter -TFEter -HFP), [37] poly(CTFEco -VDC) polymers [38] and poly(VDFco -DFAA) [44] copolymers have been previously described.

## Instruments

All data were collected and processed with Agilent VnmrJ 3.2 software. Unless otherwise noted all NMR work on small molecules was performed at Soochow University on an Agilent DD2 600-MHz spectrometer equipped with four RF channels (two of these were high band 1 H/ 19 F channels); dual power (0.6/1.2 T/m) gradient amplifier; 1 H/ 19 F/X triple resonance probe and 1 H/ 19 F diplexer. All small molecule NMR data collection was performed at 298 K. Unless otherwise noted all NMR work on polymer molecules was performed at The University of Akron on a Varian DirectDrive 500-MHz spectrometer equipped with five RF channels (two high band 1 H/ 19 F channels); dual power (0.7/1.4 T/m) gradient amplifier; 1 H/ 19 F/X triple resonance probe and 1 H/ 19 F diplexer. All polymer NMR data collection was performed at 303 K unless otherwise noted.

## General DOSY experiments

The bipolar pulse pair stimulated echo experiment [1,45] was performed with the standard (Dbppste) pulse program available in the Agilent pulse sequence library. The bipolar pulse pair stimulated echo experiment with longitudinal eddy current delay and homospoil gradient (Dbppste\_led), [1,45] together with variations that include composite (90x -180y -90x) and adiabatic refocusing pulses were performed with a modified version of the standard Dbppste\_led pulse program which is included in the Supporting Information section and is given the name Dbppste\_ad. The DOSY oneshot 45° experiment [32] was performed with the standard (Doneshot45) pulse program available in the Agilent pulse sequence library. The DOSY bipolar pulse pair stimulated echo experiment with suppression of convection artifacts [43] (Dbppste\_cc) was performed with the standard pulse program available in the Agilent pulse sequence library. All the above sequences were modified so that the LED delay could be set independently from the other gradient stabilization delays.

## Results and discussion

Figure 1 shows the 564-MHz 19 F 1D-NMR spectrum of a sample mixture containing three small molecules: FO ( 1 ), HFB ( 2 ) and TFMB ( 3 ). These structures were chosen to show the features which frequently complicate collection of DOSY spectra from highly fluorinated polymers and other molecules. They exhibit resonances which span the CF3 (  60 to  90ppm), CF2 (  100 to  150ppm) and CF (  180 to  220ppm) regions of the NMR spectrum. The resonances span a frequency range of ca. 100 kHz on a 600-MHz spectrometer. The spectrum contains resonances which are complicated by all ranges of J FF and JFH couplings. In particular, HFB shows two components of the coupling pattern from an AX spin system (shown in the center inset, with chemical shifts near  119.3 and  123.0ppm) with 2 JFF =280Hz. These signals exhibit many of the complications caused by large couplings. Fortuitously, an impurity in the commercial sample of HFB exhibits a similar AM spin coupling pattern, shown with 10× vertical expansion in the right hand inset. The spectrum was collected with a short pulse width (3.0 μ s) to minimize intensity variations across the spectral window because of resonance offset effects. The high solubility of all components makes this an ideal test sample.

## Pulse sequences

Figure 2 shows diagrams of the pulse sequences evaluated in this work. Figures 2a -c and 2f describe sequences that are part of the standard library of most modern NMR spectrometers. All the sequences begin with an hsg -90x° -hsg element so that all magnetization components from prior pulse sequence elements are destroyed. In this way, only Mz magnetization which has developed because of relaxation during the d1 relaxation delay is present at the beginning of the first DOSY pulse sequence element.

Figure 2a is the commonly used bipolar pulse pair stimulated echo experiment. A later variation (Fig. 2b) incorporates a delay element (90° -gt3 -delst -90°, the so-called ' longitudinal eddy current delay ' ) immediately before data acquisition to allow the NMR instrument to stabilize after the train of gradient pulses are applied, so that high resolution NMR spectra can be acquired. [45] The sequence has been further modified, compared to the originally published sequence, by the addition of a homospoil gradient pulse at the beginning of this stabilization delay (delst) to remove phase distortions from small J modulation and incomplete recovery after the gradient pulses. The implications of this element with regard to the problems at hand will be understood upon examination of the spectral data discussed below.

Details of how these sequences work can be found in any of the review articles cited at the beginning of this paper, and only a brief discussion relevant to the problems at hand are presented here. The first and last 90° -δ /2 -180° -δ /2 -90° sequence elements serve to defocus and refocus the magnetization as a function of the molecules ' position in the magnetic field gradients produced by the δ /2 magnetic field gradient pulses before and after diffusion during the diffusion delay Δ . The τ delays are short recovery delays to permit the system to stabilize after the gradient pulses. During the defocus and refocus time periods (timescale typically ca. 1 -10ms), magnetization is in the transverse plane and is subject to T2, T1 and J homonuclear interactions; chemical shift evolution, and JCF and JHF heteronuclear coupling interactions are removed by the refocusing pulses in the middle of these delays. During the Δ delay, also referred to as the diffusion delay, molecules move to different parts of the field based on their relative diffusion coefficients, so that signals are only partially refocused based on the differences in their position in the field gradient at the beginning and end of the sequence. During this delay the signal is subject to decay only from diffusion and T1 relaxation. Usually the DOSY experiment is performed with all delays fixed, and with the magnitudes of the

Figure 1. 564-MHz 19 F 1D-NMR spectrum of a mixture of HFB, TFB and FO in CDCl3 (pw = 3.0 μ s, 35°). The resonances are labeled with attributions to structures 1 , 2 and 3 .

<!-- image -->

Figure 2. Summary of pulse sequence diagrams evaluated in this work: a) standard Dbppste; b) standard Dbppste\_led; c) Doneshot45; d) Dbppled\_ad with adiabatic refocusing pulses, written for this work; e) Dbppled\_ad with composite refocusing pulses; and f) Dbppste\_cc with led. See text for details. In the diagrams, open and filled RF pulses are 90° and 180° pulses, respectively, Gaussian pulse shapes are meant to designate WURST adiabatic pulses and hsg are homospoil gradient pulses.

<!-- image -->

δ /2 gradient pulses varied. The signal decay is measured and fit to Equation (1).

$$I = I _ { 0 } \exp \left [ - D \gamma ^ { 2 } g ^ { 2 } \delta ^ { 2 } ( \Delta \cdot \delta / 3 ) \right ]$$

Here I and I 0 are the signal intensity and the initial signal intensity with no gradient applied, D is the diffusion coefficient and g is the gradient intensity. Note that the γ 2 dependence of signal decay is what makes proton signal intensities so sensitive to changes in diffusion, and together with relative natural abundance, is what makes the experiment more difficult to apply to other nuclei. Because 19 F and 1 H have such similar nuclear properties ( I =1/2, essentially 100% natural abundance and high γ ) both are excellent candidates for measuring DOSY spectra.

Figure 2c shows the pulse sequence for the Oneshot45 sequence which was originally developed to remove phase distortions from the small J couplings present in 1 H DOSY spectra. [46] Figure 2d shows a modified version of the Dbppste\_led sequence which has its 180 0 refocusing pulses replaced by adiabatic refocusing pulses to form the Dbppled\_ad sequence. Adiabatic pulses have been shown to extend the range of the effective B1 field by over 10-fold compared to simple 180° pulses. [47] Replacement of simple 180° pulses with adiabatic pulses has been shown to greatly increase the effective window covered in heteronuclear single quantum coherence (HSQC) 2D-NMR experiments. [48] Adams [49] has similarly shown that versions of HSQC with adiabatic pulses have been useful for extending the excitation range and eliminating problems from large 19 F homonuclear couplings in 19 F{ 13 C}-HSQC experiments. Similar results are expected when these pulses are used for refocusing magnetization in DOSY experiments. For comparison, the sequence was also modified to substitute simple 180° pulses with 90°x -180°y -90°x composite pulses, [50] which are more useful than simple 180° pulses, but far less effective than adiabatic pulses. This sequence is shown in Fig. 2e.

<!-- image -->

<!-- image -->

When high temperature measurements or high power broadband decoupling are needed during the acquisition time, the sequence developed by Jerschow and Muller [43] (Fig. 2f) can be used to remove the effects of signal decay from convective flow. This is the standard sequence present in the DOSY pulse program library, which has been modified compared to the original reference. It incorporates a homospoil gradient pulse at the beginning of the LED delay. We have further modified this sequence so that the τ and delst gradient stabilization delays can be set independently.

## Influence of large n JFF couplings

The presence of small homonuclear J couplings (0 -20Hz) is a minor nuisance in 1 H detected DOSY experiments. When the couplings are less than 10 Hz, artifacts can be removed by processing with line broadening or by analyzing the data in magnitude mode. Both of these methods are detrimental to peak resolution. At the point of data acquisition, phase distortions can be removed by adding a 90° -hsg -delst -90° sequence immediately before data acquisition.

Figure 3a shows the CF2 regions from the normal 19 F 1D-NMR spectrum. In comparison, the corresponding regions from the first increments (collected with the weakest gradient intensities) from DOSY experiments run with the pulse sequences shown in Fig. 2 are also displayed in Figs. 3b -g. These data were collected on the mixture of small molecules, hereafter referred to as mixture, defined in Fig. 1. Data were processed with exponential weighting to produce a line broadening of 5 Hz, so that many of the small couplings present in the spectra are not resolved. In particular, four broad peaks (  113.8,  122.2,  124.1 and  126.5 ppm) are resolved from the four CF2 groups of FO. An AX pattern is observed, with 2 JFF=280Hz ( δ A =  119.25 ppm δ X =  123.0 ppm), from the diastereotopic CF2 groups of HFB. The high field part of the X doublet overlaps with one of the CF2 resonances of FO. The DOSY spectra were all collected with the default delays entered by the instrument software macro command which automates the setup of these experiments. In particular, the software uses values corresponding to δ =2.0ms and gradient recovery delays τ =500 μ s. These parameters will be called the ' normal ' parameters. The diffusion delay, Δ , and range of gradient amplitudes are then normally adjusted to provide decay of the signal to 10% or less of its initial amplitude.

The normal 19 F 1D-NMR spectrum (Fig. 3a) is provided so that the relative signal strengths can be compared. Figure 3b shows the results from the Dbppste experiment; all the signals exhibit reasonable intensity and phase behavior except for the components of the AX spin pattern. While the magnetization is in the transverse plane (during the gradient defocusing and refocusing times), considerable dephasing occurs for the diastereotopic CF2 signals near  119 and  123ppm, because of modulation by 2 J FF .

The spectrum in Fig. 3c was collected in the same manner except that the magnetization was stored along the z axis while a homospoil gradient pulse destroyed the out of phase magnetization components from homonuclear J modulation. The resulting spectra are without phase distortion and are useable for calculation of DOSY 2D-NMR spectra. However, destruction of the out of phase component leads to considerable loss of signal intensity for the AX

Figure 3. Selected regions showing the CF2 resonances from the spectra of a mixture of small fluorinated molecules: a) 19 F 1D-NMR obtained with a pulse width of 3.0μ s pulse, 1.0-s relaxation delay and 0.94-s acquisition time; the remaining spectra were collected with identical acquisition time and relaxation delay. With the following exceptions all data were collected using the parameters described for the mixture in the experimental section: δ =2.0 ms, τ =500 μ s. The remaining spectra were collected with the following pulse sequences: b) Dbppste; c) Dbppste\_led; d) Doneshot45; e) Dbppled\_ad with 190μ s adiabatic pulses and with homospoil gradient pulse at the beginning of the led delay; f) Dbppled\_ad with 190μ s adiabatic pulses and without a homospoil gradient pulse at the beginning of the led delay; g) Dbppste\_cc. Because these are first increment data, these spectra were obtained with low gradient intensities.

<!-- image -->

spin pattern. Under these data acquisition conditions, the Doneshot45 sequence was found to be ineffective for removing artifacts in the presence of this large coupling (see Fig. 3d).

The spectrum collected with the Dbppled\_ad sequence (Fig. 3e) has very good signal levels for all the peaks. This is fortuitous, and results from the fact that the four long adiabatic pulses (190 μ s) provide extra time for the J modulation to refocus most of the out of phase signal components ( vide infra) . If the homospoil gradient pulse is removed from the led delay at the end of the sequence, the spectrum in Fig. 3f is observed, in which small phase distortions are observed for the component signals of the AX spin system.

With the idea that convection compensation experiments would eventually be needed, the spectrum in Fig. 3g was collected. The Dbppste\_cc sequence gives good phase characteristics, but considerable loss of intensity for the CF 2 AXpattern. Most likely, this results from considerable J-modulated dephasing of the NMR signal, as there is an additional 90° -δ /2 -τ -δ /2 -τ -180° -δ /2 -τ -δ /2 -τ 90° pulse sequence element to eliminate contributions to signal decay from convection. This will be discussed in more detail below.

None of the pulse sequences alone were effective at eliminating problems caused by large couplings. This prompted us to minimize delays when the magnetization is in the transverse plane. The most obvious approach is to reduce the gradient stabilization delays ( τ ), which had typical default values of 500 μ s on our instrument. We found that, with the exception of the last gradient stabilization delay (during the LED pulse sequence element), on the spectrometers used, the τ delays could easily be set as low as 20 μ s. Because there are four of these delays while the magnetization is in the transverse plane, the JFF modulation time could be shortened by almost 2 ms! The experiment could easily tolerate the long stabilization delay during the LED element as the magnetization to be detected is aligned along B0 during this period.

Second, the gradient time δ was reduced to 0.5ms (software default of 1 -2ms), with a corresponding increase in the diffusion delay Δ . Shorter gradient times required longer Δ and/or stronger gradients to obtain equivalent decay of the signals from diffusion. Results from these experiments, which will be referred to as the ' short ' delay ( δ + τ ) experiments, are shown in Fig. 4.

<!-- image -->

Considerable improvement in both intensity and smaller phase distortions can be observed in the spectra from all the pulse sequences when the spectra in Fig. 4 from the ' short ' delay experiments are compared with the spectra in Fig. 3 from the ' normal ' delay experiments. The exception is the spectrum obtained with adiabatic pulses in Fig. 4e where the signals of the AX patterns are slightly weaker than those in the corresponding spectrum obtained with ' normal ' delays in Fig. 3e.

To understand this more thoroughly, a careful study of the J-modulated peak intensities as a function of the gradient encoding and refocusing times was performed. Because the largest contributor to the time for J-modulated dephasing of the NMR signal is the gradient time δ , an experiment was performed in which δ was linearly incremented (from 0.4 to 8.0 ms in 0.4-ms steps) while simultaneously decreasing the gradient strength to maintain a constant gradient pulse area. As expected, all of the signals without large J FF couplings maintained a constant intensity in this constant gradient pulse area array.

Figure 5a shows the J-modulation behavior of the A doublet part of the AX multiplet pattern from HFB, along with one of the CF2 signals of FO. Null points are observed for the doublet when δ = n / (2 × J FF ) ( n =1, 3, 5, … ). The first null point, at 1/2JFF =1.8ms, is in the 1 to 2-ms range of the default delays chosen by the instrument ' s DOSY setup macro commands. Maxima occur when δ = n / (2 × J FF ) ( n =2, 4, 6, … ). In this case, the gradient recovery delays are very small ( τ =20 μ s) and are an insignificant part of the periods when the magnetization is in the xy plane of the rotating frame. However, if other delays contribute significantly to these periods, they must also be factored into consideration.

If the modulation behavior were just a simple function of one J coupling (nominally 2 JFF =280Hz for the sample studied here), then a single optimum delay could be chosen. However, the optimum delay is dependent on multiplicity (doublet, triplet, etc.), on whether or not strong coupling is present, and on the presence of other smaller couplings ( 4 J FF ≅ 20 Hz, and many 3 J FF ≅ 5 Hz). In fact the intensity of the FO CF2 resonance (apparent singlet) does decay somewhat. This decay is attributed to the lower frequency modulation characteristic of a multiplet

Figure 4. Selected regions showing the CF2 resonances from the spectra of a mixture of small fluorinated molecules: a) 19 F 1D-NMR obtained with a pulse width of 3.0μ s pulse, 1.0-s relaxation delay and 0.94-s acquisition time; the remaining spectra were collected with identical acquisition times and relaxation delays. With the following exceptions, all data were collected using the parameters described for the mixture in the experimental section: δ =0.5ms, τ =20 μ s. The remaining spectra were collected with the following pulse sequences: b) Dbppste; c) Dbppste\_led; d) Doneshot45; e) Dbppled\_ad with 190μ s adiabatic pulses and with homospoil gradient pulse at the beginning of the led delay; f) Dbppled\_ad with 190μ s adiabatic pulses and without a homospoil gradient pulse at the beginning of the led delay; g) Dbppste\_cc. Because these are first increment data, these spectra were obtained with low gradient intensities.

<!-- image -->

1097458xa, 2017, 5, Downloaded from https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/mrc.4454 by University Of Maryland, Wiley Online Library on [06/05/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by t with smaller homonuclear coupling, which is unresolved because of the 5-Hz exponential line broadening applied during processing.

<!-- image -->

Figure 5. Stacked spectra of selected regions from the 564-MHz 19 F DOSY spectra of the small molecule mixture from experiment with constant gradient pulse area and array of increasing δ ; values for each array element from left to right are: ( δ (ms)/gradient amplitude(mT/m)0.4/123, 0.8/62, 1.2/41, 1.6/31, 2.0/ 24.6, 2.4/20.5, 2.8/17.6, 3.2/15.4, 3.6/13.7, 4.0/12.3, 4.4/11.2, 4.8/10.2, 5.2/9.4, 5.6/8.8, 6.0/8.2, 6.4/7.7, 6.8/7.2, 7.2/6.8, 7.6/6.5 and 8.0/6.2. a) Dbppste\_led, resonance of AX system near  119 ppm; b) Dbppste\_led, resonances of AM system centered near  135.5 ppm; and c) Dbppste\_cc, resonance of AX system near  119 ppm. The null and maxima points at n / (2 × J FF ) ( n =1, 2, 3, … ) in the J =280-Hz modulation curve are indicated by the arrows across the top.

<!-- image -->

Figure 5b shows the modulation behavior of the diastereotopic CF2 signals from the impurity present in the HFB. Although 2 J FF is essentially identical to that of the CF2 fluorines of HFB, the chemical shift difference is much smaller, resulting in an AM coupling pattern. The intensity modulation behavior of this pattern is very different from that of the AX pattern of HFB, with a maximum occurring near δ =2.6 ms. As seen in the polymer spectra below, for AB coupling patterns the peak intensities are barely modulated.

Figure 6 exhibits the results from arrays with constant gradient pulse area, performed on poly(VDFter -TFEter -HFP) terpolymer. Selected resonances are shown from the region of the 19 F spectrum containing signals from the diastereotopic CF2 groups of the polymer. Resonance assignments can be found in reference 37. The peaks in the region displayed in Fig. 6a are predominantly from AB patterns. The slight decay of the signal might arise from T2 relaxation or from J-modulation because of smaller unresolved three- and four-bond homonuclear couplings. These signals are not significantly modulated by J-coupling in any part of the region from which typical δ values might be chosen. The peaks in the region displayed in Fig. 6b are predominantly from AM patterns.

Figure 6. Stacked spectra of selected regions from the 470-MHz 19 F DOSY spectra of poly(VDFter -TFEter -HFP) terpolymer from the experiment with constant gradient pulse area and increasing array of δ ; values for each array element from left to right are: ( δ (ms)/gradient amplitude(mT/m)0.4/123, 0.8/ 62, 1.2/41, 1.6/31, 2.0/24.6, 2.4/20.5, 2.8/17.6, 3.2/15.4, 3.6/13.7, 4.0/12.3, 4.4/11.2, 4.8/10.2, 5.2/9.4, 5.6/8.8, 6.0/8.2, 6.4/7.7, 6.8/7.2, 7.2/6.8, 7.6/6.5 and 8.0/6.2. a) Dbppste\_led, resonances of AB spin systems near  110 to  112 ppm; and b) Dbppste\_led, resonances of AM systems with resonances near  117 to  119 ppm. The insets show expansions from the normal 19 F 1D-NMR spectrum for the respective array plots.

<!-- image -->

The decay of the signal is attributed to J-modulation from 2 J FF. Optimal conditions for performing DOSY experiments include selection of a δ value consistent with δ = n / 2 × 2 JFF, where n =0, 2, 4, … .

These results imply that when diastereotopic CF2 fluorines are present, optimal gradient times will depend on factors such as solvent, B0 and other factors that might affect the chemical shift differences. It is recommended that an experiment be performed in which δ is arrayed, while maintaining a constant gradient pulse area, to determine optimal gradient times. It might not be possible to find conditions in which a single gradient time provides reasonable intensities for all of the fluorine resonances in a single DOSY experiment unless the gradients are stable and intense enough to use very short gradient pulses; δ =0.4ms seems to work in most cases. Once the optimal value of δ is determined, the gradient level range and Δ can be adjusted to obtain suitable decay curves for calculating DOSY spectra. If short intense gradients are not stable, it becomes necessary to perform experiments with δ values giving high intensities for the peaks of interest in the constant gradient pulse area array experiment.

## Chemical shift range

A version of the Dbppste\_led with WURST adiabatic pulses substituted for simple 180° pulses was developed specifically to address the problems associated with exciting the large spectral windows required to study the large chemical shift range of fluorinated materials with CF, CF2 and CF3 resonances. For comparison, a version of the sequence using simple 90°x -180°y -90°x composite pulses was incorporated into the same pulse sequence program. The three will be designated as simple 180° (Fig. 2b), composite 180° (Fig. 2e) and adiabatic 180° (Fig. 2d) DOSY experiments. Some of the results from these three experiments, along with a plot of the simple 19 F 1D-NMR experiment, are shown in Fig. 7, where the first increments from these experiments (obtained with the lowest gradient amplitude) are plotted in Figs. 7a -c. Experiments were performed with delays optimized to eliminate problems from large homonuclear J couplings, as described above. Because of the limited utility of the other sequences for reducing problems with very large J couplings, none of the other sequences were evaluated for their ability to cover large spectral windows.

<!-- image -->

Whenthe spectra are examined it is found that the signals of CF3 and CF resonances near the left and right edges of the DOSY spectra collected with simple 180° pulses (Fig. 7a) are considerably attenuated when compared with the resonances of the CF2 groups. In fact the CF resonance near  214ppm is barely detected. The signals of CF3 and CF resonances near the left and right edges of the DOSY spectra collected with composite 180° pulses (Fig. 7b) are considerably more intense when compared with the corresponding resonances in Fig. 7a. All the resonances in the first increment of the DOSY spectrum collected with adiabatic 180° pulses (Fig. 7c) have essentially recovered their full intensities compared with their intensities seen in the simple 19 F 1D-NMR spectrum (Fig. 7d).

The peak-containing regions from the full DOSY 2D-NMR spectra of the small molecule mixture are plotted in Fig. 8. The bottom three panels (Fig. 8d) were obtained from three separate experiments, with three different transmitter offsets centered in the CF3, CF2 and CF regions, using the Dbppste\_led pulse sequence in the Fig. 2b. These three spectra were collected using simple 180° pulses to obtain a benchmark of what the diffusion data should be. Values of 2.5 × 10  9 , 2.6 × 10  9 and 3.4 × 10  9 m 2 /s were obtained for FO, TFMB and HFB, respectively. Figure 2a shows the peak-containing regions from a single DOSY spectrum collected with adiabatic 180° pulses. Excellent results are obtained that are comparable to the data observed in Fig. 8d, collected from three separate standard DOSY experiments.

Figure 8b shows the results from the experiment performed with composite 180° pulses. The diffusion behavior of the signals in the CF2 region are reasonably well behaved, and the D values obtained match those from the DOSY spectra in Figs. 8a and 8d. However the D values for the CF3 group of TFMB fall at significantly lower value (D ≈ 2.0 × 10  9 m 2 /s) than those found in Figs. 8a and 8d. The D value for the CF resonance of HFB is higher (D ≈ 3.5 × 10  9 m 2 /s) than those measured for the CF2 resonances of HFB in the same spectrum, and those measured for the same resonance in Figs. 8a and 8d.

Figure 7. 564-MHz 19 F NMR spectra from the mixture of small molecules: a -c) first increment from DOSY experiments using Dbppled\_ad sequence and 7.7μ s 90° pulses; and d) simple 19 F 1D-NMR spectrum collected with a 3.0μ s (35°) pulse; a) DOSY using simple 180° pulses; b) DOSY using 90°x -180°y -90°x composite pulses; and c) DOSY using WURST adiabatic refocusing pulses. The RF transmitter was positioned at  139.21 ppm.

<!-- image -->

<!-- image -->

Figure 8. Peak containing regions from the 564-MHz 19 F DOSY 2D-NMR spectra of the small molecule mixture collected with: a) adiabatic 180° pulses; b) composite 180° pulses; c) simple 180° pulses; d) simple 180° pulses. Spectra (a -c) were collected with the transmitter offset positioned at  139.21 ppm. Spectra in (d) were collected in three separate experiments, from left to right, with the transmitter positioned in the CF3 (at  74.35 ppm), CF2 (at  124.92 ppm) and CF (at  213.92 ppm) regions.

<!-- image -->

Figure 8c shows the results from a single experiment with simple 180° pulses used to cover the entire chemical shift range. None of the D values match the correct values obtained from Figs. 8a and 8d (described above). The signal from the CF group is not even detected. This is because of resonance offset effects; the CF 2 signals are as far as 15 kHz from the transmitter. The 15μ s 180° pulse should only be effective over a range +10 kHz from the transmitter. The large resonance offset leads to incomplete refocusing of the magnetization during the gradient encoding periods and dramatically reduces signal-to-noise levels in the spectra in Figs. 8b and 8c.

So far only the influence of the effectiveness of the inversion pulse on the quality and validity of the DOSY data has been discussed. The adiabatic sequence gives good quality data and accurate diffusion coefficients for the resonances over the entire frequency range of 95 kHz. However, the effect of the 90° pulse width has not been addressed. Reasonable results have been obtained even though the 7.7μ s 90° pulse used should only provide a relatively uniform B1 RF field over the middle half of the spectral window. Therefore, the effect of deliberately setting the 90° pulse to lower values was studied; Table 1. summarizes these results.

Column 2 summarizes the signal-to-noise ratios (S:N) for the most intense CF3 resonance in the first increment (most intense data file) of the DOSY data. The S:N for this peak falls slowly until the pulse flip angle drops below 60°. At 45° the S:N drops by almost an order of magnitude. This is to be expected because after two 45° pulses flanking the first gradient encoding period, all of the magnetization is in the transverse plane and is destroyed by the homospoil gradient pulses. The DOSY processing package could not produce calculated D values in the experiment in which 90 0 pulses were all replaced by 45° pulses. However, reasonable D values across the whole spectral window were obtained with pulses that produced flip angles as small as 60°. The values for D were all in agreement within the expected 1 -2% error of the experiments.

Table 1. Summary of DOSY results for HFB in the small molecule mixture, with deliberate substitution of 90° pulses with shorter pulses; adiabatic refocusing pulses were used.

|                            |          | Diffusion coefficient (D, 10  10 m 2 s  1 )   | Diffusion coefficient (D, 10  10 m 2 s  1 )   | Diffusion coefficient (D, 10  10 m 2 s  1 )   |
|----------------------------|----------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| Pulse width (degrees/ μ s) | S:N      | CF 3                                          | CF 2                                          | CF                                            |
| 90°/7.70                   | 17 400:1 | 34.0                                          | 33.6                                          | 32.8                                          |
| 80°/6.84                   | 16 100:1 | 34.2                                          | 33.6                                          | 33.5                                          |
| 70°/5.99                   | 12 800:1 | 33.8                                          | 33.4                                          | 33.1                                          |
| 60°/5.13                   | 8200:1   | 33.8                                          | 33.3                                          | 33.1                                          |
| 45°/3.85                   | 2400:1   | - a                                           | - a                                           | - a                                           |
| a not calculated           |          |                                               |                                               |                                               |

## Polymer analysis

Below we describe applications of the new adiabatic DOSY pulse sequence to the characterizations of poly(CTFEco -VDC) and (poly (VDFco -DFAA) copolymers. Poly(CTFEco -VDC) copolymer has been investigated for use as barrier films in packaging applications. [38] Poly(VDFco -DFAA) copolymer has been investigated for its potential to provide functionalized poly(VDF) polymers. [44]

NMR parameters such as DOSY diffusion coefficients, obtained from polymers, represent the statistical average from a distribution of molecules having different molecular weights. When these parameters are measured using the polymer chain-end resonances they are determined by the number average molecular weight (Mn). When these parameters are measured using the backbone resonances, they are determined by the weight average molecular weight (Mw). [13] For polymers with a MW distribution Mw &gt; Mn, and consequently, D measured from polymer backbone resonances will be lower than D measured from polymer chain end resonances. This is a consequence of using a single exponential to fit a multiexponential decay; the resonances from different molecular weight fractions of the polymer have the same chemical shift, although different exponential decay constants (because of different D values) in the DOSY experiment. Fitting the data to a single exponential artificially increases the apparent D value of the end groups.

Based on this concept, DOSY has been used to distinguish between the chain-end and backbone (including short chain branches) of fluorinated polymers, in particular poly(VDF), [40] poly (VDFcoTFE) [41] and poly(VDFcoHFP) [42] (co)polymers. Similar spectroscopic and compositional characteristics are expected for poly(CTFEco -VDC) and poly(VDFco -DFAA) copolymers. Poly(CTFEco -VDC) and poly(VDFco -DFAA) copolymers exhibit the NMR spectral characteristics that create the types of problems in DOSY experiments which the methods described above are designed to address. In particular, the Cl and COOH branch sites (and CHF centers in DFAA) create stereogenic centers along the polymer backbone which cause the adjoining CF2 fluorines to become diastereotopic. In many cases, AM or AX patterns from these diastereotopic CF2 groups create issues in detecting their resonances in DOSY spectra. Furthermore, these copolymers have 19 F NMRresonances which span a large chemical shift range, especially in the spectra of the poly(VDFco -DFAA) copolymers which have CF and CF2 resonances that span a 120-ppm chemical shift range.

<!-- image -->

Poly(1-chloro-1,2,2-trifluoroethylene-co-vinylidene chloride) copolymer.

Scheme 1 shows the reaction for the preparation of poly(CTFEco -VDC). The random copolymer was prepared by radical polymerization of CTFE and VDC initiated by t-butylperoxypivalate (TBPPi). [38] This initiator decomposes to form t-butoxy and t-butyl radicals as the initiating species. These species can add to both comonomers in either of two positions. This gives eight different possibilities for the initiation ends of the polymer if only the structure of the first monomer unit is considered.

Propagation involves insertions of VDC and CTFE comonomers via normal and inverse additions into the polymer chain to form a variety of monomer sequences along the backbone of the polymer chain. [38] Termination of the polymerization is expected to occur via recombination of macroradicals. [51] We are in the early stages of work to completely characterize the resonances of this polymer. It would be a useful aid to sort resonances based on D values in order to identify and separate resonances of backbone structures from those of chain end structures. DOSY provides the means of distinguishing the resonances of chain-end groups from the rest of the resonances in copolymers.

Figure 9a shows the peak containing region from the 470-MHz 19 F 1D-NMR spectrum of the poly(CTFEco -VDC) copolymer. The

Scheme 1. Preparation of poly(CTFEco -VDC) copolymer.

<!-- image -->

Figure 9. Selected regions from the 470-MHz 19 F NMR spectra of poly (CTFEco -VDC) copolymer: a) normal 1D-NMR spectrum; and b and c) stacked spectra of the resonances from AM and AB spin systems in the  107 to  112 ppm region (b) and  112 to  115 ppm region (c), respectively from the DOSY experiment with constant gradient pulse area and increasing array of δ . Values for each array element from left to right are: ( δ (ms)/gradient amplitude (mT/m) 0.4/123, 0.8/62, 1.2/41, 1.6/31, 2.0/ 24.6, 2.4/20.5, 2.8/17.6, 3.2/15.4, 3.6/13.7, 4.0/12.3, 4.4/11.2, 4.8/10.2, 5.2/9.4, 5.6/8.8, 6.0/8.2, 6.4/7.7, 6.8/7.2, 7.2/6.8, 7.6/6.5 and 8.0/6.2. The null and maxima points at n / (2 × J FF ) ( n =1, 2, 3, … ) in the J =280-Hz modulation curve are indicated by the arrows across the bottom.

<!-- image -->

<!-- image -->

19 F chemical shifts of CF and CF2 resonances normally fall in distinctive regions. However, because of similar electronegativities of F and Cl, the CFCl and CF2 resonances are very similar and fall within the  115 to  130ppm and  100 to  120-ppm regions, respectively. Many of the resonances in the  115 to  125-ppm region arise from diastereotopic CF2 fluorines of groups adjoining CFCl centers. The relatively narrow chemical shift range makes it possible to perform DOSY experiments on this polymer without resorting to pulse sequences which use composite or adiabatic refocusing pulses.

Figures 9b and c show selected regions from the DOSY spectra obtained by arraying the δ gradient pulses while maintaining a constant gradient pulse area. These regions show two representative behaviors of the signal modulations from AM and AB patterns of diastereotopic CF2 groups. Selection of the correct δ delay is not critical for many of the CF2 groups. However, for a number of the CF2 resonances, patterns similar to those in Fig. 9b are observed, and selection of δ in the range of 3.2 ms is essential to avoid losing these signals.

Figure 10. 470-MHz DOSY spectrum of poly(CTFEco -VDC) copolymer (CTFE:VDC = 54:46 mol/mol) in CDCl3 obtained at 50 °C.

<!-- image -->

Scheme 2. Radical copolymerization of VDF with DFAA initiated by TBPPi ( t -butyl peroxypivalate).

<!-- image -->

Figure 10 shows the 470-MHz DOSY spectrum of poly(CTFE-coVDC) copolymer obtained using the Dbppled pulse sequence and simple 180° refocusing pulses. A plot of the corresponding region from the simple 19 F 1D-NMR spectrum appears across the top of the DOSY spectrum for comparison of the chemical shifts. Most resonances exhibit DOSY cross-peaks corresponding to D ≈ 8×10  10 m 2 /s. A few of the resonances in the  110 to  112-ppm region which exhibit AM coupling patterns, appear to have somewhat larger D values, and might be attributed to chainend resonances. These resonances are also sharper than most of the other resonances in the spectrum. This is consistent with their assignment to chain-ends as the fluorines in these groups would be expected to have longer T2 values than those of the polymer backbone fluorines. The copolymer has previously been found to contain a 3:1 ratio of CTFE:VDC. [38] Hence, it might be reasonable to assume that this group of peaks, which appears to form an AM pattern is from the diastereotopic CF2 groups of CTFE units at the polymer chain-end. It is assumed that the small but not negligible peak near  106ppm with D ≈ 1×10  10 m 2 /s is from poly(CTFE). Because VDC is more reactive than CTFE, after all the VDC is consumed, the remaining CTFE can homopolymerize.

## Poly(vinylidene fluoride-co-1,2-difluoroacrylic acid) copolymer

The preparation of poly(VDF-co-DFAA) copolymer, also initiated by TBPPi, has been reported (Scheme 2). [44] It is of interest as a means of preparing functionalized VDF-based elastomers, and graft copolymers. The copolymerization proceeds in a manner similar to that of CTFE with VDC described above. The complete study of monomer- and stereo-sequence structures in this polymer is underway. The major resonances are attributed to triad monomer sequences of VDF and DFAA units. However, there are many weak resonances that might arise from polymer chain-ends, or from low probability monomer sequences such as those from monomer inversions of VDF and DFAA. Identification of chain-end resonances with the aid of DOSY experiments would be useful for MW determinations, for mechanistic studies and for determining the possibility of reactive chain-ends. DOSY experiments would thus certainly help with efforts to completely characterize the structures present in this copolymer and to assign all of its resonances.

This polymer has both CF (without other electronegative substituents) and CF2 resonances so the large chemical shift range is expected to require special considerations. In addition, the CF2 groups in VDF units formed from normal addition are adjoining stereogenic centers and are expected to produce AB-AX patterns from diastereotopic fluorines, and will give rise to the same issues produced by large homonuclear couplings encountered with VDF units adjoining HFP and CTFE units in the polymers discussed above.

Figure 11. Peak containing regions from the 564-MHz 19 F DOSY spectrum of poly(VDF-co-DFAA) copolymer (VDF:DFAA ca. 60:40 mol/mol) copolymer obtained with Dbppled\_ad sequence using adiabatic refocusing pulses, δ =2.8 ms, Δ =40ms; other parameters are given in the experimental section. Corresponding regions from the 564-MHz 19 F 1D-NMR spectrum are plotted across the top of the spectrum.

<!-- image -->

From an arrayed experiment in which δ was increased while maintaining constant gradient pulse areas, it was determined that optimum conditions for detecting DOSY peaks from resonances of AX spin systems included δ =2.8ms. Figure 11 shows the 19 F DOSY spectrum of poly(VDFco -DFAA) copolymer obtained on a 600-MHz spectrometer. All of the intense resonances, and some of the weaker signals fall along a line with D ≈ 5.5 × 10  10 m 2 /s. These are attributed to the polymer backbone structures. Numerous weak resonances with DOSY cross-peaks at larger D values are attributed to the structures at the polymer chain ends.

## Conclusions

A new pulse sequence for obtaining DOSY spectra is presented which uses adiabatic refocusing pulses. It is evaluated, relative to other sequences, for collecting DOSY data on samples with 19 F resonances spanning a large chemical shift range and for addressing issues arising from large homonuclear couplings. Optimum conditions are evaluated using perfluorinated small molecules and highly fluorinated copolymers.

It has been found that when large homonuclear couplings are present and when the resonances of the analyte are spread over a large spectral window that: (1) the DOSY pulse sequence with adiabatic pulses gives optimum results; (2) the experiments give reliable results without significant loss of signal to noise when the 90° pulses are replaced with pulses as small as 60°; and (3) an additional setup step is needed in which the signal is monitored as a function of increasing gradient delay, while maintaining a constant gradient pulse area so that gradient encoding times do not produce null points for signals with large homonuclear couplings.

While the optimal conditions have been demonstrated with 19 F DOSY experiments on highly fluorinated molecules, they should also be relevant to DOSY experiments with detection of other heteronuclei such as 31 P or 195 Pt, where both large chemical shift ranges and large homonuclear J couplings are typically present.

## Acknowledgements

Wewish to acknowledge the support of The Ohio Board of Regents and The National Science Foundation (CHE-0341701 and DMR0414599) for funds used to purchase the NMR instrument used for this work. We thank the National Science Foundation (DMR0905120), National Science Foundation of China (21305098), E. I. du Pont de Nemours and Co. and Honeywell International Co. for their support of this work. We also wish to thank the staff members of the Magnetic Resonance Centers at the University of Akron and Soochow University for their help in maintaining the instruments used for this work.

## References

- [1] K. F. Morris, C. S. Johnson Jr. J. Am. Chem. Soc. 1992 , 114 (8), 3139 -3141.
- [2] B. Antalek. Concepts Magn. Reson. 2002 , 14 , 225 -258.
- [3] W. S. Price. Resonance 1997 , 9 , 299 -336.
- [4] W. S. Price. Concepts Magn. Resonance 1998 , 10 , 197 -237.
- [5] C. S. Johnson Jr. Prog. Nucl. Magn. Reson. Spectrosc. 1999 , 34 , 203 -256.
- [6] G. A. Morris, in Encyclopedia of Nuclear Magnetic Resonance , vol. 9 (Eds: D. M. Grand, R. K. Harris), 2002 , pp. 35 -44.
- [7] Y. Cohen, L. Avram, L. Frish. Angew. Chem. Int. Ed. 2005 , 44 , 520 -554.
- [8] T. Brand, E. J. Cabrita, S. Berger. Prog. Nucl. Magn. Reson. Spectrosc. 2005 , 46 , 159 -196.
- [9] D. Li, I. Keresztes, R. Hopson, P. G. Williard. Accts. Chem. Res. 2009 , 42 , 270 -280.
- [10] K. A. Heisel, J. J. Goto, V. V. Krishnan. Amer. J. Analyt. Chem. 2012 , 3 , 401 -409.
- [11] D. Jeannerat, J. Furrer. Comb. Chem. High Throughput Screen. 2012 , 15 , 15 -35.
- [12] A. Chen, D. Wu, C. S. Johnson Jr. J. Am. C hem. Soc. 1995 , 117 , 7965 -7970.
- [13] J. Vieville, M. Tanty, M.-A. Delsuc. J. Magn. Resonance 2011 , 212 , 169 -173.
- [14] W. Li, H. Chung, C. Daeffler, J. A. Johnson, R. H. Grubbs. Macromolecules 2012 , 45 , 9595 -9603.
- [15] N. E. Kuz ' mina, S. V. Moiseev, V. I. Krylov, V. A. Yashkir, V. A. Merkulov. J. Analytical Chem. 2015 , 70 , 843 -849.
- [16] S. Auge´, P.-O. Schmit, C. A. Crutchfield, M. T. Islam, D. J. Harris, E. Durand, M. Clemancey, A.-A. Quoineaud, J.-M. Lancelin, Y. Prigent, F. Taulelle, M.-A. Delsuc. J. Phys. Chem. B 2009 , 113 , 1914 -1918.
- [17] P. Lewinski, S. Sosnowski, S. Kazmierski, S. Penczek. Polym. Chem. 2015 , 6 , 4353 -4357.
- [18] L. Avram, Y. Cohen. Chem. Soc. Rev. 2015 , 44 , 586 -602.
- [19] F. B. T. Pessine, A. Calderini, G. L. Alexandrino. Magn. Resonance Spectrosc. 1 ed. Rijeka: In. Tech. 2012 , 1 , 237 -264.
- [20] A. Maccioni, G. Ciancaleoni, C. Gianluca, D. Zuccaccia. Supramol. Chem.: From Molecules to Nanomaterials 2012 , 2 , 319 -330.
- [21] U. Holzgrabe, M. Malet-Martino. Pharm. Biomed. Analysis 2011 , 55 , 679 -687.
- [22] N. G. Stahl, C. Zuccaccia, T. R. Jensen, T. J. Marks. J. Am. Chem. Soc. 2013 , 125 , 5256 -5257.
- [23] D. Li, I. Keresztes, R. Hopson, P. G. Williard. Acc. Chem. Res. 2009 , 42 , 270 -280.
- [24] C. A. Crutchfield, D. J. Harris, J. Magn. Resonance 2007 , 185 , 179 -182.
- [25] D. Li, G. Kagan, R. Hopson, P. G. Williard. J. Am. Chem. Soc. 2009 , 131 , 5627 -5634.
- [26] W. Li, G. Kagan, H. Yang, C. Cai, R. Hopson, D. A. Sweigert, P. G. Williard. Org. Lett. 2010 , 12 , 2698 -2701.
- [27] M. Sebban, L. Guilhaudis, H. Oulyadi, in Lithium Compounds in Organic Synthesis (Eds: R. Luisi, V. Capriati), 2014 , pp. 85 -121.
- [28] G. Kagan, W. Li, R. Hopson, P. G. Williard. Org. Lett. 2010 , 12 , 520 -523.
- [29] O. Segev, I. Columbus, Y. Ashani, Y. Cohen. J. Org. Chem. 2005 , 70 , 309 -314.
- [30] E. Martinez-Viviente, H. Ruegger, P. S. Pregosin, J. Lopez-Serrano. Organometallics 2002 , 21 , 5841 -5846.
- [31] C. Dalvit, A. Vulpetti. Magn. Resonance Chem. 2012 , 50 , 592 -597.
- [32] G. Dal Poggetto, D. C. Favaro, M. Nilsson, G. A. Morris, C. F. Tormena. Magn. Resonance Chem. 2014 , 52 , 172 -177.
- [33] E. B. Twum, X. Li, E. F. McCord, P. A. Fox, D. F. Lyons, P. L. Rinaldi, in Advances in Fluorine-Containing Polymers . ACS Symposium Series, vol. 1106 (Eds: D. Smith, S. Iacono, C. Kettwich, D. Boday), American Chemical Society, Washington, D.C., 2012 , pp. 171 -185.
- [34] D. W. Smith Jr., S. T. Iacono, S. S. Iyer, Handbook of Fluoropolymer Science and Technology , John Wiley, Hoboken, NJ, 2014 .
- [35] B. Ameduri. Chem. Rev. 2009 , 109 , 6632 -6686.
- [36] F. Boschet, B. Ameduri. Chem. Rev. 2014 , 114 , 927 -980.
- [37] E. B. Twum, E. F. McCord, D. F. Lyons, P. L. Rinaldi. Macromolecules 2015 , 48 , 3563 -3576.
- [38] G. Lopez, C. Gao, L. Li, F. J. Wyzgoski, A. Thenappan, P. L. Rinaldi, B. Ameduri. Polymer Chem. 2015 , 6 , 3790 -3799.
- [39] X. Li, J. Baughman, C. Gao, L. Li, F. J. Wyzgoski, P. L. Rinaldi, E. B. Twum, E. F. McCord, in Multidimensional NMR of Fluoropolymers, in Handbook of Fluoropolymer Science and Technology (Eds: D. W. Smith Jr., S. T. Iacono, S. S. Iyer), John Wiley, Hoboken, NJ, 2014 Ch. 24, pp. 565 -598.
- [40] E. B. Twum, C. Gao, X. Li, E. F. McCord, P. A. Fox, D. F. Lyons, P. L. Rinaldi. Macromolecules 2012 , 45 , 5501 -5512.
- [41] L. Li, E. B. Twum, X. Li, E. F. McCord, P. A. Fox, D. F. Lyons, P. L. Rinaldi. Macromolecules 2013 , 46 , 7146 -7157.
- [42] E. B. Twum, C. Gao, X. Li, E. F. McCord, P. A. Fox, D. F. Lyons, P. L. Rinaldi. Eur. Polym. J. 2014 , 51 , 136 -150.
- [43] A. Jerschow, N. Muller. J. Magn. Resonance 1997 , 125 , 372 -375.

<!-- image -->

<!-- image -->

- [44] F. Boschet, J.-M. Cracowski, V. Montembault, B. Ameduri. Macromolecules 2010 , 43 , 4879 -4888.
- [45] D. H. Wu, A. D. Chen, C. S. Johnson. J. Magn. Resonance, Ser. A 1995 , 115 , 260 -264.
- [46] A. Botana, J. A. Aguillar, M. Nilsson, G. A. Morris. J. Magn. Reson. 2011 , 208 , 270 -278.
- [47] E. Kupce, R. Freeman. J. Magn. Resonance Ser. A 1995 , 115 , 273 -276.
- [48] R. D. Boyer, R. Johnson, K. Krishnamurthy. J. Magn. Resonance, 2003 , 165 , 253 -259.
- [49] B. Adams. Magn. Resonance Chem. 2008 , 46 , 377 -380.
- [50] M. H. Levitt, R. Freeman. J. Magn. Resonance 1979 , 33 , 473 -476.
- [51] R. Timmerman, W. J. Greyson. Appl. Polym. Sci. 1962 , 6 , 456 -460.

## Supporting Information

Additional supporting information may be found in the online version of this article at the publisher ' s web site.