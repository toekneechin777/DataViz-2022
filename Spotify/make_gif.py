import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv('most-streamed-artist-monthly-cleaned.csv')

df = df.set_index("Date")

bcr.bar_chart_race(df,
                  filename='./spotify_artists.gif',
                  img_label_folder='./images_test',
                  tick_image_mode='fixed',
                  title='Most streamed artist monthly on Spotify',
                  steps_per_period=50,
		  fig_kwargs={
			'figsize': (26,15)
		  },
                  period_label={'x': .99, 'y': .05, 'ha': 'right', 'va': 'center'},
                  orientation='h',
                  n_bars=10
                  )
