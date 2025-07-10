import streamlit as st
import json

def render():
    """渲染US Trend Analyzer页面"""
    st.title("📊 US Trend Analyzer")
    st.subheader("自動化美國新聞趨勢分析系統")
    
    st.markdown("---")
    
    # 系统功能简介
    st.write("### 🎯 系統功能")
    st.write("US Trend Analyzer 是一套自動化分析近期美國新聞的智能系統，專門為投資決策提供深度市場洞察。")
    
    features = [
        "📈 **隱藏投資題材挖掘**: 從大量財經新聞中自動識別投資機會",
        "🔍 **市場趨勢分析**: 即時追蹤和分析市場動態變化",
        "🤖 **P1-GPT 整合**: 為 P1-GPT 提供高質量的分析數據",
        "📊 **公司內部使用**: 支援內部團隊的投資分析工作"
    ]
    
    for feature in features:
        st.write(feature)
    
    st.markdown("---")
    
    # 分析图表 - 使用一列的宽度
    st.write("### 📈 分析圖表")
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            st.image("assets/images/keywords_growth_rate.png", 
                    caption="關鍵字成長率", 
                    use_column_width=True)
        except:
            st.info("📊 關鍵字成長率圖（載入中...）")
    
    with col2:
        try:
            st.image("assets/images/top_keywords_trend.png", 
                    caption="熱門關鍵字趨勢", 
                    use_column_width=True)
        except:
            st.info("📈 熱門關鍵字趨勢圖（載入中...）")
    
    st.markdown("---")
    
    # 未来发展
    st.write("### 🔮 未來發展")
    st.write("**目標**: 支援用戶自定義時間區間分析")
    
    future_scenarios = [
        "🔮 **「給我2025十大題材」**",
        "📊 **「近一年，是否有大幅成長的話題」**"
    ]
    
    for scenario in future_scenarios:
        st.write(scenario) 