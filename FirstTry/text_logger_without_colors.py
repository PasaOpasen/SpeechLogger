from textblob import TextBlob
import speech_recognition as sr
             
def speech_to_text_from_micro(lang = 'ru-RU'):
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source, 0.5) 
        
        print(f"TALK ({lang[:2]})")
        audio_text = r.listen(source)
        print("Okay. Stop talking")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        return r.recognize_google(audio_text, language = lang)
    except Exception as e:
        print(e)
        return 'bad result of recognition'

             
def log_text(text, lang_of_text=None, lang_list = ['en','ru']):
    
    if len(text) < 3:
        print('too small text:',end=' ')
        print(text)
        return
    
    blob = TextBlob(text)
    if lang_of_text == None:
        lang_of_text = blob.detect_language()

    bool_list = [r != lang_of_text for r in lang_list]
    
    for lang, it in zip(lang_list, bool_list):
        print(f'\t {lang}:', end=' ')
        if it:
            print(str(blob.translate(from_lang = lang_of_text, to = lang)))
        else:
            print(f'{text} (original text)')

def do_log_with_recognition(stop_word = '+', lang_list = ['en','ru','fa'], ends=['US','RU','IR'], lang_repeat_step = 4, stop_repeat_step = 5):
    
    counter = 1
    
    print('Welcome! Write "',end='')
    print(str(stop_word),end='')    
    print('" to stop logging')
    
    print('Output lang list: ',end='')
    
    choosen_list = [f'{number+1}) {lang}' for number, lang in zip(range(len(lang_list)),lang_list)]
    
    langs_string = ' '+' '.join(choosen_list)+' '
    
    print(langs_string)  
    
    print('Choose a number of lang to start talking')
    
    
    while True:
        text = input(f'({counter})--> ')
        if text == stop_word:
            break
        
        if text.isdigit():
            try:
                number = int(text)-1
                text = speech_to_text_from_micro(f'{lang_list[number]}-{ends[number]}')
                print('You said:',end='')
                print(' '+text)
            except Exception as e:
                print('Something wrong...')
                print(e)

        log_text(text, lang_list = lang_list)
             
        counter+=1
        
        if counter%lang_repeat_step == 0:
            print("don't forget lang numbers:",end='')
            print(langs_string)
        
        if counter%stop_repeat_step == 0:
            print("to stop it write",end=' ')
            print(stop_word)


if __name__ == '__main__':
    do_log_with_recognition()