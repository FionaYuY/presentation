import streamlit as st

def render():
    """渲染Impact Analyzer页面"""
    st.title("🚀 Impact Analyzer")
    st.subheader("DEoT的加速版、簡化版實作")
    
    st.markdown("---")
    
    # 主要展示区域
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("### 🎯 項目背景")
        st.write("基於 DEoT 學術研究的深厚基礎，我們開發了 Impact Analyzer - 一個更加敏捷、實用的決策分析工具。")
        
        st.write("### ⚡ 核心特色")
        
        features = [
            "🚀 **加速版實作**: 將複雜的學術模型轉化為高效的實用工具",
            "🎨 **簡化版介面**: 保留核心功能，優化使用者體驗",
            "📊 **即時分析**: 快速處理數據，提供即時決策支援",
            "🔄 **敏捷開發**: 從學術研究到產品化的完整轉換",
            "💡 **實用導向**: 專為實際業務需求設計的分析工具"
        ]
        
        for feature in features:
            st.write(feature)
        
        st.write("### 🌐 立即體驗")
        st.markdown("**🔗 線上體驗**: [https://impact.nwstats.ai](https://impact.nwstats.ai)")
        st.info("點擊上方連結，立即體驗 Impact Analyzer 的強大功能！")
        
    with col2:
        st.write("### 📱 系統展示")
        try:
            st.image("assets/images/impact_analyzer.png", 
                    caption="Impact Analyzer 操作介面", 
                    width=400)
        except:
            st.info("🖥️ Impact Analyzer 介面（圖片載入中...）")
    
 