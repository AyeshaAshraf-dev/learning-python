full_dot = '●'
empty_dot = '○'

def create_character(name, a, b, c):
    if not isinstance (name, str):
        return 'The character name should be a string.' 
    if name.strip() == "":
        return ' The character should have a name' 
    if len(name)>10:
        return 'The character name is too long'
    if " " in name :
        return 'The character name should not contain spaces'    
    if not  all(isinstance(x,int) for x in [a, b, c ]):
        return 'All stats should be integers'
    if all(x<1 for x in [a, b, c]):
        return 'All stats should be no less than 1'
    if all(x>4 for x in [a, b, c]):
        return 'All stats should be no more than 4'            
    if a + b + c != 7:
        return ' The character should start with 7 points'

    line_str = "STR " + full_dot*a + empty_dot*(10-a)
    line_int = "INT " + full_dot*b + empty_dot*(10-b)
    line_cha = "CHA " + full_dot*c + empty_dot*(10-c)

    return(name + "\n" + line_str + "\n" + line_int + "\n" + line_cha)

print(create_character('AYESHA', 5, 1,1))