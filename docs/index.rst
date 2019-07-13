.. ancile-pylib documentation master file, created by
   sphinx-quickstart on Sat Jul 13 12:11:37 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ancile Python Library
========================================
The Ancile Python library simplifies the process of building and executing
ancile programs.

Overview
========
A simple ancile program that fetches a user's location and fuzzes it
will look like this:

.. code-block:: python

  from ancile import AncileClient, ancile_program

  API_TOKEN = '' # your application's token
  ANCILE_URL = 'https://ancile.cs.vassar.edu/api/run' # the ancile API endpoint
  PURPOSE = 'research' # the purpose of your application in ancile settings

  client = AncileClient(API_TOKEN, ANCILE_URL, PURPOSE)

  @ancile_program # turn the function into an ancile program
  def get_location(username, radius_value):
      dp = vassar_location.get_last_location(user=user(username))
      dp = vassar_location.fuzz_location(radius=radius_value, data=dp)
      dp = general.keep_keys(keys=['latitude', 'longitude'], data=dp)
      return_to_app(data=dp)

  my_program = get_location("user", 100)
  result = client.execute(my_program, ["user"])

  latitude = result[0]["latitude"]
  longitude = result[0]["longitude"]


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   ancile
