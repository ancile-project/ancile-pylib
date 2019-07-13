.. _multi_user:

Writing Multi-User Programs
===========================

It's fairly simple to write ancile programs that work with several users. This is thanks to the :func:`ancile.utils.build_programs` method. If you plan to use variables to save user-specific values for later use, then make sure you give your variables unique names.

.. note:: Prepending an underscore (_) to your ancile function parameter stops the parser from surrounding the content with quotes if it's a string. If the content is a list or tuple, it will avoid surrounding its members with quotes. This is particularily useful if you would like to use a parameter as a variable name.

This is a program that checks if all users are in a specified geofence.

.. code-block:: python
    
    from ancile import AncileClient, ancile_program, build_programs

    ...

    class User:
        def __init__(self, user_id, ancile_username):
            self.user_id = user_id
            self.ancile_user = ancile_username

    GEOFENCE = (41.686553, -73.898132)
    RADIUS = 100
    
    USERS = [User("user1", "user1@email.com"), User("user2", "user2@email.com")]

    @ancile_program
    def get_user_dp(_user_id, ancile_username, fence, radius_value):
        _user_id = vassar_location.get_last_location(user=user(ancile_username))
        vassar_location.in_geofence(geofence=fence, radius=radius_value, data=_user_id)

    @ancile_program
    def get_aggregate(_users)
        final_data = general.quorum(threshold=1, data=_users, value_keys="in_geofence")
        general.keep_keys(keys=["quorum"], data=final_data)
        result.append_dp_data_to_result(data=final_data)
    
    # Create list containing postitional arguments for every user
    program_args = []
    for user in USERS:
        program_args.append([user.user_id, user.ancile_username, GEOFENCE, RADIUS])
    
    # Generate program for all users
    users_program = build_programs(get_user_dp, program_args)
    
    # Create aggreate program
    user_ids = [user.user_id for user in USERS]
    aggregate_program = get_aggregate(user_ids)

    final_program = users_program + aggregate_program
    result = client.execute(final_program, [user.ancile_user for user in USERS])

    in_geofence = result[0]["quorum"]


