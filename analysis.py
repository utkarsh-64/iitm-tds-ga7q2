import marimo as mo
import pandas as pd
import numpy as np

# analysis.py
# Data Scientist: Technical Consultant
# Contact: 23f1001207@ds.study.iitm.ac.in

# Cell 1: Setup and Data Generation
# This cell runs first and creates our base dataset.
# The variables 'mo' and 'raw_data' defined here are available to other cells.
mo.md("# Interactive Analysis of Synthetic Sales Data")
raw_data = pd.DataFrame({
    'month': range(1, 13),
    'advertising_spend': np.random.randint(1000, 5000, size=12),
    'customer_visits': np.random.randint(500, 2000, size=12),
})
# We add a 'sales' column that is correlated with the other two variables.
raw_data['sales'] = (
    raw_data['advertising_spend'] * 2.5 +
    raw_data['customer_visits'] * 5 +
    np.random.randint(-5000, 5000, size=12)
).astype(int)

# Cell 2: Interactive Widget
# This cell defines our interactive slider.
# The 'advertising_slider' object can be referenced by other cells,
# and its 'value' will always be up-to-date.
advertising_slider = mo.ui.slider(
    1000, 5000, step=100, value=2500,
    label="Minimum Advertising Spend:"
)

# Cell 3: Display the Widget and its Value
# This cell depends on 'advertising_slider' from Cell 2.
# It displays the slider UI element and its current value.
mo.md(f"""
    Use the slider to filter the data based on the minimum monthly ad spend.
    {advertising_slider}
""")


# Cell 4: Data Filtering
# This cell has a dependency on 'raw_data' (from Cell 1) and
# 'advertising_slider' (from Cell 2).
# When the slider's value changes, this cell automatically re-runs.
min_spend = advertising_slider.value
filtered_data = raw_data[raw_data['advertising_spend'] >= min_spend]


# Cell 5: Dynamic Markdown and Data Display
# This cell depends on 'filtered_data' (from Cell 4) and 'min_spend' (from Cell 4).
# Its output updates automatically whenever 'filtered_data' changes.
# This demonstrates how UI state flows through the notebook to the final output.
mo.md(f"""
    ### Analysis Results
    
    Showing data for months with advertising spend of **${min_spend}** or more.
    
    **Months matching criteria:** {len(filtered_data)}
    
    {mo.ui.table(filtered_data, selection=None)}
""")

# Cell 6: A simple static cell for explanation
mo.md(
    "**Data Flow Documentation:** "
    "`Cell 1` creates the `raw_data`. "
    "`Cell 2` creates the `advertising_slider`. "
    "`Cell 4` uses both `raw_data` and the slider's value to create `filtered_data`. "
    "`Cell 5` uses `filtered_data` to render the final output table and summary."
)
