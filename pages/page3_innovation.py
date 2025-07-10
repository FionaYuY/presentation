import streamlit as st

def render():
    """渲染技術創新頁面"""
    # 使用HTML设置大标题
    st.markdown("""
    <h1 style="font-size: 4rem !important; font-weight: 700 !important; color: #ffffff !important; margin-bottom: 1rem !important;">
        🔥 技術創新亮點
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # NeuroWatt News 重構項目
    st.markdown("""
    <h2 style="font-size: 2.8rem !important; font-weight: 600 !important; color: #ffffff !important; margin-bottom: 1.5rem !important;">
        💎 NeuroWatt News：價值高達 56 萬的企業級產品
    </h2>
    """, unsafe_allow_html=True)
    
    # 項目背景說明
    st.write("### 📈 項目背景")
    st.write("NeuroWatt News 系統從 LDA 主題建模升級到 BERTopic，大幅提升了新聞分析的準確性和效率。")
    
    # 創建四個選項卡
    tab1, tab2, tab3, tab4 = st.tabs(["🚀 系統核心升級", "🧠 智能主題建模革新", "🎯 精準主題挑選系統", "🔧 多層驗證與情緒細化"])
    
    with tab1:
        st.markdown("""
        <h3 style="font-size: 2rem !important; font-weight: 600 !important; color: #ffffff !important; margin-bottom: 1rem !important;">
            🚀 系統核心升級
        </h3>
        """, unsafe_allow_html=True)
        
        st.write("#### 🔄 從 LDA 到 BERTopic 的技術升級")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**🏷️ LDA (舊版本)**")
            lda_features = [
                "基於詞袋模型",
                "主題數量需要預設", 
                "無法理解詞序和語境",
                "中文處理效果有限"
            ]
            for feature in lda_features:
                st.write(f"• {feature}")
        
        with col2:
            st.write("**🧠 BERTopic (新版本)**")
            bertopic_features = [
                "基於 BERT 語意理解",
                "動態主題數量生成",
                "深度理解語境和語意",
                "優秀的多語言支援"
            ]
            for feature in bertopic_features:
                st.write(f"✅ {feature}")
        
        st.success("📊 升級結果：主題分析準確度顯著提升，能更精準地識別新聞主題")
    
    with tab2:
        st.markdown("""
        <h3 style="font-size: 2rem !important; font-weight: 600 !important; color: #ffffff !important; margin-bottom: 1rem !important;">
            🧠 智能主題建模革新
        </h3>
        """, unsafe_allow_html=True)
        
        st.write("#### 🔍 5步驟主題挑選流程")
        
        steps = [
            ("1️⃣ 關鍵詞提取", "使用進階NLP技術提取新聞核心關鍵詞"),
            ("2️⃣ 主題聚類", "BERTopic自動將相似內容聚類成主題"),
            ("3️⃣ 主題篩選", "智能過濾低質量或重複主題"),
            ("4️⃣ 主題排序", "根據重要性和時效性排序"),
            ("5️⃣ 主題優化", "人工智能優化主題標題和描述")
        ]
        
        for step, description in steps:
            st.info(f"**{step}**: {description}")
        
        # 顯示NeuroWatt News圖片
        try:
            st.image("assets/images/neurowatt_news.png", 
                    caption="NeuroWatt News 主題分析示例", 
                    use_column_width=True)
        except:
            st.info("📷 NeuroWatt News 系統介面截圖")
    
    with tab3:
        st.markdown("""
        <h3 style="font-size: 2rem !important; font-weight: 600 !important; color: #ffffff !important; margin-bottom: 1rem !important;">
            🎯 精準主題挑選系統
        </h3>
        """, unsafe_allow_html=True)
        
        st.write("#### 📊 6步驟 Ticker 處理流程")
        
        ticker_steps = [
            "🏷️ **Ticker 標記**: 自動識別股票代碼和相關公司",
            "📈 **財務關聯**: 連結新聞內容與財務數據",
            "⏰ **時效性分析**: 評估新聞對股價的即時影響",
            "🎯 **重要性評分**: 根據多個維度評估新聞重要程度",
            "🔍 **相關性過濾**: 過濾無關或低價值資訊",
            "📊 **結果輸出**: 生成結構化的投資參考資訊"
        ]
        
        for step in ticker_steps:
            st.write(step)
        
        st.success("🎯 結果：為投資決策提供更精準的新聞分析和股票相關資訊")
    
    with tab4:
        st.markdown("""
        <h3 style="font-size: 2rem !important; font-weight: 600 !important; color: #ffffff !important; margin-bottom: 1rem !important;">
            🔧 多層驗證與情緒細化
        </h3>
        """, unsafe_allow_html=True)
        
        st.write("#### 🛡️ 品質保證機制")
        
        quality_features = [
            "**🔍 多層次驗證**: 確保新聞分析的準確性",
            "**😊 情緒分析**: 深度分析新聞情緒傾向",
            "**🌍 多語言支援**: 支援中英文混合內容分析",
            "**⚡ 即時處理**: 快速響應市場動態變化"
        ]
        
        for feature in quality_features:
            st.write(f"• {feature}")
        
        st.write("#### 💼 商業價值")
        
        business_value = [
            "📊 **資訊時效性大幅提升**: 即時掌握市場動態",
            "🎯 **分析準確度優化**: 更精準的投資建議",
            "🌐 **多語言內容處理**: 擴大資訊來源範圍",
            "⚡ **自動化程度提升**: 減少人工處理成本"
        ]
        
        for value in business_value:
            st.write(f"✅ {value}")
    
    st.markdown("---")
    
    # 技術成果總結
    st.write("### 🎯 技術成果總結")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("主題識別準確度", "大幅提升", "BERTopic升級")
    
    with col2:
        st.metric("處理速度", "即時分析", "流程優化")
        
    with col3:
        st.metric("產品價值", "56萬", "企業級")
    
    st.success("🚀 **NeuroWatt News 重構項目**: 從傳統 LDA 升級到先進 BERTopic，實現了企業級新聞分析平台的技術突破！") 