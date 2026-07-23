## NMR Measure of Translational Diffusion and Fractal Dimension. Application to Molecular Mass Measurement

Sophie Auge ´, † Pierre-Olivier Schmit, † Christopher A. Crutchfield, ‡ Mohammad T. Islam, ‡ Douglas J. Harris, ‡ Emmanuelle Durand, § Martin Clemancey, | Anne-Agathe Quoineaud, § Jean-Marc Lancelin, | Yann Prigent, ⊥ Francis Taulelle, ¶ and Marc-Andre ´ Delsuc* ,†,#

Centre de Biochimie Structurale, CNRS UMR 5048 - UM 1 - INSERM UMR 554, 29, rue de Na V acelles, 34090 Montpellier Cedex, France, Cytec Industries, Inc., 1937 West Main Street, Stamford, Connecticut 06902, Institut Franc ¸ais du Pe ´trole, Rond Point de l'e ´changeur de Solaize, BP 3, 69360 Solaize, France, Uni V ersite ´ de Lyon, Uni V ersite ´ Claude Bernard - Lyon 1, Sciences Analytiques, CNRS UMR 5180, domaine scientifique de la Doua, ESCPE-Lyon, 69622 Villeurbanne, France, Toulouse Uni V ersity, SFTCM FR 2599 - Uni V ersite ´ Paul Sabatier 118, route de Narbonne, 31062 Toulouse cedex 9, France, and Tectospin, Institut La V oisier, UMR 8180 Uni V ersite ´ de Versailles Saint Quentin en Y V elines 45 A V enue des E ´ tats-Unis, 78035 Versailles Cedex, France

Recei V

ed: October 24, 2008

Experimental NMR diffusion measure on polymers and on globular proteins are presented. These results, complemented with results found in the literature, enable a general description of effective fractal dimension for objects such as small organic molecules, sugars, polymers, DNA, and proteins. Results are compared to computational simulations as well as to theoretical values. A global picture of the diffusion phenomenon emerges from this description. A power law relating molecular mass with diffusion coefficients is described and found to be valid over 4 orders of magnitude. From this law, the fractal dimension of the molecular family can be measured, with experimental values ranging from 1.41 to 2.56 in full agreement with theoretical approaches. Finally, a method for evaluating the molecular mass of unknown solutes is described and implemented as a Web page.

gyration radius R g of the molecule is related to the molecular mass though the δ parameter, also called the Flory exponent.

$$R _ { g } \, \infty \, M ^ { \delta }$$

It is usually considered that this Flory exponent is the inverse of the fractal dimension d F of the molecular chain:

$$d _ { _ { F } } = 1 / \delta$$

The fractal dimension is a notion that comes from the fractal theory and can be described as a measure of the way a fractal object fills-up the 3D space. A fractal dimension of 3 means that space is completely filled with no holes left, and a fractal dimension of 1 means that the molecule is purely onedimensional and extends linearly like a rigid rod. Intermediate values are found for molecules partially filling the empty space and are a measure of the compactness of the molecular fold.

The similarity between eqs 1 and 2 has prompted several authors to treat as equivalent quantities R and δ , either implicitly 3 or explicitly, 5,6 but with a lack of theoretical evidence.

The purpose of the present work is to explore how R and δ are related, by comparing, both experimentally and theoretically, the diffusion coefficient and the Flory exponent of molecules over a wide range of sizes and molecular types. Out of this study a more global view is proposed.

## Theory

Flory Exponent and Fractal Dimension. The Flory exponent δ (eq 2) can be experimentally measured from SAXS or

## Introduction

Translational self-diffusion of diluted solutes can be accurately measured by NMR, by using the Sketjal -Tanner approach. 1 The measurement of the attenuation of a spin echo in the presence of pulsed field gradients allows the measurement of the mean displacement of the diffusing species. The analysis of the signal decay relative to the varying parameter (usually the gradient intensity), gives access to the diffusion coefficient D characteristic of the molecular species present in the solution.

Using this technique, many authors have studied the variation of D over a range of molecular sizes for a given homogeneous family of molecules and have observed that a power law between D and the molecular mass M correctly describes the observed behavior.

$$D \, \infty \, M ^ { - \alpha }$$

This property has been used for instance to check the quality of the work 2 or to predict molecular masses from the diffusion coefficient measure. 3 -5

Equation 1 is reminiscent of a similar power law used in polymer chemistry to measure the way flexible molecules, such as polymers or proteins, extend. In the Flory equation, the SANS experiments. It can also be estimated from the modeling of a molecular chain by computing the variation of R g and mass when varying the size of the integration sphere over which they are calculated.

* Corresponding author. E-mail: MA.Delsuc@cbs.cnrs.fr.

† Centre de Biochimie Structurale, CNRS.

‡ Cytec Industries, Inc.

§ Institut Franc ¸ais du Pe ´trole.

| Universite ´ de Lyon.

⊥ Toulouse University.

¶ Institut Lavoisier.

# Moved to: IGBMC, 1 rue Laurent Fries, BP 10142, 67404 Illkirch, France.

The Flory theory 7 gives some limits to the value of δ that can be observed for a linear polymer, diluted over the overlap concentration, and long enough compared to its persistence length. In a poor solvent, the polymer chain tends to fold onto itself, minimizing the contact with the solvent, and the value of δ is 1 /3. In a good solvent, the polymer chain is fully solvated, to maximize the polymer -solvent interactions, and the exponent δ is predicted to be equal to 0.588. 8 In a Θ solvent, the polymer -polymer interactions are equal to the polymer -solvent interactions, the polymer chain behaves like a Gaussian chain, and the exponent δ is predicted to be equal to 1 / 2 .

The DOSY Experiment. The Stokes -Einstein law relates the translational self-diffusion coefficient D to the molecular size:

$$D = \frac { k T } { 6 \pi \eta R _ { H } } \quad ( 4 )$$

where k is the Boltzmann constant, T is the absolute temperature, η is the solvent viscosity, and R H is the hydrodynamic radius of the molecule. The hydrodynamic radius R H is quite different in nature from the gyration radius R g found in eq 2. It can be defined as the radius of the sphere that would diffuse at the same diffusion coefficient in the same conditions (Einstein, A. Annalen der Physiks (4), 19, (1906), pp. 289-306). Thus, it is not an intrisic characteristic of the molecule, but rather a way of expressing the diffusion in a manner independent from the physicochemical surrounding (temperature and viscosity).

There is no general relationship between both quantities. However, in the case of spheres, the obvious proportionality relationship R H ) 4 / 3 R g stands. Alternatively, the Kirkwood -Riseman approximation proposes R H ≈ 3 / 2 R g 9 for a random walk polymer.

Moreover, it should be noted that the R H parameter is of geometrical nature and that the mass of the diffusing molecules is not present in the Stokes -Einstein law. As a consequence, the relationship to molecular mass, as presented in eq 1, has to be made under the assumption that all the studied molecules in a series have similar chemical compositions and similar mass distributions. This is usually ensured when the molecules share the same chemical family. However, it could be a problem if heteratoms are present, or if hollow structures are studied.

Theoretical r and δ Values. Under these assumptions, several limit values of R can be easily computed for ideal geometrical cases. For spherical objects, the Stokes -Einstein equation is exact, and the hydrodynamic radius is the sphere radius. Thus, the exponent R is naturally 1 / 3 for a family of spheres of constant density. It is thus equivalent to δ in this case, and both are equal to 1/ d F and the two descriptions match.

The fractal dimension of an infinite straight rod is naturally 1 as it extends only along one spatial axis. The hydrodynamic radius of a cylinder is not an analytic expression; however, it has been estimated by several authors (see Zhou 10 and Ortega and de la Torre 11 ). They have shown that the diffusion coefficient of a cylinder of diameter d and length L has an asymptotic dependence in (ln L )/( L ) when L f ∞ at constant d . Using the expression from Ortega and de la Torre, 11 a numerical fit of eq 1 for various rods with ratio L / d ranging from 10 to 3500 gives an R value of 0.81 ( R ) 0.998). This value is to be compared with the value of 0.997 ( R ) 0.999 99) obtained under the same a Range is defined as log( M max / M min ), where M min ( M max ) is the molecular weight of the smaller (larger) molecule studied, and log () is the decimal logarithm.

TABLE 1: Analytical Values of δ and r for Various Geometries

| object                             |     δ |    R |   d F | range a   | source       |
|------------------------------------|-------|------|-------|-----------|--------------|
| sphere                             |  0.33 | 0.33 |     3 | ∞         |              |
| polymers in                        |  0.50 |      |     2 | ∞         | ref 7        |
| Θ solvent polymers in good solvent | 0.588 |      |  1.70 | ∞         | refs 7 and 8 |
| finite rods                        |       | 0.81 |  1.24 | 2.5       | this work    |
| finite rods                        | 0.997 |      | 1.003 | 2.5       | this work    |
| infinite rod                       |     1 |    1 |     1 | ∞         |              |

conditions for eq 2, using the expression: R g ) ( d 2 /2 + L 2 /12) 1/2 . All the analytical results are summarized in Table 1.

## Experimental Section

The R parameters have been measured on a wide range of molecules, either from literature results or from NMR diffusion measurements. Three kind of molecular types were considered here: (i) linear homopolymers, with molecular sizes ranging from a few monomers to megadalton polymers; (ii) biological molecules such as globular proteins, oligosccharides or DNA; (iii) small organic molecules from various origin.

The experimental results are analyzed in terms of relative diffusion D r (or diffusivity, as defined by Crutchfield and Harris 5 ): D r ) D / D ref , where D and D ref are the diffusion coefficients observed for the molecule of interest and for the reference molecule. This approach allows the reduction of the impact of viscosity or temperature variations, and we believe it provides more robust results. In all cases care was taken to study homogeneous molecular families and to operate in a diluted mode, below the overlap concentration. All the experimental details along with the experimental values are given in the Supporting Information.

NMR Measures for Proteins. A series of globular proteins were analyzed with masses ranging from 4.19 kD to 120 kD. The proteins were dissolved at a constant 3 mg/mL in H2O, with 1 mM Tris added as a diffusion reference. Figure 1 presents the diffusivity of the proteins with respect with their molecular mass, in a log -log plot. The straight line is the result of fitting eq 1 to this data, with an R value of 0.39 ( 0.02.

NMR Measures for Polymers. Several type of linear polymers in various solvents have also been studied. Poly(ethylene oxide) (PEO) has been studied in water and in chloroform, with sizes ranging from the 62 D (monomer) to 847 kD. Polystyrene (PS) has been studied in chloroform and in toluene, with sizes ranging from 370 D to 8.4 MD. It was also studied in acetone and toluene, in which solubility is poor, with molecular masses range from 580 D to 30 kD and from 370 D to 316 kD, respectively. Poly(methyl methacrylate) (PMMA) has been studied in chloroform and in acetone with sizes ranging from 625 D to 1.6 MD.

Diffusivity was computed on the solvent diffusion when measured in D2O or in toluene, and on TMS when measured in acetone or CDCl3. Figure 2 presents the results for PEO in D2O showing the power law fit. A value of 0.539 ( 0.003 is found here for R .

In most cases, the description of the complete range with only one exponent could not be obtained. In such cases, the curve was correctly described by two independent power laws, on the lighter and on the heavier species.

TABLE 2: Experimental Values of r and d F ) 1/ r As Found in the Literature or in This Study

| molecule family             |    R |   d F | range           | source          |
|-----------------------------|------|-------|-----------------|-----------------|
| globular proteins           | 0.39 |  2.56 | 2.04            | PDB 13          |
| globular proteins           | 0.39 |  2.56 | 1.46            | this work       |
| PS in toluene               | 0.41 |  2.45 | 2.93            | this work       |
| PMMAin acetone below 30 kD  | 0.46 |  2.17 | 1.68            | this work       |
| PS in acetone               | 0.47 |  2.15 | 1.72            | this work       |
| PS in CDCl 3 below 20 kD    | 0.47 |  2.12 | 1.62            | this work       |
| PMMAin CDCl 3 below 30 kD   | 0.48 |  2.07 | 1.68            | this work       |
| oligosaccharides a          | 0.48 |  2.07 | 2.17 (3.40) b   | NMR 3           |
| PS in THF below 20 kD       | 0.50 |  2.01 | 1.72            | this work       |
| PEO in D 2 O                | 0.54 |  1.86 | 3.90            | this work       |
| small molecules in D 2 O a  | 0.54 |  1.84 | 1.39            | NMR 5           |
| PMMAin acetone above 25 kD  | 0.54 |  1.84 | 1.81            | this work       |
| PEO in water                | 0.55 |  1.82 | 2.80            | NMR 6           |
| small molecules in CDCl 3 a | 0.56 |  1.77 | 1.60            | NMR 5           |
| DNA                         | 0.57 |  1.75 | 1.69            | fluorescence 12 |
| PEO in CDCl 3               | 0.58 |  1.73 | 4.13            | this work       |
| denatured peptide a , c     | 0.58 |  1.71 | 1.15            | NMR 2           |
| PMMAin CDCl 3 above 25 kD   | 0.61 |  1.65 | 1.81            | this work       |
| PS in CDCl 3 above 20 kD    | 0.61 |  1.63 | 2.63            | this work       |
| PS in THF above 20 kD       | 0.62 |  1.61 | 2.00            | this work       |
| Linear alcanes              | 0.71 |  1.41 | 0.50 (C8 - C26) | this work       |

a Parameters have been recomputed from the values given in the published work. b The slope was determined on a range of 2.17 and graphically found to extend to the larger range. c Computations from ref 2 where only R H are given, assuming that D / D r ) R Hr / R H.

<!-- image -->

MW

Figure 1. Diffusivity vs molecular mass for a series of globular proteins. The line is the best fit of eq 1 to the data.

Additional Results from the Literature. A rapid survey of the literature shows that many such studies have already been made. To illustrate this work, we chose to present a few values found in the literature, obtained on polymers, 6 DNA, 12 oligosaccharides, 3 proteins and peptides, 2,13 or small molecules. 5 Values obtained from a large range of molecular masses were privileged. All values were determined by NMR, except for the DNA result, which was obtained by fluorescence.

All the R values, either from this study or from the literature, are presented in Table 2 along with the mass range on which the study was performed. In most literature cases, the R value was recomputed from the raw data provided by the authors. The direct non-linear fit of equation (1) used here, being different from the one usually performed in literature, this explains the slight variations from the published values which are observed.

Figure 2. Diffusion vs molecular mass for a series of monodisperse PEO in D2O. The line if the best fit of eq 1 to the data.

<!-- image -->

## Discussion

Diffusion and Fractal Dimension. Table 2 presents many examples of translational diffusion measurement, either from the literature or from our experimental results. When applied to a homogeneous molecular family, it is experimentally verified that eq 1 describes naturally the evolution of the diffusion coefficient. This behavior is verified on many different kind of samples, and up to 4 orders of magnitude in the case of PEO. It should be noted that in most cases the constant density assumption is probably perfectly respected.

On linear polymers the spreading around the theoretical curve is very weak, with R values ranging between 0.995 and 0.999 99. On less homogeneous families, such as small molecules, proteins, or peptides, a larger spreading is observed, but remains moderate, with R factors over 0.977 in all cases.

Nonetheless, a departure from the strict power law is observed on certain polymer systems, for which a separate fit has to be done below a certain molecular mass, typically around 20 kD.

Moreover, the values found for the exponents, ranging from 2.56 to 1.61 are perfectly in the range predicted by the Flory theory. Furthermore, for cases where an experimental value is known for δ , or cases where it is predictable, the value observed for R is very similar.

The protein and peptide case is exemplary in this respect. Globular proteins tends to be very structured, with the polypeptidic chain taking a definite fold determined by the collapse of the chain on a hydrophobic core and a set of hydrogen bonds further tightening the tertiary structure. They are very close to a polymer chain in a very poor solvent, and their fractal dimension is expected to be close to 3. The experimental value (2.56) found here is surprisingly equal to the fractal dimension found in a recent study by Enright and Leitner (13) on the PDB performed on 200 proteins. 13 On the other hand, unstructured peptides are expected to have lower fractal dimension. Fully denatured peptides present a d F of 1.71, very close to the theoretical value of 1.70 (inverse of 0.588) for polymers in good solvent.

Other biological polymers also present contrasting results. The value of 2.07 for oligosaccharides fits well with the fact that they do not present a global fold and that the water is nearly a Θ solvent. The DNA series, 12 though obtained by fluorescence rather than NMR, gives the theoretical value of 1.70.

Linear alkanes have also been studied. Due to the short-range of easily available lengths, the results are not fully interpretable. However, they do follow the global trend and the values were added to this study for completeness.

The values of the fractal dimension displayed by the linear polymers of this study range from 2.45 to 1.61. These values are in good agreement with the expected values. Furthermore, the polymer studies have permitted us to verify, on 4 orders of magnitude in molecular mass, that eq 1 describes adequately the diffusive behavior and that this law still holds for polymers well over the megadalton range for molecular masses. However, most polymer systems present a different behavior at low molecular weight. Short polymers do not act as freely jointed chains and have larger values of radii due to the inherent limits on bond conformations. This effect, decreasing with longer chains, explains the observed larger R values. The issue is expected to be more severe for polymers with bulky side groups, such as PS or PMMA, and nonexistent in highly flexible chains such as PEO, as observed here.

Altogether, the hypothesis that the R value is a measure of the fractal dimension characteristic of the molecular family is fully enforced by these results. In consequence, we propose the following equation, parallel to eq 3:

$$d _ { F } \approx 1 / \alpha$$

It is quite interesting to note that the larger discrepancy between the Flory exponent δ and the R coefficient appears on finite length rods. Though this structure is not meaningful for regular molecules or polymers, it has been extensively studied as a case model for short length DNA double helices 14 or virus capsids. 15 In any case, this discrepancy proves that the δ and R exponents do not measure the same quantity indeed and that the adequacy between the two descriptions should not be taken for granted in all cases.

Molecular Mass Measurement. The generality of eqs 1 and 5 that emerges from this study allows their use in evaluating molecular masses. We thus propose the following relationship for approximate molecular mass M estimation:

$$M \approx \left ( \frac { C _ { r } } { D _ { r } } \right ) ^ { d _ { F } }$$

where D r is the measured diffusivity coefficient, d F is the fractal dimension characteristic of the homogeneous molecular family, and C r is a calibration constant. Both d F and C r depend on the molecular family being studied and have to be determined experimentally. For instance, in the case of globular proteins measured at a concentration of 3 g L -1 , and using Tris as a reference, we have C Tris ) 7.2 ( 1.3 with d F ) 2.56 ( 0.13.

Expression 6, based on diffusivity coefficients D r presents the advantage of being independent of viscosity or temperature variations and provides a robust approach.

A complete table of all the determined values is available as Supporting Information. Additionally, a program and a Web page available at http://abcis.cbs.cnrs.fr/MW.py provides the estimate of the molecular mass from the diffusion coefficients of the molecule of interest and of the reference molecule, with full uncertainty propagation.

## Conclusion

We have checked the validity of the power law expressed in eq 1 for a large range of molecular types and molecular masses. It appears that this equation explains quite satisfactorily the diffusion phenomenon and that the R exponent obtained can be equaled to the δ exponent defined by Flory. 7 However, this correspondence is not strict and should not be taken for granted, as shown by the example of finite length rigid rods.

The inverse of R is an evaluation of the fractal dimension for a homogeneous molecular family. The quality of the fit obtained for PEO in water, over a range of 4 orders of magnitude, is proof that diffusion measurement by NMR is well suited to measure precisely the fractal dimension of diffusing molecules. It is striking that the power law remains the best description of the phenomenon, even for small organic molecules. This means that the observed relationship denotes a fundamental behavior of diffusive molecules in solution and that the notion of fractal dimension can be extended to non polymeric molecules.

The fractal dimension measured here is characteristic of a molecular family; this is in contrast with the fractal dimension measured by techniques such as SAXS or modeling that are obtained for one unique sample.

The possibility of estimating directly the molecular mass of species in solution, presented by eq 6, is a nice extension to the usual capabilities of NMR spectroscopy. However, it should be noted that these equations are only valid for molecules of constant density. Furthermore, the validity of this approach was only checked in the current study for small molecules, globular proteins, and linear homopolymers. It remains to be tested whether it is still valid for molecules with different geometries, such as block-copolymers, branched hyperbranched or cyclic polymers, or dendrimers.

Acknowledgment. This manuscript is dedicated to S.A., deceased June 21, 2006. We thank A. Me ´nez for various protein samples, F. de Lamotte-Gue ´ry for the thioredoxin sample, and G. Labesse for the MOMP protein sample.

Supporting Information Available: Experimental details: protein study, polymer study. Molecular mass determination: data analysis. Uncertainty calculus: uncertainty on D r, uncertainty on M . Additional tables: list of the protein measurements performed in this study, measured values for C r and d F (as defined in eq 6 in text) for all conditions and molecular families. This material is available free of charge via the Internet at http:// pubs.acs.org.

## References and Notes

- (1) Stejskal, E.; Tanner, J. J. Chem. Phys. 1965 , 42 , 288-292.
- (2) Wilkins, D. K.; Grimshaw, S. B.; Receveur, V.; Dobson, C. M.; Jones, J. A.; Smith, L. J. Biochemistry 1999 , 38 , 16424-31.
- (3) Viel, S.; Capitani, D.; Mannina, L.; Segre, A. Biomacromolecules 2003 , 4 , 1843-7.
- (4) Auguin, D.; Gostan, T.; Delsuc, M.-A.; Roumestand, C. Compt. Rend. Chim. 2004 , 7 , 265-271.
- (5) Crutchfield, C. A.; Harris, D. J. J. Magn. Reson. 2007 , 185 , 17982.
- (6) Chari, K.; Antalek, B.; Minter, J. Phys. Re V . Lett. 1995 , 74 , 36243627.
- (7) Flory, P. Principles of Polymer chemistry ; Cornell University Press: Ithaca, NY, 1953.
- (8) Doi, M.; Edwards, S. The Theory of Polymer Dynamics ; Oxford University Press: Oxford, U.K., 1986.
- (9) deGennes, P. Scaling concepts in Polymer Physics ; Cornell University Press; Ithaca, NY, 1979; pp 173 -175.
- (10) Zhou, H.-X. Biophys. J. 1995 , 69 , 2286-97.
- (11) Ortega, A.; de la Torre, J. J. Chem. Phys. 2003 , 119 , 9914-9919.
- (12) Robertson, R.; Laib, S.; Smith, D. Proc. Natl. Acad. Sci. U.S.A. 2006 , 103 , 7310-7314.
- (13) Enright, M.; Leitner, D. Phys, Re V . E 2005 , 71 , 011912 -1011912 -9.
- (14) Allison, S.; Chen, C.; Stigter, D. Biophys. J. 2001 , 81 , 2558-68.
- (15) Santos, N. C.; Castanho, M. A. Biophys. J. 1996 , 71 , 1641-50.

JP8094424