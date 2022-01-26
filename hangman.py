#   HANGMAN GAME
#    _______
#    |/    |
#    |     O
#    |    /|\
#    |     |
#    |    / \
# ___|_________
# 

def hangman_print(error):
    gallows_pole  = "    _______   \n"
    gallows_pole += "    |/    |   \n"
    gallows_pole += "    |     {head}   \n"
    gallows_pole += "    |    {left_arm}{body_upper}{right_arm}  \n"
    gallows_pole += "    |     {body_lower}   \n"
    gallows_pole += "    |    {left_leg} {right_leg}  \n"
    gallows_pole += " ___|_________\n"
    
    if error == 1:
        gallows_pole = gallows_pole.format(head = "O", left_arm = " ", body_upper = " ",
        right_arm = " ", body_lower = " ",  left_leg = " ", right_leg = " ")
    elif error == 2:
        gallows_pole = gallows_pole.format(head = "O", left_arm = " ", body_upper = "|",
        right_arm = " ", body_lower = "|",  left_leg = " ", right_leg = " ")
    elif error == 3:
        gallows_pole = gallows_pole.format(head = "O", left_arm = "/", body_upper = "|",
        right_arm = " ", body_lower = "|",  left_leg = " ", right_leg = " ")
    elif error == 4:
        gallows_pole = gallows_pole.format(head = "O", left_arm = "/", body_upper = "|",
        right_arm = "\ ", body_lower = "|",  left_leg = " ", right_leg = " ")
    elif error == 5:
        gallows_pole = gallows_pole.format(head = "O", left_arm = "/", body_upper = "|",
        right_arm = "\ ", body_lower = "|",  left_leg = "/", right_leg = " ")
    elif error == 6:
        gallows_pole = gallows_pole.format(head = "O", left_arm = "/", body_upper = "|",
        right_arm = "\ ", body_lower = "|",  left_leg = "/", right_leg = "\ ")
    else:
        gallows_pole = gallows_pole.format(head = " ", left_arm = " ", body_upper = " ",
        right_arm = " ", body_lower = " ",  left_leg = " ", right_leg = " ")
    
    print(gallows_pole)
hangman_print(546)

