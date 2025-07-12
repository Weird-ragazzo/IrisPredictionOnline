# IrisPredictor.py - Enhanced Dark Modern Version

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import streamlit.components.v1 as components
import time

# ----------------------------
# Enhanced Dark Modern Styling
# ----------------------------
def inject_modern_dark_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Dark Theme */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }
    
    /* Animated Dark Background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(255, 107, 107, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(132, 94, 194, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(255, 159, 243, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 60% 60%, rgba(58, 123, 213, 0.15) 0%, transparent 50%);
        animation: backgroundPulse 15s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes backgroundPulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.05); }
    }
    
    /* Flower Cursor */
    * {
        cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><g fill="%23ff69b4"><circle cx="16" cy="8" r="4"/><circle cx="24" cy="16" r="4"/><circle cx="16" cy="24" r="4"/><circle cx="8" cy="16" r="4"/><circle cx="16" cy="16" r="3" fill="%23ffd700"/></g></svg>'), auto;
    }
    
    /* Sparkly Trail */
    .sparkle {
        position: fixed;
        width: 6px;
        height: 6px;
        background: radial-gradient(circle, #ffd700 0%, #ff69b4 50%, transparent 100%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        animation: sparkleFloat 2s ease-out forwards;
    }
    
    @keyframes sparkleFloat {
        0% { opacity: 1; transform: scale(0); }
        50% { opacity: 1; transform: scale(1) rotate(180deg); }
        100% { opacity: 0; transform: scale(0) rotate(360deg); }
    }
    
    /* Glass morphism containers - Dark */
    .main-container {
        background: rgba(30, 30, 30, 0.4);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }
    
    .main-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(255, 107, 107, 0.2);
    }
    
    /* Title styling - Bright */
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #ff6b6b 0%, #845ec2 50%, #ff9ff3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: 0 0 20px rgba(255, 107, 107, 0.5);
        animation: titleGlow 3s ease-in-out infinite;
    }
    
    @keyframes titleGlow {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.2); }
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        text-align: center;
        color: #ffffff;
        margin-bottom: 2rem;
        font-weight: 400;
        opacity: 0.9;
    }
    
    /* Tab styling - Dark */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(20, 20, 20, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 0.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        color: #ffffff;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 107, 107, 0.2);
        transform: translateY(-2px);
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #ff6b6b 0%, #845ec2 100%);
        color: white;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
    }
    
    /* Button styling - Enhanced */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #845ec2 100%);
        color: white;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.6);
    }
    
    /* Loading spinner */
    .loading-spinner {
        display: inline-block;
        width: 40px;
        height: 40px;
        border: 3px solid rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        border-top-color: #ff6b6b;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Selectbox styling - Dark */
    .stSelectbox > div > div {
        background: rgba(30, 30, 30, 0.8);
        border: 2px solid rgba(255, 107, 107, 0.3);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .stSelectbox > div > div > select {
        background: transparent;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
    }
    
    /* Slider styling - Enhanced */
    .stSlider > div > div > div > div {
        background: linear-gradient(135deg, #ff6b6b 0%, #845ec2 100%);
    }
    
    .stSlider > div > div > div[role="slider"] {
        background: #ffffff;
        border: 3px solid #ff6b6b;
        box-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
    }
    
    /* Success/Info boxes - Dark */
    .stSuccess {
        background: rgba(76, 175, 80, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(76, 175, 80, 0.5);
        color: #ffffff;
    }
    
    .stInfo {
        background: rgba(33, 150, 243, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(33, 150, 243, 0.5);
        color: #ffffff;
    }
    
    /* Chart container - Dark */
    .chart-container {
        background: rgba(30, 30, 30, 0.8);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Scroll animations */
    .scroll-animation {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.8s ease;
    }
    
    .scroll-animation.visible {
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Floating elements animation */
    .floating {
        animation: floating 4s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(2deg); }
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #ff6b6b 0%, #845ec2 100%);
    }
    
    /* DataFrames */
    .stDataFrame {
        background: rgba(30, 30, 30, 0.8);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Text styling */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    p, span, div {
        color: #ffffff;
    }
    
    /* Sidebar styling */
    .stSidebar {
        background: rgba(20, 20, 20, 0.9);
        backdrop-filter: blur(20px);
    }
    </style>
    """, unsafe_allow_html=True)

def inject_enhanced_effects():
    effects_js = """
    <script>
    // Sparkly cursor trail
    let sparkles = [];
    let mouseX = 0;
    let mouseY = 0;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        // Create sparkle
        if (Math.random() < 0.3) {
            createSparkle(mouseX, mouseY);
        }
    });
    
    function createSparkle(x, y) {
        const sparkle = document.createElement('div');
        sparkle.className = 'sparkle';
        sparkle.style.left = (x - 3) + 'px';
        sparkle.style.top = (y - 3) + 'px';
        sparkle.style.background = `radial-gradient(circle, hsl(${Math.random() * 360}, 100%, 70%) 0%, transparent 70%)`;
        document.body.appendChild(sparkle);
        
        setTimeout(() => {
            sparkle.remove();
        }, 2000);
    }
    
    // Scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    // Observe all containers
    setTimeout(() => {
        const containers = document.querySelectorAll('.main-container');
        containers.forEach(container => {
            container.classList.add('scroll-animation');
            observer.observe(container);
        });
    }, 100);
    
    // Enhanced particles
    function createFloatingParticles() {
        const colors = ['#ff6b6b', '#845ec2', '#ff9ff3', '#ffd93d', '#6bcf7f'];
        
        for (let i = 0; i < 5; i++) {
            const particle = document.createElement('div');
            particle.style.position = 'fixed';
            particle.style.width = '4px';
            particle.style.height = '4px';
            particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            particle.style.borderRadius = '50%';
            particle.style.pointerEvents = 'none';
            particle.style.zIndex = '1000';
            particle.style.left = Math.random() * window.innerWidth + 'px';
            particle.style.top = Math.random() * window.innerHeight + 'px';
            particle.style.animation = `floatUp ${3 + Math.random() * 4}s linear infinite`;
            
            document.body.appendChild(particle);
            
            setTimeout(() => {
                particle.remove();
            }, 7000);
        }
    }
    
    // Add floating particles CSS
    const style = document.createElement('style');
    style.textContent = `
        @keyframes floatUp {
            0% { transform: translateY(0) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
    
    // Create particles periodically
    setInterval(createFloatingParticles, 2000);
    
    // Add click ripple effect
    document.addEventListener('click', (e) => {
        const ripple = document.createElement('div');
        ripple.style.position = 'fixed';
        ripple.style.left = e.clientX + 'px';
        ripple.style.top = e.clientY + 'px';
        ripple.style.width = '0px';
        ripple.style.height = '0px';
        ripple.style.borderRadius = '50%';
        ripple.style.background = 'rgba(255, 107, 107, 0.3)';
        ripple.style.pointerEvents = 'none';
        ripple.style.zIndex = '9999';
        ripple.style.animation = 'ripple 0.8s ease-out';
        
        document.body.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 800);
    });
    
    // Add ripple animation
    const rippleStyle = document.createElement('style');
    rippleStyle.textContent = `
        @keyframes ripple {
            0% { width: 0; height: 0; opacity: 0.5; }
            100% { width: 100px; height: 100px; opacity: 0; transform: translate(-50px, -50px); }
        }
    `;
    document.head.appendChild(rippleStyle);
    </script>
    """
    components.html(effects_js, height=0)

# ----------------------------
# Loading Animation Component
# ----------------------------
def show_loading_animation(message="Loading..."):
    loading_placeholder = st.empty()
    loading_placeholder.markdown(f"""
    <div style="text-align: center; padding: 2rem;">
        <div class="loading-spinner"></div>
        <p style="margin-top: 1rem; color: #ffffff; font-size: 1.2rem;">{message}</p>
    </div>
    """, unsafe_allow_html=True)
    return loading_placeholder

# ----------------------------
# Function to load models with loading animation
# ----------------------------
@st.cache_resource
def load_models():
    try:
        models = {
            "🌸 Logistic Regression": joblib.load("IrisLogRegModel.pkl"),
            "🌺 K-Nearest Neighbors": joblib.load("IrisKNN.pkl"),
            "🌷 Support Vector Machine": joblib.load("IrisSVM.pkl"),
            "🌳 Decision Tree": joblib.load("IrisDT.pkl")
        }
        scaler = joblib.load("IrisLogRegModel_scaler.pkl")
        return models, scaler
    except FileNotFoundError as e:
        st.error(f"❌ Model file not found: {e}")
        return None, None

# ----------------------------
# Function to predict species with loading
# ----------------------------
def predict_species(model, input_scaled):
    pred = model.predict(input_scaled)[0]
    if hasattr(model, "predict_proba"):
        probas = model.predict_proba(input_scaled)[0]
    else:
        probas = None
    return pred, probas

# ----------------------------
# Enhanced result display
# ----------------------------
def display_result(pred, probas, model_name):
    target_names = ['Setosa 🌸', 'Versicolor 🌺', 'Virginica 🌷']
    species_name = target_names[pred]
    
    st.markdown("""
    <div class="main-container floating">
        <h2 style="text-align: center; color: #ff6b6b; font-family: 'Poppins', sans-serif; font-size: 2.5rem;">
            ✨ Prediction Results ✨
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success(f"🎯 **Predicted Species:** {species_name}")
        st.info(f"🔍 **Model Used:** {model_name}")
        
        if probas is not None:
            st.markdown("#### 📊 **Confidence Scores:**")
            for i, prob in enumerate(probas):
                st.markdown(f"**{target_names[i]}:** {prob:.2%}")
                st.progress(prob)
    
    with col2:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #ff6b6b 0%, #845ec2 100%);
            height: 250px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 2.5rem;
            font-family: 'Poppins', sans-serif;
            box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3);
            animation: floating 3s ease-in-out infinite;
        ">
            {species_name}
        </div>
        """, unsafe_allow_html=True)
    
    st.balloons()

# ----------------------------
# Main App
# ----------------------------
def main():
    # Page config
    st.set_page_config(
        page_title="🌸 Iris Predictor",
        page_icon="🌸",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Inject styling and effects
    inject_modern_dark_style()
    inject_enhanced_effects()
    
    # Show loading animation while loading models
    loading_placeholder = show_loading_animation("Loading AI Models...")
    
    # Load models
    models, scaler = load_models()
    
    # Clear loading animation
    loading_placeholder.empty()
    
    if models is None:
        st.error("❌ Failed to load models. Please check your model files.")
        return
    
    # Model accuracies
    model_accuracies = {
        "🌸 Logistic Regression": "97%",
        "🌺 K-Nearest Neighbors": "100%",
        "🌷 Support Vector Machine": "100%",
        "🌳 Decision Tree": "100%"
    }
    
    # App title
    st.markdown("""
    <div class="main-container">
        <h1 class="main-title">🌸 Iris Predictor</h1>
        <p class="subtitle">AI-Powered Iris Species Classification with Advanced Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["🤖 Model Selection", "📊 Input Features", "🎯 Prediction"])
    
    # ----------------------------
    # Tab 1: Model Selection
    # ----------------------------
    with tab1:
        st.markdown("""
        <div class="main-container">
            <h2 style="color: #ff6b6b; font-family: 'Poppins', sans-serif; text-align: center; font-size: 2.5rem;">
                🧠 Choose Your AI Model
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            model_choice = st.selectbox(
                "🔍 Select Machine Learning Model:",
                tuple(models.keys()),
                help="Each model uses different algorithms to classify iris flowers"
            )
            
            st.markdown(f"""
            <div class="main-container" style="text-align: center; margin-top: 2rem;">
                <h3 style="color: #ff9ff3; margin: 0; font-size: 1.5rem;">Model Accuracy</h3>
                <h2 style="color: #ffd93d; margin: 0.5rem 0; font-size: 3rem; text-shadow: 0 0 10px rgba(255, 217, 61, 0.5);">
                    {model_accuracies[model_choice]}
                </h2>
                <p style="color: #ffffff; opacity: 0.8;">Tested on validation dataset</p>
            </div>
            """, unsafe_allow_html=True)
    
    # ----------------------------
    # Tab 2: Input Features
    # ----------------------------
    with tab2:
        st.markdown("""
        <div class="main-container">
            <h2 style="color: #ff6b6b; font-family: 'Poppins', sans-serif; text-align: center; font-size: 2.5rem;">
                🌿 Enter Flower Measurements
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🌸 Sepal Measurements")
            sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8, 0.1)
            sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0, 0.1)
        
        with col2:
            st.markdown("#### 🌺 Petal Measurements")
            petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.35, 0.1)
            petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3, 0.1)
        
        # Prepare input data
        input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                                columns=['sepal length (cm)', 'sepal width (cm)',
                                         'petal length (cm)', 'petal width (cm)'])
        
        input_scaled = scaler.transform(input_df)
        
        # Display input summary
        st.markdown("""
        <div class="main-container">
            <h4 style="color: #ff9ff3; text-align: center; margin-bottom: 1rem;">📋 Input Summary</h4>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(input_df.round(2), use_container_width=True)
    
    # ----------------------------
    # Tab 3: Prediction
    # ----------------------------
    with tab3:
        st.markdown("""
        <div class="main-container">
            <h2 style="color: #ff6b6b; font-family: 'Poppins', sans-serif; text-align: center; font-size: 2.5rem;">
                🎯 Get Your Prediction
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("✨ Predict Iris Species", use_container_width=True):
                # Show prediction loading
                pred_loading = show_loading_animation("🔮 Analyzing flower characteristics...")
                time.sleep(1)  # Simulate processing time
                
                model = models[model_choice]
                pred, probas = predict_species(model, input_scaled)
                
                pred_loading.empty()
                display_result(pred, probas, model_choice)
                
                # Create enhanced visualization
                st.markdown("""
                <div class="main-container">
                    <h4 style="color: #ff9ff3; text-align: center; margin-bottom: 1rem;">
                        📊 Species Distribution Visualization
                    </h4>
                </div>
                """, unsafe_allow_html=True)
                
                iris = load_iris(as_frame=True)
                df = iris.frame
                
                # Set dark theme for matplotlib
                plt.style.use('dark_background')
                fig, ax = plt.subplots(figsize=(12, 8))
                fig.patch.set_facecolor('#1a1a2e')
                ax.set_facecolor('#1a1a2e')
                
                # Plot dataset
                target_names = ['Setosa', 'Versicolor', 'Virginica']
                colors = ['#ff6b6b', '#845ec2', '#ff9ff3']
                
                for i, (target, color) in enumerate(zip(target_names, colors)):
                    mask = df['target'] == i
                    ax.scatter(df[mask]['petal length (cm)'], df[mask]['petal width (cm)'], 
                             c=color, label=target, s=80, alpha=0.8, edgecolors='white', linewidth=1)
                
                # Plot user input
                ax.scatter(petal_length, petal_width, color='#ffd93d', s=300, 
                          label='Your Input', edgecolor='white', linewidth=3, marker='*')
                
                ax.set_xlabel('Petal Length (cm)', fontsize=14, fontweight='bold', color='white')
                ax.set_ylabel('Petal Width (cm)', fontsize=14, fontweight='bold', color='white')
                ax.set_title('Petal Length vs Width Distribution', fontsize=16, fontweight='bold', color='white')
                ax.legend(fontsize=12, framealpha=0.9)
                ax.grid(True, alpha=0.3, color='white')
                
                # Style the plot
                ax.spines['bottom'].set_color('white')
                ax.spines['top'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.spines['left'].set_color('white')
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')
                
                st.pyplot(fig)
    
    # Footer
    st.markdown("""
    <div class="main-container" style="margin-top: 3rem;">
        <p style="text-align: center; color: #ff9ff3; font-family: 'Inter', sans-serif; font-size: 1.2rem;">
            🌸 Built with ❤️ using Streamlit and Advanced ML Algorithms 🌸
        </p>
        <p style="text-align: center; color: #ffffff; opacity: 0.7; margin-top: 1rem;">
            Created by Dhruv Raghav | Enhanced Dark Edition
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()