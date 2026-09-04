def http(status):
    match status:
        case 200:
         return "Ok"
        case 201:
         return "created"
        case 204:
         return "Unauth"


print(http(200))
