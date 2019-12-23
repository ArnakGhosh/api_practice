import flask
from flask import request, jsonify, redirect, url_for
from psycopg2 import connect, sql
from psycopg2.extras import RealDictCursor
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'},
#     {'id': 3,
#      'title': 'A Matchbox Full Of Dreams',
#      'author': 'Edward Dutta',
#      'first_sentence': 'Never lie under the shadow of your dreams, until you set yourself free, with no strings attached.',
#      'published': '1975'}
# ]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def apiall():
    qstr=sql.SQL("SELECT * from {};").format(
    sql.Identifier("books")
)
    conn=connect(user='pytest', password='k1t5B&q', host='localhost', port=5432, database='pytestDB', cursor_factory=RealDictCursor)
    cursr=conn.cursor()
    cursr.execute(qstr)
    rec=cursr.fetchall()
    cursr.close()
    conn.close()
    return json.dumps(rec, indent=2)

@app.route('/api/v1/resources/books/id', methods=['GET'])
def apiid():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    # results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    # for book in books:
    #     if book['id'] == id:
    #         results.append(book)
    qstr=sql.SQL("SELECT * from {} where {} = {};").format(
    sql.Identifier("books"),
    sql.Identifier("id"),
    sql.Placeholder()
)
    conn=connect(user='pytest', password='k1t5B&q', host='localhost', port=5432, database='pytestDB', cursor_factory=RealDictCursor)
    cursr=conn.cursor()
    cursr.execute(qstr, str(id))
    rec=cursr.fetchall()
    cursr.close()
    conn.close()
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return json.dumps(rec, indent=2)

@app.route('/api/v1/resources/books/year', methods=['GET'])
def apiyr():
# check the year input and return the document
    if 'year' in request.args:
        yr = request.args['year']
    else:
        return "Error: No year field provided. Please specify an year of publication."

    # Create an empty list for our results
    # results = []

    # Loop through the data and match results that fit the requested year of publishing.
    # years might be same, hence will return many results
    # for book in books:
    #     if book['published'] == yr:
    #         results.append(book)


    # Use the jsonify function from Flask to convert our list
    # Python dictionaries to the JSON format.
    # return jsonify(results)
    conn=connect(user='pytest', password='k1t5B&q', host='localhost', port=5432, database='pytestDB', cursor_factory=RealDictCursor)
    cursr=conn.cursor()
    qstr=sql.SQL("SELECT * from {} where {} = {};").format(
    sql.Identifier("books"),
    sql.Identifier("published"),
    sql.Placeholder()
)
    cursr.execute(qstr, [yr])
    rec=cursr.fetchall()
    cursr.close()
    conn.close()
    return json.dumps(rec, indent=2)

@app.route('/api/v1/resources/books', methods=['GET'])
def apifilter():
    conn=connect(user='pytest', password='k1t5B&q', host='localhost', port=5432, database='pytestDB', cursor_factory=RealDictCursor)
    cursr=conn.cursor()
    args = request.args
    if len(args)!=0:
        idd = args.get('id')
        title = args.get('title')
        author = args.get('auth')
        pubyear = args.get('year')
        filter_arr = list()
        query = sql.SQL("SELECT * FROM {} WHERE").format(
            sql.Identifier("books")
            )
        if idd:
            query += sql.SQL(' {} = {} AND').format(
                sql.Identifier("id"),
                sql.Placeholder())
            filter_arr.append(idd)
        if title:
            query += sql.SQL(' {} = {} AND').format(
                sql.Identifier("title"),
                sql.Placeholder())
            filter_arr.append(title)
        if author:
            query += sql.SQL(' {} = {} AND').format(
                sql.Identifier("author"),
                sql.Placeholder())
            filter_arr.append(author)
        if pubyear:
            query += sql.SQL(' {} = {} AND').format(
                sql.Identifier("published"),
                sql.Placeholder())
            filter_arr.append(pubyear)
        query = sql.SQL(query.as_string(conn)[:-4]) + sql.SQL(' ;')
        cursr.execute(query, filter_arr)
        rec=cursr.fetchall()
        cursr.close()
        conn.close()
        return json.dumps(rec, indent=2)
    else:
        return redirect(url_for('apiall'))

app.run()