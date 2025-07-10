import streamlit as st

def render():
    """渲染學術研究成果頁面"""
    st.title("學術研究成果")
    st.header("代表作品：DEoT (Dual Engines of Thoughts) 論文")
    
    # 使用分頁來組織內容
    tab1, tab2, tab3, tab4 = st.tabs(["📊 研究架構", "🏆 實驗成果", "👥 作者團隊", "🎯 研究成就"])
    
    with tab1:
        st.subheader("研究架構圖")
        st.write("DEoT (Dual Engines of Thoughts) 是一個創新的雙引擎推理框架，以下展示核心架構設計：")
        
        # 架構圖展示
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("#### 分析框架")
            try:
                st.image("assets/images/Analytical_Framework.jpg", 
                        caption="DEoT 分析框架架構圖", 
                        use_column_width=True)
            except:
                st.error("無法載入分析框架圖")
                
        with col2:
            st.write("#### 樹狀結構圖")
            try:
                st.image("assets/images/DEoT_Tree_Graph.jpg", 
                        caption="DEoT 樹狀推理結構", 
                        use_column_width=True)
            except:
                st.error("無法載入樹狀結構圖")
        
        st.markdown("---")
        st.write("### 技術創新特點：")
        innovations = [
            "🔬 **雙引擎推理系統**：創新的Base Prompter + Solver Agent架構",
            "🌟 **智能決策樹**：動態生成推理路徑的樹狀結構",
            "⚡ **高效問題解決**：多領域問題的統一框架解決方案",
            "🎯 **適應性學習**：根據問題複雜度自動調整推理策略"
        ]
        for innovation in innovations:
            st.write(innovation)
    
    with tab2:
        st.subheader("實驗成果展示")
        st.write("經過超過600題的深度實驗評估，DEoT在多個領域展現出優異的性能表現：")
        
        # 成果圖展示
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("#### GPT-4o 性能比較")
            try:
                st.image("assets/images/gpt4o_comparison_2.jpg", 
                        caption="DEoT vs GPT-4o 性能對比分析", 
                        use_column_width=True)
            except:
                st.error("無法載入GPT-4o比較圖")
                
        with col2:
            st.write("#### 消融實驗結果")
            try:
                st.image("assets/images/Ablation Experiment_Domains.jpg", 
                        caption="不同領域的消融實驗結果", 
                        use_column_width=True)
            except:
                st.error("無法載入消融實驗圖")
        
        st.markdown("---")
        st.write("### 實驗亮點：")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="實驗題目數量",
                value="600+",
                delta="涵蓋多領域"
            )
        
        with col2:
            st.metric(
                label="性能提升",
                value="顯著",
                delta="vs GPT-4o"
            )
            
        with col3:
            st.metric(
                label="應用領域",
                value="多元",
                delta="跨域驗證"
            )
    
    with tab3:
        st.subheader("研究團隊")
        st.write("### 作者名單：")
        
        # 作者信息展示
        authors_data = [
            {"姓名": "Fiona*", "角色": "共同第一作者", "貢獻": "架構設計、研究設計、實驗執行、論文撰寫"},
            {"姓名": "Oro*", "角色": "共同第一作者", "貢獻": "架構設計、研究設計、實驗執行、論文撰寫"},
            {"姓名": "Luka", "角色": "共同作者", "貢獻": "創意發想"},
            {"姓名": "Chun-Cheng Lin (林俊成)†", "角色": "通訊作者", "貢獻": "項目指導、論文審核"},
            {"姓名": "Peter", "角色": "共同作者", "貢獻": "金主、誇大效果，吸引外界注意力"},
            {"姓名": "Nasha", "角色": "共同作者", "貢獻": "金主"}
        ]
        
        for i, author in enumerate(authors_data, 1):
            with st.container():
                col1, col2, col3 = st.columns([1, 2, 3])
                with col1:
                    if "林俊成" in author["姓名"]:
                        st.write(f"**{i}. {author['姓名']}**")
                    elif "*" in author["姓名"]:
                        st.write(f"**{i}. {author['姓名']}**")
                    else:
                        st.write(f"{i}. {author['姓名']}")
                with col2:
                    if "共同第一" in author["角色"]:
                        st.success(author["角色"])
                    elif "通訊" in author["角色"]:
                        st.info(author["角色"])
                    else:
                        st.write(author["角色"])
                with col3:
                    st.write(author["貢獻"])
        
        st.markdown("---")
        st.write("### 註記說明：")
        st.write("• **\\*** 表示共同第一作者 (Co-first authors)")
        st.write("• **†** 表示通訊作者 (Corresponding author)")
        
    with tab4:
        st.subheader("研究成就總覽")
        
        # 研究成就
        st.write("### 🏆 主要成就：")
        achievements = [
            "📝 **論文投稿**：成功投稿至 arXiv 和 Artificial Intelligence Journal",
            "🔬 **實驗規模**：完成超過600題的深度實驗評估",
            "💼 **商業轉化**：將學術研究成功轉化為商業應用",
            "🛡️ **專利保護**：已提交相關技術專利申請",
            "🌟 **技術突破**：建立了突破性的雙引擎推理框架",
            "🏢 **企業價值**：為公司建立了重要的技術護城河",
            "🌍 **影響範圍**：DEoT技術已應用到多個實際商業項目"
        ]
        
        for achievement in achievements:
            st.write(achievement)
            
        st.markdown("---")
        
        # 總結指標
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="論文狀態",
                value="已投稿",
                delta="待審核中"
            )
        
        with col2:
            st.metric(
                label="專利狀態", 
                value="申請中",
                delta="技術保護"
            )
            
        with col3:
            st.metric(
                label="商業應用",
                value="多項目",
                delta="成功轉化"
            )
            
        with col4:
            st.metric(
                label="團隊規模",
                value="6人",
                delta="跨領域合作"
            )
            
        st.success("🎉 DEoT 項目：從學術研究到商業應用的成功典範！") 