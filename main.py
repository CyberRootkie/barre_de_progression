# Source : https://stacklima.com/python-comment-creer-une-barre-de-progression-de-terminal-en-utilisant-tqdm/

from tqdm import tqdm
from time import sleep
 
 
for i in tqdm(range(0, 1000), desc = "Texte personnalis√©"):
    sleep(.1)
 
print("Termin√© !")