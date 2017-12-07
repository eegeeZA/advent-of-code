def build_tree(tree, root):
    result = {root: []}
    if not tree[root]:
        return root
    for value in tree[root]:
        result[root].append(build_tree(tree, value))
    return result


def build_tree_weights(factor_x):
    if type(factor_x) is dict:
        for key, value in factor_x.items():
            return build_tree_weights(value)[0] + weights[key], key
    elif type(factor_x) is list:
        sub_values = []
        for value in factor_x:
            tree_weights = build_tree_weights(value)
            sub_values.append(tree_weights[0])
            if len(set(sub_values)) != 1:
                print(tree_weights)
                print(sub_values)
                exit()
        return sum(sub_values), ""
    else:
        return weights[factor_x], factor_x


inputs = """aacegb (8)
aatagmv (44)
abbnh (33)
abmqz (31)
acfyjc (85)
acxlck (73)
adbolgz (38)
adxhax (74)
aeyykn (66) -> lrkfnoy, ltdrusl
afeqhu (78)
afrywlt (80)
agliie (844) -> qjaywg, rridl, myaiu, antcinm, izhdt
ahmitv (11)
ahqfoz (52)
aidknm (97)
aiunuvn (1629) -> gjrqs, ukkaxy, lijeejc, zlgpmfs, zksmijj
ajhctd (18)
akidv (21) -> cnvyxm, fphgbca
akpnwc (90)
akwfu (50) -> tremw, uwhjd
alztgi (32)
amnoi (141) -> noxvvva, dfeyr
amrbhgv (126) -> xpker, gkkrlg, jbzaips
amzwex (218) -> vprkzya, wxixtqj, oktfn
anbcmt (17)
anmeg (58)
antcinm (178) -> dmthn, ycacj, wkhggv
aodnlv (58)
aoehbj (182) -> dyimc, scmiv
aokpx (70)
aonfaf (52)
aovlz (45)
aozygag (125)
apdfe (184) -> xrxseqy, leegl
aplbnbx (28)
apmdcz (16)
apwsmv (31)
aqkdlo (24)
asbzj (89) -> yjxyb, hsifo, fhasacf, vwojb, gcbcyn
asifeu (278) -> rtsajcq, dcouu
assuj (137) -> atfhgyu, pxhwecw
atfhgyu (57)
auneqme (86)
avelbqj (31)
avzljw (234) -> vdbihjp, zavef
awagc (18)
awccm (86)
awufxne (2141) -> qllluo, wpoga
axikbt (9) -> tjffhqh, mogwb, cykvxs, ydqjoa
ayaouxu (200) -> ksyewek, gpfrztg
ayejq (86)
ayury (23)
baawtw (50) -> nnguamj, yetcvhx
bbfaxid (138)
bbhyth (53) -> xcqwjrm, kgmwfq
bbkfiz (11)
bbzmsv (87)
bchfd (109) -> ccityq, nmvvgr
bchlcqs (53)
bcjecw (80)
bclicjl (217) -> dxufd, jhcsmc
bcyarwn (65)
bdafpm (58)
bdkoa (125) -> ctynr, tvnco
bdymucv (304) -> uzsytm, sslltlv
behncf (16)
bekxoxk (87)
beraw (14)
berje (87)
besihsl (86)
bexvn (39)
bezvr (55)
bgbnlki (2277) -> oqbfkud, qsqis, xhyqtqz, qorkez, qwzac, oewlch, gsiypfp
bgrxlxe (65)
bhwca (76)
bhxdhmr (65)
bihsr (21) -> kyjkjy, hgscccv, yonjpz
bkcghv (35)
bkkop (347)
bkldmro (212) -> bsixe, afrywlt
bkmvwp (11)
blagy (338)
blmfs (52)
bmmmp (90)
bmugsve (36)
borbd (21) -> ujktzrv, hbzju, xulwh, xatyg
boygd (13) -> wiayzvp, mdhhd, jkqvg, wouprxh
bozlg (67)
bpphw (49)
bpqhqbg (63)
bpzxjg (62)
bqifoq (55)
bqmqbi (47)
bqqwmry (73)
bqtawf (45)
bqznix (75) -> stiln, duophdw, yhzuh
brcpgz (57)
brztp (27)
bsixe (80)
bsrkr (21)
btcjg (57)
btgrhku (24)
btxepbv (90)
bugfhhx (357) -> abbnh, intfltq
bugwblt (14)
bvfcsls (227) -> knpwsi, ypfsjd, eilzvpr
bvrlaep (143) -> dnrfjv, wndpfac, bezvr
bwrpskq (65)
bwvemo (29)
bymkeq (71)
bymzb (68) -> zneumoh, zhopeqm
bzsiwp (71)
capxp (68)
cbgyk (43)
cbyvzkp (99)
ccckie (201) -> tgkusb, alztgi
ccityq (34)
ccsrkny (34)
cdbkci (79)
cdpfk (92)
cfaniht (17)
cfnce (59)
cfuqhip (57) -> ixkicz, yqnihs, vifwkwa
cgfykiv (38)
cgouh (26)
chnfm (169)
ciejakr (43) -> hcqnhm, anmeg, melsryt
ciogjt (375) -> tygnc, vhrtptr, ccckie
cipgxee (72)
cipwzoy (74)
citugfl (14)
cizehi (7)
cjcapa (292)
cjmfqbo (69)
ckhip (88) -> vhxlart, rznnmp
ckwooig (84)
ckwopo (43) -> yurfpj, bgrxlxe, tohrp
cldbz (15)
clnkvox (33)
clpekkm (77)
cluxnul (15)
cmaxybh (78)
cmfkxo (87)
cmxulaj (44) -> mnkqevh, mkbgt, nrcbc
cnbekc (92)
cnnrj (78)
cnvyxm (59)
cotpovw (91)
cotvk (91)
cpfbmv (204)
cqlwzk (217) -> besihsl, cwdmlj
crhho (1255) -> rfcfgg, chnfm, tuekps
crobb (8)
csqfv (14)
cssov (57)
cstgeia (613) -> ckwopo, sjiel, akwfu, ehvqyl, wtyfb, gcmio
ctfjb (20)
ctynr (63)
ctytfj (29)
cuhrgp (81) -> ohtply, vrfkofp
cvgbj (48)
cwdmlj (86)
cxhipq (92)
cxnjv (66)
cyielpd (6)
cykvxs (84)
cytlm (46)
cyzzsc (52)
cztikzk (174) -> wxdpcvv, lpbayb
dbnelj (212) -> jzcmf, sqiac, ijyoy, jjqguew
dbufjl (95) -> faihy, oyamw
dcmxxd (35)
dcouu (6)
dczcz (1862) -> wszghwt, navhthp, lsfggz
dfeyr (94)
dfmlo (80)
dgjls (1926) -> lgxjr, hrphtyk, mhzgkxx
dhlrq (88)
dhqzt (305) -> capxp, pttij
dihzy (79)
dkhuccj (96) -> kbyot, zhbiaq, hhmavd, xejner, cqlwzk
dkttrfw (219) -> ahqfoz, kytnz
dkvzre (99) -> mieecfc, nvdouwn, dbnelj, onlwq, ayaouxu, xrhsy, bvrlaep
dkyswuu (120) -> zjzoo, bhxdhmr
dlabh (56)
dlhiqh (7301) -> rdrad, vmmjgy, uvmqarq
dmdiy (1601) -> lazjlns, ygvol, rljjjo, whnjtp, jilomb
dmthn (25)
dmvjz (39)
dmxhbe (141) -> myhrxc, jbbivz, behncf
dnalt (35)
dnazkh (80)
dnfvldg (85) -> yjakrqa, lahain
dnrfjv (55)
dnzdqz (179)
dokgk (17)
dpdjpal (42)
dqgfb (43) -> hpuyku, rycmr
dqgivj (57)
drfwgmu (249) -> zktnjab, cmfkxo
drgtn (84)
dssdiok (97)
dtexqt (88)
dtzyg (24)
duepwu (683) -> hbueku, zbcra, yxtjx
duophdw (72)
dvfuz (30)
dvoja (54)
dwknfpc (63)
dwpqell (35)
dxboqki (78) -> nstdz, ferzy
dxhcxko (45) -> ftzht, ypsme, rmtbjn, pjyld
dxqqhhd (188) -> pzewv, oelrlp
dxufd (64)
dxympe (23)
dydwqz (97)
dyimc (54)
dyrvvfn (340) -> prxseo, vxgwku
dyscpqo (49)
dzggd (663) -> iipqh, nnxfo, veggtf
dzjyzd (39)
dzohgiq (43)
dzouqwl (57)
dzrkq (94)
ebgdslc (31)
ebmcu (30) -> glsrg, ckhip, rqhhyc, jjvxxtt, rdnpoms
ebmjz (68) -> xfydt, eqnvty
ecdieu (23)
eceocsy (35)
ecjdzpq (35)
ecoqyk (35)
ecxfenj (78) -> urjwj, jesiypo
edjwkkk (14)
edkigpl (18)
edpjix (58)
efsrz (93)
eggmj (77)
egrfvic (49)
egsil (38)
ehjnzn (79)
ehrqn (23) -> njabgq, fyzeso, jrgwnfh, fxasat
ehvqyl (192) -> zjgok, ecdieu
eilzvpr (213) -> ksrsmjx, zpntow
eiwjrxx (45) -> hbsmlf, dlabh, rcjxcou
eiyxf (32)
ejuiv (31)
ejzeqxz (51)
ekabfx (83)
ekihql (1184) -> ezxsv, vonzkut, dkyswuu, uyrght, uzjxd, yjomyth
eklahxm (51)
ekszr (148) -> gnmydtk, wchxl
ekxxsqa (83)
ekzvjj (35)
elmog (32)
enbnfw (39)
epsjj (17)
epumc (86) -> pcdjo, rerckg, dwknfpc
eqhxqxm (45)
eqnvty (87)
eqsxuaq (49)
erfndpf (89) -> kwbovke, adxhax, cipwzoy
erfnrn (6)
erggh (197) -> fksxl, ghbfyqe
erkarx (79)
eskdbe (17)
eszxg (18)
etscle (45)
etwwy (16)
etyyw (11)
euqiok (9)
eutcl (77)
evcdf (57)
evnlr (1175) -> erfndpf, hicuenj, zybeuh
evqkdq (91)
ewpbnsk (64)
ewvvi (53)
exwxepj (175) -> jszpe, guvuihw, ykruy
exxcrj (316) -> dzjyzd, pkoww
eyale (97)
ezdhr (179)
ezxsv (90) -> qzqyveb, dfmlo
faihy (65)
fbhidp (17)
fbjbwv (290)
fbqpk (38)
fcpde (175) -> beraw, qqishhq, citugfl, pmfkdn
fcscdg (276) -> twvib, skjtvyz, oybwhs, rdmggka
ferzy (65)
fetkt (203) -> nnhsuja, kxflpnl, xumsm
fgdqr (34)
fhasacf (269) -> fovilf, rjnzany
fhpaqmd (23)
fhzhqie (65)
fiufzkb (1194) -> ysigfem, bchfd, hgsmlsi
fjhqmnv (57)
fjpgybt (21)
fjzpjk (88) -> uvsny, aatagmv
fkbrmim (71889) -> peuppj, uobgj, llventw, duepwu
fkgxak (328) -> wpnqifq, xbucnh, qjwfsfk, rcsfkrb
fksxl (5)
fmkkz (319) -> owigu, ikbqz
fmqjogk (24)
fmtyy (35)
fmxtg (84) -> ursjc, eqhxqxm, qroirmg
fnoteku (2482) -> mbezs, kcuygjx, bymkeq, opsqjx
fovilf (44)
fovkc (49)
foyfb (50)
fozyip (293) -> kvlbq, pfqbht
fphgbca (59)
fpqudx (187) -> iuxgzr, icqjyqd, apmdcz, mhapqqy
fpynzz (24) -> kepkgvf, kabixkr, jbexk
frksv (89)
fticuc (1360) -> vleydj, lnczb, igpabio, wydbqai
ftzht (8102) -> dmdiy, sfrbkzf, hlcnxe, zwsrt
fukgfu (20)
fvfek (96)
fxasat (57)
fydjnl (32)
fynniwm (35)
fyzeso (57)
fzqsahw (256) -> lybovx, pdmhva
gbnxgny (12)
gcbcyn (289) -> vflyupn, mbwenqu
gcmio (126) -> ujjpxe, jjxvns
gcomv (84)
gcwcs (93) -> dokgk, epsjj
gcxrx (91)
geqwvx (129) -> acxlck, zqnmsyb, ojnziip
gexdb (6)
gfqtz (98)
ghbfyqe (5)
ghdime (76)
ghobhlm (41)
gijtd (75)
gjcxbx (44)
gjrqs (159) -> iprkb, cgouh
gkkrlg (36)
glsrg (74) -> maiimn, ufyqf
gmcsy (16)
gmdsb (75)
gmwtl (49)
gnmydtk (67)
goxfpk (6)
gpfrztg (54)
gqggcxb (29) -> tzrppo, bugfhhx, drfwgmu
gqmscj (155) -> kjlmdi, scaec
gqzva (6)
grazu (90)
grcox (91)
gsiypfp (1146) -> bhwca, qhcolun
gtervu (88) -> dkvzre, awufxne, osbbt, ycbgx, wdjzjlk
guvuihw (39)
gwnipjd (24)
gwtcgyo (24)
gwyfm (287) -> liamld, ucqdz
gxiwcqv (186) -> zfhwfsw, lovypfn
gxsbt (58)
gxzkde (65)
gylsj (52)
gynfwly (66) -> lynvd, dxhcxko, xaatl, leulsg, zworz, fkbrmim, jjjks
gyutarg (51) -> adbolgz, vdvadz
gzixhdc (124) -> ypqxs, setrric, smmgkir
hbkjjtt (61)
hbkujf (133) -> ukghke, aplbnbx
hbsmlf (56)
hbueku (10) -> ohcszyk, szutvca
hbylau (94)
hbzju (71)
hcqnhm (58)
hdlovco (5)
hdzxuz (24)
herqgqi (36)
hfvhp (2018) -> wewzb, opmmmd, zmqom
hgscccv (62)
hgsmlsi (31) -> bqqwmry, lqavsk
hhifd (6)
hhlxxzt (96) -> ixtrjm, tknmww, cnbekc
hhmavd (359) -> pxzdv, qjzol
hhqlfj (81) -> xqgwwr, zmlmsuf
hhwngc (138) -> ewpbnsk, swurfm
hicuenj (122) -> ootidjt, hlrjgro, ywvmghy
hjjfdj (11)
hkjtym (247) -> iwsjla, thqkxpl
hkjwio (322) -> hdzxuz, zdgwmi, ipryqov
hkpvwpa (75)
hlcnxe (1998) -> fcpde, zyniqni, offjbb
hlrjgro (63)
hpaggeh (88)
hpeaki (35)
hpowmso (1854) -> jhysc, xeomb, nzwxd
hpuyku (82)
hrgbkby (53) -> saowgr, lprmau, ntabiof
hrjgaqj (29)
hrncqs (12)
hrphtyk (19) -> xjcprt, bbzmsv, berje
hrvztx (57)
hsfjd (21)
hshyx (93)
hsifo (210) -> wfdlusw, myonh, qunldzi
hsoxt (62)
huhoda (191) -> bpphw, eqsxuaq, gmwtl
husmkc (29)
huunb (88)
hvcii (85)
hwrxn (53) -> dihzy, ibysnvc, zunhob
hxgidsw (332) -> fukgfu, skkatyg
iajslqp (32) -> avelbqj, ebgdslc, vzqnfs
ibiwh (26) -> ndsub, moihbcu
ibonrqn (50)
ibvaekj (9)
ibysnvc (79)
icjur (76) -> lwaeqm, rhdudt
icqjyqd (16)
iekurr (71)
ietfhkq (31)
ifbxvs (20)
ifelr (77)
igpabio (53) -> mlqxueo, lhsncv
iimfrx (59)
iipqh (299)
iizbmoz (31)
ijcojo (1042) -> dxboqki, ikplh, pubtsp, omergh
ijmfnt (28)
ijyoy (24)
ikbqz (9)
ikdsvc (1609) -> icjur, ebmjz, rxivjo, rhzimzq
ikfihh (140) -> tygwtg, vlmhyer
ikplh (98) -> bqifoq, pjedtl
ilxfa (34)
imezigo (50)
imjutr (187) -> wgeig, wqbhby
inghbu (1167) -> vcvypf, ljqmiu, tglnkgk
inldh (4965) -> ogvod, agliie, wenii
intfltq (33)
iolmgs (95)
iplyhhc (122) -> cbgyk, dzohgiq
iprkb (26)
ipryqov (24)
iqygrur (44)
isggu (5)
iteizf (21)
itttb (90)
itxycu (45) -> eutcl, kdevmnr
iuxgzr (16)
ivwcuc (88)
iwsjla (38)
iwyjkz (86)
ixkicz (353)
ixtrjm (92)
ixxkvtz (71)
izhdt (57) -> gfqtz, sztqzfl
izkaqg (26)
jancm (58)
jaxidl (86)
jbbivz (16)
jbbmcxg (34)
jbexk (73)
jbzaips (36)
jcpavmj (53)
jdzbqlz (15)
jesiypo (78)
jfdscql (362) -> amrbhgv, rfdpm, ecxfenj, dxqqhhd
jgtpw (84) -> cxnjv, zelucu, ygurya, mrsrl
jgwvp (84)
jhcsmc (64)
jhgsgy (39)
jhldwxy (26)
jhysc (274) -> cldbz, cluxnul
jijwa (3632) -> xwltxk, ikdsvc, tcghqr
jilomb (68) -> uduan, mecyei
jiuuhl (78)
jjjks (7331) -> qpefm, dlhiqh, gtervu, pcnroj, jijwa, bgbnlki
jjqguew (24)
jjvxxtt (194) -> ldfsxw, mhkcp
jjxvns (56)
jkamtqv (80)
jkfob (49)
jkqvg (28)
jlbcwrl (93)
jlfgvr (72)
jlfho (83)
jlvwibm (46)
jmieet (137) -> ckwooig, stkodp
jmlznjh (50)
jntohm (41)
jopyit (51)
jpenh (186) -> kdcvwyf, rjxvbkb
jqkaucw (53)
jqmlxr (173) -> eiyxf, fydjnl
jrgwnfh (57)
jscjw (72)
jsjaxjk (88) -> aidknm, uiwaf
jszpe (39)
jteju (54)
juptypm (14)
jvhxfl (39)
jwaskb (251)
jxfqev (99)
jzcmf (24)
jzibybz (248) -> zrpqdzn, hsoxt
jzsmy (39)
jzuvrtp (57)
kabcmf (51)
kabixkr (73)
kayqqz (77) -> kdqjj, sbdja, gmcsy
kazqnjr (391) -> qngfv, aacegb
kbppnh (99)
kbses (93)
kbyot (337) -> jhldwxy, izkaqg
kcuygjx (71)
kdcvwyf (52)
kdevmnr (77)
kdqjj (16)
kepkgvf (73)
kgevjdx (84)
kgmwfq (63)
khiom (117) -> hpaggeh, lqumiws
khpat (53)
khqhd (42)
kiauwpn (22)
kifer (53)
kigdvl (31)
kjjyu (65)
kjlmdi (96)
kkdaw (65)
kledju (95)
kmarvbs (90)
kmogwi (1139) -> hkjtym, tgujvov, dkttrfw
knpwsi (261) -> cvgbj, uzjejte
koane (8) -> rawuoi, hkjwio, vpynuf, exxcrj, ljhtov, pwdpe, bdymucv
koxiwk (929) -> fcscdg, geqwvx, jgtpw, zorvynv, zotwsb
kplegas (86)
kqaoir (80) -> ytspbx, dyrvvfn, bkldmro, qonfiro, hhlxxzt, jzibybz, slrfd
krcoaft (59)
krmphks (12)
ksrsmjx (72)
kstvq (69)
ksybvgt (213)
ksyewek (54)
ktazkb (57)
kvdrnf (72)
kvlbq (22)
kwbovke (74)
kwmam (184) -> wdybaj, cyielpd, hhifd, gexdb
kwwsxez (27)
kxflpnl (16)
kybsigz (80)
kyjkjy (62)
kytnz (52)
kzdugfh (90)
kztkiqt (13) -> egsil, mjugqpu
lafoho (250)
lageym (228)
lahain (70)
laxoeu (88)
lazjlns (190) -> xbyjur, edjwkkk
ldfsxw (17)
ldnrw (760) -> plumb, yvhilh, kztkiqt, ltbpi
ldxgz (18)
leegl (94)
leeyi (88)
leulsg (44696) -> tifqyde, olkopyn, lfjtmkg
leyiz (74) -> fvfek, njrfnvt
lfjtmkg (6095) -> lsteeu, zxkvs, sdhqlxw
lgefkp (17)
lghzki (27)
lgxjr (238) -> mhkba, bsrkr
lhsccbq (42)
lhsncv (67)
liamld (25)
lijeejc (57) -> mgkkyx, thzyz
lixqwd (35)
lixsvp (11)
ljhtov (394)
ljhxxd (38)
ljqmiu (31) -> ibonrqn, imezigo
lkorngt (132) -> tjpatnk, nmstp
llibmc (49)
llventw (308) -> lsbsfge, itxycu, nddymc
lmqaxz (146) -> ghobhlm, qvvcx
lmwrf (51)
lnczb (69) -> tzntd, cfnce
losdis (1165) -> vhmijln, lteyo, viufoq
lovypfn (53)
lpbayb (8)
lppvxfk (1001) -> nrnmjo, phmtqf, bqznix
lprmau (27) -> rqymw, dssdiok, dydwqz, eyale
lptkbzc (151) -> unvje, bzsiwp
lqavsk (73)
lqumiws (88)
lrkfnoy (78)
lsbsfge (163) -> ldxgz, mksan
lsfggz (94) -> itttb, wpdbejb
lsteeu (162) -> tatubv, rprjk, tgblta, uxrrjqx, pweea, sgieno
ltbpi (17) -> vwcygm, herqgqi
ltdrusl (78)
lteyo (157) -> mfvkd, swpfak
lwaeqm (83)
lwljcg (85)
lwwyx (41) -> vuetjdb, ciejakr, imjutr, zgimdwb, sdnlegj, gzixhdc, tlvkwlx
lxhkgs (85)
lybovx (18)
lynvd (42593) -> tuieolg, pddteg, pixmx
lytcy (2662) -> bkmvwp, uyrwi
lywkfsn (127)
lzxrfk (21)
mabkbom (57)
maiimn (77)
mbezs (71)
mbwenqu (34)
mddejh (441)
mdhhd (28)
mdzkkjf (22)
mecyei (75)
melsryt (58)
mepez (126) -> uqvyau, witovp
mewof (12)
mfjeyx (49) -> tdniuai, vdjmhb
mfvkd (21)
mfywm (79) -> erkarx, vscjrx
mgkkyx (77)
mgqfa (75) -> cipgxee, jscjw
mhapqqy (16)
mhkba (21)
mhkcp (17)
mhnlgyl (1185) -> qntstgd, qzpgle, aozygag
mhydkla (7)
mhzgkxx (156) -> qzakfh, tnayomw
mieecfc (138) -> lwljcg, acfyjc
miftchq (21)
miijab (49)
mjaol (281) -> dnazkh, jkamtqv
mjlnaz (72) -> zcgfj, jiuuhl
mjsck (90) -> mkkpihe, fmqjogk
mjugqpu (38)
mkbgt (98)
mkkpihe (24)
mksan (18)
mkyam (372)
mlqxueo (67)
mmerpi (5)
mnfqc (789) -> zqtkn, hhqlfj, lywkfsn
mnhojtk (218) -> kvdrnf, nkjgwn
mnkqevh (98)
mnksdxf (138)
mnpvutr (39)
mnvgaqh (128) -> jntohm, vobeup, ptkqcl
mnwefbn (65)
mofkvq (126) -> ejuiv, abmqz, xqobg
mogwb (84)
moihbcu (75)
mpgixa (110) -> bmmmp, btxepbv
mqhkd (100) -> pjhry, ljhxxd
mqybmn (86)
mrcoxnt (24)
mrigsjh (55)
mrsrl (66)
msfxkn (130) -> ietfhkq, kigdvl
msthql (7)
mszzq (8)
mtcxdod (80)
mttvnpg (9)
mufnw (106) -> yxdld, obkhwze, nkssh
mufrkl (60) -> wyomko, lafoho, rxanas, vlpop, ulvncs, padxpdx
muksdck (48) -> gwtcgyo, tfpuqgs
mupbrv (218) -> phkwq, hrjgaqj, bwvemo
muyodod (19) -> wolet, zzjyw
mvfhc (420) -> wchlcja, ikfihh, ybnvm, cztikzk, qhmyi, uebnns
mwirmq (188) -> mnpvutr, dmvjz
mwztduj (75)
mxusu (45)
myaiu (129) -> pqmrmke, iizbmoz, rhkbrsr, apwsmv
myhrxc (16)
myonh (49)
mzwbtsa (119) -> eceocsy, ecoqyk
navhthp (136) -> rrywqx, vjxmbzm
nbivp (106) -> ndnku, gjcxbx, iqygrur, oxyof
ncfuru (87) -> bcjecw, kybsigz, mtcxdod, ofosgz
nclwgga (201)
nddymc (93) -> ewvvi, netsm
ndnku (44)
ndsub (75)
netsm (53)
nglea (50) -> pfutotv, yrlks
nglji (311) -> cfaniht, anbcmt
nhpcp (34)
njabgq (57)
njdmj (73)
njeff (28)
njrfnvt (96)
nkjgwn (72)
nkskfx (94)
nkssh (38)
nlndxah (11)
nmstp (44)
nmvvgr (34)
nnguamj (71)
nnhsuja (16)
nnxfo (63) -> xffvy, zqmlv, krcoaft, iimfrx
noxvvva (94)
nqvflzq (61)
nrcbc (98)
nrcbij (64) -> pudyrbw, ghdime, xseshzl
nrnmjo (105) -> pzjbbdd, nvvxl
nshbwn (38)
nstdz (65)
ntabiof (365) -> rfohgya, yoqbgjb
nvdouwn (161) -> llibmc, jkfob, dyscpqo
nvlxqp (58)
nvvxl (93)
nzwxd (103) -> wykkwa, oydxsh, bozlg
oasspz (67)
obfet (87) -> iolmgs, piouhkc
obkhwze (38)
ocgkcxp (13)
odckjtb (72)
odkzxae (91)
oejqkp (13)
oelrlp (23)
oenxsfm (275) -> cuhrgp, qlgme, bbhyth, dnzdqz, ezdhr
oeqvt (19) -> grcox, otplae
oewlch (659) -> tgffx, eiwjrxx, ksybvgt
offjbb (15) -> dvoja, jteju, wuybunc, qzpzi
ofidu (349) -> pjxqt, cytlm
ofosgz (80)
ofyxhb (11)
ogvod (1281) -> bihsr, erggh, dqgfb, xguhm
ohcszyk (32)
ohplzu (58)
ohrraic (94)
ohtply (49)
ojhlp (137) -> zqnul, vmvxwar, cgfykiv
ojnziip (73)
ojpok (88)
okmqiy (46)
okseah (78)
oksoj (51)
oktfn (37)
oljci (892) -> asifeu, aoehbj, oqjkafl
olkopyn (66) -> qjcbye, cstgeia, uojcup, ycctk, dkhuccj
omergh (208)
onlwq (59) -> ekxxsqa, jlfho, ekabfx
onogiv (30)
ootidjt (63)
ootkqm (9535) -> uplweb, bdkoa, ehrqn, fpqudx, assuj, rjguqr, jwaskb
opmmmd (32) -> pcodkpi, xhonf
opqoq (648) -> mjlnaz, bymzb, lmqaxz, lageym
opsqjx (71)
oqbfkud (470) -> rnbqhk, mepez, mnksdxf, mjsck, bbfaxid, nglea
oqjkafl (32) -> iwyjkz, auneqme, awccm
oqrmida (222) -> lixqwd, dnalt
osbbt (1214) -> gqmscj, vyriv, bkkop
otplae (91)
ovvrx (84)
owigu (9)
oxcuf (80) -> crobb, xpfxwd
oxyof (44)
oyamsv (38)
oyamw (65)
oybwhs (18)
oydxsh (67)
oyfma (21)
oywob (47) -> ynayo, ixxkvtz
ozfzz (11)
pacsxn (63)
padxpdx (192) -> psvjtka, husmkc
pavwo (1890) -> mofkvq, fmxtg, rijipom, mgqfa
pbxjvnl (15)
pcdjo (63)
pcewixh (109) -> iekurr, xspxxb
pcnroj (2553) -> oljci, losdis, sdnkg, zchulv, crhho
pcodkpi (95)
pddllsa (21)
pddteg (52) -> lwwyx, mhnlgyl, mvfhc, dzggd, opqoq, mufrkl, inghbu
pdmhva (18)
pdxylvu (86) -> etscle, bqtawf
peuppj (29) -> oqrmida, txxnutu, fzqsahw
pfqbht (22)
pfutotv (44)
pgchejz (54) -> ifelr, rdkvtq
phkwq (29)
phmtqf (175) -> aodnlv, jancm
piouhkc (95)
pixmx (4482) -> hrgbkby, bvfcsls, tzvawqb, jfdscql, gqggcxb
pjedtl (55)
pjhry (38)
pjxqt (46)
pjyld (10676) -> zfhxg, oenxsfm, ciogjt, ebmcu, mnfqc, zgqzrc, pzksun
pkoww (39)
pljyyn (73)
plumb (89)
pmfkdn (14)
pmgrf (21)
pnhibed (75) -> gmdsb, gijtd
ppiiyuy (34)
pppxrv (62)
pqmrmke (31)
pqnte (70)
prcjhey (92)
prxseo (16)
psulm (1838) -> rhbouej, urhlfju, obfet
psvjtka (29)
ptkqcl (41)
pttij (68)
pubtsp (70) -> jlvwibm, uvvdw, okmqiy
pudyrbw (76)
puurcu (1689) -> awagc, ajhctd
pwdpe (42) -> leeyi, rhlpt, dtexqt, skpcerk
pweea (51) -> eggmj, clpekkm
pxhwecw (57)
pxihdrd (50)
pxteg (56) -> odkzxae, gcxrx, cotpovw
pxzdv (15)
pygfz (92) -> kledju, upevl
pzewv (23)
pzjbbdd (93)
pzksun (873) -> vyozfv, jxfqev, kbppnh
qbrrjg (14)
qeubhb (65)
qgfstpq (12)
qgvsuqv (206) -> jhgsgy, enbnfw, uflldd, jvhxfl
qhcolun (76)
qhmyi (130) -> dvfuz, scruak
qirjqsm (96)
qjaywg (94) -> khpat, jcpavmj, bchlcqs
qjcbye (535) -> fetkt, pcewixh, vaubjz, ojhlp, mnvgaqh, rcjiwg
qjdpk (28) -> wzxei, jopyit
qjwfsfk (11)
qjzol (15)
qkrydu (1886) -> leyiz, mwirmq, hhwngc
qldijf (16)
qlgme (21) -> ehjnzn, cdbkci
qllluo (57)
qmqrpcl (92)
qngfv (8)
qntstgd (103) -> bbkfiz, zonni
qoiuwmf (1008) -> vbnlfuo, wjyreb, sdbksb, lptkbzc, wopfs, khiom
qonfiro (190) -> cotvk, evqkdq
qorkez (1280) -> euqiok, ibvaekj
qpefm (823) -> kmogwi, ufyavk, evnlr, rmlddp, fticuc
qqishhq (14)
qroirmg (45)
qsqis (1208) -> aovlz, mxusu
qsrpqe (236) -> brztp, kwwsxez
qtgibw (52) -> ovvrx, ziypsz
qunldzi (49)
qvbfob (266) -> oejqkp, ocgkcxp
qvvcx (41)
qwiekvk (65)
qwzac (908) -> uiioczf, qjdpk, ylpuaf
qzakfh (62)
qzcbtes (65)
qzpgle (77) -> gwnipjd, mrcoxnt
qzpzi (54)
qzqyveb (80)
rabxkov (84)
raqjoxn (84)
rawuoi (166) -> dzouqwl, vztyfp, dqgivj, cssov
rayez (17)
rcjiwg (35) -> odckjtb, jlfgvr, tdbne
rcjqzp (65) -> mkyam, apdfe, avzljw, hxgidsw, fkgxak, wzsbsf, woczl
rcjxcou (56)
rcsfkrb (11)
rdhwx (62)
rdkvtq (77)
rdmggka (18)
rdmrzdv (99)
rdnpoms (177) -> eskdbe, fbhidp, xtkxwd
rdrad (6) -> gwyfm, fozyip, uotzz, fmkkz
rdwkvr (38)
rerckg (63)
rfcfgg (28) -> sruyra, bqmqbi, uzuawb
rfdpm (80) -> wcevmtt, tlayc
rfohgya (25)
rhbouej (181) -> udkyxw, rzphpv
rhdudt (83)
rhkbrsr (31)
rhlllw (11)
rhlpt (88)
rhpco (88)
rhzimzq (74) -> drgtn, raqjoxn
rijipom (107) -> ijmfnt, ymduw, vdpmvm, njeff
rjeunph (18)
rjguqr (183) -> fgdqr, ccsrkny
rjnzany (44)
rjxvbkb (52)
rjzrh (360) -> hbkujf, mzwbtsa, oywob, dmxhbe
rljjjo (192) -> sobzsd, ykljt
rmlddp (64) -> rufvv, gxiwcqv, cjcapa, exwxepj, qvbfob, zimrsr, nrcbij
rmtbjn (78) -> lytcy, aiunuvn, hfvhp, dczcz, kqaoir, ekihql, qkrydu
rnbqhk (62) -> rdwkvr, oyamsv
rnddnj (14)
rpoep (38)
rprjk (205)
rqhhyc (214) -> cizehi, sqypc
rqymw (97)
rqzfef (86)
rridl (131) -> nqvflzq, vwotlbl
rrywqx (69)
rsqyvy (99)
rtsajcq (6)
rufvv (162) -> qzcbtes, xekimqs
rugltaa (94)
rulhhsl (90)
ruwzkz (362)
ruxnrix (35)
rxanas (210) -> ctfjb, ifbxvs
rxivjo (206) -> mewof, hrncqs, qgfstpq
rxqfv (84)
rycmr (82)
rythrvz (65)
ryulu (61)
rznnmp (70)
rzphpv (48)
saowgr (367) -> gbnxgny, krmphks, yftjdo, zmpwz
sbdja (16)
scaec (96)
scmiv (54)
scruak (30)
sdbksb (171) -> hbkjjtt, zxson
sdhqlxw (1239) -> eklahxm, ejzeqxz, kabcmf
sdnkg (1381) -> gyutarg, gcwcs, mfjeyx
sdnlegj (207) -> hdlovco, mmerpi
sduuog (9)
setrric (31)
sfrbkzf (45) -> tgmle, mddejh, tulxgem, ofidu, mjaol, dhqzt
sgieno (107) -> miijab, zryrfnw
sjiel (238)
skjtvyz (18)
skkatyg (20)
skpcerk (88)
slhitu (27)
slrfd (340) -> etwwy, qldijf
smmgkir (31)
sobzsd (13)
sofve (139)
sqiac (24)
sqypc (7)
srneoo (11) -> dhlrq, ivwcuc, laxoeu
sruyra (47)
sslltlv (45)
stiln (72)
stkodp (84)
swpfak (21)
swrkuc (199) -> gylsj, cyzzsc, blmfs, aonfaf
swurfm (64)
syyfs (35)
sztqzfl (98)
szutvca (32)
tatubv (205)
tceog (70)
tcghqr (43) -> mnhojtk, ruwzkz, veksns, wrochvi, uycjl, umtfn, qgvsuqv
tchbf (93)
tdbne (72)
tdniuai (39)
tetdx (224) -> nshbwn, rpoep, fbqpk
tfdbdq (22)
tfhdccw (93)
tfpuqgs (24)
tgblta (141) -> elmog, woves
tgffx (75) -> kstvq, cjmfqbo
tgfgem (33)
tgkusb (32)
tglnkgk (81) -> wrxiwgy, wrfxdc
tgmle (73) -> prcjhey, thzwwh, cxhipq, tgvpi
tgujvov (59) -> rhpco, ojpok, trbnpf
tgvpi (92)
tgyavjg (18)
thqkxpl (38)
thzwwh (92)
thzyz (77)
tifqyde (2264) -> koxiwk, psulm, rcjqzp
tijkvua (18)
tjffhqh (84)
tjhmz (51)
tjpatnk (44)
tknmww (92)
tlayc (77)
tlfsn (21)
tlvkwlx (133) -> fjpgybt, miftchq, oyfma, ytivjxk
tmyhhql (51)
tnayomw (62)
tohdgsa (30)
tohrp (65)
trbnpf (88)
tremw (94)
ttnnyy (92) -> lhsccbq, dpdjpal
tuekps (169)
tuieolg (7624) -> ldnrw, cfuqhip, rjzrh
tulxgem (213) -> mabkbom, btcjg, ktazkb, evcdf
tvnco (63)
twvib (18)
txapm (272) -> isggu, yookz
txkgx (60)
txxnutu (97) -> bcyarwn, uteosk, kjjyu
tygnc (13) -> ucxedq, jgwvp, kgevjdx
tygwtg (25)
tywzhc (243)
tzmndkd (221) -> lixsvp, ofyxhb
tzntd (59)
tznwmc (1199) -> dnfvldg, dbufjl, pnhibed
tzrppo (51) -> tfhdccw, kbses, jlbcwrl, efsrz
tzvawqb (1010) -> qirjqsm, muksdck, oxcuf
tzzdbi (8)
uadnb (88)
ubgrma (1059) -> ymhxg, yvxuom, aeyykn
ucfhxsv (65)
ucqdz (25)
ucxedq (84)
udkyxw (48)
uduan (75)
uebnns (127) -> iteizf, lzxrfk, tlfsn
uflldd (39)
ufyavk (1838) -> vunam, kmarvbs, kzdugfh
ufyqf (77)
ugjzag (24)
uiioczf (130)
uiwaf (97)
ujjpxe (56)
ujktzrv (71)
ukghke (28)
ukkaxy (211)
ulvncs (172) -> bexvn, jzsmy
umtfn (80) -> hbylau, dzrkq, rugltaa
unvje (71)
uobgj (488) -> akidv, sofve, wblhx
uojcup (985) -> ttnnyy, yekjlfd, pdxylvu, fjzpjk, mqhkd, ibiwh
uotzz (61) -> xyxtm, cdpfk, qmqrpcl
upevl (95)
uplweb (127) -> bpzxjg, utivde
uqvyau (6)
urhlfju (249) -> csqfv, rnddnj
urjwj (78)
ursjc (45)
usodrg (53)
uteosk (65)
utgxfsh (959) -> mupbrv, borbd, jmieet
utivde (62)
uvmqarq (751) -> muyodod, nclwgga, oeqvt
uvsny (44)
uvvdw (46)
uwhjd (94)
uxrrjqx (205)
uycjl (292) -> xcqvne, ruxnrix
uyrght (80) -> hvcii, lxhkgs
uyrwi (11)
uzjejte (48)
uzjxd (196) -> zfnoo, wlaslo, tijkvua
uzsytm (45)
uzuawb (47)
vaubjz (233) -> erfnrn, gqzva, goxfpk
vbnlfuo (169) -> pppxrv, rdhwx
vcvypf (113) -> mttvnpg, sduuog
vdbihjp (69)
vdjmhb (39)
vdkxk (90) -> hrvztx, fjhqmnv
vdpmvm (28)
vdvadz (38)
veggtf (104) -> wnyxznj, mnwefbn, fhzhqie
veksns (308) -> slhitu, lghzki
vflyupn (34)
vhmijln (97) -> tmyhhql, ykpdiav
vhrtptr (139) -> bpqhqbg, pacsxn
vhxlart (70)
vifwkwa (173) -> zvwkjew, txkgx, vvqpffs
vipurf (15)
viufoq (25) -> bekxoxk, wmaywuo
vjxmbzm (69)
vleydj (173) -> mhydkla, msthql
vlmhyer (25)
vlpop (64) -> hshyx, tchbf
vmmjgy (742) -> vdkxk, yhyxv, cpfbmv
vmvxwar (38)
vobeup (41)
vohta (58)
vonzkut (76) -> bdafpm, nvlxqp, gxsbt
vprkzya (37)
vpynuf (214) -> akpnwc, rulhhsl
vrfkofp (49)
vscjrx (79)
vtvnn (114) -> uadnb, huunb
vuetjdb (157) -> pbxjvnl, jdzbqlz, xhnmlcw, vipurf
vunam (90)
vuyeiv (65)
vvqpffs (60)
vwbjuvx (99)
vwcygm (36)
vwojb (97) -> qeubhb, kkdaw, ucfhxsv, rythrvz
vwotlbl (61)
vxgwku (16)
vyozfv (99)
vyriv (50) -> vwbjuvx, xergqq, wlpfcsr
vzqnfs (31)
vztyfp (57)
wblhx (97) -> xayglgm, pddllsa
wcevmtt (77)
wchlcja (190)
wchxl (67)
wdjzjlk (1631) -> iplyhhc, pgchejz, kwmam
wdybaj (6)
wenii (79) -> qsrpqe, zdhqhh, jpenh, hwrxn, vtvnn, mpgixa, fbjbwv
wewzb (164) -> yzptgez, ctytfj
wfdlusw (49)
wfovakv (48) -> lppvxfk, tznwmc, utgxfsh, zyympz, asbzj, ijcojo
wgeig (15)
wgypwo (290) -> btgrhku, aqkdlo
whnjtp (146) -> zswyy, bmugsve
wiayzvp (28)
witovp (6)
wjyreb (41) -> rabxkov, rxqfv, gcomv
wkhggv (25)
wlajxb (201) -> tgyavjg, eszxg
wlaslo (18)
wlpfcsr (99)
wltpv (260) -> nlndxah, etyyw
wlufwnr (89)
wmaywuo (87)
wndpfac (55)
wnyxznj (65)
woczl (60) -> okseah, afeqhu, cnnrj, cmaxybh
wolet (91)
wonxzkm (57)
wopfs (159) -> oasspz, zgssy
wouprxh (28)
woves (32)
wpdbejb (90)
wpnqifq (11)
wpoga (57)
wqbhby (15)
wqoucl (99)
wrfxdc (25)
wrochvi (150) -> kifer, xaifomj, usodrg, jqkaucw
wrxiwgy (25)
wryfov (57)
wszghwt (160) -> brcpgz, wryfov
wtyfb (238)
wuybunc (54)
wxdpcvv (8)
wxixtqj (37)
wydbqai (65) -> ryulu, ydumax
wykkwa (67)
wyomko (184) -> tgfgem, clnkvox
wzsbsf (222) -> mwztduj, hkpvwpa
wzxei (51)
xaatl (56147) -> dgjls, qoiuwmf, koane, fnoteku, pavwo, hpowmso, yehxck
xaifomj (53)
xatyg (71)
xayglgm (21)
xbucnh (11)
xbyjur (14)
xcqvne (35)
xcqwjrm (63)
xejner (239) -> jmlznjh, foyfb, pxihdrd
xekimqs (65)
xeomb (44) -> vuyeiv, bwrpskq, qwiekvk, gxzkde
xergqq (99)
xevhcxq (86)
xffvy (59)
xfydt (87)
xguhm (102) -> syyfs, hpeaki, fynniwm
xhnmlcw (15)
xhonf (95)
xhyqtqz (77) -> swrkuc, ncfuru, kazqnjr
xjcprt (87)
xmvbzka (49)
xpfxwd (8)
xpker (36)
xqgwwr (23)
xqobg (31)
xrhsy (266) -> qbrrjg, juptypm, bugwblt
xrxseqy (94)
xseshzl (76)
xspxxb (71)
xtkxwd (17)
xulwh (71)
xumsm (16)
xwltxk (2001) -> yirnxk, baawtw, msfxkn
xyxtm (92)
ybnvm (50) -> dwpqell, fmtyy, bkcghv, ekzvjj
ycacj (25)
ycbgx (1531) -> tzmndkd, fpynzz, tywzhc
ycctk (1381) -> qtgibw, lkorngt, mufnw
ydqjoa (84)
ydumax (61)
yehxck (2391) -> boygd, kayqqz, iajslqp
yekjlfd (106) -> ecjdzpq, dcmxxd
yetcvhx (71)
yfruc (303) -> pmgrf, hsfjd
yftjdo (12)
ygmhxm (129) -> pljyyn, njdmj
ygurya (66)
ygvol (202) -> mszzq, tzzdbi
yhpiqn (99)
yhyxv (160) -> ahmitv, ozfzz, zcdzv, rhlllw
yhzuh (72)
yirnxk (158) -> lgefkp, rayez
yjakrqa (70)
yjomyth (97) -> oksoj, lmwrf, tjhmz
yjxyb (77) -> tceog, pqnte, yxxpgv, aokpx
ykljt (13)
ykpdiav (51)
ykruy (39)
ylpuaf (64) -> mdzkkjf, tfdbdq, kiauwpn
ylyef (30)
ymduw (28)
ymhxg (48) -> vohta, ohplzu, edpjix
ynayo (71)
yonjpz (62)
yookz (5)
yoqbgjb (25)
ypfsjd (60) -> rdmrzdv, yhpiqn, cbyvzkp
ypqxs (31)
ypsme (11966) -> zfkfhfn, fiufzkb, ubgrma, puurcu
yqnihs (56) -> wqoucl, rsqyvy, zetvslt
yrlks (44)
ysigfem (177)
ytivjxk (21)
ytspbx (184) -> nkskfx, ohrraic
yurfpj (65)
yvhilh (89)
yvxuom (154) -> jbbmcxg, ppiiyuy
ywvmghy (63)
yxdld (38)
yxkldyi (90)
yxtjx (74)
yxxpgv (70)
yzptgez (29)
zavef (69)
zbcra (38) -> rjeunph, edkigpl
zcdzv (11)
zcgfj (78)
zchulv (72) -> cmxulaj, tetdx, huhoda, blagy, wgypwo
zdgwmi (24)
zdhqhh (200) -> ylyef, onogiv, tohdgsa
zelucu (66)
zetvslt (99)
zfhwfsw (53)
zfhxg (345) -> srneoo, ygmhxm, epumc
zfkfhfn (33) -> txapm, pygfz, ekszr, nbivp, wltpv, jsjaxjk
zfnoo (18)
zgimdwb (107) -> znucug, mrigsjh
zgqzrc (459) -> wlajxb, mfywm, jqmlxr
zgssy (67)
zhbiaq (45) -> rqzfef, kplegas, ayejq, xevhcxq
zhopeqm (80)
zimrsr (223) -> dxympe, fhpaqmd, ayury
ziypsz (84)
zjgok (23)
zjzoo (65)
zksmijj (189) -> zsvuw, hjjfdj
zktnjab (87)
zlgpmfs (143) -> ilxfa, nhpcp
zmlmsuf (23)
zmpwz (12)
zmqom (42) -> grazu, yxkldyi
zneumoh (80)
znucug (55)
zonni (11)
zorvynv (176) -> mqybmn, jaxidl
zotwsb (170) -> wlufwnr, frksv
zpntow (72)
zqmlv (59)
zqnmsyb (73)
zqnul (38)
zqtkn (79) -> ugjzag, dtzyg
zrnlo (42)
zrpqdzn (62)
zryrfnw (49)
zsvuw (11)
zswyy (36)
zunhob (79)
zvwkjew (60)
zworz (41633) -> ootkqm, wfovakv, inldh
zwsrt (2544) -> xmvbzka, egrfvic, fovkc
zxkvs (12) -> bclicjl, yfruc, axikbt, nglji
zxson (61)
zybeuh (197) -> wonxzkm, jzuvrtp
zyniqni (147) -> khqhd, zrnlo
zyympz (887) -> pxteg, amnoi, amzwex
zzjyw (91)"""
weights = {}
towers = {}
for line in str.splitlines(inputs):
    line_split = line.split(" -> ")
    name, weight = line_split[0].split(" ")
    weights[name] = int(weight[1:-1])
    if len(line_split) > 1:
        towers[name] = line_split[1].split(", ")
    else:
        towers[name] = []
root_key = ""
for k, v in towers.items():
    if inputs.count(k) == 1:
        root_key = k

towers = build_tree(towers, root_key)
print(build_tree_weights(towers))
