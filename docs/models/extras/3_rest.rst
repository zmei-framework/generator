Rest
#########

@rest extra is simple way to add rest api to your models.

Empty @rest extra, will add read only api for your model::


    #dog
    --------------
    name
    age

    @rest

You can add authentication easily:

    #dog
    --------------
    name
    age

    @rest {
        auth(basic, session)
    }

Or token authentication::


    #token
    ----------
    name
    user: one(cratis_profile.User)

    @mixin(rest_framework.authtoken.models.Token)


    #dog
    --------------
    name
    age

    @rest {
        auth(token: #token)
    }

