# This file was automatically created by FeynRules 2.4.72
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Thu 8 Aug 2019 15:26:29


from object_library import all_orders, CouplingOrder


NP = CouplingOrder(name = 'NP',
                   expansion_order = 2,
                   hierarchy = 1)

QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 2,
                    perturbative_expansion=1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 4)

