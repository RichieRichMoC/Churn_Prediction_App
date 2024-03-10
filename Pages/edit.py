import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
 
st.set_page_config(
    page_title='Dashboard',
    page_icon='📈',
    layout='wide'
)
 
# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the homepage.')
else:
 
    st.title('Dashboard')
 
    # Access data from session state
    data = st.session_state.get("data_key", None)
    churn_rate = (data["Churn"].sum() / data.shape[0]) * 100
    average_tenure = data['tenure'].mean()
    average_monthly_charges = data['MonthlyCharges'].mean()
    total_revenue = data['MonthlyCharges'].sum()



    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>KPI's</h1>", unsafe_allow_html=True)
    if data is not None:
        
           with st.container():
                      
                        cpp1, cpp2,cpp3, cpp4 = st.columns(4)
                        with cpp1:
                     
                         st.markdown(
                f"""
                   
                           <div style="background-color: #009900; border-radius: 10px; width: 80%; margin-top: 20px;" >
                  
                         <h4 style="margin-left: 30px"> Churn Rate:
                         </br>
                          </br>
                           
                         {churn_rate:.2f}%. </h4>
                             </div>
                """,
                unsafe_allow_html=True,
            )

                   
                        with cpp2:
                         st.markdown(
                f"""
                   
                           <div style="background-color: #ff9900; border-radius: 10px; width: 80%; margin-top: 20px;" >
                  
                         <h4 style="margin-left: 30px">Average Tenure: 
                          </br>
                          </br>
                         {average_tenure:.2f} </h4>
                             </div>
                """,
                unsafe_allow_html=True,
            )

                        
                        with cpp3:
                         st.markdown(
                f"""
                   
                           <div style="background-color: #3399ff; border-radius: 10px; width: 80%; margin-top: 20px;" >
                 
                          <h4 style="margin-left: 30px">Avg Mon Chgs:
                            </br>
                          </br>
                            ${average_monthly_charges:.2f}</h4>
                             </div>
                """,
                unsafe_allow_html=True,
            )

                        
                        with cpp4:
                         st.markdown(
                f"""
                   
                           <div style="background-color: #ff6600; border-radius: 10px; width: 80%; margin-top: 20px;" >
                  
                        <h4 style="margin-left: 30px">Total Revenue: 
                        
                          </br>
                          </br>
                        ${total_revenue:.2f}</h4>
                             </div>
                """,
                unsafe_allow_html=True,
            )

                                  
    def main():
        
         
            

        st.markdown("<hr>", unsafe_allow_html=True)           
        st.markdown("<h1 style='text-align: center;'>EDA's</h1>", unsafe_allow_html=True)
        with st.container():
                    
                    st.header('Univariate')
                    co1, co2 = st.columns(2)
                                   
                    with co1:
                        fig = px.histogram(data, x="Contract", color="Contract", barmode="group", height=400, width=500)
                        fig.update_yaxes(title_text=None)
                        st.plotly_chart(fig)
 
                    with co2:
                        fig = px.box(data, x="tenure", height=400, width=500)
                        st.plotly_chart(fig)
        with st.container():
                    cn1, cn2 = st.columns(2)
                   
                    with cn1:
                        fig = px.histogram(data, x="TotalCharges", height=400, width=500)
                        fig.update_yaxes(title_text=None)
                        st.plotly_chart(fig)
 
                    with cn2:
                        fig = px.histogram(data, x="MonthlyCharges", height=400, width=500)
                        fig.update_yaxes(title_text=None)
                        st.plotly_chart(fig)
                       
        with st.container():
                    st.header('Bivariate')
                    c1, c2 = st.columns(2)
               
                    with c1:
                        senior_citizen_pie = px.pie(data, names='SeniorCitizen', title='Churn rate: Senior Vs Non-senior Citizens')
                        st.plotly_chart(senior_citizen_pie, use_container_width=True)
 
                    with c2:
                        fig = px.histogram(data, x='PaymentMethod', color='Churn', barmode='stack',
                                color_discrete_map={'Yes': 'Firebrick', 'No': 'blue'},
                                labels={'PaymentMethod': 'Payment Method', 'Churn': 'Churn'},
                                title='Churn Patterns by Payment Method')
                        fig.update_layout(xaxis_title='Payment Method', yaxis_title='Count', showlegend=True)
                        st.plotly_chart(fig, use_container_width=True)        
                   
        with st.container():
                    st.header('Multivariate')
                    ca1, ca2 = st.columns(2)
                   
 
                    with ca1:  
                        data1 = data[["tenure", "MonthlyCharges", "TotalCharges", "Churn"]]
                        fig = px.scatter_matrix(data1, dimensions=["tenure", "MonthlyCharges", "TotalCharges"],
                                            color="Churn", symbol="Churn", title="Pairplot of Churn Features")
                        st.plotly_chart(fig, use_container_width=True)
 
                    with ca2:
                        correlation_matrix = data.corr(numeric_only=True)
                        plt.figure(figsize=(10, 8))
                        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
                        plt.title("Correlation Matrix")
                        st.pyplot(plt)
                           

          
 
    if __name__ == '__main__':
              main()
 
    
 
          