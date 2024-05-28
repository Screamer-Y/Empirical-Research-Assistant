import streamlit as st


if not st.session_state.openai_api_key.startswith('sk-'):
    st.warning("Please enter your OpenAI API key to enable generation feature.", icon="⚠")

st.markdown('''
            ### Hypothesis 1: Geometric patterns have a higher consistency in color usage compared to floral and abstract patterns.''')

st.code('''
        * Load the data
import excel "pattern_data.xlsx", sheet("Sheet1") firstrow clear

* Generate dummy variables for each pattern type
gen geometric = (PatternType == "geometric")
gen floral = (PatternType == "floral")
gen abstract = (PatternType == "abstract")

* Create a measure for color consistency (e.g., number of unique colors used)
* Assuming ColorPalette is a string of comma-separated colors
egen num_colors = rownonmiss(ColorPalette), strok

* Compare the average number of colors used across pattern types
regress num_colors geometric floral abstract
''')

st.markdown('''
            ### Hypothesis 2: Patterns with larger dimensions are more likely to be geometric.''')

st.code('''
        * Load the data
import excel "pattern_data.xlsx", sheet("Sheet1") firstrow clear

* Convert Dimensions to numeric values (assuming they are in the format 'widthxheight')
gen width = real(substr(Dimensions, 1, strpos(Dimensions, "x") - 1))
gen height = real(substr(Dimensions, strpos(Dimensions, "x") + 1, .))

* Calculate the area of each pattern
gen area = width * height

* Generate dummy variables for each pattern type
gen geometric = (PatternType == "geometric")
gen floral = (PatternType == "floral")
gen abstract = (PatternType == "abstract")

* Compare the average area across pattern types
regress area geometric floral abstract
''')

st.markdown('''### Hypothesis 3: Patterns with warmer color palettes (including red and yellow) are more likely to be floral.''')

st.code('''
        * Load the data
import excel "pattern_data.xlsx", sheet("Sheet1") firstrow clear

* Create dummy variables for the presence of specific colors
gen red_present = strpos(ColorPalette, "red") > 0
gen yellow_present = strpos(ColorPalette, "yellow") > 0

* Generate a dummy variable for warm color palettes
gen warm_palette = red_present | yellow_present

* Generate dummy variables for each pattern type
gen geometric = (PatternType == "geometric")
gen floral = (PatternType == "floral")
gen abstract = (PatternType == "abstract")

* Compare the likelihood of having a warm palette across pattern types
logit warm_palette geometric floral abstract
''')
            