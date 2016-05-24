

def getUser(forename):
    return User.objects.get(forename = forename)


