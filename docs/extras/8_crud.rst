Crud
##############

Syntax::

    [dashboard_tokens: $/dashboard/tokens]
    @crud {
        rest_framework.authtoken.Token(user=request.user)
    }

