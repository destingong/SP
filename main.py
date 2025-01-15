import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config
from tokens import NGROK_TOKEN

with tgb.Page() as page:    
  tgb.text(
      "# S&P 500",
      mode='md'
  )
  
gui = tp.Gui(page)
gui.run(title='Data Science Dashboard', ngrok_token=NGROK_TOKEN)