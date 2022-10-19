#############################################
# Ask user if they want to process a triangle
# if yes, the user will input the triangle sides
#   if the triangle is not valid, it will warn the user
#   and ask if they want to retry
#  do math and print out the properties of the triangle
#   including angle, radian, area, perimeter\
#   and the kind of triangle it is
#   if succesful, add 1 to valid and ask if they want\
#   to process another triangle
#  when the user input "n", the program breaks and\
#  print out the total of valid triangles been processed
#   
# if no exit the program


import math


BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
print()
valid = 0
another_triangle = "Do you wish to process another triangle? (Y or N) "
proceed = input("Do you wish to process a triangle (Y or N)?  ").lower()
while True:
    if proceed == "n":
        break
    else:
        AB = float(input("\nEnter length of side AB: "))
        BC = float(input("\nEnter length of side BC: "))
        CA = float(input("\nEnter length of side CA: \n"))
        if (AB + BC >= CA) and (BC + CA >= AB) and (AB + CA >= BC): # valid?
            if (AB <= BC) and (BC <= CA) and ((AB + BC == CA) or\
                 (BC - CA == AB) or (AB - CA ==-(BC))): # deformed?
                print("\n  Degenerate Triangle")
                proceed =  input(f"\n{another_triangle}").lower()
            else:
                print("\n  Valid Triangle\n")

                print("  Triangle sides:")
                print(f"    Length of side AB: {AB}") 
                print(f"    Length of side BC: {BC}")
                print(f"    Length of side CA: {CA}")

                print(f"\n  Degree measure of interior angles:")
                #using law of cosine
                c_radian = ((BC**2+CA**2-AB**2)) 
                c_radian /= (2*BC*CA)
                c_radian = math.acos(c_radian)

                a_radian = ((CA**2+AB**2-BC**2))
                a_radian /= (2*CA*AB)
                a_radian = math.acos(a_radian)

                b_radian = ((AB**2+BC**2-CA**2))
                b_radian /= (2*AB*BC)
                b_radian = math.acos(b_radian)
                
                a_degree = math.degrees(a_radian)
                a_degree = round(a_degree, 1)

                b_degree = math.degrees(b_radian)
                b_degree = round(b_degree,1)

                c_degree = math.degrees(c_radian)
                c_degree = round(c_degree,1)

                print(f"    Angle A: {a_degree}")
                print(f"    Angle B: {b_degree}")
                print(f"    Angle C: {c_degree}\n")

                print("  Radian measure of interior angles:")
                print(f"    Angle A: {a_radian:.1f}")
                print(f"    Angle B: {b_radian:.1f}")
                print(f"    Angle C: {c_radian:.1f}\n")

                perimeter = AB + BC + CA
                # heron's formula
                area = math.sqrt((4*AB**2*BC**2) - 
                    ((AB**2 + BC**2 - CA**2)**2)) 
                area /= 4 

                print("  Perimeter and Area of triangle:")
                print(f"    Perimeter of triangle: {perimeter}")
                print(f"    Area of triangle: {abs(area):.1f}\n") #real number

                print("  Types of triangle:")

                if AB != BC and AB != CA and BC != CA:
                    print("    Scalene Triangle") 

                if AB == BC or BC == CA or AB == CA:
                    print("    Isosceles Triangle")

                if AB == BC == CA:
                    print("    Equilateral Triangle")
               
                if a_degree == 90 or b_degree == 90 or c_degree == 90:
                    print("    Right Triangle")
                else:
                    print("    Oblique Triangle")
                
                if a_degree > 90 or b_degree > 90 or c_degree > 90:
                    print("    Obtuse Triangle")

                valid +=1
                proceed =  input(f"\n{another_triangle}").lower()

        else:
            print("\n  Not a Triangle")
            proceed =  input(f"\n{another_triangle}").lower()

print("\nNumber of valid triangles:",valid)