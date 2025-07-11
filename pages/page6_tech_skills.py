import streamlit as st

def render():
    """渲染技術學習展示页面"""
    st.title("🎓 技術學習成果")
    st.subheader("2025上半年技術成長軌跡")
    
    st.markdown("---")
    
    # 学习概览
    st.write("### 📊 學習概覽")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("技術領域", "6個", "100%")
    
    with col2:
        st.metric("核心技能", "20+", "深度學習")
    
    with col3:
        st.metric("應用項目", "14個", "實戰驗證")
    
    with col4:
        st.metric("學習時間", "6個月", "持續進步")
    
    st.markdown("---")
    
    # 技术分类展示
    st.write("### 🔧 技術分類詳解")
    
    # 创建六个选项卡
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📝 主題建模", "🌐 Web開發", "🤖 AI機器學習", 
        "📊 數據分析", "🔧 系統集成", "💼 業務應用"
    ])
    
    with tab1:
        st.write("#### 📝 主題建模與 NLP")
        st.write("深入學習自然語言處理和主題建模技術")
        
        tech_items = [
            ("🎯 **LDA (Latent Dirichlet Allocation)**", "傳統主題建模方法，理解文本主題分布"),
            ("🧠 **BERTopic**", "基於 BERT 的現代主題建模，更準確的語意理解"),
            ("🔍 **文本預處理**", "清洗、分詞、去噪等數據準備技術"),
            ("🏷️ **關鍵詞提取**", "從大量文本中提取重要信息和關鍵詞")
        ]
        
        for title, desc in tech_items:
            st.write(f"{title}")
            st.write(f"　　{desc}")
            st.write("")
        
        st.success("✅ **實戰應用**: NeuroWatt News 主題分析系統")
    
    with tab2:
        st.write("#### 🌐 Web 開發與可視化")
        st.write("構建用戶友好的數據應用和可視化界面")
        
        tech_items = [
            ("🎨 **Streamlit**", "快速構建數據應用，打造互動式界面"),
            ("📊 **數據可視化**", "圖表設計、趨勢分析、數據呈現"),
            ("📱 **響應式設計**", "適配多設備，優化用戶體驗"),
            ("🎭 **CSS 樣式調整**", "界面美化、主題設計、視覺優化")
        ]
        
        for title, desc in tech_items:
            st.write(f"{title}")
            st.write(f"　　{desc}")
            st.write("")
        
        st.success("✅ **實戰應用**: 完整展示系統、多個數據應用")
    
    with tab3:
        st.write("#### 🤖 AI 與機器學習")
        st.write("探索人工智能和機器學習的前沿技術")
        
        tech_items = [
            ("🎨 **Image Generation**", "圖像生成技術，創造視覺內容"),
            ("🧠 **Reasoning Model Research**", "推理模型研究，提升AI邏輯能力"),
            ("🌍 **多語言模型**", "中英文處理，跨語言應用"),
            ("👁️ **OCR 文字識別**", "PDF文字提取，文檔自動化處理")
        ]
        
        for title, desc in tech_items:
            st.write(f"{title}")
            st.write(f"　　{desc}")
            st.write("")
        
        st.success("✅ **實戰應用**: 法說會分析、圖像處理系統")
    
    with tab4:
        st.write("#### 📊 數據處理與分析")
        st.write("掌握數據處理和分析的核心技能")
        
        tech_items = [
            ("📄 **PDF 處理**", "文檔解析、預覽、內容提取"),
            ("📋 **JSON 數據處理**", "結構化數據操作、格式轉換"),
            ("🕷️ **網路爬蟲**", "數據採集、自動化信息獲取"),
            ("💰 **財務數據分析**", "法說會、財報分析、趨勢預測")
        ]
        
        for title, desc in tech_items:
            st.write(f"{title}")
            st.write(f"　　{desc}")
            st.write("")
        
        st.success("✅ **實戰應用**: US Trend Analyzer、財務分析系統")
    
    with tab5:
        st.write("#### 🔧 系統集成與優化")
        st.write("構建穩定可靠的系統架構")
        
        tech_items = [
            ("🔌 **API 集成**", "第三方服務接入，系統互聯"),
            ("🔄 **系統重構**", "架構優化，提升系統維護性"),
            ("⚡ **性能優化**", "加載速度提升，用戶體驗改善"),
            ("🛡️ **錯誤處理**", "異常管理，系統穩定性保障")
        ]
        
        for title, desc in tech_items:
            st.write(f"{title}")
            st.write(f"　　{desc}")
            st.write("")
        
        st.success("✅ **實戰應用**: 所有系統的穩定運行")
    
    with tab6:
        st.write("#### 💼 業務應用開發")
        st.write("將技術轉化為實際業務價值")
        
        tech_items = [
            ("📈 **投資策略分析**", "P1 Select 系統，民主化投資策略"),
            ("📰 **新聞分析系統**", "NeuroWatt News，智能資訊處理"),
            ("📊 **趨勢分析**", "US Trend Analyzer，市場洞察"),
            ("📋 **報告生成**", "自動化分析報告，提升工作效率")
        ]
        
        for title, desc in tech_items:
            st.write(f"{title}")
            st.write(f"　　{desc}")
            st.write("")
        
        st.success("✅ **實戰應用**: 多個高價值商業系統")
    
    st.markdown("---")
    
    # 学习心得
    st.write("### 💡 學習心得")
    
    insights = [
        "🎯 **理論與實踐並重**: 每項技術都通過實際項目驗證",
        "🔄 **持續迭代優化**: 從 LDA 到 BERTopic 的技術升級",
        "🌟 **用戶體驗優先**: 技術服務於實際需求",
        "📈 **商業價值導向**: 技術轉化為具體業務成果"
    ]
    
    for insight in insights:
        st.write(insight)
    
    st.markdown("---")
    
    # 未来展望
    st.write("### 🚀 未來展望")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🎯 短期目標**")
        st.write("• 深化 AI 推理模型研究")
        st.write("• 探索更多數據視覺化技術")
        st.write("• 提升系統性能和穩定性")
    
    with col2:
        st.write("**🌟 長期願景**")
        st.write("• 成為 AI 技術專家")
        st.write("• 建立完整的數據分析平台")
        st.write("• 推動技術創新和應用")
    
    st.success("🎓 **技術學習永無止境，每一天都是新的開始！**") 