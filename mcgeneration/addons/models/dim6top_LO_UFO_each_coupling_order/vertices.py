# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.1.0 for Linux x86 (64-bit) (March 13, 2017)
# Date: Wed 6 Jun 2018 14:05:50


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_9})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_800})

V_3 = Vertex(name = 'V_3',
             particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
             particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_4})

V_5 = Vertex(name = 'V_5',
             particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
             particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
             color = [ '1' ],
             lorentz = [ L.UUS1 ],
             couplings = {(0,0):C.GC_931})

V_7 = Vertex(name = 'V_7',
             particles = [ P.ghWm, P.ghWm__tilde__, P.a ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_4})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_752})

V_9 = Vertex(name = 'V_9',
             particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_751})

V_10 = Vertex(name = 'V_10',
              particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_4})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_931})

V_12 = Vertex(name = 'V_12',
              particles = [ P.ghWp, P.ghWp__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_3})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_751})

V_14 = Vertex(name = 'V_14',
              particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_752})

V_15 = Vertex(name = 'V_15',
              particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_751})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_752})

V_17 = Vertex(name = 'V_17',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_1119})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_6})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_6})

V_20 = Vertex(name = 'V_20',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_8,(0,0):C.GC_8,(2,2):C.GC_8})

V_21 = Vertex(name = 'V_21',
              particles = [ P.c__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS3, L.FFVS6 ],
              couplings = {(0,1):C.GC_779,(0,2):C.GC_762,(0,0):C.GC_759})

V_22 = Vertex(name = 'V_22',
              particles = [ P.c__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,1):C.GC_767,(0,0):C.GC_765})

V_23 = Vertex(name = 'V_23',
              particles = [ P.c__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,1):C.GC_777,(0,0):C.GC_772})

V_24 = Vertex(name = 'V_24',
              particles = [ P.c__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS6 ],
              couplings = {(0,0):C.GC_781})

V_25 = Vertex(name = 'V_25',
              particles = [ P.c__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_938,(0,0):C.GC_941})

V_26 = Vertex(name = 'V_26',
              particles = [ P.c__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_944,(0,0):C.GC_946})

V_27 = Vertex(name = 'V_27',
              particles = [ P.c__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_951,(0,0):C.GC_956})

V_28 = Vertex(name = 'V_28',
              particles = [ P.c__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_958,(0,0):C.GC_960})

V_29 = Vertex(name = 'V_29',
              particles = [ P.t__tilde__, P.c, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_763,(0,1):C.GC_758})

V_30 = Vertex(name = 'V_30',
              particles = [ P.t__tilde__, P.c, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_767,(0,1):C.GC_765})

V_31 = Vertex(name = 'V_31',
              particles = [ P.t__tilde__, P.c, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_776,(0,1):C.GC_773})

V_32 = Vertex(name = 'V_32',
              particles = [ P.t__tilde__, P.c, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_781,(0,1):C.GC_779})

V_33 = Vertex(name = 'V_33',
              particles = [ P.t__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3, L.FFV4 ],
              couplings = {(0,2):C.GC_942,(0,1):C.GC_946,(0,0):C.GC_937})

V_34 = Vertex(name = 'V_34',
              particles = [ P.t__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_955,(0,0):C.GC_944})

V_35 = Vertex(name = 'V_35',
              particles = [ P.t__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_960,(0,0):C.GC_952})

V_36 = Vertex(name = 'V_36',
              particles = [ P.t__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11 ],
              couplings = {(0,0):C.GC_958})

V_37 = Vertex(name = 'V_37',
              particles = [ P.t__tilde__, P.u, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_761,(0,1):C.GC_756})

V_38 = Vertex(name = 'V_38',
              particles = [ P.t__tilde__, P.u, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_766,(0,1):C.GC_764})

V_39 = Vertex(name = 'V_39',
              particles = [ P.t__tilde__, P.u, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_774,(0,1):C.GC_771})

V_40 = Vertex(name = 'V_40',
              particles = [ P.t__tilde__, P.u, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_780,(0,1):C.GC_778})

V_41 = Vertex(name = 'V_41',
              particles = [ P.t__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_940,(0,0):C.GC_935})

V_42 = Vertex(name = 'V_42',
              particles = [ P.t__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_945,(0,0):C.GC_943})

V_43 = Vertex(name = 'V_43',
              particles = [ P.t__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_953,(0,0):C.GC_950})

V_44 = Vertex(name = 'V_44',
              particles = [ P.t__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_959,(0,0):C.GC_957})

V_45 = Vertex(name = 'V_45',
              particles = [ P.u__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_757,(0,1):C.GC_760})

V_46 = Vertex(name = 'V_46',
              particles = [ P.u__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_764,(0,1):C.GC_766})

V_47 = Vertex(name = 'V_47',
              particles = [ P.u__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_770,(0,1):C.GC_775})

V_48 = Vertex(name = 'V_48',
              particles = [ P.u__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS6 ],
              couplings = {(0,0):C.GC_778,(0,1):C.GC_780})

V_49 = Vertex(name = 'V_49',
              particles = [ P.u__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_936,(0,0):C.GC_939})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_943,(0,0):C.GC_945})

V_51 = Vertex(name = 'V_51',
              particles = [ P.u__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_949,(0,0):C.GC_954})

V_52 = Vertex(name = 'V_52',
              particles = [ P.u__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV3 ],
              couplings = {(0,1):C.GC_957,(0,0):C.GC_959})

V_53 = Vertex(name = 'V_53',
              particles = [ P.c__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1109,(0,2):C.GC_1116,(0,1):C.GC_668,(0,3):C.GC_671})

V_54 = Vertex(name = 'V_54',
              particles = [ P.c__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1111,(0,2):C.GC_1118,(0,1):C.GC_674,(0,3):C.GC_676})

V_55 = Vertex(name = 'V_55',
              particles = [ P.c__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1139,(0,3):C.GC_1146,(0,2):C.GC_864,(0,0):C.GC_867})

V_56 = Vertex(name = 'V_56',
              particles = [ P.c__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1141,(0,3):C.GC_1148,(0,2):C.GC_870,(0,0):C.GC_872})

V_57 = Vertex(name = 'V_57',
              particles = [ P.t__tilde__, P.c, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1108,(0,2):C.GC_1115,(0,1):C.GC_672,(0,3):C.GC_667})

V_58 = Vertex(name = 'V_58',
              particles = [ P.t__tilde__, P.c, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1111,(0,2):C.GC_1118,(0,1):C.GC_676,(0,3):C.GC_674})

V_59 = Vertex(name = 'V_59',
              particles = [ P.t__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1138,(0,3):C.GC_1145,(0,2):C.GC_868,(0,0):C.GC_863})

V_60 = Vertex(name = 'V_60',
              particles = [ P.t__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1141,(0,3):C.GC_1148,(0,2):C.GC_872,(0,0):C.GC_870})

V_61 = Vertex(name = 'V_61',
              particles = [ P.t__tilde__, P.u, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1106,(0,2):C.GC_1113,(0,1):C.GC_670,(0,3):C.GC_665})

V_62 = Vertex(name = 'V_62',
              particles = [ P.t__tilde__, P.u, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1110,(0,2):C.GC_1117,(0,1):C.GC_675,(0,3):C.GC_673})

V_63 = Vertex(name = 'V_63',
              particles = [ P.t__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1136,(0,3):C.GC_1143,(0,2):C.GC_866,(0,0):C.GC_861})

V_64 = Vertex(name = 'V_64',
              particles = [ P.t__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1140,(0,3):C.GC_1147,(0,2):C.GC_871,(0,0):C.GC_869})

V_65 = Vertex(name = 'V_65',
              particles = [ P.u__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1107,(0,2):C.GC_1114,(0,1):C.GC_666,(0,3):C.GC_669})

V_66 = Vertex(name = 'V_66',
              particles = [ P.u__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_1110,(0,2):C.GC_1117,(0,1):C.GC_673,(0,3):C.GC_675})

V_67 = Vertex(name = 'V_67',
              particles = [ P.u__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1137,(0,3):C.GC_1144,(0,2):C.GC_862,(0,0):C.GC_865})

V_68 = Vertex(name = 'V_68',
              particles = [ P.u__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,1):C.GC_1140,(0,3):C.GC_1147,(0,2):C.GC_869,(0,0):C.GC_871})

V_69 = Vertex(name = 'V_69',
              particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,1):C.GC_648,(0,3):C.GC_67,(0,2):C.GC_982,(0,0):C.GC_975})

V_70 = Vertex(name = 'V_70',
              particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS2, L.FFVS4, L.FFVS6 ],
              couplings = {(0,0):C.GC_650,(0,2):C.GC_68,(0,1):C.GC_984})

V_71 = Vertex(name = 'V_71',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,2):C.GC_844,(0,0):C.GC_801,(0,1):C.GC_748,(0,3):C.GC_1076})

V_72 = Vertex(name = 'V_72',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,2):C.GC_846,(0,0):C.GC_802,(0,1):C.GC_1069,(0,3):C.GC_1078})

V_73 = Vertex(name = 'V_73',
              particles = [ P.t__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS5, L.FFVS7 ],
              couplings = {(0,1):C.GC_754,(0,0):C.GC_755})

V_74 = Vertex(name = 'V_74',
              particles = [ P.t__tilde__, P.t, P.a, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS5, L.FFVS7 ],
              couplings = {(0,1):C.GC_768,(0,0):C.GC_769})

V_75 = Vertex(name = 'V_75',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV12, L.FFV7 ],
              couplings = {(0,2):C.GC_2,(0,1):C.GC_933,(0,0):C.GC_934})

V_76 = Vertex(name = 'V_76',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV12 ],
              couplings = {(0,1):C.GC_947,(0,0):C.GC_948})

V_77 = Vertex(name = 'V_77',
              particles = [ P.t__tilde__, P.t, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS7 ],
              couplings = {(0,0):C.GC_1105,(0,1):C.GC_1112,(0,3):C.GC_663,(0,2):C.GC_664})

V_78 = Vertex(name = 'V_78',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV10, L.FFV12, L.FFV2, L.FFV5, L.FFV9 ],
              couplings = {(0,2):C.GC_750,(0,4):C.GC_782,(0,3):C.GC_1142,(0,1):C.GC_859,(0,0):C.GC_860})

V_79 = Vertex(name = 'V_79',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_1135})

V_80 = Vertex(name = 'V_80',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_177,(0,11):C.GC_541,(0,9):C.GC_540,(0,8):C.GC_540,(0,4):C.GC_465,(0,3):C.GC_135,(0,5):C.GC_441,(0,6):C.GC_406,(0,7):C.GC_548,(0,2):C.GC_549,(0,1):C.GC_549,(0,0):C.GC_470})

V_81 = Vertex(name = 'V_81',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_188,(0,11):C.GC_588,(0,9):C.GC_587,(0,8):C.GC_587,(0,4):C.GC_489,(0,3):C.GC_146,(0,5):C.GC_632,(0,6):C.GC_417,(0,7):C.GC_596,(0,2):C.GC_595,(0,1):C.GC_595,(0,0):C.GC_493})

V_82 = Vertex(name = 'V_82',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_542,(0,0):C.GC_547})

V_83 = Vertex(name = 'V_83',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_590,(0,0):C.GC_598})

V_84 = Vertex(name = 'V_84',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_181,(0,11):C.GC_557,(0,9):C.GC_556,(0,8):C.GC_556,(0,4):C.GC_473,(0,3):C.GC_139,(0,5):C.GC_445,(0,6):C.GC_410,(0,7):C.GC_564,(0,2):C.GC_565,(0,1):C.GC_565,(0,0):C.GC_478})

V_85 = Vertex(name = 'V_85',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_190,(0,11):C.GC_604,(0,9):C.GC_603,(0,8):C.GC_603,(0,4):C.GC_497,(0,3):C.GC_148,(0,5):C.GC_634,(0,6):C.GC_419,(0,7):C.GC_612,(0,2):C.GC_611,(0,1):C.GC_611,(0,0):C.GC_501})

V_86 = Vertex(name = 'V_86',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_558,(0,0):C.GC_563})

V_87 = Vertex(name = 'V_87',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_606,(0,0):C.GC_614})

V_88 = Vertex(name = 'V_88',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_185,(0,11):C.GC_573,(0,9):C.GC_572,(0,8):C.GC_572,(0,4):C.GC_481,(0,3):C.GC_143,(0,5):C.GC_449,(0,6):C.GC_414,(0,7):C.GC_580,(0,2):C.GC_581,(0,1):C.GC_581,(0,0):C.GC_486})

V_89 = Vertex(name = 'V_89',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_192,(0,11):C.GC_620,(0,9):C.GC_619,(0,8):C.GC_619,(0,4):C.GC_505,(0,3):C.GC_150,(0,5):C.GC_636,(0,6):C.GC_421,(0,7):C.GC_628,(0,2):C.GC_627,(0,1):C.GC_627,(0,0):C.GC_509})

V_90 = Vertex(name = 'V_90',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_574,(0,0):C.GC_579})

V_91 = Vertex(name = 'V_91',
              particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_622,(0,0):C.GC_630})

V_92 = Vertex(name = 'V_92',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_178,(0,11):C.GC_549,(0,9):C.GC_548,(0,8):C.GC_548,(0,4):C.GC_469,(0,3):C.GC_442,(0,5):C.GC_136,(0,6):C.GC_407,(0,7):C.GC_540,(0,2):C.GC_541,(0,1):C.GC_541,(0,0):C.GC_466})

V_93 = Vertex(name = 'V_93',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_188,(0,11):C.GC_596,(0,9):C.GC_595,(0,8):C.GC_595,(0,4):C.GC_493,(0,3):C.GC_632,(0,5):C.GC_146,(0,6):C.GC_417,(0,7):C.GC_588,(0,2):C.GC_587,(0,1):C.GC_587,(0,0):C.GC_489})

V_94 = Vertex(name = 'V_94',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_550,(0,0):C.GC_539})

V_95 = Vertex(name = 'V_95',
              particles = [ P.t__tilde__, P.c, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_598,(0,0):C.GC_590})

V_96 = Vertex(name = 'V_96',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_182,(0,11):C.GC_565,(0,9):C.GC_564,(0,8):C.GC_564,(0,4):C.GC_477,(0,3):C.GC_446,(0,5):C.GC_140,(0,6):C.GC_411,(0,7):C.GC_556,(0,2):C.GC_557,(0,1):C.GC_557,(0,0):C.GC_474})

V_97 = Vertex(name = 'V_97',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
              couplings = {(0,10):C.GC_190,(0,11):C.GC_612,(0,9):C.GC_611,(0,8):C.GC_611,(0,4):C.GC_501,(0,3):C.GC_634,(0,5):C.GC_148,(0,6):C.GC_419,(0,7):C.GC_604,(0,2):C.GC_603,(0,1):C.GC_603,(0,0):C.GC_497})

V_98 = Vertex(name = 'V_98',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_566,(0,0):C.GC_555})

V_99 = Vertex(name = 'V_99',
              particles = [ P.t__tilde__, P.c, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF12, L.FFFF2 ],
              couplings = {(0,1):C.GC_614,(0,0):C.GC_606})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_186,(0,11):C.GC_581,(0,9):C.GC_580,(0,8):C.GC_580,(0,4):C.GC_485,(0,3):C.GC_450,(0,5):C.GC_144,(0,6):C.GC_415,(0,7):C.GC_572,(0,2):C.GC_573,(0,1):C.GC_573,(0,0):C.GC_482})

V_101 = Vertex(name = 'V_101',
               particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_192,(0,11):C.GC_628,(0,9):C.GC_627,(0,8):C.GC_627,(0,4):C.GC_509,(0,3):C.GC_636,(0,5):C.GC_150,(0,6):C.GC_421,(0,7):C.GC_620,(0,2):C.GC_619,(0,1):C.GC_619,(0,0):C.GC_505})

V_102 = Vertex(name = 'V_102',
               particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_582,(0,0):C.GC_571})

V_103 = Vertex(name = 'V_103',
               particles = [ P.t__tilde__, P.c, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_630,(0,0):C.GC_622})

V_104 = Vertex(name = 'V_104',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_176,(0,11):C.GC_545,(0,9):C.GC_544,(0,8):C.GC_544,(0,4):C.GC_467,(0,3):C.GC_134,(0,5):C.GC_440,(0,6):C.GC_405,(0,7):C.GC_536,(0,2):C.GC_537,(0,1):C.GC_537,(0,0):C.GC_464})

V_105 = Vertex(name = 'V_105',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_187,(0,11):C.GC_592,(0,9):C.GC_591,(0,8):C.GC_591,(0,4):C.GC_491,(0,3):C.GC_145,(0,5):C.GC_631,(0,6):C.GC_416,(0,7):C.GC_584,(0,2):C.GC_583,(0,1):C.GC_583,(0,0):C.GC_487})

V_106 = Vertex(name = 'V_106',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_546,(0,0):C.GC_535})

V_107 = Vertex(name = 'V_107',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_594,(0,0):C.GC_586})

V_108 = Vertex(name = 'V_108',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_180,(0,11):C.GC_561,(0,9):C.GC_560,(0,8):C.GC_560,(0,4):C.GC_475,(0,3):C.GC_138,(0,5):C.GC_444,(0,6):C.GC_409,(0,7):C.GC_552,(0,2):C.GC_553,(0,1):C.GC_553,(0,0):C.GC_472})

V_109 = Vertex(name = 'V_109',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_189,(0,11):C.GC_608,(0,9):C.GC_607,(0,8):C.GC_607,(0,4):C.GC_499,(0,3):C.GC_147,(0,5):C.GC_633,(0,6):C.GC_418,(0,7):C.GC_600,(0,2):C.GC_599,(0,1):C.GC_599,(0,0):C.GC_495})

V_110 = Vertex(name = 'V_110',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_562,(0,0):C.GC_551})

V_111 = Vertex(name = 'V_111',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_610,(0,0):C.GC_602})

V_112 = Vertex(name = 'V_112',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,12):C.GC_577,(0,11):C.GC_184,(0,9):C.GC_576,(0,8):C.GC_623,(0,10):C.GC_576,(0,4):C.GC_483,(0,7):C.GC_568,(0,3):C.GC_142,(0,5):C.GC_448,(0,6):C.GC_413,(0,2):C.GC_569,(0,1):C.GC_569,(0,0):C.GC_480})

V_113 = Vertex(name = 'V_113',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_624,(0,9):C.GC_191,(0,8):C.GC_623,(0,4):C.GC_507,(0,7):C.GC_616,(0,3):C.GC_149,(0,5):C.GC_635,(0,6):C.GC_420,(0,2):C.GC_615,(0,1):C.GC_615,(0,0):C.GC_503})

V_114 = Vertex(name = 'V_114',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_578,(0,0):C.GC_567})

V_115 = Vertex(name = 'V_115',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_626,(0,0):C.GC_618})

V_116 = Vertex(name = 'V_116',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_175,(0,11):C.GC_537,(0,9):C.GC_536,(0,8):C.GC_536,(0,4):C.GC_463,(0,3):C.GC_133,(0,5):C.GC_439,(0,6):C.GC_404,(0,7):C.GC_544,(0,2):C.GC_545,(0,1):C.GC_545,(0,0):C.GC_468})

V_117 = Vertex(name = 'V_117',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_187,(0,11):C.GC_584,(0,9):C.GC_583,(0,8):C.GC_583,(0,4):C.GC_487,(0,3):C.GC_145,(0,5):C.GC_631,(0,6):C.GC_416,(0,7):C.GC_592,(0,2):C.GC_591,(0,1):C.GC_591,(0,0):C.GC_491})

V_118 = Vertex(name = 'V_118',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_538,(0,0):C.GC_543})

V_119 = Vertex(name = 'V_119',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_586,(0,0):C.GC_594})

V_120 = Vertex(name = 'V_120',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_179,(0,11):C.GC_553,(0,9):C.GC_552,(0,8):C.GC_552,(0,4):C.GC_471,(0,3):C.GC_137,(0,5):C.GC_443,(0,6):C.GC_408,(0,7):C.GC_560,(0,2):C.GC_561,(0,1):C.GC_561,(0,0):C.GC_476})

V_121 = Vertex(name = 'V_121',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_189,(0,11):C.GC_600,(0,9):C.GC_599,(0,8):C.GC_599,(0,4):C.GC_495,(0,3):C.GC_147,(0,5):C.GC_633,(0,6):C.GC_418,(0,7):C.GC_608,(0,2):C.GC_607,(0,1):C.GC_607,(0,0):C.GC_499})

V_122 = Vertex(name = 'V_122',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_554,(0,0):C.GC_559})

V_123 = Vertex(name = 'V_123',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_602,(0,0):C.GC_610})

V_124 = Vertex(name = 'V_124',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_183,(0,11):C.GC_569,(0,9):C.GC_568,(0,8):C.GC_568,(0,4):C.GC_479,(0,3):C.GC_141,(0,5):C.GC_447,(0,6):C.GC_412,(0,7):C.GC_576,(0,2):C.GC_577,(0,1):C.GC_577,(0,0):C.GC_484})

V_125 = Vertex(name = 'V_125',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_191,(0,11):C.GC_616,(0,9):C.GC_615,(0,8):C.GC_615,(0,4):C.GC_503,(0,3):C.GC_149,(0,5):C.GC_635,(0,6):C.GC_420,(0,7):C.GC_624,(0,2):C.GC_623,(0,1):C.GC_623,(0,0):C.GC_507})

V_126 = Vertex(name = 'V_126',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_570,(0,0):C.GC_575})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_618,(0,0):C.GC_626})

V_128 = Vertex(name = 'V_128',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,3):C.GC_157,(0,4):C.GC_548,(0,2):C.GC_549,(0,1):C.GC_549,(0,0):C.GC_470,(0,5):C.GC_26})

V_129 = Vertex(name = 'V_129',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,3):C.GC_167,(0,4):C.GC_595,(0,2):C.GC_596,(0,1):C.GC_596,(0,0):C.GC_494,(0,5):C.GC_46})

V_130 = Vertex(name = 'V_130',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_547})

V_131 = Vertex(name = 'V_131',
               particles = [ P.b__tilde__, P.c, P.ve__tilde__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_597})

V_132 = Vertex(name = 'V_132',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_155,(0,5):C.GC_544,(0,3):C.GC_545,(0,2):C.GC_545,(0,1):C.GC_468,(0,0):C.GC_24})

V_133 = Vertex(name = 'V_133',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_166,(0,5):C.GC_591,(0,3):C.GC_592,(0,2):C.GC_592,(0,1):C.GC_492,(0,0):C.GC_45})

V_134 = Vertex(name = 'V_134',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_543})

V_135 = Vertex(name = 'V_135',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_593})

V_136 = Vertex(name = 'V_136',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_154,(0,5):C.GC_536,(0,3):C.GC_537,(0,2):C.GC_537,(0,1):C.GC_464,(0,0):C.GC_20})

V_137 = Vertex(name = 'V_137',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_166,(0,5):C.GC_583,(0,3):C.GC_584,(0,2):C.GC_584,(0,1):C.GC_488,(0,0):C.GC_43})

V_138 = Vertex(name = 'V_138',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_535})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_585})

V_140 = Vertex(name = 'V_140',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_156,(0,5):C.GC_540,(0,3):C.GC_541,(0,2):C.GC_541,(0,1):C.GC_466,(0,0):C.GC_22})

V_141 = Vertex(name = 'V_141',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_167,(0,5):C.GC_587,(0,3):C.GC_588,(0,2):C.GC_588,(0,1):C.GC_490,(0,0):C.GC_44})

V_142 = Vertex(name = 'V_142',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_539})

V_143 = Vertex(name = 'V_143',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_589})

V_144 = Vertex(name = 'V_144',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,3):C.GC_161,(0,4):C.GC_564,(0,2):C.GC_565,(0,1):C.GC_565,(0,0):C.GC_478,(0,5):C.GC_34})

V_145 = Vertex(name = 'V_145',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,3):C.GC_169,(0,4):C.GC_611,(0,2):C.GC_612,(0,1):C.GC_612,(0,0):C.GC_502,(0,5):C.GC_50})

V_146 = Vertex(name = 'V_146',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_563})

V_147 = Vertex(name = 'V_147',
               particles = [ P.b__tilde__, P.c, P.vm__tilde__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_613})

V_148 = Vertex(name = 'V_148',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_159,(0,5):C.GC_560,(0,3):C.GC_561,(0,2):C.GC_561,(0,1):C.GC_476,(0,0):C.GC_32})

V_149 = Vertex(name = 'V_149',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_168,(0,5):C.GC_607,(0,3):C.GC_608,(0,2):C.GC_608,(0,1):C.GC_500,(0,0):C.GC_49})

V_150 = Vertex(name = 'V_150',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_559})

V_151 = Vertex(name = 'V_151',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_609})

V_152 = Vertex(name = 'V_152',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_158,(0,5):C.GC_552,(0,3):C.GC_553,(0,2):C.GC_553,(0,1):C.GC_472,(0,0):C.GC_28})

V_153 = Vertex(name = 'V_153',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_168,(0,5):C.GC_599,(0,3):C.GC_600,(0,2):C.GC_600,(0,1):C.GC_496,(0,0):C.GC_47})

V_154 = Vertex(name = 'V_154',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_551})

V_155 = Vertex(name = 'V_155',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_601})

V_156 = Vertex(name = 'V_156',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_160,(0,5):C.GC_556,(0,3):C.GC_557,(0,2):C.GC_557,(0,1):C.GC_474,(0,0):C.GC_30})

V_157 = Vertex(name = 'V_157',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_169,(0,5):C.GC_603,(0,3):C.GC_604,(0,2):C.GC_604,(0,1):C.GC_498,(0,0):C.GC_48})

V_158 = Vertex(name = 'V_158',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_555})

V_159 = Vertex(name = 'V_159',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_605})

V_160 = Vertex(name = 'V_160',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,3):C.GC_165,(0,4):C.GC_580,(0,2):C.GC_581,(0,1):C.GC_581,(0,0):C.GC_486,(0,5):C.GC_42})

V_161 = Vertex(name = 'V_161',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,3):C.GC_171,(0,4):C.GC_627,(0,2):C.GC_628,(0,1):C.GC_628,(0,0):C.GC_510,(0,5):C.GC_54})

V_162 = Vertex(name = 'V_162',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_579})

V_163 = Vertex(name = 'V_163',
               particles = [ P.b__tilde__, P.c, P.vt__tilde__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_629})

V_164 = Vertex(name = 'V_164',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_163,(0,5):C.GC_576,(0,3):C.GC_577,(0,2):C.GC_577,(0,1):C.GC_484,(0,0):C.GC_40})

V_165 = Vertex(name = 'V_165',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_170,(0,5):C.GC_623,(0,3):C.GC_624,(0,2):C.GC_624,(0,1):C.GC_508,(0,0):C.GC_53})

V_166 = Vertex(name = 'V_166',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_575})

V_167 = Vertex(name = 'V_167',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_625})

V_168 = Vertex(name = 'V_168',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_162,(0,5):C.GC_568,(0,3):C.GC_569,(0,2):C.GC_569,(0,1):C.GC_480,(0,0):C.GC_36})

V_169 = Vertex(name = 'V_169',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_170,(0,5):C.GC_615,(0,3):C.GC_616,(0,2):C.GC_616,(0,1):C.GC_504,(0,0):C.GC_51})

V_170 = Vertex(name = 'V_170',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_567})

V_171 = Vertex(name = 'V_171',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_617})

V_172 = Vertex(name = 'V_172',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_164,(0,5):C.GC_572,(0,3):C.GC_573,(0,2):C.GC_573,(0,1):C.GC_482,(0,0):C.GC_38})

V_173 = Vertex(name = 'V_173',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_171,(0,5):C.GC_619,(0,3):C.GC_620,(0,2):C.GC_620,(0,1):C.GC_506,(0,0):C.GC_52})

V_174 = Vertex(name = 'V_174',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_571})

V_175 = Vertex(name = 'V_175',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_621})

V_176 = Vertex(name = 'V_176',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,1):C.GC_1055,(0,0):C.GC_1056})

V_177 = Vertex(name = 'V_177',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1150})

V_178 = Vertex(name = 'V_178',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS4 ],
               couplings = {(0,1):C.GC_830,(0,0):C.GC_831})

V_179 = Vertex(name = 'V_179',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_67,(0,3):C.GC_648,(0,2):C.GC_982,(0,0):C.GC_975})

V_180 = Vertex(name = 'V_180',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_69,(0,2):C.GC_649,(0,1):C.GC_983})

V_181 = Vertex(name = 'V_181',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_801,(0,0):C.GC_844,(0,1):C.GC_748,(0,3):C.GC_1076})

V_182 = Vertex(name = 'V_182',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_803,(0,0):C.GC_845,(0,1):C.GC_1069,(0,3):C.GC_1077})

V_183 = Vertex(name = 'V_183',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS7 ],
               couplings = {(0,1):C.GC_784,(0,0):C.GC_785})

V_184 = Vertex(name = 'V_184',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV12, L.FFV7 ],
               couplings = {(0,2):C.GC_1,(0,1):C.GC_1041,(0,0):C.GC_1042})

V_185 = Vertex(name = 'V_185',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS5, L.FFVS7 ],
               couplings = {(0,0):C.GC_1098,(0,1):C.GC_1091,(0,3):C.GC_731,(0,2):C.GC_732})

V_186 = Vertex(name = 'V_186',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1105})

V_187 = Vertex(name = 'V_187',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV12, L.FFV2, L.FFV5, L.FFV6 ],
               couplings = {(0,2):C.GC_749,(0,4):C.GC_782,(0,3):C.GC_1121,(0,1):C.GC_873,(0,0):C.GC_874})

V_188 = Vertex(name = 'V_188',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1128})

V_189 = Vertex(name = 'V_189',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1135})

V_190 = Vertex(name = 'V_190',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF7, L.FFFF9 ],
               couplings = {(0,4):C.GC_209,(1,4):C.GC_250,(0,2):C.GC_275,(1,2):C.GC_279,(0,3):C.GC_61,(1,3):C.GC_64,(0,5):C.GC_639,(1,5):C.GC_642,(0,0):C.GC_55,(1,0):C.GC_58,(0,1):C.GC_84,(1,1):C.GC_88})

V_191 = Vertex(name = 'V_191',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF9 ],
               couplings = {(0,2):C.GC_277,(1,2):C.GC_281,(0,3):C.GC_63,(1,3):C.GC_66,(0,4):C.GC_640,(1,4):C.GC_643,(0,0):C.GC_57,(1,0):C.GC_60,(0,1):C.GC_87,(1,1):C.GC_91})

V_192 = Vertex(name = 'V_192',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF7, L.FFFF9 ],
               couplings = {(0,4):C.GC_209,(1,4):C.GC_250,(0,2):C.GC_275,(1,2):C.GC_279,(0,3):C.GC_61,(1,3):C.GC_64,(0,5):C.GC_639,(1,5):C.GC_642,(0,0):C.GC_55,(1,0):C.GC_58,(0,1):C.GC_84,(1,1):C.GC_88})

V_193 = Vertex(name = 'V_193',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF9 ],
               couplings = {(0,2):C.GC_277,(1,2):C.GC_281,(0,3):C.GC_63,(1,3):C.GC_66,(0,4):C.GC_640,(1,4):C.GC_643,(0,0):C.GC_57,(1,0):C.GC_60,(0,1):C.GC_87,(1,1):C.GC_91})

V_194 = Vertex(name = 'V_194',
               particles = [ P.d__tilde__, P.d, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,5):C.GC_194,(1,5):C.GC_241,(0,2):C.GC_276,(1,2):C.GC_280,(0,1):C.GC_92,(1,1):C.GC_111,(0,3):C.GC_637,(1,3):C.GC_638,(0,4):C.GC_399,(1,4):C.GC_400,(0,0):C.GC_276,(1,0):C.GC_280})

V_195 = Vertex(name = 'V_195',
               particles = [ P.d__tilde__, P.d, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF7 ],
               couplings = {(0,2):C.GC_207,(1,2):C.GC_248,(0,1):C.GC_278,(1,1):C.GC_282,(0,0):C.GC_277,(1,0):C.GC_281})

V_196 = Vertex(name = 'V_196',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,5):C.GC_194,(1,5):C.GC_241,(0,2):C.GC_276,(1,2):C.GC_280,(0,1):C.GC_92,(1,1):C.GC_111,(0,3):C.GC_637,(1,3):C.GC_638,(0,4):C.GC_399,(1,4):C.GC_400,(0,0):C.GC_276,(1,0):C.GC_280})

V_197 = Vertex(name = 'V_197',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF7 ],
               couplings = {(0,2):C.GC_207,(1,2):C.GC_248,(0,1):C.GC_278,(1,1):C.GC_282,(0,0):C.GC_277,(1,0):C.GC_281})

V_198 = Vertex(name = 'V_198',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_200,(0,8):C.GC_221,(1,0):C.GC_346,(3,0):C.GC_378,(0,5):C.GC_345,(2,5):C.GC_377,(1,6):C.GC_102,(3,6):C.GC_121,(1,3):C.GC_285,(3,3):C.GC_310,(1,4):C.GC_686,(3,4):C.GC_704,(1,1):C.GC_341,(3,1):C.GC_373,(0,2):C.GC_334,(2,2):C.GC_366})

V_199 = Vertex(name = 'V_199',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_205,(0,8):C.GC_234,(1,0):C.GC_362,(3,0):C.GC_394,(0,5):C.GC_361,(2,5):C.GC_393,(1,6):C.GC_109,(3,6):C.GC_128,(1,3):C.GC_300,(3,3):C.GC_325,(1,4):C.GC_693,(3,4):C.GC_711,(1,1):C.GC_358,(3,1):C.GC_390,(0,2):C.GC_349,(2,2):C.GC_381})

V_200 = Vertex(name = 'V_200',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_219})

V_201 = Vertex(name = 'V_201',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_232})

V_202 = Vertex(name = 'V_202',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_202,(0,8):C.GC_225,(1,0):C.GC_348,(3,0):C.GC_380,(0,5):C.GC_347,(2,5):C.GC_379,(1,6):C.GC_104,(3,6):C.GC_123,(1,3):C.GC_289,(3,3):C.GC_314,(1,4):C.GC_688,(3,4):C.GC_706,(1,1):C.GC_343,(3,1):C.GC_375,(0,2):C.GC_336,(2,2):C.GC_368})

V_203 = Vertex(name = 'V_203',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_206,(0,8):C.GC_237,(1,0):C.GC_364,(3,0):C.GC_396,(0,5):C.GC_363,(2,5):C.GC_395,(1,6):C.GC_110,(3,6):C.GC_129,(1,3):C.GC_302,(3,3):C.GC_327,(1,4):C.GC_694,(3,4):C.GC_712,(1,1):C.GC_360,(3,1):C.GC_392,(0,2):C.GC_351,(2,2):C.GC_383})

V_204 = Vertex(name = 'V_204',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_223})

V_205 = Vertex(name = 'V_205',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_235})

V_206 = Vertex(name = 'V_206',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_202,(0,8):C.GC_225,(1,0):C.GC_340,(3,0):C.GC_372,(0,5):C.GC_339,(2,5):C.GC_371,(1,6):C.GC_98,(3,6):C.GC_117,(1,3):C.GC_295,(3,3):C.GC_320,(1,4):C.GC_682,(3,4):C.GC_700,(1,1):C.GC_335,(3,1):C.GC_367,(0,2):C.GC_344,(2,2):C.GC_376})

V_207 = Vertex(name = 'V_207',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_206,(0,8):C.GC_237,(1,0):C.GC_356,(3,0):C.GC_388,(0,5):C.GC_355,(2,5):C.GC_387,(1,6):C.GC_107,(3,6):C.GC_126,(1,3):C.GC_305,(3,3):C.GC_330,(1,4):C.GC_691,(3,4):C.GC_709,(1,1):C.GC_352,(3,1):C.GC_384,(0,2):C.GC_359,(2,2):C.GC_391})

V_208 = Vertex(name = 'V_208',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_223})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_235})

V_210 = Vertex(name = 'V_210',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_200,(0,8):C.GC_221,(1,0):C.GC_338,(3,0):C.GC_370,(0,5):C.GC_337,(2,5):C.GC_369,(1,6):C.GC_94,(3,6):C.GC_113,(1,3):C.GC_293,(3,3):C.GC_318,(1,4):C.GC_678,(3,4):C.GC_696,(1,1):C.GC_333,(3,1):C.GC_365,(0,2):C.GC_342,(2,2):C.GC_374})

V_211 = Vertex(name = 'V_211',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_205,(0,8):C.GC_234,(1,0):C.GC_354,(3,0):C.GC_386,(0,5):C.GC_353,(2,5):C.GC_385,(1,6):C.GC_105,(3,6):C.GC_124,(1,3):C.GC_304,(3,3):C.GC_329,(1,4):C.GC_689,(3,4):C.GC_707,(1,1):C.GC_350,(3,1):C.GC_382,(0,2):C.GC_357,(2,2):C.GC_389})

V_212 = Vertex(name = 'V_212',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_219})

V_213 = Vertex(name = 'V_213',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_232})

V_214 = Vertex(name = 'V_214',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_172,(0,11):C.GC_512,(0,9):C.GC_511,(0,8):C.GC_511,(0,4):C.GC_451,(0,3):C.GC_130,(0,5):C.GC_436,(0,6):C.GC_401,(0,7):C.GC_512,(0,2):C.GC_511,(0,1):C.GC_511,(0,0):C.GC_451})

V_215 = Vertex(name = 'V_215',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF8 ],
               couplings = {(0,7):C.GC_525,(0,6):C.GC_524,(0,5):C.GC_524,(0,3):C.GC_457,(0,4):C.GC_524,(0,2):C.GC_525,(0,1):C.GC_525,(0,0):C.GC_458})

V_216 = Vertex(name = 'V_216',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_514,(0,0):C.GC_514})

V_217 = Vertex(name = 'V_217',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_526,(0,0):C.GC_523})

V_218 = Vertex(name = 'V_218',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_173,(0,11):C.GC_516,(0,9):C.GC_515,(0,8):C.GC_515,(0,4):C.GC_453,(0,3):C.GC_131,(0,5):C.GC_437,(0,6):C.GC_402,(0,7):C.GC_516,(0,2):C.GC_515,(0,1):C.GC_515,(0,0):C.GC_453})

V_219 = Vertex(name = 'V_219',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF8 ],
               couplings = {(0,7):C.GC_529,(0,6):C.GC_528,(0,5):C.GC_528,(0,3):C.GC_459,(0,4):C.GC_528,(0,2):C.GC_529,(0,1):C.GC_529,(0,0):C.GC_460})

V_220 = Vertex(name = 'V_220',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_518,(0,0):C.GC_518})

V_221 = Vertex(name = 'V_221',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_530,(0,0):C.GC_527})

V_222 = Vertex(name = 'V_222',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,10):C.GC_174,(0,11):C.GC_520,(0,9):C.GC_519,(0,8):C.GC_519,(0,4):C.GC_455,(0,3):C.GC_132,(0,5):C.GC_438,(0,6):C.GC_403,(0,7):C.GC_520,(0,2):C.GC_519,(0,1):C.GC_519,(0,0):C.GC_455})

V_223 = Vertex(name = 'V_223',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF2, L.FFFF23, L.FFFF3, L.FFFF4, L.FFFF8 ],
               couplings = {(0,7):C.GC_533,(0,6):C.GC_532,(0,5):C.GC_532,(0,3):C.GC_461,(0,4):C.GC_532,(0,2):C.GC_533,(0,1):C.GC_533,(0,0):C.GC_462})

V_224 = Vertex(name = 'V_224',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_522,(0,0):C.GC_522})

V_225 = Vertex(name = 'V_225',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_534,(0,0):C.GC_531})

V_226 = Vertex(name = 'V_226',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_151,(0,5):C.GC_511,(0,3):C.GC_512,(0,2):C.GC_512,(0,1):C.GC_452,(0,0):C.GC_10})

V_227 = Vertex(name = 'V_227',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_524,(0,3):C.GC_525,(0,2):C.GC_525,(0,1):C.GC_458,(0,0):C.GC_14})

V_228 = Vertex(name = 'V_228',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_513})

V_229 = Vertex(name = 'V_229',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_523})

V_230 = Vertex(name = 'V_230',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_152,(0,5):C.GC_515,(0,3):C.GC_516,(0,2):C.GC_516,(0,1):C.GC_454,(0,0):C.GC_11})

V_231 = Vertex(name = 'V_231',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_528,(0,3):C.GC_529,(0,2):C.GC_529,(0,1):C.GC_460,(0,0):C.GC_16})

V_232 = Vertex(name = 'V_232',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_517})

V_233 = Vertex(name = 'V_233',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_527})

V_234 = Vertex(name = 'V_234',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_153,(0,5):C.GC_519,(0,3):C.GC_520,(0,2):C.GC_520,(0,1):C.GC_456,(0,0):C.GC_12})

V_235 = Vertex(name = 'V_235',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF8 ],
               couplings = {(0,4):C.GC_532,(0,3):C.GC_533,(0,2):C.GC_533,(0,1):C.GC_462,(0,0):C.GC_18})

V_236 = Vertex(name = 'V_236',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_521})

V_237 = Vertex(name = 'V_237',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_531})

V_238 = Vertex(name = 'V_238',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF7, L.FFFF9 ],
               couplings = {(0,4):C.GC_209,(1,4):C.GC_250,(0,2):C.GC_84,(1,2):C.GC_88,(0,3):C.GC_61,(1,3):C.GC_64,(0,5):C.GC_639,(1,5):C.GC_642,(0,0):C.GC_55,(1,0):C.GC_58,(0,1):C.GC_275,(1,1):C.GC_279})

V_239 = Vertex(name = 'V_239',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF9 ],
               couplings = {(0,2):C.GC_86,(1,2):C.GC_90,(0,3):C.GC_62,(1,3):C.GC_65,(0,4):C.GC_641,(1,4):C.GC_644,(0,0):C.GC_56,(1,0):C.GC_59,(0,1):C.GC_278,(1,1):C.GC_282})

V_240 = Vertex(name = 'V_240',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF7, L.FFFF9 ],
               couplings = {(0,4):C.GC_209,(1,4):C.GC_250,(0,2):C.GC_84,(1,2):C.GC_88,(0,3):C.GC_61,(1,3):C.GC_64,(0,5):C.GC_639,(1,5):C.GC_642,(0,0):C.GC_55,(1,0):C.GC_58,(0,1):C.GC_275,(1,1):C.GC_279})

V_241 = Vertex(name = 'V_241',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF22, L.FFFF9 ],
               couplings = {(0,2):C.GC_86,(1,2):C.GC_90,(0,3):C.GC_62,(1,3):C.GC_65,(0,4):C.GC_641,(1,4):C.GC_644,(0,0):C.GC_56,(1,0):C.GC_59,(0,1):C.GC_278,(1,1):C.GC_282})

V_242 = Vertex(name = 'V_242',
               particles = [ P.b__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF21, L.FFFF7 ],
               couplings = {(0,3):C.GC_194,(1,3):C.GC_241,(0,1):C.GC_85,(1,1):C.GC_89,(0,2):C.GC_283,(1,2):C.GC_308,(0,0):C.GC_85,(1,0):C.GC_89})

V_243 = Vertex(name = 'V_243',
               particles = [ P.b__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF7 ],
               couplings = {(0,2):C.GC_207,(1,2):C.GC_248,(0,1):C.GC_87,(1,1):C.GC_91,(0,0):C.GC_86,(1,0):C.GC_90})

V_244 = Vertex(name = 'V_244',
               particles = [ P.b__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF21, L.FFFF7 ],
               couplings = {(0,3):C.GC_194,(1,3):C.GC_241,(0,1):C.GC_85,(1,1):C.GC_89,(0,2):C.GC_283,(1,2):C.GC_308,(0,0):C.GC_85,(1,0):C.GC_89})

V_245 = Vertex(name = 'V_245',
               particles = [ P.b__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF7 ],
               couplings = {(0,2):C.GC_207,(1,2):C.GC_248,(0,1):C.GC_87,(1,1):C.GC_91,(0,0):C.GC_86,(1,0):C.GC_90})

V_246 = Vertex(name = 'V_246',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_201,(0,8):C.GC_222,(1,0):C.GC_336,(3,0):C.GC_368,(0,5):C.GC_343,(2,5):C.GC_375,(1,6):C.GC_97,(3,6):C.GC_116,(1,3):C.GC_294,(3,3):C.GC_319,(1,4):C.GC_681,(3,4):C.GC_699,(1,1):C.GC_339,(3,1):C.GC_371,(0,2):C.GC_340,(2,2):C.GC_372})

V_247 = Vertex(name = 'V_247',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_206,(0,8):C.GC_237,(1,0):C.GC_352,(3,0):C.GC_384,(0,5):C.GC_359,(2,5):C.GC_391,(1,6):C.GC_107,(3,6):C.GC_126,(1,3):C.GC_305,(3,3):C.GC_330,(1,4):C.GC_691,(3,4):C.GC_709,(1,1):C.GC_356,(3,1):C.GC_388,(0,2):C.GC_355,(2,2):C.GC_387})

V_248 = Vertex(name = 'V_248',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_224})

V_249 = Vertex(name = 'V_249',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_235})

V_250 = Vertex(name = 'V_250',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_199,(0,8):C.GC_218,(1,0):C.GC_334,(3,0):C.GC_366,(0,5):C.GC_341,(2,5):C.GC_373,(1,6):C.GC_93,(3,6):C.GC_112,(1,3):C.GC_292,(3,3):C.GC_317,(1,4):C.GC_677,(3,4):C.GC_695,(1,1):C.GC_337,(3,1):C.GC_369,(0,2):C.GC_338,(2,2):C.GC_370})

V_251 = Vertex(name = 'V_251',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_205,(0,8):C.GC_234,(1,0):C.GC_350,(3,0):C.GC_382,(0,5):C.GC_357,(2,5):C.GC_389,(1,6):C.GC_105,(3,6):C.GC_124,(1,3):C.GC_304,(3,3):C.GC_329,(1,4):C.GC_689,(3,4):C.GC_707,(1,1):C.GC_354,(3,1):C.GC_386,(0,2):C.GC_353,(2,2):C.GC_385})

V_252 = Vertex(name = 'V_252',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_220})

V_253 = Vertex(name = 'V_253',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_232})

V_254 = Vertex(name = 'V_254',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_199,(0,8):C.GC_218,(1,0):C.GC_342,(3,0):C.GC_374,(0,5):C.GC_333,(2,5):C.GC_365,(1,6):C.GC_101,(3,6):C.GC_120,(1,3):C.GC_284,(3,3):C.GC_309,(1,4):C.GC_685,(3,4):C.GC_703,(1,1):C.GC_345,(3,1):C.GC_377,(0,2):C.GC_346,(2,2):C.GC_378})

V_255 = Vertex(name = 'V_255',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_205,(0,8):C.GC_234,(1,0):C.GC_358,(3,0):C.GC_390,(0,5):C.GC_349,(2,5):C.GC_381,(1,6):C.GC_109,(3,6):C.GC_128,(1,3):C.GC_300,(3,3):C.GC_325,(1,4):C.GC_693,(3,4):C.GC_711,(1,1):C.GC_362,(3,1):C.GC_394,(0,2):C.GC_361,(2,2):C.GC_393})

V_256 = Vertex(name = 'V_256',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_220})

V_257 = Vertex(name = 'V_257',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_232})

V_258 = Vertex(name = 'V_258',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_201,(0,8):C.GC_222,(1,0):C.GC_344,(3,0):C.GC_376,(0,5):C.GC_335,(2,5):C.GC_367,(1,6):C.GC_103,(3,6):C.GC_122,(1,3):C.GC_288,(3,3):C.GC_313,(1,4):C.GC_687,(3,4):C.GC_705,(1,1):C.GC_347,(3,1):C.GC_379,(0,2):C.GC_348,(2,2):C.GC_380})

V_259 = Vertex(name = 'V_259',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_206,(0,8):C.GC_237,(1,0):C.GC_360,(3,0):C.GC_392,(0,5):C.GC_351,(2,5):C.GC_383,(1,6):C.GC_110,(3,6):C.GC_129,(1,3):C.GC_302,(3,3):C.GC_327,(1,4):C.GC_694,(3,4):C.GC_712,(1,1):C.GC_364,(3,1):C.GC_396,(0,2):C.GC_363,(2,2):C.GC_395})

V_260 = Vertex(name = 'V_260',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_224})

V_261 = Vertex(name = 'V_261',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_235})

V_262 = Vertex(name = 'V_262',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,7):C.GC_193,(0,8):C.GC_240,(1,0):C.GC_268,(3,0):C.GC_272,(0,5):C.GC_267,(2,5):C.GC_271,(1,6):C.GC_82,(3,6):C.GC_83,(1,3):C.GC_265,(3,3):C.GC_266,(1,4):C.GC_397,(3,4):C.GC_398,(1,1):C.GC_268,(3,1):C.GC_272,(0,2):C.GC_267,(2,2):C.GC_271})

V_263 = Vertex(name = 'V_263',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF6 ],
               couplings = {(1,4):C.GC_238,(1,0):C.GC_270,(3,0):C.GC_274,(0,3):C.GC_269,(2,3):C.GC_273,(1,1):C.GC_269,(3,1):C.GC_273,(0,2):C.GC_270,(2,2):C.GC_274})

V_264 = Vertex(name = 'V_264',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1149})

V_265 = Vertex(name = 'V_265',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_1151})

V_266 = Vertex(name = 'V_266',
               particles = [ P.c__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1060,(0,1):C.GC_1063})

V_267 = Vertex(name = 'V_267',
               particles = [ P.c__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1066,(0,1):C.GC_1068})

V_268 = Vertex(name = 'V_268',
               particles = [ P.t__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1064,(0,1):C.GC_1059})

V_269 = Vertex(name = 'V_269',
               particles = [ P.t__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1068,(0,1):C.GC_1066})

V_270 = Vertex(name = 'V_270',
               particles = [ P.t__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1062,(0,1):C.GC_1057})

V_271 = Vertex(name = 'V_271',
               particles = [ P.t__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1067,(0,1):C.GC_1065})

V_272 = Vertex(name = 'V_272',
               particles = [ P.u__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1058,(0,1):C.GC_1061})

V_273 = Vertex(name = 'V_273',
               particles = [ P.u__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS3 ],
               couplings = {(0,0):C.GC_1065,(0,1):C.GC_1067})

V_274 = Vertex(name = 'V_274',
               particles = [ P.c__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_835,(0,1):C.GC_838})

V_275 = Vertex(name = 'V_275',
               particles = [ P.c__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_841,(0,1):C.GC_843})

V_276 = Vertex(name = 'V_276',
               particles = [ P.t__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_839,(0,1):C.GC_834})

V_277 = Vertex(name = 'V_277',
               particles = [ P.t__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_843,(0,1):C.GC_841})

V_278 = Vertex(name = 'V_278',
               particles = [ P.t__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_837,(0,1):C.GC_832})

V_279 = Vertex(name = 'V_279',
               particles = [ P.t__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_842,(0,1):C.GC_840})

V_280 = Vertex(name = 'V_280',
               particles = [ P.u__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_833,(0,1):C.GC_836})

V_281 = Vertex(name = 'V_281',
               particles = [ P.u__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS3 ],
               couplings = {(0,0):C.GC_840,(0,1):C.GC_842})

V_282 = Vertex(name = 'V_282',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_73,(0,3):C.GC_657,(0,2):C.GC_987,(0,0):C.GC_978})

V_283 = Vertex(name = 'V_283',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_79,(0,3):C.GC_662,(0,2):C.GC_994,(0,0):C.GC_981})

V_284 = Vertex(name = 'V_284',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_807,(0,0):C.GC_853,(0,1):C.GC_1072,(0,3):C.GC_1081})

V_285 = Vertex(name = 'V_285',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_813,(0,0):C.GC_858,(0,1):C.GC_1075,(0,3):C.GC_1088})

V_286 = Vertex(name = 'V_286',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_75,(0,3):C.GC_651,(0,2):C.GC_989,(0,0):C.GC_977})

V_287 = Vertex(name = 'V_287',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_80,(0,3):C.GC_659,(0,2):C.GC_995,(0,0):C.GC_980})

V_288 = Vertex(name = 'V_288',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_809,(0,0):C.GC_847,(0,1):C.GC_1071,(0,3):C.GC_1083})

V_289 = Vertex(name = 'V_289',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_814,(0,0):C.GC_855,(0,1):C.GC_1074,(0,3):C.GC_1089})

V_290 = Vertex(name = 'V_290',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_77,(0,3):C.GC_653,(0,2):C.GC_991,(0,0):C.GC_979})

V_291 = Vertex(name = 'V_291',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_81,(0,3):C.GC_660,(0,2):C.GC_996,(0,0):C.GC_981})

V_292 = Vertex(name = 'V_292',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_811,(0,0):C.GC_849,(0,1):C.GC_1073,(0,3):C.GC_1085})

V_293 = Vertex(name = 'V_293',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_815,(0,0):C.GC_856,(0,1):C.GC_1075,(0,3):C.GC_1090})

V_294 = Vertex(name = 'V_294',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_71,(0,3):C.GC_655,(0,2):C.GC_985,(0,0):C.GC_976})

V_295 = Vertex(name = 'V_295',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_78,(0,3):C.GC_661,(0,2):C.GC_993,(0,0):C.GC_980})

V_296 = Vertex(name = 'V_296',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_805,(0,0):C.GC_851,(0,1):C.GC_1070,(0,3):C.GC_1079})

V_297 = Vertex(name = 'V_297',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_812,(0,0):C.GC_857,(0,1):C.GC_1074,(0,3):C.GC_1087})

V_298 = Vertex(name = 'V_298',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_790,(0,1):C.GC_787})

V_299 = Vertex(name = 'V_299',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_796,(0,1):C.GC_794})

V_300 = Vertex(name = 'V_300',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1047,(0,0):C.GC_1044})

V_301 = Vertex(name = 'V_301',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1053,(0,0):C.GC_1051})

V_302 = Vertex(name = 'V_302',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_792,(0,1):C.GC_789})

V_303 = Vertex(name = 'V_303',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_797,(0,1):C.GC_795})

V_304 = Vertex(name = 'V_304',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1049,(0,0):C.GC_1046})

V_305 = Vertex(name = 'V_305',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1054,(0,0):C.GC_1052})

V_306 = Vertex(name = 'V_306',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_786,(0,1):C.GC_791})

V_307 = Vertex(name = 'V_307',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_794,(0,1):C.GC_796})

V_308 = Vertex(name = 'V_308',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1043,(0,0):C.GC_1048})

V_309 = Vertex(name = 'V_309',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1051,(0,0):C.GC_1053})

V_310 = Vertex(name = 'V_310',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_788,(0,1):C.GC_793})

V_311 = Vertex(name = 'V_311',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_795,(0,1):C.GC_797})

V_312 = Vertex(name = 'V_312',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1045,(0,0):C.GC_1050})

V_313 = Vertex(name = 'V_313',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_1052,(0,0):C.GC_1054})

V_314 = Vertex(name = 'V_314',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1099,(0,2):C.GC_1092,(0,1):C.GC_737,(0,3):C.GC_734})

V_315 = Vertex(name = 'V_315',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1103,(0,2):C.GC_1096,(0,1):C.GC_743,(0,3):C.GC_741})

V_316 = Vertex(name = 'V_316',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1106})

V_317 = Vertex(name = 'V_317',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1110})

V_318 = Vertex(name = 'V_318',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1129,(0,3):C.GC_1122,(0,2):C.GC_879,(0,0):C.GC_876})

V_319 = Vertex(name = 'V_319',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1133,(0,3):C.GC_1126,(0,2):C.GC_885,(0,0):C.GC_883})

V_320 = Vertex(name = 'V_320',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1136})

V_321 = Vertex(name = 'V_321',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1140})

V_322 = Vertex(name = 'V_322',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1101,(0,2):C.GC_1094,(0,1):C.GC_739,(0,3):C.GC_736})

V_323 = Vertex(name = 'V_323',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1104,(0,2):C.GC_1097,(0,1):C.GC_744,(0,3):C.GC_742})

V_324 = Vertex(name = 'V_324',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1108})

V_325 = Vertex(name = 'V_325',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1111})

V_326 = Vertex(name = 'V_326',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1131,(0,3):C.GC_1124,(0,2):C.GC_881,(0,0):C.GC_878})

V_327 = Vertex(name = 'V_327',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1134,(0,3):C.GC_1127,(0,2):C.GC_886,(0,0):C.GC_884})

V_328 = Vertex(name = 'V_328',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1138})

V_329 = Vertex(name = 'V_329',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1141})

V_330 = Vertex(name = 'V_330',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1100,(0,2):C.GC_1093,(0,1):C.GC_733,(0,3):C.GC_738})

V_331 = Vertex(name = 'V_331',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1103,(0,2):C.GC_1096,(0,1):C.GC_741,(0,3):C.GC_743})

V_332 = Vertex(name = 'V_332',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1107})

V_333 = Vertex(name = 'V_333',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1110})

V_334 = Vertex(name = 'V_334',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1130,(0,3):C.GC_1123,(0,2):C.GC_875,(0,0):C.GC_880})

V_335 = Vertex(name = 'V_335',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1133,(0,3):C.GC_1126,(0,2):C.GC_883,(0,0):C.GC_885})

V_336 = Vertex(name = 'V_336',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1137})

V_337 = Vertex(name = 'V_337',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1140})

V_338 = Vertex(name = 'V_338',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1102,(0,2):C.GC_1095,(0,1):C.GC_735,(0,3):C.GC_740})

V_339 = Vertex(name = 'V_339',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1104,(0,2):C.GC_1097,(0,1):C.GC_742,(0,3):C.GC_744})

V_340 = Vertex(name = 'V_340',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1109})

V_341 = Vertex(name = 'V_341',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1111})

V_342 = Vertex(name = 'V_342',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1132,(0,3):C.GC_1125,(0,2):C.GC_877,(0,0):C.GC_882})

V_343 = Vertex(name = 'V_343',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,1):C.GC_1134,(0,3):C.GC_1127,(0,2):C.GC_884,(0,0):C.GC_886})

V_344 = Vertex(name = 'V_344',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1139})

V_345 = Vertex(name = 'V_345',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1141})

V_346 = Vertex(name = 'V_346',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_658,(0,3):C.GC_72,(0,2):C.GC_988,(0,0):C.GC_979})

V_347 = Vertex(name = 'V_347',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_662,(0,3):C.GC_79,(0,2):C.GC_994,(0,0):C.GC_981})

V_348 = Vertex(name = 'V_348',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_656,(0,3):C.GC_70,(0,2):C.GC_986,(0,0):C.GC_977})

V_349 = Vertex(name = 'V_349',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_661,(0,3):C.GC_78,(0,2):C.GC_993,(0,0):C.GC_980})

V_350 = Vertex(name = 'V_350',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_652,(0,3):C.GC_74,(0,2):C.GC_990,(0,0):C.GC_976})

V_351 = Vertex(name = 'V_351',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_659,(0,3):C.GC_80,(0,2):C.GC_995,(0,0):C.GC_980})

V_352 = Vertex(name = 'V_352',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_654,(0,3):C.GC_76,(0,2):C.GC_992,(0,0):C.GC_978})

V_353 = Vertex(name = 'V_353',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_660,(0,3):C.GC_81,(0,2):C.GC_996,(0,0):C.GC_981})

V_354 = Vertex(name = 'V_354',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_854,(0,0):C.GC_806,(0,1):C.GC_1073,(0,3):C.GC_1082})

V_355 = Vertex(name = 'V_355',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_858,(0,0):C.GC_813,(0,1):C.GC_1075,(0,3):C.GC_1088})

V_356 = Vertex(name = 'V_356',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_852,(0,0):C.GC_804,(0,1):C.GC_1071,(0,3):C.GC_1080})

V_357 = Vertex(name = 'V_357',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_857,(0,0):C.GC_812,(0,1):C.GC_1074,(0,3):C.GC_1087})

V_358 = Vertex(name = 'V_358',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_848,(0,0):C.GC_808,(0,1):C.GC_1070,(0,3):C.GC_1084})

V_359 = Vertex(name = 'V_359',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_855,(0,0):C.GC_814,(0,1):C.GC_1074,(0,3):C.GC_1089})

V_360 = Vertex(name = 'V_360',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_850,(0,0):C.GC_810,(0,1):C.GC_1072,(0,3):C.GC_1086})

V_361 = Vertex(name = 'V_361',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,2):C.GC_856,(0,0):C.GC_815,(0,1):C.GC_1075,(0,3):C.GC_1090})

V_362 = Vertex(name = 'V_362',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_155,(0,1):C.GC_134,(0,3):C.GC_19,(0,0):C.GC_24})

V_363 = Vertex(name = 'V_363',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_166,(0,1):C.GC_145,(0,3):C.GC_43,(0,0):C.GC_45})

V_364 = Vertex(name = 'V_364',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_176})

V_365 = Vertex(name = 'V_365',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_187})

V_366 = Vertex(name = 'V_366',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF21, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_157,(0,1):C.GC_136,(0,3):C.GC_26,(0,0):C.GC_21})

V_367 = Vertex(name = 'V_367',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF21, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_167,(0,1):C.GC_146,(0,3):C.GC_46,(0,0):C.GC_44})

V_368 = Vertex(name = 'V_368',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_178})

V_369 = Vertex(name = 'V_369',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_188})

V_370 = Vertex(name = 'V_370',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_154,(0,1):C.GC_133,(0,3):C.GC_23,(0,0):C.GC_20})

V_371 = Vertex(name = 'V_371',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_166,(0,1):C.GC_145,(0,3):C.GC_45,(0,0):C.GC_43})

V_372 = Vertex(name = 'V_372',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_175})

V_373 = Vertex(name = 'V_373',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_187})

V_374 = Vertex(name = 'V_374',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_159,(0,1):C.GC_138,(0,3):C.GC_27,(0,0):C.GC_32})

V_375 = Vertex(name = 'V_375',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_168,(0,1):C.GC_147,(0,3):C.GC_47,(0,0):C.GC_49})

V_376 = Vertex(name = 'V_376',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_180})

V_377 = Vertex(name = 'V_377',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_189})

V_378 = Vertex(name = 'V_378',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF21, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_161,(0,1):C.GC_140,(0,3):C.GC_34,(0,0):C.GC_29})

V_379 = Vertex(name = 'V_379',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF21, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_169,(0,1):C.GC_148,(0,3):C.GC_50,(0,0):C.GC_48})

V_380 = Vertex(name = 'V_380',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_182})

V_381 = Vertex(name = 'V_381',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_190})

V_382 = Vertex(name = 'V_382',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_158,(0,1):C.GC_137,(0,3):C.GC_31,(0,0):C.GC_28})

V_383 = Vertex(name = 'V_383',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_168,(0,1):C.GC_147,(0,3):C.GC_49,(0,0):C.GC_47})

V_384 = Vertex(name = 'V_384',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_179})

V_385 = Vertex(name = 'V_385',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_189})

V_386 = Vertex(name = 'V_386',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_156,(0,1):C.GC_135,(0,3):C.GC_25,(0,0):C.GC_22})

V_387 = Vertex(name = 'V_387',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_167,(0,1):C.GC_146,(0,3):C.GC_46,(0,0):C.GC_44})

V_388 = Vertex(name = 'V_388',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_177})

V_389 = Vertex(name = 'V_389',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_188})

V_390 = Vertex(name = 'V_390',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_160,(0,1):C.GC_139,(0,3):C.GC_33,(0,0):C.GC_30})

V_391 = Vertex(name = 'V_391',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_169,(0,1):C.GC_148,(0,3):C.GC_50,(0,0):C.GC_48})

V_392 = Vertex(name = 'V_392',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_181})

V_393 = Vertex(name = 'V_393',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_190})

V_394 = Vertex(name = 'V_394',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_163,(0,1):C.GC_142,(0,3):C.GC_35,(0,0):C.GC_40})

V_395 = Vertex(name = 'V_395',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_170,(0,1):C.GC_149,(0,3):C.GC_51,(0,0):C.GC_53})

V_396 = Vertex(name = 'V_396',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_184})

V_397 = Vertex(name = 'V_397',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_191})

V_398 = Vertex(name = 'V_398',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_165,(0,1):C.GC_144,(0,3):C.GC_37,(0,0):C.GC_42})

V_399 = Vertex(name = 'V_399',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_171,(0,1):C.GC_150,(0,3):C.GC_52,(0,0):C.GC_54})

V_400 = Vertex(name = 'V_400',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_186})

V_401 = Vertex(name = 'V_401',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_192})

V_402 = Vertex(name = 'V_402',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_162,(0,1):C.GC_141,(0,3):C.GC_39,(0,0):C.GC_36})

V_403 = Vertex(name = 'V_403',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_170,(0,1):C.GC_149,(0,3):C.GC_53,(0,0):C.GC_51})

V_404 = Vertex(name = 'V_404',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_183})

V_405 = Vertex(name = 'V_405',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_191})

V_406 = Vertex(name = 'V_406',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_164,(0,1):C.GC_143,(0,3):C.GC_41,(0,0):C.GC_38})

V_407 = Vertex(name = 'V_407',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_171,(0,1):C.GC_150,(0,3):C.GC_54,(0,0):C.GC_52})

V_408 = Vertex(name = 'V_408',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_185})

V_409 = Vertex(name = 'V_409',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_192})

V_410 = Vertex(name = 'V_410',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_151,(0,1):C.GC_130,(0,3):C.GC_10,(0,0):C.GC_10})

V_411 = Vertex(name = 'V_411',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_172,(0,2):C.GC_13,(0,0):C.GC_14})

V_412 = Vertex(name = 'V_412',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_152,(0,1):C.GC_131,(0,3):C.GC_11,(0,0):C.GC_11})

V_413 = Vertex(name = 'V_413',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_173,(0,2):C.GC_15,(0,0):C.GC_16})

V_414 = Vertex(name = 'V_414',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_153,(0,1):C.GC_132,(0,3):C.GC_12,(0,0):C.GC_12})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_174,(0,2):C.GC_17,(0,0):C.GC_18})

V_416 = Vertex(name = 'V_416',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7, L.FFFF9 ],
               couplings = {(0,4):C.GC_194,(1,4):C.GC_241,(0,1):C.GC_637,(1,1):C.GC_638,(0,2):C.GC_283,(1,2):C.GC_308,(0,3):C.GC_646,(1,3):C.GC_647,(0,5):C.GC_639,(1,5):C.GC_642,(0,0):C.GC_639,(1,0):C.GC_642})

V_417 = Vertex(name = 'V_417',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_208,(1,1):C.GC_249,(0,2):C.GC_641,(1,2):C.GC_644,(0,0):C.GC_640,(1,0):C.GC_643})

V_418 = Vertex(name = 'V_418',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7, L.FFFF9 ],
               couplings = {(0,4):C.GC_194,(1,4):C.GC_241,(0,1):C.GC_283,(1,1):C.GC_308,(0,2):C.GC_637,(1,2):C.GC_638,(0,3):C.GC_646,(1,3):C.GC_647,(0,5):C.GC_639,(1,5):C.GC_642,(0,0):C.GC_639,(1,0):C.GC_642})

V_419 = Vertex(name = 'V_419',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_208,(1,1):C.GC_249,(0,2):C.GC_640,(1,2):C.GC_643,(0,0):C.GC_641,(1,0):C.GC_644})

V_420 = Vertex(name = 'V_420',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_194,(1,2):C.GC_241,(0,1):C.GC_92,(1,1):C.GC_111,(0,3):C.GC_55,(1,3):C.GC_58,(0,0):C.GC_55,(1,0):C.GC_58})

V_421 = Vertex(name = 'V_421',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_208,(1,1):C.GC_249,(0,2):C.GC_56,(1,2):C.GC_59,(0,0):C.GC_57,(1,0):C.GC_60})

V_422 = Vertex(name = 'V_422',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF15, L.FFFF7, L.FFFF9 ],
               couplings = {(0,2):C.GC_194,(1,2):C.GC_241,(0,1):C.GC_92,(1,1):C.GC_111,(0,3):C.GC_55,(1,3):C.GC_58,(0,0):C.GC_55,(1,0):C.GC_58})

V_423 = Vertex(name = 'V_423',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_208,(1,1):C.GC_249,(0,2):C.GC_56,(1,2):C.GC_59,(0,0):C.GC_57,(1,0):C.GC_60})

V_424 = Vertex(name = 'V_424',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_156,(0,4):C.GC_549,(0,3):C.GC_548,(0,0):C.GC_25,(0,2):C.GC_548,(0,1):C.GC_469})

V_425 = Vertex(name = 'V_425',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_167,(0,4):C.GC_595,(0,3):C.GC_596,(0,0):C.GC_46,(0,2):C.GC_596,(0,1):C.GC_494})

V_426 = Vertex(name = 'V_426',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_550})

V_427 = Vertex(name = 'V_427',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_597})

V_428 = Vertex(name = 'V_428',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_151,(0,4):C.GC_511,(0,3):C.GC_512,(0,0):C.GC_10,(0,2):C.GC_512,(0,1):C.GC_452})

V_429 = Vertex(name = 'V_429',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23 ],
               couplings = {(0,4):C.GC_525,(0,3):C.GC_524,(0,0):C.GC_13,(0,2):C.GC_524,(0,1):C.GC_457})

V_430 = Vertex(name = 'V_430',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_513})

V_431 = Vertex(name = 'V_431',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_526})

V_432 = Vertex(name = 'V_432',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_154,(0,4):C.GC_545,(0,3):C.GC_544,(0,0):C.GC_23,(0,2):C.GC_544,(0,1):C.GC_467})

V_433 = Vertex(name = 'V_433',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_166,(0,4):C.GC_591,(0,3):C.GC_592,(0,0):C.GC_45,(0,2):C.GC_592,(0,1):C.GC_492})

V_434 = Vertex(name = 'V_434',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_546})

V_435 = Vertex(name = 'V_435',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_593})

V_436 = Vertex(name = 'V_436',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_155,(0,4):C.GC_537,(0,3):C.GC_536,(0,0):C.GC_19,(0,2):C.GC_536,(0,1):C.GC_463})

V_437 = Vertex(name = 'V_437',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_166,(0,4):C.GC_583,(0,3):C.GC_584,(0,0):C.GC_43,(0,2):C.GC_584,(0,1):C.GC_488})

V_438 = Vertex(name = 'V_438',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_538})

V_439 = Vertex(name = 'V_439',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_585})

V_440 = Vertex(name = 'V_440',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_157,(0,4):C.GC_541,(0,3):C.GC_540,(0,0):C.GC_21,(0,2):C.GC_540,(0,1):C.GC_465})

V_441 = Vertex(name = 'V_441',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_167,(0,4):C.GC_587,(0,3):C.GC_588,(0,0):C.GC_44,(0,2):C.GC_588,(0,1):C.GC_490})

V_442 = Vertex(name = 'V_442',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_542})

V_443 = Vertex(name = 'V_443',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_589})

V_444 = Vertex(name = 'V_444',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_160,(0,4):C.GC_565,(0,3):C.GC_564,(0,0):C.GC_33,(0,2):C.GC_564,(0,1):C.GC_477})

V_445 = Vertex(name = 'V_445',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_169,(0,4):C.GC_611,(0,3):C.GC_612,(0,0):C.GC_50,(0,2):C.GC_612,(0,1):C.GC_502})

V_446 = Vertex(name = 'V_446',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_566})

V_447 = Vertex(name = 'V_447',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_613})

V_448 = Vertex(name = 'V_448',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_152,(0,4):C.GC_515,(0,3):C.GC_516,(0,0):C.GC_11,(0,2):C.GC_516,(0,1):C.GC_454})

V_449 = Vertex(name = 'V_449',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23 ],
               couplings = {(0,4):C.GC_529,(0,3):C.GC_528,(0,0):C.GC_15,(0,2):C.GC_528,(0,1):C.GC_459})

V_450 = Vertex(name = 'V_450',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_517})

V_451 = Vertex(name = 'V_451',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_530})

V_452 = Vertex(name = 'V_452',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_158,(0,4):C.GC_561,(0,3):C.GC_560,(0,0):C.GC_31,(0,2):C.GC_560,(0,1):C.GC_475})

V_453 = Vertex(name = 'V_453',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_168,(0,4):C.GC_607,(0,3):C.GC_608,(0,0):C.GC_49,(0,2):C.GC_608,(0,1):C.GC_500})

V_454 = Vertex(name = 'V_454',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_562})

V_455 = Vertex(name = 'V_455',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_609})

V_456 = Vertex(name = 'V_456',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_159,(0,4):C.GC_553,(0,3):C.GC_552,(0,0):C.GC_27,(0,2):C.GC_552,(0,1):C.GC_471})

V_457 = Vertex(name = 'V_457',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_168,(0,4):C.GC_599,(0,3):C.GC_600,(0,0):C.GC_47,(0,2):C.GC_600,(0,1):C.GC_496})

V_458 = Vertex(name = 'V_458',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_554})

V_459 = Vertex(name = 'V_459',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_601})

V_460 = Vertex(name = 'V_460',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_161,(0,4):C.GC_557,(0,3):C.GC_556,(0,0):C.GC_29,(0,2):C.GC_556,(0,1):C.GC_473})

V_461 = Vertex(name = 'V_461',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_169,(0,4):C.GC_603,(0,3):C.GC_604,(0,0):C.GC_48,(0,2):C.GC_604,(0,1):C.GC_498})

V_462 = Vertex(name = 'V_462',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_558})

V_463 = Vertex(name = 'V_463',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_605})

V_464 = Vertex(name = 'V_464',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_164,(0,4):C.GC_581,(0,3):C.GC_580,(0,0):C.GC_41,(0,2):C.GC_580,(0,1):C.GC_485})

V_465 = Vertex(name = 'V_465',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_171,(0,4):C.GC_627,(0,3):C.GC_628,(0,0):C.GC_54,(0,2):C.GC_628,(0,1):C.GC_510})

V_466 = Vertex(name = 'V_466',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_582})

V_467 = Vertex(name = 'V_467',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_629})

V_468 = Vertex(name = 'V_468',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_153,(0,4):C.GC_519,(0,3):C.GC_520,(0,0):C.GC_12,(0,2):C.GC_520,(0,1):C.GC_456})

V_469 = Vertex(name = 'V_469',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23 ],
               couplings = {(0,4):C.GC_533,(0,3):C.GC_532,(0,0):C.GC_17,(0,2):C.GC_532,(0,1):C.GC_461})

V_470 = Vertex(name = 'V_470',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_521})

V_471 = Vertex(name = 'V_471',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_534})

V_472 = Vertex(name = 'V_472',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF17, L.FFFF23, L.FFFF7 ],
               couplings = {(0,6):C.GC_162,(0,5):C.GC_577,(0,3):C.GC_576,(0,0):C.GC_39,(0,2):C.GC_576,(0,4):C.GC_624,(0,1):C.GC_483})

V_473 = Vertex(name = 'V_473',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,4):C.GC_170,(0,3):C.GC_623,(0,2):C.GC_624,(0,0):C.GC_53,(0,1):C.GC_508})

V_474 = Vertex(name = 'V_474',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_578})

V_475 = Vertex(name = 'V_475',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_625})

V_476 = Vertex(name = 'V_476',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_163,(0,4):C.GC_569,(0,3):C.GC_568,(0,0):C.GC_35,(0,2):C.GC_568,(0,1):C.GC_479})

V_477 = Vertex(name = 'V_477',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_170,(0,4):C.GC_615,(0,3):C.GC_616,(0,0):C.GC_51,(0,2):C.GC_616,(0,1):C.GC_504})

V_478 = Vertex(name = 'V_478',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_570})

V_479 = Vertex(name = 'V_479',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_617})

V_480 = Vertex(name = 'V_480',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_165,(0,4):C.GC_573,(0,3):C.GC_572,(0,0):C.GC_37,(0,2):C.GC_572,(0,1):C.GC_481})

V_481 = Vertex(name = 'V_481',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF23, L.FFFF7 ],
               couplings = {(0,5):C.GC_171,(0,4):C.GC_619,(0,3):C.GC_620,(0,0):C.GC_52,(0,2):C.GC_620,(0,1):C.GC_506})

V_482 = Vertex(name = 'V_482',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_574})

V_483 = Vertex(name = 'V_483',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12 ],
               couplings = {(0,0):C.GC_621})

V_484 = Vertex(name = 'V_484',
               particles = [ P.t__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_431,(0,1):C.GC_426})

V_485 = Vertex(name = 'V_485',
               particles = [ P.t__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_435,(0,1):C.GC_433})

V_486 = Vertex(name = 'V_486',
               particles = [ P.t__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_825,(0,0):C.GC_820})

V_487 = Vertex(name = 'V_487',
               particles = [ P.t__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_829,(0,0):C.GC_827})

V_488 = Vertex(name = 'V_488',
               particles = [ P.c__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6, L.FFVS8 ],
               couplings = {(0,2):C.GC_430,(0,1):C.GC_435,(0,0):C.GC_427})

V_489 = Vertex(name = 'V_489',
               particles = [ P.c__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_433})

V_490 = Vertex(name = 'V_490',
               particles = [ P.c__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_821,(0,0):C.GC_824})

V_491 = Vertex(name = 'V_491',
               particles = [ P.c__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_827,(0,0):C.GC_829})

V_492 = Vertex(name = 'V_492',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS5, L.FFVS7 ],
               couplings = {(0,1):C.GC_422,(0,0):C.GC_423})

V_493 = Vertex(name = 'V_493',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10, L.FFV12, L.FFV7 ],
               couplings = {(0,2):C.GC_7,(0,1):C.GC_816,(0,0):C.GC_817})

V_494 = Vertex(name = 'V_494',
               particles = [ P.u__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_425,(0,1):C.GC_428})

V_495 = Vertex(name = 'V_495',
               particles = [ P.u__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_432,(0,1):C.GC_434})

V_496 = Vertex(name = 'V_496',
               particles = [ P.u__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_819,(0,0):C.GC_822})

V_497 = Vertex(name = 'V_497',
               particles = [ P.u__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_826,(0,0):C.GC_828})

V_498 = Vertex(name = 'V_498',
               particles = [ P.t__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_429,(0,1):C.GC_424})

V_499 = Vertex(name = 'V_499',
               particles = [ P.t__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_434,(0,1):C.GC_432})

V_500 = Vertex(name = 'V_500',
               particles = [ P.t__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_823,(0,0):C.GC_818})

V_501 = Vertex(name = 'V_501',
               particles = [ P.t__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV11, L.FFV3 ],
               couplings = {(0,1):C.GC_828,(0,0):C.GC_826})

V_502 = Vertex(name = 'V_502',
               particles = [ P.t__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_926,(0,1):C.GC_921})

V_503 = Vertex(name = 'V_503',
               particles = [ P.t__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_930,(0,1):C.GC_928})

V_504 = Vertex(name = 'V_504',
               particles = [ P.c__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_922,(0,1):C.GC_925})

V_505 = Vertex(name = 'V_505',
               particles = [ P.c__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_928,(0,1):C.GC_930})

V_506 = Vertex(name = 'V_506',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,1):C.GC_917,(0,0):C.GC_918})

V_507 = Vertex(name = 'V_507',
               particles = [ P.u__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_920,(0,1):C.GC_923})

V_508 = Vertex(name = 'V_508',
               particles = [ P.u__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_927,(0,1):C.GC_929})

V_509 = Vertex(name = 'V_509',
               particles = [ P.t__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_924,(0,1):C.GC_919})

V_510 = Vertex(name = 'V_510',
               particles = [ P.t__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_929,(0,1):C.GC_927})

V_511 = Vertex(name = 'V_511',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_4})

V_512 = Vertex(name = 'V_512',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_746})

V_513 = Vertex(name = 'V_513',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_932})

V_514 = Vertex(name = 'V_514',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_5})

V_515 = Vertex(name = 'V_515',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_752})

V_516 = Vertex(name = 'V_516',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_747})

V_517 = Vertex(name = 'V_517',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_753})

V_518 = Vertex(name = 'V_518',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_799})

V_519 = Vertex(name = 'V_519',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_1120})

V_520 = Vertex(name = 'V_520',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_745})

V_521 = Vertex(name = 'V_521',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_157,(0,0):C.GC_442})

V_522 = Vertex(name = 'V_522',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_167,(0,0):C.GC_632})

V_523 = Vertex(name = 'V_523',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_178})

V_524 = Vertex(name = 'V_524',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_188})

V_525 = Vertex(name = 'V_525',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_155,(0,0):C.GC_440})

V_526 = Vertex(name = 'V_526',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_166,(0,0):C.GC_631})

V_527 = Vertex(name = 'V_527',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_176})

V_528 = Vertex(name = 'V_528',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_187})

V_529 = Vertex(name = 'V_529',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_161,(0,0):C.GC_446})

V_530 = Vertex(name = 'V_530',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_169,(0,0):C.GC_634})

V_531 = Vertex(name = 'V_531',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_182})

V_532 = Vertex(name = 'V_532',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_190})

V_533 = Vertex(name = 'V_533',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_159,(0,0):C.GC_444})

V_534 = Vertex(name = 'V_534',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_168,(0,0):C.GC_633})

V_535 = Vertex(name = 'V_535',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_180})

V_536 = Vertex(name = 'V_536',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_189})

V_537 = Vertex(name = 'V_537',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_165,(0,0):C.GC_450})

V_538 = Vertex(name = 'V_538',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_171,(0,0):C.GC_636})

V_539 = Vertex(name = 'V_539',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_186})

V_540 = Vertex(name = 'V_540',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_192})

V_541 = Vertex(name = 'V_541',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_163,(0,0):C.GC_448})

V_542 = Vertex(name = 'V_542',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_170,(0,0):C.GC_635})

V_543 = Vertex(name = 'V_543',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_184})

V_544 = Vertex(name = 'V_544',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_191})

V_545 = Vertex(name = 'V_545',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_176})

V_546 = Vertex(name = 'V_546',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_187})

V_547 = Vertex(name = 'V_547',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_178})

V_548 = Vertex(name = 'V_548',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_188})

V_549 = Vertex(name = 'V_549',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_180})

V_550 = Vertex(name = 'V_550',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_189})

V_551 = Vertex(name = 'V_551',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_182})

V_552 = Vertex(name = 'V_552',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_190})

V_553 = Vertex(name = 'V_553',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_184})

V_554 = Vertex(name = 'V_554',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_191})

V_555 = Vertex(name = 'V_555',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_186})

V_556 = Vertex(name = 'V_556',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_192})

V_557 = Vertex(name = 'V_557',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_202,(0,7):C.GC_202,(0,0):C.GC_295,(2,0):C.GC_320,(1,3):C.GC_295,(3,3):C.GC_320,(1,1):C.GC_289,(3,1):C.GC_314,(1,2):C.GC_720,(0,4):C.GC_289,(2,4):C.GC_314,(0,5):C.GC_720})

V_558 = Vertex(name = 'V_558',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_206,(0,7):C.GC_206,(0,0):C.GC_305,(2,0):C.GC_330,(1,3):C.GC_305,(3,3):C.GC_330,(1,1):C.GC_302,(3,1):C.GC_327,(1,2):C.GC_724,(0,4):C.GC_302,(2,4):C.GC_327,(0,5):C.GC_724})

V_559 = Vertex(name = 'V_559',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_224,(0,1):C.GC_224})

V_560 = Vertex(name = 'V_560',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_236,(0,1):C.GC_236})

V_561 = Vertex(name = 'V_561',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_200,(0,7):C.GC_200,(0,0):C.GC_285,(2,0):C.GC_310,(1,3):C.GC_285,(3,3):C.GC_310,(1,1):C.GC_293,(3,1):C.GC_318,(1,2):C.GC_718,(0,4):C.GC_293,(2,4):C.GC_318,(0,5):C.GC_718})

V_562 = Vertex(name = 'V_562',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_205,(0,7):C.GC_205,(0,0):C.GC_300,(2,0):C.GC_325,(1,3):C.GC_300,(3,3):C.GC_325,(1,1):C.GC_304,(3,1):C.GC_329,(1,2):C.GC_723,(0,4):C.GC_304,(2,4):C.GC_329,(0,5):C.GC_723})

V_563 = Vertex(name = 'V_563',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_220,(0,1):C.GC_220})

V_564 = Vertex(name = 'V_564',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_233,(0,1):C.GC_233})

V_565 = Vertex(name = 'V_565',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_200,(0,5):C.GC_200,(0,0):C.GC_94,(2,0):C.GC_113,(1,2):C.GC_94,(3,2):C.GC_113,(1,1):C.GC_102,(3,1):C.GC_121,(0,3):C.GC_102,(2,3):C.GC_121})

V_566 = Vertex(name = 'V_566',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_205,(0,5):C.GC_205,(0,0):C.GC_105,(2,0):C.GC_124,(1,2):C.GC_105,(3,2):C.GC_124,(1,1):C.GC_109,(3,1):C.GC_128,(0,3):C.GC_109,(2,3):C.GC_128})

V_567 = Vertex(name = 'V_567',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_220,(0,1):C.GC_220})

V_568 = Vertex(name = 'V_568',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_233,(0,1):C.GC_233})

V_569 = Vertex(name = 'V_569',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_202,(0,5):C.GC_202,(0,0):C.GC_98,(2,0):C.GC_117,(1,2):C.GC_98,(3,2):C.GC_117,(1,1):C.GC_104,(3,1):C.GC_123,(0,3):C.GC_104,(2,3):C.GC_123})

V_570 = Vertex(name = 'V_570',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_206,(0,5):C.GC_206,(0,0):C.GC_107,(2,0):C.GC_126,(1,2):C.GC_107,(3,2):C.GC_126,(1,1):C.GC_110,(3,1):C.GC_129,(0,3):C.GC_110,(2,3):C.GC_129})

V_571 = Vertex(name = 'V_571',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_224,(0,1):C.GC_224})

V_572 = Vertex(name = 'V_572',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_236,(0,1):C.GC_236})

V_573 = Vertex(name = 'V_573',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_198,(3,6):C.GC_245,(0,7):C.GC_198,(2,7):C.GC_245,(0,0):C.GC_299,(2,0):C.GC_324,(1,3):C.GC_291,(3,3):C.GC_316,(1,1):C.GC_299,(3,1):C.GC_324,(1,2):C.GC_716,(3,2):C.GC_728,(0,4):C.GC_291,(2,4):C.GC_316,(0,5):C.GC_716,(2,5):C.GC_728})

V_574 = Vertex(name = 'V_574',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_204,(3,6):C.GC_247,(0,7):C.GC_204,(2,7):C.GC_247,(0,0):C.GC_307,(2,0):C.GC_332,(1,3):C.GC_303,(3,3):C.GC_328,(1,1):C.GC_307,(3,1):C.GC_332,(1,2):C.GC_722,(3,2):C.GC_730,(0,4):C.GC_303,(2,4):C.GC_328,(0,5):C.GC_722,(2,5):C.GC_730})

V_575 = Vertex(name = 'V_575',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_216,(3,0):C.GC_257,(0,1):C.GC_216,(2,1):C.GC_257})

V_576 = Vertex(name = 'V_576',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_230,(3,0):C.GC_263,(0,1):C.GC_230,(2,1):C.GC_263})

V_577 = Vertex(name = 'V_577',
               particles = [ P.c__tilde__, P.c, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_196,(1,3):C.GC_243,(0,0):C.GC_287,(1,0):C.GC_312,(0,1):C.GC_297,(1,1):C.GC_322,(0,2):C.GC_714,(1,2):C.GC_726})

V_578 = Vertex(name = 'V_578',
               particles = [ P.c__tilde__, P.c, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_203,(1,3):C.GC_246,(0,0):C.GC_301,(1,0):C.GC_326,(0,1):C.GC_306,(1,1):C.GC_331,(0,2):C.GC_721,(1,2):C.GC_729})

V_579 = Vertex(name = 'V_579',
               particles = [ P.c__tilde__, P.c, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_212,(1,0):C.GC_253})

V_580 = Vertex(name = 'V_580',
               particles = [ P.c__tilde__, P.c, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_227,(1,0):C.GC_260})

V_581 = Vertex(name = 'V_581',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_198,(1,3):C.GC_245,(0,0):C.GC_299,(1,0):C.GC_324,(0,1):C.GC_291,(1,1):C.GC_316,(0,2):C.GC_716,(1,2):C.GC_728})

V_582 = Vertex(name = 'V_582',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_204,(1,3):C.GC_247,(0,0):C.GC_307,(1,0):C.GC_332,(0,1):C.GC_303,(1,1):C.GC_328,(0,2):C.GC_722,(1,2):C.GC_730})

V_583 = Vertex(name = 'V_583',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_216,(1,0):C.GC_257})

V_584 = Vertex(name = 'V_584',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_230,(1,0):C.GC_263})

V_585 = Vertex(name = 'V_585',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_196,(3,6):C.GC_243,(0,7):C.GC_196,(2,7):C.GC_243,(0,0):C.GC_287,(2,0):C.GC_312,(1,3):C.GC_297,(3,3):C.GC_322,(1,1):C.GC_287,(3,1):C.GC_312,(1,2):C.GC_714,(3,2):C.GC_726,(0,4):C.GC_297,(2,4):C.GC_322,(0,5):C.GC_714,(2,5):C.GC_726})

V_586 = Vertex(name = 'V_586',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_203,(3,6):C.GC_246,(0,7):C.GC_203,(2,7):C.GC_246,(0,0):C.GC_301,(2,0):C.GC_326,(1,3):C.GC_306,(3,3):C.GC_331,(1,1):C.GC_301,(3,1):C.GC_326,(1,2):C.GC_721,(3,2):C.GC_729,(0,4):C.GC_306,(2,4):C.GC_331,(0,5):C.GC_721,(2,5):C.GC_729})

V_587 = Vertex(name = 'V_587',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_212,(3,0):C.GC_253,(0,1):C.GC_212,(2,1):C.GC_253})

V_588 = Vertex(name = 'V_588',
               particles = [ P.u__tilde__, P.u, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_227,(3,0):C.GC_260,(0,1):C.GC_227,(2,1):C.GC_260})

V_589 = Vertex(name = 'V_589',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_196,(1,1):C.GC_243,(0,0):C.GC_287,(1,0):C.GC_312})

V_590 = Vertex(name = 'V_590',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_203,(1,1):C.GC_246,(0,0):C.GC_301,(1,0):C.GC_326})

V_591 = Vertex(name = 'V_591',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_211,(1,0):C.GC_252})

V_592 = Vertex(name = 'V_592',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_593 = Vertex(name = 'V_593',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_217,(3,1):C.GC_258,(0,2):C.GC_198,(2,2):C.GC_245,(0,0):C.GC_291,(2,0):C.GC_316})

V_594 = Vertex(name = 'V_594',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_231,(3,1):C.GC_264,(0,2):C.GC_204,(2,2):C.GC_247,(0,0):C.GC_303,(2,0):C.GC_328})

V_595 = Vertex(name = 'V_595',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_215,(1,0):C.GC_256})

V_596 = Vertex(name = 'V_596',
               particles = [ P.c__tilde__, P.c, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_597 = Vertex(name = 'V_597',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_196,(3,1):C.GC_243,(0,2):C.GC_213,(2,2):C.GC_254,(1,0):C.GC_287,(3,0):C.GC_312})

V_598 = Vertex(name = 'V_598',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_203,(3,1):C.GC_246,(0,2):C.GC_228,(2,2):C.GC_261,(1,0):C.GC_301,(3,0):C.GC_326})

V_599 = Vertex(name = 'V_599',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_211,(1,0):C.GC_252})

V_600 = Vertex(name = 'V_600',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_601 = Vertex(name = 'V_601',
               particles = [ P.b__tilde__, P.s, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_198,(1,1):C.GC_245,(0,0):C.GC_291,(1,0):C.GC_316})

V_602 = Vertex(name = 'V_602',
               particles = [ P.b__tilde__, P.s, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_204,(1,1):C.GC_247,(0,0):C.GC_303,(1,0):C.GC_328})

V_603 = Vertex(name = 'V_603',
               particles = [ P.b__tilde__, P.s, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_215,(1,0):C.GC_256})

V_604 = Vertex(name = 'V_604',
               particles = [ P.b__tilde__, P.s, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_605 = Vertex(name = 'V_605',
               particles = [ P.t__tilde__, P.c, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,4):C.GC_198,(1,4):C.GC_245,(0,0):C.GC_299,(1,0):C.GC_324,(0,2):C.GC_100,(1,2):C.GC_119,(0,3):C.GC_684,(1,3):C.GC_702,(1,1):C.GC_710})

V_606 = Vertex(name = 'V_606',
               particles = [ P.t__tilde__, P.c, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_204,(1,3):C.GC_247,(0,0):C.GC_307,(1,0):C.GC_332,(0,1):C.GC_108,(1,1):C.GC_127,(0,2):C.GC_692})

V_607 = Vertex(name = 'V_607',
               particles = [ P.t__tilde__, P.c, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_215,(1,0):C.GC_256})

V_608 = Vertex(name = 'V_608',
               particles = [ P.t__tilde__, P.c, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_609 = Vertex(name = 'V_609',
               particles = [ P.t__tilde__, P.c, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_217,(3,3):C.GC_258,(0,4):C.GC_198,(2,4):C.GC_245,(0,0):C.GC_299,(2,0):C.GC_324,(0,1):C.GC_100,(2,1):C.GC_119,(0,2):C.GC_684,(2,2):C.GC_702})

V_610 = Vertex(name = 'V_610',
               particles = [ P.t__tilde__, P.c, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_231,(3,3):C.GC_264,(0,4):C.GC_204,(2,4):C.GC_247,(0,0):C.GC_307,(2,0):C.GC_332,(0,1):C.GC_108,(2,1):C.GC_127,(0,2):C.GC_692,(2,2):C.GC_710})

V_611 = Vertex(name = 'V_611',
               particles = [ P.t__tilde__, P.c, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_215,(1,0):C.GC_256})

V_612 = Vertex(name = 'V_612',
               particles = [ P.t__tilde__, P.c, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_613 = Vertex(name = 'V_613',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_196,(3,3):C.GC_243,(0,4):C.GC_213,(2,4):C.GC_254,(1,2):C.GC_96,(3,2):C.GC_115,(1,0):C.GC_297,(3,0):C.GC_322,(1,1):C.GC_680,(3,1):C.GC_698})

V_614 = Vertex(name = 'V_614',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_203,(3,3):C.GC_246,(0,4):C.GC_228,(2,4):C.GC_261,(1,2):C.GC_106,(3,2):C.GC_125,(1,0):C.GC_306,(3,0):C.GC_331,(1,1):C.GC_690,(3,1):C.GC_708})

V_615 = Vertex(name = 'V_615',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_211,(1,0):C.GC_252})

V_616 = Vertex(name = 'V_616',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_617 = Vertex(name = 'V_617',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_196,(1,3):C.GC_243,(0,0):C.GC_96,(1,0):C.GC_115,(0,1):C.GC_297,(1,1):C.GC_322,(0,2):C.GC_680,(1,2):C.GC_698})

V_618 = Vertex(name = 'V_618',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_203,(1,3):C.GC_246,(0,0):C.GC_106,(1,0):C.GC_125,(0,1):C.GC_306,(1,1):C.GC_331,(0,2):C.GC_690,(1,2):C.GC_708})

V_619 = Vertex(name = 'V_619',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_211,(1,0):C.GC_252})

V_620 = Vertex(name = 'V_620',
               particles = [ P.s__tilde__, P.s, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_621 = Vertex(name = 'V_621',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_196,(3,2):C.GC_243,(0,3):C.GC_196,(2,3):C.GC_243,(0,0):C.GC_96,(2,0):C.GC_115,(1,1):C.GC_96,(3,1):C.GC_115})

V_622 = Vertex(name = 'V_622',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_203,(3,2):C.GC_246,(0,3):C.GC_203,(2,3):C.GC_246,(0,0):C.GC_106,(2,0):C.GC_125,(1,1):C.GC_106,(3,1):C.GC_125})

V_623 = Vertex(name = 'V_623',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_212,(3,0):C.GC_253,(0,1):C.GC_212,(2,1):C.GC_253})

V_624 = Vertex(name = 'V_624',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_227,(3,0):C.GC_260,(0,1):C.GC_227,(2,1):C.GC_260})

V_625 = Vertex(name = 'V_625',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_198,(1,1):C.GC_245,(0,0):C.GC_100,(1,0):C.GC_119})

V_626 = Vertex(name = 'V_626',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_204,(1,1):C.GC_247,(0,0):C.GC_108,(1,0):C.GC_127})

V_627 = Vertex(name = 'V_627',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_216,(1,0):C.GC_257})

V_628 = Vertex(name = 'V_628',
               particles = [ P.d__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_230,(1,0):C.GC_263})

V_629 = Vertex(name = 'V_629',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_196,(1,1):C.GC_243,(0,0):C.GC_96,(1,0):C.GC_115})

V_630 = Vertex(name = 'V_630',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_203,(1,1):C.GC_246,(0,0):C.GC_106,(1,0):C.GC_125})

V_631 = Vertex(name = 'V_631',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_212,(1,0):C.GC_253})

V_632 = Vertex(name = 'V_632',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_227,(1,0):C.GC_260})

V_633 = Vertex(name = 'V_633',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_198,(3,2):C.GC_245,(0,3):C.GC_198,(2,3):C.GC_245,(0,0):C.GC_100,(2,0):C.GC_119,(1,1):C.GC_100,(3,1):C.GC_119})

V_634 = Vertex(name = 'V_634',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_204,(3,2):C.GC_247,(0,3):C.GC_204,(2,3):C.GC_247,(0,0):C.GC_108,(2,0):C.GC_127,(1,1):C.GC_108,(3,1):C.GC_127})

V_635 = Vertex(name = 'V_635',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_216,(3,0):C.GC_257,(0,1):C.GC_216,(2,1):C.GC_257})

V_636 = Vertex(name = 'V_636',
               particles = [ P.s__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_230,(3,0):C.GC_263,(0,1):C.GC_230,(2,1):C.GC_263})

V_637 = Vertex(name = 'V_637',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_213,(1,0):C.GC_254})

V_638 = Vertex(name = 'V_638',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_228,(1,0):C.GC_261})

V_639 = Vertex(name = 'V_639',
               particles = [ P.b__tilde__, P.c, P.u__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_217,(1,0):C.GC_258})

V_640 = Vertex(name = 'V_640',
               particles = [ P.b__tilde__, P.c, P.u__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_231,(1,0):C.GC_264})

V_641 = Vertex(name = 'V_641',
               particles = [ P.s__tilde__, P.c, P.t__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_213,(1,0):C.GC_254})

V_642 = Vertex(name = 'V_642',
               particles = [ P.s__tilde__, P.c, P.t__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_228,(1,0):C.GC_261})

V_643 = Vertex(name = 'V_643',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_217,(1,0):C.GC_258})

V_644 = Vertex(name = 'V_644',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_231,(1,0):C.GC_264})

V_645 = Vertex(name = 'V_645',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_197,(3,6):C.GC_244,(0,7):C.GC_197,(2,7):C.GC_244,(0,0):C.GC_290,(2,0):C.GC_315,(1,3):C.GC_290,(3,3):C.GC_315,(1,1):C.GC_298,(3,1):C.GC_323,(1,2):C.GC_715,(3,2):C.GC_727,(0,4):C.GC_298,(2,4):C.GC_323,(0,5):C.GC_715,(2,5):C.GC_727})

V_646 = Vertex(name = 'V_646',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_204,(3,6):C.GC_247,(0,7):C.GC_204,(2,7):C.GC_247,(0,0):C.GC_303,(2,0):C.GC_328,(1,3):C.GC_303,(3,3):C.GC_328,(1,1):C.GC_307,(3,1):C.GC_332,(1,2):C.GC_722,(3,2):C.GC_730,(0,4):C.GC_307,(2,4):C.GC_332,(0,5):C.GC_722,(2,5):C.GC_730})

V_647 = Vertex(name = 'V_647',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_215,(3,0):C.GC_256,(0,1):C.GC_215,(2,1):C.GC_256})

V_648 = Vertex(name = 'V_648',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_230,(3,0):C.GC_263,(0,1):C.GC_230,(2,1):C.GC_263})

V_649 = Vertex(name = 'V_649',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_195,(1,3):C.GC_242,(0,0):C.GC_286,(1,0):C.GC_311,(0,1):C.GC_296,(1,1):C.GC_321,(0,2):C.GC_713,(1,2):C.GC_725})

V_650 = Vertex(name = 'V_650',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_203,(1,3):C.GC_246,(0,0):C.GC_301,(1,0):C.GC_326,(0,1):C.GC_306,(1,1):C.GC_331,(0,2):C.GC_721,(1,2):C.GC_729})

V_651 = Vertex(name = 'V_651',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_211,(1,0):C.GC_252})

V_652 = Vertex(name = 'V_652',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_227,(1,0):C.GC_260})

V_653 = Vertex(name = 'V_653',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_201,(0,7):C.GC_201,(0,0):C.GC_288,(2,0):C.GC_313,(1,3):C.GC_294,(3,3):C.GC_319,(1,1):C.GC_288,(3,1):C.GC_313,(1,2):C.GC_719,(0,4):C.GC_294,(2,4):C.GC_319,(0,5):C.GC_719})

V_654 = Vertex(name = 'V_654',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_206,(0,7):C.GC_206,(0,0):C.GC_302,(2,0):C.GC_327,(1,3):C.GC_305,(3,3):C.GC_330,(1,1):C.GC_302,(3,1):C.GC_327,(1,2):C.GC_724,(0,4):C.GC_305,(2,4):C.GC_330,(0,5):C.GC_724})

V_655 = Vertex(name = 'V_655',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_223,(0,1):C.GC_223})

V_656 = Vertex(name = 'V_656',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_236,(0,1):C.GC_236})

V_657 = Vertex(name = 'V_657',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_193,(0,7):C.GC_193,(0,0):C.GC_265,(2,0):C.GC_266,(1,3):C.GC_265,(3,3):C.GC_266,(1,1):C.GC_265,(3,1):C.GC_266,(1,2):C.GC_645,(0,4):C.GC_265,(2,4):C.GC_266,(0,5):C.GC_645})

V_658 = Vertex(name = 'V_658',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_239,(0,1):C.GC_239})

V_659 = Vertex(name = 'V_659',
               particles = [ P.u__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_199,(0,7):C.GC_199,(0,0):C.GC_292,(2,0):C.GC_317,(1,3):C.GC_284,(3,3):C.GC_309,(1,1):C.GC_292,(3,1):C.GC_317,(1,2):C.GC_717,(0,4):C.GC_284,(2,4):C.GC_309,(0,5):C.GC_717})

V_660 = Vertex(name = 'V_660',
               particles = [ P.u__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_205,(0,7):C.GC_205,(0,0):C.GC_304,(2,0):C.GC_329,(1,3):C.GC_300,(3,3):C.GC_325,(1,1):C.GC_304,(3,1):C.GC_329,(1,2):C.GC_723,(0,4):C.GC_300,(2,4):C.GC_325,(0,5):C.GC_723})

V_661 = Vertex(name = 'V_661',
               particles = [ P.u__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_219,(0,1):C.GC_219})

V_662 = Vertex(name = 'V_662',
               particles = [ P.u__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_233,(0,1):C.GC_233})

V_663 = Vertex(name = 'V_663',
               particles = [ P.c__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_197,(1,3):C.GC_244,(0,0):C.GC_298,(1,0):C.GC_323,(0,1):C.GC_290,(1,1):C.GC_315,(0,2):C.GC_715,(1,2):C.GC_727})

V_664 = Vertex(name = 'V_664',
               particles = [ P.c__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_204,(1,3):C.GC_247,(0,0):C.GC_307,(1,0):C.GC_332,(0,1):C.GC_303,(1,1):C.GC_328,(0,2):C.GC_722,(1,2):C.GC_730})

V_665 = Vertex(name = 'V_665',
               particles = [ P.c__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_215,(1,0):C.GC_256})

V_666 = Vertex(name = 'V_666',
               particles = [ P.c__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_230,(1,0):C.GC_263})

V_667 = Vertex(name = 'V_667',
               particles = [ P.u__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_195,(3,6):C.GC_242,(0,7):C.GC_195,(2,7):C.GC_242,(0,0):C.GC_296,(2,0):C.GC_321,(1,3):C.GC_296,(3,3):C.GC_321,(1,1):C.GC_286,(3,1):C.GC_311,(1,2):C.GC_713,(3,2):C.GC_725,(0,4):C.GC_286,(2,4):C.GC_311,(0,5):C.GC_713,(2,5):C.GC_725})

V_668 = Vertex(name = 'V_668',
               particles = [ P.u__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,6):C.GC_203,(3,6):C.GC_246,(0,7):C.GC_203,(2,7):C.GC_246,(0,0):C.GC_306,(2,0):C.GC_331,(1,3):C.GC_306,(3,3):C.GC_331,(1,1):C.GC_301,(3,1):C.GC_326,(1,2):C.GC_721,(3,2):C.GC_729,(0,4):C.GC_301,(2,4):C.GC_326,(0,5):C.GC_721,(2,5):C.GC_729})

V_669 = Vertex(name = 'V_669',
               particles = [ P.u__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_211,(3,0):C.GC_252,(0,1):C.GC_211,(2,1):C.GC_252})

V_670 = Vertex(name = 'V_670',
               particles = [ P.u__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_227,(3,0):C.GC_260,(0,1):C.GC_227,(2,1):C.GC_260})

V_671 = Vertex(name = 'V_671',
               particles = [ P.d__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_195,(1,1):C.GC_242,(0,0):C.GC_286,(1,0):C.GC_311})

V_672 = Vertex(name = 'V_672',
               particles = [ P.d__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_203,(1,1):C.GC_246,(0,0):C.GC_301,(1,0):C.GC_326})

V_673 = Vertex(name = 'V_673',
               particles = [ P.d__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_212,(1,0):C.GC_253})

V_674 = Vertex(name = 'V_674',
               particles = [ P.d__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_675 = Vertex(name = 'V_675',
               particles = [ P.s__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_214,(3,1):C.GC_255,(0,2):C.GC_197,(2,2):C.GC_244,(0,0):C.GC_290,(2,0):C.GC_315})

V_676 = Vertex(name = 'V_676',
               particles = [ P.s__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_231,(3,1):C.GC_264,(0,2):C.GC_204,(2,2):C.GC_247,(0,0):C.GC_303,(2,0):C.GC_328})

V_677 = Vertex(name = 'V_677',
               particles = [ P.s__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_216,(1,0):C.GC_257})

V_678 = Vertex(name = 'V_678',
               particles = [ P.s__tilde__, P.b, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_679 = Vertex(name = 'V_679',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_195,(3,1):C.GC_242,(0,2):C.GC_210,(2,2):C.GC_251,(1,0):C.GC_286,(3,0):C.GC_311})

V_680 = Vertex(name = 'V_680',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF6, L.FFFF7 ],
               couplings = {(1,1):C.GC_203,(3,1):C.GC_246,(0,2):C.GC_228,(2,2):C.GC_261,(1,0):C.GC_301,(3,0):C.GC_326})

V_681 = Vertex(name = 'V_681',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_212,(1,0):C.GC_253})

V_682 = Vertex(name = 'V_682',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_683 = Vertex(name = 'V_683',
               particles = [ P.s__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_197,(1,1):C.GC_244,(0,0):C.GC_290,(1,0):C.GC_315})

V_684 = Vertex(name = 'V_684',
               particles = [ P.s__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_204,(1,1):C.GC_247,(0,0):C.GC_303,(1,0):C.GC_328})

V_685 = Vertex(name = 'V_685',
               particles = [ P.s__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_216,(1,0):C.GC_257})

V_686 = Vertex(name = 'V_686',
               particles = [ P.s__tilde__, P.b, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_687 = Vertex(name = 'V_687',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_210,(1,0):C.GC_251})

V_688 = Vertex(name = 'V_688',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_228,(1,0):C.GC_261})

V_689 = Vertex(name = 'V_689',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_214,(1,0):C.GC_255})

V_690 = Vertex(name = 'V_690',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_231,(1,0):C.GC_264})

V_691 = Vertex(name = 'V_691',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_195,(3,3):C.GC_242,(0,4):C.GC_210,(2,4):C.GC_251,(1,2):C.GC_95,(3,2):C.GC_114,(1,0):C.GC_296,(3,0):C.GC_321,(1,1):C.GC_679,(3,1):C.GC_697})

V_692 = Vertex(name = 'V_692',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF19, L.FFFF20, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_203,(3,3):C.GC_246,(0,4):C.GC_228,(2,4):C.GC_261,(1,2):C.GC_106,(3,2):C.GC_125,(1,0):C.GC_306,(3,0):C.GC_331,(1,1):C.GC_690,(3,1):C.GC_708})

V_693 = Vertex(name = 'V_693',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_212,(1,0):C.GC_253})

V_694 = Vertex(name = 'V_694',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_695 = Vertex(name = 'V_695',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_210,(1,0):C.GC_251})

V_696 = Vertex(name = 'V_696',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_228,(1,0):C.GC_261})

V_697 = Vertex(name = 'V_697',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_214,(1,0):C.GC_255})

V_698 = Vertex(name = 'V_698',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_231,(1,0):C.GC_264})

V_699 = Vertex(name = 'V_699',
               particles = [ P.s__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_214,(3,3):C.GC_255,(0,4):C.GC_197,(2,4):C.GC_244,(0,0):C.GC_99,(2,0):C.GC_118,(0,1):C.GC_298,(2,1):C.GC_323,(0,2):C.GC_683,(2,2):C.GC_701})

V_700 = Vertex(name = 'V_700',
               particles = [ P.s__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF6, L.FFFF7 ],
               couplings = {(1,3):C.GC_231,(3,3):C.GC_264,(0,4):C.GC_204,(2,4):C.GC_247,(0,0):C.GC_108,(2,0):C.GC_127,(0,1):C.GC_307,(2,1):C.GC_332,(0,2):C.GC_692,(2,2):C.GC_710})

V_701 = Vertex(name = 'V_701',
               particles = [ P.s__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_216,(1,0):C.GC_257})

V_702 = Vertex(name = 'V_702',
               particles = [ P.s__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_703 = Vertex(name = 'V_703',
               particles = [ P.d__tilde__, P.d, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_197,(1,3):C.GC_244,(0,0):C.GC_99,(1,0):C.GC_118,(0,1):C.GC_298,(1,1):C.GC_323,(0,2):C.GC_683,(1,2):C.GC_701})

V_704 = Vertex(name = 'V_704',
               particles = [ P.d__tilde__, P.d, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_204,(1,3):C.GC_247,(0,0):C.GC_108,(1,0):C.GC_127,(0,1):C.GC_307,(1,1):C.GC_332,(0,2):C.GC_692,(1,2):C.GC_710})

V_705 = Vertex(name = 'V_705',
               particles = [ P.d__tilde__, P.d, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_216,(1,0):C.GC_257})

V_706 = Vertex(name = 'V_706',
               particles = [ P.d__tilde__, P.d, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_229,(1,0):C.GC_262})

V_707 = Vertex(name = 'V_707',
               particles = [ P.s__tilde__, P.s, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_195,(1,3):C.GC_242,(0,0):C.GC_95,(1,0):C.GC_114,(0,1):C.GC_296,(1,1):C.GC_321,(0,2):C.GC_679,(1,2):C.GC_697})

V_708 = Vertex(name = 'V_708',
               particles = [ P.s__tilde__, P.s, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF15, L.FFFF21, L.FFFF22, L.FFFF7 ],
               couplings = {(0,3):C.GC_203,(1,3):C.GC_246,(0,0):C.GC_106,(1,0):C.GC_125,(0,1):C.GC_306,(1,1):C.GC_331,(0,2):C.GC_690,(1,2):C.GC_708})

V_709 = Vertex(name = 'V_709',
               particles = [ P.s__tilde__, P.s, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_212,(1,0):C.GC_253})

V_710 = Vertex(name = 'V_710',
               particles = [ P.s__tilde__, P.s, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_226,(1,0):C.GC_259})

V_711 = Vertex(name = 'V_711',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_193,(0,5):C.GC_193,(0,0):C.GC_82,(2,0):C.GC_83,(1,2):C.GC_82,(3,2):C.GC_83,(1,1):C.GC_82,(3,1):C.GC_83,(0,3):C.GC_82,(2,3):C.GC_83})

V_712 = Vertex(name = 'V_712',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_239,(0,1):C.GC_239})

V_713 = Vertex(name = 'V_713',
               particles = [ P.d__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_199,(0,5):C.GC_199,(0,0):C.GC_101,(2,0):C.GC_120,(1,2):C.GC_93,(3,2):C.GC_112,(1,1):C.GC_101,(3,1):C.GC_120,(0,3):C.GC_93,(2,3):C.GC_112})

V_714 = Vertex(name = 'V_714',
               particles = [ P.d__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_205,(0,5):C.GC_205,(0,0):C.GC_109,(2,0):C.GC_128,(1,2):C.GC_105,(3,2):C.GC_124,(1,1):C.GC_109,(3,1):C.GC_128,(0,3):C.GC_105,(2,3):C.GC_124})

V_715 = Vertex(name = 'V_715',
               particles = [ P.d__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_219,(0,1):C.GC_219})

V_716 = Vertex(name = 'V_716',
               particles = [ P.d__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_233,(0,1):C.GC_233})

V_717 = Vertex(name = 'V_717',
               particles = [ P.s__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_201,(0,5):C.GC_201,(0,0):C.GC_103,(2,0):C.GC_122,(1,2):C.GC_97,(3,2):C.GC_116,(1,1):C.GC_103,(3,1):C.GC_122,(0,3):C.GC_97,(2,3):C.GC_116})

V_718 = Vertex(name = 'V_718',
               particles = [ P.s__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF15, L.FFFF16, L.FFFF20, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,4):C.GC_206,(0,5):C.GC_206,(0,0):C.GC_110,(2,0):C.GC_129,(1,2):C.GC_107,(3,2):C.GC_126,(1,1):C.GC_110,(3,1):C.GC_129,(0,3):C.GC_107,(2,3):C.GC_126})

V_719 = Vertex(name = 'V_719',
               particles = [ P.s__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_223,(0,1):C.GC_223})

V_720 = Vertex(name = 'V_720',
               particles = [ P.s__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_236,(0,1):C.GC_236})

V_721 = Vertex(name = 'V_721',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_195,(3,2):C.GC_242,(0,3):C.GC_195,(2,3):C.GC_242,(1,0):C.GC_95,(3,0):C.GC_114,(0,1):C.GC_95,(2,1):C.GC_114})

V_722 = Vertex(name = 'V_722',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_203,(3,2):C.GC_246,(0,3):C.GC_203,(2,3):C.GC_246,(1,0):C.GC_106,(3,0):C.GC_125,(0,1):C.GC_106,(2,1):C.GC_125})

V_723 = Vertex(name = 'V_723',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_211,(3,0):C.GC_252,(0,1):C.GC_211,(2,1):C.GC_252})

V_724 = Vertex(name = 'V_724',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_227,(3,0):C.GC_260,(0,1):C.GC_227,(2,1):C.GC_260})

V_725 = Vertex(name = 'V_725',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_197,(1,1):C.GC_244,(0,0):C.GC_99,(1,0):C.GC_118})

V_726 = Vertex(name = 'V_726',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_204,(1,1):C.GC_247,(0,0):C.GC_108,(1,0):C.GC_127})

V_727 = Vertex(name = 'V_727',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_215,(1,0):C.GC_256})

V_728 = Vertex(name = 'V_728',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_230,(1,0):C.GC_263})

V_729 = Vertex(name = 'V_729',
               particles = [ P.d__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_195,(1,1):C.GC_242,(0,0):C.GC_95,(1,0):C.GC_114})

V_730 = Vertex(name = 'V_730',
               particles = [ P.d__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF21, L.FFFF7 ],
               couplings = {(0,1):C.GC_203,(1,1):C.GC_246,(0,0):C.GC_106,(1,0):C.GC_125})

V_731 = Vertex(name = 'V_731',
               particles = [ P.d__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_211,(1,0):C.GC_252})

V_732 = Vertex(name = 'V_732',
               particles = [ P.d__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_227,(1,0):C.GC_260})

V_733 = Vertex(name = 'V_733',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_197,(3,2):C.GC_244,(0,3):C.GC_197,(2,3):C.GC_244,(1,0):C.GC_99,(3,0):C.GC_118,(0,1):C.GC_99,(2,1):C.GC_118})

V_734 = Vertex(name = 'V_734',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF16, L.FFFF21, L.FFFF6, L.FFFF7 ],
               couplings = {(1,2):C.GC_204,(3,2):C.GC_247,(0,3):C.GC_204,(2,3):C.GC_247,(1,0):C.GC_108,(3,0):C.GC_127,(0,1):C.GC_108,(2,1):C.GC_127})

V_735 = Vertex(name = 'V_735',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_215,(3,0):C.GC_256,(0,1):C.GC_215,(2,1):C.GC_256})

V_736 = Vertex(name = 'V_736',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF6, L.FFFF7 ],
               couplings = {(1,0):C.GC_230,(3,0):C.GC_263,(0,1):C.GC_230,(2,1):C.GC_263})

V_737 = Vertex(name = 'V_737',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_156,(0,0):C.GC_441})

V_738 = Vertex(name = 'V_738',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_167,(0,0):C.GC_632})

V_739 = Vertex(name = 'V_739',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_177})

V_740 = Vertex(name = 'V_740',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_188})

V_741 = Vertex(name = 'V_741',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_151,(0,0):C.GC_436})

V_742 = Vertex(name = 'V_742',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_172})

V_743 = Vertex(name = 'V_743',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_154,(0,0):C.GC_439})

V_744 = Vertex(name = 'V_744',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_166,(0,0):C.GC_631})

V_745 = Vertex(name = 'V_745',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_175})

V_746 = Vertex(name = 'V_746',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_187})

V_747 = Vertex(name = 'V_747',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_160,(0,0):C.GC_445})

V_748 = Vertex(name = 'V_748',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_169,(0,0):C.GC_634})

V_749 = Vertex(name = 'V_749',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_181})

V_750 = Vertex(name = 'V_750',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_190})

V_751 = Vertex(name = 'V_751',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_152,(0,0):C.GC_437})

V_752 = Vertex(name = 'V_752',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_173})

V_753 = Vertex(name = 'V_753',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_158,(0,0):C.GC_443})

V_754 = Vertex(name = 'V_754',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_168,(0,0):C.GC_633})

V_755 = Vertex(name = 'V_755',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_179})

V_756 = Vertex(name = 'V_756',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_189})

V_757 = Vertex(name = 'V_757',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_164,(0,0):C.GC_449})

V_758 = Vertex(name = 'V_758',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_171,(0,0):C.GC_636})

V_759 = Vertex(name = 'V_759',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_185})

V_760 = Vertex(name = 'V_760',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_192})

V_761 = Vertex(name = 'V_761',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_153,(0,0):C.GC_438})

V_762 = Vertex(name = 'V_762',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_174})

V_763 = Vertex(name = 'V_763',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_162,(0,0):C.GC_447})

V_764 = Vertex(name = 'V_764',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF15, L.FFFF7 ],
               couplings = {(0,1):C.GC_170,(0,0):C.GC_635})

V_765 = Vertex(name = 'V_765',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_183})

V_766 = Vertex(name = 'V_766',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_191})

V_767 = Vertex(name = 'V_767',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_172})

V_768 = Vertex(name = 'V_768',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_175})

V_769 = Vertex(name = 'V_769',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_187})

V_770 = Vertex(name = 'V_770',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_177})

V_771 = Vertex(name = 'V_771',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_188})

V_772 = Vertex(name = 'V_772',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_173})

V_773 = Vertex(name = 'V_773',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_179})

V_774 = Vertex(name = 'V_774',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_189})

V_775 = Vertex(name = 'V_775',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_181})

V_776 = Vertex(name = 'V_776',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_190})

V_777 = Vertex(name = 'V_777',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_174})

V_778 = Vertex(name = 'V_778',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_183})

V_779 = Vertex(name = 'V_779',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_191})

V_780 = Vertex(name = 'V_780',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_185})

V_781 = Vertex(name = 'V_781',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_192})

V_782 = Vertex(name = 'V_782',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_783 = Vertex(name = 'V_783',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_784 = Vertex(name = 'V_784',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_785 = Vertex(name = 'V_785',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_786 = Vertex(name = 'V_786',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_787 = Vertex(name = 'V_787',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_788 = Vertex(name = 'V_788',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_789 = Vertex(name = 'V_789',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_790 = Vertex(name = 'V_790',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_791 = Vertex(name = 'V_791',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_792 = Vertex(name = 'V_792',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_793 = Vertex(name = 'V_793',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_794 = Vertex(name = 'V_794',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_795 = Vertex(name = 'V_795',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_796 = Vertex(name = 'V_796',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_797 = Vertex(name = 'V_797',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_798 = Vertex(name = 'V_798',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_799 = Vertex(name = 'V_799',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_800 = Vertex(name = 'V_800',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_801 = Vertex(name = 'V_801',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_802 = Vertex(name = 'V_802',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_803 = Vertex(name = 'V_803',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_748})

V_804 = Vertex(name = 'V_804',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_750,(0,1):C.GC_782})

V_805 = Vertex(name = 'V_805',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_750,(0,1):C.GC_782})

V_806 = Vertex(name = 'V_806',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_782})

V_807 = Vertex(name = 'V_807',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV6 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_782})

V_808 = Vertex(name = 'V_808',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_798})

V_809 = Vertex(name = 'V_809',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_798})

V_810 = Vertex(name = 'V_810',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_798})

V_811 = Vertex(name = 'V_811',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_783})

V_812 = Vertex(name = 'V_812',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_783})

V_813 = Vertex(name = 'V_813',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_783})

V_814 = Vertex(name = 'V_814',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_891,(0,1):C.GC_908})

V_815 = Vertex(name = 'V_815',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_896,(0,1):C.GC_915})

V_816 = Vertex(name = 'V_816',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_887,(0,1):C.GC_902})

V_817 = Vertex(name = 'V_817',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_889,(0,1):C.GC_904})

V_818 = Vertex(name = 'V_818',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_890,(0,1):C.GC_907})

V_819 = Vertex(name = 'V_819',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_894,(0,1):C.GC_913})

V_820 = Vertex(name = 'V_820',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_892,(0,1):C.GC_905})

V_821 = Vertex(name = 'V_821',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_898,(0,1):C.GC_909})

V_822 = Vertex(name = 'V_822',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_893,(0,1):C.GC_906})

V_823 = Vertex(name = 'V_823',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_900,(0,1):C.GC_911})

V_824 = Vertex(name = 'V_824',
               particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1006,(0,1):C.GC_1001})

V_825 = Vertex(name = 'V_825',
               particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1010,(0,1):C.GC_1008})

V_826 = Vertex(name = 'V_826',
               particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1002,(0,1):C.GC_1005})

V_827 = Vertex(name = 'V_827',
               particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1008,(0,1):C.GC_1010})

V_828 = Vertex(name = 'V_828',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,1):C.GC_997,(0,0):C.GC_998})

V_829 = Vertex(name = 'V_829',
               particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1000,(0,1):C.GC_1003})

V_830 = Vertex(name = 'V_830',
               particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1007,(0,1):C.GC_1009})

V_831 = Vertex(name = 'V_831',
               particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1004,(0,1):C.GC_999})

V_832 = Vertex(name = 'V_832',
               particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1009,(0,1):C.GC_1007})

V_833 = Vertex(name = 'V_833',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1015,(0,1):C.GC_1032})

V_834 = Vertex(name = 'V_834',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1021,(0,1):C.GC_1040})

V_835 = Vertex(name = 'V_835',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1012,(0,1):C.GC_1027})

V_836 = Vertex(name = 'V_836',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1013,(0,1):C.GC_1028})

V_837 = Vertex(name = 'V_837',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1014,(0,1):C.GC_1031})

V_838 = Vertex(name = 'V_838',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1019,(0,1):C.GC_1038})

V_839 = Vertex(name = 'V_839',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1016,(0,1):C.GC_1029})

V_840 = Vertex(name = 'V_840',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1023,(0,1):C.GC_1034})

V_841 = Vertex(name = 'V_841',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1017,(0,1):C.GC_1030})

V_842 = Vertex(name = 'V_842',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1025,(0,1):C.GC_1036})

V_843 = Vertex(name = 'V_843',
               particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_908,(0,1):C.GC_891})

V_844 = Vertex(name = 'V_844',
               particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_916,(0,1):C.GC_897})

V_845 = Vertex(name = 'V_845',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_903,(0,1):C.GC_888})

V_846 = Vertex(name = 'V_846',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_904,(0,1):C.GC_889})

V_847 = Vertex(name = 'V_847',
               particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_905,(0,1):C.GC_892})

V_848 = Vertex(name = 'V_848',
               particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_910,(0,1):C.GC_899})

V_849 = Vertex(name = 'V_849',
               particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_906,(0,1):C.GC_893})

V_850 = Vertex(name = 'V_850',
               particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_912,(0,1):C.GC_901})

V_851 = Vertex(name = 'V_851',
               particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_907,(0,1):C.GC_890})

V_852 = Vertex(name = 'V_852',
               particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_914,(0,1):C.GC_895})

V_853 = Vertex(name = 'V_853',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,1):C.GC_961,(0,0):C.GC_962})

V_854 = Vertex(name = 'V_854',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_963,(0,1):C.GC_968})

V_855 = Vertex(name = 'V_855',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_971,(0,1):C.GC_973})

V_856 = Vertex(name = 'V_856',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_965,(0,1):C.GC_970})

V_857 = Vertex(name = 'V_857',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_972,(0,1):C.GC_974})

V_858 = Vertex(name = 'V_858',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_967,(0,1):C.GC_964})

V_859 = Vertex(name = 'V_859',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_973,(0,1):C.GC_971})

V_860 = Vertex(name = 'V_860',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_969,(0,1):C.GC_966})

V_861 = Vertex(name = 'V_861',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_974,(0,1):C.GC_972})

V_862 = Vertex(name = 'V_862',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1032,(0,1):C.GC_1015})

V_863 = Vertex(name = 'V_863',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1039,(0,1):C.GC_1020})

V_864 = Vertex(name = 'V_864',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1026,(0,1):C.GC_1011})

V_865 = Vertex(name = 'V_865',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1028,(0,1):C.GC_1013})

V_866 = Vertex(name = 'V_866',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1029,(0,1):C.GC_1016})

V_867 = Vertex(name = 'V_867',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1033,(0,1):C.GC_1022})

V_868 = Vertex(name = 'V_868',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1030,(0,1):C.GC_1017})

V_869 = Vertex(name = 'V_869',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1035,(0,1):C.GC_1024})

V_870 = Vertex(name = 'V_870',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1031,(0,1):C.GC_1014})

V_871 = Vertex(name = 'V_871',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,0):C.GC_1037,(0,1):C.GC_1018})

