from time import sleep

from main import main

urls = ['https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br']

for url in urls:
    main(url)
    sleep(1)
    
    

