import streamlit as st
def dear_password(password):
    score = 0
    list = []
    if len (password)>= 8:
        score += 1
    else:
        list.append('🛑Use atleast 8 characters') 
    if  any (c.isupper() for c in password):
        score +=1
    else:
          list.append("Include upper letter") 
    if  any (c.islower() for c in password):
        score +=1
    else:
          list.append("Include lower letter")     
    if  any (c.isdigit() for c in password):
        score +=1
    else:
          list.append("Add a number (0-9)")      
    if  any (c in "!@#$%^*" for c in password):
      score +=1
    else:
     list.append("Use a special character (!@#$%^*:)") 
    return score , list
def main():
    st.title("🔐Password Strength Meter")
    password = st.text_input("🔑Enter Password" , type="password")
    
    if password:
        score, list = dear_password(password)
        
        if score == 5:
            st.success("😉💪Strong password! secure and safe")
        elif score == 3 or score == 4:
             st.warning("Moderate Password! Improve it")
        else:
            st.error('😥weak password follow these steps:')
        for tip in list:
            st.write(tip)            
main()


           