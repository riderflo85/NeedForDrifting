import random, string


def generate_token(user):
    """
    Generate the token for the user can use this API with mobile app.
    """

    for_key = string.ascii_letters + string.digits

    token = "".join(random.choice(for_key) for _ in range(24))
    user.token = token
    user.save()

    return token