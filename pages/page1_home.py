import streamlit as st

def render():
    """渲染首頁"""
    
    # 直接使用HTML设置大标题
    st.markdown("""
    <h1 style="font-size: 4rem !important; font-weight: 700 !important; color: #ffffff !important; margin-bottom: 1rem !important; text-align: left !important;">
        Fiona 2025上半年工作成果展示
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="font-size: 2.8rem !important; font-weight: 600 !important; color: #e0e0e0 !important; margin-bottom: 2rem !important; text-align: left !important;">
        從學術突破到商業應用的完美演出
    </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    
    st.markdown("### 🏆 主要成就")
    
    achievements = [
        "🎓 AI論文研究與專利申請",
        "🔧 大型系統重構與技術創新",
        "💼 商業策略自動化平台開發",
        "🗞️ 新聞網站重構",
        "🤝 跨部門協作與產品優化"
    ]
    
    for i, achievement in enumerate(achievements):
        st.success(f"**{i+1}.** {achievement}") 