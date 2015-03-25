from math import sqrt

def fraction(a,b,c,d):
    return (float(a+b))/(float(c+d)) 

def total_error(a,b,c,d):
    frac = fraction(a,b,c,d)
    sigmaA_overA = (sqrt(a+b)/(a+b))**2
    sigmaB_overB = (sqrt(c+d)/(c+d))**2
    squareroot = sqrt(sigmaA_overA + sigmaB_overB)

    answer = frac * squareroot
    return answer

#The first and 2nd numbers are numerator's We,Wm or Zee,Zmm and the third and fourth numbers are the denominator's We,Wm or Zee,Zmm

group1 = float(fraction(105709,124759,105638,124083)) #ZHhadhad selection 0505/11
error1 = float(total_error(105709,124759,105638,124083))

group2 = float(fraction(106041,123727,105638,124083)) #ZHhadhad selection 051/11
error2 = float(total_error(106041,123727,105638,124083))

group3 = float(fraction(105484,123994,105638,124083)) #ZHhadhad selection 105/11
error3 = float(total_error(105484,123994,105638,124083))

group4 = float(fraction(105981,124946,105638,124083)) #ZHhadhad selection 12/11
error4 = float(total_error(105981,124946,105638,124083))

group5 = float(fraction(105293,124970,105638,124083)) #ZHhadhad selection 21/11
error5 = float(total_error(105293,124970,105638,124083))

group6 = float(fraction(105265,124345,105638,124083)) #ZHhadhad selection 22/11
error6 = float(total_error(105265,124345,105638,124083))

########################
group7 = float(fraction(106642,125159,105613,124932)) #ZHlephad selection 0505/11
error7 = float(total_error(106642,125159,105613,124932))

group8 = float(fraction(106099,125005,105613,124932)) #ZHlephad selection 051/11
error8 = float(total_error(106099,125005,105613,124932))

group9 = float(fraction(106509,125399,105613,124932)) #ZHlephad selection 105/11
error9 = float(total_error(106509,125399,105613,124932))

group10 = float(fraction(106205,124926,105613,124932)) #ZHlephad selection 12/11
error10 = float(total_error(106205,124926,105613,124932))

group11 = float(fraction(106215,124637,105613,124932)) #ZHlephad selection 21/11
error11 = float(total_error(106215,124637,105613,124932))

group12 = float(fraction(106180,125065,105613,124932)) #ZHlephad selection 22/11
error12 = float(total_error(106180,125065,105613,124932))


######################
group13 = float(fraction(106213,114913,105832,114971)) #WHhadhad selection 0505/11
error13 = float(total_error(106213,114913,105832,114971))

group14 = float(fraction(106213,114624,105832,114971)) #WHhadhad selection 051/11
error14 = float(total_error(106213,114624,105832,114971))

group15 = float(fraction(105915,114688,105832,114971)) #WHhadhad selection 105/11
error15 = float(total_error(105915,114688,105832,114971))

group16 = float(fraction(105849,114181,105832,114971)) #WHhadhad selection 12/11
error16 = float(total_error(105849,114181,105832,114971))

group17 = float(fraction(105921,114727,105832,114971)) #WHhadhad selection 21/11
error17 = float(total_error(105921,114727,105832,114971))

group18 = float(fraction(105669,114532,105832,114971)) #WHhadhad selection 22/11
error18 = float(total_error(105669,114532,105832,114971))

###########################
group19 = float(fraction(52591,56459,52013,57171)) #WHlephad selection 0505/11
error19 = float(total_error(52591,56459,52013,57171))

group20 = float(fraction(51938,56711,52013,57171)) #WHlephad selection 051/11
error20 = float(total_error(51938,56711,52013,57171))

group21 = float(fraction(52123,56637,52013,57171)) #WHlephad selection 105/11
error21 = float(total_error(52123,56637,52013,57171))

group22 = float(fraction(51993,56937,52013,57171)) #WHlephad selection 12/11
error22 = float(total_error(51993,56937,52013,57171))

group23 = float(fraction(51888,56358,52013,57171)) #WHlephad selection 21/11
error23 = float(total_error(51888,56358,52013,57171))

group24 = float(fraction(52108,56401,52013,57171)) #WHlephad selection 22/11
error24 = float(total_error(52108,56401,52013,57171))



print 'ZHhh 0505/11:   %f +- %f' % (group1,error1)
print 'ZHhh 051/11:    %f +- %f' % (group2,error2)
print 'ZHhh 105/11:    %f +- %f' % (group3,error3)
print 'ZHhh 12/11:     %f +- %f' % (group4,error4)
print 'ZHhh 21/11:     %f +- %f' % (group5,error5)
print 'ZHhh 22/11:     %f +- %f' % (group6,error6)
print 'ZHlh 0505/11:   %f +- %f' % (group7,error7)
print 'ZHlh 051/11:    %f +- %f' % (group8,error8)
print 'ZHlh 105/11:    %f +- %f' % (group9,error9)
print 'ZHlh 12/11:     %f +- %f' % (group10,error10)
print 'ZHlh 21/11:     %f +- %f' % (group11,error11)
print 'ZHlh 22/11:     %f +- %f' % (group12,error12)
print 'WHhh 0505/11:   %f +- %f' % (group13,error13)
print 'WHhh 051/11:    %f +- %f' % (group14,error14)
print 'WHhh 105/11:    %f +- %f' % (group15,error15)
print 'WHhh 12/11:     %f +- %f' % (group16,error16)
print 'WHhh 21/11:     %f +- %f' % (group17,error17)
print 'WHhh 22/11:     %f +- %f' % (group18,error18)
print 'WHlh 0505/11:   %f +- %f' % (group19,error19)
print 'WHlh 051/11:    %f +- %f' % (group20,error20)
print 'WHlh 105/11:    %f +- %f' % (group21,error21)
print 'WHlh 12/11:     %f +- %f' % (group22,error22)
print 'WHlh 21/11:     %f +- %f' % (group23,error23)
print 'WHlh 22/11:     %f +- %f' % (group24,error24)
