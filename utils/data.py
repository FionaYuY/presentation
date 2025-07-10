import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def get_project_data():
    """獲取專案資料"""
    projects = [
        {
            "name": "DEoT論文 - 實驗流程設計",
            "description": "完成超過600題的深度實驗評估，成功投稿至arXiv和AI Journal",
            "completion_date": "2025-07",
            "category": "學術研究",
            "status": "完成",
            "icon": "🎓"
        },
        {
            "name": "Impact Analyzer Agent開發",
            "description": "利用DEoT技術，開發用於分析事件影響力之agent",
            "completion_date": "2025-04",
            "category": "技術開發",
            "status": "完成",
            "icon": "🚀"
        },
        {
            "name": "US趨勢分析模組開發",
            "description": "從大量財經新聞中挖掘隱藏投資題材與市場趨勢",
            "completion_date": "2025-01",
            "category": "技術開發",
            "status": "完成",
            "icon": "📈"
        },
        {
            "name": "智慧創新大賽準備作業",
            "description": "建立公司官方GitHub組織，編寫作品說明書，開源專欄生成技術",
            "completion_date": "2025-04",
            "category": "專案管理",
            "status": "完成",
            "icon": "🏆"
        },
        {
            "name": "法說會簡報內容",
            "description": "提取與解析全台2000多家公司法說會資料，建立自動化流程",
            "completion_date": "2025-01",
            "category": "資料處理",
            "status": "完成",
            "icon": "📊"
        },
        {
            "name": "簡報製作",
            "description": "AI vs. 金融市場分析、LinkVerse：AI 名流關係分析平台",
            "completion_date": "2025-06",
            "category": "商業展示",
            "status": "完成",
            "icon": "🎯"
        },
        {
            "name": "NeuroWatt News系統重構開發",
            "description": "重構生成流程、加入科學分析與趨勢分析新功能",
            "completion_date": "2025-04",
            "category": "技術開發",
            "status": "完成",
            "icon": "🔥"
        },
        {
            "name": "NeuroWatt News專欄",
            "description": "將區域general專欄擴展為按產業分類的專業化專欄系統",
            "completion_date": "2025-05",
            "category": "產品開發",
            "status": "完成",
            "icon": "📰"
        },
        {
            "name": "P1 Select策略自動化開發模組",
            "description": "完成前後端開發，實現10個投資策略的自動化模組",
            "completion_date": "2025-06",
            "category": "產品開發",
            "status": "完成",
            "icon": "💼"
        },
        {
            "name": "ISA美股系統擴展開發",
            "description": "將台股系統擴展為支援美股市場，完成財報三表數據整合",
            "completion_date": "2025-03",
            "category": "系統擴展",
            "status": "完成",
            "icon": "🌎"
        },
        {
            "name": "ITRD券商API消息面模組開發",
            "description": "開發股票分析pipeline的消息面計算模組，建立新聞情感分數計算系統",
            "completion_date": "2025-02",
            "category": "API開發",
            "status": "完成",
            "icon": "🔌"
        }
    ]
    
    return projects

def get_commute_data():
    """獲取通勤資料"""
    commute_data = {
        "daily_hours": 3,
        "monthly_hours": 60,
        "half_year_hours": 360,
        "equivalent_days": 15,
        "working_days_per_month": 20,
        "months": 6
    }
    
    return commute_data

def get_commute_comparisons():
    """獲取通勤時間有趣比較"""
    comparisons = [
        {"activity": "飛到日本來回", "times": 3, "icon": "✈️"},
        {"activity": "開車環島", "times": 2, "icon": "🚗"},
        {"activity": "讀完書", "times": 12, "icon": "📚"},
        {"activity": "看完電影", "times": 90, "icon": "🎬"},
        {"activity": "喝掉咖啡", "times": 720, "icon": "☕"},
        {"activity": "睡覺", "times": 15, "icon": "😴", "unit": "個整天"}
    ]
    
    return comparisons

def get_monthly_commute_data():
    """獲取月度通勤資料"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    monthly_hours = [60, 60, 60, 60, 60, 60]
    cumulative_hours = [60, 120, 180, 240, 300, 360]
    
    return {
        "months": months,
        "monthly_hours": monthly_hours,
        "cumulative_hours": cumulative_hours
    }

def get_achievement_stats():
    """獲取成就統計"""
    stats = {
        "total_projects": 11,
        "completion_rate": 100,
        "categories": {
            "技術開發": 3,
            "產品開發": 2,
            "學術研究": 1,
            "資料處理": 1,
            "商業展示": 1,
            "專案管理": 1,
            "系統擴展": 1,
            "API開發": 1
        },
        "timeline": {
            "2025-01": 2,
            "2025-02": 1,
            "2025-03": 1,
            "2025-04": 3,
            "2025-05": 1,
            "2025-06": 2,
            "2025-07": 1
        }
    }
    
    return stats

@st.cache_data
def load_project_dataframe():
    """載入專案資料為DataFrame"""
    projects = get_project_data()
    df = pd.DataFrame(projects)
    return df

def format_project_list(projects):
    """格式化專案列表"""
    formatted = []
    for i, project in enumerate(projects, 1):
        formatted.append(f"{i}. {project['icon']} {project['name']}")
    return formatted

def calculate_work_metrics():
    """計算工作指標"""
    projects = get_project_data()
    commute = get_commute_data()
    
    metrics = {
        "projects_completed": len(projects),
        "avg_projects_per_month": len(projects) / 6,
        "total_work_hours": commute["half_year_hours"] + (8 * 20 * 6),  # 通勤 + 工作時間
        "efficiency_score": 100,  # 所有專案按時完成
        "innovation_projects": len([p for p in projects if p["category"] in ["技術開發", "產品開發"]]),
        "research_projects": len([p for p in projects if p["category"] == "學術研究"])
    }
    
    return metrics 