import numpy as np
import cv2


import HoughTransform.RunLengthEncoding
import StaffLineRemoval
import ClassifiedTypeChord
import ChordType
import CreateStaff
import CombineOpenClose

#feature_type = ["black_chord","double close","double open","single close","single open","white_chord"]
color = [(0,0,255),(0,255,0),(0,255,255),(255,0,0),(204,0,102),(0,0,0)] # red, green, yellow, blue, purple, black

feature_type = ChordType.root

img = cv2.imread("sheet_4.jpg")

clef_sol = cv2.imread("chord.jpg")
lines, staff_height = HoughTransform.RunLengthEncoding.DrawLine(False,img)
removal = StaffLineRemoval.StaffLineRemoval(img)
print("Staff_Height",staff_height)

staffs = CreateStaff.initStaff(lines)

print(staffs)
#
chordsType = ClassifiedTypeChord.inputLabel(feature_type,color,removal,img)
for i in range(len(chordsType)):
    print(chordsType[i].type,chordsType[i].sub_type," : ",chordsType[i].pt1 )

onlyChord = []
for i in range(len(chordsType)):
    if(chordsType[i].type==1 or chordsType[i].type==4 ):
        onlyChord.append(chordsType[i])

onlySymbol = []
for i in range(len(chordsType)):
    if(chordsType[i].type==2 or chordsType[i].type==3 ):
        onlySymbol.append(chordsType[i])


CreateStaff.groupNoteToStaff(onlyChord,staffs)
CreateStaff.groupSymbolToStaff(onlySymbol,staffs)


# print("Sucessfully write result....")
#
blackChord, singleChord, doubleChord = CombineOpenClose.getCombinedType(staffs, img)
#
#
# pt_clef1, pt_clef2 = ClassifiedTypeChord.addFeature(clef_sol,removal)
# h_clef = cv2.cvtColor(clef_sol,cv2.COLOR_BGR2GRAY)
# h_clef = clef_sol.shape[0]
# #
# #
# #
# # # for pt in pt_clef1:
# # #     for i in range(pt[1],h_clef+pt[1],1):
# # #         for line in lines:
# # #             if(i==line):
# # #                 cv2.line(img, (-1000, line), (1000, line), (127, 127, 127), 1)
# #
# # # # Lines:
# # # for line in lines:
# # #         cv2.line(img, (-1000, line), (1000, line), (255,255,255), 1)
# #
# #
# #
# notes_height = ["mi_1", "re_1", "do_1", "si", "la", "son", "fa", "mi","re", "do", "si-1", "la-1" ]
# notes_height_1 = ["mi_1", "fa_1", "son_1", "la_1", "si_1", "do_2", "re_2", "mi_2", "fa_2", "son_2", "la_2", "si_2"]
# #
# staffline_dist = lines[1] - lines[0] # blank size between 2 lines in one staff
# print("StaffLine distance: ",staffline_dist)
#
# def RoundNumber(num):
#     sign = num / (abs(num))
#     standard = (int(abs(num)) + 0.5)
#     if abs(num) > standard:
#         return (int(num) + int(sign))
#     else:
#         return (int(num))
#
#
# height = []
# for k in range(len(staffs)):
#     temp = []
#     for chord in (staffs[k].chords):
#         anchorPoint = chord.pt1
#         temp.append(RoundNumber((-staffs[k].lines[0] + anchorPoint[1])/(staffline_dist/2)))
#     height.append(temp)
# #print(height)
#
# result = []
# count = 0
# for i in height:
#     temp = []
#     for j in i:
#         count+=1
#         print(count)
#         if j <0:
#             print(abs(j))
#             print(notes_height_1[abs(j)])
#             temp.append(notes_height_1[abs(j)])
#         else:
#             # print(abs(j))
#             # print(j)
#             print(notes_height[j])
#             temp.append(notes_height[j])
#     result.append(temp)
# for i in result:
#     print(i)
#
cv2.imshow("IMG",img)
cv2.waitKey(0)