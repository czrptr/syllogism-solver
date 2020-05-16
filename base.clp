(defrule ALL_ALL
	(ALL ?S1 ?P1)
	(ALL ?P1 ?P2)
	=>
	(assert (ALL ?S1 ?P2))
)

(defrule ALL_NO
	(ALL ?S1 ?P1)
	(NO ?P1 ?P2)
	=>
	(assert (NO ?S1 ?P2))
)

(defrule ALL_SOME_SUBSET
	(ALL ?S1 ?P1)
	=>
	(assert (SOME ?S1 ?P1))
)

(defrule ALL_SPECIFIC
	(SPECIFIC ?S1 ?P1)
	(ALL ?P1 ?P2)
	=>
	(assert (SPECIFIC ?S1 ?P2))
)

(defrule NO_ALL
	(NO ?S1 ?P1)
	(ALL ?P1 ?P2)
	=>
	(assert (NO ?S1 ?P2))
)

(defrule NO_SOMENO_SUBSET
	(NO ?S1 ?P1)
	=>
	(assert (SOMENO ?S1 ?P1))
)

(defrule NO_SPECIFIC_NO
	(SPECIFIC ?S1 ?P1)
	(NO ?P1 ?P2)
	=>
	(assert (SPECIFICNO ?S1 ?P2))
)

(defrule SOME_ALL
	(SOME ?S1 ?P1)
	(ALL ?P1 ?P2)
	=>
	(assert (SOME ?S1 ?P2))
)

(defrule SOMENO_ALL
	(SOMENO ?S1 ?P1)
	(ALL ?P1 ?P2)
	=>
	(assert (SOMENO ?S1 ?P2))
)

(reset)
(run)
(facts)
(exit)
