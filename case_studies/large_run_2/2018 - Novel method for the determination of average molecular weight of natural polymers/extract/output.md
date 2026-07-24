<!-- image -->

Contents lists available at ScienceDirect

## Journal of Pharmaceutical and Biomedical Analysis

j o ur nal ho me page: www.elsevier.com/lo

cate/jpba

## Novel method for the determination of average molecular weight of natural polymers based on 2D DOSY NMR and chemometrics: Example of heparin

Yulia B. Monakhova a , b , ∗ , Bernd W.K. Diehl a , Tung X. Do c , Margit Schulze c , Steffen Witzleben c

- a Spectral Service AG, Emil-Hoffmann-Straße 33, 50996 Köln, Germany
- b Institute of Chemistry, Saratov State University, Astrakhanskaya Street 83, 410012 Saratov, Russia
- c Department of Natural Sciences, University of Applied Sciences Bonn-Rhein-Sieg, Von-Liebig-Straße 20, 53359 Rheinbach, Germany

## a r t i c l e i n f o

Article history: Received 1 September 2017 Received in revised form 26 September 2017 Accepted 1 November 2017

Available online 4 November 2017

Keywords: NMR spectroscopy DOSY Molecular weight Heparin Partial least squares regression

## 1. Introduction

Heparin is a polysaccharide polymer drug isolated from glycosaminoglycans released from animal tissues [1]. This medicinal product consists of alternating highly sulfated glucosamine and uronic acid monosaccharide fragments, most of which have molecular weight between 5 and 30 kDa [1,2].

Like all other natural polysaccharides, heparin is a polydisperse mixture containing a large number of chains with varying molecular weights [2]. The variations in fractionating procedure among manufacturers result in differences in the MW distribution of the finished heparin products. On the other side, the chain length is

∗ Corresponding author at: Spectral Service AG, Emil-Hoffmann-Straße 33, 50996 Köln, Germany.

E-mail address: monakhova@spectralservice.de (Y.B. Monakhova).

## a b s t r a c t

Apart from the characterization of impurities, the full characterization of heparin and low molecular weight heparin (LMWH) also requires the determination of average molecular weight, which is closely related to the pharmaceutical properties of anticoagulant drugs.

To determine average molecular weight of these animal-derived polymer products, partial least squares regression (PLS) was utilized for modelling of diffused-ordered spectroscopy NMR data (DOSY) of a representative set of heparin (n = 32) and LMWH (n = 30) samples. The same sets of samples were measured by gel permeation chromatography (GPC) to obtain reference data. The application of PLS to the data led to calibration models with root mean square error of prediction of 498 Da and 179 Da for heparin and LMWH, respectively. The average coefficients of variation (CVs) did not exceed 2.1% excluding sample preparation (by successive measuring one solution, n = 5) and 2.5% including sample preparation (by preparing and analyzing separate samples, n = 5). An advantage of the method is that the sample after standard 1D NMR characterization can be used for the molecular weight determination without further manipulation. The accuracy of multivariate models is better than the previous results for other matrices employing internal standards. Therefore, DOSY experiment is recommended to be employed for the calculation of molecular weight of heparin products as a complementary measurement to standard 1D NMR quality control. The method can be easily transferred to other matrices as well.

© 2017 Elsevier B.V. All rights reserved.

one of the parameters highly affecting biological activity of heparin and low molecular weight heparin (LMWH) as well as therapeutic and pharmacological properties [2-4]. Therefore, an accurate determination of MW is particularly important for the heparin characterization.

The evaluation of average MW represents one of controversial aspects concerning characterization of polymer materials. In this regard, heparin is a challenging matrix due to its sequence heterogeneity, high degree of polydispersity and its polysaccharide nature with long length chains [3]. Among other techniques, liquid chromatography with mass spectrometry (LC-MS) has been used to profile heparin preparations [5,6]. However, for large polymers overlapping MW patterns prevent accurate interpretation of experimental data [5,6]. For LMWH an alternative method based on UV/refractive index ratio of a sample prepared by beta-elimination is also available [6-8].

<!-- image -->

<!-- image -->

The most common method for the determination of MW profiles of heparin and LMWH is gel permeation chromatography (GPC) with refractive index or light scattering detection [2,9,10]. Recently a GPC method for the evaluation of polymer samples was developed, which combines the performance of light-scattering detector, refractometer and viscometer [3]. However, the main disadvantage of GPC based methods is their dependency on a set of reference standards with well-defined average MW and narrow MW distribution (except recently proposed triple detection [3]), which are expensive and are not currently produced on a large scale [2,9]. An alternative universal calibration, which relates the retention times of a polymer to its hydrodynamic volume, has not been applied to heparin so far [11]. Moreover, GPC experiments are often timeconsuming and require large amounts of organic solvents.

It is well known that nuclear magnetic resonance (NMR) spectroscopy is a recognized instrumental method for heparin surveillance regarding quantitative assessment of contaminant levels and qualitative features such as animal origin or brand [12-14].

Recently the NMR method was implemented as a mandatory identity test in European Pharmacopoeia (EP) and US Pharmacopoeia (USP) [15,16]. Several attempts were also made regarding using NMR to determine MW of heparin and LMWH in a standardless manner [17,18]. For example, the 13 C NMR signal intensities of the reducing end and internal anomeric carbons were used to calculate MW of heparin and LMWH [17,18]. However, measurement times required for such analysis with sufficient accuracy even using modern NMR equipment are unacceptable for routine quality control of this medicinal drug [17,18].

In this study we report on the development of a fast and reliable method for the determination of average MW of heparin and LMWH based on diffusion ordered spectroscopy (DOSY) NMR experiments. DOSY represents a method for the discrimination of species with unequal molecular size in their mixture through the measurement of diffusion coefficients (logD) [19]. Access to a series of calibrant compounds with defined molecular weight allowed determination of MW within ± 10% deviation through diffusion coefficient -MW analysis [20]. This approach was further improved by using normalized diffusion coefficients and taking also the shape of the molecules into account [21]. For example, plot of the log of the determined diffusion coefficients versus the log of the MW was linear in case of series of N-acetyl-chitooligosaccharide complexes, pullulan fractions, a set of oligo-/polysaccharides and kinetic samples from controlled polymerization [21-23]. DOSY was also previously employed as an approach to determine the stoichiometry of intermolecular oligosaccharide and organometallic complexes [20,21].

In contrast to these previous studies, in this report multivariate calibration, namely partial least squares regression (PLS), was used to correlate the 2D NMR data with the data of reference GPC analysis. The models were constructed and validated using representative datasets of heparin and LMWH samples derived from different animal tissues (porcine, ovine, bovine). The method is suitable for routine quality control of commercial heparin and LMWH products according to international USP and EP guidelines, because no additional sample preparation is necessary. Software package for the analysis of DOSY NMR data is available to automate the process.

## 2. Materials and methods

## 2.1. Samples and sample preparation

A total of thirty-two heparin (12 bovine, 9 ovine, and 11 porcine) and thirty LMWH (8 ovine and 22 porcine) samples were investigated. Deuterated water of 99.8% purity containing

0.1% trimethylsilyl propanoic acid (TSP) as internal standard was purchased from Euriso-top (Saarbrücken, Germany). For sample preparation, 70 mg of a heparin (LMWH) sample was mixed with 0.7 mL of D2O.

## 2.2. NMR measurements

NMR measurements were performed on Bruker Avance III 600 MHz spectrometer (Bruker Biospin, Rheinstetten, Germany) with BBO cryo probe equipped with Bruker Automatic Sample Changer (B-ACS 120) at 297 K. NMR spectra were recorded with standard pulse program (zg30 in Bruker language) using 16 scans and 2 prior dummy scans. The data of 132 k points were acquired with a spectral width of 24.0155 ppm, a receiver gain of 72, an acquisition time of 4.5438 s.

2D DOSY (diffusion ordered spectroscopy) experiments were performed using standard DOSY pulse sequence with longitudinal eddy current delay (LED) with bipolar gradient pulse pair and 2 spoil gradients. The length of the gradient pulse ( 𝛅 ) was set to 1400 𝛍 s and diffusion time ( /Delta1 ) was set to 0.05 s 2 scans provided enough sensitivity for heparin measurements (this parameter was varied between 2 and 16). The measurement took only 5 min for one sample.

For the processing of DOSY spectra the following diffusion fit function was used:

f ( x ) = I 0 + e ( -y 2 g 2 ı 2 ( /Delta1 -ı 3 ) D ) , where D is the diffusion coefficient, g is the gradient strength and y is the gyromagnetic ratio. I 0 and I represent the maximum and observed signal intensity. The 2D plots show diffusion coefficient values D in [m 2 /s].

The DOSY spectra were baseline corrected and were normalized to TSP signal at -9.3 m 2 /s and ı 0.0 ppm. The data points within the range of ı 6.0-1.8 ppm for heparin and ı 6.2-1.8 ppm for LMWH were pre-processed by bucketing with 0.01 ppm width. The buckets were scaled to total intensity using in-house developed Matlab script. The water peak other solvent signals were excluded from the consideration. Each resultant matrix was unfolded to an array of 1 × 10500 (heparin) or 1 × 13200 (LMWH). Finally, the data were normalized to total intensity before multivariate modelling.

The data were recorded automatically under the control of ICON-NMR (Bruker Biospin, Rheinstetten, Germany). All NMR spectra were manually phased and baseline-corrected using Topspin 3.2 (Bruker Biospin, Rheinstetten, Germany).

## 2.3. Chemometric modelling and validation

Matlab 2015a (The Math Works, Natick, MA, USA) and SAISIR package for MATLAB [24] were used for statistical calculations. Principal component analysis (PCA) was first applied to the datasets for outlier detection.

NMR spectra were correlated with the results of the GPC analysis by PLS regression. No weighing was performed for the models. Validation of the models was first performed using leave-one-out cross validation (LOOCV) to select the number of latent variables (LVs). The simplest models regarding the number of LVs with the minimum value of root-mean-square error of validation (RMSEV) were chosen.

Afterwards, PLS models were validated using independent test set (eight samples for each data set). The splitting into calibration and validation sets was performed ten times. The samples from different animal origin were always included in both subsets. Average values of root mean square of prediction (RMSEP) were used as a quality criterion for model performance.

To assess interday and intraday precision, the analysis of selected samples was performed using separate sample preparations (n = 5) or while staying the autosampler (n = 5).

## 2.4. Reference GPC analysis

Due to the shape of heparin molecules, it is recommended to use reference LMWH materials for calibration [2]. GPC analysis was performed according to the European Pharmacopoeia 7.0 monograph: heparins, low-molecular-mass (01/2008:0828). Two standard calibrants (EP-ENOXAPARIN SODIUM CRS 5.0 and USPENOXAPARIN SODIUM) with defined MWs were used in this study. Standards with higher MW were not available for heparin matrix, therefore, the values were determined by the extrapolation of calibration curve for LMWH (third degree polynomial). For the determination of heparin molar weights an Agilent 1260 Infinity GPC system equipped with UV and RI detector as well PSS PROTEEMA columns (8 × 50 mm pre-column &amp; 8 × 300 mm analytical column with 300 Å porosity) was used. The reproducibility of GPC measurements was equal to 0.7% (six repeated measurements of USP enoxaparin standard). Similar relative standard deviation values ranged between 0.2% and 1.7% were obtained in individual laboratories during interlaboratory GPC study on heparin organized by USP [2].

## 3. Results and discussion

3.1. DOSY NMR for the characterization of MW profiling of heparin and LMWH

Fig. 1 provided a typical representation of 2D DOSY spectra of heparin and LMWH. The diffusion coefficient is a property of the whole molecule and, therefore, the signals are spread out in a horizontal line for both samples. It can be clearly seen that heparin diffuses slower than the smaller LMWH. The TSP peak can be seen at ı 0 ppm and logD = -9.3 m/s 2 (this signal was used for the spectra normalization). The solvent signals (water, methanol, etc.) were deliberately excluded from the data for modelling.

First, to see if DOSY spectra provide reliable information for the characterization of the MW of animal polymer material, five replicate measurements with and without repeated sample preparation of the selected heparin (n = 3) and LMWH (n = 3) samples were performed. The results showed that CVs for the N-acetyl peak position ( ı 2.15 ppm) did not exceed 1.0%. Moreover, the stability of DOSY profiles was given between 50 and 150 mg initial polymer weight dissolved in 1 mL D2O. Outside this region diffusion coefficient values can be influenced by changes in viscosity and solute interactions [25]. It was also confirmed that prepared heparin (LMWH) samples are stable for at least five days at room temperature.

Despite these promising results, it was noticed that the positions of different peaks within one molecule vary along Y-axis of diffusion coefficient values (Fig. 1). Therefore, the usage of only one signal for the MW determination by univariate calibration is possible only after additional standardization using an appropriate polymer reference standard with a defined molecular weight. This, however, means an additional sample preparation step and potential systematic errors introduced by internal standard of 'non-heparin' nature [2].

In the context of heparin analysis, DOSY experiments have been already applied to the screening of unfractioned heparins and LMWH to differentiate active ingredient (AI) and low molecular weight impurity dermatan sulfate (DS) and contaminant oversulfated chondroitin sulfate (OSCS) [25,26]. The region of N-acetyl peaks was selected to assess all polydesperse chemical species in heparin AIs [26,27]. In another study enzymatic depolymerization of porcine heparin was monitored using DOSY experiments [27].

Thus, up to now DOSY spectra themselves provided only qualitative information about the purity of heparin and LMWH samples but not exact molecular weight values. To achieve m2/s this goal, an alternative approach based on PLS regression has been explored in this study.

Fig. 1. Representative DOSY spectra of porcine heparin (A) and porcine LMWH (B).

<!-- image -->

## 3.2. Data preprocessing for multivariate modelling

Proper preprocessing is curial for subsequent multivariate model building. This is especially the case for multidimensional data, where random variations (for example, in peaks' positions) can occur along horizontal and vertical axes. To address this issue, bucketing with 0.01 ppm width (scaled to total intensity) was successively applied to align the spectral data along chemical shift axis, which is routine procedure for the 1D NMR spectra modelling [15]. To avoid systematical shift along diffusion coefficient axis, all spectra were normalized to TSP as an internal reference. Without this step, the results of multivariate modelling were significantly worse.

After alignment step, unfolding was applied to each 2D matrix to transfer it into 1D array. As an example, Fig. 2 showed unfolded data for the porcine LMWH spectrum depicted in Fig. 1A. Thus, the calibration sets had the size of 32 × 10500 and 30 × 13200 for heparin and LMWH, respectively.

Finally, to show whether all DOSY spectra are applicable for multivariate modelling, exploratory PCA was performed separately for heparin and LMWH unfolded datasets. No outliers (the samples that influence the model significantly more than all others) were detected.

## 3.3. Building and validation of PLS models

Preprocessed NMR profiles were correlated to the actual MW values obtained during reference GPC analysis by PLS regression.

Fig. 2. Unfolded spectral data of porcine LMWH sample (Fig. 1A).

<!-- image -->

Fig. 3. MW values of heparin samples of ovine (Ovi), porcine (Por) and bovine (Bov) origin.

<!-- image -->

Table 1 Validation results for PLS regression models for the MW quantification in heparin and LMWH.

| Parameter                   |         | Heparin     | LMWH      |
|-----------------------------|---------|-------------|-----------|
| Reference range [Da]        |         | 12130-15090 | 3858-4778 |
| Number of PLS factors       |         | 5           | 6         |
| RMSECV [Da]                 |         | 443         | 159       |
| RMSEP [Da]                  |         | 498         | 179       |
| Repeatability (CV [%], n=5) | Porcine | 2.1         | 1.8       |
| Repeatability (CV [%], n=5) | Ovine   | 2.0         | 1.3       |
| Repeatability (CV [%], n=5) | Bovine  | 1.2         | - a       |
| Precision [%] (CV [%], n=5) | Porcine | 0.26        | 1.9       |
| Precision [%] (CV [%], n=5) | Ovine   | 1.4         | 2.5       |
| Precision [%] (CV [%], n=5) | Bovine  | 1.6         | - a       |

The parameters of the best models were shown in Table 1. Among other parameters the ranges of reference values in the calibration sets were listed, which covered typical MW values for both matrices. The best PLS models were established using five and six LVs for the heparin and LMWH, respectively. The RMSEV values based on leave-out-one cross validation (LOOCV) of the whole calibration sets were found to be 443 Da and 159 Da, which corresponds to 3.2% and 3.8% of the average values for heparin and LMWH, respectively (Table 1). Fig. 3 showed the predicted-reference plot for the LMWH model obtained by LOOCV, which proved high correlation between two datasets.

To obtain practically meaningful estimates for accuracy, independent test set validation was performed. Eight samples were randomly selected from the datasets 10 times. As an example, the predicted MW values for LMWH were shown in Table 2. In this case accuracy varied between 0.3% and 5.1%. The average RMSEP values

Table 2 Independent set validation for the MW prediction of LMWH by PLS.

| Sample   |   Predicted NMR[Da] |   Reference GPC [Da] |   Error [%] |
|----------|---------------------|----------------------|-------------|
| S1       |                4030 |                 3871 |         4.1 |
| S2       |                4238 |                 4032 |         5.1 |
| S3       |                4200 |                 4317 |         2.7 |
| S4       |                4154 |                 4107 |         1.1 |
| S5       |                4132 |                 4007 |         3.1 |
| S6       |                4673 |                 4686 |         0.3 |
| S7       |                4138 |                 4086 |         1.3 |
| S8       |                4146 |                 4086 |         1.5 |

(10 x splitting into calibration and validation sets) were found to be 498 Da and 179 Da for heparin and LMWH, respectively (Table 1). Taking into account that the errors provided by quantitative DOSY measurements were reported to be about 9% [21], our PLS models represent a better choice for MW prediction than using a set of internal standards.

The standard errors of successive DOSY measurements were between 1.2% and 2.1% for heparin and 1.3% and 1.8% for LMWH without repeating sample preparation (Table 1). To evaluate the error introduced by sample preparation, six heparin and four enoxaparin samples were prepared five times. The average difference between the predictions for each sample expressed as coefficient of variation (CV) was between 0.26% and 1.6% for heparin and between 1.9% and 2.5% for LMWH (Table 1, Fig. 3). The results showed that CVs were not influenced by the animal origin of samples. These satisfactory results indicated that PLS is suitable for analysis of heparin and LMWH from different animal origin regarding average MW values.

Generally speaking, differences in MW values were previously observed among heparins produced from porcine, ovine, and bovine species [28]. Based on our measurements it was found that porcine heparin had the highest molecular weight among three major species, followed by bovine material, while ovine heparin had considerably lower values about 12.5 kDa on average (Fig. 1, Supplementary Information). In the case of LMWH, however, MW values of ovine samples were higher than those of porcine (Fig. 3). Therefore, average MW can serve as a parameter to differentiate heparin and LMWH according to its animal origin. Better discrimination can be obtained, however, by using chemometric analysis of 1D and 2D heparin (LMWH) profile [13,14].

Thus, summarizing our results, it can be stated that PLS modelling of DOSY NMR spectra can be regarded as a good analytical approach for estimating MW of heparin and LMWH samples with accuracy below 5% and repeatability of about 2%. The soundness of alternative chromatographic results mainly depends on the appropriate calibration of the GPC columns [2,10]. The same is also applicable to the previous quantitative DOSY measurements [21]. The developed DOSY-PLS method does not require calibration for routine measurements. Once PLS model is built, the method can be routinely used on a given spectrometer as an additional to standard 1D 1 H NMR measurement recommended by US and European Pharmacopoeias [15,16,]. On this stage, NMR procedure was judged as a usable screening procedure to quantitatively control the average MW of heparin in only 5 min.

## 4. Conclusions

Since several years Food and Drug Administration (FDA) has been promoting the inclusion of enhanced standards for heparin purity and identity in the relevant monographs of the United State Pharmacopea (USP) [15]. Average MW is among crucial parameters, which can potentially discriminate between products from different animal species as well as to provide measurement of consistency between heparin batches and assist in discovering new types of contamination or impurities [2]. Moreover, recent study revealed direct correlation of MW of synthesized homogeneous LMWH with reversible anticoagulant activity [4]. In this paper an alternative DOSY NMR method for the determination of the average MW of heparin and LMWH using no reference standards has successfully been developed and validated.

Only a few minutes are required to acquire a good quality DOSY spectrum of heparin (LMWH), which is considerably less than other standard 2D heteromolecular experiments and 13 C NMR measurements [13,14]. Therefore, we recommend acquiring DOSY data during the collection of routine NMR experiment to provide additional complementary information about purity and molecular weight distribution of heparin products. The method is currently dependent on a given NMR device, where reference set have been measured. However, several available mathematical tools can be used to transfer available multivariate models to other spectrometers [29].

To our knowledge, only one application of multivariate calibration by N-PLS was previously applied to DOSY NMR spectra for quantification of lipoprotein fractions in human plasma samples [30]. The idea to correlate NMR diffusion data with the results of reference analysis by multivariate regression analysis as a simple and fast way to estimate the average MW of heparin (and other polymer materials in general) has not been reported so far.

## Acknowledgements

We thank Professor Fareed and Dr. Yao for providing samples of ovine origin. Y. Monakhova acknowledges support of the Russian Ministry of Science and Education (project 4.1063.2017/4.6). TXD, MS and SW acknowledge financial support given by the German Federal Ministry of Education and Research (program 'Forschung an Fachhochschulen', projects Ingenieur Nachwuchs 03FH013IX4 and FHprofUnt 03FH012PB2).

## References

- [1] [B. Casu, A. Naggi, G. Torri, Re-visiting the structure of heparin, Carbohydr. Res. 403 (2015) 60-68.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0015)
- [2] B. Mulloy, A. Heath, Z. Shriver, F. Jameison, A. Al Hakim, T.S. Morris, A.Y. Szajek, USP compendial methods for analysis of heparin: chromatographic determination of molecular weight distributions for heparin sodium, Anal. Bioanal. Chem. 406 (2014) 4815-4823.
- [3] A. Bisio, A. Mantegazza, D. Vecchietti, D. Bensi, A. Coppa, G. Torri, S. Bertini, Determination of the molecular weight of low-molecular-weight heparins by using high-pressure size exclusion chromatography on line with a triple detector array and conventional methods, Molecules 20 (2015) 5085-5098.
- [4] Y. Xu, C. Cai, K. Chandarajoti, P.H. Hsieh, L. Li, T.Q. Pham, E.M. Sparkenbaugh, J. Sheng, N.S. Key, R. Pawlinski, E.N. Harris, R.J. Linhardt, J. Liu, Homogeneous low-molecular-weight heparins with reversible anticoagulant activity, Nat. Chem. Biol. 10 (2014) 248-250.
- [5] [C. Thanawiroon, K.G. Rice, T. Toida, R.J. Linhardt, Liquid chromatography/mass spectrometry sequencing approach for highly sulfated heparin-derived oligosaccharides, J. Biol. Chem. 279 (2004) 2608-2615.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0035)
- [6] L. Li, F. Zhang, J. Zaia, R.J. Linhardt, Top-down approach for the direct characterization of low molecular weight heparins using LCFTMS, Anal. Chem. 84 (2012) 8822-8829.
- [7] W. Jeske, A. Ahsan, J. Fareed, Molecular weight profiling of low molecular weight heparins utilizing a heparinase degraded oligosaccharide mixture as a calibrator, Thrombosis Res. 70 (1993) 39-50.
- [8] J.I. Nielsen, A convenient method for molecular mass determination of heparin, Thromb. Haemost. 68 (1992) 478-480.
- [9] J. Beirne, H. Truchan, L. Rao, Development and qualification of a size exclusion chromatography coupled with multiangle light scattering method for molecular weight determination of unfractionated heparin, Anal. Bioanal. Chem. 399 (2011) 717-725.
- [10] C.D. Sommers, H. Ye, R.E. Kolinski, M. Nasr, L.F. Buhse, A. Al-Hakim, D.A. Keire, Characterization of currently marketed heparin products: analysis of molecular weight and heparinase-I digest patterns, Anal. Bioanal. Chem. 401 (2011) 2445-2454.
- [11] M.M. Claus, D.L. Weldin, E. Frank, E. Giebel, M.R. Buchmeiser, Size-exclusion chromatography and aggregation studies of acetylated lignins in N,N-dimethylacetamide in the presence of salts, Macromol, Chem. Phys. 216 (2015) 2012-2019.
- [12] [S. Beni, J.F.K. Limtiaco, C.K. Larive, Analysis and characterization of heparin impurities, Anal. Bioanal. Chem. 399 (2011) 527-539.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0070)
- [13] T. Beyer, B. Diehl, G. Randel, E. Humpfer, H. Schäfer, M. Spraul, C. Schollmayer, U. Holzgrabe, Quality assessment of unfractionated heparin using 1H nuclear magnetic resonance spectroscopy, J. Pharm. Biomed. Anal. 48 (2008) 13-19.
- [14] Y.B. Monakhova, B.W. Diehl, Combining 1H NMR spectroscopy and multivariate regression techniques to quantitatively determine falsification of porcine heparin with bovine species, J. Pharm. Biomed. Anal. 115 (2015) 543-551.
- [15] US Pharmacopoeia, United States Pharmacopoeia Heparin Sodium Stage 3 Monograph, US Pharmacopoeia, Rockville, 2012, http://www.usp.org/sites/ default/files/usp pdf/EN/USPNF/key-issues/m36690 pf386.pdf. (Accessed June 15 2015).
- [16] European Pharmacopoeia, European Pharmacopoeia Heparin Sodium Monograph PA/PH/Exp. 6/T(0) 42 PUB Monograph Number 333, EDQM, Strasbourg, 2010, http://www.edqm.eu/medias/fichiers/NEW Heparin sodium 0820100333.pdf. (Accessed June 15 2015).
- [17] U. Desai, R.J. Linhardt, Molecular weight of low molecular weight heparins by 13C nuclear magnetic resonance spectroscopy, Carbohyd. Res. 255 (1994) 193-212.
- [18] [U. Desai, R.J. Linhardt, Molecular weight of heparin using 13c nuclear magnetic resonance spectroscopy, J. Pharm. Sci. 84 (1995) 212-215.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0100)
- [19] S. Bradamante, L. Barenghi, G. Beretta, M. Bonfa, M. Rollini, M. Manzoni, Production of lovastatin examined by an integrated approach based on chemometrics and DOSY-NMR, Biotechnol. Bioeng. 80 (2002) 589-593.
- [20] P. Groves, M.O. Rasmussen, M.D. Molero, E. Samain, F.J. Ca˜ nada, H. Driguez, J. Jiménez-Barbero, Diffusion ordered spectroscopy as a complement to size exclusion chromatography in oligosaccharide analysis, Glycobiology 14 (2004) 451-456.
- [21] R. Neufeld, D. Stalke, Accurate molecular weight determination of small molecules via DOSY-NMR by using external calibration curves with normalized diffusion coefficients, Chem. Sci. 6 (2015) 3354-3364.
- [22] S. Viel, D. Capitani, L. Mannina, A. Segre, Diffusion-ordered NMR spectroscopy: a versatile tool for the molecular weight determination of uncharged polysaccharides, Biomacromolecules 4 (2003) 1843-1847.
- [23] W. Li, H. Chung, C. Daeffler, J.A. Johnson, R.H. Grubbs, Application of 1H DOSY for facile measurement of polymer molecular weights, Macromolecules 45 (2012) 9595-9603.
- [24] [C.B.Y. Cordella, D. Bertrand, SAISIR: A new general chemometric toolbox, Trends Anal. Chem. 54 (2014) 75-82.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0130)
- [25] E. Bednarek, J. Sitkowski, W. Bocian, B. Mulloy, L. Kozerski, An assessment of polydispersed species in unfractionated and low molecular weight heparins by diffusion ordered nuclear magnetic resonance spectroscopy method, J. Pharm. Biomed. Anal. 53 (2010) 302-308.
- [26] J. Sitkowski, E. Bednarek, W. Bocian, L. Kozerski, Assessment of oversulfated chondroitin sulfate in low molecular weight and unfractioned heparins diffusion ordered nuclear magnetic resonance spectroscopy method, J. Med. Chem. 51 (2008) 7663-7665.
- [27] [J.F.K. Limtiaco, S. Beni, C.J. Jones, D.J. Langeslay, C.K. Larive, NMR methods to monitor the enzymatic depolymerization of heparin, Anal. Bioanal. Chem. 399 (2011) 593-603.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0145)
- [28] [L. Fu, G. Li, Bo Yang, A. Onishi, L. Li, P. Sun, F. Zhang, R.J. Linhardt, Structural characterization of pharmaceutical heparins prepared from different animal tissues, J. Pharm. Sci. 102 (2013) 1447-1457.](http://refhub.elsevier.com/S0731-7085(17)32214-8/sbref0150)
- [29] Y.B. Monakhova, B.W.K. Diehl, Transfer of multivariate regression models between high-resolution NMR instruments: application to authenticity control of sunflower lecithin, Magn. Reson. Chem. 54 (2016) 712-717.
- [30] M. Dyrby, M. Petersen, A.K. Whittaker, L. Lambert, L. Nørgaard, R. Bro, S.B. Engelsen, Analysis of lipoproteins using 2D diffusion-edited NMR spectroscopy and multi-way chemometrics, Anal. Chim. Acta 531 (2005) 209-216.