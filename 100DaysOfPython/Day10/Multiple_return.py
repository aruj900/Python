def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide meaning ful input"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

output = format_name(input("What is your first name? "),input("What is your last name? "))

print(output) 