import streamlit as st

def convert_units(value:float,unit_from:str,unit_to:str):
    # print("value>>>",value)
    # print("unit_from>>>",unit_from)
    # print("unit_to>>>",unit_to)
    if unit_from=="km" and  unit_to=="m":
        return value*1000
    elif unit_from=="m"and unit_to=="km":
       return value*0.001
    elif unit_from=="kg"and unit_to=="g":
       return value*1000
    elif unit_from=="g"and unit_to=="kg":
       return value*0.001
    else:
          return "conversion is not supported"
# result1=convert_units(1,"km","m")
# print("The value is",result1)
# result2=convert_units(2,"g","kg")
# print("The value in kg is:",result2)

def main():
   st.title("Unit Converter")
   st.write("welcome to the unit converter")
   value= st.number_input("Enter the value:", min_value=0.0 )
   unit_from=st.text_input("Enter the unit to convert from:")
   unit_to=st.text_input("Enter the unit to convert to :")
   if st.button("Convert"):
        result = convert_units(value,unit_from,unit_to)
        st.write(f"The value in {unit_to} is {result}")
   #  print("Unit Converter")
   #  print("welcome to the unit Converter")
   #  value=float(input("Enter the value:"))
   #  unit_from=input("Enter the unit to convert from:")
   #  unit_to=input("Enter the unit to convert to :")
   #  result = convert_units(value,unit_from,unit_to)
   #  print(f"The value in {unit_to} is {result}")
main()