import streamlit as st

def render():
    """渲染作品總覽頁面"""
    
    # 使用HTML设置大标题
    st.markdown("""
    <h1 style="font-size: 4rem !important; font-weight: 700 !important; color: #ffffff !important; margin-bottom: 1rem !important;">
        📋 2025上半年完成作品
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="font-size: 2.8rem !important; font-weight: 600 !important; color: #e0e0e0 !important; margin-bottom: 2rem !important;">
        全方位技術展示：從學術研究到商業應用
    </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 項目統計
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="完成項目",
            value="14個",
            delta="100% 完成率"
        )
    
    with col2:
        st.metric(
            label="技術領域",
            value="6大類",
            delta="全面覆蓋"
        )
    
    with col3:
        st.metric(
            label="創新突破",
            value="5項",
            delta="技術升級"
        )
    
    with col4:
        st.metric(
            label="商業價值",
            value="56萬+",
            delta="產品化"
        )
    
    st.markdown("---")
    
    # 項目分類展示
    st.markdown("### 🎯 項目分類概覽")
    
    # 學術研究類
    st.markdown("#### 🎓 學術研究類")
    academic_projects = [
        "**DEoT論文研究**: 深度探索與技術突破",
        "**Impact Analyzer**: DEoT的加速版、簡化版實作"
    ]
    
    for project in academic_projects:
        st.write(f"• {project}")
    
    st.markdown("---")
    
    # 技術創新類
    st.markdown("#### 🔧 技術創新類")
    innovation_projects = [
        "**NeuroWatt News 系統重構**: 從LDA到BERTopic的技術升級",
        "**US Trend Analyzer**: 美國財經新聞分析系統",
        "**法說會簡報分析系統**: 自動化財務報告處理"
    ]
    
    for project in innovation_projects:
        st.write(f"• {project}")
    
    st.markdown("---")
    
    # 商業應用類
    st.markdown("#### 💼 商業應用類")
    business_projects = [
        "**P1 Select策略系統**: 化繁為簡的投資策略生成器",
        "**NeuroWatt News圖標設計**: 企業視覺識別優化",
        "**炸物理論系統**: 創意發想到實現的快速原型"
    ]
    
    for project in business_projects:
        st.write(f"• {project}")
    
    st.markdown("---")
    
    # 系統維護類
    st.markdown("#### 🛠️ 系統維護與優化類")
    maintenance_projects = [
        "**LinkVerse系統**: 多平台內容管理優化",
        "**各種小工具開發**: 提升工作效率的實用工具",
        "**UI/UX改進**: 使用者體驗持續優化"
    ]
    
    for project in maintenance_projects:
        st.write(f"• {project}")
    
    st.markdown("---")
    
    # 項目時間線
    st.markdown("### 📅 完成時間線")
    
    timeline_data = [
        ("1-2月", "DEoT論文、NeuroWatt News重構"),
        ("3-4月", "P1 Select、US Trend Analyzer"),
        ("5-6月", "法說會分析、技術整合優化")
    ]
    
    for period, projects in timeline_data:
        st.info(f"**{period}**: {projects}")
    
    st.success("🎯 **總結**: 14個項目全部按時完成，涵蓋學術研究、技術創新、商業應用等多個領域，展現了全方位的技術能力！") 