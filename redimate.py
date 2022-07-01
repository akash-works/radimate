#  fuction whicj return the specification of garment
def undergarmentshop (size,brand,gender,color,price):
    brands = ["VIP","Rupa","Tantex","Crystal","Amul","Dollar Big Boss","Dixcy"]
    colors = ["Red","Blue","Green","Brown","Blank","White"]
    sizes =  ["S","M","L","XL","XXL"]
    for i in brands:
        if i==brand:
            for color in colors:
                if color==color:
                    for size in sizes:
                        if size==size:

                            return print(
                                f"""
                                gender - {gender}
                                brand Name - {i}
                                size - {size}
                                color - {color}
                                price - {price}
                                """
                            )

            
while True:
    gender = str(input("please selecrt your gender:"))
    print(
        """
        1  for "VIP",
        2 for "Rupa",
        3 for "Tantex",
        4 for "Crystal",
        5 for "Amul",
        6 for "Dollar Big Boss",
        7 for "Dixcy"
        """
    )
    user_input = int(input("please select brand which do you want:"))
    print("""
        1 for "Blue"
        2 for "Green"
        3 for "Brown",
        4 for "Black",
        5 for "White"
    """)
    color = int(input("please select brand which do you want:"))
    print("""
        1 for "S"
        2 for "M"
        3 for "L",
        4 for "Xl",
        5 for "XXL"
        
    """)
   
    size  =  int(input("please select brand which do you want:"))
    if user_input==1 and color==1 and size==1:
        brand = "VIP"
        color = "Blue"
        size = "S"
        gender = gender
        price = 100
    elif user_input==2 and color==1 and size==1:
        brand = "Rupa"
        color = "Blue"
        size = "S"
        gender = gender
        price = 150
    elif user_input==3 and color==1 and size==1:
        brand = "Tantex"
        color = "Blue"
        size = "S"
        gender = gender
        price = 200
    elif user_input==4 and color==1 and size==1:
        brand = "Amul"
        color = "Blue"
        size = "S"
        gender = gender
        price = 200
    elif user_input==5 and color==1 and size==1:
        brand = "Dollar Big Boss"
        color = "Blue"
        size = "S"
        gender = gender
        price = 200    
    elif user_input==6 and color==1 and size==1:
        brand = "Dixcy"
        color = "Blue"
        size = "S"
        gender = gender
        price = 200
    
    

    elif user_input==1 and color==1 and size==2:
        brand = "VIP"
        color = "Blue"
        size = "M"
        gender = gender
        price = 200

    elif user_input==2 and color==1 and size==2:
        brand = "Rupa"
        color = "Blue"
        size = "M"
        gender = gender
        price = 150

    elif user_input==3 and color==1 and size==2:
        brand = "Tantex"
        color = "Blue"
        size = "M"
        gender = gender
        price = 200

    elif user_input==4 and color==1 and size==2:
        brand = "Amul"
        color = "Blue"
        size = "M"
        gender = gender
        price = 200

    elif user_input==5 and color==1 and size==2:
        brand = "Dollar Big Boss"
        color = "Blue"
        size = "M"
        gender = gender
        price = 200            

    elif user_input==6 and color==1 and size==2:
        brand = "Dixcy"
        color = "Blue"
        size = "M"
        gender = gender
        price = 200
    
    elif user_input==1 and color==1 and size==3:
        brand = "VIP"
        color = "Blue"
        size = "L"
        gender = gender
        price = 200
    
    elif user_input==2 and color==1 and size==3:
        brand = "Rupa"
        color = "Blue"
        size = "L"
        gender = gender
        price = 150

    elif user_input==3 and color==1 and size==3:
        brand = "Tantex"
        color = "Blue"
        size = "L"
        gender = gender
        price = 200

    elif user_input==4 and color==1 and size==3:
        brand = "Amul"
        color = "Blue"
        size = "L"
        gender = gender
        price = 200
    elif user_input==5 and color==1 and size==3:
        brand = "Dollar Big Boss"
        color = "Blue"
        size = "L"
        gender = gender
        price = 200  
    elif user_input==6 and color==1 and size==3:
        brand = "Dixcy"
        color = "Blue"
        size = "L"
        gender = gender
        price = 200

    elif user_input==1 and color==1 and size==4:
        brand = "VIP"
        color = "Blue"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==2 and color==1 and size==4:
        brand = "Rupa"
        color = "Blue"
        size = "XL"
        gender = gender
        price = 150
    elif user_input==3 and color==1 and size==4:
        brand = "Tantex"
        color = "Blue"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==4 and color==1 and size==4:
        brand = "Amul"
        color = "Blue"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==5 and color==1 and size==4:
        brand = "Dollar Big Boss"
        color = "Blue"
        size = "XL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==1 and size==4:
        brand = "Dixcy"
        color = "Blue"
        size = "XL"
        gender = gender
        price = 200
    
    elif user_input==1 and color==2 and size==5:
        brand = "VIP"
        color = ""
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==2 and color==1 and size==5:
        brand = "Rupa"
        color = "Blue"
        size = "XXL"
        gender = gender
        price = 150
    elif user_input==3 and color==1 and size==5:
        brand = "Tantex"
        color = "Blue"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==4 and color==1 and size==5:
        brand = "Amul"
        color = "Blue"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==5 and color==1 and size==5:
        brand = "Dollar Big Boss"
        color = "Blue"
        size = "XXL"
        gender = gender
        price = 200  
    elif user_input==6 and color==1 and size==5:
        brand = "Dixcy"
        color = "Blue"
        size = "XXL"
        gender = gender
        price = 200

    elif user_input==1 and color==2 and size==1:
        brand = "VIP"
        color = "Green"
        size = "S"
        gender = gender
        price = 200
    elif user_input==2 and color==2 and size==1:
        brand = "Rupa"
        color = "Green"
        size = "S"
        gender = gender
        price = 150
    elif user_input==3 and color==2 and size==1:
        brand = "Tantex"
        color = "Green"
        size = "S"
        gender = gender
        price = 200
    elif user_input==4 and color==2 and size==1:
        brand = "Amul"
        color = "Green"
        size = "S"
        gender = gender
        price = 200
    elif user_input==5 and color==2 and size==1:
        brand = "Dollar Big Boss"
        color = "Blue"
        size = "S"
        gender = gender
        price = 200                      
    elif user_input==6 and color==2 and size==1:
        brand = "Dixcy"
        color = "Blue"
        size = "S"
        gender = gender
        price = 200
    elif user_input==1 and color==2 and size==2:
        brand = "VIP"
        color = "Green"
        size = "M"
        gender = gender
        price = 200
    elif user_input==2 and color==2 and size==2:
        brand = "Rupa"
        color = "Green"
        size = "M"
        gender = gender
        price = 150
    elif user_input==3 and color==2 and size==2:
        brand = "Tantex"
        color = "Green"
        size = "M"
        gender = gender
        price = 200        
    elif user_input==4 and color==2 and size==2:
        brand = "Amul"
        color = "Green"
        size = "M"
        gender = gender
        price = 200
    elif user_input==5 and color==2 and size==2:
        brand = "Dollar Big Boss"
        color = "Green"
        size = "M"
        gender = gender
        price = 200 
    elif user_input==6 and color==2 and size==2:
        brand = "Dixcy"
        color = "green"
        size = "M"
        gender = gender
        price = 200   


    elif user_input==1 and color==2 and size==3:
        brand = "VIP"
        color = "Green"
        size = "L"
        gender = gender
        price = 200      
    elif user_input==2 and color==2 and size==3:
        brand = "Rupa"
        color = "Green"
        size = "L"
        gender = gender
        price = 150
    elif user_input==3 and color==2 and size==3:
        brand = "Tantex"
        color = "Green"
        size = "L"
        gender = gender
        price = 200                
    elif user_input==4 and color==2 and size==3:
        brand = "Amul"
        color = "Green"
        size = "L"
        gender = gender
        price = 200
    elif user_input==5 and color==2 and size==3:
        brand = "Dollar Big Boss"
        color = "Green"
        size = "L"
        gender = gender
        price = 200  
    elif user_input==6 and color==2 and size==3:
        brand = "Dixcy"
        color = "green"
        size = "L"
        gender = gender
        price = 200                 
    elif user_input==1 and color==2 and size==4:
        brand = "VIP"
        color = "Green"
        size = "XL"
        gender = gender
        price = 200      
    elif user_input==2 and color==2 and size==4:
        brand = "Rupa"
        color = "Green"
        size = "XL"
        gender = gender
        price = 150
    elif user_input==3 and color==2 and size==4:
        brand = "Tantex"
        color = "Green"
        size = "XL"
        gender = gender
        price = 200                
    elif user_input==4 and color==2 and size==4:
        brand = "Amul"
        color = "Green"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==5 and color==2 and size==4:
        brand = "Dollar Big Boss"
        color = "Green"
        size = "XL"
        gender = gender
        price = 200  
    elif user_input==6 and color==2 and size==4:
        brand = "Dixcy"
        color = "green"
        size = "XL"
        gender = gender
        price = 200                 
    elif user_input==1 and color==2 and size==5:
        brand = "VIP"
        color = "Green"
        size = "XXL"
        gender = gender
        price = 200      
    elif user_input==2 and color==2 and size==5:
        brand = "Rupa"
        color = "Green"
        size = "XXL"
        gender = gender
        price = 150
    elif user_input==3 and color==2 and size==5:
        brand = "Tantex"
        color = "Green"
        size = "XL"
        gender = gender
        price = 200                
    elif user_input==4 and color==2 and size==5:
        brand = "Amul"
        color = "Green"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==5 and color==2 and size==5:
        brand = "Dollar Big Boss"
        color = "Green"
        size = "XXL"
        gender = gender
        price = 200  
    elif user_input==6 and color==2 and size==5:
        brand = "Dixcy"
        color = "green"
        size = "XXL"
        gender = gender
        price = 200 

    elif user_input==1 and color==3 and size==1:
        brand = "VIP"
        color = "Brown"
        size = "S"
        gender = gender
        price = 200
    elif user_input==2 and color==3 and size==1:
        brand = "Rupa"
        color = "Brown"
        size = "S"
        gender = gender
        price = 150
    elif user_input==3 and color==3 and size==1:
        brand = "Tantex"
        color = "Brown"
        size = "S"
        gender = gender
        price = 200
    elif user_input==4 and color==3 and size==1:
        brand = "Amul"
        color = "Brown"
        size = "S"
        gender = gender
        price = 200
    elif user_input==5 and color==3 and size==1:
        brand = "Dollar Big Boss"
        color = "Brown"
        size = "S"
        gender = gender
        price = 200                      
    elif user_input==6 and color==3 and size==1:
        brand = "Dixcy"
        color = "Brown"
        size = "M"
        gender = gender
        price = 200

    elif user_input==1 and color==3 and size==2:
        brand = "VIP"
        color = "Brown"
        size = "M"
        gender = gender
        price = 200
    elif user_input==2 and color==3 and size==2:
        brand = "Rupa"
        color = "Brown"
        size = "M"
        gender = gender
        price = 150
    elif user_input==3 and color==3 and size==2:
        brand = "Tantex"
        color = "Brown"
        size = "M"
        gender = gender
        price = 200
    elif user_input==4 and color==3 and size==2:
        brand = "Amul"
        color = "Brown"
        size = "M"
        gender = gender
        price = 200
    elif user_input==5 and color==3 and size==2:
        brand = "Dollar Big Boss"
        color = "Brown"
        size = "M"
        gender = gender
        price = 200                      
    elif user_input==6 and color==3 and size==2:
        brand = "Dixcy"
        color = "Brown"
        size = "M"
        gender = gender
        price = 200        
    
    elif user_input==1 and color==3 and size==3:
        brand = "VIP"
        color = "Brown"
        size = "L"
        gender = gender
        price = 200
    elif user_input==2 and color==3 and size==3:
        brand = "Rupa"
        color = "Brown"
        size = "L"
        gender = gender
        price = 150
    elif user_input==3 and color==3 and size==3:
        brand = "Tantex"
        color = "Brown"
        size = "L"
        gender = gender
        price = 200
    elif user_input==4 and color==3 and size==3:
        brand = "Amul"
        color = "Brown"
        size = "L"
        gender = gender
        price = 200
    elif user_input==5 and color==3 and size==3:
        brand = "Dollar Big Boss"
        color = "Brown"
        size = "L"
        gender = gender
        price = 200                      
    elif user_input==6 and color==3 and size==3:
        brand = "Dixcy"
        color = "Brown"
        size = "L"
        gender = gender
        price = 200                
    elif user_input==1 and color==3 and size==4:
        brand = "VIP"
        color = "Brown"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==2 and color==3 and size==4:
        brand = "Rupa"
        color = "Brown"
        size = "XL"
        gender = gender
        price = 150
    elif user_input==3 and color==3 and size==4:
        brand = "Tantex"
        color = "Brown"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==4 and color==3 and size==4:
        brand = "Amul"
        color = "Brown"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==5 and color==3 and size==4:
        brand = "Dollar Big Boss"
        color = "Brown"
        size = "XL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==3 and size==4:
        brand = "Dixcy"
        color = "Brown"
        size = "XL"
        gender = gender
        price = 200                        
    elif user_input==1 and color==3 and size==5:
        brand = "VIP"
        color = "Brown"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==2 and color==3 and size==5:
        brand = "Rupa"
        color = "Brown"
        size = "XXL"
        gender = gender
        price = 150
    elif user_input==3 and color==3 and size==5:
        brand = "Tantex"
        color = "Brown"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==4 and color==3 and size==5:
        brand = "Amul"
        color = "Brown"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==5 and color==3 and size==5:
        brand = "Dollar Big Boss"
        color = "Brown"
        size = "XXL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==3 and size==5:
        brand = "Dixcy"
        color = "Brown"
        size = "XXL"
        gender = gender
        price = 200                                
    
    
    elif user_input==1 and color==4 and size==1:
        brand = "VIP"
        color = "Black"
        size = "S"
        gender = gender
        price = 200
    elif user_input==2 and color==4 and size==1:
        brand = "Rupa"
        color = "Black"
        size = "S"
        gender = gender
        price = 150
    elif user_input==3 and color==4 and size==1:
        brand = "Tantex"
        color = "Black"
        size = "S"
        gender = gender
        price = 200
    elif user_input==4 and color==4 and size==1:
        brand = "Amul"
        color = "Black"
        size = "S"
        gender = gender
        price = 200
    elif user_input==5 and color==4 and size==1:
        brand = "Dollar Big Boss"
        color = "Black"
        size = "S"
        gender = gender
        price = 200                      
    elif user_input==6 and color==4 and size==1:
        brand = "Dixcy"
        color = "Black"
        size = "S"
        gender = gender
        price = 200        

    elif user_input==1 and color==4 and size==2:
        brand = "VIP"
        color = "Black"
        size = "M"
        gender = gender
        price = 200
    elif user_input==2 and color==4 and size==2:
        brand = "Rupa"
        color = "Black"
        size = "M"
        gender = gender
        price = 150
    elif user_input==3 and color==4 and size==2:
        brand = "Tantex"
        color = "Black"
        size = "M"
        gender = gender
        price = 200
    elif user_input==4 and color==4 and size==2:
        brand = "Amul"
        color = "Black"
        size = "M"
        gender = gender
        price = 200
    elif user_input==5 and color==4 and size==2:
        brand = "Dollar Big Boss"
        color = "Black"
        size = "M"
        gender = gender
        price = 200                      
    elif user_input==6 and color==4 and size==2:
        brand = "Dixcy"
        color = "Black"
        size = "M"
        gender = gender
        price = 200

    elif user_input==1 and color==4 and size==3:
        brand = "VIP"
        color = "Black"
        size = "L"
        gender = gender
        price = 200
    elif user_input==2 and color==4 and size==3:
        brand = "Rupa"
        color = "Black"
        size = "L"
        gender = gender
        price = 150
    elif user_input==3 and color==4 and size==3:
        brand = "Tantex"
        color = "Black"
        size = "L"
        gender = gender
        price = 200
    elif user_input==4 and color==4 and size==3:
        brand = "Amul"
        color = "Black"
        size = "L"
        gender = gender
        price = 200
    elif user_input==5 and color==4 and size==3:
        brand = "Dollar Big Boss"
        color = "Black"
        size = "L"
        gender = gender
        price = 200                      
    elif user_input==6 and color==4 and size==3:
        brand = "Dixcy"
        color = "Black"
        size = "L"
        gender = gender
        price = 200        

    elif user_input==1 and color==4 and size==4:
        brand = "VIP"
        color = "Black"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==2 and color==4 and size==4:
        brand = "Rupa"
        color = "Black"
        size = "XL"
        gender = gender
        price = 150
    elif user_input==3 and color==4 and size==4:
        brand = "Tantex"
        color = "Black"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==4 and color==4 and size==4:
        brand = "Amul"
        color = "Black"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==5 and color==4 and size==4:
        brand = "Dollar Big Boss"
        color = "Black"
        size = "XL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==4 and size==4:
        brand = "Dixcy"
        color = "Black"
        size = "XL"
        gender = gender
        price = 200        
    
    
    elif user_input==1 and color==4 and size==5:
        brand = "VIP"
        color = "Black"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==2 and color==4 and size==5:
        brand = "Rupa"
        color = "Black"
        size = "XXL"
        gender = gender
        price = 150
    elif user_input==3 and color==4 and size==5:
        brand = "Tantex"
        color = "Black"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==4 and color==4 and size==5:
        brand = "Amul"
        color = "Black"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==5 and color==4 and size==5:
        brand = "Dollar Big Boss"
        color = "Black"
        size = "XXL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==4 and size==5:
        brand = "Dixcy"
        color = "Black"
        size = "XXL"
        gender = gender
        price = 200          


    elif user_input==1 and color==5 and size==1:
        brand = "VIP"
        color = "White"
        size = "S"
        gender = gender
        price = 200
    elif user_input==2 and color==5 and size==1:
        brand = "Rupa"
        color = "White"
        size = "S"
        gender = gender
        price = 150
    elif user_input==3 and color==5 and size==1:
        brand = "Tantex"
        color = "White"
        size = "S"
        gender = gender
        price = 200
    elif user_input==4 and color==5 and size==1:
        brand = "Amul"
        color = "White"
        size = "S"
        gender = gender
        price = 200
    elif user_input==5 and color==5 and size==1:
        brand = "Dollar Big Boss"
        color = "White"
        size = "S"
        gender = gender
        price = 200                      
    elif user_input==6 and color==5 and size==1:
        brand = "Dixcy"
        color = "White"
        size = "S"
        gender = gender
        price = 200


    elif user_input==1 and color==5 and size==2:
        brand = "VIP"
        color = "White"
        size = "M"
        gender = gender
        price = 200
    elif user_input==2 and color==5 and size==2:
        brand = "Rupa"
        color = "White"
        size = "M"
        gender = gender
        price = 150
    elif user_input==3 and color==5 and size==2:
        brand = "Tantex"
        color = "White"
        size = "M"
        gender = gender
        price = 200
    elif user_input==4 and color==5 and size==2:
        brand = "Amul"
        color = "White"
        size = "M"
        gender = gender
        price = 200
    elif user_input==5 and color==5 and size==2:
        brand = "Dollar Big Boss"
        color = "White"
        size = "M"
        gender = gender
        price = 200                      
    elif user_input==6 and color==5 and size==2:
        brand = "Dixcy"
        color = "White"
        size = "M"
        gender = gender
        price = 200
                                

    elif user_input==1 and color==5 and size==3:
        brand = "VIP"
        color = "White"
        size = "L"
        gender = gender
        price = 200
    elif user_input==2 and color==5 and size==3:
        brand = "Rupa"
        color = "White"
        size = "L"
        gender = gender
        price = 150
    elif user_input==3 and color==5 and size==3:
        brand = "Tantex"
        color = "White"
        size = "L"
        gender = gender
        price = 200
    elif user_input==4 and color==5 and size==3:
        brand = "Amul"
        color = "White"
        size = "L"
        gender = gender
        price = 200
    elif user_input==5 and color==5 and size==3:
        brand = "Dollar Big Boss"
        color = "White"
        size = "L"
        gender = gender
        price = 200                      
    elif user_input==6 and color==5 and size==3:
        brand = "Dixcy"
        color = "White"
        size = "L"
        gender = gender
        price = 200

    elif user_input==1 and color==5 and size==4:
        brand = "VIP"
        color = "White"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==2 and color==5 and size==4:
        brand = "Rupa"
        color = "White"
        size = "XL"
        gender = gender
        price = 150
    elif user_input==3 and color==5 and size==4:
        brand = "Tantex"
        color = "White"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==4 and color==5 and size==4:
        brand = "Amul"
        color = "White"
        size = "XL"
        gender = gender
        price = 200
    elif user_input==5 and color==5 and size==4:
        brand = "Dollar Big Boss"
        color = "White"
        size = "XL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==5 and size==4:
        brand = "Dixcy"
        color = "White"
        size = "XL"
        gender = gender
        price = 200
                              
    elif user_input==1 and color==5 and size==5:
        brand = "VIP"
        color = "White"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==2 and color==5 and size==5:
        brand = "Rupa"
        color = "White"
        size = "XXL"
        gender = gender
        price = 150
    elif user_input==3 and color==5 and size==5:
        brand = "Tantex"
        color = "White"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==4 and color==5 and size==5:
        brand = "Amul"
        color = "White"
        size = "XXL"
        gender = gender
        price = 200
    elif user_input==5 and color==5 and size==5:
        brand = "Dollar Big Boss"
        color = "White"
        size = "XXL"
        gender = gender
        price = 200                      
    elif user_input==6 and color==5 and size==5:
        brand = "Dixcy"
        color = "White"
        size = "XXL"
        gender = gender
        price = 200                          
    undergarmentshop(brand=brand,color=color,size=size,gender=gender,price=price)
