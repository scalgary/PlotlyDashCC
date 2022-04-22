import plotly.graph_objects as go


def pie_chart():
# Add data
  labels= ['Boys', 'Girls']
  values = [48133355,32546308]


  common_props = dict(labels=labels,
                    values=values,)

  fig = go.Figure()
  fig.add_trace(go.Pie(
    **common_props,
    textinfo='label',
    textposition='outside',
    marker_colors = ["lightblue","pink"]))
  fig.add_trace(go.Pie(
    **common_props,
    textinfo='percent',
    textposition='inside',
    textfont_color= 'white'))
  
  fig.update_traces(showlegend=False)
  fig.update_layout(
    title_text='Genders', 
    title_x=0.1,
    title_y = 0.9)

  return fig


if __name__ == '__main__':
  fig=make_pie1()
  print(fig)