from js import Response

async def on_fetch(request, env):
    # Do anything else you'd like on request here!

    query = """SELECT quote, author
        FROM qtable
        ORDER BY RANDOM()
        LIMIT 1;"""
    results = await env.DB.prepare(query).all()
    # Return a JSON response
    return Response.json(results)