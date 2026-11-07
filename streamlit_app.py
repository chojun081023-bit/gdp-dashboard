from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:',  # This is an emoji shortcode. Could be a URL too.
    layout='centered',
)

# -----------------------------------------------------------------------------
# Declare some useful functions.


@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent / 'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df


gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page (mobile first: key numbers, then chart, filters tucked away)

st.title(':earth_americas: GDP dashboard')
st.caption('World Bank Open Data, 1960–2022. Some years are missing for some countries.')

min_value = int(gdp_df['Year'].min())
max_value = int(gdp_df['Year'].max())
countries = gdp_df['Country Code'].unique()
DEFAULT_COUNTRIES = ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN']

with st.expander('Filters', icon=':material/tune:'):
    from_year, to_year = st.slider(
        'Years',
        min_value=min_value,
        max_value=max_value,
        value=(min_value, max_value),
    )
    selected_countries = st.multiselect('Countries', countries, DEFAULT_COUNTRIES)

st.caption(f'{from_year}–{to_year} · {len(selected_countries)} countries')

if not selected_countries:
    st.warning('Select at least one country in Filters.')
    st.stop()

# GDP in billions, one row per year, one column per country: every lookup below is O(1).
gdp_b = (
    gdp_df[gdp_df['Country Code'].isin(selected_countries)]
    .pivot(index='Year', columns='Country Code', values='GDP')
    .loc[from_year:to_year, selected_countries]
    / 1e9
)

st.subheader(f'GDP in {to_year}', divider='gray')

# Wrapping row instead of st.columns: columns stack one per line on phones, this keeps 2 per row.
with st.container(horizontal=True, gap='small'):
    for country in selected_countries:
        first_gdp, last_gdp = gdp_b[country].loc[from_year], gdp_b[country].loc[to_year]

        if pd.isna(first_gdp) or pd.isna(last_gdp):
            growth, delta_color, arrow = 'n/a', 'off', 'off'
        else:
            growth, delta_color, arrow = f'{last_gdp / first_gdp:,.2f}x', 'normal', 'auto'

        st.metric(
            label=country,
            value='n/a' if pd.isna(last_gdp) else f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color,
            delta_arrow=arrow,
            border=True,
            width='stretch',
        )

st.subheader('GDP over time', divider='gray')

# Altair (ships with Streamlit) for plain year ticks and a legend that wraps on narrow screens.
chart_df = gdp_b.reset_index().melt('Year', var_name='Country', value_name='GDP')
chart = (
    alt.Chart(chart_df)
    .mark_line()
    .encode(
        x=alt.X('Year:Q', axis=alt.Axis(format='d', title=None)),
        y=alt.Y('GDP:Q', title='GDP (billion USD)'),
        color=alt.Color('Country:N', legend=alt.Legend(orient='bottom', columns=3, title=None)),
        tooltip=['Country', 'Year', alt.Tooltip('GDP:Q', format=',.0f')],
    )
    .properties(height=320)
)
st.altair_chart(chart)
