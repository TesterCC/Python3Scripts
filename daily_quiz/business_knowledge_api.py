import traceback

from flask import Flask, request, jsonify
app = Flask(__name__)

# mock business knowledge data structure, maybe get it from call api or search in database
business_knowledge = {
    "database": {
        "knowledge_point": "Here is database knowledge point",
        "url_link": "https://example.com/database"
    },
    "algorithm": {
        "knowledge_point": "Here is algorithm knowledge point",
        "url_link": "https://example.com/algorithm-design"
    }
}


@app.route('/api/business-knowledge', methods=['GET'])
def get_business_knowledge():

    kw = request.args.get('query')
    result = dict()

    try:
        if kw in business_knowledge.keys():
            result["code"] = 200
            result["msg"] = "success"
            result["data"] = {
                "knowledge_point": business_knowledge[kw]["knowledge_point"],
                "url_link": business_knowledge[kw]["url_link"]
            }

        else:
            result["code"] = 404
            result["msg"] = "can't find knowledge point"
            result["data"] = {}

    except Exception as err:
        traceback.print_exc()

        result["code"] = 500
        result["msg"] = f"internal error: {str(err)}"
        result["data"] = {}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

# testcase:
# curl "http://127.0.0.1:5000/api/business-knowledge?query=algorithm"