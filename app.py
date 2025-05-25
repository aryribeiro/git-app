"""
GitApp
A clean, professional Python/Streamlit application for browsing and copying Git commands.
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import json


class GitCommandsApp:
    """Professional Git Commands Reference Application"""
    
    def __init__(self):
        self.setup_page_config()
        self.load_data()
    
    def setup_page_config(self) -> None:
        """Configure Streamlit page settings"""
        st.set_page_config(
            page_title="GitApp - Comandos Git",
            page_icon="🔧",
            layout="centered",
            initial_sidebar_state="expanded"
        )
    
    def load_data(self) -> None:
        """Load Git commands data from CSV file"""
        try:
            csv_path = Path("comandos.csv")
            if not csv_path.exists():
                st.error("❌ Arquivo 'comandos.csv' não encontrado no diretório atual.")
                st.stop()
            
            self.df = pd.read_csv(csv_path)
            self.validate_data()
            
        except Exception as e:
            st.error(f"❌ Erro ao carregar dados: {str(e)}")
            st.stop()
    
    def validate_data(self) -> None:
        """Validate CSV data structure"""
        required_columns = ['comando', 'descrição', 'ordem_importância', 'como_pode_ser_usado']
        
        if not all(col in self.df.columns for col in required_columns):
            st.error("❌ Estrutura do CSV inválida. Colunas necessárias não encontradas.")
            st.stop()
        
        # Sort by importance
        self.df = self.df.sort_values('ordem_importância').reset_index(drop=True)
    
    def render_header(self) -> None:
        """Render application header"""
        st.markdown("""
        <div style='text-align: center; padding: 1rem 0;'>
            <h1 style='color: #2E86C1; margin-bottom: 0.5rem;'>
                🔧GitApp
            </h1>
            <p style='color: #566573; font-size: 1.1rem; margin-bottom: 2rem;'>
                <strong>Web App de Comandos Git</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    def render_sidebar_filters(self) -> dict:
        """Render sidebar filters and return filter values"""
        st.sidebar.markdown("""
        ### 🎯 Filtros de Pesquisa
        """)
        
        # Importance level filter
        importance_ranges = {
            "🔥 Essenciais (1-10)": (1, 10),
            "🚀 Intermediários (11-30)": (11, 30),
            "⚡ Avançados (31-60)": (31, 60),
            "🔧 Técnicos (61-100)": (61, 100),
            "🛠️ Específicos (101-157)": (101, 157),
            "📋 Todos os comandos": (1, 157)
        }
        
        selected_range = st.sidebar.selectbox(
            "Nível de Importância:",
            list(importance_ranges.keys()),
            index=0
        )
        
        min_imp, max_imp = importance_ranges[selected_range]
        
        # Search filter
        search_term = st.sidebar.text_input(
            "🔍 Buscar comando:",
            placeholder="Ex: commit, branch, merge..."
        ).lower().strip()
        
        return {
            'min_importance': min_imp,
            'max_importance': max_imp,
            'search_term': search_term
        }
    
    def filter_commands(self, filters: dict) -> pd.DataFrame:
        """Filter commands based on user selection"""
        filtered_df = self.df[
            (self.df['ordem_importância'] >= filters['min_importance']) &
            (self.df['ordem_importância'] <= filters['max_importance'])
        ].copy()
        
        if filters['search_term']:
            mask = (
                filtered_df['comando'].str.lower().str.contains(filters['search_term'], na=False) |
                filtered_df['descrição'].str.lower().str.contains(filters['search_term'], na=False)
            )
            filtered_df = filtered_df[mask]
        
        return filtered_df
    
    def render_command_selector(self, filtered_df: pd.DataFrame) -> dict:
        """Render command selection interface"""
        if filtered_df.empty:
            st.warning("🔍 Nenhum comando encontrado com os filtros aplicados.")
            return None
            
        st.markdown("### 📝 Selecione um Comando")
        
        # Create display options for selectbox
        command_options = []
        for _, row in filtered_df.iterrows():
            display_text = f"#{row['ordem_importância']:03d} - {row['comando']} - {row['descrição'][:50]}..."
            command_options.append(display_text)
        
        selected_index = st.selectbox(
            "Escolha o comando Git:",
            range(len(command_options)),
            format_func=lambda x: command_options[x],
            key="command_selector"
        )
        
        if selected_index is not None:
            return filtered_df.iloc[selected_index].to_dict()
        
        return None
    
    def render_command_details(self, selected_command: dict) -> None:
        """Render detailed view of selected command"""
        if not selected_command:
            return
            
        # Command header
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            ### 🎯 `{selected_command['comando']}`
            """)
        
        with col2:
            importance_color = self.get_importance_color(selected_command['ordem_importância'])
            st.markdown(f"""
            <div style='text-align: right; padding-top: 1rem;'>
                <span style='background-color: {importance_color}; color: white; 
                           padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem;'>
                    Importância: #{selected_command['ordem_importância']}
                </span>
            </div>
            """, unsafe_allow_html=True)
        
        # Description
        st.markdown(f"""
        **📄 Descrição:**  
        {selected_command['descrição']}
        """)
        
        # Usage examples
        st.markdown("**💡 Como usar:**")
        usage_examples = selected_command['como_pode_ser_usado'].split(', ')
        
        for i, example in enumerate(usage_examples, 1):
            example = example.strip()
            if example:
                st.code(example, language='bash')
        

    

    def get_importance_color(self, importance: int) -> str:
        """Get color based on command importance"""
        if importance <= 10:
            return "#E74C3C"  # Red - Essential
        elif importance <= 30:
            return "#F39C12"  # Orange - Intermediate
        elif importance <= 60:
            return "#3498DB"  # Blue - Advanced
        elif importance <= 100:
            return "#27AE60"  # Green - Technical
        else:
            return "#8E44AD"  # Purple - Specific

    def render_statistics(self, filtered_df: pd.DataFrame) -> None:
        """Render statistics sidebar"""
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📊 Estatísticas")
        
        total_commands = len(self.df)
        filtered_commands = len(filtered_df)
        
        st.sidebar.metric("Total de Comandos", total_commands)
        st.sidebar.metric("Comandos Filtrados", filtered_commands)
        
        # Distribution by importance
        essential = len(self.df[self.df['ordem_importância'] <= 10])
        intermediate = len(self.df[(self.df['ordem_importância'] > 10) & (self.df['ordem_importância'] <= 30)])
        advanced = len(self.df[self.df['ordem_importância'] > 30])
        
        st.sidebar.markdown(f"""
        **Distribuição:**
        - 🔥 Essenciais: {essential}
        - 🚀 Intermediários: {intermediate}
        - ⚡ Avançados: {advanced}
        """)
    
    def render_footer(self) -> None:
        """Render application footer"""
        
        total_commands = len(self.df)
        st.markdown(f"""
        <div style='text-align: center; color: #566573; padding: 2rem 0; 
                    background: white;
                    border-radius: 10px; margin-top: 2rem; 
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);'>
            <div style='padding: 1rem;'>
                <strong>
                    🔧GitApp: o seu web app de comandos Git
                </strong>
                <p style='font-size: 1rem; margin-bottom: 0.5rem; color: #34495e;'>
                    Desenvolvido por <strong>Ary Ribeiro</strong> - <a href="mailto:aryribeiro@gmail.com">aryribeiro@gmail.com</a></p>
                <p style='font-size: 0.9rem; color: #7f8c8d; margin-bottom: 1rem;'>
                    <em>Dica: Use os filtros na barra lateral p/ encontrar comandos</em>
                </p>
                <div style='border-top: 1px solid #bdc3c7; padding-top: 1rem; margin-top: 1rem;'>
                    <p style='font-size: 0.8rem; color: #95a5a6; margin: 0;'>
                        📚 {total_commands} comandos Git disponíveis | 
                        🚀 Interface moderna e intuitiva | 
                        🎯 Filtros avançados de pesquisa
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def run(self) -> None:
        """Main application execution"""
        # Render header
        self.render_header()
        
        # Get filters from sidebar
        filters = self.render_sidebar_filters()
        
        # Filter commands
        filtered_df = self.filter_commands(filters)
        
        # Render statistics
        self.render_statistics(filtered_df)
        
        # Main content
        selected_command = self.render_command_selector(filtered_df)
        
        if selected_command:
            self.render_command_details(selected_command)
        else:
            # Show welcome message when no command is selected
            st.markdown("""
            <div style='text-align: center; padding: 3rem 0; color: #566573;
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 15px; margin: 2rem 0;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
                <div style='color: white; padding: 2rem;'>
                    <h2 style='color: white; margin-bottom: 1rem;'>👋 Bem-vindo ao GitApp!</h2>
                    <p style='font-size: 1.1rem; margin-bottom: 1rem; opacity: 0.9;'>
                        Selecione um comando na lista acima para ver detalhes e exemplos de uso.
                    </p>
                    <p style='font-size: 1rem; opacity: 0.8;'>
                        💡 Use os filtros na barra lateral p/ encontrar comandos.
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Render footer
        self.render_footer()


def main():
    """Application entry point"""
    try:
        app = GitCommandsApp()
        app.run()
    except Exception as e:
        st.error(f"❌ Erro na aplicação: {str(e)}")
        st.info("🔄 Tente recarregar a página ou verifique os arquivos necessários.")


if __name__ == "__main__":
    main()

st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #333333;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    /* Esconde completamente todos os elementos da barra padrão do Streamlit */
    header {display: none !important;}
    footer {display: none !important;}
    #MainMenu {display: none !important;}
    /* Remove qualquer espaço em branco adicional */
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    /* Remove quaisquer margens extras */
    .element-container {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
</style>
""", unsafe_allow_html=True)