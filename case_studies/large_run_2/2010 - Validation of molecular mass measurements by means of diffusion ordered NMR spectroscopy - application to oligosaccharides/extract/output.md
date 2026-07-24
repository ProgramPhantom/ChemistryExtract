<!-- image -->

## Full paper/Me ´moire

## Validation of molecular mass measurements by means of diffusion-ordered NMR spectroscopy: Application to oligosaccharides

Olivier Assemat a , Marie-Aude Coutouly a , Redouane Hajjar a,b , Marc-Andre ´ Delsuc c, *

- a NMRTEC, boulevard Sebastien-Brandt, Bioparc, ba ˆtiment B, 67400 Illkirch Graffenstaden, France
- b Tectospin, institut Lavoisier, UMR 8180, universite ´ de Versailles-Saint-Quentin-en-Yvelines, 45, avenue des E ´ tats-Unis, 78035 Versailles cedex, France

c Institut de ge ´ne ´tique et de biologie mole ´culaire et cellulaire, BP 10142, 67404 Illkirch cedex, France

A R T I C L E I N F O

Article history: Received 4 May 2009 Accepted after revision 7 October 2009

Available online 29 November 2009

Keywords: DOSY Molecular mass NMR

Oligosaccharides

## 1. Introduction - theory

The DOSY experiment, by separating on two different spectral axes the chemical shift information and the translational diffusion information, is a powerful analytical tool for solution analysis. The possibility of estimating molecular masses by DOSY has recently been investigated in terms of the fractal dimension of the diffusing species [1]. In this work, it is proposed to estimate the molecular mass M of a molecule of interest from its translational diffusion coefficient, by the following relation:





$$M = \left ( \frac { C _ { r } } { D _ { r } } \right ) ^ { d _ { F } } & & ( 1 ) & \text {alone} & \text {diff}$$

where dF is the fractal dimension of the molecular family, Dr is the diffusivity (ratio of diffusion coefficients of the molecule of interest and of the reference molecule) and Cr a calibration constant. Both Cr and dF have to be determined

*

Corresponding author. E-mail address: delsuc@igbmc.fr (M.-A. Delsuc).

A B S T R A C T

The validation of molecular mass measurements by using DOSY spectrocopy is presented. A mixture of oligosaccharides has been studied and an extended model has been used. A method has been proposed and applied to correct the imperfections due either to the lock system or the room temperature regulator.

ß 2009 Acade ´mie des sciences. Published by Elsevier Masson SAS. All rights reserved.

experimentally. The reference molecule is usually the solvent residual signal, or some additional small non interacting molecule. In this work, we present an optimisation of the DOSY experiment data processing which allows anaccuratemassestimateusingEq.(1),aswellasasoftware implementation of the complete procedure.

## 2. Mass determination

Equation (1) can be easily used to determine molecular masses from a diffusion experiment. In a DOSY spectrum, each compound is displayed by its 1D spectrum located along the vertical axis at its diffusion coefficient value. The diffusivity Dr of each species is determined by taking the ratio of the diffusion coefficients of the species of interest and of the reference molecule. Inversion of Eq. (1) gives then an estimate of the molecular mass, provided that the reference values Cr and dF characteristic of the molecule and of the physical conditions, are known. In Auge ´ et al. [1], reference values are given for several molecular famillies (PolyMethylMetacrylate, PolyEthyleneOxyde, PolyStyrene, OligoSaccharides, Globular Proteins, DNA, linear alcanes) in various solvent (HDO, THF, acetone, toluene or CDCl3).

Contents lists available at ScienceDirect

## Comptes Rendus Chimie

www.sciencedirect.com

<!-- image -->

Fig. 1. Using DOSYtoMW, one first draws a line for each species to be analyzed, and a line for the reference molecule (HDO). One then chooses the molecular family and the solvent. Finally, the program provides the mass estimates and the error bars.

<!-- image -->

Additionally, this work provides a mean to estimate the uncertainty on the molecular mass from the experimental uncertainties.

A procedure called DOSYtoMW written in python, as been implemented in the NMRnotebook TM [2] and provides an easy access to this method. This program runs in graphical mode and results are displayed in a dialog box (Fig. 1).

The quality of the molecular mass measurement is closely related to the accuracy of the diffusion coefficient values. This means that the NMR experiment must be realized in best conditions. Unfortunately, in spite of the precautions taken by the experimenter, it is common to observe different perturbations due either to the lock system or the room temperature regulator. The instability of such systems leads to poor 2D spectra: generally, chemical shift variations are observed in the indirect dimension F1. The signals shown in Fig. 2 demonstrate the effect of such perturbations. We have developed a method which corrects these imperfections. The proposed method is based on three steps. (1) In the first step, for each 1D row, a peak-picking is done over a small region which contains one signal (ideally, with high signal to noise ratio and coming from a slowly diffusing species). A peak-picking determined from the maximum of a over-zero-filled spectrum was chosen, as it seems to be the best method for small shifts to be estimated accurately. (2) In the second step, the shift from the reference is estimated, the chemical shift of the first row being used as a reference. (3) In the last step, the spectrum is corrected by shifting the whole spectrum. The dataset shift is performed in the time domain by multiplying the reconstructed FID with a complex frequency. This reconstructed FID being obtained with a causality preserving inverse Fourier transform. This procedure has already been described in [3] and used for shearing. The result is shown in Fig. 3 and the signals demonstrate its efficiency.

Fig. 2. Before correction: imperfections caused by the room temperature regulator. The lock was done on the solvent signal (HDO on the left). Along the indirect dimension, chemical shift variations are observed for the other signals (on the right).

<!-- image -->

Fig. 3. After correction: now the chemical shift of the solvent varies whereas the chemical shift of the other signals remains stable.

<!-- image -->

## 3. Application to oligosaccharides

A mixture of glucose (93 mM), sucrose (26 mM), raffinose (13 mM), and b -cyclodextrin (30 mM) was prepared (all purchased from Sigma) in D2O (Eurisotop).

DOSYspectra were acquired at room temperature using LED [4] pulse sequence with bipolar field gradients [5] on a Bruker Avance I 400 MHz spectrometer equipped with a 5 mm QNP probehead and a field gradient accessory delivering z-field gradients up to 53.5 G/cm. Sequence delays were D = 100 ms (diffusion delay), D /2 = 2 ms (gradient duration) and Te = 5 ms (LED) recovery delay. For each data set, 4096 complex points were collected in eight scans, for each 40 experiments in which the gradient strength was linearly incremented from 1.0 to 47.5 G/cm. A 1.5 s recycle delay was used between scans. The spectral axis was processed with an exponential multiplication prior to Fourier transform, which was applied in order to obtain 2048 real points. The procedure described in section 2 was then applied. The diffusion dimension was obtained by performing an inverse Laplace transform using the maximumentropytechnique [6]. The DOSY reconstruction was realized with 256 points in the diffusion dimension.

The DOSYtoMW procedure was finally applied in order to estimate the molecular weight of each constituent of the oligosaccharides mixture. An error bar of 5% on measured diffusion coefficients was used.

Those results are summarized in Table 1.

From this table, it can be seen that the molecular mass estimation method used here allows to determine unambiguously the number of monosaccharide units for oligosaccharides up to seven units, since the error calculated for the 1 -cyclodextrin is close to the molecular weight of one sugar unit.

Table 1 values of molecular mass.

| Molecule         |   Theoretical mass | Experimental determined mass with initial model   | Experimental determined mass with extended model   |
|------------------|--------------------|---------------------------------------------------|----------------------------------------------------|
| Glucose          |              180.2 | 214  48                                                   | 201  43                                                    |
| Sucrose          |              342.3 | 378  82                                                   | 357  76                                                    |
| Raffinose        |              504.4 | 530  117                                                   | 500  105                                                    |
| b -cyclodextrine |               1135 | 1080  233                                                   | 1040  219                                                    |

## 4. Model extension

The molecular weight estimate proposed in [1] for oligosaccharides and used here is based on the work by Viel et al. [7] and was determined on large oligosaccharides with molecular masses ranging from 5.8 to 853 kDa, very different from that presented here. The fact that the molecular masses estimated with this model are correct is a token of the robustness of the model and of the DOSY approach for molecular mass determination.

In return, the newly determined value of diffusion have been used to extend and strengthen the model for low masses. This extended model is now available in the presented software, as well as in the reference web application available at http://abcis.cbs.cnrs.fr/MW/. With this extended model, it can be seen (Table 1) that the mass determination is significantly improved, and the error bars reduced.

## 5. Conclusion

In conclusion, we have shown that the molecular mass can be estimated by using the DOSY spectroscopy and the extended model. The efficiency of this method and this model is demonstrated through the study of a mixture of oligosaccharides. This new model provides significant improvements in the measurement of molecular mass. We have also shown that our method which corrects the perturbations due either to the lock system or the room temperature regulator, contributes to this improvement. This method is related to the FIDDLE technique proposed by Morris et al. [8] and its improvement [9] which corrects for any kind of global spectrometer perturbations such as phase of shim. The method proposed here, while being much simpler in its implementation, appears to be very efficient on the special case of slight temperature instabilities, which in the case of D2O lock creates a global shift of the spectrum.

## References

- [1] S. Auge, P.O. Schmit, C.A. Crutchfield, M.T. Islam, D.J. Harris, E. Durand, M. Clemancey, A.A. Quoineaud, J.M. Lancelin, Y. Prigent, F. Taulelle, M.A. Delsuc, J. Phys. Chem. B. 113 (2009) 1914.
- [2] NMRTEC SA, Illkirch France, http://www.nmrtec.com/software/nmrnotebook.html.
- [3] D. Tramesel, V. Catherinot, M.A. Delsuc, J. Magn. Reson. 188 (2007) 56.
- [4] S. Gibbs Jr., C. Jonhson, J. Magn. Reson. 93 (1991) 395.
- [5] D. Wu, A. Chen, C. Jonhson, J. Magn. Reson. Ser. A. 115 (1995) 260.
- [6] M.-A. Delsuc, T. Malliavin, Anal. Chem. 70 (1998) 2146.
- [7] S. Viel, D. Capitani, L. Mannina, A. Segre, Biomacromolecules 4 (2003) 1843.
- [8] G.A. Morris, H. Barjat, T.J. Home, Prog. Nucl. Magn. Reson. Spectrosc. 31 (1997) 197.
- [9] R. Huo, R. Wehrens, L.M.C. Buydens, J. Magn. Reson. 169 (2004) 257.