import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config

ngrok_token = "2rbsysF7VUDlz0D8HdQPRxFkPj3_3kahZiBoKtmgWoLe8Ntij"

with tgb.Page() as page:    
  tgb.text(
      "# S&P 500",
      mode='md'
  )
  
gui = tp.Gui(page)
gui.run(title='Data Science Dashboard', ngrok_token=ngrok_token)