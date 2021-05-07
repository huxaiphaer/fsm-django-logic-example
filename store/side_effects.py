def verify_account(model, *args, **kwargs):
    print("verify account side effect", args)
    print("verify account side effect", kwargs)


def approve_account(*args, **kwargs):
    print("approve account side effect")


def reject_account(*args, **kwargs):
    print("reject account side effect")
