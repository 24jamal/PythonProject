def employeeOfTheMonth(mylist):

    name = ""
    maxhours = 0

    for person, hours in mylist:

        if hours > maxhours:

            maxhours = hours
            name = person
        else:
            pass

    print(f"Employee of the Month : {name} with {maxhours} hours worked")
    return name, maxhours

person , hours = employeeOfTheMonth([("Jamal",80),("Jackson",100),("Khan",200)])

print(person, hours)
