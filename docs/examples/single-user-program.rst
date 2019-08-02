Writing Single-User Programs
============================

It is quite straightforward to write ancile programs that work with one user only. In most cases, you will be fine writing one function rather than splitting into multiple parts.

.. note:: Make sure that your parameter names do not conflict with any other function or variable names in your program. You can avoid this by adding an underscore (_) to the end of your parameter name. 

An example of a single-user program is a simple function that fuzzes the user's location (within a certain radius) and returns the fuzzed coordinates.

.. code-block:: python

    from ancile import AncileClient, ancile_program

    API_TOKEN = '' # your application's token
    ANCILE_URL = 'https://ancile.cs.vassar.edu/' # the ancile root URL

    client = AncileClient(API_TOKEN, ANCILE_URL)

    @ancile_program # turn the function into an ancile program
    def get_location(username, radius_):
        dp = vassar_location.get_last_location(user=user(username))
        dp = vassar_location.fuzz_location(radius=radius_, data=dp)
        dp = general.keep_keys(keys=['latitude', 'longitude'], data=dp)
        return_to_app(data=dp)

    my_program = get_location("user", 100)
    result = client.execute(my_program, ["user"])

    latitude = result[0]["latitude"]
    longitude = result[0]["longitude"]

More sophisticated applications might require splitting the program into several functions. This can be easily done using the :func:`ancile.utils.build_programs`. Check out the :ref:`multi_user` guide for more information.
