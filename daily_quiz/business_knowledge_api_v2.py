import traceback

from flask import Flask, request, jsonify
app = Flask(__name__)

# mock business knowledge data structure, maybe get it from call api or search in database
BUSINESS_KNOWLEDGE_DB = [
    {
        "id": 1,
        "title": "客户关系管理",
        "content": "客户关系管理(CRM)是一种管理公司与客户和潜在客户交互的策略。",
        "keywords": ["CRM", "客户", "关系", "管理"],
        "links": ["https://test.com/crm", "https://test.com/customer-management"]
    },
    {
        "id": 2,
        "title": "供应链管理",
        "content": "供应链管理(SCM)是对货物、数据和资金的流动进行监督和优化的系统化方法。",
        "keywords": ["SCM", "供应链", "物流"],
        "links": ["https://test.com/scm", "https://test.com/supply-chain"]
    },
    {
        "id": 3,
        "title": "企业资源规划",
        "content": "企业资源规划(ERP)是集成组织中所有业务流程和部门的管理系统。",
        "keywords": ["ERP", "资源规划", "企业管理"],
        "links": ["https://test.com/erp", "https://test.com/enterprise-planning"]
    }
]



@app.route('/api/business-knowledge', methods=['GET'])
def query_business_knowledge():
    """
    query business knowledge api
    args:
        query (str): user input query keyword
    response:
        json data
    """

    kw = request.args.get('query', '')
    result = dict()

    if not kw:
        result["code"] = 400
        result["msg"] = "query argument missing"
        result["data"] = []
        return jsonify(result)

    match_data = []

    try:
        for item in BUSINESS_KNOWLEDGE_DB:
            # search keywords in title, content and keywords field

            if (kw.lower() in item["title"].lower() or kw.lower() in item["content"].lower() or
                    any(kw.lower() in keyword.lower() for keyword in item['keywords'])):
                match_data.append({
                    "id": item['id'],
                    "title": item['title'],
                    "content": item['content'],
                    "links": item['links']
                })

        result["code"] = 200
        result["msg"] = "success"
        result["data"] = match_data

    except Exception as err:
        traceback.print_exc()

        result["code"] = 500
        result["msg"] = f"internal error: {str(err)}"
        result["data"] = []

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

# testcase:
# curl "http://127.0.0.1:5000/api/business-knowledge?query=CRM"
# curl "http://127.0.0.1:5000/api/business-knowledge?query=erp"
# curl "http://127.0.0.1:5000/api/business-knowledge?query=%E7%AE%A1%E7%90%86"