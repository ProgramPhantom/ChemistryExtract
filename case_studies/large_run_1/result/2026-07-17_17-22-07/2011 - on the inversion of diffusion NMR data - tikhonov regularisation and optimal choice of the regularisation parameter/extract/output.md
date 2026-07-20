<!-- image -->

Contents lists available at ScienceDirect

## Journal of Magnetic Resonance

j o u r n a l homepage: www.elsevier.com/locate/jmr

<!-- image -->

## On the inversion of diffusion NMR data: Tikhonov regularization and optimal choice of the regularization parameter

Iain J. Day ⇑

School of Life Sciences, University of Sussex, Falmer, Brighton BN1 9QJ, UK

## a r t i c l e i n f o

Article history: Received 24 February 2011 Revised 16 May 2011 Available online 31 May 2011

Keywords: Diffusion NMR Inversion Inverse Laplace transform Tikhonov regularization

Parameter choice

## 1. Introduction

The influence of bulk sample motion on the observed echo attenuation in pulsed-gradient spin echo (PGSE) and stimulated echo (PGStE) experiments has been known since the early days of NMR spectroscopy [1,2]. In principle, analysis of this attenuation behaviour as a function of the applied gradient strength gives one access to diffusion coefficients and bulk flow parameters [3]. Unfortunately the nature of the mathematical problem underlying the analysis of PGSE data renders this a non-trivial task in all but the simplest of cases [4,5]. In general, the echo attenuation following the application of a gradient spin-echo or stimulated echo for a diffusing spin of diffusion coefficient D is described by the StejskalTanner equation [1-5]:

$$\frac { s ( g ) } { s ( 0 ) } = \exp ( - q ^ { 2 } \Delta ^ { \prime } D ) & & ( 1 ) & \begin{smallmatrix} \text {more} & \text {c} \\ & \text {h} ( D ) . & \end{smallmatrix}$$

where q = c g d and D 0 = D  d /3 to correct for the finite duration of the gradient pulses, c is the magnetogyric ratio of the diffusing spin, g is the amplitude of the gradient pulse with duration d , and D is the diffusion labelling time. Depending on the precise details of the pulse sequence, minor modifications are required to the D 0 parameter [3,5]. The effects of coherent sample motion such as flow, which are typically observed as phase shifts, will not be considered here. In the case of a single diffusing species, or multiple, non-overlapping species, the diffusion coefficient can be obtained by the

⇑ Fax: +44 1273 876687. E-mail address: i.j.day@sussex.ac.uk

## a b s t r a c t

The analysis of diffusion NMR data in terms of distributions of diffusion coefficients is hampered by the ill-posed nature of the required inverse Laplace transformation. Naïve approaches such as multiexponential fitting or standard least-squares algorithms are numerically unstable and often fail. This paper updates the CONTIN approach of the application of Tikhonov regularization to stabilise this numerical inversion problem and demonstrates two methods for automatically choosing the optimal value of the regularization parameter. These approaches are computationally efficient and easy to implement using standard matrix algebra techniques. Example analyses are presenting using both synthetic data and experimental results of diffusion NMR studies on the azo-dye sunset yellow and some polymer molecular weight reference standards.

Ó 2011 Elsevier Inc. All rights reserved.

straight-forward least-squares fitting of Eq. (1) to the experimental data. This technique has been used for a variety of applications such as determining the oligomeric state of organometallic complexes [6] and the analysis of complex mixtures [7]. The situation becomes more challenging when multiple diffusing species are present in solution giving rise to the overlap of spectral resonances. In this case, the multi-exponential fitting of Eq. (1) can be fraught with difficulty [4,5,8] depending on the number of diffusing species and the differences in their diffusion coefficients. A number of numerical approaches have been demonstrated to attempt to solve this overlap problem both in the case when the number of diffusing species is known and when it is not. Typical methods are those such as DECRA [9,10], (S)CORE [11-13], maximum entropy methods [14] or other, more exotic methods [15,16].

In the limit of a large number of diffusing species, the system is more correctly described by a distribution of diffusion coefficients h ( D ). In the case, Eq. (1) is modified by integrating over this distribution:

Z

$$\text {sg spin} , \quad s ( g ) = \left | \ e x p ( - q ^ { 2 } \Delta ^ { \prime } D ) h ( D ) d D \right |$$

This equation can be re-cast in matrix form as:

$$\int _ { \real \ s \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{ \ } \ \{$$

where the matrix A , termed the Stejskal-Tanner matrix, can be though of as mapping the distribution of diffusion coefficients h onto the observed echo attenuation s . The elements of A are then defined as follows:

$$A _ { m n } = \exp ( - \gamma ^ { 2 } \delta ^ { 2 } g _ { n } ^ { 2 } D _ { m } ( \Delta - \delta / 3 ) )$$

As diffusion coefficients typically span several orders of magnitude, it is advantageous to consider a logarithmically spaced grid in the diffusion dimension, i.e. log( D ). As Chen et al. have noted [17], a result of this transformation is that peaks in h ( D ) at small values of D will appear larger than peaks with similar area at larger D . In order to correct for this the product D h ( D ) is typically plotted versus log( D ) [17].

Eq. (2) has the form of a Laplace transform, which occurs frequently in the analysis of magnetic resonance data, for instance in the field of relaxometry [18,19]. In order to recover the distribution of diffusion coefficients, the inverse Laplace transform is required, which is famously difficult to solve numerically, as it is an ill-posed problem [20]. Naively, one would attempt to solve Eq. (3) by either forming the (pseudo) inverse of A or by using a traditional least-squares approach:

$$h _ { L S } = A ^ { + } s \ \text { or } \ \arg \min _ { \mathfrak { h } } \| A h - s \| _ { 2 } ^ { 2 } \quad ( 5 )$$

where A + is the pseudo-inverse of A (Moore-Penrose pseudo-inverse). Fig. 1 shows this naïve approach, using Eqs. (3) and (4) to construct the echo attenuation (Fig. 1b) from the Gaussian distribution of diffusion coefficients shown in Fig. 1a. The least-squares attempt to recover this distribution clearly fails, resulting in wild oscillations of the returned distribution, characteristic of an illposed problem (Fig. 1c).

On purely physical grounds, the constraint that the distribution of diffusion coefficients should be non-negative, i.e. h P 0, is well justified. Using the non-negative least-squares algorithm (NNLS) [21] it is straight forward to solve Eq. (3). Unfortunately, the solutions produced are not realistic, as has been noted in the investigation of T 2 relaxation profiles, since the NNLS algorithm tends to produce sharply peaked results, with only a few non-zero data points [22]. While these spikes are often close in position to the maxima in the true distribution, the NNLS algorithm is unable to reproduce reliably the shape of the distribution. Despite this, however, these spikes have been put to use in the Monte Carlo style analysis of T 2 relaxation data [22]. Similar sharply spiked results were observed on application of the NNLS algorithm to the inversion of Eq. (3) (results not shown).

There have been a number of approaches described to attempt to extract meaningful distributions of diffusion coefficients from PGSE data, and similarly for the analysis of relaxation time distributions, including regularization [17,23], maximum entropy [14] and Bayesian methods [24]. Of these, the use of the CONTIN package [25] has been particularly successful [17,23]. This approach uses Tikhonov regularization to stabilise the solution to Eq. (3) by imposing a penalty on the recovered solution. The nature of this penalty can be chosen by the user. The regularized solution is obtained by the following minimisation:

$$\arg \min _ { h } \| \text {A} - \text {s} \| _ { 2 } ^ { 2 } + \lambda ^ { 2 } \| \text {L} \| _ { 2 } ^ { 2 } & & ( 6 ) & \text {pulsed-gradients} \\ & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

The formal solution to which can be written as:

$$\mathbf h _ { \xi } = ( A ^ { T } A + \lambda ^ { 2 } L ^ { T } L ) ^ { - 1 } A ^ { T } \mathbf s & & ( 7 ) & \stackrel { \stackrel { \dots } { d i f f e r n c } } { \text {difference} }$$

The second term in Eq. (6) serves to impose some constraint or prior knowledge on the size of the returned distribution, with the power of this term controlled by the regularization parameter k . The appropriate choice of this parameter is therefore very important. The CONTIN package makes the choice of the regularization parameter k based on statistical arguments and using the principle of parsimony, i.e. choose the simplest solution consistent with the data, which may depend on additional input from the user [25]. The matrix L allows a priori expectations about the data to be included such as requiring the solution to be smooth. Other constraints, based typically on physical insights, such as nonnegativity using the (F)NNLS algorithm [21,26], can also be readily included. In the magnetic resonance field, Tikhonov regularization has also been used very successfully in the analysis of DECODER solid-state NMR data [27], in the extraction of distance distributions from pulsed EPR data [28] and the recovery of radical-pair re-encounter probability distributions in magnetic field effect experiments [29].

Fig. 1. (a) Gaussian distribution of diffusion coefficients, centred at 5.0 -10  10 m 2 s  1 , with width 5.0 -10  11 m 2 s  1 on a logarithmically-spaced grid of 201 diffusion points. (b) Echo attenuation profile for a proton spin during a pulsed-gradient stimulated echo sequence, calculated using Eq. (3) assuming 64 gradient points equally spaced between 0.05 and 0.7 T m  1 . The gradient duration was 2 ms and the diffusion labelling period was 100 ms. Random Gaussian noise of zero mean, and standard deviation 5.0 -10  3 has been added. (c) Attempted recovery of the input distribution using a standard least-squares approach. Note the difference in y -scale between (a) and (c).

<!-- image -->

## 1.1. Analysis of the Stejskal-Tanner matrix

One of the major tools in the analysis of ill-posed problems is the Singular Value Decomposition (SVD) [30]. This permits an arbi- trary matrix A to be decomposed into three matrices, U , R and V such that:

$$A = U \Sigma V ^ { T }$$

The matrix U is said to contain the left singular vectors as its rows, which form an orthonormal basis for A . Similarly, V T contains the right singular vectors as its columns which also form an orthonormal basis for A . The matrix R is diagonal, containing the socalled singular values stored in decreasing order, i.e. r 1 &gt; r 2 &gt; r 3 &gt;    &gt; r n . Using the definition of the SVD in Eq. (8) it is possible to recast the solution of Eq. (3) in terms of the singular values r i and vectors ui and v i :

$$h _ { I S } = A ^ { + } s = \sum _ { i = 1 } ^ { \text {rank} ( \mathbf A ) } \frac { u _ { i } ^ { T } s } { \sigma _ { i } } \nu _ { i } & & \text {the coe} \\ & & \text {satisfies} \\ & & \text {becomes}$$

Through the use of the SVD it is possible to identify an ill-posed problem and to determine to what extent regularization approaches may succeed [30]. Fig. 2 shows a plot of the singular values (filled circles) for a typical Stejskal-Tanner matrix comprising 201 diffusion points and 64 gradient points, that used in calculating the data shown in Fig. 1. As can clearly be seen the 64 singular values rapidly decay and settle at a value proportional to the machine epsilon, or floating point precision of the software used to perform the calculations. It is these extremely small singular values, via the denominator in Eq. (9), which result in the wild oscillations observed in the least-squares solution (Fig. 1c) and the ensuing failure to recover the input distribution of diffusion coefficients. It is worth noting that these difficulties in the inversion of ill-posed problems are a general feature of the matrix A , and are present even in the absence of noise. Regularization methods work by filtering out the influence of the small singular values and hence stabilising the solution of the inverse problem [30]. In the case of Tikhonov regularization when the operator L = I , the regularized solution of Eq. (6) can be constructed from the SVD as shown:

X

$$\mathbf h _ { \lambda } = \sum _ { i = 1 } ^ { n } f _ { i } \frac { u _ { i } ^ { T } s } { \sigma _ { i } } v _ { i } & & \text {small} & ( 1 0 ) & \text {propositive} & & \text {of compact}$$

where the filter factors f i are defined as:

$$f _ { i } = \frac { \sigma _ { i } ^ { 2 } } { \sigma _ { i } ^ { 2 } + \lambda ^ { 2 } } & & \text {plest score} \\ & & \text {common} \\ & & \text {quire a}$$

Note, that when L -I , the singular values are replaced by the generalized singular values of the matrix pair ( A , L ) [30,31]. Clearly then, the effect of the regularization parameter k is to reduce the

×x

<!-- image -->

Index, i influence of the small singular values of A in a controlled manner as opposed to using a sharp cut off in the case of truncated SVD reconstructions such as those used in for example the analysis of relaxation data [32].

Fig. 2. Singular values r i , coefficients j u T i s j , and their ratio, calculated for the Stejskal-Tanner matrix used in Fig. 1.

The ability of a regularization method to return useful (meaningful) results can be investigated by examining the rates at which the singular values r i and the coefficients j u T i s j decay to small values. Considering Eq. (9), we should require that the coefficients decay more rapidly than the singular values in order that a meaningful regularized solution can be found. This can be formalized in terms of the discrete Picard condition [30], and is inspected visually for the Stejskal-Tanner matrix in Fig. 2. The singular values are represented by filled circles, while the open squares show the coefficients j u T i s j . As is clear, the discrete Picard condition is satisfied for the first 10 or so singular values until the coefficients become dominated by the noise in the measured data s . Therefore a good regularization method will favour retaining just these components. As the role of the regularization and hence the regularization parameter, is to filter out the small singular values, the problem reduces to one of how to choose an appropriate value for the regularization parameter. Another common feature of illposed problems is that increasing the size of the matrix A , in either dimension, does not in general improve the ability to obtain a stable solution.

## 1.2. Choice of regularization parameter

One of the key challenges in using any regularization method is the selection of the regularization parameter k . When the parameter is small, the solution is under regularized and the residual norm || Ah k  s ||2 dominates the solution, which in the limit of k = 0 results in the classical least squares solution with the associated wild oscillations. Similarly large values of k result in the solution norm || Lh k ||2 dominating: the solution is over penalised, i.e. oversmoothed, and information is lost. A number of methods have been proposed to determine the optimal value of k , with varying degrees of computational complexity and stability [30]. The CONTIN package, commonly used for the analysis of diffusion NMR data, uses statistical arguments and guidance from the user to find the simplest solution compatible with the observed data. Two of the most common automatic parameter choice methods, which do not require any intervention from the user, are the L-curve approach [33] and Generalized Cross Validation (GCV).

The L-curve method is, perhaps, conceptually the simplest method of choosing the regularization parameter. It is a parametric plot of the residual norm || Ah k  s ||2 against the solution norm || Lh k ||2, plotted in log-log space parametrically as a function of regularization parameter: ( q ( k ), g ( k )) = (log || Ah k  s || 2, log || Lh k || 2). The characteristic ''L'' shape of the curve gives this method its name. It can be shown that the L-curve is a monotonic function of k and that it is impossible to construct any solution h which falls below the curve [33]. The optimal value of the regularization parameter is located close to the corner of the curve, being a balance between the smooth, over-regularization of the solution (large values of k ) and perturbation errors caused by very small singular values (small values of k ). The corner of the L-curve is located at the point which has maximum curvature. The curvature j is defined as:

$$\lim _ { \substack { 1 \\ 6 0 } } \bullet - \int _ { 0 } ^ { \rho ^ { \prime } \eta ^ { \prime \prime } - \rho ^ { \prime \prime } \eta ^ { \prime } } \kappa ( \lambda ) = \frac { \rho ^ { \prime } \eta ^ { \prime \prime } - \rho ^ { \prime \prime } \eta ^ { \prime } } { ( ( \rho ^ { \prime } ) ^ { 2 } + ( \eta ^ { \prime } ) ^ { 2 } ) ^ { 3 / 2 } }$$

With the primes denoting the derivative with respect to k . A typical L-curve for Tikhonov regularization as applied to the solution of Eq. (3) via Eq. (6) is shown in Fig. 3a.

An alternative method for choosing the regularization parameter is that of Generalized Cross Validation (GCV). The principle behind this method is that a ''good'' regularized solution given by an appropriate value of the regularization parameter k should be able to predict missing data [30], i.e. if a point were dropped from the vector h , then a good value of k should be able to reconstruct this missing data point. The GCV function is defined as:

$$G ( \lambda ) = \frac { \| \mathbf A _ { \lambda } - s \| _ { 2 } ^ { 2 } } { T r ( | _ { m } - \mathbf A ^ { \# } ) ^ { 2 } } & & ( 1 3 ) & & \text {and} \ h e d { 1 } \\$$

where I m is the m -m identity and A # is the regularized inverse of A , defined such that h k = A # s . The numerator describes the quality of the solution's fit to the data being the residual norm and the denominator gives the number of effective degrees of freedom

(a)

Fig. 3. (a) L-curve analysis giving the optimal regularization parameter k c = 0.1677 and (b) Generalized Cross Validation analysis yielding an optimal regularization parameter of k min = 0.1144 for the synthetic problem shown in Fig. 1. The dotted lines indicate the optimal value of k . (c) shows the first 15 filter factors, on a semilogarithmic scale, appropriate for the regularization parameters determined via the L-curve and GCV methods.

<!-- image -->

[30]. The optimal value of the regularization parameter k min is found when this function is a close to a minimum. A typical example of the GCV function for diffusion NMR data, with the minimum highlighted, is shown in Fig. 3b. One issue with the use of the GCV function as a parameter choice method is that it is typically very flat for small values of the regularization parameter, as shown by the lefthand side of Fig. 3b. This may cause the numerical routines used to locate the minimum to select values of k smaller than the optimum, and hence this approach can often give rise to under-regularized solutions.

Using the optimal regularization parameters obtained by these two methods allows the filter factors, calculated using Eq. (11) to be inspected, as shown in Fig. 3c. The filter factors decrease logarithmically with increasing index beyond about the 7th singular value. From this it is clear that only the first few singular values of the Stejskal-Tanner matrix will contribute significantly to the recovered solution, with the smaller singular values, responsible for the wild oscillations, effectively removed from the recovered solutions.

In this work, we seek to update the CONTIN approach of applying Tikhonov regularization to the solution of Eq. (3), using the implementation in Hansen's Regularization Tools [34]. The automatic choice of the regularization parameter k , using both the L-curve and Generalized Cross Validation (GCV) methods is investigated, along with the influence of the operator L for simple synthetic distributions of diffusion coefficient. Application to the analysis of PGStE data for two chemical systems is then demonstrated.

## 2. Methods

## 2.1. Numerical calculations and data analysis

All numerical calculations were performed using the open source SciPy modules of the Python programming language [35]. Tikhonov regularization and the associated analyses were performed using routines based on Hansen's Matlab package Regularization Tools (version 4.1) [34,36], following translation into Python/SciPy code.

## 2.2. NMR spectroscopy

All NMR data were collected on a Varian VNMRS 600 spectrometer (Oxfordshire, UK), operating at a 1 H frequency of 599.7 MHz, using an X{ 1 H} broadband probe equipped with an activelyshielded z-gradient capable of up to 0.7 T m  1 . The sample temperature was regulated at 298 K. Pulsed-gradient stimulated echo diffusion data were recorded using the Oneshot sequence [37] with 64 linearly spaced gradient points spanning 0.04-0.56 T m  1 . The gradient durations were 3 ms, with the diffusion labelling period being 200 ms. The data were processed with NMRPipe [38] using 0.5 Hz exponential line broadening prior to Fourier transformation, and integrating over the aromatic region.

## 2.3. Materials

Sunset yellow FCF was obtained from Sigma Aldrich (Dorset, UK) and purified by ethanol precipitation prior to use [39,40]. Samples were prepared at concentrations of 1.64 mM, 0.10 M, 0.30 M, 0.49 M, 0.74 M and 0.90 M in D2O as used in the previous study [41]. Poly(styrene 4-sulphonate) polymer reference standards of known molecular weight and polydispersity typically less than 1.20, were purchased from Kromatek (Essex, UK) and used as obtained. All polymer samples were prepared as 1 mM solutions in D2O. Deuterium oxide was supplied by Goss Scientific (Cheshire, UK).

## 3. Results and discussion

## 3.1. Application to synthetic data

As an initial demonstration of the application of Tikhonov regularization to the inversion of Eq. (3), model echo attenuation profiles were constructed from two diffusion coefficient profiles, h ( D ): one, a unimodal Gaussian distribution centred at 5.0 -10  10 m 2 s  1 and width 5.0 -10  11 m 2 s  1 and the second, consisting of a pair of non-overlapping Gaussians, centred at 2.0 -10  9 and 3.0 -10  10 m 2 s  1 , with widths 1.3 -10  10 and 0.3 -10  10 m 2 s  1 respectively, using Eq. (3). Gaussian white noise, of standard deviation 5.0 -10  3 , was added to the resulting echo attenuations to yield a signal-to-noise ratio of  200. This is comparible to that obtainable experimentally. Fig. 4 shows the results of the application of Eq. (6) to the inversion of Eq. (3), using two choices for the operator L , either the identity, I or a discrete finite difference approximation of the second derivative operator D 2. The added constraint that the solution should be non-negative ( h P 0) was included in all cases via use of the NNLS algorithm [21] to solve Eq. (6). The appropriate model input distribution is shown for comparison. Inclusion of the non-negativity constraint was found to be vital in stopping the return of broad, featureless, slowly varying solutions (data not shown). The simplest initial test case is the unimodal distribution, with the results shown in Fig. 4a for parameter choice by the L-curve method and Fig. 4b for the GCV approach. Clearly similar results are obtained by the two methods, as indicated by the similar optimal regularization parameters returned: k c = 0.1677, and k min = 0.1144, suggesting that, in this simulation at least, the determination of the location of the GCV minimum is not strongly affected by the broadly flat GCV function observed for small values of k . In terms of the effect of the operator L , the use of the identity matrix I yields a distribution of diffusion coefficients which has abrupt, discontinuous, changes near to the baseline as a consequence of the non-negativity constraint. Similar effects have been observed in the Tikhonov regularization to recover radical pair re-encounter probabilities from magnetic field effect data [29]. The L = I recovered distribution is also slightly broader than the model it is trying to restore, more so with the use of L-curve (Fig. 4a) than the GCV method (Fig. 4b). The operator L allows additional information to be incorporated into the analysis, such as requiring any reasonable distribution of diffusion coefficients to be smooth. This can be incorporated by setting L = D 2, with the results being shown as the dashed lines in Fig. 4. This requirement that the distribution should be smooth results in a recovered distribution which more closely agrees with the model input distribution. The slight mismatch in intensity is the result of an artefact peak at 1.0 -10  8 m 2 s  1 which is not present in the model distribution. This artefact peak is probably due to numerical inaccuracies arising at the ends of the approximate D 2 operator.

In the case of a bimodal model distribution, again, the L-curve ( k c = 0.1235) and GCV ( k min = 0.0875) methods appear to perform similarly, as shown in Fig. 4c and d respectively. As observed for the unimodal case, the use of the identity, L = I , does not recover accurately the shape or centre positions of the two components of the input distribution. There is a noticeable shift to larger diffusion coefficients in the location of the more rapidly diffusing component at 2.0 -10  9 m 2 s  1 . This shift is an artefact of using the NNLS algorithm, as has been noted previously by Prange and Song

Fig. 4. Recovered diffusion coefficient distributions for unimodal and bimodal synthetic models, showing the influence of the matrix L and the parameter choice method: (a) unimodel, L-curve method; (b) unimodel, GCV method; (c) bimodal, L-curve method; and (d) bimodal, GCV method.

<!-- image -->

[22] in the analysis of T 2 relaxation distributions. When using L = D 2 the component at 3.0 -10  10 m 2 s  1 is recovered well by both methods, while the faster diffusing component is slightly reduced in intensity. The excellent recovery of the input distribution by both methods suggests that the ''ideal'' value of the regularization parameter is located somewhere between the values obtained from the L-curve and the GCV method.

## 3.2. Aggregation of sunset yellow FCF

Sunset yellow FCF is a well studied azo-dye known at ambient temperatures to form lyotropic liquid crystals at high concentrations [39,40,42,43], and form aggregates of tens to hundreds of molecules at lower concentrations [39,41,42]. Previous studies of this compound have focused on the use of optical and X-ray scattering techniques to probe the state of aggregation [39,42]. Recently, we have employed diffusion NMR methods, under the assumption that the aggregates are in a state of fast exchange, both with each other, and with pools of monomer in solution [41]. This assumption allowed the observed echo attenuation to be modelled using a single exponential function yielding an observed diffusion coefficient which is the population-weighted average of the diffusion coefficients for all the species present in the solution [5]. Here we apply Tikhonov regularization to invert Eq. (3) to directly obtain the distribution of diffusion coefficients and hence information on the distribution of aggregated species present in the NMR tube.

Following the same approach to that used for the synthetic data above, Tikhonov regularization was used employing L = D 2 and the non-negativity constraint as these yield the most accurate reconstruction of the diffusion coefficient distribution. For the majority of the sunset yellow samples the GCV approach fails, due to the inability to locate a suitable minimum. The GCV function for the samples at concentrations of 0.10 M and above, does not show a global minimum, and hence this method cannot be used to locate a suitable value of the regularization parameter. For the 1.64 mM sample, a minimum was located at k min = 1.736 -10  4 , which results in the recovered distribution having a very narrow, physically unrealistic, shape. These problems are a known pitfall of using the GCV as a parameter choice method [30].

Using the L-curve method to select the regularization parameter was more successful. The results of this analysis for a series of typical concentrations spanning those studied previously [41] are shown in Fig. 5a. The recovered distributions are all reasonably narrow and centred at similar values of the diffusion coefficient to those determined using a mono-exponential fit to the echo attenuation profile, consistent with the formation of larger aggregates at higher concentrations [41]. The narrowness of the recovered distributions is in agreement with the fact that these aggregated assemblies of sunset yellow molecules are in the fast exchange regime, with exchange occurring both between aggregates and free monomers. This is in agreement with previous studies on this system [41].

The Tikhonov filter factors for this system are plotted in Fig. 5b. As for the example data in Fig. 3c, it is clear that only the first few singular values significantly contribute to the recovered distributions, with the remaining filter factors decreasing rapidly as a function of index. Similar trends are observed for all six samples, with only minor variations arising due to the different optimal regularization parameter chosen for each sample.

## 3.3. Polymer size distributions

Another common application of PGSE diffusion NMR methods is the determination of polymer molecular weight distributions [17,44]. These parameters are important for understanding the behaviour and reactivity of polymers in solution. In principle, obtaining these data from NMR spectroscopy should be simpler and require significantly less sample preparation and solvent than more traditional approaches such as size-exclusion chromatography.

Fig. 5. (a) Distributions of diffusion coefficients recovered from the Tikhonov regularization of diffusion NMR data for six samples of the azo dye sunset yellow at six concentrations of 1.64 mM, 0.10 M, 0.30 M, 0.49 M, 0.74 M and 0.90 M in deuterium oxide, similar to those used in a previous study [41], (b) shows the first 15 (out of 64) filter factors derived from the optimal k c values for each sunset yellow concentration.

<!-- image -->

Solutions of poly(styrene 4-sulphonate) molecular weight reference standards, at a concentration of 1 mM, were investigated using the same approach as for the sunset yellow solutions and the results are shown in Fig. 6a. Tikhonov regularization was performed using L = D 2 with the non-negativity constraint. The regularization parameter was chosen using the L-curve method. Reasonably narrow unimodal distributions of diffusion coefficients are observed for all the samples, in line with the fact that the samples have low polydispersity, typically &lt;1.20. The 14.9 kDa sample does, however, show a significantly broader distribution that obtained for the other samples. As observed for the test data and some of sunset yellow distributions, artefacts are observed at the high diffusion coefficient end of the recovered distribution. Evidence that this is merely a numerical artefact was obtained by constructing the Stejskal-Tanner matrix to span a different range of diffusion coefficients results in the artefact peak being consistently observed at the high end of the scale, while the peaks corresponding to the polymer reference standards remain at constant D (data not shown). The filter factors, not shown, for the polymer reference standard data show the same trends as for both the example data (Fig. 3c) and the sunset yellow data (Fig. 5b), with only the first 7 or so singular values contributing to the recovered distribution.

The diffusion NMR data can be further used to extract characteristic parameters for the investigated polymer. The viscosity of

<!-- image -->

-10

(q)

-10.25

-10.5

-10.75

log(D)

-11

-11.25

-11.5

4

4.2

4.4

4.6

4.8

log(Mw)

Fig. 6. (a) Polymer diffusion coefficient distributions obtained for 1 mM samples, in D2O, of several poly(styrene 4-sulphonate) molecular weight reference standards with polydispersities typically &lt;1.20. The quoted molecular weights are the weightaveraged molecular weights Mw . (b) Mark-Houwink analysis of the diffusion coefficients at the peaks of the diffusion coefficient distributions. The solid line is the linear regression on all five data points, while the dashed line is the same excluding the largest reference standard (63.9 kDa).

a polymer solution can be related to the molecular weight of the polymer solute via the Mark-Houwink equation:

$$\eta = K M ^ { \alpha } \intertext { \eta = K M ^ { \alpha } } \intertext { \eta = K M ^ { \alpha } }$$

where the coefficients K and a depend on the properties of both the solvent and polymer [45]. The viscosity of a polymer solution can also be related to the diffusion coefficient, i.e. the hydrodynamic properties of the molecule, using the Stokes-Einstein equation [4,5], therefore a log-log plot of diffusion coefficient versus molecular weight should yield a straight line with gradient and intercept given by the Mark-Houwink parameters a and K 0 ¼ kT = 4 p rK respectively [45]. This plot, using the peak centres of the returned distributions, is shown in Fig. 6b, with the line of best fit yielding a value of a =  1.11, shown as the solid line in Fig. 6b, which is typical for a polyelectrolyte such as poly(styrene 4-sulphonate) in a solution of low ionic strength [46]. Since the polymer solutions are in the semi-dilute to concentrated regime [47], the highest molecular weight data point (concentrated regime) was dropped, and the remaining data refitted, yielding a revised value of a = 0.78 (dashed line in Fig. 6b) which is in excellent agreement with literature values of a = 0.78-0.89 depending on solution ionic strength [48].

## 4. Conclusions

The inversion (inverse Laplace transform) of NMR diffusion data is known to be an ill-posed problem which requires numerical stabilisation in order to yield meaningful results. In this paper we update the CONTIN approach of using Tikhonov regularization and demonstrate two methods for automatically choosing the value regularization parameter. Both parameter choice methods perform well for synthetic data, accurately recovering the model distributions of diffusion coefficients. However, the GCV approach is less stable in the case of real experimental data due to potential robustness issues with the flat minimum of the GCV function. In general, therefore, the L-curve method should be preferred. The Tikhonov regularization solution and parameter choice via the Lcurve method are both straightforward to compute from the singular value decomposition of the Stejskal-Tanner matrix. Applications to real systems have been demonstrated for the aggregation of the azo dye sunset yellow and for some polymer molecular weight reference standards. In both cases, parameters are obtained which describe realistically the underlying distributions of diffusion coefficients.

## Acknowledgments

The author thanks C.T. Rodgers for helpful discussions and critical reading of the manuscript. This work was supported by the University of Sussex and the EPSRC (EP/H025367/1).

## References

- [1] E.O. Stejskal, J.E. Tanner, Spin diffusion measurements: spin echos in the presence of a time-dependent field gradient, J. Chem. Phys. 42 (1965) 288-292.
- [2] J.E. Tanner, Use of the stimulated echo in NMR diffusion studies, J. Chem. Phys. 52 (1970) 2523-2526.
- [3] P.T. Callaghan, Principles of Nuclear Magnetic Resonance Microscopy, Oxford Science Publications, 1991.
- [4] C.S. Johnson, Diffusion ordered nuclear magnetic resonance spectroscopy: principles and applications, Prog. NMR. Spectrosc. 34 (1999) 203-256.
- [5] W.S. Price, NMR Studies of Translational Motion, Cambridge University Press, 2009.
- [6] M.S. Hill, P.B. Hitchcock, R. Pongtavornpinyo, Solidand solution-state structures of indium 'alkene analogues', Dalton Trans. (2007) 731-733.
- [7] M. Nilsson, I.F. Duarte, C. Almeida, I. Delgadillo, B.J. Goodfellow, A.M. Gil, G.A. Morris, High-resolution NMR and diffusion-ordered spectroscopy of port wine, J. Agric. Food Chem. 52 (2004) 3736-3743.
- [8] M. Nilsson, M.A. Connell, A.L. Davis, G.A. Morris, Biexponential fitting of diffusion-ordered NMR data: practicalities and limitations, Anal. Chem. 78 (2006) 3040-3045.
- [9] W. Windig, J.P. Hornak, B. Antalek, Multivariate image analysis of magnetic resonance images with the direct exponential curve resolution algorithm (DECRA) Part 1: algorithm and model study, J. Magn. Reson. 132 (1998) 298306.
- [10] B. Antalek, J.P. Hornak, W. Windig, Multivariate image analysis of magnetic resonance images with the direct curve resolution algorithm (DECRA) Part 2: application to human brain images, J. Magn. Reson. 132 (1998) 307-315.
- [11] P. Stilbs, K. Paulsen, P.C. Griffiths, Global least-squares analysis of large, correlated spectral data sets: application to component-resolved FT-PGSE NMR spectroscopy, J. Phys. Chem. 100 (1996) 8180-8189.
- [12] B. Antalek, W. Windig, Generalized rank annihilation method applied to a single multicomponent pulsed gradient spin echo NMR data set, J. Am. Chem. Soc. 118 (1996) 10331-10332.
- [13] M. Nilsson, G.A. Morris, Speedy component resolution: an improved tool for processing diffusion-ordered spectroscopy data, Anal. Chem. 80 (2008) 37773782.
- [14] M.A. Delsuc, T.E. Malliavin, Maximum entropy processing of DOSY NMR spectra, Anal. Chem. 70 (1998) 2146-2148.
- [15] G.S. Armstrong, N.M. Loening, J.E. Curtis, A.J. Shaka, V.A. Mandelshtam, Processing DOSY spectra using the regularized resolvent transform, J. Magn. Reson. 163 (2003) 139-148.
- [16] R.C.O. Sebastiao, C.N. Pacheco, J.P. Braga, D. Pilo-Vesolo, Diffusion coefficient distribution from NMR-DOSY experiments using Hopfield neural network, J. Magn. Reson. 182 (2006) 22-28.
- [17] A. Chen, D. Wu, C.S. Johnson, Determination of molecular weight distributions for polymers by diffusion-ordered NMR, J. Am. Chem. Soc. 117 (1995) 79657970.
- [18] P. Barone, A. Ramponi, G. Sebastiani, On the numerical inversion of the Laplace transform for nuclear magnetic resonance relaxometry, Inverse Probl. 17 (2001) 77-94.
- [19] R. Kimmich, E. Anoardo, Field-cycling NMR relaxometry, Prog. NMR Spectrosc. 44 (2004) 257-320.
- [20] A.A. Istratov, O.F. Vyvenko, Exponential analysis in physical phenomena, Rev. Sci. Instrum. 70 (1999) 1233-1257.

- [21] C.L. Lawson, R.J. Hanson, Solving Least Squares Problems, SIAM, Philadelphia, 1995.
- [22] M. Prange, Y.-Q. Song, Quantifying uncertainty in NMR T 2 spectra using Monte Carlo inversion, J. Magn. Reson. 196 (2009) 54-60.
- [23] K.F. Morris, C.S. Johnson, Resolution of discrete and continuous molecular size distributions by means of diffusion-ordered 2D NMR spectroscopy, J. Am. Chem. Soc. 115 (1993) 4291-4299.
- [24] J. Frandsen, A. Hobolth, L. Ostergraad, P. Vestergraad-Poulsen, E.B. Vedel Jensen, Bayesian regularization of diffusion tensor images, Biostatistics 8 (2007) 784-799.
- [25] S.W. Provencher, A constrained regularization method for inverting data represented by linear algebraic or integral equations, Comput. Phys. Commun. 27 (1982) 229-242.
- [26] R. Bro, S. de Jong, A fast non-negativity-constrained least squares algorithm, J. Chemometr. 11 (1997) 393-401.
- [27] J.D. van Beek, B.H. Meier, H. Schaefer, Inverse methods in two-dimensional NMR spectral analysis, J. Magn. Reson. 162 (2003) 141-157.
- [28] Y.-W. Chiang, P.P. Borbat, J.H. Freed, The determination of pair distance distributions by pulsed EPR using Tikhonov regularization, J. Magn. Reson. 172 (2005) 279-295.
- [29] C.T. Rodgers, S.A. Norman, K.B. Henbest, C.R. Timmel, P.J. Hore, Determination of radical re-encounter probability distributions from magnetic field effects on reaction yields, J. Am. Chem. Soc. 129 (2007) 6746-6755.
- [30] P.C. Hansen, Rank-deficient and Discrete Ill-posed Problems: Numerical Aspects of Linear Inversion, SIAM, Philadelphia, 1998.
- [31] G.H. Golub, C.F. van Loan, Matrix Computations, Johns Hopkins University Press, Baltimore, 1996.
- [32] Y.-Q. Song, L. Venkataramanan, L. Burcaw, Determining the resolution of Laplace inversion spectrum, J. Chem. Phys. 122 (2005) 104104.
- [33] P.C. Hansen, Analysis of discrete ill-posed problems by means of the L-curve, SIAM Rev. 34 (1992) 561-580.
- [34] P.C. Hansen, Regularization tools version 4.0 for Matlab 7.3, Numer. Algorithms 46 (2007) 189-194.
- [35] E. Jones, T. Oliphant, P. Peterson, SciPy: open source scientific tools for Python, 2001.
- [36] P.C. Hansen, Regularization tools: a Matlab package for analysis and solution of discrete ill-posed problems, Numer. Algorithms 6 (1994) 1-35.
- [37] M.D. Pelta, G.A. Morris, M.J. Stchedroff, S.J. Hammond, A one-shot sequence for high resolution diffusion-ordered spectroscopy, Magn. Reson. Chem. 40 (2002) S147-S152.
- [38] F. Delaglio, S. Grzesiek, G.W. Vuister, G. Zhu, J. Pfeifer, A. Bax, NMRPipe: a multidimensional spectral processing system based on UNIX pipes, J. Biomol. NMR 6 (1995) 277-293.
- [39] V.R. Horowitz, L.A. Janowitz, A.L. Modic, P.A. Heiney, P.J. Collings, Aggregation behavior and chromonic liquid crystal properties of an anionic monoazo dye, Phys. Rev. E 72 (2005) 041710.
- [40] H.-S. Park, S.-W. Kang, L. Tortora, Y. Nastishin, D. Finotello, S. Kumar, O.D. Lavrentovich, Self-assembly of lyotropic chromonic liquid crystal sunset yellow and effects of ionic additives, J. Phys. Chem. B 112 (2008) 1630716319.
- [41] M.P. Renshaw, I.J. Day, NMR characterization of the aggregation state of the azo dye sunset yellow in the isotropic phase, J. Phys. Chem. B 114 (2010) 10032-10038.
- [42] D.J. Edwards, J.W. Jones, O. Lozman, A.P. Ormerod, M. Sintyureva, G.J.T. Tiddy, Chromonic liquid crystal formation by edicol sunset yellow, J. Phys. Chem. B 112 (2008) 14628-14636.
- [43] S.K. Prasad, G.G. Nair, G. Hegde, V. Jayalakshmi, Evidence of wormlike micellar behaviour in chromonic liquid crystals: rheological, X-ray and dielectric studies, J. Phys. Chem. B 111 (2007) 9741-9746.
- [44] B. Hakansson, M. Nyden, O. Soderman, The influence of polymer molecular weight distributions on pulsed gradient nuclear magnetic resonance selfdiffusion measurements, Colloid Polym. Sci. 278 (2000) 399-405.
- [45] M. Rubinstein, R.H. Colby, Polymer Physics, Oxford University Press, Oxford, 2003.
- [46] J.Z. Knaul, V.T. Bui, K.A.M. Creber, Viscometric constants for sodium polystyrene sulfonate standards in solvents of 0.1M CH3COOH/0.2M NaCl and 0.2M CH3COOH/0.1M CH3COONa at 25 ° C, J. Chem. Eng. Data 45 (2000) 508-511.
- [47] F. Gruner, W.P. Lehmann, H. Fahlbusch, R. Weber, Dynamics of Na + polystyrene sulfonate in solution at low ionic strength, J. Phys. A Math. General 14 (1981) L307-L313.
- [48] J. Brandrup, E.H. Immergut, Polymer Handbook, John Wiley and Sons, London, 1975.