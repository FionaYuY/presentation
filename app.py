import streamlit as st
import sys
from pathlib import Path

# 添加專案根目錄到Python路徑
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# 導入配置和工具
from config.settings import APP_CONFIG
from utils.styles import apply_custom_css, render_page_section

# 導入所有頁面
from pages import (
    page1_home,
    page2_overview,
    page3_innovation,
    page4_academic,
    page4_5_impact_analyzer,
    page5_business,
    page5_5_us_trend_analyzer,
    page5_6_earnings_call_analyzer,
    page6_tech_skills,
    page6_hidden_gems,
    page7_commute,
    page8_conclusion
)

def setup_page():
    """設定Streamlit頁面配置"""
    st.set_page_config(
        page_title=APP_CONFIG["page_title"],
        page_icon=APP_CONFIG["page_icon"],
        layout=APP_CONFIG["layout"],
        initial_sidebar_state=APP_CONFIG["initial_sidebar_state"]
    )

def render_sidebar():
    """渲染側邊欄"""
    with st.sidebar:
        st.title("目錄")
        
        # 快速導航
        st.subheader("快速導航")
        sections = [
            ("home", "首頁"),
            ("overview", "作品總覽"),
            ("innovation", "技術創新"),
            ("academic", "學術研究"),
            ("impact", "Impact Analyzer"),
            ("business", "商業應用"),
            ("us_trend", "US Trend Analyzer"),
            ("earnings", "法說會簡報分析"),
            ("tech_skills", "技術學習成果"),
            ("hidden", "遺珠作品"),
            ("commute", "通勤人生"),
            ("conclusion", "結語")
        ]
        
        for section_id, section_name in sections:
            st.markdown(f"• **{section_name}**")
        
        st.markdown("---")
        
        # 資訊區
        st.subheader("📋 展示資訊")
        st.markdown("**作者：** Fiona")
        st.markdown("**期間：** 2025上半年")
        st.markdown("**完成項目：** 14個")
        st.markdown("**完成率：** 100%")

def render_all_content():
    """渲染所有頁面內容（向下滾動）"""
    
    # 頁面資訊
    pages = [
        ("home", "首頁", page1_home.render),
        ("overview", "作品總覽", page2_overview.render),
        ("innovation", "技術創新", page3_innovation.render),
        ("academic", "學術研究", page4_academic.render),
        ("impact", "Impact Analyzer", page4_5_impact_analyzer.render),
        ("business", "商業應用", page5_business.render),
        ("us_trend", "US Trend Analyzer", page5_5_us_trend_analyzer.render),
        ("earnings", "法說會簡報分析", page5_6_earnings_call_analyzer.render),
        ("tech_skills", "技術學習成果", page6_tech_skills.render),
        ("hidden", "遺珠作品", page6_hidden_gems.render),
        ("commute", "通勤人生", page7_commute.render),
        ("conclusion", "結語", page8_conclusion.render)
    ]
    
    # 渲染所有頁面區塊 - 滾動吸附效果
    for section_id, section_name, render_func in pages:
        render_page_section(section_id, render_func)

def main():
    """主函數"""
    # 設定頁面
    setup_page()
    
    # 應用自定義CSS
    apply_custom_css()
    
    # 渲染側邊欄
    render_sidebar()
    
    # 主要內容區域
    main_container = st.container()
    
    with main_container:
        # 渲染所有頁面內容
        render_all_content()
    
    # 頁腳資訊
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Fiona 工作成果展示**")
    
    with col2:
        st.write("**2025上半年**")
    
    with col3:
        st.write("**14個項目 - 100% 完成率**")

if __name__ == "__main__":
    main() 