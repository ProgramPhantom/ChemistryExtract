## Chapter 3

## Polymer Molecular Weight

## 3.1 Introduction

Polymer molecular weight is important because it determines many physical properties. Some examples include the temperatures for transitions from liquids to waxes to rubbers to solids and mechanical properties such as stiffness, strength, viscoelasticity, toughness, and viscosity. If molecular weight is too low, the transition temperatures and the mechanical properties will generally be too low for the polymer material to have any useful commercial applications. For a polymer to be useful it must have transition temperatures to waxes or liquids that are above room temperatures and it must have mechanical properties sufficient to bear design loads.

For example, consider the property of tensile strength. Figure 3.1 shows a typical plot of strength as a function of molecular weight. At low molecular weight, the strength is too low for the polymer material to be useful. At high molecular weight, the strength increases eventually saturating to the infinite molecular weight result of S ∞ . The strength-molecular weight relation can be approximated by the inverse relation

$$S = S _ { \infty } - \frac { A } { M }$$

where A is a constant and M is the molecular weight. Many properties have similar molecular weight dependencies. They start at a low value and eventually saturate at a high value that is characteristic for infinite or very large molecular weight.

Unlike small molecules, however, the molecular weight of a polymer is not one unique value. Rather, a given polymer will have a distribution of molecular weights. The distribution will depend on the way the polymer is produced. For polymers we should not speak of a molecular weight, but rather of the distribution of molecular weight, P ( M ), or of the average molecular weight, 〈 M 〉 . Polymer physical properties will be functions of the molecular weight distribution function as in

$$S = S _ { \infty } - \frac { A } { F [ P ( M ) ] }$$

Figure 3.1: A typical plot of tensile strength as a function of molecular weight.

<!-- image -->

where F [ P ( M )] is some function of the complete molecular weight distribution function. For some properties, F [ P ( M )] my reduce to simply an average molecular weight. The property will thus be a function of the average molecular weight, 〈 M 〉 , and insensitive to other the details of the molecular weight distribution function:

$$S = S _ { \infty } - \frac { A } { \langle M \rangle }$$

There are many ways, however, to calculate an average molecular weight. The question therefore is how do you define the average molecular weight for a given distribution of molecular weights. The answer is that the type of property being studied will determine the desired type of average molecular weight. For example, strength properties may be influenced more by high molecular weight molecules than by low molecular weight molecules and thus the average molecular weight for strength properties should be weighted to emphasize the presence of high molecular weight polymer. In this chapter we consider several ways of calculating molecular weights. We also consider the meanings of those averages. Finally, we consider typical distributions of molecular weights.

## 3.2 Number Average Molecular Weight

Consider a property which is only sensitive to the number of molecules present - a property that is not influenced by the size of any particle in the mixture. The best example of such properties are the colligative properties of solutions such as boiling point elevation, freezing point depression, and osmotic pressure. For such properties, the most relevant average molecular weight is the total weight of polymer divided by the number of polymer molecules. This average molecular weight follows the conventional definition for the mean value of any statistical quantity. In polymer science, it is called the number average molecular weight M N .

To get a formula for M N , we must first realize that the molecular weight distribution is not a continuous function of M . Rather, only discrete values of M are allowed. The possible values of M are the various multiples of the monomer molecular weight M 0 . By monomer molecular weight we mean the weight per monomer that appears in the polymer chain. For condensation reactions, for example, where molecules of water are typically lost from the monomers during reaction, we will take M 0 as the monomer molecular weight less any weight loss due to the polymerization reaction. The possible values of M make up a set of numbers with discrete values labeled M i . Let N i be the number of polymers with molecular weight M i . Then the total weight of all polymers is

$$T o tal Wei g h t = \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i }$$

and the total number of polymer molecules is

$$T o tal N u m b e r = \sum _ { i = 1 } ^ { \infty } N _ { i }$$

As discussed above, the number average molecular weight is

$$\overline { M _ { N } } = \frac { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } } { \sum _ { i = 1 } ^ { \infty } N _ { i } } = \frac { \text {Total Weight} } { \text {Number of Polymerors} } = \frac { \text {Weight} } { \text {Polymer} }$$

The term N i / ∑ N i is physically the number fraction of polymers with molecular weight M i . If we denote number fraction as X i ( i.e. , mole fraction) the number average molecular weight is

$$\overline { M _ { N } } = \sum _ { i = 1 } ^ { \infty } X _ { i } M _ { i }$$

In lab experiments it is more common to measure out certain weights of a polymer rather than certain numbers of moles of a polymer. It is thus useful to derive an alternate form for M N in terms or weight fraction of polymers with molecular weight M i denoted as w i . First we note that the concentration of polymer species i is (in weight per unit volume):

$$c _ { i } = \frac { N _ { i } M _ { i } } { V }$$

Inserting c i for N i M i and expressing N i in terms of c i results in

$$\overline { M _ { N } } = \frac { \sum _ { i = 1 } ^ { \infty } c _ { i } } { \sum _ { i = 1 } ^ { \infty } \frac { c _ { i } } { M _ { i } } }$$

Dividing numerator and denominator by ∑ c i results in

$$\overline { M _ { N } } = \frac { 1 } { \sum _ { i = 1 } ^ { \infty } \frac { w _ { i } } { M _ { i } } }$$

where w i is the weight fraction of polymer i or the weight of polymer i divided by the total polymer weight:

$$w _ { i } = \frac { N _ { i } M _ { i } } { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } } = \frac { c _ { i } } { \sum _ { i = 1 } ^ { \infty } c _ { i } }$$

## 3.3 Weight Average Molecular Weight

Consider of polymer property which depends not just on the number of polymer molecules but on the size or weight of each polymer molecule. A classic example is light scattering. For such a property we need a weight average molecular weight. To derive the weight average molecular weight, replace the appearance of the number of polymers of molecular weight i or N i in the number average molecular weight formula with the weight of polymer having molecular weight i or N i M i . The result is

$$\overline { M _ { W } } = \frac { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } ^ { 2 } } { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } }$$

By noting that N i M i / ∑ N i M i is the weight fraction of polymer with molecular weight i , w i , an alternative form for weight average molecular weight in terms of weight fractions

$$\overline { M _ { W } } = \sum _ { i = 1 } ^ { \infty } w _ { i } M _ { i }$$

Comparing this expression to the expression for number average molecular weight in terms of number fraction (see Eq. (3.7)) we see that M N is the average M i weighted according to number fractions and that M W is the average M i weighted according to weight fractions. The meanings of their names are thus apparent.

## 3.4 Other Average Molecular Weights

To get M W from M N we replaced N i by N i M i . We can generalize this process and replace N i by N i M k i to get an average molecular weight denoted as M k :

$$\overline { M _ { k } } = \frac { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } ^ { k + 1 } } { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } ^ { k } }$$

Thus M 0 = M N , and M 1 = M W . Several other M k forms appear in experiments. Two examples are M 2 = M z and M 3 = M z +1 which are used in analysis of ultracentrifugation experiments.

One average molecular weight which does not fit into the mold of M k is the viscosity average molecular weight or M v . It is defined by

$$\overline { M _ { v } } = \left ( \frac { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } ^ { 1 + a } } { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } } \right ) ^ { \frac { 1 } { a } }$$

Figure 3.2: A schematic plot of a distribution of molecular weights along with the rankings of the various average molecular weights.

<!-- image -->

where a is a constant that depends on the polymer/solvent pair used in the viscosity experiments. Viscosity average molecular weight and viscosity experiments are discussed in Chapter 6.

For any molecular weight distribution, the various average molecular weights always rank in the order

$$\overline { M _ { N } } \leq \overline { M _ { v } } \leq \overline { M _ { W } } \leq \overline { M _ { z } } \leq \overline { M _ { z + 1 } } \leq \overline { M _ { 4 } } \leq \dots$$

̸

The equalities hold only when the polymer is monodisperse; i.e. , only when all molecules have the same molecular weight. For monodisperse polymers all molecular weight averages are the same and equal to the one molecular weight. For polydisperse polymers, the average molecular weights will all be different and will rank in the above order. Historically this fact was not always recognized thus it was sometimes difficult to reconcile conflicting experimental results. Say two scientists measured average molecular weight, but one used a colligative property which yields M N and the other used light scattering which yields M W . Until it was recognizes that M N = M W , it was difficult to explain differing experimental results on the same polymer solution.

## 3.5 A Distribution of Molecular Weights

Schematically, a typical molecular weight distribution might appear as in Fig. 3.2. It resembles a probability distribution curve. The various average molecular weights are indicated in their expected rank.

The spread of any distribution function can be characterized by its standard deviation, or equivalently by its coefficient of variation. We can express the standard deviation of molecular weight in terms of M N and M W . The definition of variance, σ 2 , is

$$\sigma ^ { 2 } = \langle M ^ { 2 } \rangle - \langle M \rangle ^ { 2 }$$

where angle brackets ( e.g. , 〈 M 〉 ) denote conventional averaging. In terms of N i and M i the variance is

$$\sigma ^ { 2 } = \frac { 1 } { N } \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } ^ { 2 } - \left ( \frac { 1 } { N } \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } \right ) ^ { 2 } = \frac { \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } ^ { 2 } \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } } { \sum _ { i = 1 } ^ { \infty } N _ { i } \sum _ { i = 1 } ^ { \infty } N _ { i } M _ { i } } - \overline { M _ { N } } ^ { 2 }$$

which in terms of M N and M W is

$$\sigma ^ { 2 } = \overline { M _ { W } } \, \overline { M _ { N } } - \overline { M _ { N } } ^ { 2 } = \overline { M _ { N } } ^ { 2 } \left ( \frac { \overline { M _ { W } } } { \overline { M _ { N } } } - 1 \right )$$

$$\sigma = \overline { M _ { N } } \sqrt { \frac { \overline { M _ { W } } } { \overline { M _ { N } } } - 1 }$$

or the standard deviation is

The coefficient of variation is the mean divided by the standard deviation. Because M N is also the conventional mean

$$C . V . = \frac { \sigma } { \overline { M _ { N } } } = \sqrt { \frac { \overline { M _ { W } } } { \overline { M _ { N } } } - 1 }$$

A key term in the coefficient of variation is M W M N . This term is known as the polydispersity index. For the coefficient of variation to be real (as it must), the polydispersity index must be greater than or equal to one. When it is equal to one, the coefficient of variation is zero which means that the distribution is monodisperse. For all real polymers it is greater that one and the amount that it is greater than one is a measure of the polydispersity of that polymer.

## 3.6 Most Probable Molecular Weight Distribution

Many condensation polymers are synthesized by the polymerization of bifunctional monomers. If we denote two functional groups as A and B than a bifunctional monomer would have an A group on one end and a B group on the other and be denoted A B . The polymerization reaction of A B is

$$n ( A - B ) \to - ( A - B ) _ { n } -$$

For example if A is an acid group ( COOH) and B is an alcohol group ( OH), the A B monomer can polymerize to a polyester. Or, if A is an acid group ( COOH) and B is an amine group ( NH 2 ) the A B monomer can polymerize to a polyamide. Flory considered the polymerization of A B type monomers and used simple statistical arguments to calculate the expected, or most probable distribution of molecular weights. His results give us insight into typical molecular weight distributions.

̸

We define p as the fraction of functional groups of type A that have reacted at a given stage of polymerization. Because A reacts by reacting with B , the fraction of functional groups of type B that have reacted at the same stage of polymerization is also p . We define p in mathematical terms but note that in practical terms it is often easily accessible by measurement. For example, to find the fraction of reacted acid A groups of type COOH, one could use simple acid/base titration experiments. Next, after some amount of polymerization ( i.e. , p = 0) we select a molecule at random. We begin at one end of the molecule which will be an unreacted A group. The probability that the adjacent B group is also unreacted is simply (1 -p ) - one minus the probability that a B group has reacted. Thus the probability that the randomly selected molecule is a monomer is

$$P ( i = 1 ) = ( 1 - p )$$

The probability that the randomly selected molecule is a dimer is equal the product of the independent probabilities that the first group is reacted ( p ) and the second in unreacted (1 -p ):

$$P ( i = 2 ) = p ( 1 - p )$$

Continuing on by induction, the probability that the randomly selected molecule has a degree of polymerization i is

$$P ( i ) = p ^ { i - 1 } ( 1 - p )$$

The p i -1 term is for the i -1 reacted functional groups in the chain and the 1 -p term is for the terminal unreacted functional group.

If there are N molecules in the polymerizing mixture, then the number of polymer chains of length i is N times the probability of having length i :

$$N _ { i } = N p ^ { i - 1 } ( 1 - p )$$

N is related to the initial number of monomers N 0 by N = N 0 (1 -p ). This relation can easily be derived be realizing that each reaction of a functional group reduces the total number of molecules by one. For extent of reaction p , the total number of molecules is reduced by N 0 p . Now, in terms of known quantities N i is

$$N _ { i } = N _ { 0 } p ^ { i - 1 } ( 1 - p ) ^ { 2 }$$

The above equation for N i describes the complete polymer distribution. It is called the most probable distribution or the Flory Distribution. Virtually all condensation polymers no matter how they are formed will end up with a distribution resembling the most probable distribution. Plots of N i for various values of p are given in Fig. 3.3. At all values of p , all molecular weights are present to some extent. The surprising results is that at all values of p , the most probable species is the monomer. This monotonically decreasing function is not the type commonly drawn to illustrate distribution functions.

Figure 3.3: The number fraction as a function of degree of polymerization for the most probable molecular weight distribution. The three curves are for three values of p .

<!-- image -->

A more familiar distribution function results if we consider the weight fraction of polymer with length i . Weight fraction is defined by

$$w _ { i } = \frac { i M _ { 0 } N _ { i } } { N _ { 0 } M _ { 0 } } = \frac { i N _ { i } } { N _ { 0 } } = i p ^ { i - 1 } ( 1 - p ) ^ { 2 }$$

where M 0 is the monomer molecular weight. When the repeat of the polymer has lower molecular weight than the monomer, because of reaction products such as H 2 O loss due to condensation, M 0 should be the molecular weight of the monomer that makes it into the polymer. In other words, M 0 is the repeat unit molecular weight, iM 0 is the molecular weight of a polymer of length i , and N 0 M 0 is the total weight of monomer that ends up in a polymer. Some plots of weight fraction for various values of p are given in Fig. 3.4. The most prevalent species is no longer the monomer. Although there will be a lot of monomers, each monomer weighs very little. As time of reaction increases, which increases p , the peak in the weight fraction shifts to higher values and the distribution curve broadens. The peak molecular weight turns out to be very close to M N expecially as p is close to 1 (see problem 3 at end of this chapter)

Now that we have a complete distribution function ( i.e. , an equation for N i ) we can calculate M N and M W . We can calculate M N for the most probable distribution using two methods. First we evaluate the sums in the number average molecular weight formula:

$$\overline { M _ { N } } = \frac { \sum _ { i = 1 } ^ { \infty } i M _ { 0 } N _ { i } } { \sum _ { i = 1 } ^ { \infty } N _ { i } } = M _ { 0 } ( 1 - p ) \sum _ { i = 1 } ^ { \infty } i p ^ { i - 1 }$$

Figure 3.4: The weight fraction as a function of degree of polymerization for the most probable molecular weight distribution. The three curves are for three values of p.

<!-- image -->

The evaluation of the sum is nontrivial. The sum, however, can be expressed as the derivative of another sum which is simpler to evaluate.

$$\sum _ { i = 1 } ^ { \infty } i p ^ { i - 1 } = \frac { d } { d p } \sum _ { i = 1 } ^ { \infty } p ^ { i } = \frac { d } { d p } \left ( \frac { p } { 1 - p } \right )$$

Evaluating the derivative gives

$$\sum _ { i = 1 } ^ { \infty } i p ^ { i - 1 } = \frac { 1 } { ( 1 - p ) ^ { 2 } }$$

Multiplying by M 0 (1 -p ) gives

$$\overline { M _ { N } } = \frac { M _ { 0 } } { 1 - p }$$

An alternative and simpler method to M N is to realize that, by conservation of mass, the total weight of material is always M 0 N 0 . From above, the total number of polymers is N 0 (1 -p ). Thus

$$\overline { M _ { N } } = \frac { \text {Total weight of polymer} } { \text {Total number of polymers} } = \frac { M _ { 0 } N _ { 0 } } { N _ { 0 } ( 1 - p ) } = \frac { M _ { 0 } } { 1 - p }$$

To get M W for the most probable distribution we use the weight average molecular weight formula in terms of weight fractions:

$$\overline { M _ { W } } = \sum _ { i = 1 } ^ { \infty } w _ { i } i M _ { 0 } = M _ { 0 } ( 1 - p ) ^ { 2 } \sum _ { i = 1 } ^ { \infty } i ^ { 2 } p ^ { i - 1 }$$

We evaluate the sum using the trick used to find M N and some additional work.

$$\sum _ { i = 1 } ^ { \infty } i ^ { 2 } p ^ { i - 1 } = \frac { d } { d p } \sum _ { i = 1 } ^ { \infty } i p ^ { i } = \frac { d } { d p } \left ( p \sum _ { i = 1 } ^ { \infty } p ^ { i - 1 } \right ) = \frac { d } { d p } \left ( \frac { p } { ( 1 - p ) ^ { 2 } } \right )$$

The last step uses the result from the M N calculation. Evaluating the derivative gives

$$\sum _ { i = 1 } ^ { \infty } i ^ { 2 } p ^ { i - 1 } = \frac { 1 + p } { ( 1 - p ) ^ { 3 } }$$

Multiplying by M 0 (1 -p ) 2 gives the final result:

$$\overline { M _ { W } } = M _ { 0 } \frac { 1 + p } { 1 - p }$$

Combining the results for M N and M W , the polydispersity index for the most probable distribution is

$$\frac { \overline { M _ { W } } } { \overline { M _ { N } } } = 1 + p$$

As the reaction nears completion, p approaches one and the polydispersity index approaches 2. That is the coefficient of variation of the most probable distribution is 100%. That large of a coefficient of variation means that the molecular weight distribution is relatively broad.

We also notice that as p approaches one, both M N and M W approach infinity. This limit means that all the monomers will be in a single polymer molecule. It is usually not desirable to have molecular weights that are too high. Such polymers would not be processible; they would not flow when melted. To avoid unprocessible polymers, it is desirable to use methods to control molecular weight. One way to control molecular weight would be to freeze the reaction at some p less than one. This scheme, however, can produce a material that is unstable with time. Instability occurs if over long times, there are more reactions (albeit at a slow rate) which cause p to increase. When p increases, the polymer properties change with time and might eventually give a molecular weight that is too high to be processible.

One solution to molecular weight control is to polymerize the two monomers A A and B B instead of the single monomer A B . If the two monomers are mixed in equal proportions, the analysis will be identical to the one above and there will be no molecular weight control (note: although the analysis is the same, the meaning of M 0 has to be changed to be half the repeat unit molecular weight to account for the fact that the synthesis is from two monomers ( A -A and B -B ) instead of from one monomer ( A -B )). If the proportions are unequal and r = N A /N B &lt; 1 then the results are different. A more complicated analysis gives the following M N :

$$\overline { M _ { N } } = \frac { M _ { 0 } ( 1 + r ) } { 1 + r - 2 r p } \approx \frac { M _ { 0 } ( 1 + r ) } { 1 - r }$$

where, as explained above, M 0 is half the repeat unit molecular weight. The second part of this equation assumes p is equal to one. Sample calculations for various values of r give

$$r = 1 . 0 0 \quad \overline { M _ { N } } = \infty$$

$$r = 0 . 9 9 & & \overline { M _ { N } } = 1 9 9 M _ { 0 }$$

$$r = 0 . 9 5 & & M _ { N } = 3 9 M _ { 0 }$$

$$r = 0 . 9 0 \quad \overline { M _ { N } } = 1 9 M _ { 0 }$$

$$\overline { M _ { N } } = \infty 
 \overline { M _ { N } } = 1 9 9 M _ { 0 } 
 \overline { M _ { N } } = 3 9 M _ { 0 } 
 \overline { M _ { N } } = 1 9 M _ { 0 }$$

By selecting r , we see it is possible to control molecular weight to some finite value. Physically what happens is that the monomer mixture runs out of A A and all polymers are end capped with B B monomers. Because B can only react with A and no unreacted A remains, the reaction stops at a finite molecular weight. The only problem is that small changes in r lead to large changes in M N . For example a 5% deviation of r from 1.00 reduces the molecular weight from infinite to 39 M 0 . But, 39 M 0 is not a very high molecular weight and may not be high enough to be useful. To prevent polymerization from stopping at low molecular weights, you must have accurate control over r . Also you must account for any side reactions and monomer volatility which might remove monomer of one type and effectively change r .

## Problems

- 3-1. Suppose you have n batches of polydisperse polymers. Let N i,j be the number of polymers of type j with degree of polymerization i and M i,j be the molecular weight of that polymer. The basic M N and M W equations for the total mixture of polymers now require double sums:

$$\overline { M _ { N } } = \frac { \sum _ { j = 1 } ^ { n } \sum _ { i } N _ { i , j } M _ { i , j } } { \sum _ { j = 1 } ^ { n } \sum _ { i } N _ { i , j } } \quad \text { and } \quad \overline { M _ { W } } = \frac { \sum _ { j = 1 } ^ { n } \sum _ { i } N _ { i , j } M _ { i , j } ^ { 2 } } { \sum _ { j = 1 } ^ { n } \sum _ { i } N _ { i , j } M _ { i , j } }$$

Now, assume that the number average and weight average molecular weights of batch j are M Nj and M Wj . and that you mix a weight w j of each batch to make a new polymer blend.

- a. Starting from the above basic number average molecular weight definition, show that the number average molecular weight of the blend is

$$\overline { M _ { N } } = \frac { w _ { 1 } + w _ { 2 } + \cdots + w _ { n } } { \frac { w _ { 1 } } { M _ { N } } + \frac { w _ { 2 } } { M _ { N } } + \cdots + \frac { w _ { n } } { M _ { N } } }$$

In other words, show that M N of the blend can be calculated from the individual M Nj of the components of the blend. Here M Nj has the usual definition of

$$\overline { M _ { N } } _ { j } = \frac { \sum _ { i } N _ { i , j } M _ { i , j } } { \sum _ { i } N _ { i , j } }$$

or a sum over just the polymers of component j .

- b Starting from the above basic weight average molecular weight definition, show that the weight average molecular weight of the blend is

$$\overline { M _ { W } } = \frac { w _ { 1 } \overline { M _ { W } } _ { 1 } + w _ { 2 } \overline { M _ { W } } _ { 2 } + \cdots + \omega _ { n } \overline { M _ { W } } _ { n } } { w _ { 1 } + w _ { 2 } + \cdots + w _ { n } }$$

In other words, show that M W of the blend can be calculated from the individual M Wj of the components of the blend. Here M Wj has the usual definition of

$$\overline { M _ { W } } _ { j } = \frac { \sum _ { i } N _ { i , j } M _ { i , j } ^ { 2 } } { \sum _ { i } N _ { i , j } M _ { i , j } }$$

or a sum over just the polymers of component j .

- 3-2. Calcium stearate ( Ca ( OOC ( CH 2 ) 16 CH 3 ) 2 , molecular weight = 607) is sometimes used as a lubricant in the processing of poly(vinyl chloride). A sample of pure PVC polymer with a polydispersity index of 2.8 is modifed by the addition of 3% by weight of calcium stearate. TYhe mixture of PVC and salcium stearate is found to have M N = 15 , 000 g / mol.
- a. What is the M N of the PVC part of the compound? (Hint: use the blend M N result from the previous problem.)
- b. What is the M W of the blend?
- c. What effect does the calcium stearate have on the light scattering and osmotic pressure properties of the polymer? (Hint: light scattering measures M W while osmotic pressure measures M N )
- d. What is the highest possible M N for a polymer containing 3% by weight of calcium stearate?
- 3-3. Consider the most probable molecular weight distribution:
- a. Derive an expression for P ( M ) where P ( M ) is the probability that a randomly selected polymer chain as molecular weight M . Express your result in terms of M (and not degree of polymerization i ).
- b. What molecular weight has the maximum probability?
- c. Derive an expression for w ( M ) where w ( M ) is the weight fraction of polymer that has molecular weight M . Again, express your answer in terms of M (and not x ).
- d. What molecular weight has the largest weight fraction? Express your answer in terms of the number average molecular weight.
- 3-4. Calculate the percentage conversion of functional groups required to obtain a polyester with a number-average molecular weight of 24,000 g/mol from the monomer HO(CH 2 ) 14 COOH.

- 3-5. A polyamide was prepared by bulk polymerization of hexamethyl diamine (9.22 g and molecular weight 116) and adipic acid (13.2 g and molecular weight 166) at 280 ◦ C. Analysis of the whole reaction product showed that it contained 2 . 6 × 10 -3 moles of carboxylic acid groups. Evaluate M N of the mixture. Assume it has a 'most probable distibution' and also evaluate M W .