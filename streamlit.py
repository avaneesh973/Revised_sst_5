
import streamlit as st
import model


st.title("Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank")

st.header("Training our model using SVM")

acc = model.print_accuracy()
st.text("The training accuracy is:" )
st.text(acc)

# name = st.text_input("Enter ur review about bahubali", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
# if(st.button('Submit')):
#     out = sst_2_logistic_regression.predict_sentiment(name)
#     st.text(out)

name1 = st.text_input("Enter ur review about bahubali, we will predict using sst5 trained model", "")

# # display the name when the submit button is clicked
# # .title() is used to get the input text string
if(st.button('PREDICT')):
    out = model.predict_sentiment_sentence(name1)
    st.text(out)
