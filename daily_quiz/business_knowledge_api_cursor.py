from flask import Flask, request, jsonify
import json
from typing import Dict, List, Any, Optional

app = Flask(__name__)

# 模拟业务知识数据库 mock business knowledge data structure, maybe get it from call llms api or search in database
BUSINESS_KNOWLEDGE_DB = [
    {
        "id": 1,
        "title": "客户关系管理",
        "content": "客户关系管理(CRM)是一种管理公司与客户和潜在客户交互的策略。",
        "keywords": ["CRM", "客户", "关系", "管理"],
        "links": ["https://example.com/crm", "https://example.com/customer-management"]
    },
    {
        "id": 2,
        "title": "供应链管理",
        "content": "供应链管理(SCM)是对货物、数据和资金的流动进行监督和优化的系统化方法。",
        "keywords": ["SCM", "供应链", "物流"],
        "links": ["https://example.com/scm", "https://example.com/supply-chain"]
    },
    {
        "id": 3,
        "title": "企业资源规划",
        "content": "企业资源规划(ERP)是集成组织中所有业务流程和部门的管理系统。",
        "keywords": ["ERP", "资源规划", "企业管理"],
        "links": ["https://example.com/erp", "https://example.com/enterprise-planning"]
    }
]


@app.route('/api/business-knowledge', methods=['GET'])
def query_business_knowledge():
    """
    查询业务知识API

    参数:
        query (str): 用户输入的查询关键词

    返回:
        JSON格式响应，包含匹配的知识点和相关链接
    """
    # 获取查询参数
    query = request.args.get('query', '')

    if not query:
        return jsonify({
            "status": "error",
            "message": "查询参数不能为空",
            "data": []
        }), 400

    # 搜索匹配的知识
    results = []
    for item in BUSINESS_KNOWLEDGE_DB:
        # 检查标题、内容和关键词是否包含查询字符串
        if (query.lower() in item['title'].lower() or
                query.lower() in item['content'].lower() or
                any(query.lower() in keyword.lower() for keyword in item['keywords'])):
            results.append({
                "id": item['id'],
                "title": item['title'],
                "content": item['content'],
                "links": item['links']
            })

    # 返回结果
    response = {
        "status": "success",
        "count": len(results),
        "data": results
    }

    return jsonify(response)

# curl "http://127.0.0.1:5000/api/business-knowledge?query=CRM"
if __name__ == '__main__':
    app.run(debug=True)