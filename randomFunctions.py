class multipleFunctions():
    def SubfieldsInAI():
        subfields=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for subfield in subfields:
            print(subfield)
            
    def oddEven():
        num=int(input("Enter a number: "))
        if((num%2)==1):
            print(num,"is Odd Number")     
        else:
            print(num,"is Even Number")

    def EligibilityForMarriage():
        gender=input("Your Gender(Male/Female): ").strip().lower()
        age=int(input("Your Age: "))
        if((gender=="male" and age>=21) or (gender=="female" and age>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
    def FindPercent():
        subject1=int(input("Subject1= "))
        subject2=int(input("Subject2= "))
        subject3=int(input("Subject3= "))
        subject4=int(input("Subject4= "))
        subject5=int(input("Subject5= "))
        total=subject1+subject2+subject3+subject4+subject5
        percentage=total/5.0
        print("Total: ",total)
        print("Percentage : ",percentage)
        
    def AreaPerimeter():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        area=(height*breadth)/2.0
        print("Area of Triangle: ",area)
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=height1+height2+Breadth
        print("Perimeter of Triangle: ",perimeter)
    