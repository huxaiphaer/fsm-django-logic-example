def verify_account(model, *args, **kwargs):
    print("verify account callback", args)
    print("verify account callback", kwargs)


def approve_account(*args, **kwargs):
    print("approve account callback")


def reject_account(*args, **kwargs):
    print("reject account callback")
