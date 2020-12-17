# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.1.0 for Linux x86 (64-bit) (March 13, 2017)
# Date: Wed 6 Jun 2018 14:05:51


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cblS1':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cblS2':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(cblS3*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cblS3':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(cblSI1/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cblSI1':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'cblSI1/Lambda**2',
                 order = {'DIM6':1,'DIM6_cblSI1':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(cblSI2/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cblSI2':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'cblSI2/Lambda**2',
                 order = {'DIM6':1,'DIM6_cblSI2':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(cblSI3/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cblSI3':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'cblSI3/Lambda**2',
                 order = {'DIM6':1,'DIM6_cblSI3':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(cblSIx1x13/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx1x13':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'cblSIx1x13/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx1x13':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(cblSIx1x23/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx1x23':1})

GC_22 = Coupling(name = 'GC_22',
                 value = 'cblSIx1x23/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx1x23':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(cblSIx1x31/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx1x31':1})

GC_24 = Coupling(name = 'GC_24',
                 value = 'cblSIx1x31/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx1x31':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(cblSIx1x32/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx1x32':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'cblSIx1x32/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx1x32':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(cblSIx2x13/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx2x13':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'cblSIx2x13/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx2x13':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(cblSIx2x23/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx2x23':1})

GC_30 = Coupling(name = 'GC_30',
                 value = 'cblSIx2x23/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx2x23':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(cblSIx2x31/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx2x31':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'cblSIx2x31/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx2x31':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(cblSIx2x32/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx2x32':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'cblSIx2x32/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx2x32':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(cblSIx3x13/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx3x13':1})

GC_36 = Coupling(name = 'GC_36',
                 value = 'cblSIx3x13/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx3x13':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(cblSIx3x23/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx3x23':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'cblSIx3x23/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx3x23':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(cblSIx3x31/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx3x31':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'cblSIx3x31/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx3x31':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(cblSIx3x32/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cblSIx3x32':1})

GC_42 = Coupling(name = 'GC_42',
                 value = 'cblSIx3x32/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSIx3x32':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cblSx1x13*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx1x13':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cblSx1x23*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx1x23':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cblSx1x31*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx1x31':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cblSx1x32*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx1x32':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cblSx2x13*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx2x13':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cblSx2x23*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx2x23':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cblSx2x31*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx2x31':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(cblSx2x32*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx2x32':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cblSx3x13*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx3x13':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cblSx3x23*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx3x23':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cblSx3x31*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx3x31':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(cblSx3x32*complex(0,1))/Lambda**2',
                 order = {'FCNC':1,'FCNC_cblSx3x32':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(cbQqd1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbQqd1':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(cbQqd1I/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cbQqd1I':1})

GC_57 = Coupling(name = 'GC_57',
                 value = 'cbQqd1I/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbQqd1I':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cbQqd8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbQqd8':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(cbQqd8I/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cbQqd8I':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'cbQqd8I/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbQqd8I':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cbtud1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbtud1':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(cbtud1I/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cbtud1I':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'cbtud1I/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbtud1I':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(cbtud8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbtud8':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(cbtud8I/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cbtud8I':1})

GC_66 = Coupling(name = 'GC_66',
                 value = 'cbtud8I/Lambda**2',
                 order = {'DIM6':1,'DIM6_cbtud8I':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cbW*complex(0,1))/Lambda**2',
                 order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(cbWI/Lambda**2)',
                 order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_69 = Coupling(name = 'GC_69',
                 value = 'cbWI/Lambda**2',
                 order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(cbWIx13/Lambda**2)',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_71 = Coupling(name = 'GC_71',
                 value = 'cbWIx13/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(cbWIx23/Lambda**2)',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_73 = Coupling(name = 'GC_73',
                 value = 'cbWIx23/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(cbWIx31/Lambda**2)',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'cbWIx31/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(cbWIx32/Lambda**2)',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'cbWIx32/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cbWx13*complex(0,1))/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(cbWx23*complex(0,1))/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(cbWx31*complex(0,1))/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cbWx32*complex(0,1))/Lambda**2',
                 order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cQb1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQb1':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cQb8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQb8':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((cQbqu1*complex(0,1))/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cQbqu1':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cQbqu1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQbqu1':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(cQbqu1I/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cQbqu1I':1})

GC_87 = Coupling(name = 'GC_87',
                 value = 'cQbqu1I/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQbqu1I':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((cQbqu8*complex(0,1))/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cQbqu8':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cQbqu8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQbqu8':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-(cQbqu8I/Lambda**2)',
                 order = {'DIM6':1,'DIM6_cQbqu8I':1})

GC_91 = Coupling(name = 'GC_91',
                 value = 'cQbqu8I/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQbqu8I':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cQd1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1,'DIM6_cQd1':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(cqd1Ix3133/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cqd1Ix3133':1})

GC_94 = Coupling(name = 'GC_94',
                 value = 'cqd1Ix3133/Lambda**2',
                 order = {'FCNC':1,'FCNC_cqd1Ix3133':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(cqd1Ix31ii/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cqd1Ix31ii':1})

GC_96 = Coupling(name = 'GC_96',
                 value = 'cqd1Ix31ii/Lambda**2',
                 order = {'FCNC':1,'FCNC_cqd1Ix31ii':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(cqd1Ix3233/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cqd1Ix3233':1})

GC_98 = Coupling(name = 'GC_98',
                 value = 'cqd1Ix3233/Lambda**2',
                 order = {'FCNC':1,'FCNC_cqd1Ix3233':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(cqd1Ix32ii/Lambda**2)',
                 order = {'FCNC':1,'FCNC_cqd1Ix32ii':1})

GC_100 = Coupling(name = 'GC_100',
                  value = 'cqd1Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1Ix32ii':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cqd1Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd1Ix3331':1})

GC_102 = Coupling(name = 'GC_102',
                  value = 'cqd1Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1Ix3331':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(cqd1Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd1Ix3332':1})

GC_104 = Coupling(name = 'GC_104',
                  value = 'cqd1Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1Ix3332':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(cqd1x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1x3133':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(cqd1x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1x31ii':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cqd1x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1x3233':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(cqd1x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1x32ii':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cqd1x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1x3331':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(cqd1x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd1x3332':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(cQd8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQd8':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(cqd8Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd8Ix3133':1})

GC_113 = Coupling(name = 'GC_113',
                  value = 'cqd8Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8Ix3133':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(cqd8Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd8Ix31ii':1})

GC_115 = Coupling(name = 'GC_115',
                  value = 'cqd8Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8Ix31ii':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-(cqd8Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd8Ix3233':1})

GC_117 = Coupling(name = 'GC_117',
                  value = 'cqd8Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8Ix3233':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(cqd8Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd8Ix32ii':1})

GC_119 = Coupling(name = 'GC_119',
                  value = 'cqd8Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8Ix32ii':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(cqd8Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd8Ix3331':1})

GC_121 = Coupling(name = 'GC_121',
                  value = 'cqd8Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8Ix3331':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(cqd8Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqd8Ix3332':1})

GC_123 = Coupling(name = 'GC_123',
                  value = 'cqd8Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8Ix3332':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '(cqd8x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8x3133':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(cqd8x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8x31ii':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(cqd8x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8x3233':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(cqd8x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8x32ii':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(cqd8x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8x3331':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(cqd8x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqd8x3332':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cQe1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQe1':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cQe2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQe2':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(cQe3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQe3':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(cQeIx1x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQeIx1x31':1})

GC_134 = Coupling(name = 'GC_134',
                  value = 'cQeIx1x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQeIx1x31':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(cQeIx1x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQeIx1x32':1})

GC_136 = Coupling(name = 'GC_136',
                  value = 'cQeIx1x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQeIx1x32':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(cQeIx2x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQeIx2x31':1})

GC_138 = Coupling(name = 'GC_138',
                  value = 'cQeIx2x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQeIx2x31':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(cQeIx2x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQeIx2x32':1})

GC_140 = Coupling(name = 'GC_140',
                  value = 'cQeIx2x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQeIx2x32':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(cQeIx3x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQeIx3x31':1})

GC_142 = Coupling(name = 'GC_142',
                  value = 'cQeIx3x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQeIx3x31':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(cQeIx3x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQeIx3x32':1})

GC_144 = Coupling(name = 'GC_144',
                  value = 'cQeIx3x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQeIx3x32':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(cQex1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQex1x31':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cQex1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQex1x32':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(cQex2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQex2x31':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(cQex2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQex2x32':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(cQex3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQex3x31':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(cQex3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQex3x32':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(2*cQl31*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQl31':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(2*cQl32*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQl32':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(2*cQl33*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQl33':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(-2*cQl3Ix1x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix1x31':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(2*cQl3Ix1x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix1x31':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(-2*cQl3Ix1x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix1x32':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(2*cQl3Ix1x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix1x32':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(-2*cQl3Ix2x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix2x31':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(2*cQl3Ix2x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix2x31':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(-2*cQl3Ix2x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix2x32':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(2*cQl3Ix2x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix2x32':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '(-2*cQl3Ix3x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix3x31':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '(2*cQl3Ix3x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix3x31':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(-2*cQl3Ix3x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix3x32':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '(2*cQl3Ix3x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3Ix3x32':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(2*cQl3x1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3x1x31':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '(2*cQl3x1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3x1x32':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(2*cQl3x2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3x2x31':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '(2*cQl3x2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3x2x32':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(2*cQl3x3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3x3x31':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '(2*cQl3x3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQl3x3x32':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(cQlM1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQlM1':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '(cQlM2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQlM2':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(cQlM3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQlM3':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-(cQlMIx1x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQlMIx1x31':1})

GC_176 = Coupling(name = 'GC_176',
                  value = 'cQlMIx1x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMIx1x31':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(cQlMIx1x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQlMIx1x32':1})

GC_178 = Coupling(name = 'GC_178',
                  value = 'cQlMIx1x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMIx1x32':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-(cQlMIx2x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQlMIx2x31':1})

GC_180 = Coupling(name = 'GC_180',
                  value = 'cQlMIx2x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMIx2x31':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-(cQlMIx2x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQlMIx2x32':1})

GC_182 = Coupling(name = 'GC_182',
                  value = 'cQlMIx2x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMIx2x32':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-(cQlMIx3x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQlMIx3x31':1})

GC_184 = Coupling(name = 'GC_184',
                  value = 'cQlMIx3x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMIx3x31':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-(cQlMIx3x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cQlMIx3x32':1})

GC_186 = Coupling(name = 'GC_186',
                  value = 'cQlMIx3x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMIx3x32':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '(cQlMx1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMx1x31':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(cQlMx1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMx1x32':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '(cQlMx2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMx2x31':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(cQlMx2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMx2x32':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(cQlMx3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMx3x31':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '(cQlMx3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cQlMx3x32':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(cQQ1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQQ1':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(cQq11*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQq11':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-(cqq11Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq11Ix31ii':1})

GC_196 = Coupling(name = 'GC_196',
                  value = 'cqq11Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11Ix31ii':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-(cqq11Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq11Ix32ii':1})

GC_198 = Coupling(name = 'GC_198',
                  value = 'cqq11Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11Ix32ii':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-(cqq11Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq11Ix3331':1})

GC_200 = Coupling(name = 'GC_200',
                  value = 'cqq11Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11Ix3331':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-(cqq11Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq11Ix3332':1})

GC_202 = Coupling(name = 'GC_202',
                  value = 'cqq11Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11Ix3332':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cqq11x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11x31ii':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(cqq11x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11x32ii':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(cqq11x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11x3331':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cqq11x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq11x3332':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-((cQq13*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQq13':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(cQq13*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQq13':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(2*cQq13*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQq13':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '(-2*cqq13Ix31ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix31ii':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-(cqq13Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13Ix31ii':1})

GC_212 = Coupling(name = 'GC_212',
                  value = 'cqq13Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix31ii':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(2*cqq13Ix31ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix31ii':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(-2*cqq13Ix32ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix32ii':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(cqq13Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13Ix32ii':1})

GC_216 = Coupling(name = 'GC_216',
                  value = 'cqq13Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix32ii':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(2*cqq13Ix32ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix32ii':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(-2*cqq13Ix3331)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix3331':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '-(cqq13Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13Ix3331':1})

GC_220 = Coupling(name = 'GC_220',
                  value = 'cqq13Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix3331':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '(2*cqq13Ix3331)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix3331':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(-2*cqq13Ix3332)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix3332':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-(cqq13Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13Ix3332':1})

GC_224 = Coupling(name = 'GC_224',
                  value = 'cqq13Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix3332':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(2*cqq13Ix3332)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13Ix3332':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((cqq13x31ii*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13x31ii':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(cqq13x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x31ii':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(2*cqq13x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x31ii':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((cqq13x32ii*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13x32ii':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(cqq13x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x32ii':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(2*cqq13x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x32ii':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((cqq13x3331*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13x3331':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(cqq13x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x3331':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(2*cqq13x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x3331':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '-((cqq13x3332*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq13x3332':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(cqq13x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x3332':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(2*cqq13x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq13x3332':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '-(cQQ8*complex(0,1))/(6.*Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQQ8':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(cQQ8*complex(0,1))/(3.*Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQQ8':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(cQQ8*complex(0,1))/(2.*Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQQ8':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(cQq81*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQq81':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-(cqq81Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq81Ix31ii':1})

GC_243 = Coupling(name = 'GC_243',
                  value = 'cqq81Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq81Ix31ii':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-(cqq81Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq81Ix32ii':1})

GC_245 = Coupling(name = 'GC_245',
                  value = 'cqq81Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq81Ix32ii':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '(cqq81x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq81x31ii':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '(cqq81x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq81x32ii':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((cQq83*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQq83':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '(cQq83*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQq83':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(2*cQq83*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQq83':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '(-2*cqq83Ix31ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83Ix31ii':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '-(cqq83Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq83Ix31ii':1})

GC_253 = Coupling(name = 'GC_253',
                  value = 'cqq83Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83Ix31ii':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '(2*cqq83Ix31ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83Ix31ii':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '(-2*cqq83Ix32ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83Ix32ii':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-(cqq83Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq83Ix32ii':1})

GC_257 = Coupling(name = 'GC_257',
                  value = 'cqq83Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83Ix32ii':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '(2*cqq83Ix32ii)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83Ix32ii':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '-((cqq83x31ii*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq83x31ii':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '(cqq83x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83x31ii':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(2*cqq83x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83x31ii':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '-((cqq83x32ii*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqq83x32ii':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(cqq83x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83x32ii':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '(2*cqq83x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqq83x32ii':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '(cQt1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQt1':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '(cQt8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQt8':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '-((cQtQb1*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtQb1':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '(cQtQb1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtQb1':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '-(cQtQb1I/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtQb1I':1})

GC_270 = Coupling(name = 'GC_270',
                  value = 'cQtQb1I/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtQb1I':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((cQtQb8*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtQb8':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '(cQtQb8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtQb8':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '-(cQtQb8I/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtQb8I':1})

GC_274 = Coupling(name = 'GC_274',
                  value = 'cQtQb8I/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtQb8I':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '-((cQtqd1*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtqd1':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '(cQtqd1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtqd1':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '-(cQtqd1I/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtqd1I':1})

GC_278 = Coupling(name = 'GC_278',
                  value = 'cQtqd1I/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtqd1I':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '-((cQtqd8*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtqd8':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '(cQtqd8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtqd8':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '-(cQtqd8I/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cQtqd8I':1})

GC_282 = Coupling(name = 'GC_282',
                  value = 'cQtqd8I/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQtqd8I':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '(cQu1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQu1':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '-(cqu1Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ix3133':1})

GC_285 = Coupling(name = 'GC_285',
                  value = 'cqu1Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ix3133':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-(cqu1Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ix31ii':1})

GC_287 = Coupling(name = 'GC_287',
                  value = 'cqu1Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ix31ii':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '-(cqu1Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ix3233':1})

GC_289 = Coupling(name = 'GC_289',
                  value = 'cqu1Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ix3233':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '-(cqu1Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ix32ii':1})

GC_291 = Coupling(name = 'GC_291',
                  value = 'cqu1Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ix32ii':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '-(cqu1Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ix3331':1})

GC_293 = Coupling(name = 'GC_293',
                  value = 'cqu1Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ix3331':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '-(cqu1Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ix3332':1})

GC_295 = Coupling(name = 'GC_295',
                  value = 'cqu1Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ix3332':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '-(cqu1Ixii31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ixii31':1})

GC_297 = Coupling(name = 'GC_297',
                  value = 'cqu1Ixii31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ixii31':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '-(cqu1Ixii32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu1Ixii32':1})

GC_299 = Coupling(name = 'GC_299',
                  value = 'cqu1Ixii32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1Ixii32':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '(cqu1x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1x3133':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '(cqu1x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1x31ii':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '(cqu1x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1x3233':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '(cqu1x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1x32ii':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '(cqu1x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1x3331':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '(cqu1x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1x3332':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '(cqu1xii31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1xii31':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '(cqu1xii32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu1xii32':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '(cQu8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cQu8':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '-(cqu8Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ix3133':1})

GC_310 = Coupling(name = 'GC_310',
                  value = 'cqu8Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ix3133':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '-(cqu8Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ix31ii':1})

GC_312 = Coupling(name = 'GC_312',
                  value = 'cqu8Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ix31ii':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '-(cqu8Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ix3233':1})

GC_314 = Coupling(name = 'GC_314',
                  value = 'cqu8Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ix3233':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '-(cqu8Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ix32ii':1})

GC_316 = Coupling(name = 'GC_316',
                  value = 'cqu8Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ix32ii':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '-(cqu8Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ix3331':1})

GC_318 = Coupling(name = 'GC_318',
                  value = 'cqu8Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ix3331':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '-(cqu8Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ix3332':1})

GC_320 = Coupling(name = 'GC_320',
                  value = 'cqu8Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ix3332':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-(cqu8Ixii31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ixii31':1})

GC_322 = Coupling(name = 'GC_322',
                  value = 'cqu8Ixii31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ixii31':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-(cqu8Ixii32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cqu8Ixii32':1})

GC_324 = Coupling(name = 'GC_324',
                  value = 'cqu8Ixii32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8Ixii32':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(cqu8x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8x3133':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '(cqu8x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8x31ii':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(cqu8x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8x3233':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '(cqu8x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8x32ii':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cqu8x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8x3331':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '(cqu8x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8x3332':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(cqu8xii31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8xii31':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '(cqu8xii32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cqu8xii32':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '-(cquqd1Ix1333/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix1333':1})

GC_334 = Coupling(name = 'GC_334',
                  value = 'cquqd1Ix1333/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix1333':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '-(cquqd1Ix2333/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix2333':1})

GC_336 = Coupling(name = 'GC_336',
                  value = 'cquqd1Ix2333/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix2333':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '-(cquqd1Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3133':1})

GC_338 = Coupling(name = 'GC_338',
                  value = 'cquqd1Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3133':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '-(cquqd1Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3233':1})

GC_340 = Coupling(name = 'GC_340',
                  value = 'cquqd1Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3233':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '-(cquqd1Ix3313/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3313':1})

GC_342 = Coupling(name = 'GC_342',
                  value = 'cquqd1Ix3313/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3313':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '-(cquqd1Ix3323/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3323':1})

GC_344 = Coupling(name = 'GC_344',
                  value = 'cquqd1Ix3323/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3323':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-(cquqd1Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3331':1})

GC_346 = Coupling(name = 'GC_346',
                  value = 'cquqd1Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3331':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '-(cquqd1Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3332':1})

GC_348 = Coupling(name = 'GC_348',
                  value = 'cquqd1Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1Ix3332':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '-((cquqd1x1333*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x1333':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '(cquqd1x1333*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x1333':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-((cquqd1x2333*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x2333':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(cquqd1x2333*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x2333':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '-((cquqd1x3133*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x3133':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '(cquqd1x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x3133':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '-((cquqd1x3233*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x3233':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(cquqd1x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x3233':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '-((cquqd1x3313*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x3313':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(cquqd1x3313*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x3313':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '-((cquqd1x3323*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x3323':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(cquqd1x3323*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x3323':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-((cquqd1x3331*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x3331':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cquqd1x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x3331':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '-((cquqd1x3332*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd1x3332':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(cquqd1x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd1x3332':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-(cquqd8Ix1333/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix1333':1})

GC_366 = Coupling(name = 'GC_366',
                  value = 'cquqd8Ix1333/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix1333':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '-(cquqd8Ix2333/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix2333':1})

GC_368 = Coupling(name = 'GC_368',
                  value = 'cquqd8Ix2333/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix2333':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '-(cquqd8Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3133':1})

GC_370 = Coupling(name = 'GC_370',
                  value = 'cquqd8Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3133':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '-(cquqd8Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3233':1})

GC_372 = Coupling(name = 'GC_372',
                  value = 'cquqd8Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3233':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '-(cquqd8Ix3313/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3313':1})

GC_374 = Coupling(name = 'GC_374',
                  value = 'cquqd8Ix3313/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3313':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '-(cquqd8Ix3323/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3323':1})

GC_376 = Coupling(name = 'GC_376',
                  value = 'cquqd8Ix3323/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3323':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '-(cquqd8Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3331':1})

GC_378 = Coupling(name = 'GC_378',
                  value = 'cquqd8Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3331':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '-(cquqd8Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3332':1})

GC_380 = Coupling(name = 'GC_380',
                  value = 'cquqd8Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8Ix3332':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '-((cquqd8x1333*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x1333':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '(cquqd8x1333*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x1333':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '-((cquqd8x2333*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x2333':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(cquqd8x2333*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x2333':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '-((cquqd8x3133*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x3133':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(cquqd8x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x3133':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '-((cquqd8x3233*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x3233':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(cquqd8x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x3233':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '-((cquqd8x3313*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x3313':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(cquqd8x3313*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x3313':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '-((cquqd8x3323*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x3323':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(cquqd8x3323*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x3323':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '-((cquqd8x3331*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x3331':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '(cquqd8x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x3331':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '-((cquqd8x3332*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cquqd8x3332':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '(cquqd8x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cquqd8x3332':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '(ctb1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctb1':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(ctb8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctb8':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '(ctd1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctd1':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '(ctd8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctd8':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '(cte1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cte1':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '(cte2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cte2':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '(cte3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_cte3':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '-(cteIx1x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cteIx1x31':1})

GC_405 = Coupling(name = 'GC_405',
                  value = 'cteIx1x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cteIx1x31':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '-(cteIx1x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cteIx1x32':1})

GC_407 = Coupling(name = 'GC_407',
                  value = 'cteIx1x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cteIx1x32':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '-(cteIx2x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cteIx2x31':1})

GC_409 = Coupling(name = 'GC_409',
                  value = 'cteIx2x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cteIx2x31':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-(cteIx2x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cteIx2x32':1})

GC_411 = Coupling(name = 'GC_411',
                  value = 'cteIx2x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cteIx2x32':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '-(cteIx3x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cteIx3x31':1})

GC_413 = Coupling(name = 'GC_413',
                  value = 'cteIx3x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_cteIx3x31':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '-(cteIx3x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cteIx3x32':1})

GC_415 = Coupling(name = 'GC_415',
                  value = 'cteIx3x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_cteIx3x32':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '(ctex1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctex1x31':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '(ctex1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctex1x32':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '(ctex2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctex2x31':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '(ctex2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctex2x32':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '(ctex3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctex3x31':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '(ctex3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctex3x32':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '(ctG*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctG':1})

GC_423 = Coupling(name = 'GC_423',
                  value = 'ctGI/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctGI':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '-(ctGIx13/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx13':1})

GC_425 = Coupling(name = 'GC_425',
                  value = 'ctGIx13/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx13':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '-(ctGIx23/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx23':1})

GC_427 = Coupling(name = 'GC_427',
                  value = 'ctGIx23/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx23':1})

GC_428 = Coupling(name = 'GC_428',
                  value = '-(ctGIx31/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx31':1})

GC_429 = Coupling(name = 'GC_429',
                  value = 'ctGIx31/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx31':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '-(ctGIx32/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx32':1})

GC_431 = Coupling(name = 'GC_431',
                  value = 'ctGIx32/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGIx32':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '(ctGx13*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGx13':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '(ctGx23*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGx23':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(ctGx31*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGx31':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(ctGx32*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctGx32':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '(ctl1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctl1':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(ctl2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctl2':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '(ctl3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctl3':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '-(ctlIx1x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlIx1x31':1})

GC_440 = Coupling(name = 'GC_440',
                  value = 'ctlIx1x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlIx1x31':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '-(ctlIx1x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlIx1x32':1})

GC_442 = Coupling(name = 'GC_442',
                  value = 'ctlIx1x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlIx1x32':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '-(ctlIx2x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlIx2x31':1})

GC_444 = Coupling(name = 'GC_444',
                  value = 'ctlIx2x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlIx2x31':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '-(ctlIx2x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlIx2x32':1})

GC_446 = Coupling(name = 'GC_446',
                  value = 'ctlIx2x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlIx2x32':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '-(ctlIx3x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlIx3x31':1})

GC_448 = Coupling(name = 'GC_448',
                  value = 'ctlIx3x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlIx3x31':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '-(ctlIx3x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlIx3x32':1})

GC_450 = Coupling(name = 'GC_450',
                  value = 'ctlIx3x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlIx3x32':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '-((ctlS1*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlS1':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '(ctlS1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlS1':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '-((ctlS2*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlS2':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '(ctlS2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlS2':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '-((ctlS3*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlS3':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '(ctlS3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlS3':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-(ctlSI1/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlSI1':1})

GC_458 = Coupling(name = 'GC_458',
                  value = 'ctlSI1/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlSI1':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '-(ctlSI2/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlSI2':1})

GC_460 = Coupling(name = 'GC_460',
                  value = 'ctlSI2/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlSI2':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '-(ctlSI3/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlSI3':1})

GC_462 = Coupling(name = 'GC_462',
                  value = 'ctlSI3/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlSI3':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '-(ctlSIx1x13/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx1x13':1})

GC_464 = Coupling(name = 'GC_464',
                  value = 'ctlSIx1x13/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx1x13':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-(ctlSIx1x23/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx1x23':1})

GC_466 = Coupling(name = 'GC_466',
                  value = 'ctlSIx1x23/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx1x23':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '-(ctlSIx1x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx1x31':1})

GC_468 = Coupling(name = 'GC_468',
                  value = 'ctlSIx1x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx1x31':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-(ctlSIx1x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx1x32':1})

GC_470 = Coupling(name = 'GC_470',
                  value = 'ctlSIx1x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx1x32':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '-(ctlSIx2x13/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx2x13':1})

GC_472 = Coupling(name = 'GC_472',
                  value = 'ctlSIx2x13/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx2x13':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '-(ctlSIx2x23/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx2x23':1})

GC_474 = Coupling(name = 'GC_474',
                  value = 'ctlSIx2x23/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx2x23':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-(ctlSIx2x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx2x31':1})

GC_476 = Coupling(name = 'GC_476',
                  value = 'ctlSIx2x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx2x31':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '-(ctlSIx2x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx2x32':1})

GC_478 = Coupling(name = 'GC_478',
                  value = 'ctlSIx2x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx2x32':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '-(ctlSIx3x13/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx3x13':1})

GC_480 = Coupling(name = 'GC_480',
                  value = 'ctlSIx3x13/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx3x13':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '-(ctlSIx3x23/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx3x23':1})

GC_482 = Coupling(name = 'GC_482',
                  value = 'ctlSIx3x23/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx3x23':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '-(ctlSIx3x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx3x31':1})

GC_484 = Coupling(name = 'GC_484',
                  value = 'ctlSIx3x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx3x31':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '-(ctlSIx3x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSIx3x32':1})

GC_486 = Coupling(name = 'GC_486',
                  value = 'ctlSIx3x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSIx3x32':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '-((ctlSx1x13*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx1x13':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ctlSx1x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx1x13':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-((ctlSx1x23*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx1x23':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(ctlSx1x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx1x23':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '-((ctlSx1x31*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx1x31':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(ctlSx1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx1x31':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '-((ctlSx1x32*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx1x32':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ctlSx1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx1x32':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '-((ctlSx2x13*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx2x13':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '(ctlSx2x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx2x13':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '-((ctlSx2x23*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx2x23':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(ctlSx2x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx2x23':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '-((ctlSx2x31*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx2x31':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '(ctlSx2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx2x31':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '-((ctlSx2x32*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx2x32':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(ctlSx2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx2x32':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '-((ctlSx3x13*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx3x13':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '(ctlSx3x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx3x13':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '-((ctlSx3x23*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx3x23':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(ctlSx3x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx3x23':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '-((ctlSx3x31*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx3x31':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '(ctlSx3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx3x31':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '-((ctlSx3x32*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlSx3x32':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '(ctlSx3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlSx3x32':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '-((ctlT1*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlT1':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '(ctlT1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT1':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '(-4*ctlT1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT1':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '(4*ctlT1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT1':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '-((ctlT2*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlT2':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '(ctlT2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT2':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '(-4*ctlT2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT2':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '(4*ctlT2*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT2':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '-((ctlT3*complex(0,1))/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlT3':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '(ctlT3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT3':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '(-4*ctlT3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT3':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '(4*ctlT3*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlT3':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '(-4*ctlTI1)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI1':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '-(ctlTI1/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlTI1':1})

GC_525 = Coupling(name = 'GC_525',
                  value = 'ctlTI1/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI1':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '(4*ctlTI1)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI1':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '(-4*ctlTI2)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI2':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '-(ctlTI2/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlTI2':1})

GC_529 = Coupling(name = 'GC_529',
                  value = 'ctlTI2/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI2':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '(4*ctlTI2)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI2':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '(-4*ctlTI3)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI3':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '-(ctlTI3/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctlTI3':1})

GC_533 = Coupling(name = 'GC_533',
                  value = 'ctlTI3/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI3':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(4*ctlTI3)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctlTI3':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(-4*ctlTIx1x13)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x13':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '-(ctlTIx1x13/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx1x13':1})

GC_537 = Coupling(name = 'GC_537',
                  value = 'ctlTIx1x13/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x13':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '(4*ctlTIx1x13)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x13':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '(-4*ctlTIx1x23)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x23':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '-(ctlTIx1x23/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx1x23':1})

GC_541 = Coupling(name = 'GC_541',
                  value = 'ctlTIx1x23/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x23':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '(4*ctlTIx1x23)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x23':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '(-4*ctlTIx1x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x31':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '-(ctlTIx1x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx1x31':1})

GC_545 = Coupling(name = 'GC_545',
                  value = 'ctlTIx1x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x31':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '(4*ctlTIx1x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x31':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '(-4*ctlTIx1x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x32':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '-(ctlTIx1x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx1x32':1})

GC_549 = Coupling(name = 'GC_549',
                  value = 'ctlTIx1x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x32':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(4*ctlTIx1x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx1x32':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '(-4*ctlTIx2x13)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x13':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '-(ctlTIx2x13/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx2x13':1})

GC_553 = Coupling(name = 'GC_553',
                  value = 'ctlTIx2x13/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x13':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(4*ctlTIx2x13)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x13':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(-4*ctlTIx2x23)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x23':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '-(ctlTIx2x23/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx2x23':1})

GC_557 = Coupling(name = 'GC_557',
                  value = 'ctlTIx2x23/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x23':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '(4*ctlTIx2x23)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x23':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '(-4*ctlTIx2x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x31':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '-(ctlTIx2x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx2x31':1})

GC_561 = Coupling(name = 'GC_561',
                  value = 'ctlTIx2x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x31':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(4*ctlTIx2x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x31':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(-4*ctlTIx2x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x32':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '-(ctlTIx2x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx2x32':1})

GC_565 = Coupling(name = 'GC_565',
                  value = 'ctlTIx2x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x32':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '(4*ctlTIx2x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx2x32':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '(-4*ctlTIx3x13)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x13':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '-(ctlTIx3x13/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx3x13':1})

GC_569 = Coupling(name = 'GC_569',
                  value = 'ctlTIx3x13/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x13':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '(4*ctlTIx3x13)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x13':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '(-4*ctlTIx3x23)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x23':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '-(ctlTIx3x23/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx3x23':1})

GC_573 = Coupling(name = 'GC_573',
                  value = 'ctlTIx3x23/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x23':1})

GC_574 = Coupling(name = 'GC_574',
                  value = '(4*ctlTIx3x23)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x23':1})

GC_575 = Coupling(name = 'GC_575',
                  value = '(-4*ctlTIx3x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x31':1})

GC_576 = Coupling(name = 'GC_576',
                  value = '-(ctlTIx3x31/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx3x31':1})

GC_577 = Coupling(name = 'GC_577',
                  value = 'ctlTIx3x31/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x31':1})

GC_578 = Coupling(name = 'GC_578',
                  value = '(4*ctlTIx3x31)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x31':1})

GC_579 = Coupling(name = 'GC_579',
                  value = '(-4*ctlTIx3x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x32':1})

GC_580 = Coupling(name = 'GC_580',
                  value = '-(ctlTIx3x32/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTIx3x32':1})

GC_581 = Coupling(name = 'GC_581',
                  value = 'ctlTIx3x32/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x32':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '(4*ctlTIx3x32)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTIx3x32':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '-((ctlTx1x13*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx1x13':1})

GC_584 = Coupling(name = 'GC_584',
                  value = '(ctlTx1x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x13':1})

GC_585 = Coupling(name = 'GC_585',
                  value = '(-4*ctlTx1x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x13':1})

GC_586 = Coupling(name = 'GC_586',
                  value = '(4*ctlTx1x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x13':1})

GC_587 = Coupling(name = 'GC_587',
                  value = '-((ctlTx1x23*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx1x23':1})

GC_588 = Coupling(name = 'GC_588',
                  value = '(ctlTx1x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x23':1})

GC_589 = Coupling(name = 'GC_589',
                  value = '(-4*ctlTx1x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x23':1})

GC_590 = Coupling(name = 'GC_590',
                  value = '(4*ctlTx1x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x23':1})

GC_591 = Coupling(name = 'GC_591',
                  value = '-((ctlTx1x31*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx1x31':1})

GC_592 = Coupling(name = 'GC_592',
                  value = '(ctlTx1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x31':1})

GC_593 = Coupling(name = 'GC_593',
                  value = '(-4*ctlTx1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x31':1})

GC_594 = Coupling(name = 'GC_594',
                  value = '(4*ctlTx1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x31':1})

GC_595 = Coupling(name = 'GC_595',
                  value = '-((ctlTx1x32*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx1x32':1})

GC_596 = Coupling(name = 'GC_596',
                  value = '(ctlTx1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x32':1})

GC_597 = Coupling(name = 'GC_597',
                  value = '(-4*ctlTx1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x32':1})

GC_598 = Coupling(name = 'GC_598',
                  value = '(4*ctlTx1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx1x32':1})

GC_599 = Coupling(name = 'GC_599',
                  value = '-((ctlTx2x13*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx2x13':1})

GC_600 = Coupling(name = 'GC_600',
                  value = '(ctlTx2x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x13':1})

GC_601 = Coupling(name = 'GC_601',
                  value = '(-4*ctlTx2x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x13':1})

GC_602 = Coupling(name = 'GC_602',
                  value = '(4*ctlTx2x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x13':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '-((ctlTx2x23*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx2x23':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '(ctlTx2x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x23':1})

GC_605 = Coupling(name = 'GC_605',
                  value = '(-4*ctlTx2x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x23':1})

GC_606 = Coupling(name = 'GC_606',
                  value = '(4*ctlTx2x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x23':1})

GC_607 = Coupling(name = 'GC_607',
                  value = '-((ctlTx2x31*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx2x31':1})

GC_608 = Coupling(name = 'GC_608',
                  value = '(ctlTx2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x31':1})

GC_609 = Coupling(name = 'GC_609',
                  value = '(-4*ctlTx2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x31':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '(4*ctlTx2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x31':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '-((ctlTx2x32*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx2x32':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '(ctlTx2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x32':1})

GC_613 = Coupling(name = 'GC_613',
                  value = '(-4*ctlTx2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x32':1})

GC_614 = Coupling(name = 'GC_614',
                  value = '(4*ctlTx2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx2x32':1})

GC_615 = Coupling(name = 'GC_615',
                  value = '-((ctlTx3x13*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx3x13':1})

GC_616 = Coupling(name = 'GC_616',
                  value = '(ctlTx3x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x13':1})

GC_617 = Coupling(name = 'GC_617',
                  value = '(-4*ctlTx3x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x13':1})

GC_618 = Coupling(name = 'GC_618',
                  value = '(4*ctlTx3x13*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x13':1})

GC_619 = Coupling(name = 'GC_619',
                  value = '-((ctlTx3x23*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx3x23':1})

GC_620 = Coupling(name = 'GC_620',
                  value = '(ctlTx3x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x23':1})

GC_621 = Coupling(name = 'GC_621',
                  value = '(-4*ctlTx3x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x23':1})

GC_622 = Coupling(name = 'GC_622',
                  value = '(4*ctlTx3x23*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x23':1})

GC_623 = Coupling(name = 'GC_623',
                  value = '-((ctlTx3x31*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx3x31':1})

GC_624 = Coupling(name = 'GC_624',
                  value = '(ctlTx3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x31':1})

GC_625 = Coupling(name = 'GC_625',
                  value = '(-4*ctlTx3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x31':1})

GC_626 = Coupling(name = 'GC_626',
                  value = '(4*ctlTx3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x31':1})

GC_627 = Coupling(name = 'GC_627',
                  value = '-((ctlTx3x32*complex(0,1))/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctlTx3x32':1})

GC_628 = Coupling(name = 'GC_628',
                  value = '(ctlTx3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x32':1})

GC_629 = Coupling(name = 'GC_629',
                  value = '(-4*ctlTx3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x32':1})

GC_630 = Coupling(name = 'GC_630',
                  value = '(4*ctlTx3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlTx3x32':1})

GC_631 = Coupling(name = 'GC_631',
                  value = '(ctlx1x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlx1x31':1})

GC_632 = Coupling(name = 'GC_632',
                  value = '(ctlx1x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlx1x32':1})

GC_633 = Coupling(name = 'GC_633',
                  value = '(ctlx2x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlx2x31':1})

GC_634 = Coupling(name = 'GC_634',
                  value = '(ctlx2x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlx2x32':1})

GC_635 = Coupling(name = 'GC_635',
                  value = '(ctlx3x31*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlx3x31':1})

GC_636 = Coupling(name = 'GC_636',
                  value = '(ctlx3x32*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctlx3x32':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '(ctq1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctq1':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '(ctq8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctq8':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '(ctQqu1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctQqu1':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '-(ctQqu1I/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctQqu1I':1})

GC_641 = Coupling(name = 'GC_641',
                  value = 'ctQqu1I/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctQqu1I':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '(ctQqu8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctQqu8':1})

GC_643 = Coupling(name = 'GC_643',
                  value = '-(ctQqu8I/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctQqu8I':1})

GC_644 = Coupling(name = 'GC_644',
                  value = 'ctQqu8I/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctQqu8I':1})

GC_645 = Coupling(name = 'GC_645',
                  value = '(2*ctt1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctt1':1})

GC_646 = Coupling(name = 'GC_646',
                  value = '(ctu1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctu1':1})

GC_647 = Coupling(name = 'GC_647',
                  value = '(ctu8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctu8':1})

GC_648 = Coupling(name = 'GC_648',
                  value = '(ctW*complex(0,1))/Lambda**2',
                  order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_649 = Coupling(name = 'GC_649',
                  value = '-(ctWI/Lambda**2)',
                  order = {'QED':1,'DIM6':1,'DIM6_ctWI':1})

GC_650 = Coupling(name = 'GC_650',
                  value = 'ctWI/Lambda**2',
                  order = {'QED':1,'DIM6':1,'DIM6_ctWI':1})

GC_651 = Coupling(name = 'GC_651',
                  value = '-(ctWIx13/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_652 = Coupling(name = 'GC_652',
                  value = 'ctWIx13/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_653 = Coupling(name = 'GC_653',
                  value = '-(ctWIx23/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_654 = Coupling(name = 'GC_654',
                  value = 'ctWIx23/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_655 = Coupling(name = 'GC_655',
                  value = '-(ctWIx31/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_656 = Coupling(name = 'GC_656',
                  value = 'ctWIx31/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_657 = Coupling(name = 'GC_657',
                  value = '-(ctWIx32/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_658 = Coupling(name = 'GC_658',
                  value = 'ctWIx32/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_659 = Coupling(name = 'GC_659',
                  value = '(ctWx13*complex(0,1))/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '(ctWx23*complex(0,1))/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(ctWx31*complex(0,1))/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '(ctWx32*complex(0,1))/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '(ctZ*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctZ':1})

GC_664 = Coupling(name = 'GC_664',
                  value = 'ctZI/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctZI':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '-(ctZIx13/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx13':1})

GC_666 = Coupling(name = 'GC_666',
                  value = 'ctZIx13/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx13':1})

GC_667 = Coupling(name = 'GC_667',
                  value = '-(ctZIx23/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx23':1})

GC_668 = Coupling(name = 'GC_668',
                  value = 'ctZIx23/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx23':1})

GC_669 = Coupling(name = 'GC_669',
                  value = '-(ctZIx31/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx31':1})

GC_670 = Coupling(name = 'GC_670',
                  value = 'ctZIx31/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx31':1})

GC_671 = Coupling(name = 'GC_671',
                  value = '-(ctZIx32/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx32':1})

GC_672 = Coupling(name = 'GC_672',
                  value = 'ctZIx32/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx32':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '(ctZx13*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx13':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '(ctZx23*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx23':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '(ctZx31*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx31':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '(ctZx32*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx32':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '-(cud1Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud1Ix3133':1})

GC_678 = Coupling(name = 'GC_678',
                  value = 'cud1Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1Ix3133':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '-(cud1Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud1Ix31ii':1})

GC_680 = Coupling(name = 'GC_680',
                  value = 'cud1Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1Ix31ii':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '-(cud1Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud1Ix3233':1})

GC_682 = Coupling(name = 'GC_682',
                  value = 'cud1Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1Ix3233':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '-(cud1Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud1Ix32ii':1})

GC_684 = Coupling(name = 'GC_684',
                  value = 'cud1Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1Ix32ii':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '-(cud1Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud1Ix3331':1})

GC_686 = Coupling(name = 'GC_686',
                  value = 'cud1Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1Ix3331':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '-(cud1Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud1Ix3332':1})

GC_688 = Coupling(name = 'GC_688',
                  value = 'cud1Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1Ix3332':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '(cud1x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1x3133':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '(cud1x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1x31ii':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '(cud1x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1x3233':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '(cud1x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1x32ii':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '(cud1x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1x3331':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '(cud1x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud1x3332':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '-(cud8Ix3133/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud8Ix3133':1})

GC_696 = Coupling(name = 'GC_696',
                  value = 'cud8Ix3133/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8Ix3133':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '-(cud8Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud8Ix31ii':1})

GC_698 = Coupling(name = 'GC_698',
                  value = 'cud8Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8Ix31ii':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '-(cud8Ix3233/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud8Ix3233':1})

GC_700 = Coupling(name = 'GC_700',
                  value = 'cud8Ix3233/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8Ix3233':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '-(cud8Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud8Ix32ii':1})

GC_702 = Coupling(name = 'GC_702',
                  value = 'cud8Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8Ix32ii':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '-(cud8Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud8Ix3331':1})

GC_704 = Coupling(name = 'GC_704',
                  value = 'cud8Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8Ix3331':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '-(cud8Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cud8Ix3332':1})

GC_706 = Coupling(name = 'GC_706',
                  value = 'cud8Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8Ix3332':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '(cud8x3133*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8x3133':1})

GC_708 = Coupling(name = 'GC_708',
                  value = '(cud8x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8x31ii':1})

GC_709 = Coupling(name = 'GC_709',
                  value = '(cud8x3233*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8x3233':1})

GC_710 = Coupling(name = 'GC_710',
                  value = '(cud8x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8x32ii':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '(cud8x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8x3331':1})

GC_712 = Coupling(name = 'GC_712',
                  value = '(cud8x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cud8x3332':1})

GC_713 = Coupling(name = 'GC_713',
                  value = '-(cuu1Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cuu1Ix31ii':1})

GC_714 = Coupling(name = 'GC_714',
                  value = 'cuu1Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1Ix31ii':1})

GC_715 = Coupling(name = 'GC_715',
                  value = '-(cuu1Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cuu1Ix32ii':1})

GC_716 = Coupling(name = 'GC_716',
                  value = 'cuu1Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1Ix32ii':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '-(cuu1Ix3331/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cuu1Ix3331':1})

GC_718 = Coupling(name = 'GC_718',
                  value = 'cuu1Ix3331/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1Ix3331':1})

GC_719 = Coupling(name = 'GC_719',
                  value = '-(cuu1Ix3332/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cuu1Ix3332':1})

GC_720 = Coupling(name = 'GC_720',
                  value = 'cuu1Ix3332/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1Ix3332':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '(cuu1x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1x31ii':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '(cuu1x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1x32ii':1})

GC_723 = Coupling(name = 'GC_723',
                  value = '(cuu1x3331*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1x3331':1})

GC_724 = Coupling(name = 'GC_724',
                  value = '(cuu1x3332*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu1x3332':1})

GC_725 = Coupling(name = 'GC_725',
                  value = '-(cuu8Ix31ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cuu8Ix31ii':1})

GC_726 = Coupling(name = 'GC_726',
                  value = 'cuu8Ix31ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu8Ix31ii':1})

GC_727 = Coupling(name = 'GC_727',
                  value = '-(cuu8Ix32ii/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cuu8Ix32ii':1})

GC_728 = Coupling(name = 'GC_728',
                  value = 'cuu8Ix32ii/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu8Ix32ii':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '(cuu8x31ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu8x31ii':1})

GC_730 = Coupling(name = 'GC_730',
                  value = '(cuu8x32ii*complex(0,1))/Lambda**2',
                  order = {'FCNC':1,'FCNC_cuu8x32ii':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '-((cbW*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_732 = Coupling(name = 'GC_732',
                  value = '-((cbWI*cw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '-((cbWIx13*cw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '(cbWIx13*cw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '-((cbWIx23*cw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '(cbWIx23*cw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '-((cbWIx31*cw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '(cbWIx31*cw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '-((cbWIx32*cw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '(cbWIx32*cw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '-((cbWx13*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_742 = Coupling(name = 'GC_742',
                  value = '-((cbWx23*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_743 = Coupling(name = 'GC_743',
                  value = '-((cbWx31*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '-((cbWx32*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '-(ee**2*complex(0,1)) + (ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_746 = Coupling(name = 'GC_746',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '-(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_754 = Coupling(name = 'GC_754',
                  value = '(ctW*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_755 = Coupling(name = 'GC_755',
                  value = 'ctWI/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctWI':1})

GC_756 = Coupling(name = 'GC_756',
                  value = '-(ctWIx13/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_757 = Coupling(name = 'GC_757',
                  value = 'ctWIx13/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_758 = Coupling(name = 'GC_758',
                  value = '-(ctWIx23/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_759 = Coupling(name = 'GC_759',
                  value = 'ctWIx23/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '-(ctWIx31/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_761 = Coupling(name = 'GC_761',
                  value = 'ctWIx31/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_762 = Coupling(name = 'GC_762',
                  value = '-(ctWIx32/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_763 = Coupling(name = 'GC_763',
                  value = 'ctWIx32/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_764 = Coupling(name = 'GC_764',
                  value = '(ctWx13*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_765 = Coupling(name = 'GC_765',
                  value = '(ctWx23*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_766 = Coupling(name = 'GC_766',
                  value = '(ctWx31*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_767 = Coupling(name = 'GC_767',
                  value = '(ctWx32*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_768 = Coupling(name = 'GC_768',
                  value = '-((ctZ*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctZ':1})

GC_769 = Coupling(name = 'GC_769',
                  value = '-((ctZI*cw)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctZI':1})

GC_770 = Coupling(name = 'GC_770',
                  value = '-((ctZIx13*cw)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx13':1})

GC_771 = Coupling(name = 'GC_771',
                  value = '(ctZIx13*cw)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx13':1})

GC_772 = Coupling(name = 'GC_772',
                  value = '-((ctZIx23*cw)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx23':1})

GC_773 = Coupling(name = 'GC_773',
                  value = '(ctZIx23*cw)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx23':1})

GC_774 = Coupling(name = 'GC_774',
                  value = '-((ctZIx31*cw)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx31':1})

GC_775 = Coupling(name = 'GC_775',
                  value = '(ctZIx31*cw)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx31':1})

GC_776 = Coupling(name = 'GC_776',
                  value = '-((ctZIx32*cw)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx32':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '(ctZIx32*cw)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZIx32':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '-((ctZx13*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx13':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '-((ctZx23*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx23':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '-((ctZx31*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx31':1})

GC_781 = Coupling(name = 'GC_781',
                  value = '-((ctZx32*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctZx32':1})

GC_782 = Coupling(name = 'GC_782',
                  value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_783 = Coupling(name = 'GC_783',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_784 = Coupling(name = 'GC_784',
                  value = '-((cbW*complex(0,1)*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_785 = Coupling(name = 'GC_785',
                  value = '-((cbWI*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '-((cbWIx13*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '(cbWIx13*sw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_788 = Coupling(name = 'GC_788',
                  value = '-((cbWIx23*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_789 = Coupling(name = 'GC_789',
                  value = '(cbWIx23*sw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '-((cbWIx31*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '(cbWIx31*sw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '-((cbWIx32*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_793 = Coupling(name = 'GC_793',
                  value = '(cbWIx32*sw)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_794 = Coupling(name = 'GC_794',
                  value = '-((cbWx13*complex(0,1)*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_795 = Coupling(name = 'GC_795',
                  value = '-((cbWx23*complex(0,1)*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '-((cbWx31*complex(0,1)*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '-((cbWx32*complex(0,1)*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '(ee**2*complex(0,1))/2. + (ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_800 = Coupling(name = 'GC_800',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_801 = Coupling(name = 'GC_801',
                  value = '(cbW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'DIM6_cbW':1})

GC_802 = Coupling(name = 'GC_802',
                  value = '-((cbWI*vev)/Lambda**2)',
                  order = {'DIM6':1,'DIM6_cbWI':1})

GC_803 = Coupling(name = 'GC_803',
                  value = '(cbWI*vev)/Lambda**2',
                  order = {'DIM6':1,'DIM6_cbWI':1})

GC_804 = Coupling(name = 'GC_804',
                  value = '-((cbWIx13*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cbWIx13':1})

GC_805 = Coupling(name = 'GC_805',
                  value = '(cbWIx13*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWIx13':1})

GC_806 = Coupling(name = 'GC_806',
                  value = '-((cbWIx23*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cbWIx23':1})

GC_807 = Coupling(name = 'GC_807',
                  value = '(cbWIx23*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWIx23':1})

GC_808 = Coupling(name = 'GC_808',
                  value = '-((cbWIx31*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cbWIx31':1})

GC_809 = Coupling(name = 'GC_809',
                  value = '(cbWIx31*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWIx31':1})

GC_810 = Coupling(name = 'GC_810',
                  value = '-((cbWIx32*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_cbWIx32':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '(cbWIx32*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWIx32':1})

GC_812 = Coupling(name = 'GC_812',
                  value = '(cbWx13*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWx13':1})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cbWx23*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWx23':1})

GC_814 = Coupling(name = 'GC_814',
                  value = '(cbWx31*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWx31':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '(cbWx32*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_cbWx32':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '(ctG*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'DIM6_ctG':1})

GC_817 = Coupling(name = 'GC_817',
                  value = '(ctGI*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'DIM6_ctGI':1})

GC_818 = Coupling(name = 'GC_818',
                  value = '-((ctGIx13*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctGIx13':1})

GC_819 = Coupling(name = 'GC_819',
                  value = '(ctGIx13*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGIx13':1})

GC_820 = Coupling(name = 'GC_820',
                  value = '-((ctGIx23*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctGIx23':1})

GC_821 = Coupling(name = 'GC_821',
                  value = '(ctGIx23*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGIx23':1})

GC_822 = Coupling(name = 'GC_822',
                  value = '-((ctGIx31*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctGIx31':1})

GC_823 = Coupling(name = 'GC_823',
                  value = '(ctGIx31*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGIx31':1})

GC_824 = Coupling(name = 'GC_824',
                  value = '-((ctGIx32*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctGIx32':1})

GC_825 = Coupling(name = 'GC_825',
                  value = '(ctGIx32*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGIx32':1})

GC_826 = Coupling(name = 'GC_826',
                  value = '(ctGx13*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGx13':1})

GC_827 = Coupling(name = 'GC_827',
                  value = '(ctGx23*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGx23':1})

GC_828 = Coupling(name = 'GC_828',
                  value = '(ctGx31*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGx31':1})

GC_829 = Coupling(name = 'GC_829',
                  value = '(ctGx32*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctGx32':1})

GC_830 = Coupling(name = 'GC_830',
                  value = '(3*ctp*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'DIM6':1,'DIM6_ctp':1})

GC_831 = Coupling(name = 'GC_831',
                  value = '(3*ctpI*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'DIM6':1,'DIM6_ctpI':1})

GC_832 = Coupling(name = 'GC_832',
                  value = '(-3*ctpIx13*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx13':1})

GC_833 = Coupling(name = 'GC_833',
                  value = '(3*ctpIx13*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx13':1})

GC_834 = Coupling(name = 'GC_834',
                  value = '(-3*ctpIx23*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx23':1})

GC_835 = Coupling(name = 'GC_835',
                  value = '(3*ctpIx23*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx23':1})

GC_836 = Coupling(name = 'GC_836',
                  value = '(-3*ctpIx31*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx31':1})

GC_837 = Coupling(name = 'GC_837',
                  value = '(3*ctpIx31*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx31':1})

GC_838 = Coupling(name = 'GC_838',
                  value = '(-3*ctpIx32*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx32':1})

GC_839 = Coupling(name = 'GC_839',
                  value = '(3*ctpIx32*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpIx32':1})

GC_840 = Coupling(name = 'GC_840',
                  value = '(3*ctpx13*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpx13':1})

GC_841 = Coupling(name = 'GC_841',
                  value = '(3*ctpx23*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpx23':1})

GC_842 = Coupling(name = 'GC_842',
                  value = '(3*ctpx31*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpx31':1})

GC_843 = Coupling(name = 'GC_843',
                  value = '(3*ctpx32*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_ctpx32':1})

GC_844 = Coupling(name = 'GC_844',
                  value = '(ctW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctW':1})

GC_845 = Coupling(name = 'GC_845',
                  value = '-((ctWI*vev)/Lambda**2)',
                  order = {'DIM6':1,'DIM6_ctWI':1})

GC_846 = Coupling(name = 'GC_846',
                  value = '(ctWI*vev)/Lambda**2',
                  order = {'DIM6':1,'DIM6_ctWI':1})

GC_847 = Coupling(name = 'GC_847',
                  value = '-((ctWIx13*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctWIx13':1})

GC_848 = Coupling(name = 'GC_848',
                  value = '(ctWIx13*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWIx13':1})

GC_849 = Coupling(name = 'GC_849',
                  value = '-((ctWIx23*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctWIx23':1})

GC_850 = Coupling(name = 'GC_850',
                  value = '(ctWIx23*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWIx23':1})

GC_851 = Coupling(name = 'GC_851',
                  value = '-((ctWIx31*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctWIx31':1})

GC_852 = Coupling(name = 'GC_852',
                  value = '(ctWIx31*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWIx31':1})

GC_853 = Coupling(name = 'GC_853',
                  value = '-((ctWIx32*vev)/Lambda**2)',
                  order = {'FCNC':1,'FCNC_ctWIx32':1})

GC_854 = Coupling(name = 'GC_854',
                  value = '(ctWIx32*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWIx32':1})

GC_855 = Coupling(name = 'GC_855',
                  value = '(ctWx13*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWx13':1})

GC_856 = Coupling(name = 'GC_856',
                  value = '(ctWx23*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWx23':1})

GC_857 = Coupling(name = 'GC_857',
                  value = '(ctWx31*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWx31':1})

GC_858 = Coupling(name = 'GC_858',
                  value = '(ctWx32*complex(0,1)*vev)/Lambda**2',
                  order = {'FCNC':1,'FCNC_ctWx32':1})

GC_859 = Coupling(name = 'GC_859',
                  value = '(ctZ*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'DIM6_ctZ':1})

GC_860 = Coupling(name = 'GC_860',
                  value = '(ctZI*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'DIM6_ctZI':1})

GC_861 = Coupling(name = 'GC_861',
                  value = '-((ctZIx13*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx13':1})

GC_862 = Coupling(name = 'GC_862',
                  value = '(ctZIx13*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx13':1})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((ctZIx23*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx23':1})

GC_864 = Coupling(name = 'GC_864',
                  value = '(ctZIx23*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx23':1})

GC_865 = Coupling(name = 'GC_865',
                  value = '-((ctZIx31*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx31':1})

GC_866 = Coupling(name = 'GC_866',
                  value = '(ctZIx31*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx31':1})

GC_867 = Coupling(name = 'GC_867',
                  value = '-((ctZIx32*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx32':1})

GC_868 = Coupling(name = 'GC_868',
                  value = '(ctZIx32*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx32':1})

GC_869 = Coupling(name = 'GC_869',
                  value = '(ctZx13*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZx13':1})

GC_870 = Coupling(name = 'GC_870',
                  value = '(ctZx23*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZx23':1})

GC_871 = Coupling(name = 'GC_871',
                  value = '(ctZx31*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZx31':1})

GC_872 = Coupling(name = 'GC_872',
                  value = '(ctZx32*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZx32':1})

GC_873 = Coupling(name = 'GC_873',
                  value = '-((cbW*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'DIM6':1,'DIM6_cbW':1})

GC_874 = Coupling(name = 'GC_874',
                  value = '-((cbWI*cw*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'DIM6':1,'DIM6_cbWI':1})

GC_875 = Coupling(name = 'GC_875',
                  value = '-((cbWIx13*cw*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWIx13':1})

GC_876 = Coupling(name = 'GC_876',
                  value = '(cbWIx13*cw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_cbWIx13':1})

GC_877 = Coupling(name = 'GC_877',
                  value = '-((cbWIx23*cw*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWIx23':1})

GC_878 = Coupling(name = 'GC_878',
                  value = '(cbWIx23*cw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_cbWIx23':1})

GC_879 = Coupling(name = 'GC_879',
                  value = '-((cbWIx31*cw*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWIx31':1})

GC_880 = Coupling(name = 'GC_880',
                  value = '(cbWIx31*cw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_cbWIx31':1})

GC_881 = Coupling(name = 'GC_881',
                  value = '-((cbWIx32*cw*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWIx32':1})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cbWIx32*cw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_cbWIx32':1})

GC_883 = Coupling(name = 'GC_883',
                  value = '-((cbWx13*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWx13':1})

GC_884 = Coupling(name = 'GC_884',
                  value = '-((cbWx23*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWx23':1})

GC_885 = Coupling(name = 'GC_885',
                  value = '-((cbWx31*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWx31':1})

GC_886 = Coupling(name = 'GC_886',
                  value = '-((cbWx32*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_cbWx32':1})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((cbW*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_888 = Coupling(name = 'GC_888',
                  value = '(cbW*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_889 = Coupling(name = 'GC_889',
                  value = '-((cbWI*ee*vev)/Lambda**2)',
                  order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_890 = Coupling(name = 'GC_890',
                  value = '-((cbWIx13*ee*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_891 = Coupling(name = 'GC_891',
                  value = '-((cbWIx23*ee*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_892 = Coupling(name = 'GC_892',
                  value = '-((cbWIx31*ee*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_893 = Coupling(name = 'GC_893',
                  value = '-((cbWIx32*ee*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_894 = Coupling(name = 'GC_894',
                  value = '-((cbWx13*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_895 = Coupling(name = 'GC_895',
                  value = '(cbWx13*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_896 = Coupling(name = 'GC_896',
                  value = '-((cbWx23*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_897 = Coupling(name = 'GC_897',
                  value = '(cbWx23*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_898 = Coupling(name = 'GC_898',
                  value = '-((cbWx31*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_899 = Coupling(name = 'GC_899',
                  value = '(cbWx31*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_900 = Coupling(name = 'GC_900',
                  value = '-((cbWx32*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_901 = Coupling(name = 'GC_901',
                  value = '(cbWx32*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_902 = Coupling(name = 'GC_902',
                  value = '-((ctW*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_903 = Coupling(name = 'GC_903',
                  value = '(ctW*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_904 = Coupling(name = 'GC_904',
                  value = '(ctWI*ee*vev)/Lambda**2',
                  order = {'QED':1,'DIM6':1,'DIM6_ctWI':1})

GC_905 = Coupling(name = 'GC_905',
                  value = '(ctWIx13*ee*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_906 = Coupling(name = 'GC_906',
                  value = '(ctWIx23*ee*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_907 = Coupling(name = 'GC_907',
                  value = '(ctWIx31*ee*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_908 = Coupling(name = 'GC_908',
                  value = '(ctWIx32*ee*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_909 = Coupling(name = 'GC_909',
                  value = '-((ctWx13*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_910 = Coupling(name = 'GC_910',
                  value = '(ctWx13*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_911 = Coupling(name = 'GC_911',
                  value = '-((ctWx23*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_912 = Coupling(name = 'GC_912',
                  value = '(ctWx23*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_913 = Coupling(name = 'GC_913',
                  value = '-((ctWx31*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_914 = Coupling(name = 'GC_914',
                  value = '(ctWx31*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_915 = Coupling(name = 'GC_915',
                  value = '-((ctWx32*ee*complex(0,1)*vev)/Lambda**2)',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_916 = Coupling(name = 'GC_916',
                  value = '(ctWx32*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((ctG*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'DIM6':1,'DIM6_ctG':1})

GC_918 = Coupling(name = 'GC_918',
                  value = '(ctGI*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QCD':1,'DIM6':1,'DIM6_ctGI':1})

GC_919 = Coupling(name = 'GC_919',
                  value = '-((ctGIx13*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx13':1})

GC_920 = Coupling(name = 'GC_920',
                  value = '(ctGIx13*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx13':1})

GC_921 = Coupling(name = 'GC_921',
                  value = '-((ctGIx23*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx23':1})

GC_922 = Coupling(name = 'GC_922',
                  value = '(ctGIx23*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx23':1})

GC_923 = Coupling(name = 'GC_923',
                  value = '-((ctGIx31*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx31':1})

GC_924 = Coupling(name = 'GC_924',
                  value = '(ctGIx31*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx31':1})

GC_925 = Coupling(name = 'GC_925',
                  value = '-((ctGIx32*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx32':1})

GC_926 = Coupling(name = 'GC_926',
                  value = '(ctGIx32*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGIx32':1})

GC_927 = Coupling(name = 'GC_927',
                  value = '-((ctGx13*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGx13':1})

GC_928 = Coupling(name = 'GC_928',
                  value = '-((ctGx23*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGx23':1})

GC_929 = Coupling(name = 'GC_929',
                  value = '-((ctGx31*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGx31':1})

GC_930 = Coupling(name = 'GC_930',
                  value = '-((ctGx32*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'QCD':1,'FCNC':1,'FCNC_ctGx32':1})

GC_931 = Coupling(name = 'GC_931',
                  value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_932 = Coupling(name = 'GC_932',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_933 = Coupling(name = 'GC_933',
                  value = '(ctW*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'DIM6_ctW':1})

GC_934 = Coupling(name = 'GC_934',
                  value = '(ctWI*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'DIM6_ctWI':1})

GC_935 = Coupling(name = 'GC_935',
                  value = '-((ctWIx13*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctWIx13':1})

GC_936 = Coupling(name = 'GC_936',
                  value = '(ctWIx13*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWIx13':1})

GC_937 = Coupling(name = 'GC_937',
                  value = '-((ctWIx23*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctWIx23':1})

GC_938 = Coupling(name = 'GC_938',
                  value = '(ctWIx23*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWIx23':1})

GC_939 = Coupling(name = 'GC_939',
                  value = '-((ctWIx31*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctWIx31':1})

GC_940 = Coupling(name = 'GC_940',
                  value = '(ctWIx31*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWIx31':1})

GC_941 = Coupling(name = 'GC_941',
                  value = '-((ctWIx32*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctWIx32':1})

GC_942 = Coupling(name = 'GC_942',
                  value = '(ctWIx32*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWIx32':1})

GC_943 = Coupling(name = 'GC_943',
                  value = '(ctWx13*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWx13':1})

GC_944 = Coupling(name = 'GC_944',
                  value = '(ctWx23*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWx23':1})

GC_945 = Coupling(name = 'GC_945',
                  value = '(ctWx31*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWx31':1})

GC_946 = Coupling(name = 'GC_946',
                  value = '(ctWx32*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctWx32':1})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((ctZ*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'DIM6':1,'DIM6_ctZ':1})

GC_948 = Coupling(name = 'GC_948',
                  value = '-((ctZI*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'DIM6':1,'DIM6_ctZI':1})

GC_949 = Coupling(name = 'GC_949',
                  value = '-((ctZIx13*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx13':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '(ctZIx13*cw*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx13':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '-((ctZIx23*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx23':1})

GC_952 = Coupling(name = 'GC_952',
                  value = '(ctZIx23*cw*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx23':1})

GC_953 = Coupling(name = 'GC_953',
                  value = '-((ctZIx31*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx31':1})

GC_954 = Coupling(name = 'GC_954',
                  value = '(ctZIx31*cw*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx31':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '-((ctZIx32*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZIx32':1})

GC_956 = Coupling(name = 'GC_956',
                  value = '(ctZIx32*cw*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'FCNC':1,'FCNC_ctZIx32':1})

GC_957 = Coupling(name = 'GC_957',
                  value = '-((ctZx13*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZx13':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '-((ctZx23*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZx23':1})

GC_959 = Coupling(name = 'GC_959',
                  value = '-((ctZx31*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZx31':1})

GC_960 = Coupling(name = 'GC_960',
                  value = '-((ctZx32*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'FCNC':1,'FCNC_ctZx32':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '-((cbW*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((cbWI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_963 = Coupling(name = 'GC_963',
                  value = '-((cbWIx13*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_964 = Coupling(name = 'GC_964',
                  value = '(cbWIx13*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_965 = Coupling(name = 'GC_965',
                  value = '-((cbWIx23*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_966 = Coupling(name = 'GC_966',
                  value = '(cbWIx23*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_967 = Coupling(name = 'GC_967',
                  value = '-((cbWIx31*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_968 = Coupling(name = 'GC_968',
                  value = '(cbWIx31*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '-((cbWIx32*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '(cbWIx32*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '-((cbWx13*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((cbWx23*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_973 = Coupling(name = 'GC_973',
                  value = '-((cbWx31*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((cbWx32*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_975 = Coupling(name = 'GC_975',
                  value = '(cpQ3*ee*complex(0,1)*vev*cmath.sqrt(2))/(Lambda**2*sw)',
                  order = {'QED':2,'DIM6':1,'DIM6_cpQ3':1})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((cpQ3Ix31*ee*vev*cmath.sqrt(2))/(Lambda**2*sw))',
                  order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_977 = Coupling(name = 'GC_977',
                  value = '(cpQ3Ix31*ee*vev*cmath.sqrt(2))/(Lambda**2*sw)',
                  order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_978 = Coupling(name = 'GC_978',
                  value = '-((cpQ3Ix32*ee*vev*cmath.sqrt(2))/(Lambda**2*sw))',
                  order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_979 = Coupling(name = 'GC_979',
                  value = '(cpQ3Ix32*ee*vev*cmath.sqrt(2))/(Lambda**2*sw)',
                  order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_980 = Coupling(name = 'GC_980',
                  value = '(cpQ3x31*ee*complex(0,1)*vev*cmath.sqrt(2))/(Lambda**2*sw)',
                  order = {'QED':2,'FCNC':1,'FCNC_cpQ3x31':1})

GC_981 = Coupling(name = 'GC_981',
                  value = '(cpQ3x32*ee*complex(0,1)*vev*cmath.sqrt(2))/(Lambda**2*sw)',
                  order = {'QED':2,'FCNC':1,'FCNC_cpQ3x32':1})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((cptb*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'DIM6':1,'DIM6_cptb':1})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((cptbI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'DIM6':1,'DIM6_cptbI':1})

GC_984 = Coupling(name = 'GC_984',
                  value = '(cptbI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':2,'DIM6':1,'DIM6_cptbI':1})

GC_985 = Coupling(name = 'GC_985',
                  value = '-((cptbIx13*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx13':1})

GC_986 = Coupling(name = 'GC_986',
                  value = '(cptbIx13*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx13':1})

GC_987 = Coupling(name = 'GC_987',
                  value = '-((cptbIx23*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx23':1})

GC_988 = Coupling(name = 'GC_988',
                  value = '(cptbIx23*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx23':1})

GC_989 = Coupling(name = 'GC_989',
                  value = '-((cptbIx31*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx31':1})

GC_990 = Coupling(name = 'GC_990',
                  value = '(cptbIx31*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx31':1})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((cptbIx32*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx32':1})

GC_992 = Coupling(name = 'GC_992',
                  value = '(cptbIx32*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbIx32':1})

GC_993 = Coupling(name = 'GC_993',
                  value = '-((cptbx13*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbx13':1})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((cptbx23*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbx23':1})

GC_995 = Coupling(name = 'GC_995',
                  value = '-((cptbx31*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbx31':1})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((cptbx32*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':2,'FCNC':1,'FCNC_cptbx32':1})

GC_997 = Coupling(name = 'GC_997',
                  value = '(ctW*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_998 = Coupling(name = 'GC_998',
                  value = '(ctWI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'DIM6':1,'DIM6_ctWI':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '-((ctWIx13*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '(ctWIx13*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '-((ctWIx23*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '(ctWIx23*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '-((ctWIx31*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(ctWIx31*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-((ctWIx32*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '(ctWIx32*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(ctWx13*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(ctWx23*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(ctWx31*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(ctWx32*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((cbW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(cbW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'DIM6':1,'DIM6_cbW':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(cbWI*cw*ee*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'DIM6':1,'DIM6_cbWI':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(cbWIx13*cw*ee*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWIx13':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(cbWIx23*cw*ee*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWIx23':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(cbWIx31*cw*ee*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWIx31':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(cbWIx32*cw*ee*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWIx32':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '-((cbWx13*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(cbWx13*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx13':1})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((cbWx23*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(cbWx23*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx23':1})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '-((cbWx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(cbWx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx31':1})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '-((cbWx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(cbWx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_cbWx32':1})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-((ctW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(ctW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'DIM6':1,'DIM6_ctW':1})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((ctWI*cw*ee*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'DIM6':1,'DIM6_ctWI':1})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-((ctWIx13*cw*ee*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx13':1})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-((ctWIx23*cw*ee*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx23':1})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-((ctWIx31*cw*ee*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx31':1})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '-((ctWIx32*cw*ee*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWIx32':1})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '-((ctWx13*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(ctWx13*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx13':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-((ctWx23*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(ctWx23*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx23':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((ctWx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(ctWx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx31':1})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '-((ctWx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(ctWx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                   order = {'QED':1,'FCNC':1,'FCNC_ctWx32':1})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((cbW*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'DIM6':1,'DIM6_cbW':1})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((cbWI*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'DIM6':1,'DIM6_cbWI':1})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((cbWIx13*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWIx13':1})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '(cbWIx13*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                   order = {'FCNC':1,'FCNC_cbWIx13':1})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '-((cbWIx23*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWIx23':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '(cbWIx23*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                   order = {'FCNC':1,'FCNC_cbWIx23':1})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '-((cbWIx31*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWIx31':1})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(cbWIx31*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                   order = {'FCNC':1,'FCNC_cbWIx31':1})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-((cbWIx32*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWIx32':1})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(cbWIx32*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                   order = {'FCNC':1,'FCNC_cbWIx32':1})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '-((cbWx13*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWx13':1})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((cbWx23*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWx23':1})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '-((cbWx31*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWx31':1})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-((cbWx32*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'FCNC':1,'FCNC_cbWx32':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(ctp*complex(0,1)*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'DIM6':1,'DIM6_ctp':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(ctpI*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'DIM6':1,'DIM6_ctpI':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '-((ctpIx13*vev**2)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx13':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(ctpIx13*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx13':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-((ctpIx23*vev**2)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx23':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '(ctpIx23*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx23':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-((ctpIx31*vev**2)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx31':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(ctpIx31*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx31':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-((ctpIx32*vev**2)/(Lambda**2*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx32':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '(ctpIx32*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpIx32':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '(ctpx13*complex(0,1)*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpx13':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(ctpx23*complex(0,1)*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpx23':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '(ctpx31*complex(0,1)*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpx31':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(ctpx32*complex(0,1)*vev**2)/(Lambda**2*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_ctpx32':1})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(cpQ3*ee*complex(0,1)*vev**2)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'DIM6':1,'DIM6_cpQ3':1})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-((cpQ3Ix31*ee*vev**2)/(Lambda**2*sw*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(cpQ3Ix31*ee*vev**2)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '-((cpQ3Ix32*ee*vev**2)/(Lambda**2*sw*cmath.sqrt(2)))',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '(cpQ3Ix32*ee*vev**2)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(cpQ3x31*ee*complex(0,1)*vev**2)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3x31':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '(cpQ3x32*ee*complex(0,1)*vev**2)/(Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3x32':1})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-(cptb*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'DIM6':1,'DIM6_cptb':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-(cptbI*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'DIM6':1,'DIM6_cptbI':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '(cptbI*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'DIM6':1,'DIM6_cptbI':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-(cptbIx13*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx13':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(cptbIx13*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx13':1})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '-(cptbIx23*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx23':1})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(cptbIx23*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx23':1})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-(cptbIx31*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx31':1})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '(cptbIx31*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx31':1})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-(cptbIx32*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx32':1})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(cptbIx32*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbIx32':1})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-(cptbx13*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbx13':1})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-(cptbx23*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbx23':1})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-(cptbx31*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbx31':1})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-(cptbx32*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                   order = {'QED':1,'FCNC':1,'FCNC_cptbx32':1})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-((cpb*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpb*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'DIM6':1,'DIM6_cpb':1})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '-((cpbIx31*cw*ee*vev)/(Lambda**2*sw)) - (cpbIx31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpbIx31':1})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(cpbIx31*cw*ee*vev)/(Lambda**2*sw) + (cpbIx31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpbIx31':1})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '-((cpbIx32*cw*ee*vev)/(Lambda**2*sw)) - (cpbIx32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpbIx32':1})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(cpbIx32*cw*ee*vev)/(Lambda**2*sw) + (cpbIx32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpbIx32':1})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '-((cpbx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpbx31*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpbx31':1})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-((cpbx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpbx32*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpbx32':1})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '(-2*cpQ3*cw*ee*complex(0,1)*vev)/(Lambda**2*sw) - (2*cpQ3*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'DIM6':1,'DIM6_cpQ3':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(-2*cpQ3Ix31*cw*ee*vev)/(Lambda**2*sw) - (2*cpQ3Ix31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '(2*cpQ3Ix31*cw*ee*vev)/(Lambda**2*sw) + (2*cpQ3Ix31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(-2*cpQ3Ix32*cw*ee*vev)/(Lambda**2*sw) - (2*cpQ3Ix32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '(2*cpQ3Ix32*cw*ee*vev)/(Lambda**2*sw) + (2*cpQ3Ix32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '(-2*cpQ3x31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw) - (2*cpQ3x31*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQ3x31':1})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(-2*cpQ3x32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw) - (2*cpQ3x32*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQ3x32':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '-((cpQM*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpQM*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'DIM6':1,'DIM6_cpQM':1})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((cpQMIx31*cw*ee*vev)/(Lambda**2*sw)) - (cpQMIx31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQMIx31':1})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(cpQMIx31*cw*ee*vev)/(Lambda**2*sw) + (cpQMIx31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQMIx31':1})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '-((cpQMIx32*cw*ee*vev)/(Lambda**2*sw)) - (cpQMIx32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQMIx32':1})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(cpQMIx32*cw*ee*vev)/(Lambda**2*sw) + (cpQMIx32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQMIx32':1})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '-((cpQMx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpQMx31*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQMx31':1})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '-((cpQMx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpQMx32*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cpQMx32':1})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-((cpt*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpt*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'DIM6':1,'DIM6_cpt':1})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '-((cptIx31*cw*ee*vev)/(Lambda**2*sw)) - (cptIx31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cptIx31':1})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(cptIx31*cw*ee*vev)/(Lambda**2*sw) + (cptIx31*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cptIx31':1})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '-((cptIx32*cw*ee*vev)/(Lambda**2*sw)) - (cptIx32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cptIx32':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '(cptIx32*cw*ee*vev)/(Lambda**2*sw) + (cptIx32*ee*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cptIx32':1})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '-((cptx31*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cptx31*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cptx31':1})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-((cptx32*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cptx32*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                   order = {'QED':2,'FCNC':1,'FCNC_cptx32':1})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '-(ee**2*complex(0,1)*vev)/4. - (ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                   order = {'QED':1})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(ee**2*complex(0,1)*vev)/2. + (ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                   order = {'QED':1})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '-(cpb*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpb*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'DIM6':1,'DIM6_cpb':1})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-(cpbIx31*cw*ee*vev**2)/(2.*Lambda**2*sw) - (cpbIx31*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpbIx31':1})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(cpbIx31*cw*ee*vev**2)/(2.*Lambda**2*sw) + (cpbIx31*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpbIx31':1})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-(cpbIx32*cw*ee*vev**2)/(2.*Lambda**2*sw) - (cpbIx32*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpbIx32':1})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(cpbIx32*cw*ee*vev**2)/(2.*Lambda**2*sw) + (cpbIx32*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpbIx32':1})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '-(cpbx31*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpbx31*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpbx31':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '-(cpbx32*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpbx32*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpbx32':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '-((cpQ3*cw*ee*complex(0,1)*vev**2)/(Lambda**2*sw)) - (cpQ3*ee*complex(0,1)*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'DIM6':1,'DIM6_cpQ3':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '-((cpQ3Ix31*cw*ee*vev**2)/(Lambda**2*sw)) - (cpQ3Ix31*ee*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(cpQ3Ix31*cw*ee*vev**2)/(Lambda**2*sw) + (cpQ3Ix31*ee*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix31':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-((cpQ3Ix32*cw*ee*vev**2)/(Lambda**2*sw)) - (cpQ3Ix32*ee*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '(cpQ3Ix32*cw*ee*vev**2)/(Lambda**2*sw) + (cpQ3Ix32*ee*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3Ix32':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '-((cpQ3x31*cw*ee*complex(0,1)*vev**2)/(Lambda**2*sw)) - (cpQ3x31*ee*complex(0,1)*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3x31':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-((cpQ3x32*cw*ee*complex(0,1)*vev**2)/(Lambda**2*sw)) - (cpQ3x32*ee*complex(0,1)*sw*vev**2)/(cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQ3x32':1})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '-(cpQM*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpQM*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'DIM6':1,'DIM6_cpQM':1})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '-(cpQMIx31*cw*ee*vev**2)/(2.*Lambda**2*sw) - (cpQMIx31*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQMIx31':1})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '(cpQMIx31*cw*ee*vev**2)/(2.*Lambda**2*sw) + (cpQMIx31*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQMIx31':1})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-(cpQMIx32*cw*ee*vev**2)/(2.*Lambda**2*sw) - (cpQMIx32*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQMIx32':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(cpQMIx32*cw*ee*vev**2)/(2.*Lambda**2*sw) + (cpQMIx32*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQMIx32':1})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '-(cpQMx31*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpQMx31*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQMx31':1})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-(cpQMx32*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpQMx32*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cpQMx32':1})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-(cpt*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpt*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'DIM6':1,'DIM6_cpt':1})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '-(cptIx31*cw*ee*vev**2)/(2.*Lambda**2*sw) - (cptIx31*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cptIx31':1})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(cptIx31*cw*ee*vev**2)/(2.*Lambda**2*sw) + (cptIx31*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cptIx31':1})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '-(cptIx32*cw*ee*vev**2)/(2.*Lambda**2*sw) - (cptIx32*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cptIx32':1})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '(cptIx32*cw*ee*vev**2)/(2.*Lambda**2*sw) + (cptIx32*ee*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cptIx32':1})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-(cptx31*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cptx31*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cptx31':1})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-(cptx32*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cptx32*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                   order = {'QED':1,'FCNC':1,'FCNC_cptx32':1})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                   order = {'QED':1})

